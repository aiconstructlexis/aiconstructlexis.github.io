"""Tests for the summary checks: each hard problem and soft flag, the written checks file,
and the retry path with a fake client."""
import importlib
import json
import types

from aiconstructlexis.prompts import load_prompts
S = importlib.import_module("aiconstructlexis.summarize.characterize")   # aiconstructlexis.summarize.characterize resolves to the re-exported function, so the module is loaded by name
K = importlib.import_module("aiconstructlexis.summarize.checks")

P = load_prompts("default")
LABELS = dict(P.CHARACTERIZE_SECTION_LABELS["constructs"])


def entity(name, n_papers, sections=None):
    e = {"canonical_name": name,
         "original_nodes": {name: {"definition": "The ability to reason over important inputs.",
                                   "papers": [["iclr24", f"{name} paper {i}"] for i in range(n_papers)]}},
         "source_snippets_evidence": [{"original_name": name, "paper": f"{name} paper {i}", "source_snippets": ["q"]}
                                      for i in range(n_papers)],
         "papers": [{"conference": "iclr24", "paper": f"{name} paper {i}"} for i in range(n_papers)],
         "paper_count": n_papers}
    if sections is not None:
        e["characterization_sections"] = sections
        e["characterization"] = "\n\n".join(f"{LABELS[k]} {v}" for k, v in sections.items() if v)
    return e


def network(sections=None):
    return {"constructs": [entity("Reasoning", 4, sections), entity("Thin", 1)],
            "measurements": [], "behaviors": [],
            "relationships": [{"source": "Reasoning", "type": "measured_by", "target": "GSM8K", "evidence": ["ev"],
                               "papers": [{"conference": "iclr24", "paper": "Reasoning paper 0"}]}]}


def ctx_for(net):
    index = {e["canonical_name"]: (et, e) for et in K.TYPES for e in net[et]}
    return S.build_entity_context(net["constructs"][0], "constructs", net["relationships"], index)


def good():
    return {"definition": "Most papers treat it as an ability to reason over important inputs.",
            "systematization": "A few papers split it into facets.", "measurement": "", "links": "It is linked to GSM8K."}


def test_clean_summary_has_no_hard_problems_and_reports_empty_sections():
    net = network(good())
    hard, soft = K.check("constructs", net["constructs"][0], ctx_for(net))
    assert hard == [] and soft == ["empty sections: measurement"]


def test_each_hard_problem_is_detected():
    bad = dict(good(), definition="A crucial ability \u2014 studied in 14 papers \u2013 with 93 instruments; the stats show "
                                  "Reasoning paper 0, Reasoning paper 1 and Reasoning paper 2.")
    net = network(bad)
    hard, soft = K.check("constructs", net["constructs"][0], ctx_for(net))
    kinds = [h.split(":")[0] for h in hard]
    assert kinds == ["em dash", "spaced en dash", "banned words", "counts in digits", "meta wording",
                     "numbers not in input", "3 paper titles", "link counts that differ from the input"]
    assert "banned words: crucial" in hard and "numbers not in input: 14, 93" in hard


def test_banned_word_in_a_source_phrase_and_derived_counts_are_not_hard():
    net = network(dict(good(), definition="Papers describe reasoning over important inputs; GSM8K and 15 other instruments."))
    # Twenty linked instruments (names without digits): "15 other" is a count derived from the input.
    for letter in "ABCDEFGHIJKLMNOPQRS":
        net["measurements"].append({"canonical_name": f"Bench {letter}", "paper_count": 1})
        net["relationships"].append({"source": "Reasoning", "type": "measured_by", "target": f"Bench {letter}",
                                     "papers": [{"conference": "iclr24", "paper": "Reasoning paper 0"}]})
    hard, soft = K.check("constructs", net["constructs"][0], ctx_for(net))
    assert hard == [] and "derived counts: 15" in soft


def test_missing_sections_and_soft_flags():
    net = network({"definition": "", "systematization": "", "measurement": "", "links": ""})
    hard, soft = K.check("constructs", net["constructs"][0], ctx_for(net))
    assert hard == ["no sections (request failed or did not parse)"] and soft == []
    net = network(dict(good(), links="This suggests reasoning improves GSM8K scores across two papers."))
    hard, soft = K.check("constructs", net["constructs"][0], ctx_for(net))
    assert hard == []
    assert "interpretive words: suggests" in soft and "causal verbs: improves" in soft and "counts in words: two papers" in soft


