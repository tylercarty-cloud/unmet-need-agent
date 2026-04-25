# HCP Unmet Needs Bucketing Dashboard

## Project Overview
Build a full-stack application that pulls HCP (Healthcare Professional) feedback data from a Google Sheet, uses the Claude API to dynamically categorize requests into buckets based on shared themes, and displays the results in an interactive dashboard. The data represents end-user messages where Impiricus does not currently have an aligned product offering, so the goal is to surface patterns in unmet needs.

## Tech Stack
- **Backend:** Python (FastAPI)
- **Frontend:** React (Vite) + TailwindCSS + shadcn/ui components
- **Data Source:** Google Sheets API
- **AI:** Anthropic Claude API (use `claude-opus-4-5` or latest available model)
- **Charts/Viz:** Recharts for bucket counts visualization

## Data Schema
The source Google Sheet has these columns:
- `HCP Response` (string) — the actual message content
- `Date Time` (datetime)
- `First Name` (string)
- `Last Name` (string)
- `NPI` (string) — National Provider Identifier
- `Link to Slack post` (URL)
- `Slack Channel Name` (string)
- `Pulse` (string)

## Backend Requirements (Python / FastAPI)

### Project Structure
backend/
├── main.py              # FastAPI app entry
├── config.py            # Env vars, settings
├── services/
│   ├── sheets.py        # Google Sheets API client
│   └── claude.py        # Claude API client + bucketing logic
├── models/
│   └── schemas.py       # Pydantic models
├── requirements.txt
└── .env.example


### Endpoints
- `GET /api/buckets` — Pulls fresh data from Google Sheets, sends to Claude for categorization, returns structured buckets
- `GET /api/health` — Health check

### Google Sheets Integration
- Use `google-api-python-client` and `google-auth` for service account auth
- Env vars: `GOOGLE_SHEETS_ID`, `GOOGLE_SHEETS_RANGE` (e.g. `Sheet1!A:H`), `GOOGLE_SERVICE_ACCOUNT_JSON` (path to credentials JSON)
- Normalize the data into a list of dicts matching the schema above
- Handle empty rows and malformed data gracefully

### Claude Bucketing Logic
The prompt sent to Claude should:
1. Receive the full list of HCP responses with their metadata
2. Instruct Claude to dynamically identify natural thematic buckets (no predefined categories)
3. Return a strict JSON response with this structure:

```json
{
  "buckets": [
    {
      "bucket_name": "Rep Requests",
      "description": "HCPs requesting direct contact with a sales or medical rep",
      "count": 12,
      "requests": [
        {
          "hcp_response": "Can a rep reach out to discuss...",
          "first_name": "Jane",
          "last_name": "Doe",
          "npi": "1234567890",
          "date_time": "2026-04-20T14:30:00",
          "slack_link": "https://...",
          "slack_channel": "#feedback",
          "pulse": "..."
        }
      ]
    }
  ],
  "total_requests": 47,
  "analysis_timestamp": "2026-04-24T10:00:00Z"
}
```

### Claude Prompt Template
Use this system prompt for the Claude API call:

> You are analyzing messages from healthcare professionals (HCPs) that represent unmet needs — requests for which Impiricus does not currently have an aligned product. Your job is to identify natural thematic groupings in these messages and bucket them accordingly.
>
> Rules:
> - Identify buckets dynamically based on shared intent or topic (e.g., "Rep Requests", "CME Content Needs", "Patient Resource Requests")
> - Each request must be assigned to exactly one bucket (pick the best fit)
> - Bucket names should be concise (2-4 words), title-cased, and descriptive of the underlying need
> - Preserve ALL original metadata for each request in the output
> - Aim for 4-12 buckets depending on data volume — don't over-fragment or over-consolidate
> - If a request doesn't fit a clear theme, place it in an "Other" bucket
>
> Return ONLY valid JSON matching the specified schema. No preamble, no markdown code fences.

Use Claude's JSON mode / response prefilling (`{` prefill) to guarantee clean JSON output. Handle parse errors with a retry.

### Error Handling
- If Google Sheets fetch fails → return 503 with message
- If Claude API fails → return 502 with message
- If JSON parsing fails → retry once, then return 500 with the raw response for debugging
- Log all errors to stdout with timestamps

## Frontend Requirements (React + Vite + Tailwind)

### Project Structure
### Endpoints
- `GET /api/buckets` — Pulls fresh data from Google Sheets, sends to Claude for categorization, returns structured buckets
- `GET /api/health` — Health check

### Google Sheets Integration
- Use `google-api-python-client` and `google-auth` for service account auth
- Env vars: `GOOGLE_SHEETS_ID`, `GOOGLE_SHEETS_RANGE` (e.g. `Sheet1!A:H`), `GOOGLE_SERVICE_ACCOUNT_JSON` (path to credentials JSON)
- Normalize the data into a list of dicts matching the schema above
- Handle empty rows and malformed data gracefully

### Claude Bucketing Logic
The prompt sent to Claude should:
1. Receive the full list of HCP responses with their metadata
2. Instruct Claude to dynamically identify natural thematic buckets (no predefined categories)
3. Return a strict JSON response with this structure:

