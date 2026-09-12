"""Teanga (Celtic language) ADK configuration.

Per the `2026-09-06-ciancheiltis-v1` umbrella, the Teanga ADK agents
(`celtic_corpus_search`, `gaelic_lexicographer`, `duchas_htr`,
`toponym_resolution`, `ncca_syllabus_lookup`, `irish_translation`)
read their model assignment + jurisdiction scope from this config.

Status: STUB. The real config (LiteLLM-resolved models per jurisdiction)
ships when the umbrella's Phase 2 lands.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class TeangaConfig:
    """Resolved ADK config for the Teanga Celtic language agent fleet."""

    worker_model: str = "gemini/gemini-2.5-flash"
    orchestrator_model: str = "gemini/gemini-2.5-pro"
    jurisdictions: tuple[str, ...] = field(
        default_factory=lambda: (
            "ireland", "scotland", "wales", "cornwall",
            "isle_of_man", "brittany",
        )
    )
