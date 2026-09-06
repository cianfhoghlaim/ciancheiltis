"""ciancheiltis.meaisinfhoghlaim.models.teanga_registry — the teanga-specific model registry.

Per the 2026-XX-XX-ciancheiltis-enrichment plan. The teanga surface owns
its own model registry (the 10+ teanga models) that complements the
central cianfhoghlaim registry. The teanga models are loaded into Unsloth
Studio on the bunchloch host and dispatched via the ciancheiltis agent
fleet (Hermes + OpenClaw).
"""
from __future__ import annotations

import os
from typing import Any


# === TEANGA_MODEL_REGISTRY ===
# Each entry: (model_key, model_id, backend, capabilities, hf_repo, unsloth_id, mlx_id)
TEANGA_MODEL_REGISTRY: dict[str, dict[str, Any]] = {
    # === Unsloth GGUF models (Qwen3 family) ===
    "qwen3.8-27b-instruct": {
        "model_key": "qwen3.8-27b-instruct",
        "display_name": "Qwen 3.8 27B Instruct (Unsloth GGUF)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/Qwen3.8-27B-Instruct-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 32768,
        "capabilities": ["text", "chat", "bilingual_translation", "tool_calling"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "Bilingual EN↔GA translation, general chat",
    },
    # === Unsloth GGUF models (Gemma 4 family) ===
    "gemma-4-e4b-it": {
        "model_key": "gemma-4-e4b-it",
        "display_name": "Gemma 4 E4B IT (Unsloth GGUF)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/gemma-4-E4B-it-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 8192,
        "capabilities": ["text", "chat", "alignment_finetune"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "Bilingual alignment fine-tune (fast_align + eflomal)",
    },
    "gemma-4-12b-it": {
        "model_key": "gemma-4-12b-it",
        "display_name": "Gemma 4 12B IT (Unsloth GGUF)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/gemma-4-12B-it-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 8192,
        "capabilities": ["text", "chat", "translation"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "Mid-size bilingual translation",
    },
    "gemma-4-26b-a4b-it": {
        "model_key": "gemma-4-26b-a4b-it",
        "display_name": "Gemma 4 26B-A4B IT (Unsloth GGUF MoE)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/gemma-4-26B-A4B-it-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 16384,
        "capabilities": ["text", "chat", "translation", "bilingual_reasoning"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "High-quality bilingual translation + reasoning",
    },
    # === Unsloth Qwen3-VL (vision-language for HTR) ===
    "qwen3-vl-8b-instruct": {
        "model_key": "qwen3-vl-8b-instruct",
        "display_name": "Qwen 3-VL 8B Instruct (Unsloth GGUF, vision)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/Qwen3-VL-8B-Instruct-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 32768,
        "capabilities": ["vision", "ocr", "htr", "vqa", "multilingual"],
        "languages": ["en", "ga", "cy", "gd", "br", "kw", "gv"],
        "use_case": "HTR (handwritten text recognition) on Duchas.ie manuscripts",
    },
    "qwen3-vl-32b-instruct": {
        "model_key": "qwen3-vl-32b-instruct",
        "display_name": "Qwen 3-VL 32B Instruct (Unsloth GGUF, vision)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/Qwen3-VL-32B-Instruct-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 32768,
        "capabilities": ["vision", "ocr", "htr", "vqa"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "Higher-accuracy HTR on difficult manuscripts",
    },
    # === Unsloth Ministral (compact) ===
    "ministral-8b-instruct": {
        "model_key": "ministral-8b-instruct",
        "display_name": "Ministral 8B Instruct (Unsloth GGUF, compact)",
        "backend": "unsloth_studio",
        "model_id": "unsloth/Ministral-8B-Instruct-GGUF",
        "gguf_variant": "UD-Q4_K_XL",
        "context_length": 8192,
        "capabilities": ["text", "chat", "bilingual_translation"],
        "languages": ["en", "ga", "cy", "gd"],
        "use_case": "Compact edge deployment for mobile/edge translation",
    },
    # === UDPipe-2 (UD parsing) ===
    "udpipe-2-irish-gaeilge": {
        "model_key": "udpipe-2-irish-gaeilge",
        "display_name": "UDPipe-2 Irish (Gaeilge)",
        "backend": "udpipe_2",
        "model_id": "irish-gaeilge",
        "context_length": 0,
        "capabilities": ["ud_parse", "pos_tag", "lemma", "dep_parse"],
        "languages": ["gle"],
        "use_case": "Universal Dependencies parsing for Irish text",
    },
    "udpipe-2-welsh": {
        "model_key": "udpipe-2-welsh",
        "display_name": "UDPipe-2 Welsh (Cymraeg)",
        "backend": "udpipe_2",
        "model_id": "cym",
        "context_length": 0,
        "capabilities": ["ud_parse", "pos_tag", "lemma", "dep_parse"],
        "languages": ["cym"],
        "use_case": "UD parsing for Welsh text",
    },
    "udpipe-2-scottish-gaelic": {
        "model_key": "udpipe-2-scottish-gaelic",
        "display_name": "UDPipe-2 Scottish Gaelic (Gàidhlig)",
        "backend": "udpipe_2",
        "model_id": "gla",
        "context_length": 0,
        "capabilities": ["ud_parse", "pos_tag", "lemma", "dep_parse"],
        "languages": ["gla"],
        "use_case": "UD parsing for Scottish Gaelic text",
    },
    "udpipe-2-breton": {
        "model_key": "udpipe-2-breton",
        "display_name": "UDPipe-2 Breton (Brezhoneg)",
        "backend": "udpipe_2",
        "model_id": "bre",
        "context_length": 0,
        "capabilities": ["ud_parse", "pos_tag", "lemma", "dep_parse"],
        "languages": ["bre"],
        "use_case": "UD parsing for Breton text",
    },
    # === fastText language detection ===
    "fasttext-langdetect-176": {
        "model_key": "fasttext-langdetect-176",
        "display_name": "fastText language identification (176 langs)",
        "backend": "fasttext",
        "model_id": "facebook/fasttext-language-identification",
        "context_length": 0,
        "capabilities": ["lang_detect"],
        "languages": ["all"],
        "use_case": "Language detection for IR/EN/Cym/gla/bre/cor/mnx text",
    },
    # === MMS multilingual speech ===
    "mms-300m-teanga": {
        "model_key": "mms-300m-teanga",
        "display_name": "MMS 300M Teanga (multilingual speech)",
        "backend": "transformers",
        "model_id": "facebook/mms-300m",
        "context_length": 0,
        "capabilities": ["asr", "tts", "lang_detect"],
        "languages": ["gle", "cym", "gla", "bre", "cor", "mnx"],
        "use_case": "ASR/TTS for the 6 Celtic languages",
    },
}


def get_teanga_model(model_key: str) -> dict[str, Any] | None:
    """Get a teanga model by its canonical key."""
    return TEANGA_MODEL_REGISTRY.get(model_key)


def list_teanga_models(language: str | None = None) -> list[str]:
    """List all teanga model keys, optionally filtered by language."""
    if language is None:
        return list(TEANGA_MODEL_REGISTRY.keys())
    return [
        key for key, model in TEANGA_MODEL_REGISTRY.items()
        if language in model.get("languages", [])
    ]


__all__ = [
    "TEANGA_MODEL_REGISTRY",
    "get_teanga_model",
    "list_teanga_models",
]
