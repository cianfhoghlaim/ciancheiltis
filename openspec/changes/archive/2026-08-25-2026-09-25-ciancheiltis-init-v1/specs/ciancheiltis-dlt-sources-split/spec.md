# Spec delta — `ciancheiltis` DLT Sources Split v1

> **Parent change**: [`2026-08-24-dlt-sources-to-multi-repo-scaffold-v1`](../../../../../2026-08-24-dlt-sources-to-multi-repo-scaffold-v1/proposal.md) §21.3
> **Companion plan**: [`openspec/plans/2026-08-24-dlt-deep-analysis-v2.md`](../../../../../plans/2026-08-24-dlt-deep-analysis-v2.md) §Phase 4 + §A (the bilingual educational carve rule)
> **Capability spec**: this is a **CAPABILITY** spec (per the openspec convention), describing the end state of the `ciancheiltis-init-v1` carve-out.
> **Status**: ACTIVE (the skeleton is wired; Phase 5+ source wire-up is deferred).

## Purpose

This spec captures the end state that the `2026-09-25-ciancheiltis-init-v1` change must produce:

1. **`ciancheiltis` is a NEW sister repo** at `/Users/cianmacandeisigh/dev/ciancheiltis/` that did not exist before this change. The repo owns the Irish + Celtic languages + cultural-heritage vertical per the user-confirmed bilingual educational carve rule (Q3 + Q5).

2. **Three subtrees are carved from cianfhoghlaim → ciancheiltis**:
   - `dlt_sources/language/` — the canonical home for pure Irish-language datasets (Logainm, Téarma, Ainm, Gaois, Dúchas, Canúint, UD variants)
   - `dlt_sources/cultural_heritage/` — Celtic heritage sources (Dúchas-as-dataset, hidden_heritages, local_* heritage files)
   - `dlt_sources/lexicographic/` — lexicographic helpers (the `_tearma_helpers.py` relocation)

3. **Three backward-compat shims at the old cianfhoghlaim paths** emit `DeprecationWarning` + lazy `__getattr__` re-export from ciancheiltis, so any consumer that still imports `dlt_sources.language.X` continues to work (with a warning).

4. **The bilingual educational carve rule is honoured**: LC Gaeilge (in `tuatha/subjects/gaeilge.py`) + WJEC Welsh-medium (`british_isles/wales/education/`) + UoG bilingual (`filesystem/uog_personal_archive.py` + `filesystem/leabharlann_books.py` + `api_sources/leabharlann_education_notes.py`) STAY in cianfhoghlaim. Only pure-language datasets + non-educational Celtic-language pipelines move to ciancheiltis.

5. **The 6 cascade contracts from the parent change are wired for ciancheiltis identically to ciandlíthe + cianchosaint**:
   - openspec cascade (the openspec change itself)
   - dlt-source cascade (the per-PR reciprocal mirror workflow)
   - schema cascade (BAML placeholders created in `ciancheiltis/baml_src/`)
   - destination cascade (`cianfhoghlaim >=1.0,<2.0` pin in `ciancheiltis/pyproject.toml`)
   - observability cascade (`ciancheiltis/observability.py` for Langfuse + MLflow)
   - knowledge-graph cascade (the 6 per-cluster Cognee twins — `ciancheiltis_dlt_sources` + 5 others)

## Background

Per `openspec/plans/2026-08-24-dlt-deep-analysis-v2.md` §A, the bilingual educational carve rule resolves every grey-area DLT source. Pure Irish-language datasets + non-educational Celtic-language pipelines go to ciancheiltis; LC Gaeilge + WJEC Welsh-medium + UoG bilingual content stays in cianfhoghlaim.

The carve-out affects exactly 3 cianfhoghlaim subtrees: `language/`, `cultural_heritage/`, `lexicographic/`. The remaining 37 cianfhoghlaim subtrees are unaffected.

## ADDED Requirements

### Requirement: Ciancheiltis is the canonical home for pure Irish-language datasets + non-educational Celtic-language pipelines

The CIANCHEILTIS sister repo SHALL own the `language/`, `cultural_heritage/`, and `lexicographic/` DLT subtrees as the canonical home for pure Irish-language datasets (per the bilingual educational carve rule).

#### Scenario: A consumer queries the canonical pure-Irish-language dataset

- **GIVEN** the `ciancheiltis-init-v1` change has been archived
- **AND** the 3 subtrees are at `ciancheiltis/dlt_sources/{language,cultural_heritage,lexicographic}/`
- **WHEN** a consumer queries the canonical pure-Irish-language dataset (Logainm, Téarma, Ainm, Gaois, Dúchas, Canúint, UD-Irish)
- **THEN** the consumer SHALL import from `ciancheiltis.dlt_sources.language` (the canonical home)
- **AND** the canonical home SHALL expose:
  - `tearma.py` + `_tearma_helpers.py` — the Téarma dataset
  - `logainm.py` — the Logainm placenames dataset
  - `gaois.py` + `_gaois_helpers.py` — the Gaois dataset
  - `duchas.py` + `_duchas_images_helpers.py` — the Dúchas dataset
  - `canuint.py` + 5 submodules — the Canúint dialect dataset
  - `ainm.py` — the Ainm names dataset
  - `heritage.py` + `hidden_heritages.py` + 4 local_* files — the heritage dataset

#### Scenario: The ciancheiltis smoke test passes

- **GIVEN** the ciancheiltis-init-v1 carve-out is complete
- **WHEN** `cd /Users/cianmacandeisigh/dev/ciancheiltis && uv run pytest tests/dlt/test_imports.py -q`
- **THEN** the smoke test SHALL pass with **5 OK / 0 FAIL / 5 total** (the 5 subtrees: `_cross`, `common`, `language`, `cultural_heritage`, `lexicographic`)

