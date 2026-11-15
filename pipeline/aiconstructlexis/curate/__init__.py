"""Curation: reviewer operations applied as an overlay, and catalog invariants."""
from __future__ import annotations

import importlib

_EXPORTS = {
    "OverlayError": "overlay",
    "apply_entity_operations": "overlay",
    "apply_overlay": "overlay",
    "apply_relationship_operations": "overlay",
    "read_overlay": "overlay",
    "drop_orphan_definitions": "cleanup",
    "drop_orphans": "cleanup",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)
