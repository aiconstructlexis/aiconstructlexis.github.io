"""End-to-end test of the orchestrator on synthetic data.

``aiconstructlexis.pipeline.run`` is driven through its public entry with a Config built
by ``config_from_dict``. The stages that call a model provider (ingest, screen, extract,
simplify, harmonize, the cross-venue merge, summaries) are replaced by fakes that write
the fixture files where the pipeline expects them and record the keyword arguments they
were called with; the deterministic stages (votes, filter, join, consolidation, curation
overlay, release artifact, site export, readable mirror, analysis bundle, graph layout,
export check) run for real.

The synthetic corpus: two venues, four extracted papers each (plus one paper screened
out), three model labels, entities shared across venues, one entity the vote drops
(one model names it), one the minimum-paper filter drops (one paper), one the overlay
renames and one it removes, and relationships of every type, including a pair that two
models link with different types.
"""
from __future__ import annotations

import copy
import json
import shutil
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

import aiconstructlexis.extract as extract_pkg
import aiconstructlexis.extract.simplify as simplify_mod
import aiconstructlexis.harmonize as harmonize_pkg
import aiconstructlexis.ingest as ingest_pkg
import aiconstructlexis.join as join_pkg
import aiconstructlexis.screen as screen_pkg
import aiconstructlexis.summarize.characterize as characterize_mod
import aiconstructlexis.summarize.checks as checks_mod
from aiconstructlexis import cli, pipeline
from aiconstructlexis.config import ConfigError, config_from_dict, load_config
from aiconstructlexis.export.check import check_site_export
from aiconstructlexis.export.site_data import match_paper_urls, title_key
from aiconstructlexis.ingest.listed import download_listed
from aiconstructlexis.ingest.proceedings import slugify as pdf_stem
from aiconstructlexis.pipeline import Layout, StageError
from aiconstructlexis.util.names import slugify

# ------------------------------------------------------------------------ synthetic corpus

A1 = "Chain of Thought Prompting Elicits Reasoning"
A2 = "Measuring Reasoning with GSM8K"
A3 = "Safety Training and Refusal Behavior"
A4 = "Gradient Clipping Stabilizes Fine-Tuning"
B0 = "A Survey of Graph Databases"            # screened out: not about language models
B1 = "Scaling Laws for Reasoning"
B2 = "Do GSM8K and MMLU Agree?"
B3 = "Fluency and Refusal in Chat Models"
B4 = "Why Models Refuse"

VENUE_A, VENUE_B = "venue_a", "venue_b"
LABELS = ["m1", "m2", "m3"]
PANEL = [{"provider": "google", "model": "gemini-test", "label": "m1"},
         {"provider": "openai", "model": "gpt-test", "label": "m2"},
         {"provider": "together", "model": "qwen-test", "label": "m3"}]
PANEL_B = [dict(PANEL[0]), dict(PANEL[1]), {"provider": "together", "model": "qwen-other-test", "label": "m3"}]

PAPER_LISTS = {
    VENUE_A: [{"title": A1, "url": "https://a.example/1", "is_LLM_paper": True},
              {"title": A2, "url": "https://a.example/2", "is_LLM_paper": True},
              {"title": A3, "url": "https://a.example/3", "is_LLM_paper": True},
              {"title": A4, "url": "https://a.example/4", "is_LLM_paper": True}],
    VENUE_B: [{"name": B0, "url": "https://b.example/0"},
              {"name": B1, "url": "https://b.example/1"},
              {"name": B2, "url": "https://b.example/2"},
              {"name": B3, "url": "https://b.example/3"},
              {"name": B4, "url": "https://b.example/4"}],
}


def C(*names):
    return {"constructs": list(names)}


def _types(**kw):
    """_types(C=[...], M=[...], B=[...]) -> {"constructs": [...], ...}"""
    key = {"C": "constructs", "M": "measurements", "B": "behaviors"}
    return {key[k]: v for k, v in kw.items()}


# Entity trials: {venue: {label: {paper: {entity type: [surface names]}}}}
ENTITY_TRIALS = {
    VENUE_A: {
        "m1": {A1: _types(C=["Reasoning", "Safety"], M=["GSM8K"]),
               A2: _types(C=["Reasoning", "Calibration"], M=["GSM8K"]),
               A3: _types(C=["Safety", "Gradient Clipping"], B=["Refusal"]),
               A4: _types(C=["Gradient Clipping"], B=["Refusal"], M=["GSM8K"])},
        "m2": {A1: _types(C=["reasoning", "safety"], M=["GSM-8K"]),
               A2: _types(C=["Reasoning"], M=["GSM8K"]),
               A3: _types(C=["Safety", "Gradient clipping"], B=["Refusal"]),
               A4: _types(C=["Gradient Clipping"], B=["Refusals"])},
        "m3": {A1: _types(C=["Reasoning"], M=["GSM8K"]),
               A2: _types(C=["Reasoning"]),
               A3: _types(B=["Refusal"]),
               A4: _types(C=["Gradient Clipping"])},
    },
    VENUE_B: {
        "m1": {B1: _types(C=["Reasoning"], M=["GSM8K"]),
               B2: _types(C=["Reasoning"], M=["GSM8K", "MMLU"]),
               B3: _types(C=["Fluency"], M=["MMLU"], B=["Refusal"]),
               B4: _types(B=["Refusal"])},
        "m2": {B1: _types(C=["Reasoning"], M=["GSM8K"]),
               B2: _types(C=["Reasoning"], M=["GSM-8K", "MMLU"]),
               B3: _types(C=["Fluency"], M=["MMLU"], B=["Refusal"]),
               B4: _types(B=["Refusal behavior"])},
        "m3": {B1: _types(C=["Reasoning"]),
               B2: _types(M=["MMLU"]),
               B3: _types(B=["Refusal"]),
               B4: _types(C=["Reasoning"])},
    },
}


def R(src, tgt, rtype, quote):
    return {"source": src, "target": tgt, "type": rtype, "evidence": quote}


# Relationship trials: {venue: {label: {paper: [claims]}}}
RELATIONSHIP_TRIALS = {
    VENUE_A: {
        "m1": {A1: [R("Reasoning", "GSM8K", "measured_by", "We evaluate reasoning on GSM8K.")],
               A2: [R("GSM8K", "Reasoning", "measured_by", "GSM8K scores track reasoning."),
                    R("Calibration", "GSM8K", "measured_by", "Calibration on GSM8K.")],
               A3: [R("Safety", "Refusal", "causes", "Safety training increases refusals."),
                    R("Gradient Clipping", "Reasoning", "related", "Clipping and reasoning.")],
               A4: [R("Refusal", "GSM8K", "related", "A claim one model makes."),
                    R("Gradient Clipping", "Reasoning", "related", "Clipping stabilizes reasoning training.")]},
        "m2": {A1: [R("Reasoning", "GSM8K", "related", "GSM8K is a reasoning dataset."),
                    R("Reasoning", "Safety", "related", "Reasoning and safety interact.")],
               A2: [R("Calibration", "GSM8K", "measured_by", "Calibration measured on GSM8K.")],
               A3: [R("Safety", "Refusal", "causes", "Safety tuning causes refusal."),
                    R("Gradient clipping", "Reasoning", "related", "Clipping versus reasoning.")],
               A4: []},
        "m3": {A1: [R("Safety", "Reasoning", "related", "Safety relates to reasoning.")],
               A2: [R("Reasoning", "GSM8K", "measured_by", "Reasoning is measured by GSM8K.")],
               A3: [],
               A4: [R("Gradient Clipping", "Reasoning", "related", "Clipping helps reasoning.")]},
    },
    VENUE_B: {
        "m1": {B1: [R("Reasoning", "GSM8K", "measured_by", "GSM8K measures reasoning.")],
               B2: [R("Reasoning", "GSM8K", "measured_by", "We report GSM8K for reasoning."),
                    R("GSM8K", "MMLU", "correlates", "GSM8K and MMLU scores correlate.")],
               B3: [R("Refusal", "MMLU", "measured_by", "Refusal rate on MMLU."),
                    R("Fluency", "MMLU", "measured_by", "Fluency on MMLU.")],
               B4: [R("Reasoning", "GSM8K", "related", "Refusing models score lower on GSM8K.")]},
        "m2": {B1: [R("GSM8K", "Reasoning", "causes", "Training on GSM8K causes reasoning.")],
               B2: [R("Reasoning", "GSM8K", "measured_by", "GSM8K as the reasoning measure."),
                    R("MMLU", "GSM8K", "correlates", "MMLU correlates with GSM8K.")],
               B3: [R("Refusal", "MMLU", "measured_by", "MMLU refusal rate."),
                    R("Fluency", "MMLU", "measured_by", "Fluency on MMLU.")],
               B4: []},
        "m3": {B1: [], B2: [], B3: [],
               B4: [R("GSM8K", "Reasoning", "related", "GSM8K relates to reasoning.")]},
    },
}


