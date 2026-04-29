"""Pydantic models describing the API surface."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class RoadmapItem(BaseModel):
    """A single roadmap initiative parsed from `roadmap.md`."""

    key: str = Field(default="")  # e.g. "PROD-201"
    title: str = Field(default="")
    url: str = Field(default="")
    initiative: str = Field(default="")
    status: str = Field(default="")
    # Optional short rationale Claude provides explaining WHY this roadmap
    # item is a good match for the request. Empty when surfaced as a raw
    # roadmap item (e.g. in /api/diagnostics).
    rationale: str = Field(default="")


class HCPRequest(BaseModel):
    """Single message sourced from the Google Sheet or Slack."""

    hcp_response: str = Field(default="")
    first_name: str = Field(default="")
    last_name: str = Field(default="")
    npi: str = Field(default="")
    date_time: Optional[str] = Field(default=None)
    slack_link: str = Field(default="")
    slack_channel: str = Field(default="")
    pulse: str = Field(default="")
    # Stable identifier so bucketed copies can be re-linked to the original
    # (and so we can deduplicate Slack publishes across runs).
    request_id: str = Field(default="")
    # Slack message timestamp, populated only for Slack-sourced rows. Used to
    # post the unmet-need acknowledgement as a thread reply on the original.
    slack_ts: str = Field(default="")
    # Roadmap items Claude identified as relevant to this request. Filled in
    # AFTER bucketing by the alignment pass; empty during bucketing.
    roadmap_alignments: List[RoadmapItem] = Field(default_factory=list)
    # True when no roadmap item matches this request (i.e. genuine gap).
    # Derived from `roadmap_classification == "gap"` — kept on the model for
    # convenience in the frontend.
    unaligned: bool = Field(default=False)
    # Anna McDermott's roadmap-comparison schema, surfaced live on the
    # dashboard. All four fields are populated by services/alignment.py.
    roadmap_classification: str = Field(default="")  # "covered" | "partial" | "gap" | ""
    gap_category: str = Field(default="")  # content-gap / channel-gap / data-gap / workflow-gap / cross-product-gap
    confidence: str = Field(default="")  # "high" | "medium" | "low" | ""
    roadmap_reasoning: str = Field(default="")  # 1-2 sentence justification


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
