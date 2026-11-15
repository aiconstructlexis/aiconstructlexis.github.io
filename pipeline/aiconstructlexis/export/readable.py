"""
Write the Markdown mirror of the site's per-entity records.

Reads the per-entity JSON records written by ``aiconstructlexis.export.site_data`` under
``<site_dir>/data/{constructs,measurements,behaviors_tasks}/<slug>.json``
and the paper URLs in ``<site_dir>/data/paper_urls.json``, and writes
one ``<slug>.md`` per record into the same three subdirectories of the output directory
(default ``<site_dir>/data/readable/``). Records flagged ``expert_removed`` get no page.
The three output subdirectories are emptied first, so no file from an earlier export
survives.

Each page has the entity's name, type, number of supporting papers (the record's
``paper_count``, else the length of its ``papers``) and aliases, the "State of the Field"
summary (its labeled sections), the definitions ("Sources": one per surface name, headed by
that name and the papers that use it, each linked when its URL is known; the text is the
first definition extracted for the name), and the relationships the record holds:
outgoing, incoming, and symmetric "related" pairs (both directions merged) under
"Associated with".

Each relationship entry gives the partner, its type, the relationship type and the number
of papers, then lists every paper of the relationship (the titles in the record's
``papers_by_conference``, venue by venue, plus its ``paper``), linked when the URL is known.
When the record has per-paper quotes (``evidence_by_paper``: ``[{paper, quote}]``), each
paper is followed by its quote. Otherwise the record's one quote (``evidence``) is shown
once, above the list, since the record does not say which paper it comes from. The site
export limits a record's relationships to partners that are in-scope entities, so every
partner a page names has a page of its own.
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
from pathlib import Path
from typing import Any, Dict, List
from aiconstructlexis.util.names import DATA_SUBDIR, READABLE_SUBDIR

logger = logging.getLogger(__name__)

ENTITY_SUBDIRS = ("constructs", "measurements", "behaviors_tasks")

# Display label of a relationship partner's type, keyed on the site subdirectory that the
# record's other_type field holds.
PARTNER_TYPE_LABELS = {
    "constructs": "construct",
    "measurements": "measurement instrument",
    "behaviors_tasks": "behavioral indicator",
}


def load_paper_urls(path: Path) -> Dict[str, str]:
    """Read the plain {paper title: url} map written by the site export."""
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if isinstance(v, str) and v}


def _fmt_type(raw: str) -> str:
    """Display label of a record's type ("construct", "measurement" or "behavior")."""
    return {
        "construct": "Construct",
        "measurement": "Measurement instrument",
        "behavior": "Behavioral indicator",
    }.get(raw, raw.replace("_", " ").title())


def _fmt_partner_type(subdir: str) -> str:
    """Display label of a relationship partner's type, given its site subdirectory."""
    return PARTNER_TYPE_LABELS.get(subdir, subdir.replace("_", " "))


def _paper_link(title: str, urls: Dict[str, str]) -> str:
    url = urls.get(title, "")
    if url:
        return f"[{title}]({url})"
    return title


def _rel_type_label(t: str) -> str:
    return t if t else "related"


def _title(p: Any) -> str:
    """A paper title, as stored, from a plain title or a {conference, paper} entry ("" if blank)."""
    if isinstance(p, dict):
        p = p.get("paper") or ""
    return p if isinstance(p, str) and p.strip() else ""


def _relationship_papers(r: Dict[str, Any]) -> List[str]:
    """Every paper title of a relationship record, without repeats: ``papers_by_conference``
    venue by venue, then ``papers`` and ``paper``, then the papers of ``evidence_by_paper``."""
    titles: List[str] = []
    for ps in (r.get("papers_by_conference") or {}).values():
        titles.extend(_title(p) for p in ps or [])
    titles.extend(_title(p) for p in r.get("papers") or [])
    titles.append(_title(r.get("paper")))
    titles.extend(_title(e) for e in r.get("evidence_by_paper") or [] if isinstance(e, dict))
    return list(dict.fromkeys(t for t in titles if t))


def _quotes_by_paper(r: Dict[str, Any]) -> Dict[str, str]:
    """{paper title: quote} from the record's ``evidence_by_paper``, first quote per paper."""
    out: Dict[str, str] = {}
    for e in r.get("evidence_by_paper") or []:
        if not isinstance(e, dict):
            continue
        title, quote = _title(e), (e.get("quote") or "").strip()
        if title and quote:
            out.setdefault(title, quote)
    return out


def _loose_quotes(r: Dict[str, Any]) -> List[str]:
    """The record's ``evidence``: one quote (a string) or a list of quotes."""
    ev = r.get("evidence")
    items = [ev] if isinstance(ev, str) else (ev or [])
    return list(dict.fromkeys(q.strip() for q in items if isinstance(q, str) and q.strip()))


def _relationship_entry(r: Dict[str, Any]) -> Dict[str, Any]:
    return {"other_canonical_name": r.get("other_canonical_name", "?"),
            "other_type": r.get("other_type", ""),
            "relationship_type": _rel_type_label(r.get("relationship_type", "")),
            "direction": r.get("direction", ""),
            "papers": _relationship_papers(r),
            "quotes_by_paper": _quotes_by_paper(r),
            "quotes": _loose_quotes(r)}


