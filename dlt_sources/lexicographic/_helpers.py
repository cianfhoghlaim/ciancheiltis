"""Shared helpers re-export for the lexicographic DLT surface.

The canonical implementations live in `dlt_sources/language/_helpers.py`
(per the `2026-09-06-ciancheiltis-v1` umbrella). This file re-exports
just the names that `lexicographic/*.py` uses so the import contract
`from ._helpers import get_http_client, wikipedia_search` resolves
locally.
"""

from dlt_sources.language._helpers import (  # noqa: F401
    get_http_client,
    wikipedia_search,
)

__all__ = ["get_http_client", "wikipedia_search"]
