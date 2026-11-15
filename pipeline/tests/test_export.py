"""Tests of the export stages on a small synthetic network."""
from __future__ import annotations

import json

import pytest

from aiconstructlexis.export.analysis_bundle import build_analysis_bundle
from aiconstructlexis.export.check import check_site_export, main as check_main
from aiconstructlexis.export.graph_layout import build_graph_layout
from aiconstructlexis.export.readable import render_node, write_readable
from aiconstructlexis.export.release_artifact import (
    build_name_mapping, clean_removed_reason, write_release_artifact,
)
from aiconstructlexis.export.site_data import export_site_data
from aiconstructlexis.util.names import slugify

P1 = "Paper A: Reasoning in Models"
P2 = "Paper B: Code Generation"
P3 = "Paper C: Refusals"

# The hand-maintained file of the Empirical Evidence page; the export must leave it alone.
EMPIRICAL_EVIDENCE = {"about": "Papers that empirically validate constructs.",
                      "rows": [{"title": P1, "venue": "venue_a", "constructs": ["Reasoning"]}]}


def _entity(name, papers, definition, sections=None, **extra):
    pbc = {}
    for conf, title in papers:
        pbc.setdefault(conf, []).append(title)
    rec = {
        "canonical_name": name,
        "original_names": [name] + extra.pop("aliases", []),
        "original_nodes": {name: {"definition": definition,
                                  "papers": [{"conference": c, "paper": t} for c, t in papers]}},
        "source_snippets_evidence": [],
        "papers_by_conference": pbc,
        "papers": [{"conference": c, "paper": t} for c, t in papers],
        "paper_count": len(papers),
        "paper_count_by_conference": {c: len(v) for c, v in pbc.items()},
        "characterization": "Stored summary of " + name,
    }
    if sections:
        rec["characterization_sections"] = sections
    rec.update(extra)
    return rec


def _rel(source, target, rtype, papers, quote="evidence sentence", **extra):
    pbc = {}
    for conf, title in papers:
        pbc.setdefault(conf, []).append(title)
    rec = {
        "source": source, "target": target, "type": rtype,
        "papers": [{"conference": c, "paper": t, "type_share": 1.0} for c, t in papers],
        "papers_by_conference": pbc,
        "paper_count": len(papers),
        "paper_weight": float(len(papers)),
        "n_papers_split": 0,
        "paper_count_by_conference": {c: len(v) for c, v in pbc.items()},
        "evidence": [quote],
        "evidence_by_paper": [{"conference": c, "paper": t, "quote": quote} for c, t in papers],
    }
    rec.update(extra)
    return rec


def make_network():
    return {
        "metadata": {"joint_of": ["venue_a", "venue_b"], "built_from": "merged.json",
                     "review": {"lines": 3}},
        "constructs": [
            _entity("Reasoning", [("venue_a", P1), ("venue_b", P2)], "Reasoning is the ability to infer.",
                    sections={"definition": "Papers define it as inference.", "links": "Linked to code."},
                    aliases=["Reasoning ability"],
                    rating={"rating": "consensus", "reason": "all agree"},
                    _vote_detail="x", revision_note="rewritten", extra_summaries={"a": 1}),
            _entity("Gradient Clipping", [("venue_a", P1), ("venue_b", P2)], "A training trick.",
                    expert_removed=True,
                    expert_removed_reason="a training technique, not a property of a model",
                    _review_tag="x"),
        ],
        "measurements": [
            _entity("HumanEval+", [("venue_b", P2), ("venue_a", P1)], "Extended HumanEval.", _credit_note={"n": 1}),
            _entity("HumanEval", [("venue_b", P2)], "Code benchmark.",
                    expert_removed=True, expert_removed_reason="metric"),
        ],
        "behaviors": [
            _entity("Refusal", [("venue_a", P3), ("venue_b", P2)], "Declining to answer.", _restored="x"),
        ],
        "relationships": [
            _rel("Reasoning", "HumanEval+", "measured_by", [("venue_a", P1), ("venue_b", P2)], quote="measured with HumanEval+"),
            _rel("Refusal", "Reasoning", "causes", [("venue_b", P2)]),
            _rel("Reasoning", "Refusal", "related", [("venue_a", P1), ("venue_a", P3)], _vote_note="x"),
            _rel("Gradient Clipping", "HumanEval", "measured_by", [("venue_a", P1)]),
            _rel("Gradient Clipping", "HumanEval+", "related", [("venue_a", P1)]),
        ],
        "papers": [{"conference": "venue_a", "paper": P1}, {"conference": "venue_b", "paper": P2},
                   {"conference": "venue_a", "paper": P3}],
        "paper_count_by_conference": {"venue_a": 2, "venue_b": 1},
        "name_mapping": {"Reasoning ability": "Reasoning"},
    }