def _ent(name, names, nodes, definition="A definition."):
    """A harmonized entity: nodes maps surface name -> papers (venue-level: plain titles)."""
    papers = sorted({p for ps in nodes.values() for p in ps})
    return {
        "canonical_name": name,
        "original_names": list(names),
        "original_nodes": {n: {"definition": definition if ps else "An orphan definition.", "papers": list(ps)}
                           for n, ps in nodes.items()},
        "source_snippets_evidence": [{"original_name": n, "paper": ps[0], "snippet": f"{n} snippet"}
                                     for n, ps in nodes.items() if ps],
        "papers": papers,
        "paper_count": len(papers),
    }


def _hrel(src, tgt, rtype, papers):
    return {"source": src, "target": tgt, "type": rtype, "papers": list(papers),
            "evidence": [f"{src} {rtype} {tgt}"], "paper_count": len(papers)}


# What the (faked) harmonization stage writes per venue; the vote rewrites the paper lists.
HARMONIZED = {
    VENUE_A: {
        "metadata": {"conference": VENUE_A},
        "constructs": [
            _ent("Reasoning", ["Reasoning", "Reasoning ability"],
                 {"Reasoning": [A1, A2], "Reasoning ability": []}, "The ability to draw inferences."),
            _ent("Safety", ["Safety"], {"Safety": [A1, A3]}, "Avoiding harmful outputs."),
            _ent("Calibration", ["Calibration"], {"Calibration": [A2]}, "Confidence matches accuracy."),
            _ent("Gradient Clipping", ["Gradient Clipping"], {"Gradient Clipping": [A3, A4]}, "A training trick."),
        ],
        "measurements": [_ent("GSM8K", ["GSM8K", "GSM-8K"], {"GSM8K": [A1, A2, A4], "GSM-8K": [A1]},
                              "Grade-school math word problems.")],
        "behaviors": [_ent("Refusal", ["Refusal", "Refusals"], {"Refusal": [A3, A4], "Refusals": [A4]},
                           "Declining to answer.")],
        "relationships": [_hrel("Reasoning", "GSM8K", "measured_by", [A1, A2]),
                          _hrel("Safety", "Refusal", "causes", [A3]),
                          _hrel("Calibration", "GSM8K", "measured_by", [A2])],
        "name_mapping": {"Reasoning": "Reasoning", "Reasoning ability": "Reasoning", "Safety": "Safety",
                         "Calibration": "Calibration", "Gradient Clipping": "Gradient Clipping",
                         "GSM8K": "GSM8K", "GSM-8K": "GSM8K", "Refusal": "Refusal", "Refusals": "Refusal"},
        "papers": [A1, A2, A3, A4],
    },
    VENUE_B: {
        "metadata": {"conference": VENUE_B},
        "constructs": [
            _ent("Reasoning", ["Reasoning"], {"Reasoning": [B1, B2, B4]}, "Multi-step inference."),
            _ent("Fluency", ["Fluency"], {"Fluency": [B3]}, "Natural, well-formed text."),
        ],
        "measurements": [_ent("GSM8K", ["GSM8K", "GSM-8K"], {"GSM8K": [B1, B2], "GSM-8K": [B2]}, "Math problems."),
                         _ent("MMLU", ["MMLU"], {"MMLU": [B2, B3]}, "Multitask knowledge test.")],
        "behaviors": [_ent("Refusal", ["Refusal", "Refusal behavior"],
                           {"Refusal": [B3, B4], "Refusal behavior": [B4]}, "Refusing a request.")],
        "relationships": [_hrel("Reasoning", "GSM8K", "measured_by", [B1, B2]),
                          _hrel("GSM8K", "MMLU", "correlates", [B2])],
        "name_mapping": {"Reasoning": "Reasoning", "Fluency": "Fluency", "GSM8K": "GSM8K", "GSM-8K": "GSM8K",
                         "MMLU": "MMLU", "Refusal": "Refusal", "Refusal behavior": "Refusal"},
        "papers": [B1, B2, B3, B4],
    },
}

OVERLAY_LINES = [
    {"op": "rename", "entity": {"type": "construct", "name": "Safety"}, "to": "Model safety"},
    {"op": "remove_entity", "entity": {"type": "construct", "name": "Gradient Clipping"},
     "reason": "A training technique, not a property of a model"},
]

REMOVED_REASON = "A training technique, not a property of a model"

EMPIRICAL_EVIDENCE = {"about": "Papers that empirically validate constructs, instruments or behaviors.",
                      "rows": [{"title": A1, "venue": VENUE_A, "constructs": ["Reasoning"]}]}


def raw_config(summaries_enabled=False):
    return copy.deepcopy({
        "version": "0.0.1",
        "paths": {"work_dir": "work", "pdf_dir": "pdfs", "log_dir": "logs"},
        "prompts": "default",
        "venues": [
            {"id": VENUE_A, "conference": "iclr", "year": 2024, "source": "proceedings",
             "papers": f"lists/{VENUE_A}.json"},
            {"id": VENUE_B, "conference": "neurips", "year": 2024, "source": "proceedings", "models": PANEL_B},
        ],
        "screening": {"enabled": True, "provider": "together", "model": "test-screener", "mode": "sync",
                      "workers": 2, "max_rpm": 100, "poll_interval": 5},
        "extraction": {"models": PANEL, "temperature": 0.0, "workers": 3, "max_papers": 0, "max_tokens": 4096},
        "harmonization": {"provider": "google", "model": "gemini-harmonizer", "batch_size": 50,
                          "batch_retries": 1, "on_batch_failure": "stop", "reasoning_effort": "low"},
        "voting": {"threshold": 2, "min_papers": 2, "survivor": "strictest", "type_guard": True},
        "join": {"provider": "openai", "model": "gpt-merger", "batch_size": 250, "reasoning_effort": "medium",
                 "postmerge": True},
        "curation": {"overlay": "overlay.jsonl"},
        "summaries": {"enabled": summaries_enabled, "provider": "openai", "model": "gpt-summarizer",
                      "reasoning_effort": "low", "min_papers": 3, "poll_interval": 1, "check_retry": False},
        "export": {"site_dir": "site", "artifact_out": "lexis/artifact.json", "readable": True,
                   "analysis_bundle": True, "graph_layout": True, "layout_seed": 3, "check": True},
    })


def write_inputs(root: Path) -> None:
    (root / "lists").mkdir(parents=True, exist_ok=True)
    (root / "lists" / f"{VENUE_A}.json").write_text(json.dumps(PAPER_LISTS[VENUE_A]), encoding="utf-8")
    (root / "overlay.jsonl").write_text("\n".join(json.dumps(line) for line in OVERLAY_LINES) + "\n",
                                        encoding="utf-8")
    # the hand-maintained file of the Empirical Evidence page, which the export leaves alone
    write_json(root / "site" / "data" / "empirical_evidence.json", EMPIRICAL_EVIDENCE)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=1), encoding="utf-8")