def test_check_characterizations_writes_the_checks_file(tmp_path):
    src, out = tmp_path / "in.json", tmp_path / "characterized.json"
    src.write_text(json.dumps(network()))
    out.write_text(json.dumps(network(dict(good(), definition="Studied in 14 papers."))))
    (tmp_path / "characterized.batch_results.jsonl").write_text(json.dumps({"response": {"body": {
        "model": "gpt-5.4", "status": "completed", "reasoning": {"effort": "high"},
        "usage": {"input_tokens": 1000, "output_tokens": 100, "output_tokens_details": {"reasoning_tokens": 40}}}}}) + "\n")
    summary = K.check_characterizations(src, out, min_papers=3)
    assert summary["entities_checked"] == 1 and summary["with_hard_problems"] == 1
    assert summary["hard_problem_kinds"] == {"counts in digits": 1, "numbers not in input": 1}
    assert summary["batch_usage"] == {"input": 1000, "output": 100, "reasoning": 40, "requests": 1}
    assert summary["batch_echo"] == {"gpt-5.4 | effort high | completed": 1}
    checks = json.loads((tmp_path / "characterized.checks.json").read_text())
    assert checks["entities"][0]["name"] == "Reasoning" and checks["summary"]["retries"]["attempted"] == 0


class FakeResponses:
    """client.responses.create returning one scripted answer; records the calls."""

    def __init__(self, answer):
        self.answer = answer
        self.calls = []
        self.responses = types.SimpleNamespace(create=self._create)

    def _create(self, **kw):
        self.calls.append(kw)
        return types.SimpleNamespace(output_text=json.dumps(self.answer), model=kw["model"],
                                     usage=types.SimpleNamespace(input_tokens=10, output_tokens=5))


def test_retry_replaces_a_failing_summary_when_the_retry_is_cleaner(tmp_path):
    src, out = tmp_path / "in.json", tmp_path / "characterized.json"
    src.write_text(json.dumps(network()))
    out.write_text(json.dumps(network(dict(good(), definition="A crucial ability \u2014 in 14 papers."))))
    client = FakeResponses(good())
    summary = K.check_characterizations(src, out, min_papers=3, retry=True, model="gpt-5.4", client=client)
    assert len(client.calls) == 1 and client.calls[0]["reasoning"] == {"effort": "high"}
    assert client.calls[0]["input"][0]["content"] == S.SYSTEM_PROMPT and "Reasoning" in client.calls[0]["input"][1]["content"]
    assert summary["retries"] == {"attempted": 1, "kept": 1, "still_failing": 0, "errors": 0,
                                  "input_tokens": 10, "output_tokens": 5}
    rewritten = json.loads(out.read_text())
    assert rewritten["constructs"][0]["characterization_sections"]["definition"] == good()["definition"]
    checks = json.loads((tmp_path / "characterized.checks.json").read_text())
    assert checks["entities"][0]["retried"] == "kept" and checks["entities"][0]["hard"] == []
    # A later check without retries keeps the record of the retry pass.
    again = K.check_characterizations(src, out, min_papers=3)
    assert again["retries"]["attempted"] == 1


def test_small_counts_up_to_the_stats_list_length_are_not_unknown_numbers():
    def unknown(definition):
        net = network(dict(good(), definition=definition))
        hard, _ = K.check("constructs", net["constructs"][0], ctx_for(net))
        return [h for h in hard if h.startswith("numbers not in input")]
    assert unknown(f"Studies name {S.STATS_TOP_N} facets and 0 or 1 alternative.") == []
    assert unknown(f"Studies name {S.STATS_TOP_N + 1} facets.") == [f"numbers not in input: {S.STATS_TOP_N + 1}"]


def test_normalize_wording_rewrites_references_to_the_input_and_keeps_domain_uses():
    n = K.normalize_wording
    assert n("Across the provided sources, X is defined as Y.") == "Across the papers, X is defined as Y."
    assert n("Based on the provided data, X is a metric.") == "In the papers, X is a metric."
    assert n("The provided data also indicates that X is used.") == "The papers also indicate that X is used."
    assert n("The provided literature offers two framings.") == "The literature offers two framings."
    assert n("a causal link supported by multiple papers in this set.") == "a causal link supported by multiple papers."
    assert n("Definitions and snippets describe it; one snippet says so.") == \
        "Definitions and quoted passages describe it; one quoted passage says so."
    assert n("Source snippets place it among the datasets.") == "Quoted passages place it among the datasets."
    assert n("and many snippets tie it to traceability") == "and many quoted passages tie it to traceability"
    assert n("answers grounded in the provided context") == "answers grounded in the provided context"
    assert n("a missing span inside the code snippet") == "a missing span inside the code snippet"
    assert n("in-context learning. In the snippets it appears alongside X.") == \
        "in-context learning. In the quoted passages it appears alongside X."
    assert n("receiving a snippet of conversation") == "receiving a snippet of conversation"
    assert n("a missing span inside the snippet", name="Code completion") == "a missing span inside the snippet"
    assert n("") == ""


