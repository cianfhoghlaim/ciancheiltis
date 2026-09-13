# Change: Ciancheiltis Enrichment v1 — 6 Celtic-Language Phase Specs + Pathological-Namespace Cleanup

## Why

The `ciancheiltis-init-v1` change (archived `2026-08-25-2026-09-25-ciancheiltis-init-v1`, commit `ba19bea`) carved the pure Irish-language datasets + non-educational Celtic-language pipelines
out of `cianfhoghlaim` into the `ciancheiltis` sister repo. The init change landed
halfway: 9 stub modules were filed to fix module-load breakers (Round 1, commit `564c200`)
but the umbrella spec + 6 phase specs were never filed, the agent-fleet DEVELOPMENT doc
was never written, and the pathologically-named namespace
`meaisinfhoghlaim/models/src/cianfhoghlaim/meaisinfhoghlaim/models/` was never cleaned up.

This change is the landing pad for the rest of the enrichment:

1. File the umbrella spec + 6 phase specs (one per Celtic language family / jurisdiction).
2. Add `agents/teanga/DEVELOPMENT.md` documenting how to add a new Celtic-language agent.
3. Rename the pathological namespace `meaisinfhoghlaim/models/src/cianfhoghlaim/` →
   `meaisinfhoghlaim/models/src/ciancheiltis/`. The parent package (`ciancheiltis-meaisinfhoghlaim`)
   was renamed in commit `ba19bea` but the leaf-level `meaisinfhoghlaim/models/src/`
   segment kept the legacy `cianfhoghlaim/` prefix.

## What changes

1. New openspec change folder: `openspec/changes/2026-09-13-ciancheiltis-enrichment-v1/`
   with `proposal.md`, `tasks.md`, and `specs/ciancheiltis-umbrella/spec.md`.
2. Six new phase specs under `openspec/specs/`:
   - `ciancheiltis-en-cy` — Cornish bilingual (Cornwall, UK)
   - `ciancheiltis-en-ga-roi` — Irish/Gaeilge (Republic of Ireland)
   - `ciancheiltis-en-ga-ni` — Northern Irish / Ulster Scots context (Northern Ireland, UK)
   - `ciancheiltis-en-gd` — Scottish Gaelic / Gàidhlig (Scotland, UK)
   - `ciancheiltis-en-gv` — Manx Gaelic (Isle of Man, British Crown Dependency)
   - `ciancheiltis-en-ga-eu` — Breton / Brezhoneg (Brittany, France; EU)
3. New `agents/teanga/DEVELOPMENT.md` documenting the ADK agent + tool + config triad.
4. Rename `meaisinfhoghlaim/models/src/cianfhoghlaim/meaisinfhoghlaim/models/` →
   `meaisinfhoghlaim/models/src/ciancheiltis/meaisinfhoghlaim/models/`. Update the
   `__init__.py` import to match the canonical `ciancheiltis.meaisinfhoghlaim.models.teanga_registry`
   path.

## Out of scope

- Real LLM-backed translation (the stubs remain `LlmAgent` definitions; real LiteLLM
  routing ships when the umbrella's Phase 2 lands).
- Embedding + indexing layer (lives on the `cianfhoghlaim` side per the bilingual
  educational carve rule).
- BAML/Cognee/MotherDuck cascade contracts for the 6 Celtic languages (Phase 5+).

## Scope (today)

- File the umbrella spec + 6 phase specs.
- Add the agent DEVELOPMENT doc.
- Rename the pathological namespace.
- Validate with `openspec validate 2026-09-13-ciancheiltis-enrichment-v1 --strict`.
- Archive the change.

## Dependencies

```markdown
## Dependencies

`Blocked by: openspec/changes/archive/2026-08-25-2026-09-25-ciancheiltis-init-v1/`

`Affected repos: ciancheiltis`
```
