"""Roadmap comparison: classify each HCP unmet need against product roadmap
Ideas, then emit a CSV join table and a markdown coverage report.

Input sources are the SAME ones the live API uses — the Google Sheet and
(optionally) Slack — so the CLI never goes stale relative to the dashboard.
The roadmap is parsed from `backend/roadmap.md`.

Run from backend/:
    python -m analysis.roadmap_comparison.compare

Optional flags:
    --no-slack          Skip Slack ingestion (Sheet only)
    --skip-buckets      Skip the dashboard's bucketing pass (default — we
                        only need classification here)
"""
from __future__ import annotations

import argparse
import csv
import logging
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Make `from config import …` work when run as a module.
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config import get_settings  # noqa: E402
from models.schemas import HCPRequest, RoadmapItem  # noqa: E402
from services.alignment import AlignmentError, classify_requests  # noqa: E402
from services.roadmap import load_roadmap  # noqa: E402
from services.sheets import SheetsError, fetch_hcp_requests  # noqa: E402
from services.slack import SlackError, fetch_slack_requests  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

MODULE_DIR = Path(__file__).parent
OUTPUTS_DIR = MODULE_DIR / "outputs"
JOIN_TABLE_CSV = OUTPUTS_DIR / "join_table.csv"
COVERAGE_REPORT_MD = OUTPUTS_DIR / "coverage_report.md"


# ---------------------------------------------------------------------------
# Input loading (now sourced from the live API pipeline)
# ---------------------------------------------------------------------------

def load_unmet_needs(
    *,
    settings,
    include_slack: bool,
) -> List[HCPRequest]:
    """Pull HCP requests from the same ingestion paths the API uses."""
    needs: List[HCPRequest] = []

    try:
        sheet_needs = fetch_hcp_requests(
            spreadsheet_id=settings.google_sheets_id,
            sheet_range=settings.google_sheets_range,
            credentials_path=settings.google_service_account_json,
        )
        needs.extend(sheet_needs)
        logger.info("Loaded %d unmet needs from Google Sheet", len(sheet_needs))
    except SheetsError as exc:
        logger.error("Sheets fetch failed: %s", exc)

    if include_slack and settings.slack_bot_token and settings.slack_channel_id:
        try:
            slack_needs = fetch_slack_requests(
                bot_token=settings.slack_bot_token,
                channel_id=settings.slack_channel_id,
                message_limit=settings.slack_message_limit,
            )
            needs.extend(slack_needs)
            logger.info("Loaded %d unmet needs from Slack", len(slack_needs))
        except SlackError as exc:
            logger.warning("Slack fetch failed (continuing without it): %s", exc)
    elif include_slack:
        logger.info("Slack ingestion not configured — skipping")

    return needs


def load_roadmap_ideas(*, settings) -> List[RoadmapItem]:
    items = load_roadmap(settings.roadmap_path)
    logger.info("Loaded %d roadmap items from %s", len(items), settings.roadmap_path)
    return items


# ---------------------------------------------------------------------------
# Output: join_table.csv
# ---------------------------------------------------------------------------

