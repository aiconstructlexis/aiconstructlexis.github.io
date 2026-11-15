"""Synthetic tests for the curation overlay: each case builds a tiny network and checks one
rule of the stage (entity operations, paper credits, relationship operations, type guard)."""
import copy
import json

import pytest

from aiconstructlexis.curate import overlay as O
from aiconstructlexis.curate.overlay import (OverlayError, apply_entity_operations, apply_overlay,
                                             apply_relationship_operations, read_overlay)


# ---------------------------------------------------------------- helpers

def ent(name, names, papers=None, snippets=()):
    """An entity whose node for each surface name n lists the paper P-n; by default it is
    credited with exactly those papers."""
    if papers is None:
        papers = [f"P-{n}" for n in names]
    return {"canonical_name": name, "original_names": list(names),
            "original_nodes": {n: {"definition": f"def of {n}", "papers": [["iclr24", f"P-{n}"]]} for n in names},
            "source_snippets_evidence": [{"original_name": n, "paper": f"P-{n}", "snippet": "s"} for n in snippets],
            "papers": [{"conference": "iclr24", "paper": p} for p in papers],
            "paper_count": len(papers), "characterization": f"summary of {name}"}


def net(constructs=(), measurements=(), behaviors=(), relationships=()):
    return {"constructs": list(constructs), "measurements": list(measurements), "behaviors": list(behaviors),
            "relationships": list(relationships), "name_mapping": {}}


def C(name):
    return {"type": "construct", "name": name}


def M(name):
    return {"type": "measurement", "name": name}


def B(name):
    return {"type": "behavior", "name": name}


def lines(*ops):
    return list(enumerate(ops, 1))


def run(network, *ops):
    new, rep, cmap = apply_entity_operations(network, lines(*ops))
    live = {(et, g["canonical_name"]): g for et in O.ENTITY_TYPES for g in new[et]}
    return new, rep, live, cmap


def three():
    return net(constructs=[ent("Alpha", ["Alpha", "x", "y"], snippets=["x"]), ent("Beta", ["Beta", "y2"]),
                           ent("Gamma", ["Gamma"])],
               behaviors=[ent("Act", ["Act", "doing"])])


def papers_of(g):
    return {p["paper"] for p in g["papers"]}


# ---------------------------------------------------------------- entity operations