@pytest.fixture
def site(tmp_path):
    """A site directory exported from the synthetic network; returns (site_dir, network_path)."""
    net_path = tmp_path / "network.json"
    net_path.write_text(json.dumps(make_network()))
    list_a = tmp_path / "list_a.json"
    list_b = tmp_path / "list_b.json"
    list_a.write_text(json.dumps([{"title": P1, "url": "https://a.example/p1", "is_LLM_paper": True},
                                  {"title": P2, "url": "https://a.example/p2", "is_LLM_paper": True}]))
    list_b.write_text(json.dumps([{"name": P1, "url": "https://b.example/p1"},
                                  {"title": P3, "url": "https://b.example/p3"},
                                  {"title": "No URL paper", "url": ""}]))
    site_dir = tmp_path / "site"
    (site_dir / "data/readable" / "constructs").mkdir(parents=True)
    (site_dir / "data/readable" / "constructs" / "stale.md").write_text("old")
    (site_dir / "data" / "empirical_evidence.json").write_text(json.dumps(EMPIRICAL_EVIDENCE))
    counts = export_site_data(net_path, site_dir, [list_a, list_b])
    assert counts["constructs"] == 1 and counts["measurements"] == 1 and counts["behaviors"] == 1
    return site_dir, net_path


@pytest.fixture
def full_site(site):
    """The site fixture with the readable mirror, the analysis bundle and the graph layout added."""
    site_dir, net_path = site
    write_readable(site_dir)
    build_analysis_bundle(net_path, site_dir)
    build_graph_layout(site_dir, seed=3, iterations=20)
    return site_dir, net_path


def _load(site_dir, sub, name):
    return json.loads((site_dir / "data" / sub / f"{slugify(name)}.json").read_text())


def test_site_data_files_are_the_in_scope_entities(site):
    site_dir, _ = site
    data = site_dir / "data"
    assert slugify("HumanEval+") == "humaneval_plus"
    assert sorted(p.name for p in data.iterdir()) == ["behaviors_tasks", "constructs", "empirical_evidence.json",
                                                      "graph.bundle.json", "measurements", "paper_urls.json", "readable"]
    assert json.loads((data / "empirical_evidence.json").read_text()) == EMPIRICAL_EVIDENCE
    assert [p.name for p in (data / "constructs").iterdir()] == ["reasoning.json"]
    assert [p.name for p in (data / "measurements").iterdir()] == ["humaneval_plus.json"]
    assert [p.name for p in (data / "behaviors_tasks").iterdir()] == ["refusal.json"]


def test_site_data_record_fields(site):
    site_dir, _ = site
    rec = _load(site_dir, "constructs", "Reasoning")
    assert list(rec.keys()) == [
        "canonical_name", "type", "canonical_definition", "expert_removed",
        "expert_removed_reason", "names", "papers", "paper_count", "definitions",
        "definition_count", "relationships", "relationship_count", "incoming_relationship_count",
        "outgoing_relationship_count", "characterization_sections", "characterization",
        "characterization_status", "papers_by_conference", "paper_count_by_conference", "conferences",
    ]
    assert rec["type"] == "construct"
    assert rec["names"] == ["Reasoning", "Reasoning ability"]
    assert rec["papers"] == [P1, P2] and rec["paper_count"] == 2
    # the labeled summary is recomposed from its sections in display order
    assert rec["canonical_definition"] == ("Space of definitions. Papers define it as inference.\n\n"
                                           "Links. Linked to code.")
    assert rec["characterization_status"] == "llm"
    assert [s["label"] for s in rec["characterization_sections"]] == ["Space of definitions.", "Links."]
    # a surface name's definition is attributed to every paper that used the name, in the stored order
    assert rec["definitions"] == [{"text": "Reasoning is the ability to infer.", "papers": [P1, P2],
                                  "original_name": "Reasoning"}]
    assert rec["definition_count"] == 1
    kept = _load(site_dir, "measurements", "HumanEval+")
    assert kept["definitions"] == [{"text": "Extended HumanEval.", "papers": [P2, P1], "original_name": "HumanEval+"}]
    assert kept["expert_removed"] is False and kept["expert_removed_reason"] == ""
    # the relationship with the removed Gradient Clipping is left out of the in-scope endpoint's record
    assert [r["other_canonical_name"] for r in kept["relationships"]] == ["Reasoning"]
    assert kept["relationship_count"] == 1 and kept["incoming_relationship_count"] == 1
    assert kept["outgoing_relationship_count"] == 0


