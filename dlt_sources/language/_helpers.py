"""ciancheiltis.dlt_sources.language._helpers — shared utilities for teanga DLT sources.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides:
- IIIF download helpers (duchas.ie manuscript images)
- TEI-XML parser for Duchas transcriptions
- ISO 639-3 language code validation
- UD treebank loader (CoNLL-U format)
- Wikipedia API helpers (MediaWiki)
- Bilingual sentence alignment helpers
"""
from __future__ import annotations

import os
import re
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import httpx
import structlog

logger = structlog.get_logger(__name__)


# Common HTTP client (cached across sources)
_http_client: httpx.Client | None = None


def get_http_client() -> httpx.Client:
    """Get a shared httpx client for all teanga sources."""
    global _http_client
    if _http_client is None:
        timeout = int(os.environ.get("CIANCHEILTIS_HTTP_TIMEOUT", "30"))
        _http_client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={"User-Agent": "ciancheiltis-teanga/0.2.0 (ducklake-ingest)"},
        )
    return _http_client


# === IIIF helpers (Duchas.ie manuscript images) ===

IIIF_INFO_RE = re.compile(r'\{\s*"@context"\s*:\s*"http://iiif.io/api/image/2\.0/context\.json"')
IIIF_TILE_SIZE_RE = re.compile(r'/(?:full|\d+,\d+|\d+,|,)/0/default\.(?:jpg|png)$')


def get_iiif_dimensions(client: httpx.Client, image_url: str) -> tuple[int, int]:
    """Fetch image dimensions from IIIF info.json endpoint.

    Args:
        client: httpx client.
        image_url: IIIF image URL (e.g. /iiif/v2/<id>/full/full/0/default.jpg).

    Returns:
        (width, height) tuple. Returns (0, 0) on failure.
    """
    try:
        info_url = image_url.rsplit("/", 1)[0] + "/info.json"
        resp = client.get(info_url)
        resp.raise_for_status()
        info = resp.json()
        return info.get("width", 0), info.get("height", 0)
    except Exception as e:
        logger.warning("iiif.info_failed", url=image_url, error=str(e))
        return 0, 0


def parse_iiif_url(image_url: str) -> dict[str, Any]:
    """Parse a IIIF image URL into its components.

    Returns:
        Dict with keys: base_uri, region, size, rotation, quality, format.
    """
    parts = image_url.rsplit("/", 5)
    if len(parts) < 6:
        return {}
    base_uri, region, size, rotation, quality, fmt = parts[:6]
    return {
        "base_uri": base_uri,
        "region": region,
        "size": size,
        "rotation": rotation,
        "quality": quality,
        "format": fmt,
    }


# === TEI-XML helpers (Duchas transcriptions) ===

TEI_NS = {"tei": "http://www.tei-c.org/ns/1.0"}


def parse_tei_xml_transcription(tei_xml: str) -> dict[str, Any]:
    """Parse a TEI-XML transcription into a flat dict.

    Args:
        tei_xml: The TEI-XML string.

    Returns:
        Dict with keys: text (flat string), lines (list of line dicts), language (ISO 639-3).
    """
    try:
        root = ET.fromstring(tei_xml)
    except ET.ParseError as e:
        logger.warning("tei.parse_failed", error=str(e))
        return {"text": "", "lines": [], "language": ""}

    # Extract language
    lang = root.get("{http://www.w3.org/XML/1998/namespace}lang", "")

    # Extract lines
    lines = []
    for line_el in root.iter("{http://www.tei-c.org/ns/1.0}lb"):
        line_id = line_el.get("{http://www.w3.org/XML/1998/namespace}id", "")
        line_text = "".join(line_el.itertext()).strip()
        if line_text:
            lines.append({"id": line_id, "text": line_text})

    # Extract full text
    text = "".join(root.itertext()).strip()

    return {"text": text, "lines": lines, "language": lang}


# === ISO 639-3 helpers ===

