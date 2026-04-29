"""Roadmap comparison: classify each HCP unmet need against product roadmap Ideas.

Run from backend/:
    python -m analysis.roadmap_comparison.compare
"""
from __future__ import annotations

import csv
import json
import logging
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import TypedDict

from anthropic import Anthropic, APIError

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import get_settings

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
MODULE_DIR = Path(__file__).parent
OUTPUTS_DIR = MODULE_DIR / "outputs"

UNMET_NEEDS_CSV = DATA_DIR / "unmet_needs_master.csv"
ROADMAP_CSV = DATA_DIR / "roadmap.csv"
PROMPT_MD = MODULE_DIR / "prompt.md"
JOIN_TABLE_CSV = OUTPUTS_DIR / "join_table.csv"
COVERAGE_REPORT_MD = OUTPUTS_DIR / "coverage_report.md"

DESCRIPTION_MAX_CHARS = 400
MAX_RETRIES = 1

GAP_CATEGORIES = (
    "content-gap",
    "channel-gap",
    "data-gap",
    "workflow-gap",
    "cross-product-gap",
)


class RoadmapItem(TypedDict):
    issue_key: str
    summary: str
    status: str
    description: str
    initiative: str
    project_start: str
    project_target: str


class UnmetNeed(TypedDict):
    hcp_response: str
    first_name: str
    last_name: str
    npi: str
    slack_channel: str
    pulse: str
    source_channel_type: str


