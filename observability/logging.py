"""ciancheiltis.observability.logging — backwards-compat alias for the carved DLT sources.

The original `cianfhoghlaim.observability.logging` module lives at the
cianfhoghlaim repo root + provides the full observability surface
(`get_logger`, `add_environment`, `configure_logging`, `LogContext`,
`log_operation`). This shim re-exports `get_logger` (a minimal structlog
wrapper) so the carved source files under
`dlt_sources/{language,cultural_heritage,lexicographic}/` that do
`from observability.logging import get_logger` continue to work without
forcing a wholesale copy of the full cianfhoghlaim observability tree.

See `ciancheiltis.observability.__init__.py` for the design rationale.
"""

from __future__ import annotations

import structlog


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Return a structlog bound logger with the given name.

    Drop-in replacement for `cianfhoghlaim.observability.logging.get_logger`.
    Mirrors the production observability's `get_logger` contract: returns
    a `structlog.stdlib.BoundLogger` ready to receive structured key-value
    pairs (`logger.info("event_name", key=value, ...)`).
    """
    return structlog.get_logger(name)


__all__ = ["get_logger"]
