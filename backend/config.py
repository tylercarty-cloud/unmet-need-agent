"""Application configuration loaded from environment variables."""
from __future__ import annotations

from functools import lru_cache
from typing import Annotated, List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    anthropic_model: str = Field(default="claude-opus-4-5", alias="ANTHROPIC_MODEL")

    google_sheets_id: str = Field(default="", alias="GOOGLE_SHEETS_ID")
    google_sheets_range: str = Field(default="Sheet1!A:H", alias="GOOGLE_SHEETS_RANGE")
    google_service_account_json: str = Field(
        default="./credentials/service-account.json",
        alias="GOOGLE_SERVICE_ACCOUNT_JSON",
    )

    slack_bot_token: str = Field(default="", alias="SLACK_BOT_TOKEN")
    slack_channel_id: str = Field(default="", alias="SLACK_CHANNEL_ID")
    slack_message_limit: int = Field(default=1000, alias="SLACK_MESSAGE_LIMIT")
    slack_publish_enabled: bool = Field(default=True, alias="SLACK_PUBLISH_ENABLED")
    slack_publish_state_path: str = Field(
        default="./data/posted_requests.json",
        alias="SLACK_PUBLISH_STATE_PATH",
    )
    dashboard_url: str = Field(default="http://localhost:5173", alias="DASHBOARD_URL")

    roadmap_path: str = Field(default="./roadmap.md", alias="ROADMAP_PATH")
    alignment_enabled: bool = Field(default=True, alias="ALIGNMENT_ENABLED")

    cors_origins: Annotated[List[str], NoDecode] = Field(
        default_factory=lambda: ["http://localhost:5173"],
        alias="CORS_ORIGINS",
    )
    cache_ttl_seconds: int = Field(default=0, alias="CACHE_TTL_SECONDS")

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_cors(cls, value):
        if isinstance(value, str):
            return [v.strip() for v in value.split(",") if v.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
