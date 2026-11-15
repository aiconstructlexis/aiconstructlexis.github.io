"""
Write the release artifact: a network JSON with release metadata and without the internal
bookkeeping that the pipeline stages leave on records.

The output keeps the input's top-level keys in their order and changes four things:

- ``metadata`` becomes ``{name, version, venues, paper_count_by_conference, counts, notes}``,
  where ``counts`` gives the number of in-scope (not ``expert_removed``) constructs,
  measurements and behaviors, the number of relationships (all, and those between in-scope
  entities) and the number of papers.
- Every entity and relationship loses the keys whose name starts with an underscore (the
  stages' working fields, such as the vote diagnostics) plus any key named in
  ``drop_fields``; an empty ``canonical_definition`` is dropped as well. Everything else
  (names, papers, original nodes, evidence, summaries, ``expert_removed`` and its reason) is
  kept unchanged.
- ``expert_removed_reason`` is trimmed and starts with a capital letter.
- ``name_mapping`` is rebuilt from the entities (``build_name_mapping``), replacing the
  network's own, which earlier stages built before curation renamed and merged entities.
  Its keys, sorted, are every canonical name and every surface name in an entity's
  ``original_names``, over all entities including the ``expert_removed`` ones:

  - a canonical name maps to itself, even when another entity also lists it among its
    ``original_names``;
  - any other surface name maps to the canonical name of the one entity that lists it, or,
    when several entities list it, to the sorted list of their canonical names.

  So a value is a string, or a list of two or more canonical names for an ambiguous
  surface name. ``build_name_mapping`` can be re-applied to an existing artifact.

The file is written with ``ensure_ascii=False`` and ``indent=1``.
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple, Union

from aiconstructlexis.util.names import ENTITY_TYPES

logger = logging.getLogger(__name__)

ARTIFACT_NAME = "AI Construct Lexis"
DEFAULT_NOTES = ("Entities flagged expert_removed were extracted by the pipeline and judged out of scope by "
                 "expert review; they are kept for transparency and are not shown in the interface.")


def clean_removed_reason(reason: str) -> Tuple[str, str]:
    """Trim an ``expert_removed_reason`` and capitalise its first letter.

    Returns ``(new_reason, action)`` with ``action`` "kept" or "rewritten".
    """
    text = (reason or "").strip()
    new = text[0].upper() + text[1:] if text else ""
    return new, ("rewritten" if new != (reason or "") else "kept")


def build_name_mapping(network: Dict[str, Any]) -> Dict[str, Union[str, List[str]]]:
    """The release ``name_mapping`` of ``network``, built from its entities only.

    Keys (sorted) are the canonical names and the surface names in ``original_names`` of
    every entity, ``expert_removed`` ones included. A canonical name maps to itself; any
    other surface name maps to the canonical name of the entity that lists it, or to the
    sorted list of canonical names when several entities list it. Blank names are skipped.
    """
    canonical: Set[str] = set()
    listed_by: Dict[str, Set[str]] = {}
    for et in ENTITY_TYPES:
        for g in network.get(et) or []:
            canon = g.get("canonical_name") or ""
            if not canon.strip():
                continue
            canonical.add(canon)
            for name in g.get("original_names") or []:
                if isinstance(name, str) and name.strip():
                    listed_by.setdefault(name, set()).add(canon)
    mapping: Dict[str, Union[str, List[str]]] = {}
    for name in sorted(canonical | set(listed_by)):
        owners = sorted(listed_by.get(name, ()))
        if name in canonical:
            mapping[name] = name
        elif len(owners) == 1:
            mapping[name] = owners[0]
        else:
            mapping[name] = owners
    return mapping


def _strip(record: Dict[str, Any], drop_fields: Iterable[str]) -> int:
    doomed = [k for k in record if k.startswith("_") or k in drop_fields]
    if record.get("canonical_definition", None) == "":
        doomed.append("canonical_definition")
    for key in doomed:
        del record[key]
    return len(doomed)


def build_metadata(net: Dict[str, Any], version: str, venues: List[str], name: str = ARTIFACT_NAME,
                   notes: str = DEFAULT_NOTES) -> Dict[str, Any]:
    """The release ``metadata`` block for ``net``."""
    live_names = set()
    live = {}
    for et in ENTITY_TYPES:
        live[et] = 0
        for g in net.get(et) or []:
            if not g.get("expert_removed"):
                live[et] += 1
                live_names.add(g.get("canonical_name"))
    rels = net.get("relationships") or []
    return {
        "name": name,
        "version": version,
        "venues": list(venues),
        "paper_count_by_conference": dict(net.get("paper_count_by_conference") or {}),
        "counts": {
            "constructs": live["constructs"],
            "measurements": live["measurements"],
            "behaviors": live["behaviors"],
            "relationships": len(rels),
            "relationships_between_in_scope_entities": sum(
                1 for r in rels if r.get("source") in live_names and r.get("target") in live_names),
            "papers": len(net.get("papers") or []),
        },
        "notes": notes,
    }


def clean_network(net: Dict[str, Any], version: str, venues: List[str], name: str = ARTIFACT_NAME,
                  notes: str = DEFAULT_NOTES, drop_fields: Iterable[str] = ()) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Return the cleaned network (a new dict; ``net`` is modified in place) and a report."""
    drop = tuple(drop_fields)
    report = {"entity_fields_removed": 0, "relationship_fields_removed": 0,
              "reasons_kept": 0, "reasons_rewritten": 0}
    for et in ENTITY_TYPES:
        for g in net.get(et) or []:
            report["entity_fields_removed"] += _strip(g, drop)
            if g.get("expert_removed") and "expert_removed_reason" in g:
                new, action = clean_removed_reason(g["expert_removed_reason"])
                g["expert_removed_reason"] = new
                report[f"reasons_{action}"] += 1
    for r in net.get("relationships") or []:
        report["relationship_fields_removed"] += _strip(r, drop)
    net["name_mapping"] = build_name_mapping(net)
    report["name_mapping_keys"] = len(net["name_mapping"])
    report["name_mapping_ambiguous"] = sum(1 for v in net["name_mapping"].values() if isinstance(v, list))

    metadata = build_metadata(net, version, venues, name=name, notes=notes)
    out: Dict[str, Any] = {}
    placed = False
    for key, value in net.items():
        if key == "metadata":
            out[key] = metadata
            placed = True
        else:
            out[key] = value
    if not placed:
        out = {"metadata": metadata, **out}
    report["metadata"] = metadata
    return out, report