def test_move_chain_lands_in_the_last_entity_with_node_and_snippets():
    new, rep, live, _ = run(three(), {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": C("Beta")},
                            {"op": "move_alias", "name": "x", "from": C("Beta"), "to": C("Gamma")})
    gamma = live[("constructs", "Gamma")]
    assert "x" in gamma["original_names"] and "x" in gamma["original_nodes"]
    assert "x" not in live[("constructs", "Beta")]["original_names"]
    assert any(s["original_name"] == "x" for s in gamma["source_snippets_evidence"])
    assert rep["status"]["1"] == "applied" and rep["status"]["2"].startswith("applied")
    assert papers_of(gamma) == {"P-Gamma", "P-x"} and papers_of(live[("constructs", "Alpha")]) == {"P-Alpha", "P-y"}


def test_move_chain_is_found_whatever_the_line_order():
    new, rep, live, _ = run(three(), {"op": "move_alias", "name": "x", "from": C("Beta"), "to": C("Gamma")},
                            {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": C("Beta")})
    assert "x" in live[("constructs", "Gamma")]["original_names"]
    assert rep["status"]["1"].startswith("applied")


def test_remove_alias_drops_name_node_snippets_and_mapping():
    network = three()
    network["name_mapping"] = {"x": "Alpha", "x variant": "x"}
    new, rep, live, _ = run(network, {"op": "remove_alias", "entity": C("Alpha"), "name": "x", "reason": "r"})
    a = live[("constructs", "Alpha")]
    assert "x" not in a["original_names"] and "x" not in a["original_nodes"]
    assert not any(s["original_name"] == "x" for s in a["source_snippets_evidence"])
    assert "x" not in new["name_mapping"] and papers_of(a) == {"P-Alpha", "P-y"}


def test_two_moves_of_one_name_the_later_line_wins():
    new, rep, live, _ = run(three(), {"op": "move_alias", "name": "y", "from": C("Alpha"), "to": C("Beta")},
                            {"op": "move_alias", "name": "y", "from": C("Alpha"), "to": C("Gamma")})
    assert "y" in live[("constructs", "Gamma")]["original_names"]
    assert rep["status"]["1"].startswith("conflict") and rep["conflicts"] == [[1, 2]]


def test_new_destination_is_created_once_in_its_type_and_reused():
    new, rep, live, _ = run(three(), {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": B("Xing")},
                            {"op": "move_alias", "name": "doing", "from": B("Act"), "to": B("Xing")})
    x = live.get(("behaviors", "Xing"))
    assert x is not None and set(x["original_names"]) == {"x", "doing"}
    assert ("constructs", "Xing") not in live
    assert len(rep["created"]) == 1 and rep["summary"]["created_and_kept"] == 1
    assert papers_of(x) == {"P-x", "P-doing"}


def test_new_entity_names_match_across_case_and_hyphens():
    new, rep, live, _ = run(three(), {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": C("Fact checking ability")},
                            {"op": "move_alias", "name": "y2", "from": C("Beta"), "to": C("Fact-checking ability")})
    fc = [g for g in new["constructs"] if O.norm(g["canonical_name"]) == "fact checking ability"]
    assert len(fc) == 1 and set(fc[0]["original_names"]) == {"x", "y2"}


def test_opposite_moves_are_settled_by_the_later_line():
    network = net(constructs=[ent("Alpha", ["Alpha", "dup"]), ent("Beta", ["Beta", "dup"])])
    new, rep, live, _ = run(network, {"op": "move_alias", "name": "dup", "from": C("Alpha"), "to": C("Beta")},
                            {"op": "move_alias", "name": "dup", "from": C("Beta"), "to": C("Alpha")})
    assert "dup" in live[("constructs", "Alpha")]["original_names"]
    assert "dup" not in live[("constructs", "Beta")]["original_names"]
    assert rep["status"]["1"].startswith("conflict")


def test_destination_matches_an_entity_by_its_final_name_and_type():
    network = net(behaviors=[ent("Problem-solving", ["Problem-solving", "Real-world problem solving"])])
    new, rep, live, _ = run(network, {"op": "set_type", "entity": B("Problem-solving"), "to": "construct"},
                            {"op": "rename", "entity": B("Problem-solving"), "to": "Problem-solving ability"},
                            {"op": "move_alias", "name": "Real-world problem solving", "from": B("Problem-solving"),
                             "to": B("Problem solving")})
    assert ("behaviors", "Problem solving") in live and ("constructs", "Problem-solving ability") in live
    new, rep, live, _ = run(three(), {"op": "rename", "entity": C("Beta"), "to": "Beta ability"},
                            {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": C("Beta ability")})
    assert "x" in live[("constructs", "Beta ability")]["original_names"] and rep["created"] == []


def test_merge_cluster_becomes_one_entity_with_the_cluster_name_and_all_names():
    network = three()
    network["constructs"][1]["papers"] = [{"conference": "iclr24", "paper": p} for p in ("p1", "p2", "p3")]
    new, rep, live, _ = run(network,
                            {"op": "merge", "entities": [C("Alpha"), C("Beta")], "into": C("Beta"), "canonical_name": "Merged"},
                            {"op": "merge", "entities": [C("Beta"), C("Gamma")], "into": C("Gamma"), "canonical_name": "Merged"})
    assert [g["canonical_name"] for g in new["constructs"]] == ["Merged"]
    merged = new["constructs"][0]
    assert {"Alpha", "Beta", "Gamma", "x", "y", "y2"} <= set(merged["original_names"])
    assert papers_of(merged) == {"P-Alpha", "P-x", "P-y", "p1", "p2", "p3", "P-Gamma"}
    assert rep["status"]["1"].startswith("applied") and rep["status"]["2"].startswith("applied")


def test_rename_keeps_old_name_as_alias_and_set_type_moves_the_entity():
    new, rep, live, cmap = run(three(), {"op": "rename", "entity": C("Beta"), "to": "Beta ability"},
                               {"op": "set_type", "entity": C("Gamma"), "to": "behavior"})
    assert "Beta" in live[("constructs", "Beta ability")]["original_names"]
    assert ("behaviors", "Gamma") in live and ("constructs", "Gamma") not in live
    assert cmap["Beta"] == "Beta ability" and cmap["Gamma"] == "Gamma"


def test_remove_restore_and_the_merged_away_conflict():
    new, rep, live, _ = run(three(),
                            {"op": "merge", "entities": [C("Alpha"), C("Beta")], "into": C("Beta"), "canonical_name": "Beta"},
                            {"op": "remove_entity", "entity": C("Alpha"), "reason": "r"},
                            {"op": "remove_entity", "entity": C("Gamma"), "reason": "Out of scope"},
                            {"op": "restore_entity", "entity": B("Act")})
    gamma = live[("constructs", "Gamma")]
    assert gamma["expert_removed"] is True and gamma["expert_removed_reason"] == "Out of scope"
    assert not live[("constructs", "Beta")].get("expert_removed")
    assert rep["status"]["2"].startswith("conflict")
    assert live[("behaviors", "Act")]["expert_removed"] is False


def test_set_summary_replaces_the_summary():
    network = three()
    network["constructs"][0]["characterization_sections"] = {"definition": "old"}
    new, rep, live, _ = run(network, {"op": "set_summary", "entity": C("Alpha"), "text": "New summary."})
    a = live[("constructs", "Alpha")]
    assert a["characterization"] == "New summary." and "characterization_sections" not in a


def test_split_parts_go_to_existing_or_new_entities_never_the_own_name():
    new, rep, live, _ = run(three(), {"op": "split", "entity": C("Alpha"), "into": [
        {"name": "Alpha", "type": "construct", "names": ["Alpha"]},
        {"name": "Gamma", "type": "construct", "names": ["x"]},
        {"name": "Delta", "type": "behavior", "names": ["y", "Alpha"]}]})
    assert "x" in live[("constructs", "Gamma")]["original_names"]
    assert live[("behaviors", "Delta")]["original_names"] == ["y"]
    assert "Alpha" in live[("constructs", "Alpha")]["original_names"]
    assert rep["status"]["1"].startswith("applied: also moved")


def test_paper_credits_follow_names_through_node_papers():
    alpha = ent("Alpha", ["Alpha", "x", "y"], papers=["p0", "p1", "p2", "p3"])
    alpha["original_nodes"]["Alpha"]["papers"] = [["iclr24", "p1"]]
    alpha["original_nodes"]["x"]["papers"] = [["iclr24", "p1"], ["iclr24", "p2"]]
    alpha["original_nodes"]["y"]["papers"] = [["iclr24", "p3"], ["iclr24", "p2"]]
    new, rep, live, _ = run(net(constructs=[alpha]), {"op": "move_alias", "name": "y", "from": C("Alpha"), "to": B("Why")})
    assert papers_of(live[("constructs", "Alpha")]) == {"p0", "p1", "p2"}
    assert papers_of(live[("behaviors", "Why")]) == {"p2", "p3"}
    assert rep["paper_links_gained"] == 2 and rep["paper_links_lost"] == 1


def test_new_entity_without_credits_keeps_its_node_papers():
    alpha = ent("Alpha", ["Alpha", "rare"], papers=["other"])
    new, rep, live, _ = run(net(constructs=[alpha]), {"op": "move_alias", "name": "rare", "from": C("Alpha"), "to": B("Rare twin")})
    assert papers_of(live[("behaviors", "Rare twin")]) == {"P-rare"}
    assert papers_of(live[("constructs", "Alpha")]) == {"other"}
    assert rep["new_entities_on_node_papers"] == 1


def test_case_variants_split_by_their_node_papers():
    lv = ent("LongEval", ["LongEval", "LONGEVAL"], papers=["p1", "p2"])
    lv["original_nodes"]["LongEval"]["papers"] = [["iclr24", "p1"]]
    lv["original_nodes"]["LONGEVAL"]["papers"] = [["iclr24", "p2"]]
    new, rep, live, _ = run(net(measurements=[lv]),
                            {"op": "move_alias", "name": "LONGEVAL", "from": M("LongEval"), "to": M("LongEval (other)")})
    assert papers_of(live[("measurements", "LongEval")]) == {"p1"}
    assert papers_of(live[("measurements", "LongEval (other)")]) == {"p2"}


def test_entities_left_without_names_or_papers_are_dropped():
    network = net(constructs=[ent("Alpha", ["Alpha"]), ent("Beta", ["Beta"])])
    new, rep, live, cmap = run(network, {"op": "move_alias", "name": "Beta", "from": C("Beta"), "to": C("Alpha")})
    assert ("constructs", "Beta") not in live and rep["dropped"][0]["canonical_name"] == "Beta"
    assert cmap["Beta"] == "Alpha"      # Beta's input name lives on in Alpha, which now holds it


def test_name_mapping_follows_moves_and_drops_removed_names():
    network = three()
    network["name_mapping"] = {"x": "Alpha", "y": "Alpha", "old variant": "Alpha"}
    new, rep, live, _ = run(network, {"op": "remove_alias", "entity": C("Alpha"), "name": "x"},
                            {"op": "move_alias", "name": "y", "from": C("Alpha"), "to": C("Gamma")})
    nm = new["name_mapping"]
    assert "x" not in nm and nm["y"] == "Gamma" and nm["old variant"] == "Alpha"


def test_stale_references_are_reported_not_applied():
    new, rep, live, _ = run(three(), {"op": "rename", "entity": C("Nobody"), "to": "X"},
                            {"op": "move_alias", "name": "zzz", "from": C("Alpha"), "to": C("Beta")})
    assert rep["status"]["1"].startswith("stale") and rep["status"]["2"].startswith("stale")
    assert rep["summary"]["status_counts"] == {"stale": 2}


def test_malformed_lines_raise():
    with pytest.raises(OverlayError):
        run(three(), {"op": "rename", "entity": "Alpha", "to": "X"})
    with pytest.raises(OverlayError):
        run(three(), {"op": "set_type", "entity": C("Alpha"), "to": "thing"})


def test_input_network_is_not_modified_by_entity_operations():
    network = three()
    before = copy.deepcopy(network)
    run(network, {"op": "move_alias", "name": "x", "from": C("Alpha"), "to": C("Beta")})
    assert network == before


# ---------------------------------------------------------------- relationship operations

def rel(s, ty, t, papers):
    """papers: list of (title, share, quote)."""
    return {"source": s, "type": ty, "target": t,
            "papers": [{"conference": "iclr24", "paper": p, "type_share": sh} for p, sh, _ in papers],
            "evidence_by_paper": [{"conference": "iclr24", "paper": p, "quote": q} for p, _, q in papers],
            "paper_count": len(papers), "n_papers_split": 0}


def rnet(*rels):
    return {"constructs": [{"canonical_name": n} for n in ("Reasoning", "Mathematical reasoning", "Planning")],
            "measurements": [{"canonical_name": n} for n in ("GSM8K", "MATH")], "behaviors": [],
            "relationships": list(rels)}


def retract(s, ty, t, p, reason="not in the paper"):
    return {"op": "retract_claim", "source": s, "type": ty, "target": t, "paper": f"iclr24:{p}", "reason": reason}


def move(s, ty, t, p, to, quote=None):
    o = {"op": "move_claim", "source": s, "type": ty, "target": t, "paper": f"iclr24:{p}", "to": to}
    if quote is not None:
        o["quote"] = quote
    return o


def add(s, ty, t, p, quote):
    return {"op": "add_claim", "source": s, "type": ty, "target": t, "paper": f"iclr24:{p}", "quote": quote}


def get(N, s, ty, t):
    return next((r for r in N["relationships"] if (r["source"], r["type"], r["target"]) == (s, ty, t)), None)


def rapply(n, *ops, canon_map=None):
    return apply_relationship_operations(n, lines(*ops), canon_map)


def test_retract_drops_paper_and_empty_relationship():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "q1"), ("P2", 1.0, "q2")]),
             rel("Planning", "related", "Reasoning", [("P3", 1.0, "q3")]))
    N, rep = rapply(n, retract("Reasoning", "measured_by", "GSM8K", "P1"), retract("Planning", "related", "Reasoning", "P3"))
    r = get(N, "Reasoning", "measured_by", "GSM8K")
    assert [p["paper"] for p in r["papers"]] == ["P2"] and r["paper_count"] == 1 and r["evidence"] == ["q2"]
    assert get(N, "Planning", "related", "Reasoning") is None and rep["relationships_dropped"] == 1
    assert rep["status"] == {"1": "applied", "2": "applied"}


def test_move_claim_carries_its_evidence_unless_a_quote_is_given():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "stored"), ("P2", 1.0, "q2")]))
    N, rep = rapply(n, move("Reasoning", "measured_by", "GSM8K", "P1", {"source": "Mathematical reasoning"}),
                    move("Reasoning", "measured_by", "GSM8K", "P2", {"source": "Mathematical reasoning"}, quote="new"))
    r = get(N, "Mathematical reasoning", "measured_by", "GSM8K")
    assert r and r["paper_count"] == 2 and [e["quote"] for e in r["evidence_by_paper"]] == ["stored", "new"]
    assert get(N, "Reasoning", "measured_by", "GSM8K") is None and rep["relationships_created"] == 1


