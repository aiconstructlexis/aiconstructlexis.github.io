"""Tests of aiconstructlexis.harmonize.residuals: the normalization, the collapse, the
rebuilt name mapping and the command line (in place and with --out)."""
import json

from aiconstructlexis.harmonize import residuals
from aiconstructlexis.harmonize.residuals import collapse, collapse_residuals, normalize, rebuild_name_mapping

# Synthetic name pairs, each labelled with the normalization rule it exercises: the two names
# of a pair differ only by that rule's surface variant, so normalize() gives them one key.
VARIANT_PAIRS = [
    ("case", ["Gizmo reasoning", "GIZMO Reasoning"]),
    ("punctuation and hyphenation", ["Zorp-QA!", "Zorp QA"]),
    ("punctuation and hyphenation", ["Plonk_Bench/Mini", "Plonk Bench Mini"]),
    ("whitespace", ["  Zorp   QA ", "Zorp QA"]),
    ("parenthetical", ["Plonk Bench Hard (PBH)", "Plonk Bench Hard"]),
    ("parenthetical", ["Zorp(I)", "Zorp"]),
    ("filler suffix", ["Gizmo planning", "Gizmo planning ability"]),
    ("filler suffix", ["Gizmo planning abilities", "Gizmo planning skill"]),
    ("filler suffix", ["Zorp", "Zorp benchmark dataset"]),
    ("plural", ["Widget puzzle", "Widget puzzles"]),
    ("plural", ["Widget query", "Widget queries"]),
    ("plural", ["Widget class", "Widget classes"]),
    ("synonym noun", ["Gizmo comprehension", "Gizmo understanding"]),
    ("synonym noun", ["Gizmo awareness", "Gizmo understanding"]),
    ("synonym noun", ["Widget identification", "Widget recognition"]),
    ("morphology", ["Logical gizmo inference", "Logic gizmo inference"]),
    ("morphology", ["Numerical widget estimation", "Numeric widget estimation"]),
    ("morphology", ["Mathematical widget reasoning", "Math widget reasoning"]),
    ("morphology", ["Visio-linguistic gizmo grounding", "Vision-language gizmo grounding"]),
    ("modality prefix", ["Multi-modal gizmo reasoning", "Multimodal gizmo reasoning"]),
    ("modality prefix", ["Cross-modal gizmo retrieval", "Multimodal gizmo retrieval"]),
    ("stopword", ["Recall of the widget facts", "Recall widget facts"]),
    ("word order", ["Gizmo refusal", "Refusal gizmo"]),
]
VARIANT_RULES = {"case", "punctuation and hyphenation", "whitespace", "parenthetical", "filler suffix", "plural",
                 "synonym noun", "morphology", "modality prefix", "stopword", "word order"}


def _g(name, papers):
    papers = list(papers)
    return {"canonical_name": name, "original_names": [name], "papers": papers,
            "paper_count": len(papers), "original_nodes": {name: {"definition": "", "papers": papers}},
            "source_snippets_evidence": [{"original_name": name, "paper": p} for p in papers]}


# ---------------------------------------------------------------- normalize

def test_normalize_folds_the_variant_of_each_rule():
    assert {rule for rule, _ in VARIANT_PAIRS} == VARIANT_RULES
    for rule, names in VARIANT_PAIRS:
        assert len({normalize(n) for n in names}) == 1, (rule, names)


def test_normalize_examples():
    assert normalize("Reasoning ability") == normalize("Reasoning") == "reasoning"
    assert normalize("BIG-Bench Hard (BBH)") == "big bench hard"
    assert normalize("Answer refusal") == normalize("Refusal answer")
    assert normalize("Multi-modal reasoning") == normalize("Multimodal reasoning") == normalize("Cross-modal reasoning")
    assert normalize("Logical reasoning") == normalize("Logic reasoning")
    assert normalize("Reading comprehension") == normalize("Reading understanding")
    assert normalize("") == ""


def test_normalize_keeps_distinct_concepts_apart():
    assert normalize("Mathematical reasoning") != normalize("Reasoning")
    assert normalize("MMLU") != normalize("MMLU-Pro")
    assert normalize("BigBench") != normalize("BIG-bench")  # the hyphen splits a word


# ---------------------------------------------------------------- collapse

def test_collapse_does_not_fold_different_spellings():
    out, merged = collapse([_g("BigBench", ["p0"] * 1), _g("BIG-bench", ["p1"])])
    assert merged == 0 and len(out) == 2


