"""ciancheiltis.dlt_sources.cultural_heritage.hidden_heritages_extended — Hidden Heritage extended corpus.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Extends the existing
hidden_heritages.py with: oral histories, place-name chants, folk songs,
famine narratives, and emigration stories. These are long-form Irish
language texts that don't fit the standard Duchas.ie Schools' Collection
template but are part of the broader Irish cultural heritage.

Landing schema: `ciancheiltis.language.hidden_heritages_extended`
- oral_histories: (history_id, county, decade, summary, audio_url, transcript_url)
- place_name_chants: (chant_id, location, lat, lon, transcript_ga, transcript_en)
- folk_songs: (song_id, title_ga, region, audio_url, lyrics_ga, lyrics_en)
- famine_narratives: (narrative_id, county, year, family_name, transcript, language)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


HIDDEN_HERITAGE_API = "https://hiddenheritage.duchas.ie/api/v1"


@dlt.source(name="hidden_heritages_extended")
def hidden_heritages_extended_source() -> DltResource:
    """Hidden Heritage extended corpus loader."""

    @dlt.resource(
        name="oral_histories",
        write_disposition="merge",
        primary_key=["history_id"],
    )
    def oral_histories() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{HIDDEN_HERITAGE_API}/oral_histories", params={"limit": 500})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("hidden_heritage.oral_failed", error=str(e))
            return
        for h in data.get("oral_histories", []):
            yield {
                "history_id": h.get("id"),
                "county": h.get("county", ""),
                "decade": h.get("decade", ""),
                "summary": h.get("summary", ""),
                "audio_url": h.get("audio_url", ""),
                "transcript_url": h.get("transcript_url", ""),
            }

    @dlt.resource(
        name="place_name_chants",
        write_disposition="merge",
        primary_key=["chant_id"],
    )
    def place_name_chants() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{HIDDEN_HERITAGE_API}/place_name_chants", params={"limit": 1000})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("hidden_heritage.chants_failed", error=str(e))
            return
        for c in data.get("chants", []):
            yield {
                "chant_id": c.get("id"),
                "location": c.get("location", ""),
                "lat": c.get("lat", 0.0),
                "lon": c.get("lon", 0.0),
                "transcript_ga": c.get("transcript_ga", ""),
                "transcript_en": c.get("transcript_en", ""),
            }

    @dlt.resource(
        name="folk_songs",
        write_disposition="merge",
        primary_key=["song_id"],
    )
    def folk_songs() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{HIDDEN_HERITAGE_API}/folk_songs", params={"limit": 500})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("hidden_heritage.songs_failed", error=str(e))
            return
        for s in data.get("songs", []):
            yield {
                "song_id": s.get("id"),
                "title_ga": s.get("title_ga", ""),
                "region": s.get("region", ""),
                "audio_url": s.get("audio_url", ""),
                "lyrics_ga": s.get("lyrics_ga", ""),
                "lyrics_en": s.get("lyrics_en", ""),
            }

    @dlt.resource(
        name="famine_narratives",
        write_disposition="merge",
        primary_key=["narrative_id"],
    )
    def famine_narratives() -> list[dict[str, Any]]:
        client = get_http_client()
        try:
            resp = client.get(f"{HIDDEN_HERITAGE_API}/famine_narratives", params={"limit": 200})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("hidden_heritage.famine_failed", error=str(e))
            return
        for n in data.get("narratives", []):
            yield {
                "narrative_id": n.get("id"),
                "county": n.get("county", ""),
                "year": n.get("year", 0),
                "family_name": n.get("family_name", ""),
                "transcript": n.get("transcript", ""),
                "language": n.get("language", "gle"),
            }

    return oral_histories(), place_name_chants(), folk_songs(), famine_narratives()


__all__ = ["hidden_heritages_extended_source"]
