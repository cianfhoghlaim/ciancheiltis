# ciancheiltis-en-ga-ni Specification

## Purpose

The `ciancheiltis-en-ga-ni` phase spec defines the **Northern Irish bilingual coverage**
(English ↔ Irish / Ulster Scots / Northern Irish context) for the ciancheiltis sister repo.
Unlike the other 5 phases, this phase is a **context-aware routing surface** rather than
a discrete Celtic-language pipeline — it bridges the Irish-ROI phase with the
Northern Irish political + educational context (Ulster Scots, NI curriculum).

## Jurisdictional metadata

| Field | Value |
|-------|-------|
| Phase slug | `ciancheiltis-en-ga-ni` |
| ISO 639-1 | `ga` (Irish context) / `sco` (Ulster Scots) |
| ISO 639-3 | `gle` (Irish) / `xgb` / `nul` (Ulster Scots / Northern Irish) |
| Jurisdiction | Northern Ireland, United Kingdom |
| Parent umbrella | `ciancheiltis-umbrella` |
| Parent DLT carve-out | `ciancheiltis-dlt-sources-split` |
| Canonical agent slug | `irish_translation_agent` (shared with ROI, NI-context-routed) |

> **Carve note.** The `en-ga-ni` phase is the **bilingual jurisdictional bridge** between
> the ROI Irish phase and the UK-NI political context. Ulster Scots is a sister language
> under the NI Good Friday Agreement framework but is **not** a Celtic language per the
> canonical ISO 639 classification. This phase routes NI-context requests to the Irish-ROI
> `irish_translation_agent` with a `jurisdiction="uk-ni"` flag, and provides a separate
> context overlay for Ulster Scots historical-cultural references.

## Requirements

### Requirement: The Northern Irish phase routes Irish-language requests to the ROI agent

The `ciancheiltis-en-ga-ni` phase SHALL route Irish-language EN ↔ GA translation requests
to the same `irish_translation_agent` used by `ciancheiltis-en-ga-roi`, but with the
`jurisdiction="uk-ni"` flag set.

#### Scenario: A NI-context Irish translation request routes with jurisdiction flag

- **GIVEN** a consumer requests EN ↔ GA translation in a NI context (post-Good Friday
  Agreement framing)
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to `irish_translation_agent`
- **AND** the dispatch context SHALL include `jurisdiction="uk-ni"`
- **AND** the NI context overlay SHALL be applied (Ulster dialect preferences, Gaelscoil
  educational framing)

### Requirement: The Northern Irish phase provides a context overlay

The `ciancheiltis-en-ga-ni` phase SHALL publish a context overlay that augments the
`irish_translation_agent` with NI-specific terminology:

- Gaelscoil (Irish-medium school) terminology
- Ulster dialect markers (Donegal, Derry, Belfast Gaeltacht)
- NI Curriculum (CCEA) cross-references

#### Scenario: A Gaelscoil request includes NI curriculum cross-references

- **GIVEN** the consumer is a Gaelscoil teacher in NI
- **WHEN** the dispatcher routes the syllabus lookup request
- **THEN** the dispatcher SHALL route to `ncca_syllabus_lookup_agent` (shared)
- **AND** the agent SHALL include CCEA cross-references alongside the NCCA (ROI) syllabus

### Requirement: The Northern Irish phase does not claim the bilingual educational carve

The `ciancheiltis-en-ga-ni` phase SHALL NOT claim `tuatha/subjects/gaeilge.py` (which
stays in cianfhoghlaim's carved `tuatha/` sub-project). The NI-phase is a context
overlay, not a discrete LC subject package.

#### Scenario: LC Gaeilge requests still route to cianfhoghlaim

- **GIVEN** a consumer requests Leaving Cert Gaeilge content (NI or ROI)
- **WHEN** the dispatcher routes the request
- **THEN** the dispatcher SHALL route to cianfhoghlaim's `tuatha/subjects/gaeilge.py`
- **AND** the `ciancheiltis-en-ga-ni` phase SHALL NOT intercept it
