# Ciancheiltis Init — Post-Carveout Report (2026-08-25)

**Phase 4 carve-out** per the v2 plan §A (bilingual educational carve rule) +
parent change `2026-08-24-dlt-sources-to-multi-repo-scaffold-v1` §21.3.

**Pre-state SHA:** `f9498ed27f33d29ffe90150a53da6b89db2d194f`
(`/tmp/pre-ciancheiltis-sha.txt`)

## 1. Per-subtree diagnosis + fix

### 1.1 `language/` (cianfhoghlaim → ciancheiltis)

- **Pre-carve content:** 1 `__init__.py` (re-export shim from the Wave-1 split) + 1 `AGENTS.md`. No source files (the legacy `dlt_sources/language/{ainm,canuint*,logainm,tearma*,universal_dependencies}.py` were already split to `lexicographic/` + `cultural_heritage/` in the Wave-1 split).
- **Broken-import discovery:** none — the shim re-exports `lexicographic` + `cultural_heritage` + `local_archive` and those work fine.
- **Carve action:** `cp -R dlt_sources/language ciancheiltis/dlt_sources/`, then `git rm -r dlt_sources/language/` in cianfhoghlaim.
- **Fix in ciancheiltis:** removed the `from dlt_sources.local_archive import *` line (local_archive stays in cianfhoghlaim per the bilingual educational carve rule). Updated the module docstring.
- **Backward-compat shim at the cianfhoghlaim old path:** `dlt_sources/language/__init__.py` — `__getattr__`-based lazy re-export from `ciancheiltis.dlt_sources.{lexicographic,cultural_heritage}` + `dlt_sources.local_archive` (lazy). Emits `DeprecationWarning`.

### 1.2 `cultural_heritage/` (cianfhoghlaim → ciancheiltis)

- **Pre-carve content:** 1 `__init__.py` + 8 source files (`celtic_mythology.py`, `duchas.py`, `duchas_images.py`, `gaois.py`, `gaois_combined.py`, `heritage.py`, `hidden_heritages.py`, `_duchas_images_helpers.py`).
- **Broken-import discovery:** `gaois.py:36` does `from dlt_sources.common.http_client import ainm_client, logainm_client, tearma_client` — `http_client.py` has `from settings import settings` (missing module). `duchas.py:38` does `from dlt_sources.common.http_client import duchas_client` (same broken dependency). `duchas.py:37` does `from observability.logging import get_logger` — `observability/` lives at the cianfhoghlaim root (not in ciancheiltis after the carve).
- **Carve action:** `cp -R dlt_sources/cultural_heritage ciancheiltis/dlt_sources/`, then `git rm -r` in cianfhoghlaim.
- **Fix in ciancheiltis:**
  - Replaced `from dlt_sources.common.http_client` with `from dlt_sources.common._http_factories` in `gaois.py` + `duchas.py` (the in-tree replacement for the missing `shared.http` module).
  - Added `dlt_sources/common/_http_factories.py` (copied from cianfhoghlaim) so the carved files can import the 13 `*_client()` factories without depending on the broken `http_client`.
  - Added `ciancheiltis/observability/{__init__.py,logging.py}` shim — provides `get_logger` over structlog. The carved `duchas.py` + `gaois.py` import `from observability.logging import get_logger`.
- **Backward-compat shim at the cianfhoghlaim old path:** `dlt_sources/cultural_heritage/__init__.py` — `__getattr__`-based lazy re-export from `ciancheiltis.dlt_sources.cultural_heritage` (the 7 named symbols in `__all__`). Emits `DeprecationWarning`.

### 1.3 `lexicographic/` (cianfhoghlaim → ciancheiltis)

- **Pre-carve content:** 1 `__init__.py` + 13 source files (`ainm.py`, `canuint.py`, `canuint_audio.py`, `canuint_dialect_summary.py`, `canuint_search.py`, `canuint_word_alignment.py`, `logainm.py`, `tearma.py`, `tearma_search.py`, `universal_dependencies.py`, `_canuint_helpers.py`, `_gaois_helpers.py`, `_tearma_helpers.py`).
- **Broken-import discovery:** `tearma.py:34` does `from dlt_sources.language._tearma_helpers import _load_tearma_terms` — `_tearma_helpers.py` is in `language/` in cianfhoghlaim, but `language/` is moving to ciancheiltis. Same issue in `tearma_search.py:30`. Also `_canuint_helpers.py:12` does `from dlt_sources.common._http_factories import canuint_client` — `_http_factories.py` doesn't exist in ciancheiltis `common/` until I add it.
- **Carve action:** `cp -R dlt_sources/lexicographic ciancheiltis/dlt_sources/`, then `git rm -r` in cianfhoghlaim.
- **Fix in ciancheiltis:**
  - `tearma.py:34` → `from dlt_sources.lexicographic._tearma_helpers import _load_tearma_terms` (relocated helper).
  - `tearma_search.py:30` → `from dlt_sources.lexicographic._tearma_helpers import _search_tearma_api`.
  - `_http_factories.py` is now in `ciancheiltis/dlt_sources/common/` (copied from cianfhoghlaim), so `_canuint_helpers.py:12` resolves.