def test_site_data_definitions_follow_their_surface_names(tmp_path):
    """One definition per surface name: attributed to its recorded source paper when the node
    carries ``definition_paper``, otherwise to every paper that used the name; a name without a
    definition gets no entry."""
    net = make_network()
    ent = _entity("Honesty", [("venue_a", P1), ("venue_b", P2), ("venue_a", P3)], "Telling the truth.",
                  aliases=["Truthfulness", "Candor"])
    ent["original_nodes"] = {
        "Honesty": {"definition": "Telling the truth.", "papers": [["venue_a", P1], ["venue_b", P2]]},
        "Truthfulness": {"definition": "Not asserting falsehoods.", "definition_paper": P3,
                         "papers": [["venue_a", P3], ["venue_a", P1]]},
        "Candor": {"definition": "", "papers": [["venue_b", P2]]},
    }
    net["constructs"].append(ent)
    net_path = tmp_path / "network.json"
    net_path.write_text(json.dumps(net))
    site_dir = tmp_path / "site"
    export_site_data(net_path, site_dir, [])
    rec = _load(site_dir, "constructs", "Honesty")
    assert rec["definitions"] == [
        {"text": "Telling the truth.", "papers": [P1, P2], "original_name": "Honesty"},
        {"text": "Not asserting falsehoods.", "papers": [P3], "original_name": "Truthfulness"},
    ]
    assert rec["definition_count"] == 2
    (site_dir / "data" / "paper_urls.json").write_text(json.dumps({P1: "https://a.example/p1"}))
    write_readable(site_dir)
    md = (site_dir / "data/readable" / "constructs" / "honesty.md").read_text(encoding="utf-8")
    assert ("## Sources\n\n"
            f"**Honesty** (2 papers: [{P1}](https://a.example/p1), {P2})\n> Telling the truth.\n\n"
            f"**Truthfulness** (1 paper: {P3})\n> Not asserting falsehoods.\n") in md
    assert "Candor" in md.split("## Sources")[0] and "Candor" not in md.split("## Sources")[1]


def test_site_data_relationship_directions(site):
    site_dir, _ = site
    reasoning = _load(site_dir, "constructs", "Reasoning")
    rels = {(r["direction"], r["other_canonical_name"], r["relationship_type"]): r for r in reasoning["relationships"]}
    assert set(rels) == {("outgoing", "HumanEval+", "measured_by"), ("incoming", "Refusal", "causes"),
                         ("outgoing", "Refusal", "related")}
    assert reasoning["outgoing_relationship_count"] == 2 and reasoning["incoming_relationship_count"] == 1
    mb = rels[("outgoing", "HumanEval+", "measured_by")]
    assert mb["other_type"] == "measurements"
    assert mb["paper"] == P1 and mb["evidence"] == "measured with HumanEval+"
    assert mb["paper_count"] == 2 and mb["paper_weight"] == 2.0
    assert rels[("incoming", "Refusal", "causes")]["other_type"] == "behaviors_tasks"
    humaneval_plus = _load(site_dir, "measurements", "HumanEval+")
    assert [(r["direction"], r["other_canonical_name"], r["other_type"]) for r in humaneval_plus["relationships"]] == [
        ("incoming", "Reasoning", "constructs")]


def test_site_data_paper_urls_first_wins(site):
    site_dir, _ = site
    urls = json.loads((site_dir / "data" / "paper_urls.json").read_text())
    assert urls == {P1: "https://a.example/p1", P2: "https://a.example/p2", P3: "https://b.example/p3"}


def test_site_data_graph_bundle(site):
    site_dir, _ = site
    graph = json.loads((site_dir / "data" / "graph.bundle.json").read_text())
    assert graph["schema_version"] == 1
    assert [n["name"] for n in graph["nodes"]] == ["Reasoning", "HumanEval+", "Refusal"]
    assert all(set(n.keys()) == {"name", "type", "paper_count", "names", "definition"} for n in graph["nodes"])
    assert graph["node_count"] == 3 and graph["edge_count"] == 3
    edges = {(e["source"], e["target"], e["type"]) for e in graph["edges"]}
    assert edges == {("Reasoning", "HumanEval+", "measured_by"), ("Refusal", "Reasoning", "causes"),
                     ("Reasoning", "Refusal", "related")}
    # the edges of the removed Gradient Clipping, to HumanEval (removed) and HumanEval+ (in scope), are absent
    assert not any("Gradient Clipping" in (e["source"], e["target"]) for e in graph["edges"])


