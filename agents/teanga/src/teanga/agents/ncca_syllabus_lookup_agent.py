"""ciancheiltis.agents.teanga.ncca_syllabus_lookup_agent — NCCA syllabus LO lookup.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Looks up Learning
Outcomes (LOs) in the NCCA Leaving Certificate syllabus. Bilingual
EN+GA support.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.ncca_syllabus_lookup import ncca_syllabus_lookup

config = TeangaConfig.from_env()


ncca_syllabus_lookup_agent = LlmAgent(
    name="ncca_syllabus_lookup_agent",
    model=config.litellm.resolve_model("text_llm", "ncca"),
    description=(
        "NCCA syllabus LO lookup agent. Looks up Learning Outcomes (LOs) "
        "in the NCCA Leaving Certificate syllabus across all 8 NCCA "
        "subjects. Bilingual EN+GA support."
    ),
    instruction=(
        "You are the NCCA syllabus lookup agent. When the user provides a "
        "subject + LO code (e.g., 'mathematics LO-1.1.1') or a topic query, "
        "return: the LO code, title (EN + GA), description (EN + GA), "
        "level (higher/ordinary), and any cross-references. Use the "
        "ncca_syllabus_lookup tool."
    ),
    tools=[ncca_syllabus_lookup],
)


async def run_ncca_lookup(
    subject: str, lo_code: str = "", topic: str = ""
) -> dict[str, Any]:
    """Look up an NCCA LO."""
    return await ncca_syllabus_lookup(subject, lo_code, topic)


__all__ = ["ncca_syllabus_lookup_agent", "run_ncca_lookup"]
