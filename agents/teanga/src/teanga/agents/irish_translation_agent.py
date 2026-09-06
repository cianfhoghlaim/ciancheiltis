"""ciancheiltis.agents.teanga.irish_translation_agent — EN ↔ GA translation.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Uses Unsloth Qwen3.8-27B
for bilingual translation. Part of the ciancheiltis teanga agent fleet.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.gaelic_translate import gaelic_translate

config = TeangaConfig.from_env()


irish_translation_agent = LlmAgent(
    name="irish_translation_agent",
    model=config.litellm.resolve_model("text_llm", "translation"),
    description=(
        "Bilingual English ↔ Irish (Gaeilge) translation agent. Uses "
        "Unsloth Qwen3.8-27B for high-quality translation between English "
        "and Irish. Supports full bilingual EN+GA surface with context-aware "
        "translation."
    ),
    instruction=(
        "You are the Irish (Gaeilge) translation agent. When the user "
        "provides text in English or Irish, translate it to the other "
        "language using the gaelic_translate tool. Preserve formatting, "
        "handle idioms carefully, and provide cultural context when relevant."
    ),
    tools=[gaelic_translate],
)


async def run_irish_translate(
    text: str, source_lang: str, target_lang: str
) -> dict[str, Any]:
    """Run bilingual EN↔GA translation."""
    return await gaelic_translate(text, source_lang, target_lang)


__all__ = ["irish_translation_agent", "run_irish_translate"]
