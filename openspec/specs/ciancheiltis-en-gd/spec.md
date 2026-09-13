# ciancheiltis-en-gd Specification

## Purpose

The `ciancheiltis-en-gd` phase spec defines the **Scottish Gaelic (Gàidhlig) bilingual
coverage** (EN ↔ Scottish Gaelic) for the ciancheiltis sister repo. This phase owns the
Scottish Gaelic Wikipedia corpus, Bòrd na Gàidhlig terminology, and the UD-Scottish-Gaelic
parsing pipeline.

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-gd` |
| ISO 639-1 | `gd` |
| ISO 639-3 | `gla` |
| Jurisdiction | Scotland (Alba), United Kingdom |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `scottish_gaelic_translation_agent` |

## Requirements

### Requirement: The Scottish Gaelic phase owns the Gàidhlig-language datasets

The `ciancheiltis-en-gd` phase SHALL be the canonical home for Scottish Gaelic datasets:
Scottish Gaelic Wikipedia, Bòrd na Gàidhlig terminology, UD-Scottish-Gaelic treebank, and
the Ainmean-Àite na h-Alba ( Gaelic placenames) corpus.

#### Scenario: A consumer queries the Scottish Gaelic Wikipedia corpus

- **GIVEN** the consumer requests `dlt_sources.language.wikipedia_teanga.run("gla")`
- **WHEN** the pipeline executes
- **THEN** the `wikipedia_teanga` source SHALL return Scottish Gaelic pages
- **AND** the result rows SHALL have `language="gla"`

#### Scenario: UDPipe-2 Scottish Gaelic parses Gàidhlig sentences

- **GIVEN** the consumer dispatches a UD parse request for Scottish Gaelic text
- **WHEN** the agent resolves its model via `TEANGA_MODEL_REGISTRY`
- **THEN** the registry SHALL return the `udpipe-2-scottish-gaelic` entry
- **AND** the model SHALL use `model_id="gla"` with the `udpipe_2` backend

### Requirement: The Scottish Gaelic phase exposes the 6 sub-phase surfaces

| Sub-phase | Agent slug | Tool |
|-----------|------------|------|
| Corpus search | `celtic_corpus_search_agent` (shared) | `celtic_corpus_search` |
| Lexicography | `gaelic_lexicographer_agent` (shared) | `lexicographer` |
| Syllabus lookup | `ncca_syllabus_lookup_agent` (NI/Scotland variant) | `ncca_syllabus_lookup` |
| Toponym resolution | `toponym_resolution_agent` (shared, gb-sct subset) | `toponym_resolver` |
| HTR | `duchas_htr_agent` (shared) | `duchas_htr` |
| Translation | `scottish_gaelic_translation_agent` | `gaelic_translate` |

The `scottish_gaelic_translation_agent` uses the shared `gaelic_translate` tool with
`source_lang="en"`, `target_lang="gla"` (or vice versa) per the `TEANGA_MODEL_REGISTRY`.

### Requirement: The Scottish Gaelic phase declares its upstream DLT sources

The `ciancheiltis-en-gd` phase SHALL consume:

- `language/wikipedia_teanga.py` (gd.wikipedia.org)
- `language/clarin.py` (CLARIN-UK Scottish Gaelic corpora, Sabhal Mòr Ostaig)
- `language/ud_parse.py` (UD-Scottish-Gaelic, model `gla`)
- `language/eur_lex.py` (EU EUR-Lex Scottish Gaelic translations)
- `lexicographic/wordnet_ga.py` (WordNet Gàidhlig subset)
- `cultural_heritage/heritage.py` (Scottish heritage subset)

#### Scenario: A consumer streams Scottish Gaelic Wikipedia

- **GIVEN** the consumer requests Scottish Gaelic Wikipedia pages
- **WHEN** the pipeline executes
- **THEN** the source SHALL return rows with `language="gla"` and `jurisdiction="gb-sct"`
- **AND** the rows SHALL include the Gàidhlig-language page metadata (title, content,
  categories, lenition markers)

### Requirement: The Scottish Gaelic phase does not encroach on Scottish education

The `ciancheiltis-en-gd` phase SHALL NOT claim Scottish-medium education pipelines
(those stay in cianfhoghlaim per the bilingual educational carve rule). The Scottish
Gaelic Curriculum for Excellence cross-references are handled by the
`ncca_syllabus_lookup_agent` shared surface, not a discrete Scottish education pipeline.

#### Scenario: CfE-syllabus requests route via the shared surface

- **GIVEN** a consumer requests Curriculum for Excellence (CfE) cross-references
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to `ncca_syllabus_lookup_agent` (shared)
- **AND** the agent SHALL return CfE cross-references alongside the NCCA syllabus
- **AND** the ciancheiltis-en-gd phase SHALL NOT spawn a separate Scottish education pipeline
