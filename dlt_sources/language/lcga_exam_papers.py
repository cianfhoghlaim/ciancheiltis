"""ciancheiltis.dlt_sources.language.lcga_exam_papers — LCGA Irish-medium school papers loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the Irish-medium
school examination papers from the Lámhleabhar na Gaeilge / Comhairle
na Gaeilge / LCGÁ archives. These are Irish-medium school-leaving
certificates used for HTR fine-tuning + bilingual alignment.

Landing schema: `ciancheiltis.language.lcga_papers`
- papers: (paper_id, year, level, subject, language, pdf_url, sha256, fetched_at)
- transcripts: (paper_id, page, language, text, confidence, ocr_engine)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


LCGA_ARCHIVE = "https://www.lcga.ie/archive"


@dlt.source(name="lcga_papers")
def lcga_exam_papers_source(
    year_from: int = 2010,
    year_to: int = 2026,
) -> DltResource:
    """LCGA Irish-medium school exam papers loader.

    Args:
        year_from: Earliest year of papers to include.
        year_to: Latest year of papers to include.
    """
    @dlt.resource(
        name="papers",
        write_disposition="merge",
        primary_key=["paper_id"],
    )
    def papers() -> list[dict[str, Any]]:
        client = get_http_client()
        for year in range(year_from, year_to + 1):
            try:
                resp = client.get(f"{LCGA_ARCHIVE}/papers/{year}", timeout=30)
                resp.raise_for_status()
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, "html.parser")
                for link in soup.select("a[href$='.pdf']"):
                    href = link.get("href", "")
                    if not href:
                        continue
                    full_url = href if href.startswith("http") else f"{LCGA_ARCHIVE}{href}"
                    yield {
                        "paper_id": f"lcga_{year}_{href.split('/')[-1].replace('.pdf', '')}",
                        "year": year,
                        "level": "higher" if "higher" in href.lower() else "ordinary",
                        "subject": "gaeilge",
                        "language": "gle",
                        "pdf_url": full_url,
                    }
            except Exception as e:
                logger.warning("lcga.fetch_failed", year=year, error=str(e))

    @dlt.resource(
        name="transcripts",
        write_disposition="merge",
        primary_key=["paper_id", "page"],
    )
    def transcripts() -> list[dict[str, Any]]:
        for paper in papers():
            # OCR would happen here via Unsloth Studio + Qwen3-VL-8B
            # For now emit placeholder
            yield {
                "paper_id": paper["paper_id"],
                "page": 1,
                "language": paper["language"],
                "text": "[OCR pending via Unsloth Studio Qwen3-VL-8B]",
                "confidence": 0.0,
                "ocr_engine": "unsloth/qwen3-vl-8b-instruct",
            }

    return papers(), transcripts()


__all__ = ["lcga_exam_papers_source"]
