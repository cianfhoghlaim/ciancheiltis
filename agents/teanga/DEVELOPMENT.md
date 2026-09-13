# Teanga (Celtic-Language) Agent Fleet — DEVELOPMENT.md

This document explains how the `agents/teanga/` agent fleet is organized, how to add a new
Celtic-language agent, and the contract that every teanga agent follows.

## Overview

The teanga agent fleet is the ciancheiltis-side ADK (Agent Development Kit) implementation
for the 6 Celtic-language phases declared in `openspec/specs/ciancheiltis-en-*/spec.md`:

| Phase | ISO 639-3 | Jurisdiction | Canonical agent slug |
|-------|-----------|--------------|----------------------|
| `ciancheiltis-en-ga-roi` | `gle` | Republic of Ireland | `irish_translation_agent` |
| `ciancheiltis-en-cy` | `cor` | Cornwall, UK | `cornish_translation_agent` |
| `ciancheiltis-en-ga-ni` | `gle` + NI context | Northern Ireland, UK | `irish_translation_agent` (NI-routed) |
| `ciancheiltis-en-gd` | `gla` | Scotland, UK | `scottish_gaelic_translation_agent` |
| `ciancheiltis-en-gv` | `glv` | Isle of Man | `manx_translation_agent` |
| `ciancheiltis-en-ga-eu` | `bre` | Brittany, France (EU) | `breton_translation_agent` |

The fleet is dispatched via Google ADK + LiteLLM routing per the `agents/routing_keywords.py`
buckets (which lives on the cianfhoghlaim side; the ciancheiltis teanga fleet inherits the
dispatcher).

## File layout

```text
agents/teanga/
├── pyproject.toml              # ciancheiltis-teanga package metadata
├── DEVELOPMENT.md              # this file
└── src/teanga/
    ├── __init__.py             # re-exports the 6 agents
    ├── config.py               # TeangaConfig — LiteLLM-resolved models per jurisdiction
    ├── agents/                 # one ADK LlmAgent per Celtic-language phase
    │   ├── celtic_corpus_search_agent.py
    │   ├── gaelic_lexicographer_agent.py
    │   ├── duchas_htr_agent.py
    │   ├── toponym_resolution_agent.py
    │   ├── ncca_syllabus_lookup_agent.py
    │   └── irish_translation_agent.py
    └── tools/                  # one ADK tool per agent
        ├── celtic_corpus_search.py
        ├── lexicographer.py
        ├── duchas_htr.py
        ├── toponym_resolver.py
        ├── ncca_syllabus_lookup.py
        └── gaelic_translate.py
```

## The agent + tool + config triad

Every teanga agent follows the same three-file contract:

1. **`agents/<agent>.py`** — the ADK `LlmAgent` definition + a thin async `run_*` wrapper.
2. **`tools/<tool>.py`** — the ADK tool implementation (the side-effecting or
   data-fetching function the agent calls).
3. **`config.py`** — the `TeangaConfig` singleton that resolves LiteLLM models per
   agent role (`text_llm`, `search`, `translation`, `ocr`, etc.) and declares the
   jurisdiction scope.

The agent imports the tool, the agent imports the config, and the dispatcher (cianfhoghlaim)
imports the agent. Nothing else imports the tool directly.

```python
# agents/<agent>.py — canonical pattern
from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.<tool> import <tool>

config = TeangaConfig.from_env()

<agent_slug>_agent = LlmAgent(
    name="<agent_slug>",
    model=config.litellm.resolve_model("<role>", "<use_case>"),
    description="<one-sentence description>",
    instruction="<system prompt for the LLM>",
    tools=[<tool>],
)

async def run_<action>(...) -> ...:
    return await <tool>(...)

__all__ = ["<agent_slug>", "run_<action>"]
```

## How to add a new Celtic-language agent

The 6 phases above already cover the canonical 6 Celtic languages (Gaeilge, Cornish,
Scottish Gaelic, Manx, Breton, plus the NI jurisdictional bridge). To add a **new
Celtic-language agent** (e.g. for Welsh-medium support outside the bilingual educational
carve rule, or for a revival-language dialect agent), follow these steps:

### 1. Decide whether the agent belongs in ciancheiltis or cianfhoghlaim

The **bilingual educational carve rule** keeps the following in cianfhoghlaim (not ciancheiltis):

- `british_isles/ireland/education/subjects/gaeilge/` — LC Gaeilge
- `british_isles/wales/education/` — WJEC Welsh-medium
- `filesystem/uog_personal_archive.py`, `filesystem/university_of_galway.py`,
  `filesystem/leabharlann_books.py`, `api_sources/leabharlann_education_notes.py` — UoG
- `tuatha/subjects/gaeilge.py` — LC Gaeilge subject agent

