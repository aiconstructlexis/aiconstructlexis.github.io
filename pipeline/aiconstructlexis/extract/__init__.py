"""Extraction stage: per-paper entities and relationships from a panel of models.

``run_extraction`` sends each paper to every model of the panel in two passes
(entities, then relationships) through the providers' batch APIs and votes
across models; ``aiconstructlexis.extract.simplify`` reduces its output to the
fields the harmonization stages read. ``aiconstructlexis.extract.batch`` holds the request builders,
provider batch helpers and per-paper vote functions they share.

The functions are imported lazily so that ``python -m aiconstructlexis.extract.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "ExtractionIncomplete": "multi_model",
    "run_extraction": "multi_model",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)

