"""Tests for the orphan-node invariant: nodes with no papers are dropped, nothing else changes."""
import json

from aiconstructlexis.curate.cleanup import drop_orphan_definitions, drop_orphans


def network():
    return {"constructs": [{"canonical_name": "Alpha",
                            "original_nodes": {"Alpha": {"definition": "kept", "papers": [["iclr24", "P1"]]},
                                               "alpha variant": {"definition": "orphan", "papers": []},
                                               "bare": {"definition": "", "papers": []}},
                            "papers": [{"conference": "iclr24", "paper": "P1"}], "paper_count": 1}],
            "measurements": [{"canonical_name": "Bench", "original_nodes": {"Bench": {"definition": "only", "papers": []}},
                              "papers": [], "paper_count": 0}],
            "behaviors": [], "relationships": [{"source": "Alpha", "type": "measured_by", "target": "Bench"}]}


def test_drop_orphans_removes_only_nodes_without_papers():
    net = network()
    report = drop_orphans(net)
    assert list(net["constructs"][0]["original_nodes"]) == ["Alpha"]
    assert net["measurements"][0]["original_nodes"] == {}
    assert report["stats"] == {"definitions dropped": 2, "nodes dropped": 3, "entities touched": 2,
                               "entities left with no definition": 1}
    assert report["examples"][0] == "Alpha <- alpha variant"
    assert net["constructs"][0]["papers"] == [{"conference": "iclr24", "paper": "P1"}]
    assert net["relationships"] == network()["relationships"]


def test_drop_orphans_is_idempotent():
    net = network()
    drop_orphans(net)
    again = drop_orphans(net)
    assert again == {"stats": {}, "examples": []}


def test_drop_orphan_definitions_writes_the_output_file(tmp_path):
    src = tmp_path / "in.json"
    src.write_text(json.dumps(network()))
    report = drop_orphan_definitions(src, src)
    out = json.loads(src.read_text())
    assert report["stats"]["nodes dropped"] == 3
    assert list(out["constructs"][0]["original_nodes"]) == ["Alpha"]
