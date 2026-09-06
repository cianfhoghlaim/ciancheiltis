"""ciancheiltis.agents.teanga.gaelic_lexicographer_agent — Lexicon lookup agent.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Looks up lemmas,
definitions, and translations across Foclóir, gaois, tearma, ainm,
canuint, and the WordNet Gaeilge resource.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.lexicographer import lexicographer_lookup

config = TeangaConfig.from_env()


gaelic_lexicographer_agent = LlmAgent(
    name="gaelic_lexicographer_agent",
    model=config.litellm.resolve_model("text_llm", "lexicon"),
    description=(
        "Gaelic lexicographer agent. Looks up lemmas, definitions, and "
        "translations across Foclóir, gaois, tearma, ainm, canuint, and "
        "the WordNet Gaeilge resource. Provides citation + morphological "
        "info for each lookup."
    ),
    instruction=(
        "You are the Gaelic lexicographer agent. When the user provides a "
        "word in Irish, Welsh, Scottish Gaelic, Breton, Cornish, or Manx, "
        "look it up in the canonical lexicon and return: lemma, definition, "
        "POS, citations, and cross-language translations. Use the "
        "lexicographer_lookup tool."
    ),
    tools=[lexicographer_lookup],
)


async def run_lex_lookup(word: str, lang: str) -> dict[str, Any]:
    """Look up a word in the lexicon."""
    return await lexicographer_lookup(word, lang)


__all__ = ["gaelic_lexicographer_agent", "run_lex_lookup"]
