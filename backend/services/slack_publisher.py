"""Slack publisher: posts each newly-bucketed unmet need back to the Slack
channel and persists which request_ids have already been published so we
don't double-post on cache misses or restarts."""
from __future__ import annotations

import json
import logging
import os
import tempfile
import threading
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from models.schemas import Bucket, BucketsResponse, HCPRequest
from services.slack import _build_ssl_context  # reuse the certifi-backed context

logger = logging.getLogger(__name__)


# Marker stamped into Slack `metadata` so the agent (or future tooling) can
# unambiguously recognize its own posts on top of the bot_id/auth.test checks.
AGENT_EVENT_TYPE = "hcp_unmet_need_agent_post"


class SlackPublishError(Exception):
    """Raised on unrecoverable Slack publish failures."""


_state_lock = threading.Lock()


def _load_state(path: str) -> Dict[str, dict]:
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Could not read Slack publish state at %s: %s", path, exc)
        return {}
    return (data or {}).get("posted") or {}


def _save_state(path: str, posted: Dict[str, dict]) -> None:
    if not path:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    payload = {"version": 1, "posted": posted}
    # Atomic write: tmp file in same dir, then os.replace.
    fd, tmp_path = tempfile.mkstemp(
        prefix=".posted_", suffix=".json", dir=os.path.dirname(path) or "."
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        raise


def _full_name(req: HCPRequest) -> str:
    parts = [p for p in (req.first_name, req.last_name) if p]
    return " ".join(parts).strip()


def _format_blocks(
    *,
    bucket: Bucket,
    request: HCPRequest,
    dashboard_url: str,
) -> Tuple[str, List[dict]]:
    """Build (fallback_text, blocks) for a single unmet-need post."""
    name = _full_name(request) or "Unknown HCP"
    bucket_name = bucket.bucket_name or "Other"

    fallback = f"[{bucket_name}] {name}: {request.hcp_response}"

    header_text = f":pushpin: New Unmet Need — {bucket_name}"
    blocks: List[dict] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": header_text[:150], "emoji": True},
        }
    ]

    if bucket.description:
        blocks.append(
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f"_{bucket.description}_"}
                ],
            }
        )

    # Body: the actual HCP message. Slack section text caps at 3000 chars.
    body = request.hcp_response or "_(no message body)_"
    if len(body) > 2800:
        body = body[:2800].rstrip() + "…"
    blocks.append(
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f">>> {body}"},
        }
    )

    # Metadata grid: name / NPI / pulse / channel / date.
    fields: List[dict] = []

    def _add_field(label: str, value: str) -> None:
        if not value:
            return
        fields.append(
            {"type": "mrkdwn", "text": f"*{label}*\n{value}"}
        )

    _add_field("HCP", name)
    _add_field("NPI", request.npi)
    _add_field("Pulse", request.pulse)
    _add_field("Source channel", request.slack_channel)
    _add_field("Submitted", request.date_time or "")

    # Slack only allows up to 10 fields per section; we have at most 5 here.
    if fields:
        blocks.append({"type": "section", "fields": fields})

    # Action links: original Slack post (if any) + dashboard link.
    action_elements: List[dict] = []
    if request.slack_link:
        action_elements.append(
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Original Slack post"},
                "url": request.slack_link,
            }
        )
    if dashboard_url:
        action_elements.append(
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "View in dashboard"},
                "url": dashboard_url,
                "style": "primary",
            }
        )
    if action_elements:
        blocks.append({"type": "actions", "elements": action_elements})

    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"`request_id: {request.request_id or 'n/a'}`",
                }
            ],
        }
    )

    return fallback[:300], blocks


