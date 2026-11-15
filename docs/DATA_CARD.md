# Data card: AI Construct Lexis

**Release.** v0.0.1 (November 2026), accompanying *AI Construct Lexis: A Network of Constructs and
Measurement Instruments Used in AI Evaluation* (NeurIPS 2026, Evaluations and Datasets
track).

**Artifact.** `lexis/ai_construct_lexis_v0.0.1.json` (schema in `lexis/README.md`).

**Licence.** CC BY 4.0.

## Summary

The Lexis is a nomological network over three kinds of entities used to evaluate language
models: *constructs* (properties such as reasoning, robustness, safety), *behavioral
indicators* (observable tasks and output patterns such as code generation or hallucination)
and *measurement instruments* (benchmarks, datasets, human studies, protocols such as MMLU,
GSM8K or human evaluation), together with the relationships among them as published papers
assert them. Each entity carries its canonical name, the surface variants seen in the
papers, its supporting papers by venue, verbatim source snippets and a synthesized summary
of how the literature defines, operationalizes and uses it. Each relationship carries its
type, its supporting papers and the quotes that assert it.

## Source venues

| Venue | Year | In the corpus / screened |
| --- | --- | ---: |
| ICLR | 2024 | 513 / 2,260 |
| NeurIPS | 2024 | 731 / 4,494 |
| ICLR | 2025 | 1,365 / 3,703 |
| NAACL | 2025 | 551 / 637 |
| ACL | 2025 | 1,417 / 1,602 |
| ICML | 2025 | 992 / 3,330 |
| EMNLP | 2025 | 1,604 / 1,809 |
| Total | | 7,173 / 17,835 |

Main-conference proceedings only (no workshop, Findings, demo or industry-track papers; for
ACL and NAACL the long-paper volume; for NeurIPS 2024 the main track and the Datasets and
Benchmarks track, not the Creative AI track). LLM-relatedness was decided by an LLM screening pass
over each paper's text; the screened lists with every decision are in `lexis/paper_lists/`
(7,175 entries screened as LLM-related, of which two could not be matched to their PDFs and
are not in the corpus; two ACL 2025 entries carry no screening decision).

## Composition

| | In the release | Out of scope (kept, flagged) | Total extracted |
| --- | ---: | ---: | ---: |
| Constructs | 919 | 72 | 991 |
| Behavioral indicators | 899 | 51 | 950 |
| Measurement instruments | 1,356 | 248 | 1,604 |

Of the in-scope entities, 686 constructs, 683 behavioral indicators and 1,177 measurement
instruments have at least two supporting papers and are shown in the interface by default
(`site/config/view_network.json`); single-paper entities are in the artifact and not shown by default.

6,054 relationships of four types: `measured_by` (3,798), `related` (1,387), `causes` (795)
and `correlates` (74); 5,479 of them link in-scope entities (`measured_by` 3,475, `related`
1,265, `causes` 674, `correlates` 65), the rest touch an entity marked out of scope and are
kept but not shown. Papers are in English; the time span is ICLR 2024 through EMNLP 2025.

An entity's supporting papers are those for which at least two of the three extraction
models proposed one of its surface names (`docs/MODEL_CARD.md` notes where one model's runs
are incomplete). Relationships are kept per paper when at least two
models linked the same pair of entities; each pair of entities carries one type, the
strictest any paper's vote produced. Entities marked `expert_removed` were extracted by the
pipeline and judged out of scope by expert review (methods, metrics, properties of data or of
attacks rather than of a model); they are kept for transparency and are not shown in the
interface.

## Intended uses

- Compare how constructs are operationalized across instruments and venues, and how that
  changes over time.
- Find jingle and jangle cases: one instrument claimed for many constructs, one construct
  measured by heterogeneous instruments.
- Formulate falsifiable hypotheses about what instruments measure, and test them with
  measurement models on model-performance data (see `analysis/`).
- Locate under-validated constructs, redundant instruments and orphaned evaluation methods.

## Out-of-scope uses

- The Lexis describes the literature; it is not a normative reference for what a construct
  means or which instrument is valid for it.
- Paper counts measure how often the literature mentions or uses something, not quality.
- It does not replace reading the source papers when making a specific scholarly claim.

## Known limitations

- **Venue coverage.** Seven core machine learning and NLP conferences; other venues
  (including journals), informal and industry evaluations, and work not codified in papers
  are not covered.
- **Benchmark-centric literature.** User studies, audits and deployment-based assessments
  are under-represented, reflecting the surveyed venues.
- **Extraction and harmonization noise.** Entities and relationships are extracted by
  language models and merged by a language model; the vote and the expert review reduce but
  do not remove errors. Treat a canonical name as a grouping hypothesis and inspect
  `original_names` and the quotes before relying on a specific claim. The paper's Section
  3.1 and appendix report expert validation of extraction, harmonization, relationships and
  summaries.
- **Main text only.** Screening and extraction read each paper up to the venue's main-body
  page limit plus a small buffer; appendices and references are not read, so instruments or
  claims that appear only there are missed.
- **Per-venue floor.** Within each venue, entities supported by fewer than two papers are
  dropped before venues are joined, which removes single-mention noise but also loses a term
  used once in each of several venues. Single-paper entities in the artifact arise later,
  when the joint vote and the expert curation leave one credited paper.
- **Prompt vocabulary.** The extraction prompt resolves ambiguity between construct and
  behavioral indicator toward construct, names example entities of each type, and prescribes
  labels such as "User preference study" for unnamed human evaluations; those examples and
  labels may be more frequent in the Lexis for that reason (print the prompts with
  `lexis prompts`).
- **Summaries are synthesized.** Each `characterization` is a language-model summary of the
  entity's recorded definitions, quotes and relationships; it describes usage in the
  literature and is not a peer-reviewed definition. The prompt asks for frequency-based
  framing and forbids evaluative words and causal verbs the evidence does not use, so
  summaries read more hedged than the source papers. Summaries were checked against the
  released network and regenerated where they no longer matched it; one was corrected by
  hand for a misread test-set name.
- **Conservative recall.** The vote drops mentions that only one model proposed; absence
  from the Lexis is not evidence that a term is unused.
- **Interface defaults.** The explorer lists entities with at least the configured minimum
  number of supporting papers (`site/config/view_network.json`, two); the interactive network
  draws relationships reported in at least two papers (single-paper relationships stay on the
  entity pages); the analysis tools leave out six generic evaluation procedures, such as human
  evaluation and LLM-as-a-judge, by default (`site/config/tools.json`, restored by a toggle).
  The artifact holds all of them.

## Maintenance

New venues are added by running the pipeline with the previous release's artifact as the
harmonization seed, so that canonical names stay stable (`pipeline/README.md`). `CHANGELOG.md` records added, removed,
renamed and re-typed entities between releases; `CONTRIBUTING.md` describes how to report
errors and propose additions.

## Citation

Olawale Salaudeen, Florian E. Dorner, Tom Sühr, Sang Truong, Haoran Zhang, Patrick G.
Bissett, James Fox, Marzyeh Ghassemi, Tom Hartvigsen, Peter Hase, Augustin Kelava, Suhas
Mahesh, Margaret Mitchell, Jamelle Watson-Daniels, Sanmi Koyejo, and Angelina Wang (2026).
AI Construct Lexis: A Network of Constructs and Measurement Instruments Used in AI Evaluation.
*Advances in Neural Information Processing Systems (NeurIPS), Evaluations and Datasets
Track*. To appear.