def write_join_table(
    needs: List[HCPRequest],
    classifications: Dict[str, dict],
) -> None:
    OUTPUTS_DIR.mkdir(exist_ok=True)
    fieldnames = [
        "request_id",
        "hcp_response",
        "first_name",
        "last_name",
        "npi",
        "slack_channel",
        "pulse",
        "date_time",
        "classification",
        "gap_category",
        "confidence",
        "matched_roadmap_keys",
        "reasoning",
    ]
    with open(JOIN_TABLE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for need in needs:
            clf = classifications.get(need.request_id) or {}
            writer.writerow(
                {
                    "request_id": need.request_id,
                    "hcp_response": need.hcp_response,
                    "first_name": need.first_name,
                    "last_name": need.last_name,
                    "npi": need.npi,
                    "slack_channel": need.slack_channel,
                    "pulse": need.pulse,
                    "date_time": need.date_time or "",
                    "classification": clf.get("classification", ""),
                    "gap_category": clf.get("gap_category", ""),
                    "confidence": clf.get("confidence", ""),
                    "matched_roadmap_keys": "; ".join(
                        clf.get("matched_roadmap_keys") or []
                    ),
                    "reasoning": clf.get("reasoning", ""),
                }
            )
    logger.info("Wrote %s", JOIN_TABLE_CSV)


# ---------------------------------------------------------------------------
# Output: coverage_report.md
# ---------------------------------------------------------------------------

def _hcp_label(need: HCPRequest) -> str:
    name = " ".join(p for p in (need.first_name, need.last_name) if p) or "HCP"
    ch = need.slack_channel or ""
    return f"{name} ({ch})" if ch else name


def write_coverage_report(
    needs: List[HCPRequest],
    classifications: Dict[str, dict],
    roadmap_by_key: Dict[str, RoadmapItem],
) -> None:
    pairs: List[tuple[HCPRequest, dict]] = []
    for need in needs:
        clf = classifications.get(need.request_id)
        if clf is None:
            continue
        pairs.append((need, clf))

    total = len(pairs)
    covered = [p for p in pairs if p[1]["classification"] == "covered"]
    partial = [p for p in pairs if p[1]["classification"] == "partial"]
    gaps = [p for p in pairs if p[1]["classification"] == "gap"]

    gap_category_counts: Counter[str] = Counter()
    for _, clf in pairs:
        if clf.get("gap_category"):
            gap_category_counts[clf["gap_category"]] += 1
    top_3_gaps = gap_category_counts.most_common(3)

    roadmap_validation: Dict[str, list[tuple[HCPRequest, dict]]] = {}
    for need, clf in pairs:
        for key in clf.get("matched_roadmap_keys") or []:
            roadmap_validation.setdefault(key, []).append((need, clf))

    lines: List[str] = []

    # --- Executive summary ---
    lines += [
        "# HCP Unmet Needs × Product Roadmap: Coverage Report",
        "",
        f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} — "
        f"{total} unmet needs × {len(roadmap_by_key)} roadmap Ideas_",
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
        "_Unmet needs with zero roadmap coverage, grouped by theme._",
        "",
    ]

    gaps_by_cat: Dict[str, list[tuple[HCPRequest, dict]]] = {}
    for need, clf in gaps:
        cat = clf.get("gap_category") or "uncategorized"
        gaps_by_cat.setdefault(cat, []).append((need, clf))

    for cat in sorted(gaps_by_cat, key=lambda c: -len(gaps_by_cat[c])):
        group = gaps_by_cat[cat]
        lines.append(f"### {cat} ({len(group)} need{'s' if len(group) != 1 else ''})")
        lines.append("")
        for need, clf in group:
            quote = (need.hcp_response or "").replace("\n", " ").strip()
            lines.append(f'- **{_hcp_label(need)}**: "{quote}"')
            if clf.get("reasoning"):
                lines.append(f"  _{clf['reasoning']}_")
        lines.append("")

    if not gaps:
        lines += ["_No pure gaps found._", ""]

    if partial:
        lines += ["### Partial coverage (adjacent but incomplete)", ""]
        for need, clf in partial:
            quote = (need.hcp_response or "").replace("\n", " ").strip()
            cat = clf.get("gap_category") or ""
            keys = ", ".join(clf.get("matched_roadmap_keys") or []) or "—"
            lines.append(f'- **{_hcp_label(need)}** [{cat}]: "{quote}"')
            lines.append(f"  _Nearest match: {keys}. {clf.get('reasoning', '')}_")
        lines.append("")

    # --- Validated roadmap items ---
    lines += [
        "---",
        "",
        "## Validated Roadmap Items",
        "",
        "_Roadmap initiatives where at least one HCP unmet need confirms real demand._",
        "",
        "| Roadmap Item | Title | Status | Validating Needs |",
        "|-------------|-------|--------|-----------------|",
    ]
    for key, validators in sorted(
        roadmap_validation.items(), key=lambda kv: -len(kv[1])
    ):
        item = roadmap_by_key.get(key)
        title = item.title if item else key
        status = item.status if item else "—"
        labels = "; ".join(_hcp_label(n) for n, _ in validators[:3])
        if len(validators) > 3:
            labels += f" (+{len(validators) - 3} more)"
        lines.append(f"| {key} | {title} | {status} | {labels} |")
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
    initiative_data: Dict[str, dict] = {}
    for key, validators in roadmap_validation.items():
        item = roadmap_by_key.get(key)
        initiative = (item.initiative if item else "") or "Unassigned"
        entry = initiative_data.setdefault(
            initiative, {"keys": [], "validators": [], "confidences": []}
        )
        entry["keys"].append(key)
        entry["validators"].extend(validators)
        for _, clf in validators:
            entry["confidences"].append(clf.get("confidence", ""))

    for initiative in sorted(
        initiative_data, key=lambda i: -len(initiative_data[i]["validators"])
    ):
        entry = initiative_data[initiative]
        keys_str = ", ".join(sorted(set(entry["keys"])))
        count = len({n.request_id for n, _ in entry["validators"]})
        conf_counts = Counter(entry["confidences"])
        conf_str = " / ".join(f"{v} {k}" for k, v in conf_counts.most_common() if k)
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-slack",
        action="store_true",
        help="Skip Slack ingestion even if a token is configured",
    )
    args = parser.parse_args()

    settings = get_settings()
    if not settings.anthropic_api_key:
        sys.exit("ANTHROPIC_API_KEY is not set — add it to backend/.env")

    needs = load_unmet_needs(settings=settings, include_slack=not args.no_slack)
    if not needs:
        sys.exit("No unmet needs found — check sheet/Slack configuration")

    roadmap_items = load_roadmap_ideas(settings=settings)
    if not roadmap_items:
        sys.exit(
            f"No roadmap items parsed from {settings.roadmap_path}. "
            "Make sure the roadmap markdown is present and well-formed."
        )

    roadmap_by_key: Dict[str, RoadmapItem] = {item.key: item for item in roadmap_items}

    try:
        classifications = classify_requests(
            needs,
            roadmap_items,
            api_key=settings.anthropic_api_key,
            model=settings.anthropic_model,
        )
    except AlignmentError as exc:
        sys.exit(f"Alignment failed: {exc}")

    write_join_table(needs, classifications)
    write_coverage_report(needs, classifications, roadmap_by_key)

    n_covered = sum(
        1 for c in classifications.values() if c["classification"] == "covered"
    )
    n_partial = sum(
        1 for c in classifications.values() if c["classification"] == "partial"
    )
    n_gap = sum(1 for c in classifications.values() if c["classification"] == "gap")
    print(
        f"\nDone. {len(needs)} needs — covered: {n_covered}, "
        f"partial: {n_partial}, gap: {n_gap}"
    )
    print(f"  {JOIN_TABLE_CSV}")
    print(f"  {COVERAGE_REPORT_MD}")


if __name__ == "__main__":
    main()
