"""Roadmap alignment: classifies each HCP request against the product
roadmap and writes the result back onto the request in-place.

Single source of truth for the prompt is
`analysis/roadmap_comparison/prompt.md` (authored by Anna McDermott). This
service reuses that prompt verbatim, plus a small batching addendum so
multiple requests can be classified in one Claude call.

The output schema mirrors Anna's CLI exactly (per-request):

    classification:        "covered" | "partial" | "gap"
    gap_category:          content-gap | channel-gap | data-gap |
                           workflow-gap | cross-product-gap | null
    confidence:            "high" | "medium" | "low"
    matched_roadmap_keys:  ["PROD-NNN", ...]
    reasoning:             "1-2 sentences"

Bucketing is intentionally untouched. Failures are non-fatal: if alignment
falls over, the dashboard still gets buckets, just without alignment data.
"""
from __future__ import annotations

import json
import logging
import os
import re
from threading import Lock
from typing import Dict, List, Optional

from anthropic import Anthropic, APIError

from models.schemas import BucketsResponse, HCPRequest, RoadmapItem
from services.roadmap import roadmap_payload_for_prompt

logger = logging.getLogger(__name__)


_PROMPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "analysis",
    "roadmap_comparison",
    "prompt.md",
)


_BATCH_ADDENDUM = """

---

## Batch mode

You are processing MULTIPLE HCP unmet needs in a single call, not one. Each
input request has a stable `request_id` you must echo back unchanged. Apply
the classification rules above independently to each request and return a
single JSON object with the shape:

```json
{
  "alignments": [
    {
      "request_id": "string (echo verbatim)",
      "classification": "covered | partial | gap",
      "gap_category": "content-gap | channel-gap | data-gap | workflow-gap | cross-product-gap | null",
      "confidence": "high | medium | low",
      "matched_roadmap_keys": ["PROD-NNN", ...],
      "reasoning": "string (1-2 sentences)"
    }
  ]
}
```

Every input request_id MUST appear exactly once in the `alignments` array.
Use only roadmap keys present in the candidate set provided below. Do not
emit markdown code fences. Your response must start with `{` and end with `}`.
"""


_VALID_CLASSIFICATIONS = {"covered", "partial", "gap"}
_VALID_CONFIDENCES = {"high", "medium", "low"}
_VALID_GAP_CATEGORIES = {
    "content-gap",
    "channel-gap",
    "data-gap",
    "workflow-gap",
    "cross-product-gap",
}


class AlignmentError(Exception):
    """Raised when alignment cannot complete. Callers should treat this as
    non-fatal and continue without alignment data."""


_PROMPT_LOCK = Lock()
_PROMPT_CACHE: Optional[str] = None


def _load_prompt() -> str:
    """Read prompt.md once, then cache it. The CLI and the live service
    share this file so prompts cannot drift out of sync."""
    global _PROMPT_CACHE
    with _PROMPT_LOCK:
        if _PROMPT_CACHE is not None:
            return _PROMPT_CACHE
        if not os.path.exists(_PROMPT_PATH):
            raise AlignmentError(
                f"Alignment prompt not found at {_PROMPT_PATH}. "
                "Make sure the analysis/roadmap_comparison module is checked in."
            )
        with open(_PROMPT_PATH, "r", encoding="utf-8") as fh:
            _PROMPT_CACHE = fh.read() + _BATCH_ADDENDUM
        return _PROMPT_CACHE


def reset_prompt_cache() -> None:
    """Test/reload helper."""
    global _PROMPT_CACHE
    with _PROMPT_LOCK:
        _PROMPT_CACHE = None


# Compact JSON serializer — eliminates whitespace overhead, ~15% fewer tokens
# on the wire. Matters most for the cached roadmap block.
def _compact(payload) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def _request_payload(req: HCPRequest) -> dict:
    """Trim the HCPRequest down to the fields the prompt needs."""
    return {
        "request_id": req.request_id,
        "hcp_response": req.hcp_response,
        "first_name": req.first_name,
        "last_name": req.last_name,
        "slack_channel": req.slack_channel,
        "pulse": req.pulse,
    }


