"""Google Sheets service: reads the HCP feedback sheet and normalizes rows."""
from __future__ import annotations

import logging
import os
from typing import Dict, List

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from models.schemas import HCPRequest

logger = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Canonical column keys mapped from the (possibly noisy) header row in the sheet.
_HEADER_ALIASES: Dict[str, str] = {
    "hcp response": "hcp_response",
    "response": "hcp_response",
    "message": "hcp_response",
    "date time": "date_time",
    "datetime": "date_time",
    "date": "date_time",
    "first name": "first_name",
    "last name": "last_name",
    "npi": "npi",
    "link to slack post": "slack_link",
    "slack link": "slack_link",
    "slack post": "slack_link",
    "slack channel name": "slack_channel",
    "slack channel": "slack_channel",
    "channel": "slack_channel",
    "pulse": "pulse",
}


class SheetsError(Exception):
    """Raised when we cannot fetch or parse the source spreadsheet."""


def _normalize_header(value: str) -> str:
    return value.strip().lower() if isinstance(value, str) else ""


def _build_service(credentials_path: str):
    if not credentials_path or not os.path.exists(credentials_path):
        raise SheetsError(
            f"Service account credentials not found at: {credentials_path}"
        )
    creds = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def fetch_hcp_requests(
    spreadsheet_id: str,
    sheet_range: str,
    credentials_path: str,
) -> List[HCPRequest]:
    """Pull rows from the configured Google Sheet and return HCPRequest objects."""
    if not spreadsheet_id:
        raise SheetsError("GOOGLE_SHEETS_ID is not configured")

    try:
        service = _build_service(credentials_path)
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=sheet_range)
            .execute()
        )
    except HttpError as exc:
        raise SheetsError(f"Google Sheets API error: {exc}") from exc
    except SheetsError:
        raise
    except Exception as exc:  # noqa: BLE001 - surface root cause
        raise SheetsError(f"Failed to read spreadsheet: {exc}") from exc

    values: List[List[str]] = result.get("values", [])
    if not values:
        logger.warning("Sheet %s returned no rows", spreadsheet_id)
        return []

    header_row = values[0]
    column_map: Dict[int, str] = {}
    for idx, raw in enumerate(header_row):
        key = _HEADER_ALIASES.get(_normalize_header(raw))
        if key:
            column_map[idx] = key

    if not column_map:
        raise SheetsError(
            "No recognizable headers in sheet. Expected columns include "
            "'HCP Response', 'Date Time', 'First Name', 'Last Name', 'NPI', "
            "'Link to Slack post', 'Slack Channel Name', 'Pulse'."
        )

    requests: List[HCPRequest] = []
    for row in values[1:]:
        if not any(cell.strip() for cell in row if isinstance(cell, str)):
            continue

        record = {field: "" for field in HCPRequest.model_fields}
        for idx, key in column_map.items():
            cell = row[idx] if idx < len(row) else ""
            record[key] = (cell or "").strip() if isinstance(cell, str) else str(cell)

        if not record.get("hcp_response"):
            continue

        try:
            requests.append(HCPRequest(**record))
        except Exception as exc:  # noqa: BLE001 - skip malformed row
            logger.warning("Skipping malformed row: %s", exc)
            continue

    logger.info("Fetched %d HCP requests from sheet", len(requests))
    return requests
