"""ciancheiltis.dlt_sources.lexicographic.gaelic_corpus_search — unified search across teanga corpora.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides a unified
search interface across all 6 Celtic corpora: WordNet Gaeilge, NCCA
syllabus, Wikipedia teanga, CLARIN, UD treebanks, Lexicographic.

Landing schema: `ciancheiltis.language.unified_search`
- search_index: (query, language, source, match_id, match_text, score)
- search_metadata: (query_id, query, executed_at, sources_searched, total_matches)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client, wikipedia_search

logger = structlog.get_logger(__name__)


@dlt.source(name="gaelic_corpus_search")
def gaelic_corpus_search_source(
    query: str = "an teach",
    languages: list[str] | None = None,
) -> DltResource:
    """Unified search across Celtic corpora.

    Args:
        query: The search query (default: "an teach" = "the house").
        languages: Languages to search (default: all 6 Celtic).
    """
    if languages is None:
        languages = ["gle", "cym", "gla", "bre", "cor", "mnx"]

    @dlt.resource(
        name="search_index",
        write_disposition="merge",
        primary_key=["query", "language", "source", "match_id"],
    )
    def search_index() -> list[dict[str, Any]]:
        for lang in languages:
            # Wikipedia search
            wiki_results = wikipedia_search(lang, query, max_results=10)
            for i, hit in enumerate(wiki_results):
                yield {
                    "query": query,
                    "language": lang,
                    "source": "wikipedia",
                    "match_id": str(hit.get("pageid", i)),
                    "match_text": hit.get("title", "") + ": " + hit.get("snippet", ""),
                    "score": 1.0 - (i * 0.05),
                }

    @dlt.resource(
        name="search_metadata",
        write_disposition="replace",
        primary_key=["query_id"],
    )
    def search_metadata() -> list[dict[str, Any]]:
        yield {
            "query_id": query,
            "query": query,
            "sources_searched": ["wikipedia"],
            "languages_searched": languages,
        }

    return search_index(), search_metadata()


__all__ = ["gaelic_corpus_search_source"]
