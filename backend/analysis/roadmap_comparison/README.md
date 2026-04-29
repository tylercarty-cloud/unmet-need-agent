# Roadmap Comparison

Classifies each HCP unmet need against the product roadmap (Jira Ideas) using Claude, then outputs a structured coverage report and join table.

## Inputs

| File | Description |
|------|-------------|
| `backend/data/unmet_needs_master.csv` | 32 HCP unmet needs captured from field channels |
| `backend/data/roadmap.csv` | Jira export — filtered to `Issue Type = Idea` |

## Outputs

| File | Description |
|------|-------------|
| `outputs/join_table.csv` | One row per unmet need with classification, gap category, confidence, matched Jira keys, and reasoning |
| `outputs/coverage_report.md` | Markdown report with executive summary, gap leaderboard, validated roadmap items, and coverage matrix |

## Run

From `backend/`:

```bash
python3 -m analysis.roadmap_comparison.compare
```

Requires `ANTHROPIC_API_KEY` in `backend/.env`. Uses whatever model is set in `ANTHROPIC_MODEL` (default: `claude-opus-4-5`).

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
