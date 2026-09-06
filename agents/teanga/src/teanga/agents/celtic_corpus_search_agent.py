"""ciancheiltis.agents.teanga.celtic_corpus_search_agent — unified CLARIN + UD + Wikipedia search.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Unified search across
the 6 Celtic language corpora via CLARIN Virtual Language Observatory
(VLO), Universal Dependencies treebanks, and the 6 Wikipedia APIs.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.celtic_corpus_search import celtic_corpus_search

config = TeangaConfig.from_env()


celtic_corpus_search_agent = LlmAgent(
    name="celtic_corpus_search_agent",
    model=config.litellm.resolve_model("text_llm", "search"),
    description=(
        "Unified search agent across the 6 Celtic language corpora: "
        "CLARIN-UK + CLARIN-Ireland VLO, Universal Dependencies treebanks "
        "(6 languages), and the 6 Wikipedia APIs (gle, cym, gla, bre, cor, "
        "mnx). Returns ranked results across all sources."
    ),
    instruction=(
        "You are the Celtic corpus search agent. When the user provides a "
        "search query, search CLARIN + UD + Wikipedia for the 6 Celtic "
        "languages and return ranked results. Use the celtic_corpus_search "
        "tool. Cross-reference the results across sources for the best answer."
    ),
    tools=[celtic_corpus_search],
)


async def run_celtic_search(query: str, language: str = "all") -> list[dict[str, Any]]:
    """Search the Celtic corpora."""
    return await celtic_corpus_search(query, language)


__all__ = ["celtic_corpus_search_agent", "run_celtic_search"]
