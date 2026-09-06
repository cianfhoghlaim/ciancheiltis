"""ciancheiltis.dlt_sources.language.ud_parse — Universal Dependencies parser loader.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Loads the Universal
Dependencies treebanks for the 6 Celtic languages (gle, cym, gla, bre,
cor, mnx) via UDPipe-2 REST API or direct CoNLL-U file download.

Landing schema: `ciancheiltis.language.ud_treebanks`
- treebanks: (language, treebank_id, genre, size, url, license)
- sentences: (treebank_id, sent_id, language, form, lemma, upos, feats, head, deprel, text)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import CONLLU_COLUMNS, get_http_client, parse_conllu_file

logger = structlog.get_logger(__name__)


UD_BASE_URLS = {
    "gle": "https://github.com/UniversalDependencies/UD_Irish-GTwBL/raw/master",
    "cym": "https://github.com/UniversalDependencies/UD_Welsh-CCG/raw/master",
    "gla": "https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG/raw/master",
    "bre": "https://github.com/UniversalDependencies/UD_Breton-ABTB/raw/master",
    "cor": "https://github.com/UniversalDependencies/UD_Cornish-Kertonks/raw/master",
    "mnx": "https://github.com/UniversalDependencies/UD_Manx-Cadhan/raw/master",
}


@dlt.source(name="ud_parse")
def ud_parse_source(
    languages: list[str] | None = None,
) -> DltResource:
    """UD treebank loader for the 6 Celtic languages.

    Args:
        languages: List of ISO 639-3 codes (default: all 6 Celtic).
    """
    if languages is None:
        languages = list(UD_BASE_URLS.keys())

    @dlt.resource(
        name="treebanks",
        write_disposition="merge",
        primary_key=["treebank_id"],
    )
    def treebanks() -> list[dict[str, Any]]:
        for lang in languages:
            if lang not in UD_BASE_URLS:
                logger.warning("ud.unsupported_lang", lang=lang)
                continue
            yield {
                "treebank_id": f"UD_{lang}",
                "language": lang,
                "genre": "mixed",
                "url": UD_BASE_URLS[lang],
                "license": "CC BY-SA 4.0",
            }

    @dlt.resource(
        name="sentences",
        write_disposition="merge",
        primary_key=["treebank_id", "sent_id"],
    )
    def sentences() -> list[dict[str, Any]]:
        client = get_http_client()
        for lang in languages:
            if lang not in UD_BASE_URLS:
                continue
            try:
                url = f"{UD_BASE_URLS[lang]}/ga_idt-ud-train.conllu"
                resp = client.get(url, timeout=60)
                resp.raise_for_status()
                # Save to temp file and parse
                import tempfile
                with tempfile.NamedTemporaryFile(mode="w", suffix=".conllu", delete=False) as tf:
                    tf.write(resp.text)
                    tmpfile = tf.name
                for sent in parse_conllu_file(tmpfile):
                    yield {
                        "treebank_id": f"UD_{lang}",
                        "sent_id": sent.get("metadata", {}).get("id", ""),
                        "language": lang,
                        "text": " ".join(
                            t.get("form", "") for t in sent.get("tokens", [])
                        ),
                        "tokens": sent.get("tokens", []),
                        "metadata": sent.get("metadata", {}),
                    }
                import os
                os.unlink(tmpfile)
            except Exception as e:
                logger.warning("ud.fetch_failed", lang=lang, error=str(e))

    return treebanks(), sentences()


__all__ = ["ud_parse_source"]