def test_write_readable(site):
    site_dir, _ = site
    n = write_readable(site_dir)
    assert n == 3
    readable = site_dir / "data/readable"
    assert not (readable / "constructs" / "stale.md").exists()
    assert [p.name for p in (readable / "constructs").iterdir()] == ["reasoning.md"]
    assert [p.name for p in (readable / "measurements").iterdir()] == ["humaneval_plus.md"]
    md = (readable / "constructs" / "reasoning.md").read_text(encoding="utf-8")
    # the header counts the entity's supporting papers (paper_count), not those of its relationships
    assert md.startswith("# Reasoning\n**Type:** Construct  \n**Supporting papers:** 2  \n"
                         "**Also known as:** Reasoning ability  \n")
    assert "## State of the Field\n\n**Space of definitions.** Papers define it as inference." in md
    assert (f"## Sources\n\n**Reasoning** (2 papers: [{P1}](https://a.example/p1), [{P2}](https://a.example/p2))\n"
            "> Reasoning is the ability to infer.\n") in md
    # the site record carries one quote per relationship: it is shown once, above every paper of the relationship
    assert ("### Reasoning \u2192\n- **HumanEval+** (measurement instrument): *measured_by*, 2 papers\n"
            "  > measured with HumanEval+\n"
            f"  - [{P1}](https://a.example/p1)\n"
            f"  - [{P2}](https://a.example/p2)\n") in md
    assert (f"### \u2192 Reasoning\n- **Refusal** (behavioral indicator): *causes*, 1 paper\n"
            f"  > evidence sentence\n  - [{P2}](https://a.example/p2)\n") in md
    # a related relationship is listed under "Associated with", without its type
    assert (f"### Associated with\n- **Refusal** (behavioral indicator), 2 papers\n"
            f"  > evidence sentence\n  - [{P1}](https://a.example/p1)\n  - [{P3}](https://b.example/p3)\n") in md
    refusal = (readable / "behaviors_tasks" / "refusal.md").read_text(encoding="utf-8")
    assert refusal.startswith("# Refusal\n**Type:** Behavioral indicator  \n")
    # the page names only partners that have a page: the removed Gradient Clipping is not on HumanEval+'s
    humaneval_plus = (readable / "measurements" / "humaneval_plus.md").read_text(encoding="utf-8")
    assert humaneval_plus.startswith("# HumanEval+\n**Type:** Measurement instrument  \n")
    assert "### \u2192 HumanEval+\n- **Reasoning** (construct): *measured_by*" in humaneval_plus
    assert "Gradient Clipping" not in humaneval_plus
    other = site_dir / "elsewhere"
    assert write_readable(site_dir, other) == 3
    assert (other / "measurements" / "humaneval_plus.md").read_text(encoding="utf-8") == \
        (readable / "measurements" / "humaneval_plus.md").read_text(encoding="utf-8")