def test_normalize_wording_rules_for_snippets_relationships_and_double_reports():
    n = K.normalize_wording
    cases = {
        # the available snippet(s)
        "The available snippet positions WebQA as one dataset.": "The quoted passage positions WebQA as one dataset.",
        "The available snippets agree.": "The quoted passages agree.",
        "as the available snippet says": "as the quoted passage says",
        "In the available usage snippet, it is a test.": "In the one quoted passage, it is a test.",
        "the available usage snippet says": "the quoted passage says",
        # relationship, usage and source snippets
        "and one relationship snippet describes LogiQA2 as a revision": "and one quoted passage describes LogiQA2 as a revision",
        "One usage snippet also places it in generation.": "One quoted passage also places it in generation.",
        "Usage snippets place it among datasets.": "Quoted passages place it among datasets.",
        "a source snippet names it": "a quoted passage names it",
        "Source snippets place it among the datasets.": "Quoted passages place it among the datasets.",
        "Relationship snippets tie it to GSM8K.": "Quoted passages tie it to GSM8K.",
        # sentence-initial Snippets / The snippets, and the snippets after a verb or preposition
        "Snippets describe it as used for both tasks.": "Quoted passages describe it as used for both tasks.",
        "It is a benchmark. Snippets place it in zero-shot work.": "It is a benchmark. Quoted passages place it in zero-shot work.",
        "The snippets describe IMDb as a corpus.": "The quoted passages describe IMDb as a corpus.",
        "as described in the snippets.": "as described in the quoted passages.",
        "Several papers cite the snippets above.": "Several papers cite the quoted passages above.",
        # relationships, papers represented here, provided materials
        "In the available relationships, papers use it to measure one construct.":
            "In the recorded relationships, papers use it to measure one construct.",
        "The available relationships do not link SUPERB directly.": "The recorded relationships do not link SUPERB directly.",
        "No papers in the provided relationships claim a causal link.":
            "No papers in the recorded relationships claim a causal link.",
        "The provided relationships are few.": "The recorded relationships are few.",
        "on or explicit disagreement appears in the papers represented here.":
            "on or explicit disagreement appears in the papers.",
        "The papers represented here therefore define it narrowly.": "The papers therefore define it narrowly.",
        "a case-linked legal outcome drawn from the provided materials.": "a case-linked legal outcome drawn from the papers.",
        "The provided materials discuss it.": "The papers discuss it.",
        # reports that X is reported to correlate with
        "One paper reports that aleatoric uncertainty is reported to correlate with hallucination.":
            "One paper reports that aleatoric uncertainty correlates with hallucination.",
        "one paper reports that Flexibility is reported to correlate with Originality.":
            "one paper reports that Flexibility correlates with Originality.",
        "It reports that LogiQA 2.0 is reported to correlate with ReClor.": "It reports that LogiQA 2.0 correlates with ReClor.",
        "Reports that the base model on long inputs is reported to correlate with recall.":
            "Reports that the base model on long inputs correlates with recall.",
    }
    for before, after in cases.items():
        assert n(before) == after, before
        assert n(after) == after, after          # idempotent
    # X is one to six words; a longer subject, or no "reports that", is left as it is
    long = "It reports that a b c d e f g is reported to correlate with recall."
    assert n(long) == long
    plain = "Coding ability is also reported to correlate with knowledge."
    assert n(plain) == plain
    # a snippet is left alone only when its own word says what kind it is, or inside quotation marks
    assert n("Retrieval of code. Snippets of code are ranked.") == "Retrieval of code. Snippets of code are ranked."
    assert n("It ranks code snippets by relevance.") == "It ranks code snippets by relevance."
    assert n("the model sees text classification; the snippets describe IMDb") == \
        "the model sees text classification; the quoted passages describe IMDb"
    assert n("It retrieves code. Snippets are ranked by relevance.") == \
        "It retrieves code. Quoted passages are ranked by relevance."
    assert n("books and the snippets that follow") == "books and the quoted passages that follow"
    assert n("Across snippets, and another snippet, supporting snippets agree.") == \
        "Across quoted passages, and another quoted passage, supporting quoted passages agree."
    assert n('One paper says "we pass text snippets to the model" here.') == 'One paper says "we pass text snippets to the model" here.'
    assert n('One paper says "the snippets are short" here.') == 'One paper says "the snippets are short" here.'
    assert n("a snippet-level score") == "a snippet-level score"
    assert n("Snippets are partial programs.", name="Code completion") == "Snippets are partial programs."
    assert n("the snippets are edited", name="Code editing") == "the snippets are edited"
    assert n("the available papers and The available descriptions and the available usage") == \
        "the papers and The descriptions and the usage in the papers"
    assert n("The available paper frames it. In the available work, the available operationalizations differ.") == \
        "The paper frames it. In the papers, the operationalizations differ."
    kept_available = "because the available options are wrong and the available context or the available training data"
    assert n(kept_available) == kept_available
    assert n("given a suffix the snippets end with") == "given a suffix the quoted passages end with"
    assert n("adversarial suffix snippets") == "adversarial suffix snippets"
    assert n("a book; the snippets are excerpts") == "a book; the quoted passages are excerpts"
    assert n("book snippets") == "book snippets"
    # the compound rules are not exempt: "usage snippet" never means code
    assert n("Usage snippets show code.", name="Code generation") == "Quoted passages show code."


