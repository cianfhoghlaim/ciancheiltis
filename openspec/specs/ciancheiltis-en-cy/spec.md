# ciancheiltis-en-cy Specification

## Purpose

The `ciancheiltis-en-cy` phase spec defines the **Cornish bilingual (EN ↔ Cornish / Kernewek)**
coverage of the `ciancheiltis` sister repo. It declares the canonical agent slug,
ISO 639 codes, jurisdiction, upstream DLT sources, and the 6 sub-phases (corpus search,
lexicography, syllabus lookup, toponym resolution, HTR, translation).

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-cy` |
| ISO 639-1 | `cy` (Welsh — see carve note) |
| ISO 639-2 / 639-3 | `cor` (Cornish) |
| Jurisdiction | Cornwall, United Kingdom |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `cornish_translation_agent` |

> **Carve note.** ISO 639-1 `cy` is reserved for Welsh. Cornish uses `cor` (ISO 639-3).
> The phase slug `en-cy` is the ciancheiltis convention for "English + a Celtic-language
> jurisdiction starting with `cy`" — Cornish qualifies because the **language family code**
> (Brythonic / `cy`) overlaps. Welsh-medium education stays in cianfhoghlaim per the
> bilingual educational carve rule.

## Requirements

### Requirement: The Cornish bilingual phase exposes the 6 sub-phase surfaces

The `ciancheiltis-en-cy` phase SHALL expose 6 sub-phase surfaces, each backed by a
canonical ADK agent under `agents/teanga/src/teanga/agents/`:

| Sub-phase | Agent slug | Tool |
|-----------|------------|------|
| Corpus search | `celtic_corpus_search_agent` (shared) | `celtic_corpus_search` |
| Lexicography | `gaelic_lexicographer_agent` (shared) | `lexicographer` |
| Syllabus lookup | `ncca_syllabus_lookup_agent` (shared) | `ncca_syllabus_lookup` |
| Toponym resolution | `toponym_resolution_agent` (shared) | `toponym_resolver` |
| HTR | `duchas_htr_agent` (shared) | `duchas_htr` |
| Translation | `cornish_translation_agent` | `gaelic_translate` |

#### Scenario: A consumer queries the Cornish translation agent

- **GIVEN** the `ciancheiltis-en-cy` phase is wired
- **WHEN** the consumer dispatches a Cornish EN ↔ cor translation request
- **THEN** the dispatcher SHALL route to `cornish_translation_agent`
- **AND** the agent SHALL use the `gaelic_translate` tool with `source_lang="en"`,
  `target_lang="cor"` (or vice versa)

#### Scenario: The Cornish toponym resolution routes to Logainm-Cornwall

- **GIVEN** the consumer requests toponym resolution for a Cornish placename
- **WHEN** the `toponym_resolution_agent` is dispatched
- **THEN** the agent SHALL use the `toponym_resolver` tool
- **AND** the tool SHALL query the Logainm-Cornwall subset (the Cornish-language
  Logainm derivative) under the ciancheiltis DLT carve-out

### Requirement: The Cornish phase declares its upstream DLT sources

The `ciancheiltis-en-cy` phase SHALL consume the following DLT sources under
`ciancheiltis/dlt_sources/`:

- `language/wikipedia_teanga.py` — Cornish Wikipedia (cor.wikipedia.org)
- `language/clarin.py` — CLARIN-UK Cornish-language corpora
- `language/eur_lex.py` — EU EUR-Lex Cornish translations
- `lexicographic/wordnet_ga.py` — WordNet Gaeilge (Brythonic shared lexicon)
- `cultural_heritage/heritage.py` — Cornish heritage subset

#### Scenario: A consumer streams Cornish-language Wikipedia pages

- **GIVEN** the consumer requests `dlt_sources.language.wikipedia_teanga.run("cor")`
- **WHEN** the pipeline executes
- **THEN** the `wikipedia_teanga` source SHALL return Cornish-language pages
- **AND** the result rows SHALL have `language="cor"`

### Requirement: The Cornish phase does not encroach on Welsh-medium education

The `ciancheiltis-en-cy` phase SHALL NOT claim the Welsh-medium education pipeline
(`british_isles/wales/education/` in cianfhoghlaim). Welsh-medium stays in cianfhoghlaim
per the bilingual educational carve rule.

#### Scenario: A Welsh-medium request does not route to Cornish agents

- **GIVEN** a Welsh-medium consumer request arrives
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to the cianfhoghlaim Welsh-medium agent
- **AND** the `cornish_translation_agent` SHALL NOT receive Welsh-medium requests