# -------------------------------------------------------------------------------- fakes

class Fakes:
    """Replacements for the provider-calling stage functions. Every call is recorded."""

    def __init__(self):
        self.calls = defaultdict(list)

    def install(self, mp: pytest.MonkeyPatch) -> None:
        mp.setattr(ingest_pkg, "download_listed", self.download_listed)
        mp.setattr(ingest_pkg, "download_venue", self.download_venue)
        mp.setattr(screen_pkg, "screen_papers", self.screen_papers)
        mp.setattr(extract_pkg, "run_extraction", self.run_extraction)
        mp.setattr(simplify_mod, "simplify", self.simplify)
        mp.setattr(harmonize_pkg, "harmonize", self.harmonize)
        mp.setattr(harmonize_pkg, "aggregate_relationships", self.aggregate_relationships)
        mp.setattr(harmonize_pkg, "collapse_residuals", self.collapse_residuals)
        mp.setattr(join_pkg, "merge_joint_network", self.merge_joint_network)
        mp.setattr(characterize_mod, "characterize", self.characterize)
        mp.setattr(checks_mod, "check_characterizations", self.check_characterizations)

    def _record(self, name, **kwargs):
        self.calls[name].append(kwargs)

    @staticmethod
    def _venue_of(path) -> str:
        return Path(path).parent.name

    # ingest
    def download_listed(self, paper_list_json, out_json, pdf_dir=None, **kw):
        self._record("download_listed", paper_list_json=paper_list_json, out_json=out_json, pdf_dir=pdf_dir, **kw)
        records = read_json(paper_list_json)
        entries = []
        for p in records:
            e = {"name": p.get("name") or p["title"], "url": p["url"], "is_LLM_paper": p["is_LLM_paper"]}
            if e["is_LLM_paper"]:
                e["path"] = str(Path(pdf_dir) / f"{slugify(e['name'])}.pdf")
            entries.append(e)
        write_json(out_json, entries)
        return Path(out_json)

    def download_venue(self, conference, year, out_json, pdf_dir, source="proceedings", **kw):
        self._record("download_venue", conference=conference, year=year, out_json=out_json, pdf_dir=pdf_dir,
                     source=source, **kw)
        venue = self._venue_of(out_json)
        entries = [{"name": p["name"], "url": p["url"], "path": str(Path(pdf_dir) / f"{slugify(p['name'])}.pdf")}
                   for p in PAPER_LISTS[venue]]
        write_json(out_json, entries)
        return Path(out_json)

    # screen
    def screen_papers(self, input_json, output_json, **kw):
        self._record("screen_papers", input_json=input_json, output_json=output_json, **kw)
        papers = read_json(input_json)
        for p in papers:
            p["is_LLM_paper"] = p["name"] != B0
        write_json(output_json, papers)
        return Path(output_json)

    # extract
    def run_extraction(self, papers_json, work_dir, models=None, vote_threshold=2, **kw):
        self._record("run_extraction", papers_json=papers_json, work_dir=work_dir, models=models,
                     vote_threshold=vote_threshold, **kw)
        work_dir = Path(work_dir)
        if kw.get("dry_run"):
            report = work_dir / "dry_run" / "report.json"
            write_json(report, {"requests": 0})
            return report
        venue = self._venue_of(papers_json)
        flagged = [p["name"] for p in read_json(papers_json) if p.get("is_LLM_paper") is True]
        assert B0 not in flagged
        for m in models:
            label = m["label"]
            ents = {paper: [{"Nomological Network": {et: [{"name": n} for n in names]
                                                     for et, names in types.items()}}]
                    for paper, types in ENTITY_TRIALS[venue][label].items() if paper in flagged}
            rels = {paper: [claims] for paper, claims in RELATIONSHIP_TRIALS[venue][label].items()
                    if paper in flagged}
            write_json(work_dir / "trials" / label / "entity_trials.json", ents)
            write_json(work_dir / "trials" / label / "relationship_trials.json", rels)
        extraction = work_dir / "inputs" / "extraction.json"
        write_json(extraction, {p: {"name": p, "result": {"parsed_text": {"Nomological Network": {}}}}
                                for p in flagged})
        return extraction

    def simplify(self, input_json, output_json, **kw):
        self._record("simplify", input_json=input_json, output_json=output_json, **kw)
        Path(output_json).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(input_json, output_json)
        return Path(output_json)

    # harmonize
    def harmonize(self, input_json, output_json, **kw):
        self._record("harmonize", input_json=input_json, output_json=output_json, **kw)
        assert Path(input_json).is_file()
        write_json(output_json, HARMONIZED[self._venue_of(output_json)])
        return Path(output_json)

    def aggregate_relationships(self, simplified_json, harmonized_json, **kw):
        self._record("aggregate_relationships", simplified_json=simplified_json, harmonized_json=harmonized_json, **kw)
        assert Path(simplified_json).is_file() and Path(harmonized_json).is_file()
        return Path(harmonized_json)

    def collapse_residuals(self, harmonized_json, simplified_json=None, **kw):
        self._record("collapse_residuals", harmonized_json=harmonized_json, simplified_json=simplified_json, **kw)
        assert Path(harmonized_json).is_file()
        return Path(harmonized_json)

    # join
    def merge_joint_network(self, input_json, output_json, **kw):
        self._record("merge_joint_network", input_json=input_json, output_json=output_json, **kw)
        Path(output_json).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(input_json, output_json)
        return Path(output_json)

    # summarize
    def characterize(self, input_json, output_json, **kw):
        self._record("characterize", input_json=input_json, output_json=output_json, **kw)
        net = read_json(input_json)
        for et in ("constructs", "measurements", "behaviors"):
            for g in net[et]:
                if g["paper_count"] >= kw["min_papers"] and not g.get("expert_removed"):
                    g["characterization"] = f"Summary of {g['canonical_name']}."
        write_json(output_json, net)
        return Path(output_json)

    def check_characterizations(self, input_json, output_json, **kw):
        self._record("check_characterizations", input_json=input_json, output_json=output_json, **kw)
        assert Path(input_json).is_file() and Path(output_json).is_file()
        return {"entities_checked": 0}


class World:
    """Everything a test needs from the full run."""

    def __init__(self, root: Path, cfg, fakes: Fakes, written):
        self.root, self.cfg, self.fakes, self.written = root, cfg, fakes, written
        self.lay = Layout(cfg)
        self.site = cfg.export.site_dir
        self.data = self.site / "data"

    def venue(self, vid):
        return self.cfg.venue(vid)

    def artifact(self):
        return read_json(self.lay.artifact)


@pytest.fixture(scope="module")
def world(tmp_path_factory) -> World:
    root = tmp_path_factory.mktemp("lexis_run")
    write_inputs(root)
    cfg = config_from_dict(raw_config(), base_dir=root)
    fakes = Fakes()
    with pytest.MonkeyPatch.context() as mp:
        fakes.install(mp)
        written = pipeline.run(cfg)
    return World(root, cfg, fakes, written)


def entities(net, et):
    return {g["canonical_name"]: g for g in net[et]}


def pair_types(net):
    out = defaultdict(set)
    for r in net["relationships"]:
        out[frozenset((r["source"], r["target"]))].add(r["type"])
    return out


# ---------------------------------------------------------------- the run as a whole

def test_run_returns_every_stage_output(world):
    lay = world.lay
    expected = {}
    for v in world.cfg.venues:
        expected[f"{v.id}/ingest"] = lay.papers(v)
        expected[f"{v.id}/screen"] = lay.papers(v)
        expected[f"{v.id}/extract"] = lay.extraction(v)
        expected[f"{v.id}/simplify"] = lay.simplified(v)
        expected[f"{v.id}/harmonize"] = lay.harmonized(v)
        expected[f"{v.id}/vote"] = lay.multi_paper(v)
    expected.update({"join": lay.voted, "curate": lay.curated, "summarize": lay.summarized,
                     "export": lay.artifact})
    assert world.written == expected
    for path in expected.values():
        assert Path(path).is_file(), path


