"""ciancheiltis.dlt_sources.language.clarin — CLARIN corpus loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the CLARIN-UK
and CLARIN-Ireland curated corpora via the Centre for Language Technology
(CLT) and the CLARIN Virtual Language Observatory (VLO).

Landing schema: `ciancheiltis.language.clarin`
- corpora: (corpus_id, language, title, description, size, url, license)
- texts: (corpus_id, text_id, language, content, metadata)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


CLARIN_VLO_API = "https://vlo.clarin.eu/api/v1"


@dlt.source(name="clarin")
def clarin_source(
    language: str = "gle",
    max_corpora: int = 50,
) -> DltResource:
    """CLARIN-UK + CLARIN-Ireland corpus loader.

    Args:
        language: ISO 639-3 code (default "gle" for Irish).
        max_corpora: Maximum number of corpora to fetch.
    """
    @dlt.resource(
        name="corpora",
        write_disposition="merge",
        primary_key=["corpus_id"],
    )
    def corpora() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(
                f"{CLARIN_VLO_API}/search",
                params={"q": f"language:{language}", "limit": max_corpora},
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("clarin.fetch_failed", language=language, error=str(e))
            return

        for item in data.get("results", []):
            yield {
                "corpus_id": item.get("id"),
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "language": language,
                "size": item.get("size", 0),
                "url": item.get("landing_page", ""),
                "license": item.get("licence", ""),
            }

    return corpora()


__all__ = ["clarin_source"]
