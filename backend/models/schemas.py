"""Pydantic models describing the API surface."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class HCPRequest(BaseModel):
    """Single message sourced from the Google Sheet."""

    hcp_response: str = Field(default="")
    first_name: str = Field(default="")
    last_name: str = Field(default="")
    npi: str = Field(default="")
    date_time: Optional[str] = Field(default=None)
    slack_link: str = Field(default="")
    slack_channel: str = Field(default="")
    pulse: str = Field(default="")


class Bucket(BaseModel):
    """A thematic grouping of HCP requests as identified by Claude."""

    bucket_name: str
    description: str = ""
    count: int = 0
    requests: List[HCPRequest] = Field(default_factory=list)


class BucketsResponse(BaseModel):
    """Top-level response for the /api/buckets endpoint."""

    buckets: List[Bucket]
    total_requests: int
    analysis_timestamp: datetime


class HealthResponse(BaseModel):
    status: str = "ok"
    timestamp: datetime
