"""Harmonization: from per-paper surface names to canonical entities and relationships.

Three stages, run in this order on one venue's simplified extraction:

- ``aggregator.harmonize``: an LLM groups the surface names of each entity type into
  canonical entities (batched grouping, hierarchical cross-batch merge) and builds the
  original-name -> canonical-name mapping; its relationship list is left empty.
- ``relationships.aggregate_relationships``: deterministic aggregation of the raw
  relationships at the canonical level (symmetric types folded, self-loops dropped,
  evidence and papers unioned).
- ``residuals.collapse_residuals``: deterministic collapse of canonical names that are
  still surface variants of each other, followed by a rebuild of the name mapping and
  of the relationships.

``batching.make_batches`` packs names into LLM batches by token signature, so surface
variants and thematic neighbours sit together; the aggregator and the join stage use it.

The functions are imported lazily so that ``python -m aiconstructlexis.harmonize.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "harmonize": "aggregator",
    "aggregate_relationships": "relationships",
    "collapse_residuals": "residuals",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)