Anything else (a new Celtic dialect, a new revival-language pipeline, a new
non-educational Welsh-language pipeline) belongs in ciancheiltis.

### 2. Add a new openspec phase spec

Open a new openspec change in the ciancheiltis repo:

```bash
mkdir -p openspec/changes/YYYY-MM-DD-<phase-slug>-v1/specs/<phase-slug>
```

Write `proposal.md`, `tasks.md`, and `specs/<phase-slug>/spec.md` using the 6 existing
phase specs (`ciancheiltis-en-cy`, `ciancheiltis-en-ga-roi`, …) as templates. Declare
the ISO 639-3 code, jurisdiction, parent umbrella (`ciancheiltis-umbrella`), and parent
DLT carve-out (`ciancheiltis-dlt-sources-split`).

### 3. Add the agent + tool + config triad

Add three new files under `agents/teanga/src/teanga/`:

```python
# agents/teanga/src/teanga/agents/<agent_slug>_agent.py
"""ciancheiltis.agents.teanga.<agent_slug>_agent — <one-line description>.

Per the <openspec change id> plan. <2-3 sentence rationale>.
"""
from __future__ import annotations

from typing import Any

from google.adk.agents import LlmAgent

from ..config import TeangaConfig
from ..tools.<tool> import <tool>

config = TeangaConfig.from_env()


<agent_slug>_agent = LlmAgent(
    name="<agent_slug>",
    model=config.litellm.resolve_model("<role>", "<use_case>"),
    description="<one-sentence description>",
    instruction="<system prompt>",
    tools=[<tool>],
)


async def run_<action>(...) -> dict[str, Any]:
    return await <tool>(...)


__all__ = ["<agent_slug>", "run_<action>"]
```

```python
# agents/teanga/src/teanga/tools/<tool>.py
"""ciancheiltis.agents.teanga.<tool> — <one-line description>."""
from __future__ import annotations

from typing import Any

# Tool implementation here.


async def <tool>(...) -> dict[str, Any]:
    """<docstring>."""
    ...


__all__ = ["<tool>"]
```

If the agent needs a new LiteLLM-resolved model or a new jurisdiction, amend
`config.py` (the `TeangaConfig` frozen dataclass). For the model itself, add the entry
to `meaisinfhoghlaim/models/src/ciancheiltis/meaisinfhoghlaim/models/teanga_registry.py`
(the canonical `TEANGA_MODEL_REGISTRY`).

### 4. Re-export the agent from `__init__.py`

Add the agent slug to the `agents/teanga/src/teanga/__init__.py` re-export list so the
dispatcher can import it.

### 5. Add a routing keyword on the cianfhoghlaim side

The dispatcher lives on the cianfhoghlaim side (`agents/routing_keywords.py`). Add a new
routing bucket for the new agent. The ciancheiltis side has no dispatcher of its own.

### 6. Validate

```bash
openspec validate <phase-slug> --strict
```

Archive the change when validation passes:

```bash
openspec archive <phase-slug> -y
```

## Stub status

The 6 agent files in `agents/teanga/src/teanga/agents/` and the 6 tool files in
`agents/teanga/src/teanga/tools/` are **stubs** filed in commit `564c200` to fix
module-load breakers. The stubs:

- Define the ADK `LlmAgent` with a placeholder model resolution
  (`config.litellm.resolve_model(...)` — `litellm` is **not** yet wired on the
  `TeangaConfig` dataclass; it ships when the umbrella's Phase 2 lands).
- Reference `2026-XX-XX-ciancheiltis-enrichment` in their module docstrings; replace
  this reference with the archived change id once `2026-09-13-ciancheiltis-enrichment-v1`
  is archived.
- Call the tool directly from the `run_*` wrapper (which is the canonical pattern).

The stubs are **safe to import** but the real LLM-backed translation ships in a
follow-up change. Do not call any `run_*` wrapper in production until the umbrella's
Phase 2 wires `config.litellm`.

## Cross-references

- `openspec/specs/ciancheiltis-umbrella/spec.md` — the umbrella spec
- `openspec/specs/ciancheiltis-en-*/spec.md` — the 6 phase specs
- `openspec/changes/2026-09-13-ciancheiltis-enrichment-v1/proposal.md` — this change
- `dlt_sources/language/wikipedia_teanga.py` — canonical 6-Celtic-language Wikipedia loader
- `dlt_sources/language/clarin.py` — canonical CLARIN-UK/IE loader
- `dlt_sources/language/ud_parse.py` — canonical UD-6 loader
- `meaisinfhoghlaim/models/src/ciancheiltis/meaisinfhoghlaim/models/teanga_registry.py` —
  canonical `TEANGA_MODEL_REGISTRY`