ISO_6393_GAELIC = {
    "gle",  # Irish (Gaeilge)
    "cym",  # Welsh (Cymraeg)
    "gla",  # Scottish Gaelic
    "bre",  # Breton
    "cor",  # Cornish
    "mnx",  # Manx
    "lat",  # Latin (for the historical records)
    "eng",  # English
    "fra",  # French (for EU sources)
    "deu",  # German
    "spa",  # Spanish
}


def is_gaelic_lang(lang_code: str) -> bool:
    """Check if a language code is one of the canonical Celtic/Gaelic languages."""
    return lang_code.lower() in ISO_6393_GAELIC


def validate_lang_code(lang_code: str) -> str:
    """Validate + normalize an ISO 639-3 language code. Returns '' if invalid."""
    if not lang_code:
        return ""
    code = lang_code.lower().strip()
    if code in ISO_6393_GAELIC:
        return code
    logger.warning("language.unknown_code", code=code)
    return code


# === UD treebank helpers (CoNLL-U format) ===

CONLLU_COLUMNS = ["id", "form", "lemma", "upos", "xpos", "feats", "head", "deprel", "deps", "misc"]


def parse_conllu_file(filepath: str) -> Iterator[dict[str, Any]]:
    """Parse a CoNLL-U file and yield sentence dicts.

    Each sentence has:
    - metadata: dict of # key=value lines
    - tokens: list of token dicts (one per CoNLL-U row)
    """
    sentence: dict[str, Any] = {"metadata": {}, "tokens": []}

    with open(filepath, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                if sentence["tokens"] or sentence["metadata"]:
                    yield sentence
                    sentence = {"metadata": {}, "tokens": []}
                continue
            if line.startswith("#"):
                if "=" in line:
                    key, _, value = line[1:].partition("=")
                    sentence["metadata"][key.strip()] = value.strip()
                continue
            fields = line.split("\t")
            if len(fields) >= 10:
                token = dict(zip(CONLLU_COLUMNS, fields[:10]))
                sentence["tokens"].append(token)

    if sentence["tokens"] or sentence["metadata"]:
        yield sentence


# === Wikipedia API helpers (MediaWiki) ===

WIKIPEDIA_API_BASE = "https://{lang}.wikipedia.org/w/api.php"


def wikipedia_search(
    lang_code: str, query: str, max_results: int = 10
) -> list[dict[str, Any]]:
    """Search Wikipedia for a query in the given language.

    Returns:
        List of dicts with keys: title, pageid, snippet.
    """
    base = WIKIPEDIA_API_BASE.format(lang=lang_code)
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srlimit": max_results,
        "format": "json",
    }
    try:
        client = get_http_client()
        resp = client.get(base, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("query", {}).get("search", [])
    except Exception as e:
        logger.warning("wikipedia.search_failed", lang=lang_code, error=str(e))
        return []


# === Bilingual sentence alignment helpers ===

def extract_sentences(text: str, lang_code: str) -> list[str]:
    """Extract sentences from text using a simple heuristic.

    For more sophisticated tokenization, use UDPipe.
    """
    # Split on period, exclamation, question mark followed by space
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


def compute_alignment_score(src: list[str], tgt: list[str]) -> float:
    """Compute a simple length-ratio based alignment quality score.

    Returns:
        1.0 = perfect, 0.0 = no alignment.
    """
    if not src or not tgt:
        return 0.0
    src_words = sum(len(s.split()) for s in src)
    tgt_words = sum(len(s.split()) for s in tgt)
    if src_words == 0 or tgt_words == 0:
        return 0.0
    ratio = min(src_words, tgt_words) / max(src_words, tgt_words)
    return ratio


__all__ = [
    "get_http_client",
    "get_iiif_dimensions",
    "parse_iiif_url",
    "parse_tei_xml_transcription",
    "ISO_6393_GAELIC",
    "is_gaelic_lang",
    "validate_lang_code",
    "CONLLU_COLUMNS",
    "parse_conllu_file",
    "WIKIPEDIA_API_BASE",
    "wikipedia_search",
    "extract_sentences",
    "compute_alignment_score",
]
