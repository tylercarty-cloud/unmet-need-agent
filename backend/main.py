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
from services.claude import ClaudeError, bucketize_requests
from services.sheets import SheetsError, fetch_hcp_requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("hcp_unmet_need_agent")

settings = get_settings()

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


@app.get("/api/buckets", response_model=BucketsResponse)
def get_buckets() -> BucketsResponse:
    cached = _cached_response()
    if cached is not None:
        return cached

    try:
        requests = fetch_hcp_requests(
            spreadsheet_id=settings.google_sheets_id,
            sheet_range=settings.google_sheets_range,
            credentials_path=settings.google_service_account_json,
        )
    except SheetsError as exc:
        logger.error("Sheets fetch failed: %s", exc)
        raise HTTPException(status_code=503, detail=f"Google Sheets error: {exc}")

    logger.info("Sending %d requests to Claude for bucketing", len(requests))

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

    _store_cache(response)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