def test_every_expected_file_exists(world):
    lay, data, site = world.lay, world.data, world.site
    for name in ("union.json", "merged.json", "voted.json", "curated.json", "curated.report.json",
                 "summarized.json", "ai_construct_lexis_v0.0.1.json"):
        assert (world.cfg.joint_dir / name).is_file(), name
    assert lay.artifact.name == "ai_construct_lexis_v0.0.1.json"
    assert (world.root / "lexis" / "artifact.json").read_bytes() == lay.artifact.read_bytes()
    for name in ("paper_urls.json", "graph.bundle.json", "analysis.bundle.json", "analysis_evidence.json",
                 "layout.json"):
        assert (data / name).is_file(), name
    assert sorted(p.name for p in data.iterdir()) == [
        "analysis.bundle.json", "analysis_evidence.json", "behaviors_tasks", "constructs", "empirical_evidence.json",
        "graph.bundle.json", "layout.json", "measurements", "paper_urls.json", "readable"]
    assert read_json(data / "empirical_evidence.json") == EMPIRICAL_EVIDENCE
    # one record and one Markdown page per in-scope entity; the removed one has neither
    files = {sub: sorted(p.name for p in (data / sub).iterdir()) for sub in ("constructs", "measurements", "behaviors_tasks")}
    assert files == {"constructs": ["model_safety.json", "reasoning.json"],
                     "measurements": ["gsm8k.json", "mmlu.json"],
                     "behaviors_tasks": ["refusal.json"]}
    for sub, names in files.items():
        assert sorted(p.name for p in (site / "data/readable" / sub).iterdir()) == \
            [f.replace(".json", ".md") for f in names]


def test_plan_lists_every_stage(world):
    lines = pipeline.plan(world.cfg)
    assert len(lines) == 2 * len(pipeline.VENUE_STAGES) + len(pipeline.JOINT_STAGES)
    for stage in pipeline.STAGES:
        assert any(f" {stage} " in line or f" {stage:<9} " in line for line in lines), stage
    for v in world.cfg.venues:
        assert sum(v.id in line for line in lines) == len(pipeline.VENUE_STAGES)
    assert sum("joint" in line for line in lines) == len(pipeline.JOINT_STAGES)
    only = pipeline.plan(world.cfg, stages=["vote,join"], venues=[VENUE_B])
    assert [line.split()[1] for line in only] == ["vote", "join"]
    with pytest.raises(StageError):
        pipeline.select_stages(["vote", "polish"])


# ---------------------------------------------------------------- the fakes saw the config

def test_ingest_and_screen_calls(world):
    calls, cfg, lay = world.fakes.calls, world.cfg, world.lay
    a, b = world.venue(VENUE_A), world.venue(VENUE_B)
    assert calls["download_listed"] == [{"paper_list_json": a.papers, "out_json": lay.papers(a),
                                         "pdf_dir": cfg.pdf_dir / VENUE_A, "sample": None}]
    assert a.papers == world.root / "lists" / f"{VENUE_A}.json"
    assert calls["download_venue"] == [{"conference": "neurips", "year": 2024, "out_json": lay.papers(b), "tracks": None, "sample": None,
                                        "pdf_dir": cfg.pdf_dir / VENUE_B, "source": "proceedings"}]
    # venue_a's list already carried is_LLM_paper, so only venue_b was screened
    assert calls["screen_papers"] == [{"input_json": lay.papers(b), "output_json": lay.papers(b),
                                       "provider": "together", "model": "test-screener", "mode": "sync",
                                       "prompts": "default", "workers": 2, "max_rpm": 100, "poll_interval": 5,
                                       "conference": "neurips"}]
    papers_b = read_json(lay.papers(b))
    assert [p["is_LLM_paper"] for p in papers_b] == [False, True, True, True, True]


def test_extract_simplify_harmonize_calls(world):
    calls, cfg, lay = world.fakes.calls, world.cfg, world.lay
    a, b = world.venue(VENUE_A), world.venue(VENUE_B)
    common = {"temperature": 0.0, "workers": 3, "max_papers": 0, "allow_partial": False, "dry_run": False,
              "prompts": "default", "max_tokens": 4096, "vote_threshold": 2}
    assert calls["run_extraction"] == [
        {"papers_json": lay.papers(a), "work_dir": lay.extraction_dir(a), "models": PANEL, "conference": "iclr",
         **common},
        {"papers_json": lay.papers(b), "work_dir": lay.extraction_dir(b), "models": PANEL_B, "conference": "neurips",
         **common},
    ]
    assert calls["simplify"] == [{"input_json": lay.extraction(v), "output_json": lay.simplified(v)} for v in (a, b)]
    assert calls["harmonize"] == [
        {"input_json": lay.simplified(v), "output_json": lay.harmonized(v), "provider": "google",
         "model": "gemini-harmonizer", "batch_size": 50, "name_mapping": None,
         "name_mapping_out": cfg.venue_dir(v.id) / "name_mapping.json",
         "batch_retries": 1, "on_batch_failure": "stop", "reasoning_effort": "low", "prompts": "default"}
        for v in (a, b)]
    assert calls["aggregate_relationships"] == [{"simplified_json": lay.simplified(v), "harmonized_json": lay.harmonized(v)}
                                                for v in (a, b)]
    assert calls["collapse_residuals"] == [{"harmonized_json": lay.harmonized(v), "simplified_json": lay.simplified(v)}
                                           for v in (a, b)]
    for v in (a, b):
        for label in LABELS:
            assert (lay.trials_dir(v) / label / "entity_trials.json").is_file()
            assert (lay.trials_dir(v) / label / "relationship_trials.json").is_file()


def test_join_and_summary_calls(world):
    calls, lay = world.fakes.calls, world.lay
    assert calls["merge_joint_network"] == [{"input_json": lay.union, "output_json": lay.merged, "provider": "openai",
                                             "model": "gpt-merger", "batch_size": 250, "reasoning_effort": "medium",
                                             "prompts": "default"}]
    assert calls["characterize"] == [] and calls["check_characterizations"] == []
    # summaries disabled: the curated network is carried forward unchanged
    assert read_json(lay.summarized) == read_json(lay.curated)


# ---------------------------------------------------------------- per-venue vote

def test_venue_vote_and_filter(world):
    lay = world.lay
    a = read_json(lay.multi_paper(world.venue(VENUE_A)))
    b = read_json(lay.multi_paper(world.venue(VENUE_B)))
    # one model named Calibration: dropped by the vote; Fluency had one paper: dropped by the filter
    assert set(entities(a, "constructs")) == {"Reasoning", "Safety", "Gradient Clipping"}
    assert set(entities(b, "constructs")) == {"Reasoning"}
    harmonized_b = read_json(lay.harmonized(world.venue(VENUE_B)))
    fluency = entities(harmonized_b, "constructs")["Fluency"]
    assert fluency["papers"] == [B3] and fluency["_canonical_mv"] == {"threshold": 2, "n_papers_total": 1, "n_papers_mv": 1}
    assert "Calibration" not in entities(read_json(lay.harmonized(world.venue(VENUE_A))), "constructs")
    # credits are counted at the canonical level: GSM-8K and Refusals count as votes for their entities
    assert entities(a, "measurements")["GSM8K"]["papers"] == sorted([A1, A2])      # A4: one model only
    assert entities(a, "behaviors")["Refusal"]["papers"] == sorted([A3, A4])
    assert entities(b, "behaviors")["Refusal"]["papers"] == sorted([B3, B4])
    assert entities(b, "constructs")["Reasoning"]["papers"] == sorted([B1, B2])     # B4: one model only
    assert entities(b, "measurements")["MMLU"]["papers"] == sorted([B2, B3])
    for net in (a, b):
        for et in ("constructs", "measurements", "behaviors"):
            for g in net[et]:
                assert g["paper_count"] == len(g["papers"]) >= 2 and g["_canonical_mv"]["threshold"] == 2
    # the filter rebuilds the name mapping from the survivors
    assert "Fluency" not in b["name_mapping"] and b["name_mapping"]["Refusal behavior"] == "Refusal"
    assert all(r["source"] != "Calibration" for r in a["relationships"])


