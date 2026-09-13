# ciancheiltis-en-ga-roi Specification

## Purpose

The `ciancheiltis-en-ga-roi` phase spec defines the **Irish (Gaeilge) bilingual coverage
for the Republic of Ireland (ROI)** in the `ciancheiltis` sister repo. This phase owns
the **pure Irish-language** datasets (Téarma, Logainm, Ainm, Gaois, Dúchas, Canúint,
UD-Irish) carved out by the `ciancheiltis-dlt-sources-split` spec.

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-ga-roi` |
| ISO 639-1 | `ga` |
| ISO 639-3 | `gle` |
| Jurisdiction | Republic of Ireland (Gaeltacht + broader) |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `irish_translation_agent` |

## Requirements

### Requirement: The Irish-ROI phase owns the pure Irish-language datasets

The `ciancheiltis-en-ga-roi` phase SHALL be the canonical home for the pure Irish-language
datasets carved out from cianfhoghlaim. The phase SHALL NOT claim LC Gaeilge (which is
the bilingual educational carve, owned by cianfhoghlaim's `tuatha/subjects/gaeilge.py`).

#### Scenario: A consumer queries the canonical pure-Irish Téarma dataset

- **GIVEN** the `ciancheiltis-en-ga-roi` phase is wired
- **WHEN** the consumer queries the Téarma dataset
- **THEN** the consumer SHALL import from `ciancheiltis.dlt_sources.lexicographic.tearma`
  (the canonical Irish-ROI home)
- **AND** the import SHALL NOT require any cianfhoghlaim dependency

#### Scenario: The Logainm Irish placenames resolve via the ROI-specific toponym resolver

- **GIVEN** the consumer requests toponym resolution for a Gaeltacht placename
- **WHEN** the `toponym_resolution_agent` is dispatched
- **THEN** the agent SHALL query the Logainm-IE subset
- **AND** the result rows SHALL have `jurisdiction="ie-roi"`

### Requirement: The Irish-ROI phase exposes the 6 sub-phase surfaces

The `ciancheiltis-en-ga-roi` phase SHALL expose 6 sub-phase surfaces, each backed by a
canonical ADK agent under `agents/teanga/src/teanga/agents/`:

| Sub-phase | Agent slug | Tool |
|-----------|------------|------|
| Corpus search | `celtic_corpus_search_agent` | `celtic_corpus_search` |
| Lexicography | `gaelic_lexicographer_agent` | `lexicographer` |
| Syllabus lookup | `ncca_syllabus_lookup_agent` | `ncca_syllabus_lookup` |
| Toponym resolution | `toponym_resolution_agent` | `toponym_resolver` |
| HTR | `duchas_htr_agent` | `duchas_htr` |
| Translation | `irish_translation_agent` | `gaelic_translate` |

The `irish_translation_agent` SHALL use Unsloth Qwen3.8-27B for high-quality bilingual
EN ↔ GA translation (per the `TEANGA_MODEL_REGISTRY["qwen3.8-27b-instruct"]` entry).

#### Scenario: The Irish translation agent uses Qwen3.8-27B per the registry

- **GIVEN** the `irish_translation_agent` is dispatched for an EN ↔ GA request
- **WHEN** the agent initialises
- **THEN** the agent SHALL resolve its model via
  `TEANGA_MODEL_REGISTRY["qwen3.8-27b-instruct"]`
- **AND** the resolved model SHALL be `unsloth/Qwen3.8-27B-Instruct-GGUF`
  (variant `UD-Q4_K_XL`, 32 768-token context)

### Requirement: The Irish-ROI phase declares its upstream DLT sources

The `ciancheiltis-en-ga-roi` phase SHALL consume:

- `language/wikipedia_teanga.py` (gle.wikipedia.org)
- `language/clarin.py` (CLARIN-IE Irish corpora, IDTÁC, Corpas NaCo)
- `language/eur_lex.py` (EU EUR-Lex Irish translations)
- `language/ud_parse.py` (UD-Irish)
- `language/lcga_exam_papers.py` (Irish-medium Leaving Cert)
- `lexicographic/tearma.py`, `lexicographic/logainm.py`, `lexicographic/ainm.py`,
  `lexicographic/gaois.py`, `lexicographic/wordnet_ga.py`, `lexicographic/ud_extensions_ga.py`
- `lexicographic/canuint.py` (Canúint dialects)
- `cultural_heritage/duchas.py`, `cultural_heritage/heritage.py`,
  `cultural_heritage/hidden_heritages.py`, `cultural_heritage/hidden_heritages_extended.py`,
  `cultural_heritage/meitheal_corrections.py`

#### Scenario: A consumer streams Canúint dialect data

- **GIVEN** the consumer requests Canúint dialect data
- **WHEN** the pipeline executes
- **THEN** the `canuint.py` source SHALL return rows with `language="gle"` and
  `dialect ∈ {munster, connacht, ulster}`
- **AND** the rows SHALL include the 5 Canúint submodules per the
  `ciancheiltis-dlt-sources-split` spec