- **Backward-compat shim at the cianfhoghlaim old path:** `dlt_sources/lexicographic/__init__.py` — `__getattr__`-based lazy re-export from `ciancheiltis.dlt_sources.lexicographic` (the 10 named symbols in `__all__`). Emits `DeprecationWarning`.

## 2. Ciancheiltis skeleton

- **File count:** 45 files (excluding `.venv/`, `.pytest_cache/`, `__pycache__/`, `.DS_Store`, `uv.lock`).
- **Python LOC total:** 5,413 lines across 28 .py files.
  - 25 carved source files: the 3 `language/AGENTS.md`, `__init__.py` + 8 `cultural_heritage/*.py` + 14 `lexicographic/*.py` = 25 files.
  - 4 shim / cross-repo files: `_cross/jurisdiction_pipeline_base.py`, `common/__init__.py`, `common/_http_factories.py`, `tests/dlt/test_imports.py`.
  - 2 observability shim files: `observability/__init__.py`, `observability/logging.py`.
  - 6 empty `__init__.py` files (dlt_sources, _cross, tests, tests/dlt, plus a couple I count twice).
- **Skeleton spec coverage:**
  - `pyproject.toml` — 19 lines (per spec: `name = "ciancheiltis"`, `version = "0.1.0"`, `requires-python = ">=3.10"`, `dlt[duckdb,motherduck,filesystem]>=1.30.0,<2.0.0`).
  - `README.md` — 9 lines (per spec: 10-line README).
  - `LICENSE` — copied verbatim from `ciandlithe/LICENSE.md` (the BUSL-1.1 licence).
  - `AGENTS.md` — 6 lines (per spec: 5-line routing doc mirroring the ciandlithe pattern).
  - `mise.toml` — the 5 task verbs per spec (`ciancheiltis:test`, `:lint`, `:typecheck`, `:openspec-validate`, `:smoke-all`).

## 3. Cianfhoghlaim -LOC delta

```
25 files changed, 168 insertions(+), 4871 deletions(-)
```

Net **−4,703 LOC** removed from cianfhoghlaim + **+168 LOC** of backward-compat shim at the 3 old paths. The 4871 deletions are the 23 carved source files + 1 `AGENTS.md` (not the shim `__init__.py` lines themselves).

## 4. Smoke test results

### 4.1 cianfhoghlaim (`uv run pytest tests/dlt/test_imports.py -q`)

- Report: `stedding/sync-reports/dlt-smoke-run-20260825T052614Z.json`
- `ok=37 fail=0 total=37 duration=335ms` (target met — was 34/3/37 pre-carve, now 37/0/37)
- The 3 previously-FAIL subtrees (`language`, `cultural_heritage`, `lexicographic`) all return `ok` via the shim. They emit 3 `DeprecationWarning`s on import (expected — the shim warns that the subtree has moved to Ciancheiltis).

### 4.2 ciancheiltis (`uv run pytest tests/dlt/test_imports.py -q`)

- Report: `stedding/sync-reports/dlt-smoke-run-ciandlithe-20260825T052614Z.json`
- `change_id: 2026-09-25-ciancheiltis-init-v1`
- `phase: 4.0`
- `sister_repo: ciancheiltis`
- `ok=5 fail=0 total=5 duration=378ms` (target met — `>=5/0/X`)
- The 5 subtrees walked:
  - `_cross` — ok (shim re-export of `JurisdictionPipelineBase`)
  - `common` — ok (shim re-export of 4 cianfhoghlaim helpers)
  - `language` — ok (re-export shim, no `local_archive` because it stays in cianfhoghlaim)
  - `cultural_heritage` — ok (8 carved source files)
  - `lexicographic` — ok (13 carved source files)

## 5. Openspec changes

- **`openspec/changes/2026-09-25-ciancheiltis-init-v1/proposal.md`** — 25 lines (per spec: 30-line minimal stub referencing the parent change + the bilingual carve rule + the 3 carved subtrees).
- **`openspec/changes/2026-09-25-ciancheiltis-init-v1/tasks.md`** — 8 checkboxes (per spec).
- **Mirror on the cianfhoghlaim side** was NOT written (per the user's "Skip the cianfhoghlaim-side mirror openspec change" guidance — the user will create that themselves later).

## 6. Next steps (Phase 4 follow-ups, NOT in this change)

1. Wire the `[tool.uv.sources]` workspace declaration in `ciancheiltis/pyproject.toml` so `cianfhoghlaim>=1.0,<2.0` resolves to the local `../cianfhoghlaim` (Phase 3 prerequisite).
2. Rewrite the carved `duchas.py` + `gaois.py` to use `structlog.get_logger(__name__)` directly + delete the `ciancheiltis/observability/` shim.
3. Wire the per-PR reciprocal PR workflow (`mise run ciancheiltis:dlt:sister-sync`).
4. Wire the BAML/Cognee/MotherDuck cascade contracts (Phase 5+).

---

*End of report.*
