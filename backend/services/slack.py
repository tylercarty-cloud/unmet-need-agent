"""Slack service: pulls top-level messages from a channel and normalizes them
into HCPRequest objects so they can flow through the same bucketing pipeline
as Google Sheet rows."""
from __future__ import annotations

import logging
import re
import ssl
from datetime import datetime, timezone
from typing import Dict, List, Optional

import certifi
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from models.schemas import HCPRequest

logger = logging.getLogger(__name__)


def _build_ssl_context() -> ssl.SSLContext:
    """Slack SDK uses urllib under the hood, which on python.org macOS builds
    has no CA bundle configured. Force it to use certifi's bundle so HTTPS to
    slack.com verifies cleanly on every machine."""
    return ssl.create_default_context(cafile=certifi.where())


def _make_client(token: str) -> WebClient:
    return WebClient(token=token, ssl=_build_ssl_context())


class SlackError(Exception):
    """Raised when we cannot fetch or parse Slack channel messages."""


_USER_MENTION_RE = re.compile(r"<@([UW][A-Z0-9]+)(?:\|[^>]+)?>")
_LINK_RE = re.compile(r"<(https?://[^|>]+)(?:\|([^>]+))?>")
_CHANNEL_REF_RE = re.compile(r"<#[CG][A-Z0-9]+(?:\|([^>]+))?>")


def _format_ts(ts: str) -> str:
    """Convert a Slack `ts` (e.g. '1714512345.123456') to ISO-8601 UTC."""
    try:
        seconds = float(ts)
    except (TypeError, ValueError):
        return ""
    return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()


def _ts_to_permalink_fragment(ts: str) -> str:
    """Slack permalinks use the ts with the dot stripped, prefixed with `p`."""
    return "p" + ts.replace(".", "")


def _clean_text(text: str, user_names: Dict[str, str]) -> str:
    """Replace Slack-specific markup (user/channel mentions, links) with
    readable equivalents so the bucketing prompt sees plain prose."""
    if not text:
        return ""

    def _user_repl(match: re.Match) -> str:
        uid = match.group(1)
        name = user_names.get(uid)
        return f"@{name}" if name else f"@{uid}"

    def _link_repl(match: re.Match) -> str:
        url, label = match.group(1), match.group(2)
        return label if label else url

    def _channel_repl(match: re.Match) -> str:
        label = match.group(1)
        return f"#{label}" if label else "#channel"

    out = _USER_MENTION_RE.sub(_user_repl, text)
    out = _LINK_RE.sub(_link_repl, out)
    out = _CHANNEL_REF_RE.sub(_channel_repl, out)
    return out.strip()


def _split_name(profile: dict) -> tuple[str, str]:
    first = (profile.get("first_name") or "").strip()
    last = (profile.get("last_name") or "").strip()
    if first or last:
        return first, last

    real = (profile.get("real_name") or profile.get("display_name") or "").strip()
    if not real:
        return "", ""
    parts = real.split(None, 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1]


def _resolve_users(client: WebClient, user_ids: set[str]) -> Dict[str, dict]:
    """Look up Slack user profiles in bulk; tolerate partial failures."""
    profiles: Dict[str, dict] = {}
    for uid in user_ids:
        try:
            resp = client.users_info(user=uid)
        except SlackApiError as exc:
            logger.warning("users.info failed for %s: %s", uid, exc.response.get("error"))
            continue
        user = resp.get("user") or {}
        profile = user.get("profile") or {}
        profiles[uid] = {
            "real_name": user.get("real_name") or profile.get("real_name") or "",
            "display_name": profile.get("display_name") or "",
            "first_name": profile.get("first_name") or "",
            "last_name": profile.get("last_name") or "",
            "is_bot": bool(user.get("is_bot")),
        }
    return profiles


def _resolve_channel(client: WebClient, channel_id: str) -> tuple[str, str]:
    """Return (channel_name, workspace_domain) for permalink construction."""
    name = ""
    try:
        info = client.conversations_info(channel=channel_id)
        name = (info.get("channel") or {}).get("name") or ""
    except SlackApiError as exc:
        logger.warning("conversations.info failed: %s", exc.response.get("error"))

    domain = ""
    try:
        team = client.team_info()
        domain = (team.get("team") or {}).get("domain") or ""
    except SlackApiError as exc:
        logger.warning("team.info failed: %s", exc.response.get("error"))

    return name, domain


def _identify_self(client: WebClient) -> tuple[str, str]:
    """Get this bot's user_id and bot_id so we can confidently skip our own
    posts (defense in depth on top of the generic bot_id filter)."""
    try:
        resp = client.auth_test()
    except SlackApiError as exc:
        logger.warning("auth.test failed: %s", exc.response.get("error"))
        return "", ""
    except Exception as exc:  # noqa: BLE001 - SSL/network errors etc.
        # Re-raise as SlackError so the caller surfaces a friendly message
        # instead of an opaque urllib SSL traceback bubbling to the API layer.
        raise SlackError(f"Slack auth.test transport error: {exc}") from exc
    return resp.get("user_id") or "", resp.get("bot_id") or ""