def test_render_node_relationship_papers_and_quotes():
    """Per-paper quotes when the record has them; the two directions of a related pair merged;
    the header falls back to the length of ``papers`` without ``paper_count``."""
    node = {
        "canonical_name": "Reasoning", "type": "construct", "papers": [P1, P2, P3],
        "relationships": [
            {"direction": "outgoing", "other_canonical_name": "GSM8K", "other_type": "measurements",
             "relationship_type": "measured_by", "paper": P1, "evidence": "quote one",
             "papers_by_conference": {"venue_a": [P1, P3], "venue_b": [P2]},
             "evidence_by_paper": [{"conference": "venue_a", "paper": P1, "quote": "quote one"},
                                   {"conference": "venue_b", "paper": P2, "quote": "quote two"},
                                   {"conference": "venue_a", "paper": P3, "quote": ""}]},
            {"direction": "outgoing", "other_canonical_name": "Refusal", "other_type": "behaviors_tasks",
             "relationship_type": "related", "paper": P1, "evidence": "first direction",
             "papers_by_conference": {"venue_a": [P1]}},
            {"direction": "incoming", "other_canonical_name": "Refusal", "other_type": "behaviors_tasks",
             "relationship_type": "related", "paper": P2, "evidence": "second direction",
             "papers_by_conference": {"venue_a": [P1], "venue_b": [P2]}},
            {"direction": "incoming", "other_canonical_name": "Planning", "other_type": "constructs",
             "relationship_type": "causes", "paper": "", "evidence": "", "papers_by_conference": {}},
        ],
    }
    md = render_node(node, {P1: "https://a.example/p1"})
    assert md.startswith("# Reasoning\n**Type:** Construct  \n**Supporting papers:** 3  \n")
    assert ("### Reasoning →\n- **GSM8K** (measurement instrument): *measured_by*, 3 papers\n"
            f"  - [{P1}](https://a.example/p1)\n    > quote one\n"
            f"  - {P3}\n"
            f"  - {P2}\n    > quote two\n") in md
    assert ("### → Reasoning\n- **Planning** (construct): *causes*\n\n") in md
    assert ("### Associated with\n- **Refusal** (behavioral indicator), 2 papers\n"
            "  > first direction\n  >\n  > second direction\n"
            f"  - [{P1}](https://a.example/p1)\n  - {P2}\n") in md
    assert md.count("**Refusal**") == 1


def test_removed_entity_has_no_record_and_no_page(site):
    site_dir, _ = site
    data = site_dir / "data"
    assert (data / "constructs" / "reasoning.json").exists()
    assert not (data / "constructs" / "gradient_clipping.json").exists()
    assert not (data / "measurements" / "humaneval.json").exists()
    # a record flagged expert_removed that is nevertheless present in data/ gets no page either
    removed = json.loads((data / "constructs" / "reasoning.json").read_text())
    removed.update(canonical_name="Gradient Clipping", expert_removed=True, expert_removed_reason="Method")
    (data / "constructs" / "gradient_clipping.json").write_text(json.dumps(removed))
    assert write_readable(site_dir) == 3
    readable = data / "readable"
    assert (readable / "constructs" / "reasoning.md").exists()
    assert not (readable / "constructs" / "gradient_clipping.md").exists()
    assert not (readable / "measurements" / "humaneval.md").exists()


def test_clean_removed_reason():
    assert clean_removed_reason("metric") == ("Metric", "rewritten")
    assert clean_removed_reason("Metric") == ("Metric", "kept")
    assert clean_removed_reason("  a technique, treated as method ") == ("A technique, treated as method", "rewritten")
    assert clean_removed_reason("") == ("", "kept")


def test_build_name_mapping_follows_the_entities():
    net = {
        "constructs": [
            {"canonical_name": "Episodic memory", "original_names": ["Episodic memory", "episodic recall"]},
            {"canonical_name": "Temporal grounding",
             "original_names": ["Temporal grounding", "Episodic memory", "time grounding", "memory"]},
            {"canonical_name": "Spatial understanding", "original_names": ["Visual grounding"]},
            {"canonical_name": "Removed thing", "original_names": ["memory", "removed alias"],
             "expert_removed": True},
            {"canonical_name": "  ", "original_names": ["orphan"]},
        ],
        "measurements": [{"canonical_name": "MMLU", "original_names": ["MMLU", "mmlu", "", "  "]}],
        "behaviors": [{"canonical_name": "Recall", "original_names": ["episodic recall"]}],
        # the network's own mapping is stale and plays no part
        "name_mapping": {"Spatial understanding": "Visual grounding", "Gone": "Gone"},
    }
    nm = build_name_mapping(net)
    assert nm == {
        "Episodic memory": "Episodic memory",          # a canonical name maps to itself even when listed elsewhere
        "MMLU": "MMLU",
        "Recall": "Recall",
        "Removed thing": "Removed thing",              # expert_removed entities are included
        "Spatial understanding": "Spatial understanding",
        "Temporal grounding": "Temporal grounding",
        "Visual grounding": "Spatial understanding",
        "episodic recall": ["Episodic memory", "Recall"],   # listed by two entities: the sorted canonical names
        "memory": ["Removed thing", "Temporal grounding"],
        "mmlu": "MMLU",
        "removed alias": "Removed thing",
        "time grounding": "Temporal grounding",
    }
    assert list(nm) == sorted(nm)
    # re-applied to its own output's entities, the mapping is unchanged
    assert build_name_mapping(dict(net, name_mapping=nm)) == nm
    assert build_name_mapping({}) == {}


