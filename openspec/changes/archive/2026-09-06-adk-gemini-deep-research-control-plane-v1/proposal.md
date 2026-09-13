# Change: ADK + Gemini Deep Research Mirror (ciancheiltis)

## Why

This is the ciancheiltis-side mirror of the parent change
`2026-09-06-adk-gemini-deep-research-control-plane-v1` in
`cianfhoghlaim/openspec/changes/`. The ciancheiltis repo is
**DLT-only** for Celtic-language pipelines and inherits all
embedding + indexing from `cianfhoghlaim/cocoindex_flows`. It
needs the `gemini_deep_research` tool primarily for cross-language
research synthesis (e.g. comparing Welsh soft-mutation vs
Scottish Gaelic lenition patterns from primary sources).

## What changes

- **DLT source mirror**: copy `dlt_sources/_shared/gemini_deep_research.py`
  from the parent and register it under
  `ciancheiltis/dlt_sources/_shared/`.
- **BAML schema mirror**: copy `baml_src/_shared/gemini_deep_research.baml`
  from the parent and adapt for the 6 Celtic languages.
- **Routing**: extend `agents/routing_keywords.py` with a
  `celtic_research` bucket.

## Out of scope

- Embedding + indexing layer (lives on the cianfhoghlaim side).

## Dependencies

```markdown
## Dependencies

`Blocked by: cianfhoghlaim/openspec/changes/2026-09-06-adk-gemini-deep-research-control-plane-v1`

`Affected repos: ciancheiltis`
```