def _fetch_history(
    client: WebClient,
    channel_id: str,
    limit: int,
) -> List[dict]:
    """Page through conversations.history until we have `limit` messages or
    there are no more to fetch."""
    collected: List[dict] = []
    cursor: Optional[str] = None
    page_size = min(200, max(1, limit))

    while len(collected) < limit:
        try:
            resp = client.conversations_history(
                channel=channel_id,
                limit=page_size,
                cursor=cursor,
            )
        except SlackApiError as exc:
            err = exc.response.get("error", "unknown")
            if err == "not_in_channel":
                raise SlackError(
                    f"Bot is not a member of channel {channel_id}. "
                    "Invite the Slack app to the channel and retry."
                ) from exc
            if err == "channel_not_found":
                raise SlackError(
                    f"Channel {channel_id} not found or not visible to the bot."
                ) from exc
            if err == "missing_scope":
                needed = exc.response.get("needed", "channels:history")
                raise SlackError(
                    f"Slack token missing scope: {needed}. Re-install the app "
                    "with channels:history, groups:history, users:read, and team:read."
                ) from exc
            raise SlackError(f"Slack API error: {err}") from exc
        except Exception as exc:  # noqa: BLE001 - SSL/network failures
            raise SlackError(
                f"Slack conversations.history transport error: {exc}"
            ) from exc

        messages = resp.get("messages") or []
        collected.extend(messages)

        if not resp.get("has_more"):
            break
        cursor = (resp.get("response_metadata") or {}).get("next_cursor")
        if not cursor:
            break

    return collected[:limit]


def fetch_slack_requests(
    *,
    bot_token: str,
    channel_id: str,
    message_limit: int = 1000,
) -> List[HCPRequest]:
    """Pull top-level (non-thread-reply, non-bot) messages from `channel_id`
    and shape them into HCPRequest objects."""
    if not bot_token:
        raise SlackError("SLACK_BOT_TOKEN is not configured")
    if not channel_id:
        raise SlackError("SLACK_CHANNEL_ID is not configured")
    if not bot_token.startswith(("xoxb-", "xoxp-")):
        raise SlackError(
            "SLACK_BOT_TOKEN does not look like a Slack OAuth token "
            "(expected to start with 'xoxb-' or 'xoxp-'). Use the Bot User "
            "OAuth Token from your Slack app's OAuth & Permissions page."
        )

    logger.info(
        "[slack] Fetching from channel=%s limit=%d", channel_id, message_limit
    )
    client = _make_client(bot_token)

    self_user_id, self_bot_id = _identify_self(client)
    logger.info(
        "[slack] auth.test resolved: user_id=%s bot_id=%s",
        self_user_id or "<none>",
        self_bot_id or "<none>",
    )

    raw_messages = _fetch_history(client, channel_id, limit=message_limit)
    if not raw_messages:
        logger.warning(
            "[slack] conversations.history returned 0 messages from %s. "
            "Verify the bot was invited to the channel and that the channel ID is correct.",
            channel_id,
        )
        return []
    logger.info("[slack] conversations.history returned %d raw messages", len(raw_messages))

    # Filter to top-level human posts. Slack thread replies have `thread_ts`
    # set to a value other than their own `ts`. We also drop:
    #   - any message authored by THIS bot (defense against the publish loop)
    #   - any other bot/system posts (they aren't HCP feedback)
    human_messages: List[dict] = []
    drop_counts: Dict[str, int] = {
        "self_user": 0,
        "self_bot": 0,
        "subtype": 0,
        "other_bot": 0,
        "thread_reply": 0,
        "empty_text": 0,
    }
    for msg in raw_messages:
        if self_user_id and msg.get("user") == self_user_id:
            drop_counts["self_user"] += 1
            continue
        if self_bot_id and msg.get("bot_id") == self_bot_id:
            drop_counts["self_bot"] += 1
            continue
        if msg.get("subtype"):
            drop_counts["subtype"] += 1
            continue
        if msg.get("bot_id"):
            drop_counts["other_bot"] += 1
            continue
        thread_ts = msg.get("thread_ts")
        if thread_ts and thread_ts != msg.get("ts"):
            drop_counts["thread_reply"] += 1
            continue
        if not (msg.get("text") or "").strip():
            drop_counts["empty_text"] += 1
            continue
        human_messages.append(msg)

    logger.info(
        "[slack] Filter pass: kept=%d dropped=%s",
        len(human_messages),
        {k: v for k, v in drop_counts.items() if v},
    )

    user_ids = {m.get("user") for m in human_messages if m.get("user")}
    # Also resolve users referenced in mentions so we can render @names.
    for msg in human_messages:
        for match in _USER_MENTION_RE.finditer(msg.get("text") or ""):
            user_ids.add(match.group(1))

    profiles = _resolve_users(client, user_ids) if user_ids else {}
    channel_name, workspace_domain = _resolve_channel(client, channel_id)

    user_names = {
        uid: (
            (p.get("real_name") or p.get("display_name") or "").strip()
            or uid
        )
        for uid, p in profiles.items()
    }

    requests: List[HCPRequest] = []
    for msg in human_messages:
        author_id = msg.get("user") or ""
        profile = profiles.get(author_id) or {}
        if profile.get("is_bot"):
            continue

        first, last = _split_name(profile)
        ts = msg.get("ts") or ""

        permalink = ""
        if workspace_domain and ts:
            permalink = (
                f"https://{workspace_domain}.slack.com/archives/"
                f"{channel_id}/{_ts_to_permalink_fragment(ts)}"
            )

        record = HCPRequest(
            hcp_response=_clean_text(msg.get("text") or "", user_names),
            first_name=first,
            last_name=last,
            npi="",
            date_time=_format_ts(ts),
            slack_link=permalink,
            slack_channel=channel_name or channel_id,
            pulse="",
            request_id=f"slack:{channel_id}:{ts}",
            slack_ts=ts,
        )
        if record.hcp_response:
            requests.append(record)

    logger.info(
        "Fetched %d Slack messages from channel %s (%s)",
        len(requests),
        channel_name or channel_id,
        channel_id,
    )
    return requests
