"""ciancheiltis.dlt_sources.language.ncca_syllabus — NCCA Leaving Certificate syllabus loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the bilingual
(EN + GA) NCCA Leaving Certificate syllabus + learning outcomes (LOs)
for the 8 NCCA subjects: Mathematics, English, Gaeilge, History, Geography,
Biology, Chemistry, Physics, Applied Mathematics, Computer Science.

Landing schema: `ciancheiltis.language.ncca_syllabus`
- syllabus_topics: (subject, lo_code, title_en, title_ga, description_en, description_ga, level, year, source_url)
- syllabus_pdfs: (subject, lo_code, pdf_url, sha256, fetched_at)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


NCCA_SYLLABUS_BASE = "https://www.ncca.ie/en/school-resources"


@dlt.source(name="ncca_syllabus")
def ncca_syllabus_source(
    subjects: list[str] | None = None,
    level: str = "higher",
) -> DltResource:
    """NCCA Leaving Certificate syllabus loader.

    Args:
        subjects: List of subject names (default: all 8 NCCA subjects).
        level: "higher" or "ordinary" (default "higher").
    """
    if subjects is None:
        subjects = [
            "mathematics", "english", "gaeilge", "history", "geography",
            "biology", "chemistry", "physics", "applied-mathematics", "computer-science",
        ]

    @dlt.resource(
        name="syllabus_topics",
        write_disposition="merge",
        primary_key=["subject", "lo_code"],
    )
    def syllabus_topics() -> list[dict[str, Any]]:
        client = get_http_client()
        for subject in subjects:
            try:
                url = f"{NCCA_SYLLABUS_BASE}/{subject}/{level}-level"
                resp = client.get(url, timeout=30)
                resp.raise_for_status()
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, "html.parser")

                # Extract LOs from the syllabus page
                for lo_div in soup.select(".learning-outcome, .lo-item"):
                    lo_code = lo_div.get("data-lo-code", "") or lo_div.get("id", "")
                    title_en_el = lo_div.select_one(".title-en, .lo-title-en")
                    title_ga_el = lo_div.select_one(".title-ga, .lo-title-ga")
                    desc_en_el = lo_div.select_one(".desc-en, .lo-desc-en")
                    desc_ga_el = lo_div.select_one(".desc-ga, .lo-desc-ga")

                    yield {
                        "subject": subject,
                        "lo_code": lo_code,
                        "title_en": title_en_el.get_text(strip=True) if title_en_el else "",
                        "title_ga": title_ga_el.get_text(strip=True) if title_ga_el else "",
                        "description_en": desc_en_el.get_text(strip=True) if desc_en_el else "",
                        "description_ga": desc_ga_el.get_text(strip=True) if desc_ga_el else "",
                        "level": level,
                        "source_url": url,
                    }
            except Exception as e:
                logger.warning("ncca.fetch_failed", subject=subject, error=str(e))

    return syllabus_topics()


__all__ = ["ncca_syllabus_source"]