def _merge_relationships(rels: List[Dict[str, Any]], name: str) -> List[Dict[str, Any]]:
    """One entry per relationship, with the two directions of a symmetric "related" pair
    merged into one entry (``merged``) that holds the papers and quotes of both."""
    related: Dict[str, Dict[str, Any]] = {}
    out: List[Dict[str, Any]] = []
    for r in rels:
        entry = _relationship_entry(r)
        if entry["relationship_type"] != "related":
            out.append(entry)
            continue
        key = "||".join(sorted([name.lower(), entry["other_canonical_name"].lower()]))
        if key not in related:
            related[key] = dict(entry, direction="", merged=True)
            continue
        seen = related[key]
        seen["papers"] = list(dict.fromkeys(seen["papers"] + entry["papers"]))
        for title, quote in entry["quotes_by_paper"].items():
            seen["quotes_by_paper"].setdefault(title, quote)
        seen["quotes"] = list(dict.fromkeys(seen["quotes"] + entry["quotes"]))
    return out + list(related.values())


def _render_relationship(entry: Dict[str, Any], urls: Dict[str, str], show_type: bool = True) -> List[str]:
    """The Markdown lines of one relationship entry (see the module docstring)."""
    papers = entry["papers"]
    head = f"- **{entry['other_canonical_name']}** ({_fmt_partner_type(entry['other_type'])})"
    if show_type:
        head += f": *{entry['relationship_type']}*"
    if papers:
        head += f", {len(papers)} paper{'s' if len(papers) != 1 else ''}"
    lines = [head]
    by_paper = entry["quotes_by_paper"]
    if by_paper:
        for p in papers:
            lines.append(f"  - {_paper_link(p, urls)}")
            if by_paper.get(p):
                lines.append(f"    > {by_paper[p]}")
        return lines
    for i, q in enumerate(entry["quotes"]):
        if i:
            lines.append("  >")       # keeps two quotes apart as two paragraphs of the blockquote
        lines.append(f"  > {q}")
    lines.extend(f"  - {_paper_link(p, urls)}" for p in papers)
    return lines


def render_node(node: Dict[str, Any], urls: Dict[str, str]) -> str:
    """Render a single entity record as Markdown."""
    lines: List[str] = []
    name = node.get("canonical_name", "Unnamed")
    ntype = _fmt_type(node.get("type", ""))

    n_papers = node.get("paper_count") or len(node.get("papers") or [])

    lines.append(f"# {name}")
    lines.append(f"**Type:** {ntype}  ")
    lines.append(f"**Supporting papers:** {n_papers}  ")

    names = node.get("names", [])
    aliases = [n for n in names if n != name]
    if aliases:
        lines.append(f"**Also known as:** {', '.join(aliases)}  ")

    characterization = node.get("characterization", "")
    sections = node.get("characterization_sections") or []
    if characterization or sections:
        lines.append("")
        lines.append("## State of the Field")
        if sections:
            for s in sections:
                lines.append("")
                lines.append(f"**{s['label']}** {s['text']}")
        else:
            lines.append("")
            lines.append(characterization)

    defs = node.get("definitions", [])
    if defs:
        lines.append("")
        lines.append("## Sources")
        for d in defs:
            text = d.get("text", "")
            papers = d.get("papers", [])
            orig_name = d.get("original_name") or name

            lines.append("")
            header = f"**{orig_name}**"
            if papers:
                links = ", ".join(_paper_link(p, urls) for p in papers)
                header += f" ({len(papers)} paper{'s' if len(papers) != 1 else ''}: {links})"
            lines.append(header)
            if text:
                lines.append(f"> {text}")

    rels = node.get("relationships", [])
    if rels:
        merged = _merge_relationships(rels, name)
        sections = [
            (f"### {name} \u2192", [e for e in merged if not e.get("merged") and e["direction"] == "outgoing"], True),
            (f"### \u2192 {name}", [e for e in merged if not e.get("merged") and e["direction"] == "incoming"], True),
            ("### Associated with", [e for e in merged if e.get("merged")], False),
        ]
        if any(entries for _, entries, _ in sections):
            lines.append("")
            lines.append("## Relationships")
        for heading, entries, show_type in sections:
            if not entries:
                continue
            lines.append("")
            lines.append(heading)
            for entry in entries:
                lines.extend(_render_relationship(entry, urls, show_type=show_type))

    lines.append("")
    return "\n".join(lines)


def write_readable(site_dir: str | Path, out_dir: str | Path | None = None) -> int:
    """Write one Markdown page per in-scope entity record of ``<site_dir>/data``.

    ``out_dir`` defaults to ``<site_dir>/data/readable``; its three
    entity subdirectories are emptied before writing. Returns the number of pages written.
    """
    site = Path(site_dir)
    config_dir = site / DATA_SUBDIR
    output_dir = Path(out_dir) if out_dir else site / READABLE_SUBDIR

    urls = load_paper_urls(config_dir / "paper_urls.json")
    logger.info("Loaded URLs for %d papers", len(urls))

    total = 0
    for subdir in ENTITY_SUBDIRS:
        src = config_dir / subdir
        if not src.exists():
            continue
        dst = output_dir / subdir
        if dst.exists():
            shutil.rmtree(dst)
        dst.mkdir(parents=True, exist_ok=True)

        for json_file in sorted(src.glob("*.json")):
            with json_file.open("r", encoding="utf-8") as f:
                node = json.load(f)
            if node.get("expert_removed"):
                continue
            md_text = render_node(node, urls)
            md_path = dst / f"{json_file.stem}.md"
            md_path.write_text(md_text, encoding="utf-8")
            total += 1

    logger.info("Generated %d readable Markdown files in %s", total, output_dir)
    return total


def main(argv: List[str] | None = None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    parser = argparse.ArgumentParser(
        description="Write the Markdown mirror of the site's per-entity records."
    )
    parser.add_argument("--site", type=Path, required=True,
                        help="site directory holding data/")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="where the .md files go (default: <site>/data/readable)")
    parser.add_argument("--log-dir", default="logs")
    args = parser.parse_args(argv)
    setup_logging(run_name="export_readable", log_dir=args.log_dir)
    write_readable(args.site, args.output_dir)


if __name__ == "__main__":
    main()