class Classification(TypedDict):
    classification: str
    gap_category: str | None
    confidence: str
    matched_roadmap_keys: list[str]
    reasoning: str


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_unmet_needs() -> list[UnmetNeed]:
    needs: list[UnmetNeed] = []
    with open(UNMET_NEEDS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            needs.append(
                UnmetNeed(
                    hcp_response=row.get("HCP Response", "").strip(),
                    first_name=row.get("First Name", "").strip(),
                    last_name=row.get("Last Name", "").strip(),
                    npi=row.get("NPI", "").strip(),
                    slack_channel=row.get("Slack Channel Name", "").strip(),
                    pulse=row.get("Pulse", "").strip(),
                    source_channel_type=row.get("Source Channel Type", "").strip(),
                )
            )
    logger.info("Loaded %d unmet needs", len(needs))
    return needs


def load_roadmap_ideas() -> list[RoadmapItem]:
    items: list[RoadmapItem] = []
    with open(ROADMAP_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("Issue Type", "").strip() != "Idea":
                continue
            desc = row.get("Description", "").strip()
            if len(desc) > DESCRIPTION_MAX_CHARS:
                desc = desc[:DESCRIPTION_MAX_CHARS] + "…"
            items.append(
                RoadmapItem(
                    issue_key=row.get("Issue key", "").strip(),
                    summary=row.get("Summary", "").strip(),
                    status=row.get("Status", "").strip(),
                    description=desc,
                    initiative=row.get("Custom field (Initiative)", "").strip(),
                    project_start=row.get("Custom field (Project start)", "").strip(),
                    project_target=row.get("Custom field (Project target)", "").strip(),
                )
            )
    logger.info("Loaded %d roadmap Ideas", len(items))
    return items


# ---------------------------------------------------------------------------
# Claude classification
# ---------------------------------------------------------------------------

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


def _build_user_message(need: UnmetNeed, roadmap_items: list[RoadmapItem]) -> str:
    need_block = json.dumps(
        {
            "hcp_response": need["hcp_response"],
            "first_name": need["first_name"],
            "last_name": need["last_name"],
            "slack_channel": need["slack_channel"],
            "pulse": need["pulse"],
            "source_channel_type": need["source_channel_type"],
        },
        ensure_ascii=False,
        indent=2,
    )
    roadmap_block = json.dumps(roadmap_items, ensure_ascii=False, indent=2)
    return (
        f"## HCP Unmet Need\n\n```json\n{need_block}\n```\n\n"
        f"## Roadmap Ideas ({len(roadmap_items)} items)\n\n```json\n{roadmap_block}\n```\n\n"
        "Classify the unmet need against the roadmap. "
        "Respond with ONLY the JSON object. "
        "Your entire response must start with `{` and end with `}`."
    )


def classify_need(
    need: UnmetNeed,
    roadmap_items: list[RoadmapItem],
    *,
    client: Anthropic,
    model: str,
    system_prompt: str,
) -> Classification:
    user_message = _build_user_message(need, roadmap_items)
    last_raw = ""
    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES + 1):
        try:
            message = client.messages.create(
                model=model,
                max_tokens=1024,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )
        except APIError as exc:
            raise RuntimeError(f"Claude API error: {exc}") from exc

        text_chunks = [
            block.text
            for block in message.content
            if getattr(block, "type", "") == "text"
        ]
        last_raw = "".join(text_chunks)

        try:
            parsed = _extract_json(last_raw)
        except json.JSONDecodeError as exc:
            last_error = exc
            logger.warning(
                "JSON parse failed (attempt %d/%d): %s",
                attempt + 1,
                MAX_RETRIES + 1,
                exc,
            )
            continue

        return Classification(
            classification=str(parsed.get("classification", "gap")).strip(),
            gap_category=parsed.get("gap_category") or None,
            confidence=str(parsed.get("confidence", "low")).strip(),
            matched_roadmap_keys=parsed.get("matched_roadmap_keys") or [],
            reasoning=str(parsed.get("reasoning", "")).strip(),
        )

    raise RuntimeError(
        f"Failed to parse Claude response after retries. "
        f"Raw head: {last_raw[:500]!r} | Last error: {last_error}"
    )


# ---------------------------------------------------------------------------
# Output: join_table.csv
# ---------------------------------------------------------------------------

def write_join_table(
    needs: list[UnmetNeed],
    classifications: list[Classification],
) -> None:
    OUTPUTS_DIR.mkdir(exist_ok=True)
    fieldnames = [
        "hcp_response",
        "first_name",
        "last_name",
        "npi",
        "slack_channel",
        "pulse",
        "source_channel_type",
        "classification",
        "gap_category",
        "confidence",
        "matched_roadmap_keys",
        "reasoning",
    ]
    with open(JOIN_TABLE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for need, clf in zip(needs, classifications):
            writer.writerow(
                {
                    **need,
                    "classification": clf["classification"],
                    "gap_category": clf["gap_category"] or "",
                    "confidence": clf["confidence"],
                    "matched_roadmap_keys": "; ".join(clf["matched_roadmap_keys"]),
                    "reasoning": clf["reasoning"],
                }
            )
    logger.info("Wrote %s", JOIN_TABLE_CSV)


# ---------------------------------------------------------------------------
# Output: coverage_report.md
# ---------------------------------------------------------------------------

def _hcp_label(need: UnmetNeed) -> str:
    parts = [need["first_name"], need["last_name"]]
    name = " ".join(p for p in parts if p) or "HCP"
    ch = need["source_channel_type"] or need["slack_channel"]
    return f"{name} ({ch})" if ch else name


def write_coverage_report(
    needs: list[UnmetNeed],
    classifications: list[Classification],
    roadmap_by_key: dict[str, RoadmapItem],
) -> None:
    pairs = list(zip(needs, classifications))

    total = len(pairs)
    covered = [p for p in pairs if p[1]["classification"] == "covered"]
    partial = [p for p in pairs if p[1]["classification"] == "partial"]
    gaps = [p for p in pairs if p[1]["classification"] == "gap"]

    gap_category_counts: Counter[str] = Counter()
    for _, clf in pairs:
        if clf["gap_category"]:
            gap_category_counts[clf["gap_category"]] += 1

    top_3_gaps = gap_category_counts.most_common(3)

    # Build roadmap validation index: key → list of (need, clf)
    roadmap_validation: dict[str, list[tuple[UnmetNeed, Classification]]] = {}
    for need, clf in pairs:
        for key in clf["matched_roadmap_keys"]:
            roadmap_validation.setdefault(key, []).append((need, clf))

    lines: list[str] = []

    # --- Executive summary ---
    lines += [
        "# HCP Unmet Needs × Product Roadmap: Coverage Report",
        "",
        f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} — {total} unmet needs × {len(roadmap_by_key)} roadmap Ideas_",
        "",
        "## Executive Summary",
        "",
        "| Covered | Partial | Gap | Total |",
        "|---------|---------|-----|-------|",
        f"| {len(covered)} | {len(partial)} | {len(gaps)} | {total} |",
        "",
    ]
    if top_3_gaps:
        lines.append("**Top 3 gap categories:**")
        lines.append("")
        for cat, count in top_3_gaps:
            lines.append(f"- **{cat}** — {count} need(s)")
        lines.append("")

    # --- Gap leaderboard ---
    lines += [
        "---",
        "",
        "## Gap Leaderboard",
        "",
        "_Unmet needs with zero roadmap coverage, grouped by theme. "
        "Themes derived from gap categories and reasoning._",
        "",
    ]

    # Group pure gaps by gap_category
    gaps_by_cat: dict[str, list[tuple[UnmetNeed, Classification]]] = {}
    for need, clf in gaps:
        cat = clf["gap_category"] or "uncategorized"
        gaps_by_cat.setdefault(cat, []).append((need, clf))

    # Sort categories by count descending
    for cat in sorted(gaps_by_cat, key=lambda c: -len(gaps_by_cat[c])):
        group = gaps_by_cat[cat]
        lines.append(f"### {cat} ({len(group)} need{'s' if len(group) != 1 else ''})")
        lines.append("")
        for need, clf in group:
            label = _hcp_label(need)
            quote = need["hcp_response"].replace("\n", " ").strip()
            lines.append(f'- **{label}**: "{quote}"')
            if clf["reasoning"]:
                lines.append(f"  _{clf['reasoning']}_")
        lines.append("")

    if not gaps:
        lines += ["_No pure gaps found._", ""]

    # Also list partial-coverage items under this section for completeness
    if partial:
        lines += [
            "### Partial coverage (adjacent but incomplete)",
            "",
        ]
        for need, clf in partial:
            label = _hcp_label(need)
            quote = need["hcp_response"].replace("\n", " ").strip()
            cat = clf["gap_category"] or ""
            keys = ", ".join(clf["matched_roadmap_keys"]) or "—"
            lines.append(f'- **{label}** [{cat}]: "{quote}"')
            lines.append(f"  _Nearest match: {keys}. {clf['reasoning']}_")
        lines.append("")

    # --- Validated roadmap items ---
    lines += [
        "---",
        "",
        "## Validated Roadmap Items",
        "",
        "_Roadmap initiatives where at least one HCP unmet need confirms real demand._",
        "",
        "| Roadmap Item | Summary | Status | Validating Needs |",
        "|-------------|---------|--------|-----------------|",
    ]

    for key, validators in sorted(
        roadmap_validation.items(), key=lambda kv: -len(kv[1])
    ):
        item = roadmap_by_key.get(key)
        summary = item["summary"] if item else key
        status = item["status"] if item else "—"
        hcp_labels = "; ".join(_hcp_label(n) for n, _ in validators[:3])
        if len(validators) > 3:
            hcp_labels += f" (+{len(validators) - 3} more)"
        lines.append(f"| {key} | {summary} | {status} | {hcp_labels} |")

    if not roadmap_validation:
        lines.append("| — | No validated items | — | — |")
    lines.append("")

    # --- Coverage matrix ---
    lines += [
        "---",
        "",
        "## Coverage Matrix",
        "",
        "_Roadmap initiatives × count of validating unmet needs._",
        "",
        "| Initiative | Roadmap Items | Validating Needs | Confidence |",
        "|-----------|--------------|-----------------|------------|",
    ]

    # Group by initiative
    initiative_data: dict[str, dict] = {}
    for key, validators in roadmap_validation.items():
        item = roadmap_by_key.get(key)
        initiative = (item["initiative"] if item else "") or "Unassigned"
        entry = initiative_data.setdefault(
            initiative, {"keys": [], "validators": [], "confidences": []}
        )
        entry["keys"].append(key)
        entry["validators"].extend(validators)
        for _, clf in validators:
            entry["confidences"].append(clf["confidence"])

    # Sort by validating need count descending
    for initiative in sorted(
        initiative_data, key=lambda i: -len(initiative_data[i]["validators"])
    ):
        entry = initiative_data[initiative]
        keys_str = ", ".join(sorted(set(entry["keys"])))
        count = len(set(id(n) for n, _ in entry["validators"]))
        conf_counts = Counter(entry["confidences"])
        conf_str = " / ".join(
            f"{v} {k}" for k, v in conf_counts.most_common()
        )
        lines.append(f"| {initiative} | {keys_str} | {count} | {conf_str} |")

    if not initiative_data:
        lines.append("| — | — | 0 | — |")
    lines.append("")

    OUTPUTS_DIR.mkdir(exist_ok=True)
    COVERAGE_REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Wrote %s", COVERAGE_REPORT_MD)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    settings = get_settings()
    if not settings.anthropic_api_key:
        sys.exit("ANTHROPIC_API_KEY is not set — add it to backend/.env")

    system_prompt = PROMPT_MD.read_text(encoding="utf-8")
    client = Anthropic(api_key=settings.anthropic_api_key)
    model = settings.anthropic_model

    needs = load_unmet_needs()
    roadmap_items = load_roadmap_ideas()
    roadmap_by_key: dict[str, RoadmapItem] = {
        item["issue_key"]: item for item in roadmap_items
    }

    classifications: list[Classification] = []
    for i, need in enumerate(needs, 1):
        logger.info(
            "[%d/%d] Classifying: %s",
            i,
            len(needs),
            need["hcp_response"][:80],
        )
        clf = classify_need(
            need,
            roadmap_items,
            client=client,
            model=model,
            system_prompt=system_prompt,
        )
        logger.info(
            "  → %s | %s | confidence=%s",
            clf["classification"],
            clf["gap_category"] or "—",
            clf["confidence"],
        )
        classifications.append(clf)

    write_join_table(needs, classifications)
    write_coverage_report(needs, classifications, roadmap_by_key)

    total = len(needs)
    n_covered = sum(1 for c in classifications if c["classification"] == "covered")
    n_partial = sum(1 for c in classifications if c["classification"] == "partial")
    n_gap = sum(1 for c in classifications if c["classification"] == "gap")
    print(
        f"\nDone. {total} needs — covered: {n_covered}, partial: {n_partial}, gap: {n_gap}"
    )
    print(f"  {JOIN_TABLE_CSV}")
    print(f"  {COVERAGE_REPORT_MD}")


if __name__ == "__main__":
    main()