# ---------------------------------------------------------------- joint stages

def test_union_merges_shared_entities(world):
    union = read_json(world.lay.union)
    assert union["metadata"]["joint_of"] == [VENUE_A, VENUE_B]
    assert [g["canonical_name"] for g in union["constructs"]] == ["Reasoning", "Safety", "Gradient Clipping"]
    reasoning = entities(union, "constructs")["Reasoning"]
    assert {c: sorted(ps) for c, ps in reasoning["papers_by_conference"].items()} == \
        {VENUE_A: sorted([A1, A2]), VENUE_B: sorted([B1, B2])}
    assert reasoning["original_nodes"]["Reasoning ability"]["papers"] == []     # the orphan node, still present here
    assert union["paper_count_by_conference"] == {VENUE_A: 4, VENUE_B: 4}
    assert len(union["papers"]) == 8
    # merged.json is the (faked) merge output after the joint entity vote rewrote it in place
    merged = read_json(world.lay.merged)
    for et in ("constructs", "measurements", "behaviors"):
        assert [g["canonical_name"] for g in merged[et]] == [g["canonical_name"] for g in union[et]]
        assert all(g["_canonical_mv"]["threshold"] == 2 for g in merged[et])
    assert merged["relationships"] == union["relationships"]


def test_voted_network(world):
    voted = read_json(world.lay.voted)
    assert set(entities(voted, "constructs")) == {"Reasoning", "Safety", "Gradient Clipping"}
    assert set(entities(voted, "measurements")) == {"GSM8K", "MMLU"}
    assert set(entities(voted, "behaviors")) == {"Refusal"}
    reasoning = entities(voted, "constructs")["Reasoning"]
    assert reasoning["paper_count"] == 4 and reasoning["paper_count_by_conference"] == {VENUE_A: 2, VENUE_B: 2}
    assert "Reasoning ability" not in reasoning["original_nodes"]           # orphan definition dropped
    rels = {(r["source"], r["type"], r["target"]): r for r in voted["relationships"]}
    assert set(rels) == {
        ("Reasoning", "measured_by", "GSM8K"),
        ("Reasoning", "related", "Safety"),
        ("Safety", "causes", "Refusal"),
        ("Gradient Clipping", "related", "Reasoning"),
        ("GSM8K", "correlates", "MMLU"),
        ("Refusal", "measured_by", "MMLU"),
    }
    mb = rels[("Reasoning", "measured_by", "GSM8K")]
    # A1: one model said measured_by, the other related -> the strictest type, measured_by, counts for the paper;
    # A2: the model that put the instrument first still votes for the same label;
    # B1: the strictest type was causes, which the type guard drops for an instrument;
    # B4: both models said related, folded into the pair's one surviving type.
    assert {c: sorted(ps) for c, ps in mb["papers_by_conference"].items()} == \
        {VENUE_A: sorted([A1, A2]), VENUE_B: sorted([B2, B4])}
    assert mb["paper_count"] == 4 and mb["paper_weight"] == 4.0 and mb["n_papers_split"] == 1
    assert mb["type_breakdown"] == {"measured_by": 3, "related": 1}
    assert mb["consolidated_from"] == [["GSM8K", "related", "Reasoning"]]
    claim_types = {p["paper"]: p["claim_type"] for p in mb["papers"]}
    assert claim_types == {A1: "measured_by", A2: "measured_by", B2: "measured_by", B4: "related"}
    quotes = {e["paper"]: e["quote"] for e in mb["evidence_by_paper"]}
    assert quotes[A1] == "We evaluate reasoning on GSM8K."
    assert rels[("Gradient Clipping", "related", "Reasoning")]["paper_count"] == 2
    assert all(p["type_share"] == 1.0 for r in voted["relationships"] for p in r["papers"])
    assert voted["metadata"]["pair_type_consolidation"]["edges_merged"] == 1


def test_curation_overlay_applied(world):
    curated = read_json(world.lay.curated)
    cons = entities(curated, "constructs")
    assert set(cons) == {"Reasoning", "Model safety", "Gradient Clipping"}
    assert "Safety" in cons["Model safety"]["original_names"]
    assert cons["Model safety"]["paper_count"] == 2
    assert cons["Gradient Clipping"]["expert_removed"] is True
    assert cons["Gradient Clipping"]["expert_removed_reason"] == REMOVED_REASON
    # the relationship vote ran again on the renamed catalog
    rels = {(r["source"], r["type"], r["target"]) for r in curated["relationships"]}
    assert ("Model safety", "related", "Reasoning") in rels and ("Model safety", "causes", "Refusal") in rels
    assert not any("Safety" in k for k in rels)
    assert curated["metadata"]["curation"]["entity_operations"] == {"applied": 2}
    report = read_json(world.lay.curated.with_suffix(".report.json"))
    assert report["entities"]["status"] == {"1": "applied", "2": "applied"}
    assert report["relationships"]["type_guard_rule_from"] == "aiconstructlexis.vote.relationships"


# ---------------------------------------------------------------- the artifact

def test_artifact_metadata_and_entities(world):
    art = world.artifact()
    assert list(art)[0] == "metadata"
    live = {et: [g["canonical_name"] for g in art[et] if not g.get("expert_removed")]
            for et in ("constructs", "measurements", "behaviors")}
    assert live == {"constructs": ["Model safety", "Reasoning"], "measurements": ["GSM8K", "MMLU"],
                    "behaviors": ["Refusal"]}
    assert art["metadata"] == {
        "name": "AI Construct Lexis", "version": "0.0.1", "venues": [VENUE_A, VENUE_B],
        "paper_count_by_conference": {VENUE_A: 4, VENUE_B: 4},
        "counts": {"constructs": 2, "measurements": 2, "behaviors": 1, "relationships": 6,
                   "relationships_between_in_scope_entities": sum(
                       1 for r in art["relationships"]
                       if r["source"] in set(sum(live.values(), [])) and r["target"] in set(sum(live.values(), []))),
                   "papers": 8},
        "notes": art["metadata"]["notes"]}
    assert "expert review" in art["metadata"]["notes"]
    names = {g["canonical_name"] for et in ("constructs", "measurements", "behaviors") for g in art[et]}
    assert {"Calibration", "Fluency", "Safety"}.isdisjoint(names)
    assert "Model safety" in names
    removed = entities(art, "constructs")["Gradient Clipping"]
    assert removed["expert_removed"] is True and removed["expert_removed_reason"] == REMOVED_REASON
    for et in ("constructs", "measurements", "behaviors"):
        for g in art[et]:
            assert "_canonical_mv" not in g and "characterizations" not in g
    assert len(art["papers"]) == 8


def test_artifact_relationships_one_type_per_pair(world):
    art = world.artifact()
    instruments = set(entities(art, "measurements"))
    types = pair_types(art)
    assert all(len(ts) == 1 for ts in types.values()), types
    assert len(art["relationships"]) == len(types) == 6
    for r in art["relationships"]:
        if r["type"] == "measured_by":
            assert r["target"] in instruments and r["source"] not in instruments
        if r["type"] == "causes":
            assert r["source"] not in instruments and r["target"] not in instruments
        if r["type"] in ("related", "correlates"):
            assert r["source"] < r["target"]
        assert r["paper_count"] == len(r["papers"]) == sum(len(ps) for ps in r["papers_by_conference"].values())
        assert r["paper_weight"] == pytest.approx(sum(p["type_share"] for p in r["papers"]))
    assert {r["type"] for r in art["relationships"]} == {"measured_by", "related", "causes", "correlates"}