def test_retype_changes_the_type_and_sorts_undirected_endpoints():
    n = rnet(rel("Mathematical reasoning", "measured_by", "GSM8K", [("P1", 1.0, "q")]))
    N, rep = rapply(n, {"op": "retype", "source": "Mathematical reasoning", "type": "measured_by", "target": "GSM8K",
                        "paper": "iclr24:P1", "to": "related"})
    r = get(N, "GSM8K", "related", "Mathematical reasoning")
    assert r and r["papers"][0]["paper"] == "P1" and r["evidence"] == ["q"] and rep["claims_moved"] == 1


def test_add_claim_replaces_the_quote_of_an_existing_claim_only():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "bad"), ("P2", 1.0, "q2")]))
    N, rep = rapply(n, add("Reasoning", "measured_by", "GSM8K", "P1", "good"))
    r = get(N, "Reasoning", "measured_by", "GSM8K")
    assert r["paper_count"] == 2 and r["evidence_by_paper"][0]["quote"] == "good" and rep["quotes_replaced"] == 1


def test_add_claim_creates_a_claim_and_a_relationship():
    n = rnet()
    N, rep = rapply(n, add("Planning", "causes", "Reasoning", "P9", "planning helps"))
    r = get(N, "Planning", "causes", "Reasoning")
    assert r["paper_count"] == 1 and r["evidence"] == ["planning helps"] and rep["claims_added"] == 1


