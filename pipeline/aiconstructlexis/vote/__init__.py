"""Majority votes and consolidation on harmonized networks.

- ``entities``: canonical-level entity vote for one venue (``vote_entities``)
- ``filter``: minimum-paper filter before the join (``filter_min_papers``)
- ``joint_entities``: the entity vote across venues on the joint network
  (``vote_joint_entities``)
- ``relationships``: pair-level relationship vote, strictest type wins
  (``vote_relationships``; also ``guard_target``, the relationship type guard)
- ``pair_types``: one relationship type per unordered entity pair
  (``consolidate_pair_types``)

The functions are imported lazily so that ``python -m aiconstructlexis.vote.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "vote_entities": "entities",
    "filter_min_papers": "filter",
    "vote_joint_entities": "joint_entities",
    "vote_relationships": "relationships",
    "guard_target": "relationships",
    "consolidate_pair_types": "pair_types",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)