# ---------------------------------------------------------------- the site export

def test_site_export_matches_artifact(world):
    assert check_site_export(world.site, world.lay.artifact) == []
    data = world.data
    graph = read_json(data / "graph.bundle.json")
    assert {n["name"] for n in graph["nodes"]} == {"Reasoning", "Model safety", "GSM8K", "MMLU", "Refusal"}
    assert graph["node_count"] == 5 and graph["edge_count"] == 5        # the removed entity's edge is left out
    assert not any("Gradient Clipping" in (e["source"], e["target"]) for e in graph["edges"])
    assert not (data / "constructs" / "gradient_clipping.json").exists()
    assert not (world.site / "data/readable" / "constructs" / "gradient_clipping.md").exists()
    renamed = read_json(data / "constructs" / "model_safety.json")
    assert renamed["names"] == ["Safety"]                               # the old name stays as a surface name
    assert {(r["direction"], r["other_canonical_name"], r["relationship_type"]) for r in renamed["relationships"]} == {
        ("outgoing", "Reasoning", "related"), ("outgoing", "Refusal", "causes")}
    reasoning = read_json(data / "constructs" / "reasoning.json")
    assert sorted(reasoning["papers"]) == sorted([A1, A2, B1, B2]) and reasoning["conferences"] == [VENUE_A, VENUE_B]
    assert reasoning["paper_count"] == 4 and reasoning["paper_count_by_conference"] == {VENUE_A: 2, VENUE_B: 2}
    # the surface name's definition is attributed to every paper the node stores, venue by venue (the vote
    # trims the entity's paper list, not the node's, so B4 is still there)
    assert reasoning["definitions"][0] == {"text": "The ability to draw inferences.", "papers": [A1, A2, B1, B2, B4],
                                           "original_name": "Reasoning"}
    assert reasoning["characterization_status"] == "placeholder"
    urls = read_json(data / "paper_urls.json")
    assert urls == {A1: "https://a.example/1", A2: "https://a.example/2", A3: "https://a.example/3",
                    A4: "https://a.example/4", B0: "https://b.example/0", B1: "https://b.example/1",
                    B2: "https://b.example/2", B3: "https://b.example/3", B4: "https://b.example/4"}
    md = (world.site / "data/readable" / "constructs" / "reasoning.md").read_text(encoding="utf-8")
    # the header gives the entity's supporting papers (the record's paper_count); the relationship with the
    # removed Gradient Clipping (A3, A4) is not on the record, so neither it nor its papers reach the page
    assert md.startswith(f"# Reasoning\n**Type:** Construct  \n**Supporting papers:** {reasoning['paper_count']}  \n"
                         "**Also known as:** Reasoning ability  \n")
    assert reasoning["paper_count"] == 4
    assert f"[{A1}](https://a.example/1)" in md
    assert "Gradient Clipping" not in md and A3 not in md and A4 not in md
    assert all(r["other_canonical_name"] != "Gradient Clipping" for r in reasoning["relationships"])
    assert {(r["direction"], r["other_canonical_name"]) for r in reasoning["relationships"]} == {
        ("outgoing", "GSM8K"), ("incoming", "Model safety")}
    assert reasoning["relationship_count"] == 2
    assert "- **GSM8K** (measurement instrument): *measured_by*" in md
    # every paper of the relationship is listed, not only the first
    gsm8k = next(r for r in reasoning["relationships"] if r["other_canonical_name"] == "GSM8K")
    titles = [t for ps in gsm8k["papers_by_conference"].values() for t in ps]
    entry = md.split("- **GSM8K** (measurement instrument): ")[1].split("\n- ")[0].split("\n### ")[0]
    assert entry.startswith(f"*measured_by*, {len(titles)} paper{'s' if len(titles) != 1 else ''}\n")
    assert [line for line in entry.splitlines() if line.startswith("  - ")] == [
        f"  - [{t}]({urls[t]})" if t in urls else f"  - {t}" for t in titles]
    analysis = read_json(data / "analysis.bundle.json")
    assert analysis["meta"]["joint_of"] == [VENUE_A, VENUE_B]
    assert analysis["meta"]["n_nodes"] == 5 and analysis["meta"]["n_edges"] == 5 and analysis["meta"]["n_papers"] == 6
    layout = read_json(world.site / "data" / "layout.json")
    assert layout["params"]["seed"] == 3 and set(layout["nodes"]) == {n["name"] for n in graph["nodes"]}


# ---------------------------------------------------------------- resumed runs

def copy_world(world, tmp_path, **overrides):
    """A fresh root holding a copy of the run's work directory, with a config built on it."""
    root = tmp_path / "copy"
    shutil.copytree(world.root, root)
    raw = raw_config(**overrides)
    return root, config_from_dict(raw, base_dir=root)


def test_summaries_enabled_wires_the_summary_stage(tmp_path, world):
    root, cfg = copy_world(world, tmp_path, summaries_enabled=True)
    lay = Layout(cfg)
    fakes = Fakes()
    with pytest.MonkeyPatch.context() as mp:
        fakes.install(mp)
        written = pipeline.run(cfg, stages=["summarize", "export"])
    assert set(written) == {"summarize", "export"}
    assert fakes.calls["characterize"] == [{"input_json": lay.curated, "output_json": lay.summarized,
                                            "provider": "openai", "model": "gpt-summarizer", "reasoning_effort": "low",
                                            "min_papers": 3, "poll_interval": 1, "prompts": "default"}]
    assert fakes.calls["check_characterizations"] == [{"input_json": lay.curated, "output_json": lay.summarized,
                                                       "min_papers": 3, "retry": False, "model": "gpt-summarizer",
                                                       "reasoning_effort": "low"}]
    # the export took the summarized network: entities with >= 3 papers carry the summary
    rec = read_json(cfg.export.site_dir / "data" / "constructs" / "reasoning.json")
    assert rec["characterization"] == "Summary of Reasoning." and rec["characterization_status"] == "llm"
    small = read_json(cfg.export.site_dir / "data" / "constructs" / "model_safety.json")
    assert small["characterization_status"] == "placeholder"
    assert check_site_export(cfg.export.site_dir, lay.artifact) == []


def test_trials_dir_venue_without_a_panel(tmp_path, world):
    """A venue that brings existing trials skips extraction and votes with the labels found there."""
    root = tmp_path / "copy"
    shutil.copytree(world.root, root)
    raw = raw_config()
    raw["extraction"]["models"] = []
    raw["venues"][0]["trials_dir"] = f"work/venues/{VENUE_A}/extraction/trials"
    cfg = config_from_dict(raw, base_dir=root)
    lay = Layout(cfg)
    a = cfg.venue(VENUE_A)
    assert cfg.models_for(a) == [] and lay.trials_dir(a) == root / "work" / "venues" / VENUE_A / "extraction" / "trials"
    assert pipeline._venue_labels(cfg, lay, a) == LABELS
    assert pipeline._all_labels(cfg, lay) == LABELS
    fakes = Fakes()
    with pytest.MonkeyPatch.context() as mp:
        fakes.install(mp)
        written = pipeline.run(cfg, stages=["extract", "vote", "join"], venues=[VENUE_A])
    assert fakes.calls["run_extraction"] == []                        # existing trials: nothing extracted
    assert written[f"{VENUE_A}/extract"] == lay.extraction(a)
    multi = read_json(written[f"{VENUE_A}/vote"])
    assert set(entities(multi, "constructs")) == {"Reasoning", "Safety", "Gradient Clipping"}
    voted = read_json(written["join"])
    assert entities(voted, "constructs")["Reasoning"]["paper_count"] == 4
    # an extraction JSON beside trials from another work directory is found as well
    elsewhere = tmp_path / "elsewhere"
    shutil.copytree(root / "work" / "venues" / VENUE_A / "extraction", elsewhere)
    raw["venues"][0]["trials_dir"] = str(elsewhere / "trials")
    raw["paths"]["work_dir"] = "work_fresh"
    cfg2 = config_from_dict(raw, base_dir=root)
    assert Layout(cfg2).extraction(cfg2.venue(VENUE_A)) == elsewhere / "inputs" / "extraction.json"
    shutil.rmtree(elsewhere / "inputs")
    with pytest.raises(StageError, match="trials_dir"):
        pipeline.stage_extract(cfg2, Layout(cfg2), cfg2.venue(VENUE_A))


