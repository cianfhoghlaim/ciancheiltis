"""ciancheiltis.dlt_sources.language — canonical entry point for ALL teanga sources.

Per the 2026-XX-XX-ciancheiltis-enrichment plan + the bilingual
educational carve rule (v2 plan §A + parent change
`2026-08-24-dlt-sources-to-multi-repo-scaffold-v1` §21.3):

**Carved from cianfhoghlaim to Ciancheiltis:**
- `dlt_sources.lexicographic/` — ainm + canuint + logainm + tearma + UD
- `dlt_sources.cultural_heritage/` — duchas + gaois + heritage

**New in Ciancheiltis (this enrichment):**
- `dlt_sources.language.eur_lex` — EU IR-EN legal parallel corpus
- `dlt_sources.language.ncca_syllabus` — NCCA LC bilingual EN+GA syllabus
- `dlt_sources.language.wikipedia_teanga` — Wikipedia IR+cym+gla+bre+cor+mnx
- `dlt_sources.language.clarin` — CLARIN-UK + CLARIN-Ireland VLO
- `dlt_sources.language.ud_parse` — Universal Dependencies for 6 Celtic langs
- `dlt_sources.language.lcga_exam_papers` — LCGÁ Irish-medium school papers

**Helpers (also new in Ciancheiltis):**
- `dlt_sources.language._helpers` — IIIF, TEI-XML, ISO 639-3, UD, Wikipedia
  bilingual sentence alignment

The cianfhoghlaim-side `dlt_sources/language/__init__.py` retains the
full 3-package re-export for backwards compat (it pulls local_archive
from cianfhoghlaim proper).

**Landing schemas:**
- `ciancheiltis.language.lexicographic` (already there)
- `ciancheiltis.language.cultural_heritage` (already there)
- `ciancheiltis.language.eur_lex` (NEW)
- `ciancheiltis.language.ncca_syllabus` (NEW)
- `ciancheiltis.language.wikipedia` (NEW)
- `ciancheiltis.language.clarin` (NEW)
- `ciancheiltis.language.ud_treebanks` (NEW)
- `ciancheiltis.language.lcga_papers` (NEW)
"""
from dlt_sources.lexicographic import *  # noqa: F401,F403
from dlt_sources.cultural_heritage import *  # noqa: F401,F403

# New in Ciancheiltis per the 2026-XX-XX-ciancheiltis-enrichment plan
from dlt_sources.language._helpers import (  # noqa: F401
    get_http_client,
    get_iiif_dimensions,
    parse_iiif_url,
    parse_tei_xml_transcription,
    ISO_6393_GAELIC,
    is_gaelic_lang,
    validate_lang_code,
    CONLLU_COLUMNS,
    parse_conllu_file,
    WIKIPEDIA_API_BASE,
    wikipedia_search,
    extract_sentences,
    compute_alignment_score,
)
from dlt_sources.language.eur_lex import eur_lex_source  # noqa: F401
from dlt_sources.language.ncca_syllabus import ncca_syllabus_source  # noqa: F401
from dlt_sources.language.wikipedia_teanga import wikipedia_teanga_source  # noqa: F401
from dlt_sources.language.clarin import clarin_source  # noqa: F401
from dlt_sources.language.ud_parse import ud_parse_source  # noqa: F401
from dlt_sources.language.lcga_exam_papers import lcga_exam_papers_source  # noqa: F401
