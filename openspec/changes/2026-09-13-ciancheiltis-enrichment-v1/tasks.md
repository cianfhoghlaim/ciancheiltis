# Tasks — 2026-09-13-ciancheiltis-enrichment-v1

## Stage 0 — Pre-flight
- [x] T0.1 — Confirm `ciancheiltis-init-v1` is archived (`openspec/changes/archive/2026-08-25-2026-09-25-ciancheiltis-init-v1/`)
- [x] T0.2 — Inspect current state: `git log --oneline -5`, `git status --short`

## Stage 1 — Spec delta
- [x] T1.1 — Write `openspec/changes/2026-09-13-ciancheiltis-enrichment-v1/proposal.md`
- [x] T1.2 — Write `openspec/changes/2026-09-13-ciancheiltis-enrichment-v1/tasks.md`
- [x] T1.3 — Write `openspec/changes/2026-09-13-ciancheiltis-enrichment-v1/specs/ciancheiltis-umbrella/spec.md`

## Stage 2 — Phase specs (6 Celtic-language phases)
- [x] T2.1 — Write `openspec/specs/ciancheiltis-en-cy/spec.md` (Cornish bilingual)
- [x] T2.2 — Write `openspec/specs/ciancheiltis-en-ga-roi/spec.md` (Irish / Gaeilge ROI)
- [x] T2.3 — Write `openspec/specs/ciancheiltis-en-ga-ni/spec.md` (Northern Irish context)
- [x] T2.4 — Write `openspec/specs/ciancheiltis-en-gd/spec.md` (Scottish Gaelic / Gàidhlig)
- [x] T2.5 — Write `openspec/specs/ciancheiltis-en-gv/spec.md` (Manx Gaelic)
- [x] T2.6 — Write `openspec/specs/ciancheiltis-en-ga-eu/spec.md` (Breton / Brezhoneg, EU)

## Stage 3 — Agent DEVELOPMENT doc
- [x] T3.1 — Write `agents/teanga/DEVELOPMENT.md` documenting the agent + tool + config triad

## Stage 4 — Namespace rename
- [x] T4.1 — Move `meaisinfhoghlaim/models/src/cianfhoghlaim/meaisinfhoghlaim/models/` →
             `meaisinfhoghlaim/models/src/ciancheiltis/meaisinfhoghlaim/models/`
- [x] T4.2 — Update the `__init__.py` import to use the canonical
             `ciancheiltis.meaisinfhoghlaim.models.teanga_registry` path
- [x] T4.3 — Confirm no other files in the repo reference the old path

## Stage 5 — Commits
- [x] T5.1 — Commit 1: `feat(ciancheiltis): file umbrella openspec change with 6 phase specs`
- [x] T5.2 — Commit 2: `docs(teanga): add DEVELOPMENT.md for Celtic-language agents`
- [x] T5.3 — Commit 3: `refactor(ciancheiltis): rename meaisinfhoghlaim/models/src/cianfhoghlaim/ → ciancheiltis/`

## Stage 6 — Validation + archive
- [x] T6.1 — Run `openspec validate 2026-09-13-ciancheiltis-enrichment-v1 --strict`
- [x] T6.2 — Archive the change (`openspec archive 2026-09-13-ciancheiltis-enrichment-v1 -y`)
