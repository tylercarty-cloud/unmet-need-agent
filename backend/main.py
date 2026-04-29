"""FastAPI entry point for the HCP Unmet Needs dashboard."""
from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Optional, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import get_settings
from models.schemas import BucketsResponse, HealthResponse
from services.alignment import AlignmentError, align_requests
from services.claude import ClaudeError, bucketize_requests
from services.diagnostics import collect_diagnostics
from services.roadmap import get_roadmap_error, load_roadmap
from services.sheets import SheetsError, fetch_hcp_requests
from services.slack import SlackError, fetch_slack_requests
from services.slack_publisher import publish_buckets

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("hcp_unmet_need_agent")

settings = get_settings()


def _mask(value: str, keep: int = 4) -> str:
    if not value:
        return "<unset>"
    if len(value) <= keep:
        return "*" * len(value)
    return value[:keep] + "…" + "*" * max(0, len(value) - keep - 1)


def _log_startup_config() -> None:
    """Loud, visible summary of which integrations are configured. Helps
    diagnose 'why didn't my new Slack message show up' in one glance."""
    sheets_ok = bool(settings.google_sheets_id)
    anthropic_ok = bool(settings.anthropic_api_key)
    slack_token_ok = bool(settings.slack_bot_token)
    slack_channel_ok = bool(settings.slack_channel_id)
    slack_token_format_ok = settings.slack_bot_token.startswith(("xoxb-", "xoxp-"))

    logger.info("=" * 60)
    logger.info("HCP Unmet Needs API — startup configuration")
    logger.info("=" * 60)
    logger.info(
        "  Anthropic:  %s  (model=%s)",
        "OK" if anthropic_ok else "MISSING ANTHROPIC_API_KEY",
        settings.anthropic_model,
    )
    logger.info(
        "  Sheets:     %s  (id=%s, range=%s)",
        "OK" if sheets_ok else "MISSING GOOGLE_SHEETS_ID",
        _mask(settings.google_sheets_id, 6),
        settings.google_sheets_range,
    )
    if not slack_token_ok or not slack_channel_ok:
        logger.info(
            "  Slack:      DISABLED  (bot_token=%s, channel_id=%s)",
            "set" if slack_token_ok else "<unset>",
            settings.slack_channel_id or "<unset>",
        )
    elif not slack_token_format_ok:
        logger.warning(
            "  Slack:      MISCONFIGURED — token does not start with 'xoxb-' "
            "or 'xoxp-'. Got %s. Grab the *Bot User OAuth Token* from "
            "Slack app settings → OAuth & Permissions.",
            _mask(settings.slack_bot_token, 4),
        )
    else:
        logger.info(
            "  Slack:      OK  (channel=%s, token=%s, publish=%s)",
            settings.slack_channel_id,
            _mask(settings.slack_bot_token, 8),
            "on" if settings.slack_publish_enabled else "off",
        )
    logger.info(
        "  Cache TTL:  %ss   CORS: %s",
        settings.cache_ttl_seconds,
        ",".join(settings.cors_origins) or "*",
    )
    # Roadmap status is logged separately because loading happens below.
    logger.info("=" * 60)


_log_startup_config()


# Load roadmap once at startup so the first /api/buckets call doesn't pay
# the parse cost. Failures are logged but never block startup.
_roadmap_items = load_roadmap(settings.roadmap_path)
if _roadmap_items:
    logger.info(
        "  Roadmap:    OK  (path=%s, items=%d)",
        settings.roadmap_path,
        len(_roadmap_items),
    )
else:
    logger.warning(
        "  Roadmap:    UNAVAILABLE  (path=%s, error=%s) — alignment will be skipped",
        settings.roadmap_path,
        get_roadmap_error() or "no items parsed",
    )

app = FastAPI(title="HCP Unmet Needs API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


_cache: dict[str, Tuple[float, BucketsResponse]] = {}


def _cached_response() -> Optional[BucketsResponse]:
    if settings.cache_ttl_seconds <= 0:
        return None
    entry = _cache.get("buckets")
    if not entry:
        return None
    cached_at, payload = entry
    if (time.time() - cached_at) <= settings.cache_ttl_seconds:
        logger.info("Serving /api/buckets from cache")
        return payload
    return None


def _store_cache(payload: BucketsResponse) -> None:
    if settings.cache_ttl_seconds > 0:
        _cache["buckets"] = (time.time(), payload)


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", timestamp=datetime.now(timezone.utc))


@app.get("/api/diagnostics")
def diagnostics() -> dict:
    """Returns a JSON dump of integration health (Anthropic, Sheets, Slack)
    so the dashboard (or curl) can immediately see what's misconfigured."""
    return collect_diagnostics(settings)


@app.get("/api/buckets", response_model=BucketsResponse)
def get_buckets() -> BucketsResponse:
    cached = _cached_response()
    if cached is not None:
        return cached

    try:
        sheet_requests = fetch_hcp_requests(
            spreadsheet_id=settings.google_sheets_id,
            sheet_range=settings.google_sheets_range,
            credentials_path=settings.google_service_account_json,
        )
    except SheetsError as exc:
        logger.error("Sheets fetch failed: %s", exc)
        raise HTTPException(status_code=503, detail=f"Google Sheets error: {exc}")

    slack_requests = []
    if settings.slack_bot_token and settings.slack_channel_id:
        try:
            slack_requests = fetch_slack_requests(
                bot_token=settings.slack_bot_token,
                channel_id=settings.slack_channel_id,
                message_limit=settings.slack_message_limit,
            )
        except SlackError as exc:
            # Slack is an optional augmentation; log and continue with sheet data.
            logger.error("Slack fetch failed, continuing without Slack data: %s", exc)
    else:
        logger.info("Slack ingestion disabled (SLACK_BOT_TOKEN or SLACK_CHANNEL_ID not set)")

    requests = list(sheet_requests) + list(slack_requests)
    logger.info(
        "Sending %d requests to Claude for bucketing (sheet=%d, slack=%d)",
        len(requests),
        len(sheet_requests),
        len(slack_requests),
    )

    try:
        response = bucketize_requests(
            requests,
            api_key=settings.anthropic_api_key,
            model=settings.anthropic_model,
        )
    except ClaudeError as exc:
        message = str(exc)
        logger.error("Claude bucketing failed: %s", message)
        if "parse" in message.lower():
            raise HTTPException(status_code=500, detail=message)
        raise HTTPException(status_code=502, detail=message)

    if settings.alignment_enabled and _roadmap_items:
        try:
            align_requests(
                response,
                _roadmap_items,
                api_key=settings.anthropic_api_key,
                model=settings.anthropic_model,
            )
        except AlignmentError as exc:
            # Non-fatal: render buckets without alignment data.
            logger.error("Alignment step failed: %s", exc)

    if (
        settings.slack_publish_enabled
        and settings.slack_bot_token
        and settings.slack_channel_id
    ):
        try:
            publish_buckets(
                response,
                bot_token=settings.slack_bot_token,
                channel_id=settings.slack_channel_id,
                dashboard_url=settings.dashboard_url,
                state_path=settings.slack_publish_state_path,
            )
        except Exception as exc:  # noqa: BLE001 - publish must never fail the API
            logger.error("Slack publish step failed: %s", exc)

    _store_cache(response)
    return response


if __name__ == "__main__":
    import uvicorn

    # Watch .env in addition to *.py so config edits trigger a reload —
    # otherwise the running process keeps stale Settings until manual restart.
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_includes=["*.py", ".env"],
    )
