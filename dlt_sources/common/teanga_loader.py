"""ciancheiltis.dlt_sources.common.teanga_loader — shared loader for parallel IR+EN corpora.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides a unified
loader interface for any teanga (language) parallel corpus: takes a
list of (source_text, target_text, language_pair) tuples and writes
them to the canonical `ciancheiltis.language.parallel_corpus` schema
in DuckLake.

This is the bridge between the various source-specific loaders
(EUR-Lex, NCCA, Wikipedia, CLARIN, UD) and the canonical alignment
pipeline (which uses fast_align + eflomal — see
`dlt_sources/language/bilingual_alignment.py`).
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

logger = structlog.get_logger(__name__)


@dlt.source(name="teanga_loader")
def teanga_loader_source(
    pairs: list[dict[str, Any]],
    schema_name: str = "parallel_corpus",
) -> DltResource:
    """Shared loader for parallel IR+EN corpora.

    Args:
        pairs: List of dicts with keys: source_text, target_text, lang_pair, source (str).
        schema_name: DuckLake schema name (default: "parallel_corpus").
    """
    @dlt.resource(
        name=schema_name,
        write_disposition="merge",
        primary_key=["source_text", "target_text", "lang_pair"],
    )
    def parallel_corpus() -> list[dict[str, Any]]:
        for pair in pairs:
            yield {
                "source_text": pair.get("source_text", ""),
                "target_text": pair.get("target_text", ""),
                "lang_pair": pair.get("lang_pair", ""),
                "source": pair.get("source", "unknown"),
                "corpus_name": pair.get("corpus_name", ""),
            }

    return parallel_corpus()


__all__ = ["teanga_loader_source"]