def test_collapse_winner_has_most_papers_and_unions_metadata():
    groups = [_g("Travel planning ability", ["a", "d"]), _g("Travel planning", ["a", "b", "c"]), _g("Memory", ["x"])]
    out, merged = collapse(groups)
    assert merged == 1
    names = [g["canonical_name"] for g in out]
    assert names == ["Travel planning", "Memory"]  # collapsed sets first, then the singletons in order
    win = out[0]
    assert win["original_names"] == ["Travel planning", "Travel planning ability"]
    assert win["papers"] == ["a", "b", "c", "d"] and win["paper_count"] == 4
    assert set(win["original_nodes"]) == {"Travel planning", "Travel planning ability"}
    assert len(win["source_snippets_evidence"]) == 5
    assert groups[0]["canonical_name"] == "Travel planning ability"  # the loser is left as it was


def test_collapse_tie_prefers_shorter_name():
    out, merged = collapse([_g("Reasoning abilities", ["a"]), _g("Reasoning", ["b"])])
    assert merged == 1 and out[0]["canonical_name"] == "Reasoning"
    assert out[0]["papers"] == ["b", "a"]


def test_rebuild_name_mapping():
    net = {"constructs": [{"canonical_name": "Reasoning", "original_names": ["Reasoning ability", "reasoning"]}],
           "measurements": [{"canonical_name": "GSM8K", "original_names": []}],
           "behaviors": [{"canonical_name": "", "original_names": ["ignored"]}]}
    assert rebuild_name_mapping(net) == {"Reasoning": "Reasoning", "Reasoning ability": "Reasoning",
                                         "reasoning": "Reasoning", "GSM8K": "GSM8K"}


# ---------------------------------------------------------------- entry function and CLI

def _net():
    return {"metadata": {"total_papers": 2},
            "constructs": [_g("Travel planning", ["p0", "p1", "p2"]), _g("Travel planning ability", ["p3"])],
            "measurements": [_g("AddSub", ["p0", "p1"]), _g("AddSub+", ["p2"])],
            "behaviors": [], "relationships": [], "name_mapping": {}, "papers": ["p0", "p1", "p2", "p3"]}


def test_collapse_residuals_in_place(tmp_path):
    path = tmp_path / "a.json"
    path.write_text(json.dumps(_net()))
    assert collapse_residuals(path) == path
    out = json.loads(path.read_text())
    assert [g["canonical_name"] for g in out["constructs"]] == ["Travel planning"]
    assert [g["canonical_name"] for g in out["measurements"]] == ["AddSub"]
    assert out["name_mapping"] == {"Travel planning": "Travel planning", "Travel planning ability": "Travel planning",
                                   "AddSub": "AddSub", "AddSub+": "AddSub"}
    assert list(out) == list(_net())  # schema and key order kept
    assert out["metadata"] == {"total_papers": 2}


def test_collapse_residuals_reaggregates_relationships(tmp_path):
    net_path = tmp_path / "net.json"
    net_path.write_text(json.dumps(_net()))
    simplified = {
        "p0": {"parsed_text": {"Nomological Network": {"relationships": [
            {"source": "Travel planning", "target": "AddSub", "type": "measured_by", "evidence": "e0"}]}}},
        "p3": {"parsed_text": {"Nomological Network": {"relationships": [
            {"source": "Travel planning ability", "target": "AddSub+", "type": "measured_by", "evidence": "e3"}]}}},
    }
    simp_path = tmp_path / "simplified.json"
    simp_path.write_text(json.dumps(simplified))
    out_path = collapse_residuals(net_path, simplified_json=simp_path, out_json=tmp_path / "out.json")
    assert out_path == tmp_path / "out.json"
    assert json.loads(net_path.read_text()) == _net()  # input left alone when --out is given
    rels = json.loads(out_path.read_text())["relationships"]
    assert rels == [{"source": "Travel planning", "target": "AddSub", "type": "measured_by",
                     "evidence": ["e0", "e3"], "papers": ["p0", "p3"], "paper_count": 2}]


def test_cli_in_place_and_with_out(tmp_path):
    a, b, b_out = tmp_path / "a.json", tmp_path / "b.json", tmp_path / "b_out.json"
    a.write_text(json.dumps(_net()))
    b.write_text(json.dumps(_net()))
    assert residuals.main(["--harmonized", str(a), "--log-dir", str(tmp_path / "logs")]) == 0
    res = json.loads(a.read_text())
    assert len(res["constructs"]) == 1 and len(res["measurements"]) == 1
    assert residuals.main(["--harmonized", str(b), "--out", str(b_out), "--log-dir", str(tmp_path / "logs")]) == 0
    assert json.loads(b.read_text()) == _net()
    assert json.loads(b_out.read_text()) == res
