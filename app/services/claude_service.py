"""Claude API service using the official Anthropic Python SDK."""

from __future__ import annotations

import anthropic

from app.config import get_settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ClaudeServiceError(Exception):
    """Raised when a Claude API call fails."""


async def ask_claude(
    system_prompt: str,
    user_prompt: str,
    *,
    max_tokens: int | None = None,
) -> str:
    """
    Send prompts to Claude and return only the generated assistant text.
    """
    settings = get_settings()
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    token_limit = max_tokens if max_tokens is not None else settings.claude_max_tokens

    logger.info(
        "Claude request started | model=%s | max_tokens=%d | system_chars=%d | user_chars=%d",
        settings.claude_model,
        token_limit,
        len(system_prompt),
        len(user_prompt),
    )

    try:
        message = await client.messages.create(
            model=settings.claude_model,
            max_tokens=token_limit,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except anthropic.AuthenticationError as exc:
        logger.error("Claude authentication failed: %s", exc)
        raise ClaudeServiceError("Invalid Anthropic API key") from exc
    except anthropic.APIStatusError as exc:
        logger.error("Claude API status error | status=%s | message=%s", exc.status_code, exc.message)
        raise ClaudeServiceError(exc.message) from exc
    except anthropic.APIError as exc:
        logger.error("Claude API error: %s", exc)
        raise ClaudeServiceError(str(exc)) from exc
    except Exception as exc:
        logger.error("Claude unexpected error: %s", exc)
        raise ClaudeServiceError(f"Claude request failed: {exc}") from exc

    text_parts = [
        block.text
        for block in message.content
        if getattr(block, "type", None) == "text" and block.text
    ]
    result = "\n".join(text_parts).strip()

    if not result:
        logger.error("Claude returned an empty response")
        raise ClaudeServiceError("Claude returned an empty response")

    logger.info("Claude request succeeded | response_chars=%d", len(result))
    return result
