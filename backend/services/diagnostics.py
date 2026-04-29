"""Lightweight runtime diagnostics so config breakage is visible from the
dashboard, not just from `tail -f` on uvicorn."""
from __future__ import annotations

import logging
import os
from datetime import datetime, timezone
from typing import Any, Dict

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from services.roadmap import get_roadmap_error, load_roadmap
from services.slack import _build_ssl_context

logger = logging.getLogger(__name__)


def _mask(value: str, keep: int = 4) -> str:
    if not value:
        return ""
    if len(value) <= keep:
        return "*" * len(value)
    return value[:keep] + "…" + "*" * max(0, len(value) - keep - 1)


def collect_diagnostics(settings) -> Dict[str, Any]:
    """Run synchronous, side-effect-free probes against each integration and
    return a plain dict the frontend can render."""
    out: Dict[str, Any] = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "anthropic": _check_anthropic(settings),
        "sheets": _check_sheets(settings),
        "slack": _check_slack(settings),
        "roadmap": _check_roadmap(settings),
    }
    return out


def _check_roadmap(settings) -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "ok": False,
        "configured": settings.alignment_enabled,
        "path": settings.roadmap_path,
        "items": 0,
        "initiatives": 0,
        "error": None,
    }
    if not settings.alignment_enabled:
        info["error"] = "ALIGNMENT_ENABLED=false; roadmap matching is disabled"
        return info
    items = load_roadmap(settings.roadmap_path)
    info["items"] = len(items)
    info["initiatives"] = len({i.initiative for i in items if i.initiative})
    err = get_roadmap_error()
    if err:
        info["error"] = err
        return info
    if not items:
        info["error"] = "Roadmap parsed 0 items"
        return info
    info["ok"] = True
    return info


def _check_anthropic(settings) -> Dict[str, Any]:
    if not settings.anthropic_api_key:
        return {
            "ok": False,
            "configured": False,
            "error": "ANTHROPIC_API_KEY is not set",
            "model": settings.anthropic_model,
        }
    return {
        "ok": True,
        "configured": True,
        "error": None,
        "model": settings.anthropic_model,
        "key_preview": _mask(settings.anthropic_api_key, 10),
    }


def _check_sheets(settings) -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "ok": False,
        "configured": bool(settings.google_sheets_id),
        "spreadsheet_id_preview": _mask(settings.google_sheets_id, 6),
        "range": settings.google_sheets_range,
        "credentials_path": settings.google_service_account_json,
        "credentials_present": False,
        "error": None,
    }
    if not settings.google_sheets_id:
        info["error"] = "GOOGLE_SHEETS_ID is not set"
        return info
    info["credentials_present"] = os.path.exists(
        settings.google_service_account_json or ""
    )
    if not info["credentials_present"]:
        info["error"] = (
            f"Service account credentials not found at "
            f"{settings.google_service_account_json}"
        )
        return info
    info["ok"] = True
    return info


def _check_slack(settings) -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "ok": False,
        "configured": bool(settings.slack_bot_token and settings.slack_channel_id),
        "publish_enabled": bool(settings.slack_publish_enabled),
        "channel_id": settings.slack_channel_id,
        "channel_name": None,
        "bot_user_id": None,
        "team": None,
        "token_preview": _mask(settings.slack_bot_token, 8),
        "token_format_ok": settings.slack_bot_token.startswith(("xoxb-", "xoxp-")),
        "error": None,
    }

    if not settings.slack_bot_token:
        info["error"] = "SLACK_BOT_TOKEN is not set"
        return info
    if not settings.slack_channel_id:
        info["error"] = "SLACK_CHANNEL_ID is not set"
        return info
    if not info["token_format_ok"]:
        info["error"] = (
            "SLACK_BOT_TOKEN does not start with 'xoxb-' or 'xoxp-'. Use the "
            "Bot User OAuth Token from your Slack app → OAuth & Permissions."
        )
        return info

    client = WebClient(token=settings.slack_bot_token, ssl=_build_ssl_context())

    try:
        auth = client.auth_test()
        info["bot_user_id"] = auth.get("user_id")
        info["team"] = auth.get("team")
    except SlackApiError as exc:
        info["error"] = (
            f"auth.test failed: {exc.response.get('error')}. "
            "Token is invalid, revoked, or has insufficient scopes."
        )
        return info
    except Exception as exc:  # noqa: BLE001 - SSL/network
        info["error"] = (
            f"auth.test transport error: {exc}. If this is "
            "'CERTIFICATE_VERIFY_FAILED', see the README — Python on macOS "
            "needs certifi (now wired up automatically) or run "
            "'/Applications/Python 3.14/Install Certificates.command'."
        )
        return info

    try:
        ch = client.conversations_info(channel=settings.slack_channel_id)
        channel = ch.get("channel") or {}
        info["channel_name"] = channel.get("name")
        if not channel.get("is_member"):
            info["error"] = (
                f"Bot is not a member of #{channel.get('name') or settings.slack_channel_id}. "
                f"Run `/invite @your-app` in that channel."
            )
            return info
    except SlackApiError as exc:
        err = exc.response.get("error", "unknown")
        if err == "channel_not_found":
            info["error"] = (
                f"Channel {settings.slack_channel_id} not found or not "
                "visible to the bot."
            )
        elif err == "missing_scope":
            needed = exc.response.get("needed", "channels:read")
            info["error"] = (
                f"Slack token missing scope: {needed}. Re-install the app "
                "with channels:history, groups:history, channels:read, "
                "users:read, team:read, chat:write."
            )
        else:
            info["error"] = f"conversations.info failed: {err}"
        return info
    except Exception as exc:  # noqa: BLE001 - SSL/network
        info["error"] = f"conversations.info transport error: {exc}"
        return info

    info["ok"] = True
    return info
