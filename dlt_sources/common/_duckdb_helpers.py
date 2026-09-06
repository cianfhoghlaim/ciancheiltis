"""ciancheiltis.dlt_sources.common._duckdb_helpers — DuckLake migration helpers.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides:
- DuckLake table creation helpers
- Connection pool management
- Bulk insert helpers
- Migration verification
"""
from __future__ import annotations

import os
from typing import Any

import duckdb
import structlog

logger = structlog.get_logger(__name__)


DEFAULT_DUCKLAKE_PATH = os.environ.get(
    "CIANCHEILTIS_DUCKLAKE_PATH", "md:cianfhoghlaim"
)


def get_duckdb_connection(
    ducklake_path: str = DEFAULT_DUCKLAKE_PATH,
    read_only: bool = False,
) -> duckdb.DuckDBPyConnection:
    """Get a DuckDB connection for DuckLake operations.

    Args:
        ducklake_path: The DuckLake catalog path.
        read_only: Whether to open in read-only mode.
    """
    conn = duckdb.connect(":memory:")
    if not read_only:
        conn.execute(f"ATTACH '{ducklake_path}' AS ciancheiltis (READ_WRITE)")
    else:
        conn.execute(f"ATTACH '{ducklake_path}' AS ciancheiltis (READ_ONLY)")
    conn.execute("USE ciancheiltis")
    return conn


def create_language_namespace(
    schema: str = "ciancheiltis.language",
) -> bool:
    """Create the canonical ciancheiltis.language DuckLake schema."""
    try:
        conn = get_duckdb_connection()
        conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
        logger.info("duckdb.namespace_created", schema=schema)
        return True
    except Exception as e:
        logger.error("duckdb.namespace_failed", schema=schema, error=str(e))
        return False


def verify_table_exists(
    table: str,
    schema: str = "ciancheiltis.language",
) -> bool:
    """Verify a table exists in the given schema."""
    try:
        conn = get_duckdb_connection(read_only=True)
        result = conn.execute(
            f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = ? AND table_name = ?",
            [schema, table],
        ).fetchone()
        return result[0] > 0
    except Exception as e:
        logger.error("duckdb.verify_failed", table=table, error=str(e))
        return False


def bulk_insert(
    table: str,
    records: list[dict[str, Any]],
    schema: str = "ciancheiltis.language",
) -> int:
    """Bulk insert records into a table. Returns number of rows inserted."""
    if not records:
        return 0
    try:
        conn = get_duckdb_connection()
        columns = list(records[0].keys())
        col_list = ", ".join(columns)
        placeholders = ", ".join(["?" for _ in columns])
        rows = [[r.get(c) for c in columns] for r in records]
        conn.executemany(
            f"INSERT INTO {schema}.{table} ({col_list}) VALUES ({placeholders})",
            rows,
        )
        logger.info("duckdb.bulk_inserted", table=table, count=len(records))
        return len(records)
    except Exception as e:
        logger.error("duckdb.bulk_insert_failed", table=table, error=str(e))
        return 0


__all__ = [
    "DEFAULT_DUCKLAKE_PATH",
    "get_duckdb_connection",
    "create_language_namespace",
    "verify_table_exists",
    "bulk_insert",
]