def test_write_release_artifact(tmp_path):
    net_path = tmp_path / "network.json"
    net = make_network()
    net["behaviors"][0]["canonical_definition"] = ""
    net_path.write_text(json.dumps(net))
    out_path = tmp_path / "lexis" / "artifact.json"
    report = write_release_artifact(net_path, out_path, "0.0.1", ["venue_a", "venue_b"],
                                    drop_fields=("revision_note", "extra_summaries", "rating"))
    out = json.loads(out_path.read_text(encoding="utf-8"))
    assert list(out.keys()) == list(make_network().keys())
    assert out["metadata"] == {
        "name": "AI Construct Lexis",
        "version": "0.0.1",
        "venues": ["venue_a", "venue_b"],
        "paper_count_by_conference": {"venue_a": 2, "venue_b": 1},
        "counts": {"constructs": 1, "measurements": 1, "behaviors": 1, "relationships": 5,
                   "relationships_between_in_scope_entities": 3, "papers": 3},
        "notes": ("Entities flagged expert_removed were extracted by the pipeline and judged out of scope by "
                  "expert review; they are kept for transparency and are not shown in the interface."),
    }
    assert report["metadata"] == out["metadata"]
    for et in ("constructs", "measurements", "behaviors"):
        for g in out[et]:
            for key in ("_vote_detail", "_review_tag", "_restored", "_credit_note",
                        "revision_note", "extra_summaries", "rating"):
                assert key not in g, (g["canonical_name"], key)
    assert all("_vote_note" not in r for r in out["relationships"])
    assert "canonical_definition" not in out["behaviors"][0]
    assert report["entity_fields_removed"] == 8 and report["relationship_fields_removed"] == 1
    reasoning = out["constructs"][0]
    assert reasoning["characterization_sections"] == {"definition": "Papers define it as inference.",
                                                     "links": "Linked to code."}
    assert reasoning["original_names"] == ["Reasoning", "Reasoning ability"]
    assert out["constructs"][1]["expert_removed_reason"] == "A training technique, not a property of a model"
    assert out["measurements"][1]["expert_removed_reason"] == "Metric"
    assert report["reasons_rewritten"] == 2 and report["reasons_kept"] == 0
    # name_mapping is rebuilt from the entities, the expert_removed ones included
    assert out["name_mapping"] == {"Gradient Clipping": "Gradient Clipping", "HumanEval": "HumanEval",
                                   "HumanEval+": "HumanEval+", "Reasoning": "Reasoning",
                                   "Reasoning ability": "Reasoning", "Refusal": "Refusal"}
    assert report["name_mapping_keys"] == 6 and report["name_mapping_ambiguous"] == 0
    assert out["relationships"][0]["evidence_by_paper"] == make_network()["relationships"][0]["evidence_by_paper"]
    # the written file keeps non-ASCII characters and is indented by one space
    text = out_path.read_text(encoding="utf-8")
    assert text.startswith('{\n "metadata": {\n  "name": "AI Construct Lexis",')
    # a cleaned artifact exports exactly like the raw network
    site_dir = tmp_path / "site"
    export_site_data(out_path, site_dir, [])
    (site_dir / "data" / "empirical_evidence.json").write_text(json.dumps(EMPIRICAL_EVIDENCE))
    write_readable(site_dir)
    build_analysis_bundle(out_path, site_dir)
    build_graph_layout(site_dir, seed=3, iterations=20)
    assert check_site_export(site_dir, out_path) == []


