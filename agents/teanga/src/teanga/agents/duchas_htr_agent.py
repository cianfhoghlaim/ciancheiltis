"""ciancheiltis.agents.teanga.duchas_htr_agent — HTR for Duchas.ie manuscript transcriptions.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Performs handwritten
text recognition (HTR) on Duchas.ie IIIF manuscript images using
Unsloth Qwen3-VL-8B-Instruct. Produces TEI-XML transcriptions aligned
to the page bounding boxes.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.duchas_htr import duchas_htr_transcribe

config = TeangaConfig.from_env()


duchas_htr_agent = LlmAgent(
    name="duchas_htr_agent",
    model=config.litellm.resolve_model("ocr_vision", "htr"),
    description=(
        "Duchas.ie HTR agent. Performs handwritten text recognition (HTR) "
        "on Duchas.ie IIIF manuscript page images using Unsloth "
        "Qwen3-VL-8B-Instruct. Produces TEI-XML transcriptions aligned "
        "to page bounding boxes, with confidence scores per word."
    ),
    instruction=(
        "You are the Duchas HTR agent. When the user provides a Duchas.ie "
        "IIIF page URL + volume + page numbers, transcribe the handwritten "
        "text on each page using the duchas_htr_transcribe tool. Return "
        "TEI-XML + per-word confidence. Validate against the Meitheal "
        "crowdsourced corrections when available."
    ),
    tools=[duchas_htr_transcribe],
)


async def run_duchas_htr(
    page_urls: list[str], volume_number: int
) -> list[dict[str, Any]]:
    """Transcribe Duchas.ie pages via HTR."""
    return await duchas_htr_transcribe(page_urls, volume_number)


__all__ = ["duchas_htr_agent", "run_duchas_htr"]
