"""Application configuration via environment variables."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = PROJECT_ROOT / "prompts"

VALID_AGENTS = frozenset(
    {"ceo", "sales", "finance", "marketing", "customer_success", "hr"}
)


class Settings(BaseSettings):
    """Central configuration loaded from environment / .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = "Bitrix24 Claude Integration"
    app_env: Literal["development", "staging", "production"] = "development"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Bitrix24
    bitrix24_webhook_url: str = Field(
        ...,
        description="Incoming webhook URL for Bitrix24 REST API",
    )

    # Anthropic
    anthropic_api_key: str = Field(..., description="Anthropic API key for Claude")
    claude_model: str = "claude-sonnet-4-6"
    claude_max_tokens: int = 4096

    # Telegram
    telegram_bot_token: str = Field(..., description="Telegram Bot API token")
    telegram_chat_id: str = Field(..., description="Target chat ID for reports")

    # Scheduler
    daily_report_enabled: bool = True
    daily_report_hour: int = Field(9, ge=0, le=23)
    daily_report_minute: int = Field(0, ge=0, le=59)
    daily_report_timezone: str = "Asia/Tashkent"
    daily_report_agent: str = "ceo"

    # Bitrix24 fetch limits
    bitrix_leads_limit: int = Field(50, ge=1, le=500)
    bitrix_deals_limit: int = Field(50, ge=1, le=500)
    bitrix_contacts_limit: int = Field(50, ge=1, le=500)
    bitrix_tasks_limit: int = Field(50, ge=1, le=500)

    # Claude.ai connector (optional)
    connector_secret: str = Field(
        default="",
        description="Optional secret for /tools/* and /claude/* (except /claude/health)",
    )
    public_base_url: str = Field(
        default="",
        description="Public base URL for connector manifest (e.g. https://your-app.onrender.com)",
    )

    @field_validator("bitrix24_webhook_url")
    @classmethod
    def validate_bitrix_url(cls, value: str) -> str:
        value = value.strip().rstrip("/")
        if not value.startswith("https://"):
            raise ValueError("BITRIX24_WEBHOOK_URL must be an HTTPS URL")
        return value

    @field_validator("daily_report_agent")
    @classmethod
    def validate_daily_agent(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized not in VALID_AGENTS:
            raise ValueError(
                f"daily_report_agent must be one of: {', '.join(sorted(VALID_AGENTS))}"
            )
        return normalized


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