def test_check_site_export(full_site, capsys):
    site_dir, net_path = full_site
    data = site_dir / "data"
    assert check_site_export(site_dir, net_path) == []
    assert check_main([str(site_dir), str(net_path), "--log-dir", str(site_dir / "logs")]) == 0
    # a record whose relationships differ from the network's
    rec_path = data / "constructs" / "reasoning.json"
    rec = json.loads(rec_path.read_text())
    rec["relationships"][0]["paper_count"] = 99
    rec_path.write_text(json.dumps(rec))
    problems = check_site_export(site_dir, net_path)
    assert problems == ["relationships differ for Reasoning: 1 extra, 1 missing"]
    # a file of a removed entity, a file of no entity, a missing file and a renamed record
    export_site_data(net_path, site_dir, [])
    (data / "constructs" / "gradient_clipping.json").write_text(json.dumps(rec))
    (data / "behaviors_tasks" / "nobody.json").write_text("{}")
    (data / "measurements" / "humaneval_plus.json").unlink()
    rec["canonical_name"] = "Reasoning ability"
    rec_path.write_text(json.dumps(rec))
    problems = check_site_export(site_dir, net_path)
    assert problems == ["constructs/gradient_clipping.json has no in-scope entity in the network",
                        "constructs/reasoning.json names 'Reasoning ability', network has 'Reasoning'",
                        "measurements/humaneval_plus.json missing for 'HumanEval+'",
                        "behaviors_tasks/nobody.json has no in-scope entity in the network"]
    # the network gains an entity and a relationship the export does not have
    export_site_data(net_path, site_dir, [])
    net = make_network()
    net["relationships"].append(_rel("Refusal", "HumanEval+", "measured_by", [("venue_a", P3)]))
    net["behaviors"].append(_entity("Extra", [("venue_a", P3), ("venue_b", P2)], "x"))
    problems = check_site_export(site_dir, net)
    assert problems == ["behaviors_tasks/extra.json missing for 'Extra'",
                        "relationships differ for HumanEval+: 0 extra, 1 missing",
                        "relationships differ for Refusal: 0 extra, 1 missing",
                        "graph.bundle.json: 1 node(s) missing: Extra",
                        "readable/behaviors_tasks/extra.md missing for 'Extra'"]
    # a relationship between an in-scope and a removed entity is not expected on any record
    net = make_network()
    net["relationships"].append(_rel("Refusal", "HumanEval", "measured_by", [("venue_a", P3)]))
    assert check_site_export(site_dir, net) == []
    # the graph bundle carries a removed entity and an edge to it; required files are gone
    graph_path = data / "graph.bundle.json"
    graph = json.loads(graph_path.read_text())
    graph["nodes"].append({"name": "Gradient Clipping", "type": "construct", "paper_count": 2, "names": [], "definition": ""})
    graph["edges"].append({"source": "Gradient Clipping", "target": "HumanEval", "type": "measured_by", "paper_count": 1})
    graph_path.write_text(json.dumps(graph))
    (data / "layout.json").unlink()
    (data / "empirical_evidence.json").unlink()
    problems = check_site_export(site_dir, net_path)
    assert problems == ["graph.bundle.json: 1 node(s) not in scope: Gradient Clipping",
                        "graph.bundle.json: 1 edge(s) touch a node that is not in the bundle",
                        "empirical_evidence.json missing",
                        "layout.json missing"]
    graph_path.unlink()
    assert "graph.bundle.json missing" in check_site_export(site_dir, net_path)
    assert check_main([str(site_dir), str(net_path), "--log-dir", str(site_dir / "logs")]) == 1
    assert "FAILED" in capsys.readouterr().out


def test_check_site_export_flags(full_site):
    site_dir, net_path = full_site
    data = site_dir / "data"
    assert check_site_export(site_dir, net_path) == []
    # a site built without the analysis bundle passes only when the check knows that
    (data / "analysis.bundle.json").unlink()
    assert check_site_export(site_dir, net_path) == ["analysis.bundle.json missing"]
    assert check_site_export(site_dir, net_path, analysis_bundle=False) == []
    (data / "analysis_evidence.json").unlink()
    assert check_site_export(site_dir, net_path) == ["analysis.bundle.json missing", "analysis_evidence.json missing"]
    assert check_site_export(site_dir, net_path, analysis_bundle=False) == []
    # the same for the layout
    (data / "layout.json").unlink()
    assert check_site_export(site_dir, net_path, analysis_bundle=False) == ["layout.json missing"]
    assert check_site_export(site_dir, net_path, analysis_bundle=False, graph_layout=False) == []
    # a stale readable page, a stray folder and a missing page fail the readable check
    (data / "readable" / "constructs" / "stale.md").write_text("old")
    (data / "readable" / "measurements" / "drafts").mkdir()
    (data / "readable" / "behaviors_tasks" / "refusal.md").unlink()
    assert check_site_export(site_dir, net_path, analysis_bundle=False, graph_layout=False) == [
        "readable/constructs/stale.md is not the page of an in-scope entity",
        "readable/measurements/drafts is not the page of an in-scope entity",
        "readable/behaviors_tasks/refusal.md missing for 'Refusal'"]
    assert check_site_export(site_dir, net_path, analysis_bundle=False, graph_layout=False, readable=False) == []
    # the hand-maintained file is required whatever the flags
    (data / "empirical_evidence.json").unlink()
    assert check_site_export(site_dir, net_path, analysis_bundle=False, graph_layout=False, readable=False) == [
        "empirical_evidence.json missing"]