def test_resolved_direction_tie_returns_share_to_one():
    n = rnet(rel("Planning", "causes", "Reasoning", [("P1", 0.5, "a")]), rel("Reasoning", "causes", "Planning", [("P1", 0.5, "a")]))
    N, rep = rapply(n, move("Reasoning", "causes", "Planning", "P1", {"source": "Planning", "target": "Reasoning"}))
    r = get(N, "Planning", "causes", "Reasoning")
    assert r["papers"][0]["type_share"] == 1.0 and r["paper_weight"] == 1.0
    assert get(N, "Reasoning", "causes", "Planning") is None and rep["claims_merged_into_existing"] == 1


def test_unresolved_tie_keeps_half_shares():
    n = rnet(rel("Planning", "causes", "Reasoning", [("P1", 0.5, "a")]), rel("Reasoning", "causes", "Planning", [("P1", 0.5, "a")]))
    N, _ = rapply(n)
    assert all(r["papers"][0]["type_share"] == 0.5 for r in N["relationships"])


def test_unmatched_claim_is_skipped():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "q")]))
    N, rep = rapply(n, {"op": "retype", "source": "Reasoning", "type": "measured_by", "target": "MATH",
                        "paper": "iclr24:P1", "to": "related"})
    assert rep["skipped"] == [1] and rep["status"]["1"].startswith("skipped")
    assert get(N, "Reasoning", "measured_by", "GSM8K")["paper_count"] == 1


