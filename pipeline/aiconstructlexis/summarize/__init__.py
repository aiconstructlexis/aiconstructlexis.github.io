"""Summaries: per-entity sectioned summaries through a batch API, and checks on them.

The functions are imported lazily so that ``python -m aiconstructlexis.summarize.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "attach_results": "characterize",
    "build_entity_context": "characterize",
    "build_requests": "characterize",
    "compose_sections": "characterize",
    "check": "checks",
    "check_characterizations": "checks",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)