def _post_one(
    client: WebClient,
    *,
    channel_id: str,
    bucket: Bucket,
    request: HCPRequest,
    dashboard_url: str,
) -> Optional[str]:
    """Post a single unmet need; returns the resulting message ts on success."""
    fallback, blocks = _format_blocks(
        bucket=bucket, request=request, dashboard_url=dashboard_url
    )

    # If the request originated from this same Slack channel, post the
    # acknowledgement as a thread reply on the original message. Otherwise,
    # post a top-level message.
    thread_ts: Optional[str] = None
    if request.slack_ts and request.slack_link and f"/archives/{channel_id}/" in request.slack_link:
        thread_ts = request.slack_ts

    try:
        resp = client.chat_postMessage(
            channel=channel_id,
            text=fallback,
            blocks=blocks,
            thread_ts=thread_ts,
            unfurl_links=False,
            unfurl_media=False,
            metadata={
                "event_type": AGENT_EVENT_TYPE,
                "event_payload": {
                    "request_id": request.request_id,
                    "bucket_name": bucket.bucket_name,
                },
            },
        )
    except SlackApiError as exc:
        err = exc.response.get("error", "unknown")
        if err == "thread_not_found" and thread_ts:
            # Original message was deleted; retry as a top-level post.
            logger.warning(
                "Thread parent missing for %s; falling back to top-level post",
                request.request_id,
            )
            try:
                resp = client.chat_postMessage(
                    channel=channel_id,
                    text=fallback,
                    blocks=blocks,
                    unfurl_links=False,
                    unfurl_media=False,
                    metadata={
                        "event_type": AGENT_EVENT_TYPE,
                        "event_payload": {
                            "request_id": request.request_id,
                            "bucket_name": bucket.bucket_name,
                        },
                    },
                )
            except SlackApiError as exc2:
                logger.error(
                    "chat.postMessage failed for %s: %s",
                    request.request_id,
                    exc2.response.get("error"),
                )
                return None
        else:
            logger.error(
                "chat.postMessage failed for %s: %s", request.request_id, err
            )
            return None

    return resp.get("ts")


def publish_buckets(
    response: BucketsResponse,
    *,
    bot_token: str,
    channel_id: str,
    dashboard_url: str,
    state_path: str,
) -> Dict[str, int]:
    """Post any not-yet-published unmet needs from `response` to Slack.

    Returns a small stats dict for logging purposes:
        {"posted": N, "skipped": M, "failed": K}
    """
    if not bot_token or not channel_id:
        logger.info(
            "Slack publishing disabled (SLACK_BOT_TOKEN or SLACK_CHANNEL_ID not set)"
        )
        return {"posted": 0, "skipped": 0, "failed": 0}

    client = WebClient(token=bot_token, ssl=_build_ssl_context())

    with _state_lock:
        posted = _load_state(state_path)

        stats = {"posted": 0, "skipped": 0, "failed": 0}
        dirty = False

        for bucket in response.buckets:
            for request in bucket.requests:
                rid = request.request_id
                if not rid:
                    # No stable id — skip rather than risk duplicate posts.
                    logger.warning(
                        "Skipping publish for request without request_id: %r",
                        request.hcp_response[:80],
                    )
                    stats["skipped"] += 1
                    continue
                if rid in posted:
                    stats["skipped"] += 1
                    continue

                ts = _post_one(
                    client,
                    channel_id=channel_id,
                    bucket=bucket,
                    request=request,
                    dashboard_url=dashboard_url,
                )
                if ts is None:
                    stats["failed"] += 1
                    continue

                posted[rid] = {
                    "posted_at": datetime.now(timezone.utc).isoformat(),
                    "channel": channel_id,
                    "message_ts": ts,
                    "bucket_name": bucket.bucket_name,
                }
                stats["posted"] += 1
                dirty = True

        if dirty:
            try:
                _save_state(state_path, posted)
            except OSError as exc:
                logger.error("Failed to persist Slack publish state: %s", exc)

    logger.info(
        "Slack publish summary: posted=%d skipped=%d failed=%d",
        stats["posted"],
        stats["skipped"],
        stats["failed"],
    )
    return stats