def _build_cacheable_block(roadmap_items: List[RoadmapItem]) -> str:
    """Static portion of the prompt — roadmap candidate set. Identical
    across calls so we mark it cache_control=ephemeral."""
    payload = roadmap_payload_for_prompt(roadmap_items)
    return (
        f"## Roadmap candidate set ({len(payload)} items)\n\n"
        "These are the ONLY valid roadmap keys you may emit:\n\n"
        f"```json\n{_compact(payload)}\n```"
    )


def _build_user_message(requests: List[HCPRequest]) -> str:
    """Dynamic per-call portion."""
    payload = [_request_payload(r) for r in requests if r.request_id]
    return (
        f"## HCP unmet needs to classify ({len(payload)} requests)\n\n"
        f"```json\n{_compact(payload)}\n```\n\n"
        "Classify each request against the roadmap and return the batch JSON "
        "object as specified."
    )


def _extract_json(text: str) -> dict:
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = re.sub(r"^```(?:json)?\s*", "", candidate)
        if candidate.endswith("```"):
            candidate = candidate[:-3]
        candidate = candidate.strip()
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        first = candidate.find("{")
        last = candidate.rfind("}")
        if first == -1 or last == -1 or last <= first:
            raise
        return json.loads(candidate[first : last + 1])


def _normalize_classification(value) -> str:
    val = str(value or "").strip().lower()
    return val if val in _VALID_CLASSIFICATIONS else ""


def _normalize_confidence(value) -> str:
    val = str(value or "").strip().lower()
    return val if val in _VALID_CONFIDENCES else ""


def _normalize_gap_category(value, classification: str) -> str:
    if classification == "covered":
        # Anna's contract: gap_category MUST be null when covered.
        return ""
    val = str(value or "").strip().lower()
    return val if val in _VALID_GAP_CATEGORIES else ""


def classify_requests(
    requests: List[HCPRequest],
    roadmap_items: List[RoadmapItem],
    *,
    api_key: str,
    model: str,
) -> Dict[str, dict]:
    """Run the classification call and return a mapping of
    request_id → {classification, gap_category, confidence, matched_keys, reasoning}.

    This is the SHARED kernel used by both /api/buckets (live dashboard) and
    Anna's analysis CLI. It does not mutate input objects.
    """
    if not roadmap_items:
        logger.info("[alignment] No roadmap items loaded — skipping classification")
        return {}
    if not api_key:
        raise AlignmentError("ANTHROPIC_API_KEY is not configured")

    candidate_requests = [r for r in requests if r.request_id]
    if not candidate_requests:
        return {}

    user_message = _build_user_message(candidate_requests)
    cacheable_block = _build_cacheable_block(roadmap_items)
    base_prompt = _load_prompt()

    logger.info(
        "[alignment] Classifying %d requests against %d roadmap items",
        len(candidate_requests),
        len(roadmap_items),
    )

    client = Anthropic(api_key=api_key)
    try:
        message = client.messages.create(
            model=model,
            max_tokens=8192,
            system=[
                {"type": "text", "text": base_prompt},
                {
                    "type": "text",
                    "text": cacheable_block,
                    "cache_control": {"type": "ephemeral"},
                },
            ],
            messages=[{"role": "user", "content": user_message}],
        )
    except APIError as exc:
        raise AlignmentError(f"Claude API error during alignment: {exc}") from exc
    except Exception as exc:  # noqa: BLE001
        raise AlignmentError(f"Unexpected alignment error: {exc}") from exc

    usage = getattr(message, "usage", None)
    if usage is not None:
        logger.info(
            "[alignment] tokens — input=%s output=%s cache_write=%s cache_read=%s",
            getattr(usage, "input_tokens", "?"),
            getattr(usage, "output_tokens", "?"),
            getattr(usage, "cache_creation_input_tokens", 0) or 0,
            getattr(usage, "cache_read_input_tokens", 0) or 0,
        )

    text_chunks = [
        block.text for block in message.content if getattr(block, "type", "") == "text"
    ]
    raw_text = "".join(text_chunks)

    try:
        parsed = _extract_json(raw_text)
    except json.JSONDecodeError as exc:
        raise AlignmentError(
            f"Failed to parse alignment JSON. Raw head: {raw_text[:500]!r}"
        ) from exc

    valid_keys = {item.key for item in roadmap_items}
    result: Dict[str, dict] = {}

    for raw in parsed.get("alignments") or []:
        if not isinstance(raw, dict):
            continue
        rid = str(raw.get("request_id") or "").strip()
        if not rid:
            continue

        classification = _normalize_classification(raw.get("classification"))
        confidence = _normalize_confidence(raw.get("confidence"))
        gap_category = _normalize_gap_category(raw.get("gap_category"), classification)

        keys_in = raw.get("matched_roadmap_keys") or []
        matched_keys: List[str] = []
        for k in keys_in:
            ks = str(k or "").strip()
            if ks in valid_keys:
                matched_keys.append(ks)
            elif ks:
                logger.warning(
                    "[alignment] Claude returned unknown roadmap key=%s for "
                    "request_id=%s; dropping",
                    ks,
                    rid,
                )

        # Anna's contract: matched_roadmap_keys must be empty when gap.
        if classification == "gap":
            matched_keys = []

        result[rid] = {
            "classification": classification or "gap",
            "gap_category": gap_category,
            "confidence": confidence or "low",
            "matched_roadmap_keys": matched_keys,
            "reasoning": str(raw.get("reasoning") or "").strip(),
        }

    return result


