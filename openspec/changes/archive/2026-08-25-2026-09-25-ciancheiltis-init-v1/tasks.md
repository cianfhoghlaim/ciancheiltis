# Tasks — 2026-09-25-ciancheiltis-init-v1

- [x] Create ciancheiltis/ skeleton (pyproject, README, LICENSE, AGENTS, mise.toml)
- [x] Carve `dlt_sources/language/` from cianfhoghlaim → ciancheiltis
- [x] Carve `dlt_sources/cultural_heritage/` from cianfhoghlaim → ciancheiltis
- [x] Carve `dlt_sources/lexicographic/` from cianfhoghlaim → ciancheiltis
- [x] Add backward-compat shims at the old cianfhoghlaim paths
- [x] Fix broken imports in the new ciancheiltis location (`from dlt_sources.language.X` → `from dlt_sources.lexicographic.X`; replace `dlt_sources.common.http_client` with `dlt_sources.common._http_factories`)
- [x] Smoke test: `ciancheiltis/dlt_sources/{_cross,common,language,cultural_heritage,lexicographic}` 5/0/5
- [x] Smoke test: `cianfhoghlaim/dlt_sources/{language,cultural_heritage,lexicographic}` 37/0/37 (shims OK)
