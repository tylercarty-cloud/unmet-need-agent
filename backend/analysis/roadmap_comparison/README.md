# Roadmap Comparison

Classifies each HCP unmet need against the product roadmap (Jira Ideas) using
Claude, then outputs a structured coverage report and join table.

This module shares its prompt (`prompt.md`) and classification logic with the
live `services/alignment.py` service — both call the same `classify_requests`
kernel, so the dashboard view and the offline report stay in lockstep.

## Inputs (live, no separate CSVs needed)

| Source | Loaded via |
|--------|-----------|
| Google Sheet of HCP feedback | `services.sheets.fetch_hcp_requests` |
| Slack channel (optional) | `services.slack.fetch_slack_requests` |
| Roadmap markdown | `services.roadmap.load_roadmap` (`backend/roadmap.md`) |

The same `backend/.env` the API uses configures all three sources.

## Outputs

| File | Description |
|------|-------------|
| `outputs/join_table.csv` | One row per unmet need with classification, gap category, confidence, matched Jira keys, and reasoning |
| `outputs/coverage_report.md` | Markdown report with executive summary, gap leaderboard, validated roadmap items, and coverage matrix |

## Run

From `backend/`:

```bash
python -m analysis.roadmap_comparison.compare           # Sheet + Slack
python -m analysis.roadmap_comparison.compare --no-slack  # Sheet only
```

Requires `ANTHROPIC_API_KEY`, `GOOGLE_SHEETS_ID`, and `GOOGLE_SERVICE_ACCOUNT_JSON`
in `backend/.env`. Slack ingestion is auto-enabled if `SLACK_BOT_TOKEN` and
`SLACK_CHANNEL_ID` are set.

Uses whatever model is set in `ANTHROPIC_MODEL` (default: `claude-opus-4-5`).
The classification prompt enables Anthropic prompt caching on the roadmap
block, so repeated runs within a 5-minute window are cheap.

## Classifications

| Value | Meaning |
|-------|---------|
| `covered` | At least one roadmap item alone would substantially satisfy the need |
| `partial` | A roadmap item is adjacent but misses a key dimension |
| `gap` | No roadmap item addresses the need |

## Gap categories

`content-gap` · `channel-gap` · `data-gap` · `workflow-gap` · `cross-product-gap`

## Confidence

`high` = explicit match · `medium` = interpretive match · `low` = stretch

## Prompt

See [`prompt.md`](prompt.md) for the full classification prompt sent to Claude.
This file is also loaded at runtime by `backend/services/alignment.py`, so
edits here flow through to the dashboard automatically.
