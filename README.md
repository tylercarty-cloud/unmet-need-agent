# HCP Unmet Needs Bucketing Dashboard

A full-stack internal tool that pulls Healthcare Professional (HCP) feedback
from a Google Sheet, asks Claude to discover natural thematic groupings in the
messages, and displays the results as an interactive dashboard.

The data represents HCP requests for which **Impiricus does not currently have
an aligned product offering**, so the goal of the tool is to surface patterns
in *unmet* needs.

## Architecture

```
hcp-unmet-need-agent/
├── backend/                 FastAPI service
│   ├── main.py              FastAPI entry point + endpoints
│   ├── config.py            Environment configuration
│   ├── services/
│   │   ├── sheets.py        Google Sheets client + row normalization
│   │   └── claude.py        Claude bucketing + JSON-mode prefill
│   └── models/schemas.py    Pydantic request/response models
└── frontend/                Vite + React + Tailwind dashboard
    └── src/
        ├── App.jsx
        ├── components/      StatsHeader, BucketChart, BucketGrid, …
        ├── hooks/useBuckets.js
        └── lib/api.js
```

## 1. Set up the Google service account

1. In the [Google Cloud Console](https://console.cloud.google.com/), create a
   project (or pick an existing one) and enable the **Google Sheets API**.
2. Open **IAM & Admin → Service Accounts**, create a new service account, and
   under **Keys** generate a new **JSON** key. Download the file.
3. Save the file at `backend/credentials/service-account.json` (or any path you
   prefer; just point `GOOGLE_SERVICE_ACCOUNT_JSON` at it).
4. Open your source Google Sheet and click **Share**. Add the service
   account's email address (looks like `xxx@yyy.iam.gserviceaccount.com`) with
   **Viewer** access.
5. Copy the spreadsheet ID from its URL:
   `https://docs.google.com/spreadsheets/d/{THIS_PART}/edit`.

The sheet is expected to have a header row containing some recognizable
combination of these columns (case-insensitive, order doesn't matter):

| HCP Response | Date Time | First Name | Last Name | NPI | Link to Slack post | Slack Channel Name | Pulse |

Empty rows and rows missing an HCP response are skipped automatically.

## 2. Get an Anthropic API key

1. Sign in to <https://console.anthropic.com/>.
2. Go to **API Keys** and create a new key (starts with `sk-ant-…`).
3. The default model is `claude-opus-4-5`. Override with `ANTHROPIC_MODEL` in
   `.env` if you want a different snapshot.

## 3. Run the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Fill in ANTHROPIC_API_KEY, GOOGLE_SHEETS_ID, etc.

python main.py
# or: uvicorn main:app --reload --port 8000
```

The API is now serving at <http://localhost:8000>.

### Endpoints

- `GET /api/health` — liveness check
- `GET /api/buckets` — fetches the sheet, sends rows to Claude, returns
  bucketed JSON. May take 10–30 seconds depending on data volume.

### Error semantics

| Failure                           | Status | Body                                   |
| --------------------------------- | ------ | -------------------------------------- |
| Google Sheets unreachable / empty | 503    | `{ "detail": "Google Sheets error: …" }` |
| Claude API error                  | 502    | `{ "detail": "Claude API error: …" }`  |
| Claude JSON unparseable (after retry) | 500    | `{ "detail": "Failed to parse Claude response …" }` |

All errors are logged to stdout with timestamps.

## 4. Run the frontend

```bash
cd frontend
npm install

cp .env.example .env
# VITE_API_BASE_URL defaults to http://localhost:8000

npm run dev
```

Open <http://localhost:5173>. The dashboard will auto-fetch buckets on mount.

## Features

- **Auto-refresh on load** with skeleton loaders during the (slow) Claude call
- **Manual refresh button** in the header
- **Recharts horizontal bar chart** of bucket counts; clicking a bar scrolls
  to and highlights that bucket
- **Sortable buckets** (by count desc — default — or alphabetical)
- **Search/filter** across HCP names, NPIs, response text, channels, pulse
- **CSV export** of the (filtered) bucketed results
- **Dark mode** toggle (persisted to `localStorage`)
- **Responsive grid** — 1 col mobile, 2 col tablet, 3 col desktop
- Click-through to the original Slack post opens in a new tab

## Configuration reference

### `backend/.env`

| Var                           | Required | Default                                  | Notes |
| ----------------------------- | -------- | ---------------------------------------- | ----- |
| `ANTHROPIC_API_KEY`           | yes      | —                                        | `sk-ant-…` |
| `ANTHROPIC_MODEL`             | no       | `claude-opus-4-5`                        | |
| `GOOGLE_SHEETS_ID`            | yes      | —                                        | Sheet ID from URL |
| `GOOGLE_SHEETS_RANGE`         | no       | `Sheet1!A:H`                             | A1 notation |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | no       | `./credentials/service-account.json`     | Path to JSON key |
| `CORS_ORIGINS`                | no       | `http://localhost:5173`                  | Comma-separated |
| `CACHE_TTL_SECONDS`           | no       | `0`                                      | Optional in-memory cache for `/api/buckets` |

### `frontend/.env`

| Var                  | Default                  | Notes |
| -------------------- | ------------------------ | ----- |
| `VITE_API_BASE_URL`  | `http://localhost:8000`  | Backend base URL |

## Privacy notes

- NPIs are PII-adjacent. The backend never logs NPIs; the frontend masks all
  but the last four digits in the UI.
- The Claude call sends the full HCP responses + metadata to Anthropic. Make
  sure your data-sharing posture is acceptable for this use case before
  pointing it at production data.
- Set `CACHE_TTL_SECONDS` to a small value (e.g. 300) if you'd like to avoid
  re-running the analysis on every page load during development.

## Scaling tips

- The Claude call is the slow part. For sheets with >500 rows, consider
  chunking inputs and merging buckets across chunks (not implemented today).
- The default `max_tokens` for the Claude response is `8192`; raise it if you
  expect very large bucketed payloads.
