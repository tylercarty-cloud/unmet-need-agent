"""Claude service: bucketizes HCP feedback into thematic groupings."""
from __future__ import annotations

import json
import logging
import re
from datetime import datetime, timezone
from typing import List

from anthropic import Anthropic, APIError

from models.schemas import Bucket, BucketsResponse, HCPRequest

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are analyzing messages from healthcare professionals (HCPs) that "
    "represent unmet needs — requests for which Impiricus does not currently "
    "have an aligned product. Your job is to identify natural thematic "
    "groupings in these messages and bucket them accordingly.\n\n"
    "Rules:\n"
    "- Identify buckets dynamically based on shared intent or topic (e.g., "
    "\"Rep Requests\", \"CME Content Needs\", \"Patient Resource Requests\")\n"
    "- Each request must be assigned to exactly one bucket (pick the best fit)\n"
    "- Bucket names should be concise (2-4 words), title-cased, and "
    "descriptive of the underlying need\n"
    "- Preserve ALL original metadata for each request in the output, "
    "including the opaque `request_id` and `slack_ts` fields — copy them "
    "through verbatim\n"
    "- Aim for 4-12 buckets depending on data volume — don't over-fragment "
    "or over-consolidate\n"
    "- If a request doesn't fit a clear theme, place it in an \"Other\" "
    "bucket\n\n"
    "Return ONLY valid JSON matching the specified schema. No preamble, no "
    "markdown code fences."
)

JSON_SCHEMA_HINT = """{
  "buckets": [
    {
      "bucket_name": "string (2-4 words, Title Case)",
      "description": "string (one short sentence)",
      "count": 0,
      "requests": [
        {
          "hcp_response": "string",
          "first_name": "string",
          "last_name": "string",
          "npi": "string",
          "date_time": "string",
          "slack_link": "string",
          "slack_channel": "string",
          "pulse": "string",
          "request_id": "string (copy verbatim from input)",
          "slack_ts": "string (copy verbatim from input)"
        }
      ]
    }
  ]
}"""


class ClaudeError(Exception):
    """Raised when Claude cannot return a usable response."""


def _build_user_message(requests: List[HCPRequest]) -> str:
    payload = [r.model_dump() for r in requests]
    return (
        f"Here is the JSON schema you must follow:\n```\n{JSON_SCHEMA_HINT}\n```\n\n"
        f"Here are {len(payload)} HCP messages to bucket:\n"
        f"```json\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n```\n\n"
        "Respond with ONLY the JSON object that matches the schema above. "
        "Do not include any preamble, explanation, or markdown code fences. "
        "Your entire response must start with `{` and end with `}`."
    )


def _extract_json(text: str) -> dict:
    """Best-effort extraction of a JSON object from a model response."""
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


def _coerce_response(parsed: dict, originals: List[HCPRequest]) -> BucketsResponse:
    raw_buckets = parsed.get("buckets") or []
    buckets: List[Bucket] = []

    # Build a lookup of originals by request_id and by content fingerprint so
    # we can restore request_id/slack_ts even if Claude drops them.
    by_id: dict[str, HCPRequest] = {o.request_id: o for o in originals if o.request_id}
    by_fingerprint: dict[str, HCPRequest] = {
        f"{o.hcp_response}|{o.date_time or ''}|{o.first_name}|{o.last_name}|{o.npi}": o
        for o in originals
    }

    for raw in raw_buckets:
        if not isinstance(raw, dict):
            continue
        requests_in = raw.get("requests") or []
        coerced_requests: List[HCPRequest] = []
        for r in requests_in:
            if not isinstance(r, dict):
                continue
            try:
                coerced = HCPRequest(**r)
            except Exception as exc:  # noqa: BLE001
                logger.warning("Dropping malformed bucketed request: %s", exc)
                continue

            original = by_id.get(coerced.request_id) if coerced.request_id else None
            if original is None:
                fp = (
                    f"{coerced.hcp_response}|{coerced.date_time or ''}|"
                    f"{coerced.first_name}|{coerced.last_name}|{coerced.npi}"
                )
                original = by_fingerprint.get(fp)
            if original is not None:
                if not coerced.request_id:
                    coerced.request_id = original.request_id
                if not coerced.slack_ts:
                    coerced.slack_ts = original.slack_ts

            coerced_requests.append(coerced)

        bucket = Bucket(
            bucket_name=str(raw.get("bucket_name") or "Other").strip() or "Other",
            description=str(raw.get("description") or "").strip(),
            count=len(coerced_requests),
            requests=coerced_requests,
        )
        buckets.append(bucket)

    total = sum(b.count for b in buckets)

    if total == 0 and originals:
        logger.warning(
            "Claude returned zero bucketed requests; falling back to single 'Other' bucket"
        )
        buckets = [
            Bucket(
                bucket_name="Other",
                description="Unclassified requests",
                count=len(originals),
                requests=list(originals),
            )
        ]
        total = len(originals)

    return BucketsResponse(
        buckets=buckets,
        total_requests=total,
        analysis_timestamp=datetime.now(timezone.utc),
    )


def bucketize_requests(
    requests: List[HCPRequest],
    *,
    api_key: str,
    model: str,
    max_retries: int = 1,
) -> BucketsResponse:
    """Send HCP requests to Claude and return structured buckets."""
    if not api_key:
        raise ClaudeError("ANTHROPIC_API_KEY is not configured")

    if not requests:
        return BucketsResponse(
            buckets=[],
            total_requests=0,
            analysis_timestamp=datetime.now(timezone.utc),
        )

    client = Anthropic(api_key=api_key)
    user_message = _build_user_message(requests)

    last_raw_text = ""
    last_error: Exception | None = None

    for attempt in range(max_retries + 1):
        try:
            message = client.messages.create(
                model=model,
                max_tokens=8192,
                system=SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": user_message},
                ],
            )
        except APIError as exc:
            raise ClaudeError(f"Claude API error: {exc}") from exc
        except Exception as exc:  # noqa: BLE001
            raise ClaudeError(f"Unexpected Claude error: {exc}") from exc

        text_chunks = [
            block.text for block in message.content if getattr(block, "type", "") == "text"
        ]
        raw_text = "".join(text_chunks)
        last_raw_text = raw_text

        try:
            parsed = _extract_json(raw_text)
        except json.JSONDecodeError as exc:
            last_error = exc
            logger.warning(
                "Claude JSON parse failed (attempt %d/%d): %s",
                attempt + 1,
                max_retries + 1,
                exc,
            )
            continue

        return _coerce_response(parsed, requests)

    raise ClaudeError(
        "Failed to parse Claude response as JSON after retry. "
        f"Raw response head: {last_raw_text[:500]!r} | Last error: {last_error}"
    )