def test_normalize_entity_recomposes_the_summary_and_is_idempotent():
    e = entity("Reasoning", 4, {"definition": "Across the provided literature, it is X.",
                                "links": "Definitions and snippets agree."})
    assert K.normalize_entity("constructs", e, P)
    assert e["characterization_sections"] == {"definition": "Across the papers, it is X.",
                                              "links": "Definitions and quoted passages agree."}
    assert e["characterization"] == f"{LABELS['definition']} Across the papers, it is X.\n\n" \
                                    f"{LABELS['links']} Definitions and quoted passages agree."
    assert not K.normalize_entity("constructs", e, P)
    assert not K.normalize_entity("constructs", entity("Thin", 1), P)


def test_check_characterizations_rewords_summaries_in_place(tmp_path):
    sections = dict(good(), definition="Across the provided sources, most papers treat it as an ability.")
    src, out = tmp_path / "in.json", tmp_path / "out.json"
    src.write_text(json.dumps(network()), encoding="utf-8")
    out.write_text(json.dumps(network(sections)), encoding="utf-8")
    summary = K.check_characterizations(input_json=src, output_json=out)
    assert summary["reworded"] == 1 and summary["with_hard_problems"] == 0
    rewritten = json.loads(out.read_text(encoding="utf-8"))["constructs"][0]
    assert rewritten["characterization_sections"]["definition"].startswith("Across the papers, most papers")
    assert "provided" not in rewritten["characterization"]


def network_with_gsm8k():
    net = network()
    net["measurements"].append(entity("GSM8K", 2))
    return net


def test_link_count_that_differs_from_the_input_is_a_hard_problem():
    ctx = ctx_for(network_with_gsm8k())
    assert ctx["stats"]["linked_instruments_count"] == 1
    off = entity("Reasoning", 4, dict(good(), measurement="It is linked to 3 measurement instruments."))
    hard, _ = K.check("constructs", off, ctx, P)
    assert any(h.startswith("link counts that differ from the input") for h in hard)
    right = entity("Reasoning", 4, dict(good(), measurement="It is linked to 1 measurement instrument."))
    hard, _ = K.check("constructs", right, ctx, P)
    assert not any(h.startswith("link counts") for h in hard)
    others = entity("Reasoning", 4, dict(good(), measurement="It is linked to GSM8K and 3 other instruments."))
    hard, _ = K.check("constructs", others, ctx, P)
    assert not any(h.startswith("link counts") for h in hard)


def test_link_section_naming_an_entity_absent_from_the_input_is_flagged():
    ctx = ctx_for(network_with_gsm8k())
    names = ["Zorblax planning", "GSM8K", "Reasoning"]
    stale = entity("Reasoning", 4, dict(good(), links="Papers relate it to Zorblax planning and GSM8K."))
    hard, soft = K.check("constructs", stale, ctx, P, entity_names=names)
    assert "entities not in the input: Zorblax planning" in soft and not hard
    _, soft = K.check("constructs", entity("Reasoning", 4, good()), ctx, P, entity_names=names)
    assert not any(f.startswith("entities not in the input") for f in soft)
    elsewhere = entity("Reasoning", 4, dict(good(), definition="Most papers contrast it with Zorblax planning."))
    _, soft = K.check("constructs", elsewhere, ctx, P, entity_names=names)
    assert not any(f.startswith("entities not in the input") for f in soft)


def test_zero_link_count_in_digits_is_a_hard_problem():
    ctx = ctx_for(network())
    zero = entity("Reasoning", 4, dict(good(), measurement="It is linked to 0 measurement instruments."))
    hard, _ = K.check("constructs", zero, ctx, P)
    assert "zero link counts in digits: 0 measurement instruments" in hard
    words = entity("Reasoning", 4, dict(good(), measurement="No measurement instrument is linked to it."))
    hard, _ = K.check("constructs", words, ctx, P)
    assert not any(h.startswith("zero link counts") for h in hard)