def write_release_artifact(network_json: str | Path, out_json: str | Path, version: str, venues: List[str],
                           name: str = ARTIFACT_NAME, notes: str = DEFAULT_NOTES,
                           drop_fields: Iterable[str] = ()) -> Dict[str, Any]:
    """Clean ``network_json`` and write it to ``out_json``. Returns the cleaning report."""
    with open(network_json, encoding="utf-8") as f:
        net = json.load(f)
    out, report = clean_network(net, version, venues, name=name, notes=notes, drop_fields=drop_fields)
    out_path = Path(out_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_name(out_path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    tmp.replace(out_path)
    logger.info("Wrote %s (%d KB): %s", out_path, out_path.stat().st_size // 1024, report["metadata"]["counts"])
    logger.info("Removed %d entity fields and %d relationship fields; reasons kept %d, rewritten %d",
                report["entity_fields_removed"], report["relationship_fields_removed"],
                report["reasons_kept"], report["reasons_rewritten"])
    logger.info("name_mapping: %d names, %d of them listed by several entities",
                report["name_mapping_keys"], report["name_mapping_ambiguous"])
    return report


def main(argv: List[str] | None = None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Write the versioned release artifact from a network JSON.")
    p.add_argument("--input", required=True, help="network JSON produced by the pipeline")
    p.add_argument("--output", required=True, help="where to write the release artifact")
    p.add_argument("--version", required=True, help="release version, e.g. 0.0.1")
    p.add_argument("--venues", nargs="+", required=True, help="venue keys the network was built from, in order")
    p.add_argument("--name", default=ARTIFACT_NAME)
    p.add_argument("--drop-fields", nargs="*", default=[], help="further record keys to leave out")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="export_release_artifact", log_dir=args.log_dir)
    write_release_artifact(args.input, args.output, args.version, args.venues, name=args.name,
                           drop_fields=args.drop_fields)


if __name__ == "__main__":
    main()
