"""ciancheiltis.dlt_sources.common.huggingface_factory — HuggingFace dataset factory.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. Provides a factory
for loading HuggingFace datasets for teanga sources, including
teanga/gaelic, teanga/celtic, and the Tríonóidí Tíreolaíochta Gaeltachta.

Landing schema: `ciancheiltis.language.huggingface`
- datasets: (dataset_id, language, description, size, license, url)
- configs: (dataset_id, config_name, split, num_examples, features)
"""
from __future__ import annotations

from typing import Any

import dlt
import structlog
from dlt.sources import DltResource

from ._duckdb_helpers import get_duckdb_connection

logger = structlog.get_logger(__name__)


@dlt.source(name="huggingface")
def huggingface_factory_source(
    dataset_name: str,
    config_name: str | None = None,
    split: str = "train",
) -> DltResource:
    """HuggingFace dataset factory loader for teanga sources.

    Args:
        dataset_name: The HuggingFace dataset name (e.g. "teanga/gaelic-corpus").
        config_name: Optional config name within the dataset.
        split: Dataset split to load (default "train").
    """
    @dlt.resource(
        name="configs",
        write_disposition="merge",
        primary_key=["dataset_id", "config_name", "split"],
    )
    def configs() -> list[dict[str, Any]]:
        try:
            from datasets import load_dataset
            dataset = load_dataset(dataset_name, config_name, split=split, streaming=True)
            yield {
                "dataset_id": dataset_name,
                "config_name": config_name or "default",
                "split": split,
                "num_examples": dataset.info.splits[split].num_examples if hasattr(dataset.info, 'splits') else 0,
                "features": str(dataset.info.features) if hasattr(dataset.info, 'features') else "",
            }
        except Exception as e:
            logger.warning("huggingface.load_failed", dataset=dataset_name, error=str(e))

    return configs()


__all__ = ["huggingface_factory_source"]