def test_unknown_endpoint_is_skipped():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "q")]))
    N, rep = rapply(n, move("Reasoning", "measured_by", "GSM8K", "P1", {"source": "No such entity"}))
    assert rep["unknown_endpoint"] == [1] and get(N, "Reasoning", "measured_by", "GSM8K")["paper_count"] == 1


def test_guard_drops_causes_with_an_instrument():
    n = rnet(rel("GSM8K", "causes", "Mathematical reasoning", [("P1", 1.0, "q")]),
             rel("Planning", "causes", "Reasoning", [("P2", 1.0, "q2")]))
    N, rep = rapply(n)
    assert get(N, "GSM8K", "causes", "Mathematical reasoning") is None and rep["guard_claims_dropped:causes"] == 1
    assert get(N, "Planning", "causes", "Reasoning")["paper_count"] == 1


def test_guard_correlates_mixed_becomes_related_but_instrument_pairs_stay():
    n = rnet(rel("GSM8K", "correlates", "Reasoning", [("P1", 1.0, "q1")]),
             rel("GSM8K", "correlates", "MATH", [("P2", 1.0, "q2")]),
             rel("GSM8K", "related", "Reasoning", [("P3", 1.0, "q3")]))
    N, rep = rapply(n)
    assert get(N, "GSM8K", "correlates", "Reasoning") is None
    r = get(N, "GSM8K", "related", "Reasoning")
    assert sorted(p["paper"] for p in r["papers"]) == ["P1", "P3"]
    assert get(N, "GSM8K", "correlates", "MATH")["paper_count"] == 1