def test_export_backup_moves_only_what_the_export_writes(full_site):
    site_dir, net_path = full_site
    data = site_dir / "data"
    before = {p.name: p.read_bytes() for p in data.iterdir() if p.is_file()}
    pages_before = sorted(p.name for p in (data / "readable" / "constructs").iterdir())
    export_site_data(net_path, site_dir, [], backup=True)
    backups = sorted(site_dir.glob("data.backup-*"))
    assert len(backups) == 1
    assert sorted(p.name for p in backups[0].iterdir()) == ["behaviors_tasks", "constructs", "graph.bundle.json",
                                                             "measurements", "paper_urls.json"]
    assert sorted(p.name for p in (backups[0] / "constructs").iterdir()) == ["reasoning.json"]
    assert (backups[0] / "graph.bundle.json").read_bytes() == before["graph.bundle.json"]
    # the files the export does not write stayed in place, byte for byte
    for name in ("empirical_evidence.json", "analysis.bundle.json", "analysis_evidence.json", "layout.json"):
        assert (data / name).read_bytes() == before[name], name
    assert json.loads((data / "empirical_evidence.json").read_text()) == EMPIRICAL_EVIDENCE
    assert sorted(p.name for p in (data / "readable" / "constructs").iterdir()) == pages_before
    # the export was written again
    assert sorted(p.name for p in (data / "constructs").iterdir()) == ["reasoning.json"]
    assert (data / "graph.bundle.json").read_bytes() == before["graph.bundle.json"]
    assert check_site_export(site_dir, net_path) == []
    # with nothing to move aside, no backup directory appears
    fresh = site_dir.parent / "fresh"
    export_site_data(net_path, fresh, [], backup=True)
    assert list(fresh.glob("data.backup-*")) == []


def test_build_analysis_bundle(site):
    site_dir, net_path = site
    counts = build_analysis_bundle(net_path, site_dir)
    assert counts == {"nodes": 3, "edges": 3, "papers": 3}
    data = site_dir / "data"
    bundle = json.loads((data / "analysis.bundle.json").read_text())
    assert set(bundle.keys()) == {"meta", "nodes", "edges", "papers"}
    assert bundle["meta"]["joint_of"] == ["venue_a", "venue_b"]
    assert bundle["meta"]["n_nodes"] == 3 and bundle["meta"]["n_edges"] == 3 and bundle["meta"]["n_papers"] == 3
    # nodes are sorted by type then name; the removed entities are absent
    assert [n[:3] for n in bundle["nodes"]] == [["Refusal", "b", 2], ["Reasoning", "c", 2], ["HumanEval+", "m", 2]]
    idx = {n[0]: i for i, n in enumerate(bundle["nodes"])}
    edge = next(e for e in bundle["edges"] if e[2] == "measured_by")
    assert edge[0] == idx["Reasoning"] and edge[1] == idx["HumanEval+"]
    assert edge[3] == 2 and edge[4] == 2.0 and edge[6] == [1.0, 1.0]
    assert [bundle["papers"][i] for i in edge[5]] == [[P1, "venue_a"], [P2, "venue_b"]]
    evidence = json.loads((data / "analysis_evidence.json").read_text())
    assert len(evidence["evidence"]) == 3
    assert evidence["evidence"][0] == [[edge[5][0], "measured with HumanEval+"], [edge[5][1], "measured with HumanEval+"]]


def test_build_graph_layout(site):
    site_dir, _ = site
    layout = build_graph_layout(site_dir, seed=3, iterations=20)
    out = json.loads((site_dir / "data" / "layout.json").read_text(encoding="utf-8"))
    assert out == layout
    assert out["schema"] == "lexis-graph-layout/1"
    assert out["source"]["path"] == "data/graph.bundle.json"
    assert out["source"]["node_count"] == 3 and out["source"]["edge_count"] == 3
    assert out["params"]["seed"] == 3 and out["params"]["iterations"] == 20
    assert set(out["nodes"]) == {"Reasoning", "HumanEval+", "Refusal"}
    assert all(len(v) == 3 for v in out["nodes"].values())
    assert out["isolated_count"] == 0 and out["levels"] == {}
    # the layout is deterministic for a given seed
    again = build_graph_layout(site_dir, seed=3, iterations=20, output_json=site_dir / "again.json")
    assert again["nodes"] == out["nodes"] and again["communities"] == out["communities"]