def test_export_without_a_joint_network_fails_clearly(tmp_path):
    write_inputs(tmp_path)
    cfg = config_from_dict(raw_config(), base_dir=tmp_path)
    with pytest.raises(StageError, match="join stage"):
        pipeline.run(cfg, stages=["export"])
    with pytest.raises(StageError, match="produced by the ingest"):
        pipeline.run(cfg, stages=["screen"], venues=[VENUE_B])


# ---------------------------------------------------------------- the command line

def write_yaml(path: Path, raw) -> Path:
    path.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    return path


def test_cli_check_config_and_plan(tmp_path, capsys):
    write_inputs(tmp_path)
    cfg_path = write_yaml(tmp_path / "lexis.yaml", raw_config())
    assert cli.main(["check-config", str(cfg_path)]) == 0
    out, err = capsys.readouterr()
    resolved = json.loads(out)
    assert resolved["version"] == "0.0.1"
    assert resolved["paths"]["work_dir"] == str(tmp_path / "work")       # relative to the config file
    assert resolved["venues"][0]["papers"] == str(tmp_path / "lists" / f"{VENUE_A}.json")
    assert resolved["venues"][1]["models"][2]["model"] == "qwen-other-test"
    assert resolved["curation"]["overlay"] == str(tmp_path / "overlay.jsonl")
    assert resolved["export"]["site_dir"] == str(tmp_path / "site")
    assert "OK: 2 venue(s), 3 extraction model label(s)" in err

    assert cli.main(["plan", "--config", str(cfg_path)]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 2 * len(pipeline.VENUE_STAGES) + len(pipeline.JOINT_STAGES)
    assert lines == pipeline.plan(load_config(cfg_path))
    assert cli.main(["plan", "--config", str(cfg_path), "--stages", "harmonize,export", "--venues", VENUE_A]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert [line.split()[1] for line in lines] == ["harmonize", "export"]
    assert lines[0].split()[0] == VENUE_A and lines[1].split()[0] == "joint"

    assert cli.main(["stages"]) == 0
    assert capsys.readouterr().out.split() == list(pipeline.STAGES)
    assert cli.main(["version"]) == 0
    assert capsys.readouterr().out.strip() == "0.0.1"

    bad = write_yaml(tmp_path / "bad.yaml", {**raw_config(), "colour": "blue"})
    assert cli.main(["check-config", str(bad)]) == 2
    assert "error: unknown top-level key(s) ['colour']" in capsys.readouterr().err
    assert cli.main(["plan", "--config", str(tmp_path / "missing.yaml")]) == 2
    assert "Config file not found" in capsys.readouterr().err
    assert cli.main(["plan", "--config", str(cfg_path), "--venues", "nowhere"]) == 2
    assert "Unknown venue 'nowhere'" in capsys.readouterr().err


def test_cli_run_dry_run_stops_before_the_joint_stages(tmp_path, world, capsys):
    root = tmp_path / "copy"
    shutil.copytree(world.root, root)
    cfg_path = write_yaml(root / "lexis.yaml", raw_config())
    shutil.rmtree(root / "work" / "joint")
    fakes = Fakes()
    with pytest.MonkeyPatch.context() as mp:
        fakes.install(mp)
        rc = cli.main(["--log-dir", str(root / "cli_logs"), "run", "--config", str(cfg_path),
                       "--stages", "extract,join", "--dry-run"])
    assert rc == 0
    assert [c["dry_run"] for c in fakes.calls["run_extraction"]] == [True, True]
    assert not (root / "work" / "joint").exists()                      # join did not run
    out = capsys.readouterr().out
    assert f"{VENUE_A}/extract" in out and f"{VENUE_B}/extract" in out and "join" not in out


# ---------------------------------------------------------------- configuration errors

def base_raw(tmp_path=None):
    raw = raw_config()
    raw["venues"][0].pop("papers")
    if tmp_path is not None:
        # the overlay must exist for the base config to validate
        (Path(tmp_path) / raw["curation"]["overlay"]).write_text("")
    return raw


@pytest.mark.parametrize("edit, message", [
    (lambda r: r.update(colour="blue"), "unknown top-level key"),
    (lambda r: r["voting"].update(thresold=2), "voting: unknown key"),
    (lambda r: r["venues"][0].update(track="main"), "venues\\[0\\]: unknown key"),
    (lambda r: r["venues"].append({"id": "icml25", "conference": "icml", "year": 2025, "source": "pmlr"}),
     "source 'pmlr' needs a volume"),
    (lambda r: r["venues"].append({"id": "acl25", "conference": "acl", "year": 2025, "source": "anthology"}),
     "source 'anthology' needs a volume"),
    (lambda r: r["voting"].update(threshold=4), "3 model\\(s\\) cannot reach voting.threshold=4"),
    (lambda r: r["extraction"].update(models=PANEL[:1]), "1 model\\(s\\) cannot reach voting.threshold=2"),
    (lambda r: r["extraction"].update(models=[]), "no extraction models configured"),
    (lambda r: r["extraction"]["models"].append(dict(PANEL[0])), "duplicate model label 'm1'"),
    (lambda r: r["extraction"]["models"].append({"provider": "mistral", "model": "x", "label": "m4"}),
     "provider must be one of"),
    (lambda r: r["extraction"]["models"].append({"provider": "openai", "model": "x", "label": "bad label"}),
     "must be alphanumeric/underscore"),
    (lambda r: r.update(venues=[]), "at least one venue is required"),
    (lambda r: r["venues"].append(dict(r["venues"][0])), "duplicate id"),
    (lambda r: r["venues"][0].update(source="arxiv"), "source must be one of"),
    (lambda r: r["venues"][0].update(id="venue a"), "must be alphanumeric/underscore"),
    (lambda r: r["screening"].update(mode="async"), "screening.mode must be"),
    (lambda r: r["screening"].update(mode="batch", provider="openai"), "Together batch API"),
    (lambda r: r["harmonization"].update(provider="mistral"), "harmonization.provider must be"),
    (lambda r: r["harmonization"].update(on_batch_failure="retry"), "on_batch_failure"),
    (lambda r: r["voting"].update(survivor="loudest"), "voting.survivor"),
    (lambda r: r["voting"].update(threshold=0), "voting.threshold must be at least 1"),
    (lambda r: r["voting"].update(min_papers=0), "voting.min_papers must be at least 1"),
    (lambda r: r["summaries"].update(enabled=True, provider="together"), "summaries.provider must be"),
    (lambda r: r["summaries"].update(min_papers=0), "summaries.min_papers"),
    (lambda r: r["export"].update(site_dir=None, artifact_out=None), "set site_dir and/or artifact_out"),
    (lambda r: r.update(paths="runs"), "paths: expected a mapping"),
    (lambda r: r["extraction"].update(models={"provider": "openai"}), "expected a list of models"),
])
def test_config_errors(edit, message, tmp_path):
    raw = base_raw(tmp_path)
    config_from_dict(raw, base_dir=tmp_path)                           # the base passes
    edit(raw)
    with pytest.raises(ConfigError, match=message):
        config_from_dict(raw, base_dir=tmp_path)


def test_config_defaults_and_derived_values(tmp_path):
    base = tmp_path.resolve()
    raw = base_raw(base)
    cfg = config_from_dict(raw, base_dir=base)
    assert cfg.pdf_dir == base / "pdfs" and cfg.joint_dir == base / "work" / "joint"
    assert cfg.venue_dir(VENUE_B) == base / "work" / "venues" / VENUE_B
    assert cfg.all_model_labels() == LABELS
    assert [m.model for m in cfg.models_for(cfg.venue(VENUE_B))] == ["gemini-test", "gpt-test", "qwen-other-test"]
    assert [m.model for m in cfg.models_for(cfg.venue(VENUE_A))] == ["gemini-test", "gpt-test", "qwen-test"]
    raw["paths"].pop("pdf_dir")
    raw["venues"][1]["volume"] = 267                                     # a bare number is accepted
    raw["venues"][1]["source"] = "pmlr"
    cfg = config_from_dict(raw, base_dir=base)
    assert cfg.pdf_dir == base / "work" / "pdfs"
    assert cfg.venue(VENUE_B).volume == 267 and int(cfg.venue(VENUE_B).volume) == 267
    with pytest.raises(ConfigError, match="Unknown venue"):
        cfg.venue("venue_c")


def test_load_config_resolves_relative_to_the_file(tmp_path):
    sub = tmp_path / "configs"
    sub.mkdir()
    raw = raw_config()
    raw["paths"]["work_dir"] = "../runs/work"
    write_inputs(tmp_path)
    raw["venues"][0]["papers"] = f"../lists/{VENUE_A}.json"
    raw["curation"]["overlay"] = "../overlay.jsonl"
    write_yaml(sub / "run.yaml", raw)
    cfg = load_config(sub / "run.yaml")
    assert cfg.source_file == (sub / "run.yaml").resolve()
    assert cfg.paths.work_dir == (tmp_path / "runs" / "work").resolve()
    assert cfg.venue(VENUE_A).papers == (tmp_path / "lists" / f"{VENUE_A}.json").resolve()
    assert cfg.curation.overlay == (tmp_path / "overlay.jsonl").resolve()
    assert cfg.export.site_dir == (sub / "site").resolve()
    with pytest.raises(ConfigError, match="top level must be a mapping"):
        (sub / "list.yaml").write_text("- a\n- b\n", encoding="utf-8")
        load_config(sub / "list.yaml")


# ---------------------------------------------------------------- ingest of a paper list

def fake_fetch(fail=()):
    calls = []

    def fetch(url, path):
        calls.append((url, Path(path)))
        if url in fail:
            return "HTTP 404"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_bytes(b"%PDF-1.4\n" + b"0" * 2000)
        return None
    return fetch, calls


def test_download_listed_fetches_only_screened_in_papers(tmp_path):
    src = tmp_path / "list.json"
    src.write_text(json.dumps([
        {"title": A1, "url": "https://a.example/1", "is_LLM_paper": True},
        {"name": A2, "pdf_url": "https://a.example/2", "is_LLM_paper": True, "paper_id": "a.2"},
        {"title": A3, "url": "https://a.example/3", "is_LLM_paper": False},
        {"title": A4, "url": "https://a.example/4", "is_LLM_paper": True, "path": "/old/location.pdf"},
        {"title": "", "url": "https://a.example/5", "is_LLM_paper": True},   # no title: not a usable record
        "not a record",
    ]), encoding="utf-8")
    fetch, calls = fake_fetch(fail={"https://a.example/4"})
    out = download_listed(src, tmp_path / "work" / "papers.json", tmp_path / "pdfs", fetch=fetch)
    assert out == tmp_path / "work" / "papers.json"
    assert sorted(u for u, _ in calls) == ["https://a.example/1", "https://a.example/2", "https://a.example/4"]
    papers = json.loads(out.read_text(encoding="utf-8"))
    assert [p["name"] for p in papers] == [A1, A2, A3, A4]
    assert all(set(p) >= {"name", "url", "is_LLM_paper"} for p in papers)
    assert papers[0]["path"] == str(tmp_path / "pdfs" / f"{pdf_stem(A1)}.pdf") and Path(papers[0]["path"]).is_file()
    assert papers[1]["url"] == "https://a.example/2" and papers[1]["path"] == str(tmp_path / "pdfs" / "a.2.pdf")
    assert "path" not in papers[2] and papers[2]["is_LLM_paper"] is False
    assert "path" not in papers[3] and papers[3]["download_error"] == "HTTP 404"
    assert "title" not in papers[0] and "pdf_url" not in papers[1]
    # the list is rewritten on a second run; PDFs already fetched are offered to fetch again
    fetch2, calls2 = fake_fetch()
    download_listed(src, out, tmp_path / "pdfs", fetch=fetch2)
    assert len(calls2) == 3
    # only_flagged=False fetches every record; a list without decisions is fetched entirely
    fetch3, calls3 = fake_fetch()
    download_listed(src, tmp_path / "all.json", tmp_path / "pdfs_all", only_flagged=False, fetch=fetch3)
    assert len(calls3) == 4
    unscreened = tmp_path / "unscreened.json"
    unscreened.write_text(json.dumps({"x": {"title": B1, "url": "https://b.example/1"},
                                      "y": {"title": B2, "url": "https://b.example/2"}}), encoding="utf-8")
    fetch4, calls4 = fake_fetch()
    out4 = download_listed(unscreened, tmp_path / "u" / "papers.json", fetch=fetch4)
    assert len(calls4) == 2
    assert all(p["path"].startswith(str(tmp_path / "u" / "papers")) for p in json.loads(out4.read_text()))
    empty = tmp_path / "empty.json"
    empty.write_text("[]", encoding="utf-8")
    with pytest.raises(RuntimeError, match="no usable paper records"):
        download_listed(empty, tmp_path / "e.json", fetch=fetch4)


# ---------------------------------------------------------------- paper URL matching

def test_title_key_and_match_paper_urls():
    assert title_key("A Study of  Spacing") == title_key("A Study of Spacing") == "astudyofspacing"
    assert title_key(r"\textit{Emph} Title") == title_key("Emph Title")
    assert title_key('Quotes "Here"') == title_key("Quotes \u201cHere\u201d") == title_key("Quotes Here")
    assert title_key("Long\u2013dash") == title_key("Long-dash") == title_key("Long dash")
    assert title_key("\ufb01ne-tuning") == title_key("fine-tuning")          # ligature
    assert title_key("\uff21bc") == title_key("Abc")                         # full-width letter
    assert title_key("Caf\u00e9 R\u00e9sum\u00e9") == title_key("Cafe Resume")   # accents
    assert title_key(r"\emph{Top}-$n$: Eliminating") == title_key("Top-n: Eliminating")
    assert title_key("") == ""

    url_by_title = {
        "A Study of  Spacing": "https://x/1",
        r"\textit{Emph} Title: Why": "https://x/2",
        "Quotes \u201cHere\u201d": "https://x/3",
        "Caf\u00e9 R\u00e9sum\u00e9 Models": "https://x/4",
        "Same Key": "https://x/5a",
        "Same  Key": "https://x/5b",
        "Twin Title": "https://x/6",
        "Twin  Title": "https://x/6",
    }
    titles = ["A Study of Spacing", "Emph Title: Why", 'Quotes "Here"', "Cafe Resume Models",
              "Same key", "Twin title", "Unknown Paper", "", "A Study of  Spacing"]
    out = match_paper_urls(url_by_title, titles)
    assert {k: v for k, v in out.items() if k not in url_by_title} == {
        "A Study of Spacing": "https://x/1",
        "Emph Title: Why": "https://x/2",
        'Quotes "Here"': "https://x/3",
        "Cafe Resume Models": "https://x/4",
        "Twin title": "https://x/6",          # two list titles, one URL: not ambiguous
    }
    assert "Same key" not in out and "Unknown Paper" not in out and "" not in out
    assert all(out[k] == v for k, v in url_by_title.items())           # the input entries are kept
    assert match_paper_urls({}, titles) == {}