def test_guard_measured_by_is_reversed_or_made_related():
    n = rnet(rel("GSM8K", "measured_by", "Reasoning", [("P1", 1.0, "q1")]),
             rel("MATH", "measured_by", "GSM8K", [("P2", 1.0, "q2")]))
    N, rep = rapply(n)
    assert get(N, "Reasoning", "measured_by", "GSM8K")["papers"][0]["paper"] == "P1"
    assert get(N, "GSM8K", "related", "MATH")["papers"][0]["paper"] == "P2"
    assert get(N, "MATH", "measured_by", "GSM8K") is None


def test_guard_merges_into_existing_claim_keeping_its_quote():
    n = rnet(rel("GSM8K", "correlates", "Reasoning", [("P1", 1.0, "moved")]),
             rel("GSM8K", "related", "Reasoning", [("P1", 1.0, "kept")]))
    N, rep = rapply(n)
    r = get(N, "GSM8K", "related", "Reasoning")
    assert r["paper_count"] == 1 and r["evidence_by_paper"][0]["quote"] == "kept" and r["papers"][0]["type_share"] == 1.0
    assert rep["type_guard_rule_from"]


def test_endpoints_follow_renames_merges_and_drops():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "a")]),
             rel("Planning", "measured_by", "GSM8K", [("P1", 1.0, "b"), ("P2", 1.0, "c")]),
             rel("Mathematical reasoning", "measured_by", "MATH", [("P3", 1.0, "d")]))
    n["constructs"] = [{"canonical_name": "Reasoning ability"}, {"canonical_name": "Planning"}]
    N, rep = rapply(n, canon_map={"Reasoning": "Reasoning ability", "Planning": "Reasoning ability",
                                  "Mathematical reasoning": None})
    r = get(N, "Reasoning ability", "measured_by", "GSM8K")
    assert r["paper_count"] == 2 and [e["quote"] for e in r["evidence_by_paper"]] == ["a", "c"]
    assert rep["relationships_merged_after_entity_changes"] == 1
    assert get(N, "Mathematical reasoning", "measured_by", "MATH") is None and rep["relationships_dropped_with_entities"] == 1


def test_relationship_input_is_not_modified():
    n = rnet(rel("Reasoning", "measured_by", "GSM8K", [("P1", 1.0, "q1"), ("P2", 1.0, "q2")]))
    before = copy.deepcopy(n)
    rapply(n, retract("Reasoning", "measured_by", "GSM8K", "P1"))
    assert n == before


