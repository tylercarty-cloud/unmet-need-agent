"""Roadmap loader: parses `backend/roadmap.md` into compact `RoadmapItem`s
that we can hand to Claude alongside HCP requests for alignment.

The full markdown (~9k lines / 385 KB) is too big to feed Claude on every
call, so we extract just the fields we need for matching:
    key, title, url, initiative, status, summary

The parser is intentionally lenient: anything it can't extract gets a sane
default rather than raising — bad data in the markdown should never break
the bucketing pipeline.
"""
from __future__ import annotations

import logging
import os
import re
from threading import Lock
from typing import List, Optional, Tuple

from models.schemas import RoadmapItem

logger = logging.getLogger(__name__)


_HEADING_RE = re.compile(
    r"^###\s+\[(?P<key>[A-Z]+-\d+)\]\((?P<url>https?://[^)]+)\)\s+[—-]\s+(?P<title>.+?)\s*$"
)
_STATUS_HEADING_RE = re.compile(r"^##\s+(?P<status>[^()]+?)(?:\s+\(\d+\))?\s*$")
_INITIATIVE_RE = re.compile(r"^-\s+\*\*Initiative:\*\*\s*(?P<value>.+?)\s*$")
_OVERVIEW_HEADING_RE = re.compile(r"^####\s+\*?Overview\*?\s*$", re.IGNORECASE)
_HEADING_ANY_RE = re.compile(r"^#{1,6}\s")

_SUMMARY_MAX_CHARS = 200


def _normalize_summary(text: str) -> str:
    """Collapse whitespace, strip markdown noise, and truncate."""
    text = re.sub(r"\s+", " ", text).strip()
    # Remove leftover markdown emphasis markers — they only add noise to the
    # alignment prompt.
    text = text.replace("**", "").replace("__", "")
    if len(text) > _SUMMARY_MAX_CHARS:
        text = text[: _SUMMARY_MAX_CHARS - 1].rstrip() + "…"
    return text


def _extract_summary(body_lines: List[str]) -> str:
    """Pick a useful 1-3 sentence summary from a roadmap entry's body.

    Priority:
      1. First non-empty paragraph under an "Overview" heading.
      2. First non-empty paragraph after the **Description** marker.
      3. First non-empty bullet anywhere in the body.
    """
    in_overview = False
    overview_buf: List[str] = []
    description_buf: List[str] = []
    saw_description_marker = False
    first_bullet: Optional[str] = None

    for raw in body_lines:
        line = raw.rstrip()

        if _OVERVIEW_HEADING_RE.match(line):
            in_overview = True
            continue
        # Any other sub-heading after entering overview ends it.
        if in_overview and _HEADING_ANY_RE.match(line):
            in_overview = False
        if line.strip() == "**Description**":
            saw_description_marker = True
            continue

        stripped = line.strip()
        if not stripped:
            # Paragraph break — if we already collected something for the
            # current candidate buffer, that's our paragraph.
            if in_overview and overview_buf:
                break
            continue

        if in_overview:
            overview_buf.append(stripped.lstrip("- ").lstrip("* "))
            continue
        if saw_description_marker and not stripped.startswith("####"):
            description_buf.append(stripped.lstrip("- ").lstrip("* "))
        if first_bullet is None and stripped.startswith(("- ", "* ")):
            first_bullet = stripped[2:]

    for candidate in (overview_buf, description_buf):
        if candidate:
            return _normalize_summary(" ".join(candidate))
    if first_bullet:
        return _normalize_summary(first_bullet)
    return ""


def _flush_item(
    *,
    key: str,
    title: str,
    url: str,
    initiative: str,
    status: str,
    body: List[str],  # unused at construction time; summary cached separately
) -> RoadmapItem:
    del body  # quiet unused-arg lints; summary is captured via _SUMMARY_BY_KEY
    return RoadmapItem(
        key=key,
        title=title.strip(),
        url=url,
        initiative=initiative.strip(),
        status=status.strip(),
    )


