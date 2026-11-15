"""Joining the per-venue networks into one.

- ``union``: cross-venue union at canonical name (``build_joint_network``)
- ``llm_merge``: semantic cross-venue merge with an LLM (``merge_joint_network``)

The functions are imported lazily so that ``python -m aiconstructlexis.join.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "build_joint_network": "union",
    "merge_joint_network": "llm_merge",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)