### Requirement: The 3 backward-compat shims at the cianfhoghlaim old paths

The CIANFHGLAIM main repo SHALL provide 3 backward-compat shims at the old `dlt_sources/{language,cultural_heritage,lexicographic}/` paths. Each shim SHALL emit a `DeprecationWarning` + lazy `__getattr__` re-export from ciancheiltis.

#### Scenario: A consumer still imports from the old cianfhoghlaim path

- **GIVEN** a consumer has `from dlt_sources.language.X import Y` in their code (the legacy path)
- **WHEN** the consumer's code runs
- **THEN** the import SHALL succeed (the `__getattr__` in the shim re-exports from ciancheiltis)
- **AND** a `DeprecationWarning` SHALL be emitted with the message `dlt_sources.language has moved to the ciancheiltis sister repo. Update your imports to from ciancheiltis.dlt_sources.language import <symbol>. See openspec/changes/2026-09-25-ciancheiltis-init-v1/proposal.md for the carve-out plan + the bilingual educational carve rule.`
- **AND** the consumer's import path keeps working for at least 1 release cycle (per the deprecation convention)

#### Scenario: The cianfhoghlaim smoke test post-carve-out passes

- **GIVEN** the ciancheiltis-init-v1 carve-out is complete
- **WHEN** `cd /Users/cianmacandeisigh/dev/cianfhoghlaim && uv run pytest tests/dlt/test_imports.py -q`
- **THEN** the smoke test SHALL pass with **37 OK / 0 FAIL / 37 total** (the 37 subtrees: all 34 unchanged + the 3 shimmed subtrees `language`, `cultural_heritage`, `lexicographic` now pass via the `__getattr__` re-export)

### Requirement: The bilingual educational carve rule is honoured

The CIANCHEILTIS carve-out SHALL NOT touch any of the following 4 cianfhoghlaim subtrees (which stay in cianfhoghlaim per the bilingual educational carve rule):

1. `british_isles/ireland/education/subjects/gaeilge/` — the LC Gaeilge NCCA subject package
2. `british_isles/wales/education/` — the WJEC Welsh-medium pipeline
3. `filesystem/uog_personal_archive.py` + `filesystem/university_of_galway.py` + `filesystem/leabharlann_books.py` + `api_sources/leabharlann_education_notes.py` — the University of Galway bilingual content
4. `tuatha/subjects/gaeilge.py` — the LC Gaeilge subject agent in the already-carved `tuatha/` sub-project

#### Scenario: The LC Gaeilge subject remains in cianfhoghlaim

- **GIVEN** the ciancheiltis-init-v1 carve-out is complete
- **WHEN** a consumer queries the LC Gaeilge subject agent at `tuatha/subjects/gaeilge.py` (in cianfhoghlaim)
- **THEN** the consumer's import SHALL succeed (no `ModuleNotFoundError`)
- **AND** the LC Gaeilge subject SHALL reference the canonical `UD/ud_irish` corpus via the versioned `ciar://ciancheiltis/datasets/ud_irish@v<N>` URI contract (not as an embedded copy)

#### Scenario: The WJEC Welsh-medium pipeline remains in cianfhoghlaim

- **GIVEN** the ciancheiltis-init-v1 carve-out is complete
- **WHEN** a consumer queries the WJEC Welsh-medium pipeline at `british_isles/wales/education/`
- **THEN** the consumer's import SHALL succeed (no `ModuleNotFoundError`)
- **AND** the WJEC Welsh-medium pipeline SHALL reference the canonical `UD/ud_welsh` corpus via the versioned `ciar://ciancheiltis/datasets/ud_welsh@v<N>` URI contract

### Requirement: The 6 cascade contracts are wired for ciancheiltis

The CIANCHEILTIS sister repo SHALL be wired into the same 6 cascade contracts as ciandlíthe + cianchosaint:

1. **openspec cascade** — the openspec change `2026-09-25-ciancheiltis-init-v1` is the entry point
2. **dlt-source cascade** — `pyproject.toml` pins `cianfhoghlaim >=1.0,<2.0`
3. **schema cascade** — `baml_src/` placeholders for `ExtractTermFrequency` + `ExtractWordAlignment` + `ExtractDialectSummary` + `ExtractPlacenameOrigin`
4. **destination cascade** — per-sister `dlt:destination-validate` CI gate
5. **observability cascade** — `ciancheiltis/observability.py` for Langfuse + MLflow
6. **knowledge-graph cascade** — 6 per-cluster Cognee twins (`ciancheiltis_dlt_sources` + 5 others)

#### Scenario: The ciancheiltis pyproject.toml pins cianfhoghlaim

- **WHEN** the consumer inspects `/Users/cianmacandeisigh/dev/ciancheiltis/pyproject.toml`
- **THEN** the `[project]` section SHALL declare `dependencies = ["cianfhoghlaim>=1.0,<2.0", ...]`
- **AND** the `[tool.uv.sources]` section SHALL point at the local `../../cianfhoghlaim` path (per the uv workspace member pattern)

#### Scenario: The ciancheiltis mise.toml has the per-sister task namespace

- **WHEN** the consumer inspects `/Users/cianmacandeisigh/dev/ciancheiltis/mise.toml`
- **THEN** the file SHALL declare the per-sister task namespace (`ciancheiltis:test`, `ciancheiltis:lint`, `ciancheiltis:typecheck`, `ciancheiltis:openspec-validate`, `ciancheiltis:smoke-all`)
- **AND** each task SHALL mirror the canonical pattern from ciandlíthe/mise.toml + cianchosaint/mise.toml