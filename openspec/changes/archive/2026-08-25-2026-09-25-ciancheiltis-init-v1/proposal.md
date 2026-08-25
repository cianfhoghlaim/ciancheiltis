# 2026-09-25-ciancheiltis-init-v1

## Why

Per the v2 plan §A (the bilingual educational carve rule) + the parent change
`2026-08-24-dlt-sources-to-multi-repo-scaffold-v1` §21.3, the Ciancheiltis sister
repo carves out 3 DLT subtrees from Cianfhoghlaim:

- `dlt_sources/language/` — re-export shim (Phase 4 init: points at the ciancheiltis-owned lexicographic + cultural_heritage subtrees)
- `dlt_sources/cultural_heritage/` — Dúchas, Gaois, heritage sources
- `dlt_sources/lexicographic/` — Téarma, Ainm, Logainm, Canúint, UD sources

The bilingual educational carve rule keeps LC Gaeilge + WJEC Welsh-medium +
UoG bilingual content in Cianfhoghlaim (via Tuatha) and ships pure Irish-language
datasets + non-educational Celtic-language pipelines to Ciancheiltis.

## What changes

1. New repo: `/Users/cianmacandeisigh/dev/ciancheiltis/` — initial skeleton + 3 carved subtrees + 2 cross-repo shims (`_cross/`, `common/`).
2. Cianfhoghlaim: `dlt_sources/{language,cultural_heritage,lexicographic}/` replaced by backward-compat shims (`from ciancheiltis.dlt_sources.<subtree> import *` + `DeprecationWarning`).
3. Openspec change `2026-09-25-ciancheiltis-init-v1` documents the carve.

## Scope (Phase 4 init, today)

- Carve the 3 subtrees; mirror them at `ciancheiltis/dlt_sources/<subtree>/`.
- Wire the 5-subtree smoke test (`tests/dlt/test_imports.py`).
- Add the openspec change + tasks.
- Do NOT wire the destination-versioning contract (Phase 3 follow-up).
- Do NOT wire the per-PR reciprocal PR workflow (Phase 4 follow-up).
- Do NOT wire the BAML/Cognee/MotherDuck cascade contracts (Phase 5+).
