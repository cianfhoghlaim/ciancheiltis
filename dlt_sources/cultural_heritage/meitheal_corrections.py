"""ciancheiltis.dlt_sources.cultural_heritage.meitheal_corrections — Meitheal Dúchas crowdsourced corrections.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the crowdsourced
corrections submitted by Meitheal Dúchas volunteers. This is the canonical
verified training data for the Irish-language HTR fine-tune.

Landing schema: `ciancheiltis.language.meitheal_corrections`
- corrections: (correction_id, page_id, volume_number, original_text, corrected_text, corrector, verified, updated_at)
- contributors: (corrector_id, name, location, total_corrections, joined_at)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


MEITHEAL_API = "https://meitheal.duchas.ie/api/v1"


@dlt.source(name="meitheal_corrections")
def meitheal_corrections_source(
    volume_from: int = 1,
    volume_to: int = 100,
) -> DltResource:
    """Meitheal Dúchas crowdsourced corrections loader.

    Args:
        volume_from: First Duchas.ie volume number.
        volume_to: Last Duchas.ie volume number.
    """
    @dlt.resource(
        name="corrections",
        write_disposition="merge",
        primary_key=["correction_id"],
    )
    def corrections() -> list[dict[str, Any]]:
        client = get_http_client()
        for vol in range(volume_from, volume_to + 1):
            try:
                resp = client.get(
                    f"{MEITHEAL_API}/corrections",
                    params={"volume": vol, "limit": 500},
                )
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                logger.warning("meitheal.fetch_failed", volume=vol, error=str(e))
                continue
            for corr in data.get("corrections", []):
                yield {
                    "correction_id": corr.get("id"),
                    "page_id": corr.get("page_id"),
                    "volume_number": vol,
                    "original_text": corr.get("original", ""),
                    "corrected_text": corr.get("corrected", ""),
                    "corrector": corr.get("corrector", ""),
                    "verified": corr.get("verified", False),
                    "updated_at": corr.get("updated_at", ""),
                }

    @dlt.resource(
        name="contributors",
        write_disposition="merge",
        primary_key=["corrector_id"],
    )
    def contributors() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{MEITHEAL_API}/contributors", params={"limit": 1000})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("meitheal.contributors_failed", error=str(e))
            return
        for contrib in data.get("contributors", []):
            yield {
                "corrector_id": contrib.get("id"),
                "name": contrib.get("name", ""),
                "location": contrib.get("location", ""),
                "total_corrections": contrib.get("count", 0),
                "joined_at": contrib.get("joined_at", ""),
            }

    return corrections(), contributors()


__all__ = ["meitheal_corrections_source"]
