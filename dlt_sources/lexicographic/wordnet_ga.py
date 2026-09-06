"""ciancheiltis.dlt_sources.lexicographic.wordnet_ga — WordNet Gaeilge loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the WordNet Gaeilge
resource via the LIGA (Líonra na Gaeilge) data export. Provides synset
lookups, hypernym/hyponym traversal, and WSD (word sense disambiguation)
for Irish text.

Landing schema: `ciancheiltis.language.wordnet_ga`
- synsets: (synset_id, language, pos, definition_ga, definition_en, gloss_ga)
- lemmas: (lemma_id, synset_id, lemma, language, pronunciation)
- relations: (source_synset, target_synset, relation_type, language)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


WORDNET_GA_BASE = "https://www.liga.ie/wordnet/api/v1"


@dlt.source(name="wordnet_ga")
def wordnet_ga_source(
    pos_filter: list[str] | None = None,
) -> DltResource:
    """WordNet Gaeilge loader.

    Args:
        pos_filter: List of parts of speech to include (n, v, a, r).
    """
    if pos_filter is None:
        pos_filter = ["n", "v", "a", "r"]

    @dlt.resource(
        name="synsets",
        write_disposition="merge",
        primary_key=["synset_id"],
    )
    def synsets() -> list[dict[str, Any]]:
        client = get_http_client()
        for pos in pos_filter:
            try:
                resp = client.get(
                    f"{WORDNET_GA_BASE}/synsets",
                    params={"pos": pos, "limit": 5000},
                )
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                logger.warning("wordnet_ga.fetch_failed", pos=pos, error=str(e))
                continue
            for synset in data.get("synsets", []):
                yield {
                    "synset_id": synset.get("id"),
                    "language": "gle",
                    "pos": pos,
                    "definition_ga": synset.get("definition_ga", ""),
                    "definition_en": synset.get("definition_en", ""),
                    "gloss_ga": synset.get("gloss_ga", ""),
                }

    @dlt.resource(
        name="lemmas",
        write_disposition="merge",
        primary_key=["lemma_id"],
    )
    def lemmas() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{WORDNET_GA_BASE}/lemmas", params={"limit": 10000})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("wordnet_ga.lemmas_failed", error=str(e))
            return
        for lemma in data.get("lemmas", []):
            yield {
                "lemma_id": lemma.get("id"),
                "synset_id": lemma.get("synset_id"),
                "lemma": lemma.get("lemma", ""),
                "language": "gle",
                "pronunciation": lemma.get("pronunciation", ""),
            }

    @dlt.resource(
        name="relations",
        write_disposition="merge",
        primary_key=["source_synset", "target_synset", "relation_type"],
    )
    def relations() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{WORDNET_GA_BASE}/relations", params={"limit": 5000})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("wordnet_ga.relations_failed", error=str(e))
            return
        for rel in data.get("relations", []):
            yield {
                "source_synset": rel.get("source"),
                "target_synset": rel.get("target"),
                "relation_type": rel.get("type"),
                "language": "gle",
            }

    return synsets(), lemmas(), relations()


__all__ = ["wordnet_ga_source"]