def parse_roadmap_markdown(markdown: str) -> List[RoadmapItem]:
    """Parse the contents of `roadmap.md` into RoadmapItems."""
    items: List[RoadmapItem] = []
    summaries: List[str] = []  # parallel to items, used to attach via dict later
    current_status = ""
    cur_key: Optional[str] = None
    cur_title = ""
    cur_url = ""
    cur_initiative = ""
    cur_body: List[str] = []

    def flush() -> None:
        if cur_key is None:
            return
        item = _flush_item(
            key=cur_key,
            title=cur_title,
            url=cur_url,
            initiative=cur_initiative,
            status=current_status,
            body=cur_body,
        )
        items.append(item)
        summaries.append(_extract_summary(cur_body))

    for line in markdown.splitlines():
        # Status section heading (## Now / ## Parking lot / etc.)
        m_status = _STATUS_HEADING_RE.match(line)
        if m_status and not line.startswith("### "):
            heading = m_status.group("status").strip()
            # Skip the housekeeping ## sections.
            if heading.lower() not in {"overview", "ideas by status"}:
                current_status = heading
            continue

        # Idea heading (### [PROD-NNN](url) — title)
        m_idea = _HEADING_RE.match(line)
        if m_idea:
            flush()
            cur_key = m_idea.group("key")
            cur_url = m_idea.group("url")
            cur_title = m_idea.group("title")
            cur_initiative = ""
            cur_body = []
            continue

        if cur_key is None:
            continue

        # Initiative metadata bullet (only the first match wins)
        if not cur_initiative:
            m_init = _INITIATIVE_RE.match(line)
            if m_init:
                cur_initiative = m_init.group("value")
                continue

        cur_body.append(line)

    flush()

    # Attach the parallel summary list to each item via a private cache field.
    # We add summary as part of the prompt payload, not the API response, so
    # we keep it on a sidecar dict instead of the schema.
    for item, summary in zip(items, summaries):
        _SUMMARY_BY_KEY[item.key] = summary

    return items


# Module-level cache so the roadmap is loaded once per process.
_ROADMAP_LOCK = Lock()
_ROADMAP_ITEMS: Optional[List[RoadmapItem]] = None
_SUMMARY_BY_KEY: dict[str, str] = {}
_ROADMAP_ERROR: Optional[str] = None


def load_roadmap(path: str) -> List[RoadmapItem]:
    """Load the roadmap from disk, caching the result. Returns [] if the file
    is missing or unreadable (alignment will simply be skipped)."""
    global _ROADMAP_ITEMS, _ROADMAP_ERROR
    with _ROADMAP_LOCK:
        if _ROADMAP_ITEMS is not None:
            return _ROADMAP_ITEMS

        if not path or not os.path.exists(path):
            _ROADMAP_ERROR = f"Roadmap file not found at {path}"
            logger.warning("[roadmap] %s — alignment will be skipped", _ROADMAP_ERROR)
            _ROADMAP_ITEMS = []
            return _ROADMAP_ITEMS

        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as exc:
            _ROADMAP_ERROR = f"Failed to read roadmap at {path}: {exc}"
            logger.error("[roadmap] %s", _ROADMAP_ERROR)
            _ROADMAP_ITEMS = []
            return _ROADMAP_ITEMS

        items = parse_roadmap_markdown(raw)
        _ROADMAP_ITEMS = items
        _ROADMAP_ERROR = None
        logger.info(
            "[roadmap] Parsed %d items from %s (initiatives: %d)",
            len(items),
            path,
            len({i.initiative for i in items if i.initiative}),
        )
        return items


def get_summary(key: str) -> str:
    return _SUMMARY_BY_KEY.get(key, "")


def get_roadmap_error() -> Optional[str]:
    return _ROADMAP_ERROR


def reset_cache() -> None:
    """Test/reload helper — clears the in-memory cache."""
    global _ROADMAP_ITEMS, _ROADMAP_ERROR
    with _ROADMAP_LOCK:
        _ROADMAP_ITEMS = None
        _ROADMAP_ERROR = None
        _SUMMARY_BY_KEY.clear()


def roadmap_payload_for_prompt(items: List[RoadmapItem]) -> List[dict]:
    """Compact dict form fed to Claude in the alignment prompt.
    Strips fields that aren't useful for matching (rationale is empty here)."""
    return [
        {
            "key": i.key,
            "title": i.title,
            "initiative": i.initiative,
            "status": i.status,
            "summary": get_summary(i.key),
        }
        for i in items
    ]
