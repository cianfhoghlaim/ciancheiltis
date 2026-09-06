"""ciancheiltis.agents.teanga.toponym_resolution_agent — Irish place name resolution.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Resolves Irish place
names via the Logainm API. Provides the canonical Irish form, English
equivalent, county, GPS coordinates, and historical context.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.toponym_resolver import toponym_resolve

config = TeangaConfig.from_env()


toponym_resolution_agent = LlmAgent(
    name="toponym_resolution_agent",
    model=config.litellm.resolve_model("text_llm", "toponym"),
    description=(
        "Irish toponym resolution agent. Resolves Irish place names via "
        "the Logainm API. Returns the canonical Irish form, English "
        "equivalent, county, GPS coordinates, and historical context."
    ),
    instruction=(
        "You are the Irish toponym resolution agent. When the user provides "
        "a place name (in Irish or English), look it up in Logainm and "
        "return: canonical Irish form, English equivalent, county, "
        "GPS coordinates, historical context, and any alternate names. "
        "Use the toponym_resolve tool."
    ),
    tools=[toponym_resolve],
)


async def run_toponym(name: str) -> dict[str, Any]:
    """Resolve a place name."""
    return await toponym_resolve(name)


__all__ = ["toponym_resolution_agent", "run_toponym"]