# ---------------------------------------------------------------- file-level stage

def test_apply_overlay_end_to_end_with_rerun_vote(tmp_path):
    network = three()
    network["relationships"] = [rel("Alpha", "related", "Beta", [("P-x", 1.0, "q")]),
                                rel("Beta", "measured_by", "Gamma", [("P-Beta", 1.0, "q2")])]
    net_path, ov_path, out_path = tmp_path / "net.json", tmp_path / "ops.jsonl", tmp_path / "out" / "curated.json"
    net_path.write_text(json.dumps(network))
    ops = [{"op": "rename", "entity": C("Gamma"), "to": "Gamma ability", "reason": "ability construct"},
           {"op": "remove_entity", "entity": B("Act"), "reason": "A method"},
           {"op": "retract_claim", "source": "Alpha", "type": "related", "target": "Beta", "paper": "iclr24:P-x"},
           {"op": "retract_claim", "source": "Alpha", "type": "related", "target": "Beta", "paper": "iclr24:nope"}]
    ov_path.write_text("\n".join(json.dumps(o) for o in ops) + "\n\n")
    calls = []

    def revote(network_json, out_json):
        calls.append((network_json, out_json))
        n = json.loads(network_json.read_text())
        assert [g["canonical_name"] for g in n["constructs"]] == ["Alpha", "Beta", "Gamma ability"]
        n["relationships"] = [rel("Alpha", "related", "Beta", [("P-x", 1.0, "q")]),
                              rel("Beta", "related", "Gamma ability", [("P-Beta", 1.0, "q2")])]
        out_json.write_text(json.dumps(n))
        return out_json

    written = apply_overlay(net_path, ov_path, out_path, report_json=tmp_path / "report.json", rerun_vote=revote)
    assert written == out_path and calls == [(out_path, out_path)]
    out = json.loads(out_path.read_text())
    assert [g["canonical_name"] for g in out["constructs"]] == ["Alpha", "Beta", "Gamma ability"]
    act = out["behaviors"][0]
    assert act["expert_removed"] is True and act["expert_removed_reason"] == "A method"
    assert [(r["source"], r["type"], r["target"]) for r in out["relationships"]] == [("Beta", "related", "Gamma ability")]
    assert out["metadata"]["curation"]["lines"] == 4
    assert out["metadata"]["curation"]["relationship_operations"] == {"applied": 1, "skipped": 1}
    report = json.loads((tmp_path / "report.json").read_text())
    assert report["entities"]["status"] == {"1": "applied", "2": "applied"}
    assert report["relationships"]["status"] == {"3": "applied", "4": "skipped: claim not in the network"}
    assert json.loads(net_path.read_text()) == network


def test_apply_overlay_without_rerun_vote_maps_relationship_endpoints(tmp_path):
    network = three()
    network["relationships"] = [rel("Gamma", "measured_by", "Act", [("P-x", 1.0, "q")])]
    network["measurements"] = [ent("Act", ["Act"])]
    network["behaviors"] = []
    net_path, ov_path, out_path = tmp_path / "net.json", tmp_path / "ops.jsonl", tmp_path / "curated.json"
    net_path.write_text(json.dumps(network))
    ov_path.write_text(json.dumps({"op": "rename", "entity": C("Gamma"), "to": "Gamma ability"}) + "\n")
    apply_overlay(net_path, ov_path, out_path)
    out = json.loads(out_path.read_text())
    assert [(r["source"], r["type"], r["target"]) for r in out["relationships"]] == [("Gamma ability", "measured_by", "Act")]


def test_read_overlay_rejects_unknown_operations(tmp_path):
    p = tmp_path / "ops.jsonl"
    p.write_text('{"op": "delete_everything"}\n')
    with pytest.raises(OverlayError):
        read_overlay(p)
    p.write_text('{"op": "rename", "entity": {"type": "construct", "name": "A"}, "to": "B"}\n\n')
    assert read_overlay(p) == [(1, {"op": "rename", "entity": {"type": "construct", "name": "A"}, "to": "B"})]
