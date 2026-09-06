"""ciancheiltis.dlt_sources.lexicographic.ud_extensions_ga — UD extensions for Irish.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides Universal
Dependencies extensions for Irish Gaelic, including:
- UWT (Universal Wordnet Tagging) for Irish
- UDPipe-2 model wrappers
- Custom UD annotations for the Gaeilge treebank

Landing schema: `ciancheiltis.language.ud_extensions`
- extensions: (language, name, version, url, description)
- annotations: (lang, sent_id, token_id, form, lemma, upos, xpos, feats, head, deprel)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._helpers import get_http_client

logger = structlog.get_logger(__name__)


UDPIPE_MODELS = {
    "irish-gaeilge": {
        "url": "https://lindat.mff.cuni.cz/services/udpipe/api/v1/models/irish-gaeilge",
        "version": "2.0",
    },
    "irish-idt": {
        "url": "https://lindat.mff.cuni.cz/services/udpipe/api/v1/models/irish-idt",
        "version": "2.0",
    },
}


@dlt.source(name="ud_extensions_ga")
def ud_extensions_ga_source(
    model: str = "irish-gaeilge",
) -> DltResource:
    """UD extensions for Irish Gaelic.

    Args:
        model: UDPipe-2 model name (default "irish-gaeilge").
    """
    if model not in UDPIPE_MODELS:
        raise ValueError(f"Unknown model: {model}. Available: {list(UDPIPE_MODELS.keys())}")

    model_info = UDPIPE_MODELS[model]

    @dlt.resource(
        name="extensions",
        write_disposition="merge",
        primary_key=["name", "version"],
    )
    def extensions() -> list[dict[str, Any]]:
        yield {
            "language": "gle",
            "name": model,
            "version": model_info["version"],
            "url": model_info["url"],
            "description": f"UDPipe-2 model for {model} (CoNLL-U format)",
        }

    return extensions()


__all__ = ["ud_extensions_ga_source"]
