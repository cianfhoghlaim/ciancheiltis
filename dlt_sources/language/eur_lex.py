"""ciancheiltis.dlt_sources.language.eur_lex — EUR-Lex Irish-English parallel corpus.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the EU EUR-Lex
bilingual parallel corpus (Irish + English) for legal/regulatory text.
The EUR-Lex API exposes aligned CELEX documents in both languages.

Landing schema: `ciancheiltis.language.eur_lex`
- aligned_pairs: (src_text, tgt_text, src_lang, tgt_lang, doc_id, title, year)
- celex_metadata: (doc_id, title, date, sector, year)
"""
from __future__ import annotations

import os
from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client, parse_conllu_file

logger = structlog.get_logger(__name__)


EUR_LEX_API_BASE = "https://eur-lex.europa.eu/api/v1/eurlex"


@dlt.source(name="eur_lex")
def eur_lex_source(
    lang_pair: str = "ga-en",
    sector: str | None = None,
    year_from: int = 2010,
    year_to: int = 2026,
) -> DltResource:
    """EUR-Lex Irish-English parallel corpus loader.

    Args:
        lang_pair: ISO 639-1 pair (default "ga-en" for Irish-English).
        sector: Optional sector filter (e.g. "agric", "envir", "trans").
        year_from: Earliest year of documents to include.
        year_to: Latest year of documents to include.
    """
    src_lang, tgt_lang = lang_pair.split("-")

    @dlt.resource(
        name="aligned_pairs",
        write_disposition="merge",
        primary_key=["doc_id", "lang_pair"],
    )
    def aligned_pairs() -> list[dict[str, Any]]:
        client = get_http_client()
        for year in range(year_from, year_to + 1):
            params = {
                "year": year,
                "language": f"{src_lang.upper()};{tgt_lang.upper()}",
            }
            if sector:
                params["sector"] = sector
            try:
                resp = client.get(EUR_LEX_API_BASE, params=params)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                logger.warning("eur_lex.fetch_failed", year=year, error=str(e))
                continue

            for doc in data.get("docs", []):
                yield {
                    "doc_id": doc.get("celex_id"),
                    "title": doc.get("title", ""),
                    "src_text": doc.get(f"text_{src_lang}", ""),
                    "tgt_text": doc.get(f"text_{tgt_lang}", ""),
                    "src_lang": src_lang,
                    "tgt_lang": tgt_lang,
                    "lang_pair": lang_pair,
                    "year": year,
                    "sector": doc.get("sector", ""),
                    "date": doc.get("date", ""),
                    "url": doc.get("url", ""),
                }

    @dlt.resource(name="celex_metadata")
    def celex_metadata() -> list[dict[str, Any]]:
        client = get_http_client()
        for year in range(year_from, year_to + 1):
            try:
                resp = client.get(EUR_LEX_API_BASE, params={"year": year})
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                logger.warning("eur_lex.metadata_failed", year=year, error=str(e))
                continue
            for doc in data.get("docs", []):
                yield {
                    "doc_id": doc.get("celex_id"),
                    "title": doc.get("title", ""),
                    "date": doc.get("date", ""),
                    "sector": doc.get("sector", ""),
                    "year": year,
                    "url": doc.get("url", ""),
                }

    return aligned_pairs(), celex_metadata()


__all__ = ["eur_lex_source"]
