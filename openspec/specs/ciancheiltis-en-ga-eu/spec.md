# ciancheiltis-en-ga-eu Specification

## Purpose

The `ciancheiltis-en-ga-eu` phase spec defines the **Breton (Brezhoneg) bilingual
coverage** (EN ↔ Breton / FR ↔ Breton) for the ciancheiltis sister repo. Breton is the
only **EU Member State** Celtic language (spoken in Brittany / Breizh, France, EU);
the `ciancheiltis-en-ga-eu` phase is the EU-jurisdictional sibling of the Irish,
Scottish, Manx, and Cornish phases.

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-ga-eu` |
| ISO 639-1 | `br` (Breton) |
| ISO 639-3 | `bre` |
| Jurisdiction | Brittany (Breizh), France, European Union |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `breton_translation_agent` |

> **Carve note.** The phase slug `en-ga-eu` is the ciancheiltis convention for
> "English + a Celtic-language EU jurisdiction". French is **not** a Celtic language
> (it's a Romance language), but Breton operates in the French + EU multilingual
> context. The phase provides EN ↔ Breton + (via the EUR-Lex DLT source) FR ↔ Breton
> + EU institutional Breton (Ofis ar Brezhoneg, Région Bretagne terminology).

## Requirements

### Requirement: The Breton phase owns the Brezhoneg-language datasets

The `ciancheiltis-en-ga-eu` phase SHALL be the canonical home for Breton-language
datasets: Breton Wikipedia, the Ofis ar Brezhoneg terminology database, the
Brud Nevez corpus, and the UD-Breton treebank.

#### Scenario: A consumer queries the Breton Wikipedia corpus

- **GIVEN** the consumer requests `dlt_sources.language.wikipedia_teanga.run("bre")`
- **WHEN** the pipeline executes
- **THEN** the `wikipedia_teanga` source SHALL return Breton-language pages
- **AND** the result rows SHALL have `language="bre"`

#### Scenario: UDPipe-2 Breton parses Brezhoneg sentences

- **GIVEN** the consumer dispatches a UD parse request for Breton text
- **WHEN** the agent resolves its model via `TEANGA_MODEL_REGISTRY`
- **THEN** the registry SHALL return the `udpipe-2-breton` entry
- **AND** the model SHALL use `model_id="bre"` with the `udpipe_2` backend

### Requirement: The Breton phase exposes the 6 sub-phase surfaces

The `ciancheiltis-en-ga-eu` phase SHALL expose 6 sub-phase surfaces, each backed by a
canonical ADK agent under `agents/teanga/src/teanga/agents/`:

| Sub-phase | Agent slug | Tool |
|-----------|------------|------|
| Corpus search | `celtic_corpus_search_agent` (shared) | `celtic_corpus_search` |
| Lexicography | `gaelic_lexicographer_agent` (shared) | `lexicographer` |
| Syllabus lookup | `ncca_syllabus_lookup_agent` (Breton variant) | `ncca_syllabus_lookup` |
| Toponym resolution | `toponym_resolution_agent` (shared, fr-bre subset) | `toponym_resolver` |
| HTR | `duchas_htr_agent` (shared, Breton historical manuscripts) | `duchas_htr` |
| Translation | `breton_translation_agent` | `gaelic_translate` |

#### Scenario: The Breton translation agent uses the shared gaelic_translate tool

- **GIVEN** the consumer dispatches an EN ↔ bre translation request
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to `breton_translation_agent`
- **AND** the agent SHALL use the shared `gaelic_translate` tool with `source_lang="en"`,
  `target_lang="bre"` (or vice versa)

#### Scenario: The Breton toponym resolution uses the fr-bre subset

- **GIVEN** the consumer requests toponym resolution for a Breton placename
- **WHEN** the `toponym_resolution_agent` is dispatched
- **THEN** the agent SHALL use the `toponym_resolver` tool with the `fr-bre` subset flag
- **AND** the tool SHALL query the Breton-language placenames under the ciancheiltis DLT
  carve-out

### Requirement: The Breton phase declares its upstream DLT sources

The `ciancheiltis-en-ga-eu` phase SHALL consume:

- `language/wikipedia_teanga.py` (br.wikipedia.org)
- `language/clarin.py` (CLARIN-FR Breton corpora, Ofis ar Brezhoneg)
- `language/ud_parse.py` (UD-Breton, model `bre`)
- `language/eur_lex.py` (EU EUR-Lex Breton translations — primary EU-institutional source)
- `lexicographic/wordnet_ga.py` (shared Celtic lexicon — Breton subset)
- `cultural_heritage/heritage.py` (Breton heritage subset, Région Bretagne cultural content)

#### Scenario: A consumer streams Breton EUR-Lex translations

- **GIVEN** the consumer requests EU EUR-Lex content in Breton
- **WHEN** the `eur_lex.py` source executes
- **THEN** the source SHALL return rows with `language="bre"`
- **AND** the rows SHALL include the EU institutional Breton terminology from
  Ofis ar Brezhoneg + Région Bretagne

### Requirement: The Breton phase does not encroach on French-language pipelines

The `ciancheiltis-en-ga-eu` phase SHALL NOT claim French-language pipelines (French
is a Romance language and out of scope for ciancheiltis). The phase owns only the
Breton subset of any EU/French-language source.

#### Scenario: A French-language EU EUR-Lex request routes to the French pipeline

- **GIVEN** a consumer requests EU EUR-Lex content in French (not Breton)
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL NOT route to `breton_translation_agent`
- **AND** the FR subset SHALL be handled by the cianfhoghlaim French pipeline
  (out of scope for ciancheiltis)

### Requirement: The Breton phase honours the EU Charter for Regional or Minority Languages

The `ciancheiltis-en-ga-eu` phase SHALL respect France's EU Charter for Regional or
Minority Languages commitments to Breton: Breton-language education (Diwan schools),
public signage, and EU institutional use.

#### Scenario: Diwan-school requests route via the syllabus agent with EU context

- **GIVEN** a consumer requests Breton-medium education (Diwan schools) content
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to `ncca_syllabus_lookup_agent` (shared)
- **AND** the agent SHALL return Diwan curriculum cross-references alongside any
  EU Charter context
- **AND** the ciancheiltis-en-ga-eu phase SHALL NOT claim Diwan policy ownership
  (the policy layer lives on the cianfhoghlaim side per the bilingual educational
  carve rule)
