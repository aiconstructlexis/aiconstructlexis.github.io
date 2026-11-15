"""Tests of aiconstructlexis.harmonize.relationships: canonical resolution, symmetric
bucketing, self-loop removal and the in-place / --out writing of the entry function."""
import json

from aiconstructlexis.harmonize import relationships
from aiconstructlexis.harmonize.relationships import aggregate, aggregate_relationships, build_canonical_lookup, resolve

NETWORK = {
    "constructs": [{"canonical_name": "Reasoning", "original_names": ["Reasoning ability", "reasoning skills"]},
                   {"canonical_name": "Memory", "original_names": []}],
    "measurements": [{"canonical_name": "GSM8K", "original_names": ["GSM-8K"]}],
    "behaviors": [],
    "name_mapping": {"Reasoning ability": "Reasoning", "Reasoning": "Reasoning", "GSM-8K": "GSM8K", "GSM8K": "GSM8K"},
    "relationships": [],
}


def _paper(*rels):
    return {"parsed_text": {"Nomological Network": {"relationships": list(rels)}}}


def test_resolve_exact_then_normalized_then_as_is():
    lookup = build_canonical_lookup(NETWORK)
    assert resolve("Reasoning ability", lookup) == "Reasoning"
    assert resolve("reasoning skills", lookup) == "Reasoning"
    assert resolve("Reasoning-Ability", lookup) == "Reasoning"  # normalized fallback
    assert resolve("gsm_8k", lookup) == "GSM8K"
    assert resolve("Unknown thing", lookup) == "Unknown thing"


def test_symmetric_types_share_a_bucket_and_directed_types_do_not():
    simplified = {
        "p1": _paper({"source": "Reasoning", "target": "Memory", "type": "related", "evidence": "a"},
                     {"source": "Reasoning", "target": "Memory", "type": "causes", "evidence": "c1"}),
        "p2": _paper({"source": "Memory", "target": "Reasoning ability", "type": "related", "evidence": ["b", "a"]},
                     {"source": "Memory", "target": "Reasoning", "type": "causes", "evidence": "c2"}),
    }
    rels, stats = aggregate(simplified, NETWORK)
    by_key = {(r["source"], r["target"], r["type"]): r for r in rels}
    assert set(by_key) == {("Memory", "Reasoning", "related"), ("Reasoning", "Memory", "causes"),
                           ("Memory", "Reasoning", "causes")}
    related = by_key[("Memory", "Reasoning", "related")]
    assert related["papers"] == ["p1", "p2"] and related["paper_count"] == 2
    assert related["evidence"] == ["a", "b"]
    assert stats == {"n_raw": 4, "n_resolved": 4, "n_aggregated": 3, "n_unresolved_src": 0,
                     "n_unresolved_tgt": 0, "n_self_loops_dropped": 0}
    assert rels[0] is related  # sorted by descending paper count


def test_self_loops_dropped_and_unresolved_counted():
    simplified = {
        "p1": _paper({"source": "Reasoning ability", "target": "Reasoning", "type": "related"},
                     {"source": "Novel construct", "target": "GSM8K", "type": "measured_by"},
                     {"source": "", "target": "GSM8K", "type": "measured_by"}),
    }
    rels, stats = aggregate(simplified, NETWORK)
    assert [(r["source"], r["target"], r["type"]) for r in rels] == [("Novel construct", "GSM8K", "measured_by")]
    assert stats["n_self_loops_dropped"] == 1 and stats["n_unresolved_src"] == 1 and stats["n_raw"] == 3


def test_aggregate_relationships_writes_in_place_or_to_out(tmp_path):
    net_path = tmp_path / "net.json"
    net_path.write_text(json.dumps(NETWORK))
    simp_path = tmp_path / "simplified.json"
    simp_path.write_text(json.dumps({"p1": _paper({"source": "Reasoning", "target": "GSM-8K", "type": "measured_by"})}))
    expected = [{"source": "Reasoning", "target": "GSM8K", "type": "measured_by", "evidence": [],
                 "papers": ["p1"], "paper_count": 1}]

    out = aggregate_relationships(simp_path, net_path, out_json=tmp_path / "out.json")
    assert out == tmp_path / "out.json"
    assert json.loads(net_path.read_text()) == NETWORK
    written = json.loads(out.read_text())
    assert written["relationships"] == expected
    assert list(written) == list(NETWORK)

    assert aggregate_relationships(simp_path, net_path) == net_path
    assert json.loads(net_path.read_text())["relationships"] == expected


def test_cli(tmp_path):
    net_path = tmp_path / "net.json"
    net_path.write_text(json.dumps(NETWORK))
    simp_path = tmp_path / "simplified.json"
    simp_path.write_text(json.dumps({"p1": _paper({"source": "Reasoning", "target": "GSM8K", "type": "measured_by"})}))
    assert relationships.main(["--simplified", str(simp_path), "--harmonized", str(net_path),
                               "--log-dir", str(tmp_path / "logs")]) == 0
    assert json.loads(net_path.read_text())["relationships"][0]["paper_count"] == 1
