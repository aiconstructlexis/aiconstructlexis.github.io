"""Ingest stage: paper lists and PDFs for one venue.

Three downloaders write the same paper-list JSON (a list of ``{name, url,
path, ...}`` dicts; see ``aiconstructlexis.ingest.proceedings``):

- ``download_venue``: proceedings.iclr.cc / proceedings.neurips.cc, PMLR by
  conference and year, or the OpenReview API.
- ``download_anthology``: one ACL Anthology main-conference volume.
- ``download_pmlr``: one PMLR volume by number.
- ``download_listed``: the papers of an existing (screened) paper list.

The functions are imported on first use, so each submodule can also run as
``python -m aiconstructlexis.ingest.<module>`` without a double import.
"""
from __future__ import annotations

import importlib

__all__ = ["download_venue", "download_anthology", "download_pmlr", "download_listed"]

_HOME = {
    "download_venue": "aiconstructlexis.ingest.proceedings",
    "download_anthology": "aiconstructlexis.ingest.anthology",
    "download_pmlr": "aiconstructlexis.ingest.pmlr",
    "download_listed": "aiconstructlexis.ingest.listed",
}


def __getattr__(name: str):
    if name in _HOME:
        return getattr(importlib.import_module(_HOME[name]), name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(set(globals()) | set(_HOME))
