"""ciancheiltis.dlt_sources.common — re-export shim.

Re-exports the 4 canonical helpers from `cianfhoghlaim.dlt_sources.common`:

- `endpoint_recovery`
- `firecrawl_source`
- `http_client`
- `destinations_cianfhoghlaim`

Per the parent change `2026-08-24-dlt-sources-to-multi-repo-scaffold-v1`
§18 (destination-versioning contract) + the v2 plan §12.5 (the destination
factory). Ciancheiltis sources depend on these helpers for the 13
`*_client()` factories + the MotherDuck / DuckLake / multischema destinations.

Today (Phase 4 init) the re-export is a lazy `__getattr__` so the import
only resolves if cianfhoghlaim is actually installed. The carved subtrees
(`language/`, `cultural_heritage/`, `lexicographic/`) import the in-tree
`_http_factories.py` shim instead, which avoids the `settings` / `shared`
runtime dependencies that the original `http_client` brings in.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cianfhoghlaim.dlt_sources.common import (  # noqa: F401
        endpoint_recovery,
        firecrawl_source,
        http_client,
        destinations_cianfhoghlaim,
    )

__all__ = [
    "endpoint_recovery",
    "firecrawl_source",
    "http_client",
    "destinations_cianfhoghlaim",
]


def __getattr__(name: str):
    if name in __all__:
        try:
            import importlib

            _common = importlib.import_module("cianfhoghlaim.dlt_sources.common")
        except ImportError as exc:
            raise ImportError(
                f"ciancheiltis.dlt_sources.common.{name} requires "
                "cianfhoghlaim to be installed. Wire the [tool.uv.sources] "
                "workspace declaration in Phase 3+ or run "
                "`uv pip install -e ../cianfhoghlaim`."
            ) from exc
        return getattr(_common, name)
    raise AttributeError(
        f"module 'ciancheiltis.dlt_sources.common' has no attribute {name!r}"
    )
