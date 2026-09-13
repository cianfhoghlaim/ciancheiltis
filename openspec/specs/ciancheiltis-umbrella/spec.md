# ciancheiltis-umbrella Specification

## Purpose

The `ciancheiltis-umbrella` spec defines the 6-phase Celtic-language coverage of the
`ciancheiltis` sister repo. Each phase pairs an English-facing ADK agent with one
Celtic language (Cornish, Irish, Northern Irish, Scottish Gaelic, Manx, Breton) and
the canonical jurisdictional carve rule. The umbrella spec is the single source of
truth for which Celtic languages the `ciancheiltis` repo covers + the bilingual
educational carve rule (LC Gaeilge + WJEC Welsh-medium + UoG bilingual content stay
in `cianfhoghlaim`).

Filed by change `2026-09-13-ciancheiltis-enrichment-v1` (parent:
`2026-09-25-ciancheiltis-init-v1`).

## Requirements

### Requirement: ciancheiltis owns 6 Celtic-language phase specs

The `ciancheiltis` repo SHALL publish 6 phase specs under `openspec/specs/`, one per
Celtic-language jurisdiction, plus this umbrella spec that ties them together.

#### Scenario: All 6 phase specs are present and validate cleanly

- **GIVEN** the `2026-09-13-ciancheiltis-enrichment-v1` change is archived
- **WHEN** `openspec validate --specs --strict` runs
- **THEN** the 7 specs SHALL validate: `ciancheiltis-umbrella`,
  `ciancheiltis-en-cy`, `ciancheiltis-en-ga-roi`, `ciancheiltis-en-ga-ni`,
  `ciancheiltis-en-gd`, `ciancheiltis-en-gv`, `ciancheiltis-en-ga-eu`

#### Scenario: Each phase spec declares its jurisdiction + ISO 639 code

- **GIVEN** the consumer queries a phase spec
- **THEN** the spec SHALL declare:
  - ISO 639-1 / ISO 639-3 language code
  - Jurisdiction (e.g. Cornwall, ROI, NI, Scotland, Isle of Man, Brittany)
  - Canonical agent slug (e.g. `cornish_translation_agent`, `irish_translation_agent`)
  - Upstream DLT source(s) (e.g. `dlt_sources/language/clarin.py`,
    `dlt_sources/lexicographic/wordnet_ga.py`)

### Requirement: The umbrella documents the pathological-namespace cleanup

The umbrella spec SHALL document the rename of the pathologically-named namespace
`meaisinfhoghlaim/models/src/cianfhoghlaim/meaisinfhoghlaim/models/` →
`meaisinfhoghlaim/models/src/ciancheiltis/meaisinfhoghlaim/models/`.

#### Scenario: The teanga_registry import resolves under the canonical package prefix

- **GIVEN** the namespace rename is complete
- **WHEN** the consumer writes
  `from ciancheiltis.meaisinfhoghlaim.models.teanga_registry import TEANGA_MODEL_REGISTRY`
- **THEN** the import SHALL resolve without `ModuleNotFoundError`
- **AND** the `TEANGA_MODEL_REGISTRY` SHALL contain the 12 teanga models (Unsloth Qwen3,
  Unsloth Gemma 4, Unsloth Qwen3-VL, Unsloth Ministral, UDPipe-2 × 4, fastText langid,
  MMS 300M)

### Requirement: The umbrella is the single source of truth for Celtic-language coverage

The umbrella spec SHALL be the entry point for downstream consumers discovering which
Celtic languages the `ciancheiltis` repo covers, and SHALL link each phase spec by name.

#### Scenario: A consumer discovers the 6 Celtic-language phases from the umbrella

- **GIVEN** the consumer reads `openspec/specs/ciancheiltis-umbrella/spec.md`
- **THEN** the umbrella SHALL list the 6 phase specs by name and link to their `spec.md`
- **AND** the umbrella SHALL declare the parent `ciancheiltis-dlt-sources-split` spec as
  the upstream DLT carve-out contract

### Requirement: The umbrella respects the bilingual educational carve rule

The umbrella SHALL NOT claim jurisdiction over:
- `british_isles/ireland/education/subjects/gaeilge/` (LC Gaeilge — stays in cianfhoghlaim)
- `british_isles/wales/education/` (WJEC Welsh-medium — stays in cianfhoghlaim)
- `filesystem/uog_personal_archive.py`, `filesystem/university_of_galway.py`,
  `filesystem/leabharlann_books.py`, `api_sources/leabharlann_education_notes.py`
  (University of Galway bilingual content — stays in cianfhoghlaim)
- `tuatha/subjects/gaeilge.py` (LC Gaeilge subject agent — stays in cianfhoghlaim's
  carved `tuatha/` sub-project)

#### Scenario: The bilingual carve rule is honoured

- **GIVEN** the umbrella spec is archived
- **WHEN** any consumer cross-references the umbrella with `cianfhoghlaim`
- **THEN** none of the 4 carve-protected subtrees SHALL be claimed by the umbrella
- **AND** any new Celtic-language pipeline that overlaps with these 4 subtrees
  SHALL defer to the bilingual educational carve rule and route to cianfhoghlaim
