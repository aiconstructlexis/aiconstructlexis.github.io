"""
Export a network JSON into the site's data layout.

The site reads one JSON file per entity plus the graph bundle and the paper URLs. This stage
writes all of them under ``<site_dir>/data/``:

  constructs/<slug>.json             one record per in-scope construct
  measurements/<slug>.json           one record per in-scope measurement instrument
  behaviors_tasks/<slug>.json        one record per in-scope behavior
  paper_urls.json                    {paper title: url} built from the paper lists given
  graph.bundle.json                  nodes and de-duplicated edges for the network graph

Per-entity record:
  canonical_name, type (singular), canonical_definition, expert_removed, expert_removed_reason,
  names[], papers[] (flat list of titles), paper_count,
  definitions[{text, papers[], original_name}], definition_count,
  relationships[{direction, other_canonical_name, other_type, relationship_type, paper,
                 evidence, paper_count, paper_weight, papers_by_conference}],
  relationship_count, incoming_relationship_count, outgoing_relationship_count,
  characterization_sections[{label, text}], characterization, characterization_status,
  papers_by_conference, paper_count_by_conference, conferences

Rules:
  - File names are ``aiconstructlexis.util.names.slugify(canonical_name)``; the site's
    JavaScript computes the same slug to fetch a record.
  - ``canonical_definition`` is the labeled summary recomposed from
    ``characterization_sections`` in display order, with the section labels
    (``CHARACTERIZE_SECTION_LABELS``) of the prompt set named by ``prompts`` (default
    "default"); without sections it falls back to the
    stored ``characterization``, then ``canonical_definition``, then the first definition
    among the original nodes.
  - ``definitions`` holds one entry per surface name (``original_name``) that has a
    definition. The text is the first definition extracted for that surface name; ``papers``
    is the paper it was extracted from when the node records ``definition_paper``, and
    otherwise every paper that used the name, in the order the node stores them.
  - Each relationship between two in-scope entities is listed on both endpoints, as outgoing
    on the source and incoming on the target, with the partner's type; ``relationship_count``
    and the two direction counts count these.
  - Entities flagged ``expert_removed`` get no file: the site cannot reach them, and the
    network JSON keeps their records. Relationships touching one are left out of the records
    of their in-scope partners, since the site has no page to link to. The graph bundle omits
    the removed entities and every edge touching one; edges are de-duplicated by
    (source, target, type).
  - ``paper_urls.json`` takes the first URL seen for a title, in the order the paper lists
    are given.
  - ``backup=True`` moves the paths this stage writes (the three entity folders,
    ``paper_urls.json`` and ``graph.bundle.json``) into ``<site_dir>/data.backup-<timestamp>/``
    first; the other files under ``data/`` (the hand-maintained ``empirical_evidence.json``,
    the readable pages, the analysis bundle and the layout) stay where they are.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List

from aiconstructlexis.prompts import DEFAULT_PROMPT_SET, load_prompts
from aiconstructlexis.util.names import DATA_SUBDIR, ENTITY_TYPES, SITE_SUBDIR, TYPE_SINGULAR, slugify

logger = logging.getLogger(__name__)

SUBDIR = SITE_SUBDIR
PAPER_URLS_FILE = "paper_urls.json"
GRAPH_BUNDLE_FILE = "graph.bundle.json"


def papers_to_pbc(papers: List[Any]) -> Dict[str, List[str]]:
    """Group a paper list into {conference: [title, ...]} without duplicates."""
    out: Dict[str, List[str]] = defaultdict(list)
    seen: Dict[str, set] = defaultdict(set)
    for p in papers or []:
        if isinstance(p, dict):
            conf = p.get("conference") or "_unknown"
            paper = p.get("paper") or ""
        elif isinstance(p, list) and len(p) == 2:
            conf, paper = p
        else:
            conf, paper = "_unknown", str(p)
        if paper and paper not in seen[conf]:
            out[conf].append(paper)
            seen[conf].add(paper)
    return dict(out)


def flat_paper_titles(pbc: Dict[str, List[str]]) -> List[str]:
    """Return de-duplicated flat list of paper titles across conferences."""
    seen, out = set(), []
    for conf in sorted(pbc.keys()):
        for p in pbc[conf]:
            if p not in seen:
                out.append(p)
                seen.add(p)
    return out


def paper_titles(papers: List[Any]) -> List[str]:
    """The titles of a paper list ({conference, paper} dicts, [conference, title] pairs or
    plain titles) in the stored order, without duplicates."""
    out: List[str] = []
    for p in papers or []:
        if isinstance(p, dict):
            title = p.get("paper") or ""
        elif isinstance(p, (list, tuple)) and len(p) == 2:
            title = p[1]
        else:
            title = str(p)
        if title and title not in out:
            out.append(title)
    return out


def build_definitions(g: Dict[str, Any]) -> List[Dict[str, Any]]:
    """One {text, papers, original_name} per surface name with a definition.

    The text is the first definition extracted for the surface name. ``papers`` is the paper
    it came from when the node records ``definition_paper``; otherwise it is every paper that
    used the name, in the stored order, since the stored definition is not tied to one of them.
    """
    out: List[Dict[str, Any]] = []
    for orig_name, node in (g.get("original_nodes") or {}).items():
        d = (node.get("definition") or "").strip()
        if not d:
            continue
        source = (node.get("definition_paper") or "").strip()
        papers = [source] if source else paper_titles(node.get("papers") or [])
        out.append({"text": d, "papers": papers, "original_name": orig_name})
    return out


def build_entity_record(g: Dict[str, Any], etype: str, rels_by_canon: Dict[str, List[Dict[str, Any]]],
                        section_labels: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """The per-entity site record for entity ``g`` of type ``etype`` (plural key).

    ``section_labels`` is a prompt set's ``CHARACTERIZE_SECTION_LABELS``; when it is None the
    labels of the default prompt set are used.
    """
    if section_labels is None:
        section_labels = load_prompts(DEFAULT_PROMPT_SET).CHARACTERIZE_SECTION_LABELS
    canon = (g.get("canonical_name") or "").strip()
    pbc = g.get("papers_by_conference") or papers_to_pbc(g.get("papers") or [])
    paper_count = sum(len(v) for v in pbc.values()) if pbc else g.get("paper_count", 0)
    papers_flat = flat_paper_titles(pbc)

    # canonical_definition = the synthesized summary (or a fallback).
    canon_def = (g.get("characterization") or "").strip()
    # Recompose the labeled summary from its sections so the current display labels are
    # used (the stored text keeps the labels it was written with).
    sections = g.get("characterization_sections") or {}
    labeled = [f"{label} {sections[key].strip()}" for key, label in section_labels[etype]
               if isinstance(sections.get(key), str) and sections[key].strip()]
    if labeled:
        canon_def = "\n\n".join(labeled)
    is_placeholder = not canon_def
    if is_placeholder:
        canon_def = (g.get("canonical_definition") or "").strip()
    if not canon_def:
        for _, node in (g.get("original_nodes") or {}).items():
            d = (node.get("definition") or "").strip()
            if d:
                canon_def = d
                break

    # Relationships involving this entity
    rels_for_node: List[Dict[str, Any]] = []
    in_count = out_count = 0
    for r in rels_by_canon.get(canon, []):
        is_outgoing = r["source"] == canon
        other = r["target"] if is_outgoing else r["source"]
        rel_pbc = r.get("papers_by_conference") or papers_to_pbc(r.get("papers") or [])
        first_paper = ""
        if rel_pbc:
            first_conf = next(iter(rel_pbc))
            ps = rel_pbc[first_conf]
            if ps:
                first_paper = ps[0]
        first_evidence = ""
        for e in (r.get("evidence") or []):
            if isinstance(e, str) and e.strip():
                first_evidence = e.strip()
                break
            if isinstance(e, dict):
                t = (e.get("evidence") or e.get("text") or "").strip()
                if t:
                    first_evidence = t
                    break
        other_type = r.get("_other_type", "")
        rels_for_node.append({
            "direction": "outgoing" if is_outgoing else "incoming",
            "other_canonical_name": other,
            "other_type": other_type,
            "relationship_type": r.get("type", ""),
            "paper": first_paper,
            "evidence": first_evidence,
            "paper_count": r.get("paper_count", 0),
            # Vote-weighted paper count (type shares from the relationship vote).
            "paper_weight": r.get("paper_weight", r.get("paper_count", 0)),
            "papers_by_conference": rel_pbc,
        })
        if is_outgoing:
            out_count += 1
        else:
            in_count += 1

    return {
        "canonical_name": canon,
        "type": TYPE_SINGULAR[etype],
        "canonical_definition": canon_def,
        "expert_removed": bool(g.get("expert_removed")),
        "expert_removed_reason": g.get("expert_removed_reason", "") if g.get("expert_removed") else "",
        "names": g.get("original_names") or [canon],
        "papers": papers_flat,
        "paper_count": paper_count,
        "definitions": build_definitions(g),
        "definition_count": len([d for d in (g.get("original_nodes") or {}).values() if (d.get("definition") or "").strip()]),
        "relationships": rels_for_node,
        "relationship_count": len(rels_for_node),
        "incoming_relationship_count": in_count,
        "outgoing_relationship_count": out_count,
        # Summary sections in display order with their labels.
        "characterization_sections": [{"label": label, "text": (g.get("characterization_sections") or {})[key]}
                                      for key, label in section_labels[etype]
                                      if (g.get("characterization_sections") or {}).get(key)],
        "characterization": "" if is_placeholder else canon_def,
        "characterization_status": "placeholder" if is_placeholder else "llm",
        "papers_by_conference": pbc,
        "paper_count_by_conference": {c: len(v) for c, v in pbc.items()},
        "conferences": sorted(pbc.keys()),
    }


def build_paper_urls(paper_lists: Iterable[str | Path]) -> Dict[str, str]:
    """{title: url} from paper-list JSON files; the first URL seen for a title wins.

    Each file holds a list (or a dict of) records with ``title`` (or ``name``) and ``url``
    (or ``pdf_url`` / ``openreview_url``). Files that are missing or unreadable are skipped.
    """
    url_by_title: Dict[str, str] = {}
    for f in paper_lists:
        path = Path(f)
        if not path.exists():
            logger.warning("Paper list %s not found; skipped", path)
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            logger.warning("Paper list %s could not be read (%s); skipped", path, e)
            continue
        items = list(data.values()) if isinstance(data, dict) else data
        for p in items:
            if not isinstance(p, dict):
                continue
            title = (p.get("name") or p.get("title") or "").strip()
            url = (p.get("url") or p.get("pdf_url") or p.get("openreview_url") or "").strip()
            if title and url and title not in url_by_title:
                url_by_title[title] = url
    return url_by_title


_LATEX_CMD = re.compile(r"\\(?:textit|textbf|textsc|textrm|texttt|emph|text|mathcal|mathbf|mathrm|mathit|mathsf|rm|bf|it|sc)")
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def title_key(title: str) -> str:
    """Spelling-insensitive key of a paper title.

    Titles taken from a PDF can differ from the proceedings listing in spacing, LaTeX
    markup, quotes, dashes, accents and Unicode variants of letters (ligatures, full-width
    forms); the key drops all of that.
    """
    t = unicodedata.normalize("NFKD", title or "")
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = _LATEX_CMD.sub("", t).lower()
    return _NON_ALNUM.sub("", t)


def match_paper_urls(url_by_title: Dict[str, str], titles: Iterable[str]) -> Dict[str, str]:
    """Extend ``url_by_title`` with the given titles that have no exact entry but match one
    paper-list title after normalization (``title_key``). Ambiguous keys are left out."""
    by_key: Dict[str, List[str]] = defaultdict(list)
    for t in url_by_title:
        by_key[title_key(t)].append(t)
    out = dict(url_by_title)
    for t in titles:
        if not t or t in out:
            continue
        hits = by_key.get(title_key(t)) or []
        if len({url_by_title[h] for h in hits}) == 1:
            out[t] = url_by_title[hits[0]]
    return out


def network_paper_titles(net: Dict[str, Any]) -> List[str]:
    """Every paper title the network refers to (corpus list, entities, relationships)."""
    titles: Dict[str, None] = {}
    for p in net.get("papers") or []:
        t = p.get("paper") if isinstance(p, dict) else (p[1] if isinstance(p, list) and len(p) == 2 else p)
        if t:
            titles[str(t)] = None
    for et in ENTITY_TYPES:
        for g in net.get(et) or []:
            for ps in (g.get("papers_by_conference") or {}).values():
                for t in ps:
                    titles[t] = None
    for r in net.get("relationships") or []:
        for ps in (r.get("papers_by_conference") or {}).values():
            for t in ps:
                titles[t] = None
    return list(titles)


def export_site_data(network_json: str | Path, site_dir: str | Path, paper_lists: Iterable[str | Path] = (),
                     backup: bool = False, prompts: str = DEFAULT_PROMPT_SET) -> Dict[str, int]:
    """Write the site's data files from ``network_json`` into ``<site_dir>/data``.

    ``paper_lists`` are the screened paper-list JSON files (title, url) whose URLs the site
    links to; ``backup=True`` moves the files this function would overwrite aside first.
    ``prompts`` names the prompt set ("default" or a dotted module path) whose
    ``CHARACTERIZE_SECTION_LABELS`` label the summary sections.
    Returns counts of the files written and of the graph bundle's nodes and edges.
    """
    section_labels = load_prompts(prompts).CHARACTERIZE_SECTION_LABELS
    in_path = Path(network_json)
    site = Path(site_dir)
    out_dir = site / DATA_SUBDIR

    if backup:
        written_paths = [out_dir / SUBDIR[et] for et in SUBDIR] + [out_dir / PAPER_URLS_FILE, out_dir / GRAPH_BUNDLE_FILE]
        existing = [p for p in written_paths if p.exists()]
        if existing:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = site / f"{DATA_SUBDIR}.backup-{ts}"
            backup_dir.mkdir(parents=True)
            for p in existing:
                shutil.move(str(p), str(backup_dir / p.name))
            logger.info("Moved the previous %d export path(s) to %s", len(existing), backup_dir)

    out_dir.mkdir(parents=True, exist_ok=True)
    for et in SUBDIR:
        d = out_dir / SUBDIR[et]
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    with open(in_path, encoding="utf-8") as f:
        net = json.load(f)
    logger.info("Loaded %s", in_path)

    # canonical name -> entity type of the in-scope entities (for the partner type of each
    # relationship); the removed ones have no page, so no record points at them.
    name_type: Dict[str, str] = {}
    for et in ENTITY_TYPES:
        for g in net.get(et) or []:
            cn = (g.get("canonical_name") or "").strip()
            if cn and not g.get("expert_removed"):
                name_type[cn] = et

    # Index the relationships between in-scope entities by canonical name (both endpoints)
    rels_by_canon: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for r in net.get("relationships") or []:
        src = (r.get("source") or "").strip()
        tgt = (r.get("target") or "").strip()
        if src not in name_type or tgt not in name_type:
            continue
        r_for_src = dict(r); r_for_src["_other_type"] = SUBDIR.get(name_type.get(tgt, ""), "")
        r_for_tgt = dict(r); r_for_tgt["_other_type"] = SUBDIR.get(name_type.get(src, ""), "")
        rels_by_canon[src].append(r_for_src)
        rels_by_canon[tgt].append(r_for_tgt)

    # Per-entity files of the in-scope entities; the removed ones stay in the network JSON only.
    records: Dict[str, List[Dict[str, Any]]] = {et: [] for et in ENTITY_TYPES}
    skipped = 0
    for et in ENTITY_TYPES:
        for g in (net.get(et) or []):
            if g.get("expert_removed"):
                skipped += 1
                continue
            rec = build_entity_record(g, et, rels_by_canon, section_labels)
            with open(out_dir / SUBDIR[et] / f"{slugify(rec['canonical_name'])}.json", "w") as f:
                json.dump(rec, f, indent=2)
            records[et].append(rec)
        records[et].sort(key=lambda rec: slugify(rec["canonical_name"]))
    logger.info("Entities flagged expert_removed, not exported: %d", skipped)

    # Paper title -> URL, so the site links to the paper instead of a web search.
    url_by_title = match_paper_urls(build_paper_urls(paper_lists), network_paper_titles(net))
    url_path = out_dir / PAPER_URLS_FILE
    with open(url_path, "w") as f:
        json.dump(url_by_title, f)
    logger.info("paper_urls.json: %d titles with a URL (%d KB)", len(url_by_title), url_path.stat().st_size // 1024)

    # Graph bundle: only what the network graph needs (name, type, paper count, names,
    # a trimmed summary for hovers, and edges), so it loads fast.
    graph_nodes = []
    seen_canon = set()
    for et in ENTITY_TYPES:
        sing = TYPE_SINGULAR[et]
        for rec in records[et]:
            cn = rec["canonical_name"]
            if not cn or cn in seen_canon:
                continue
            seen_canon.add(cn)
            cd = (rec.get("canonical_definition") or "").strip()
            graph_nodes.append({
                "name": cn,
                "type": sing,
                "paper_count": rec.get("paper_count", 0),
                "names": rec.get("names") or [],
                "definition": cd[:1200],  # tooltip text, capped
            })
    # Edges: de-duplicated by (source, target, type); both endpoints must be graph nodes.
    graph_edges = []
    seen_edges = set()
    for r in (net.get("relationships") or []):
        s = (r.get("source") or "").strip()
        t = (r.get("target") or "").strip()
        if s not in seen_canon or t not in seen_canon or s == t:
            continue
        rt = (r.get("type") or "").strip()
        key = (s, t, rt)
        if key in seen_edges:
            continue
        seen_edges.add(key)
        graph_edges.append({
            "source": s,
            "target": t,
            "type": rt,
            "paper_count": r.get("paper_count", 0),
        })
    graph_payload = {"nodes": graph_nodes, "edges": graph_edges,
                     "schema_version": 1, "node_count": len(graph_nodes), "edge_count": len(graph_edges)}
    graph_path = out_dir / GRAPH_BUNDLE_FILE
    with open(graph_path, "w") as f:
        json.dump(graph_payload, f, indent=2)
    logger.info("bundle graph.bundle.json: %d nodes, %d edges, %d KB",
                len(graph_nodes), len(graph_edges), graph_path.stat().st_size // 1024)

    logger.info("Wrote %s", out_dir)
    for et in ENTITY_TYPES:
        logger.info("  %s: %d files", SUBDIR[et], len(records[et]))

    placeholder_count = sum(1 for et in ENTITY_TYPES for rec in records[et]
                            if rec["characterization_status"] == "placeholder")
    logger.info("Entities without a synthesized summary (placeholder canonical_definition): %d", placeholder_count)

    return {
        "constructs": len(records["constructs"]),
        "measurements": len(records["measurements"]),
        "behaviors": len(records["behaviors"]),
        "paper_urls": len(url_by_title),
        "graph_nodes": len(graph_nodes),
        "graph_edges": len(graph_edges),
        "placeholders": placeholder_count,
    }


def main(argv: List[str] | None = None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Export a network JSON into the site's data layout.")
    p.add_argument("--input", required=True, help="network JSON (the release artifact or a pipeline output)")
    p.add_argument("--site", required=True, help="site directory; data goes under its data/")
    p.add_argument("--paper-lists", nargs="*", default=[],
                   help="paper-list JSON files (title, url) used for paper_urls.json, in priority order")
    p.add_argument("--backup", action="store_true",
                   help="move the entity folders, paper_urls.json and graph.bundle.json of an existing data/ "
                        "aside before writing")
    p.add_argument("--prompts", default=DEFAULT_PROMPT_SET,
                   help="prompt set whose summary section labels are used: 'default' or a dotted module path")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="export_site_data", log_dir=args.log_dir)
    counts = export_site_data(args.input, args.site, args.paper_lists, backup=args.backup, prompts=args.prompts)
    logger.info("Done: %s", counts)


if __name__ == "__main__":
    main()
