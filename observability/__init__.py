"""ciancheiltis.observability — minimal logging shim for the carved DLT sources.

The original `cianfhoghlaim.observability` module lives at the cianfhoghlaim
root + provides structured-logging helpers (`get_logger`, `add_environment`,
`configure_logging`, etc.) over `structlog`. The carved subtrees under
`dlt_sources/{language,cultural_heritage,lexicographic}/` reference
`from observability.logging import get_logger` (a legacy import path).

Rather than wholesale-copy the full cianfhoghlaim observability tree
(~1.2k LOC) into ciancheiltis, this shim provides ONLY the `get_logger`
helper that the carved DLT sources actually use. New code in ciancheiltis
should import `structlog` directly + follow the standard structlog idiom:

    import structlog
    logger = structlog.get_logger(__name__)

The shim preserves the legacy `observability.logging.get_logger` path so
the carved source files do not need per-file import rewrites — they
import the shim instead. Phase 4 follow-up: rewrite the carved source
files to use structlog directly + delete this shim.
"""
