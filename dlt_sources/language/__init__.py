"""ciancheiltis.dlt_sources.language — re-export shim.

Per the bilingual educational carve rule (v2 plan §A + parent change
`2026-08-24-dlt-sources-to-multi-repo-scaffold-v1` §21.3):

- `dlt_sources.lexicographic/` — carved to Ciancheiltis
- `dlt_sources.cultural_heritage/` — carved to Ciancheiltis
- `dlt_sources.local_archive/` — STAYS in Cianfhoghlaim (per the carve rule,
   because local_archive contains education-curriculum-referenced sources)

This shim re-exports the 2 carved sub-packages for backwards compatibility.
The cianfhoghlaim-side `dlt_sources/language/__init__.py` retains the
full 3-package re-export for backwards compat (it pulls local_archive
from cianfhoghlaim proper).
"""
from dlt_sources.lexicographic import *  # noqa: F401,F403
from dlt_sources.cultural_heritage import *  # noqa: F401,F403
