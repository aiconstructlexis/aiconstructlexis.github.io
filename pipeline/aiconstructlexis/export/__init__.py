"""Export stages: from a network JSON to the release artifact and the site's data files.

- ``write_release_artifact``: the cleaned, versioned Lexis JSON.
- ``export_site_data``: per-entity JSON files of the in-scope entities (with their
  relationships to other in-scope entities), paper URLs and graph bundle under
  ``<site_dir>/data/``.
- ``write_readable``: the Markdown mirror under ``<site_dir>/data/readable/``.
- ``build_analysis_bundle``: the compact files behind the analysis tools page.
- ``build_graph_layout``: the precomputed layout of the interactive network page.
- ``check_site_export``: consistency check of the site's data against its network JSON,
  covering the files the pages read.

The functions are imported lazily so that ``python -m aiconstructlexis.export.<module>``
runs without importing the whole subpackage first.
"""
from __future__ import annotations

import importlib

_EXPORTS = {
    "write_release_artifact": "release_artifact",
    "export_site_data": "site_data",
    "build_paper_urls": "site_data",
    "write_readable": "readable",
    "build_analysis_bundle": "analysis_bundle",
    "build_graph_layout": "graph_layout",
    "check_site_export": "check",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module = _EXPORTS.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f"{__name__}.{module}"), name)
