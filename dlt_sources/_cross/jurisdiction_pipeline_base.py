"""ciancheiltis.dlt_sources._cross.jurisdiction_pipeline_base — re-export shim.

Re-exports `JurisdictionPipelineBase` from
`cianfhoghlaim.dlt_sources.british_isles._cross.jurisdiction_pipeline_base`
so any Ciancheiltis pipeline that needs the canonical per-jurisdiction +
per-nation DLT source contract can `from ciancheiltis.dlt_sources._cross
import JurisdictionPipelineBase` once cianfhoghlaim is installed (Phase 3+).

Today (Phase 4 init) the re-export is a lazy `__getattr__` so the import
only resolves if cianfhoghlaim is actually installed. This lets the
per-repo smoke test pass without forcing a workspace dependency.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cianfhoghlaim.dlt_sources.british_isles._cross.jurisdiction_pipeline_base import (  # noqa: F401
        JurisdictionPipelineBase,
    )

__all__ = ["JurisdictionPipelineBase"]


def __getattr__(name: str):
    if name == "JurisdictionPipelineBase":
        try:
            from cianfhoghlaim.dlt_sources.british_isles._cross.jurisdiction_pipeline_base import (  # noqa: F401
                JurisdictionPipelineBase as _JPB,
            )
        except ImportError as exc:
            raise ImportError(
                "JurisdictionPipelineBase requires cianfhoghlaim to be "
                "installed. Wire the [tool.uv.sources] workspace "
                "declaration in Phase 3+ or run "
                "`uv pip install -e ../cianfhoghlaim`."
            ) from exc
        return _JPB
    raise AttributeError(
        f"module 'ciancheiltis.dlt_sources._cross.jurisdiction_pipeline_base' "
        f"has no attribute {name!r}"
    )