def align_requests(
    response: BucketsResponse,
    roadmap_items: List[RoadmapItem],
    *,
    api_key: str,
    model: str,
) -> Dict[str, int]:
    """Run alignment, mutating `response.buckets[*].requests[*]` in-place to
    attach classification + alignment metadata.

    Returns a small stats dict for logging:
        {"covered": N, "partial": M, "gap": K, "skipped": S}
    """
    by_id: Dict[str, HCPRequest] = {}
    for bucket in response.buckets:
        for req in bucket.requests:
            if req.request_id and req.request_id not in by_id:
                by_id[req.request_id] = req

    if not by_id:
        logger.info("[alignment] No requests with request_ids — skipping")
        return {"covered": 0, "partial": 0, "gap": 0, "skipped": 0}

    classifications = classify_requests(
        list(by_id.values()),
        roadmap_items,
        api_key=api_key,
        model=model,
    )

    by_key: Dict[str, RoadmapItem] = {item.key: item for item in roadmap_items}
    stats = {"covered": 0, "partial": 0, "gap": 0, "skipped": 0}

    for rid, req in by_id.items():
        clf = classifications.get(rid)
        if clf is None:
            # Claude silently dropped this request — surface as gap so the
            # UI doesn't show stale/empty alignment.
            req.roadmap_classification = "gap"
            req.gap_category = ""
            req.confidence = "low"
            req.roadmap_reasoning = (
                "Alignment service did not return a classification for this "
                "request; surfaced as a gap pending manual review."
            )
            req.roadmap_alignments = []
            req.unaligned = True
            stats["skipped"] += 1
            logger.warning(
                "[alignment] No classification for request_id=%s; marking gap", rid
            )
            continue

        classification = clf["classification"]
        req.roadmap_classification = classification
        req.gap_category = clf["gap_category"]
        req.confidence = clf["confidence"]
        req.roadmap_reasoning = clf["reasoning"]

        attached: List[RoadmapItem] = []
        for key in clf["matched_roadmap_keys"]:
            base = by_key.get(key)
            if base is None:
                continue
            attached.append(
                RoadmapItem(
                    key=base.key,
                    title=base.title,
                    url=base.url,
                    initiative=base.initiative,
                    status=base.status,
                    rationale="",  # rationale is per-request, lives in roadmap_reasoning
                )
            )
        req.roadmap_alignments = attached
        req.unaligned = classification == "gap"

        if classification in stats:
            stats[classification] += 1

    logger.info(
        "[alignment] Done: covered=%d partial=%d gap=%d skipped=%d",
        stats["covered"],
        stats["partial"],
        stats["gap"],
        stats["skipped"],
    )
    return stats
