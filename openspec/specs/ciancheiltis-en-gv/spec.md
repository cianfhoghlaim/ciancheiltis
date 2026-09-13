# ciancheiltis-en-gv Specification

## Purpose

The `ciancheiltis-en-gv` phase spec defines the **Manx Gaelic (Gaelg) bilingual coverage**
(EN ↔ Manx) for the ciancheiltis sister repo. Manx is a critically endangered Celtic
language (revival started 1970s; UNESCO 2026 lists ~2 200 L2 speakers); the
`ciancheiltis-en-gv` phase provides the canonical corpus, lexicographic, and
translation surfaces for Manx-language content.

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-gv` |
| ISO 639-1 | `gv` |
| ISO 639-3 | `glv` |
| Jurisdiction | Isle of Man (Ellan Vannin), British Crown Dependency |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `manx_translation_agent` |

## Requirements

### Requirement: The Manx phase owns the Gaelg-language datasets

The `ciancheiltis-en-gv` phase SHALL be the canonical home for Manx Gaelic datasets:
Manx Wikipedia, the Manx Corpus (CAG), the Manx Electronic Dictionary, and the Bunscoill
Ghaelgagh (Manx-medium primary school) curriculum.

#### Scenario: A consumer queries the Manx Wikipedia corpus

- **GIVEN** the consumer requests `dlt_sources.language.wikipedia_teanga.run("glv")`
- **WHEN** the pipeline executes
- **THEN** the `wikipedia_teanga` source SHALL return Manx-language pages
- **AND** the result rows SHALL have `language="glv"`

### Requirement: The Manx phase exposes the 6 sub-phase surfaces

| Sub-phase | Agent slug | Tool |
|-----------|------------|------|
| Corpus search | `celtic_corpus_search_agent` (shared) | `celtic_corpus_search` |
| Lexicography | `gaelic_lexicographer_agent` (shared) | `lexicographer` |
| Syllabus lookup | `ncca_syllabus_lookup_agent` (Bunscoill Ghaelgagh) | `ncca_syllabus_lookup` |
| Toponym resolution | `toponym_resolution_agent` (shared, im subset) | `toponym_resolver` |
| HTR | `duchas_htr_agent` (shared, Manx historical manuscripts) | `duchas_htr` |
| Translation | `manx_translation_agent` | `gaelic_translate` |

The `manx_translation_agent` uses the shared `gaelic_translate` tool with
`source_lang="en"`, `target_lang="glv"` (or vice versa).

#### Scenario: The Manx translation agent uses MMS 300M for low-resource support

- **GIVEN** Manx is low-resource (revival language)
- **WHEN** the `manx_translation_agent` resolves its model
- **THEN** the dispatcher MAY fall back to `TEANGA_MODEL_REGISTRY["mms-300m-teanga"]`
  (which supports ASR/TTS for `glv`) for speech-driven Manx interactions
- **AND** the canonical text-only path SHALL use the shared `gaelic_translate` tool

### Requirement: The Manx phase declares its upstream DLT sources

The `ciancheiltis-en-gv` phase SHALL consume:

- `language/wikipedia_teanga.py` (gv.wikipedia.org — small but growing)
- `language/clarin.py` (CLARIN-UK Manx corpus, Coonceil ny Gaelgey)
- `language/eur_lex.py` (EU EUR-Lex Manx translations)
- `lexicographic/wordnet_ga.py` (shared Celtic lexicon — Manx subset)
- `cultural_heritage/heritage.py` (Manx heritage subset, Tynwald Day content)

#### Scenario: A consumer streams Manx Wikipedia

- **GIVEN** the consumer requests Manx-language Wikipedia pages
- **WHEN** the pipeline executes
- **THEN** the source SHALL return rows with `language="glv"` and
  `jurisdiction="im"` (Isle of Man ISO 3166-1 alpha-2)
- **AND** the rows SHALL include Manx-language page metadata

### Requirement: The Manx phase respects the British Crown Dependency carve

The `ciancheiltis-en-gv` phase SHALL respect the British Crown Dependency carve: the
Isle of Man is **not** part of the UK for education-policy purposes (Manx-medium
education is governed by Coonceil ny Gaelgey + the Isle of Man Department of Education).
The phase SHALL NOT claim UK education pipelines.

#### Scenario: Bunscoill Ghaelgagh content routes via the syllabus agent

- **GIVEN** a consumer requests Bunscoill Ghaelgagh (Manx-medium primary) curriculum
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to `ncca_syllabus_lookup_agent`
- **AND** the agent SHALL return Bunscoill Ghaelgagh curriculum cross-references
- **AND** the ciancheiltis-en-gv phase SHALL NOT claim UK or ROI education policy
