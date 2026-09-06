"""ciancheiltis.dlt_sources.language.wikipedia_teanga — Wikipedia Irish + Celtic API loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the Irish (gle),
Welsh (cym), Scottish Gaelic (gla), Breton (bre), Cornish (cor), and
Manx (mnx) Wikipedia APIs via the MediaWiki REST v1 endpoint.

Landing schema: `ciancheiltis.language.wikipedia`
- pages: (lang_code, page_id, title, summary, full_text, url, fetched_at)
- categories: (lang_code, page_id, category)
- links: (lang_code, page_id, link_target, link_lang)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client, wikipedia_search

logger = structlog.get_logger(__name__)


WIKIPEDIA_LANGS = ["gle", "cym", "gla", "bre", "cor", "mnx"]


@dlt.source(name="wikipedia_teanga")
def wikipedia_teanga_source(
    queries: list[str] | None = None,
    langs: list[str] | None = None,
    max_pages_per_query: int = 5,
) -> DltResource:
    """Wikipedia Irish + Celtic corpus loader.

    Args:
        queries: List of search queries (default: "Ireland", "Gaeilge", "Cymru", etc.)
        langs: List of ISO 639-3 codes (default: 6 Celtic languages).
        max_pages_per_query: Max pages to fetch per query.
    """
    if queries is None:
        queries = [
            "Ireland", "Gaeilge", "Cymru", "Welsh language", "Scottish Gaelic",
            "Breton language", "Cornish language", "Manx language", "Celtic nations",
        ]
    if langs is None:
        langs = WIKIPEDIA_LANGS

    @dlt.resource(
        name="pages",
        write_disposition="merge",
        primary_key=["lang_code", "page_id"],
    )
    def pages() -> list[dict[str, Any]]:
        for lang_code in langs:
            for query in queries:
                results = wikipedia_search(lang_code, query, max_results=max_pages_per_query)
                for hit in results:
                    page_id = hit.get("pageid")
                    if not page_id:
                        continue
                    full_text = _fetch_page(lang_code, page_id)
                    if not full_text:
                        continue
                    yield {
                        "lang_code": lang_code,
                        "page_id": page_id,
                        "title": hit.get("title", ""),
                        "summary": hit.get("snippet", ""),
                        "full_text": full_text,
                        "url": f"https://{lang_code}.wikipedia.org/wiki/{hit.get('title', '').replace(' ', '_')}",
                        "query": query,
                    }

    @dlt.resource(
        name="categories",
        write_disposition="merge",
        primary_key=["lang_code", "page_id", "category"],
    )
    def categories() -> list[dict[str, Any]]:
        for lang_code in langs:
            for query in queries:
                results = wikipedia_search(lang_code, query, max_results=3)
                for hit in results:
                    page_id = hit.get("pageid")
                    if not page_id:
                        continue
                    for cat in _fetch_categories(lang_code, page_id):
                        yield {"lang_code": lang_code, "page_id": page_id, "category": cat}

    return pages(), categories()


def _fetch_page(lang_code: str, page_id: int) -> str:
    """Fetch the full text of a Wikipedia page."""
    try:
        client = get_http_client()
        params = {
            "action": "query",
            "prop": "extracts",
            "pageids": page_id,
            "explaintext": True,
            "format": "json",
        }
        resp = client.get(
            f"https://{lang_code}.wikipedia.org/w/api.php", params=params
        )
        resp.raise_for_status()
        data = resp.json()
        pages = data.get("query", {}).get("pages", {})
        if pages:
            page = list(pages.values())[0]
            return page.get("extract", "")
    except Exception as e:
        logger.warning("wikipedia.page_fetch_failed", page_id=page_id, error=str(e))
    return ""


def _fetch_categories(lang_code: str, page_id: int) -> list[str]:
    """Fetch the categories of a Wikipedia page."""
    try:
        client = get_http_client()
        params = {
            "action": "query",
            "prop": "categories",
            "pageids": page_id,
            "format": "json",
        }
        resp = client.get(
            f"https://{lang_code}.wikipedia.org/w/api.php", params=params
        )
        resp.raise_for_status()
        data = resp.json()
        pages = data.get("query", {}).get("pages", {})
        if pages:
            page = list(pages.values())[0]
            return [c.get("title", "") for c in page.get("categories", [])]
    except Exception:
        return []
    return []


__all__ = ["wikipedia_teanga_source"]