```json
{
  "buckets": [
    {
      "bucket_name": "Rep Requests",
      "description": "HCPs requesting direct contact with a sales or medical rep",
      "count": 12,
      "requests": [
        {
          "hcp_response": "Can a rep reach out to discuss...",
          "first_name": "Jane",
          "last_name": "Doe",
          "npi": "1234567890",
          "date_time": "2026-04-20T14:30:00",
          "slack_link": "https://...",
          "slack_channel": "#feedback",
          "pulse": "..."
        }
      ]
    }
  ],
  "total_requests": 47,
  "analysis_timestamp": "2026-04-24T10:00:00Z"
}
```

### Claude Prompt Template
Use this system prompt for the Claude API call:

> You are analyzing messages from healthcare professionals (HCPs) that represent unmet needs — requests for which Impiricus does not currently have an aligned product. Your job is to identify natural thematic groupings in these messages and bucket them accordingly.
>
> Rules:
> - Identify buckets dynamically based on shared intent or topic (e.g., "Rep Requests", "CME Content Needs", "Patient Resource Requests")
> - Each request must be assigned to exactly one bucket (pick the best fit)
> - Bucket names should be concise (2-4 words), title-cased, and descriptive of the underlying need
> - Preserve ALL original metadata for each request in the output
> - Aim for 4-12 buckets depending on data volume — don't over-fragment or over-consolidate
> - If a request doesn't fit a clear theme, place it in an "Other" bucket
>
> Return ONLY valid JSON matching the specified schema. No preamble, no markdown code fences.

Use Claude's JSON mode / response prefilling (`{` prefill) to guarantee clean JSON output. Handle parse errors with a retry.

### Error Handling
- If Google Sheets fetch fails → return 503 with message
- If Claude API fails → return 502 with message
- If JSON parsing fails → retry once, then return 500 with the raw response for debugging
- Log all errors to stdout with timestamps

## Frontend Requirements (React + Vite + Tailwind)

### Project Structure
frontend/
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/
│   │   ├── BucketGrid.jsx       # Main grid of bucket cards
│   │   ├── BucketCard.jsx       # Individual bucket with count + requests
│   │   ├── RequestItem.jsx      # Single HCP request display
│   │   ├── BucketChart.jsx      # Bar chart of bucket counts
│   │   ├── StatsHeader.jsx      # Total count, last refreshed, etc.
│   │   └── LoadingState.jsx
│   ├── hooks/
│   │   └── useBuckets.js        # Fetch + refresh logic
│   ├── lib/
│   │   └── api.js               # API client
│   └── index.css
├── package.json
└── vite.config.js

### UX Requirements
- **Auto-refresh on page load** — fetch buckets as soon as the app mounts
- **Loading state** — skeleton loaders while Claude analyzes (this can take 10-30s)
- **Manual refresh button** in the header (bonus)
- **Responsive** — works well on desktop, tablet, and mobile
- **Last updated timestamp** visible at the top

### Dashboard Layout

**Header Section:**
- Title: "HCP Unmet Needs Dashboard"
- Total requests count (large number)
- Total buckets count
- Last analyzed timestamp
- Refresh button

**Visualization Section:**
- Horizontal bar chart (Recharts) showing bucket name → request count, sorted descending
- Clicking a bar scrolls to / highlights that bucket below

**Buckets Grid:**
- Responsive grid (1 col mobile, 2 col tablet, 3 col desktop)
- Each BucketCard shows:
  - Bucket name (prominent)
  - Count badge (e.g., "12 requests")
  - Short description
  - Collapsible/expandable list of requests
  - Each request shows: HCP name, NPI, the response text (truncated with expand), date, and a link to the original Slack post
- Sort buckets by count descending by default; allow toggle to sort alphabetically

### Styling
- Clean, professional look — this is an internal tool for a healthcare/pharma company
- Use a neutral palette (slate/gray base) with one accent color (suggest teal or indigo)
- Count badges should be visually prominent
- Use subtle card shadows and rounded corners
- Ensure text is readable — HCP responses can be long, so use appropriate line heights and max-widths

## Environment Variables

### Backend `.env`
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_SHEETS_ID=...
GOOGLE_SHEETS_RANGE=Sheet1!A:H
GOOGLE_SERVICE_ACCOUNT_JSON=./credentials/service-account.json
CORS_ORIGINS=http://localhost:5173

### Frontend `.env`
VITE_API_BASE_URL=http://localhost:8000

## Deliverables
1. Working backend with all endpoints functional
2. Working frontend that auto-loads buckets on mount
3. `README.md` with setup instructions for both backend and frontend, including:
   - How to set up the Google service account and share the sheet with it
   - How to get the Anthropic API key
   - How to run both services locally
4. `requirements.txt` and `package.json` with pinned versions
5. Example `.env.example` files for both

## Nice-to-Haves (if time permits)
- Search/filter across all requests
- Export buckets to CSV
- Click-through to the original Slack post opens in new tab
- Dark mode toggle
- Caching layer so repeated page loads within N minutes reuse the last analysis

## Important Notes
- NPIs are PII-adjacent — don't log them unnecessarily
- The Claude call can be expensive with large datasets — consider chunking if sheet has >500 rows
- Sheet data will change over time; always fetch fresh on each `/api/buckets` call (no stale caching beyond the optional short-term cache above)