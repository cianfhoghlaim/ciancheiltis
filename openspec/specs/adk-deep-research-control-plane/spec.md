# Mirror: ciancheiltis ADK + Gemini Deep Research

Per the parent openspec change
`2026-09-06-adk-gemini-deep-research-control-plane-v1`. Adds a
cross-Celtic-language research capability.

## Requirements

### Requirement: Celtic-language Gemini Deep Research query
The `dlt_sources/_shared/gemini_deep_research.py` mirror SHALL
support queries in the 6 Celtic languages (Irish, Welsh, Scottish
Gaelic, Breton, Cornish, Manx).

#### Scenario: Welsh query
- **WHEN** a Welsh-language query (e.g. `"Cymraeg: beth yw'r system addysg uwchradd yng Nghymru?"`) is submitted
- **THEN** the DLT source MUST accept it
- **AND** MUST yield a `gemini_deep_research_report` row

### Requirement: Embedding handoff to cianfhoghlaim
The BAML extraction output MUST be uploaded to `cianfhoghlaim`'s
shared CocoIndex `_lifespan.py` (`BAAI/bge-m3` 1024-d embedder)
for cross-language embedding parity.

#### Scenario: Embedding handoff
- **WHEN** `baml_extract_agent` returns a row
- **THEN** the row MUST be tagged with `embedding_target="cianfhoghlaim.shared"`
- **AND** `cocoindex_index_agent` MUST use the parent repo's embedder
