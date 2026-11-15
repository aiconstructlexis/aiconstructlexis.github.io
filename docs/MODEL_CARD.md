# Model card: the Lexis extraction pipeline

**Release.** v0.0.1 (November 2026).

**System.** A chain of language-model calls and deterministic steps that turns conference
proceedings into the Lexis: screening, two-pass extraction with three models, harmonization,
majority votes, a cross-venue merge, expert curation, summaries and export. Code and
configuration: `pipeline/` (`pipeline/configs/lexis_v0.0.1.yaml`). Prompts:
`pipeline/aiconstructlexis/prompts/` (print them with `lexis prompts`).

## Stages and models

| Stage | Model(s) | What it does |
| --- | --- | --- |
| Screening (`screen`) | gpt-oss-120b (Together) | one yes/no relevance decision per paper, from its main text |
| Extraction (`extract`) | Gemini 2.5 Pro, GPT-5.4 mini, and Qwen3.5-397B-A17B (NeurIPS 2024, ICLR 2025) or Qwen3-235B-A22B-Instruct-2507 (the other venues) | two passes per paper, entities and then the relationships among them; temperature 0; main text only (the venue's main-body page limit plus a small buffer, cut at the references) |
| Harmonization (`harmonize`) | Gemini 2.5 Pro | groups surface names into canonical entities per venue and type; deterministic passes split groups that mix a generic term with its qualified variants and merge names that differ only in spelling, case, plural or filler words; every surface name is kept in `original_names` |
| Entity vote (`vote`) | none | a paper supports an entity when at least two models proposed one of its surface names for it; within a venue an entity needs at least two papers |
| Join (`join`) | Gemini 2.5 Pro | union across venues, an LLM merge of duplicates, and the joint vote |
| Relationship vote (`join`, again in `curate`) | none | a pair of entities counts for a paper when at least two models link it; the paper's type is the strictest any of them gave (causes > measured_by > correlates > related), since a model that read the passage can name the stronger claim; across papers each pair keeps one type, again the strictest |
| Curation (`curate`) | none | expert review applied as operations: on entities, moving surface names, merging, splitting, renaming, re-typing and marking out of scope; on relationships, retracting claims the quoted passage does not support, re-typing, and moving a claim to the entity its quote names; then a type guard (`measured_by` points at an instrument, `causes` never touches one) |
| Summaries (`summarize`) | GPT-5.4, reasoning effort high | a sectioned summary per entity with at least three papers, written from the entity's definitions, quotes, relationships and link counts; a check pass re-requests summaries that break the prompt's rules or no longer match the released network; entities below three papers carry their first recorded definition |
| Export (`export`) | none | the release artifact, the per-entity site records and the site's graph and analysis files |

## Notes on the release run

- **Panel coverage.** Two provider batches were never collected: GPT-5.4 mini on ACL 2025,
  and the Qwen relationship pass on EMNLP 2025 (that pass is also incomplete on ICLR 2024 and
  ACL 2025). Where only two models ran on a paper, a credit needs both.
- **Prompt revision.** The extraction prompts were revised once during the run. NeurIPS 2024,
  ICLR 2025 and part of NAACL 2025 and ICLR 2024 were extracted with the earlier revision
  (`prompts/earlier.py`), the rest with `prompts/default.py`. The other prompts did not change.
- **Harmonization batches.** Some harmonization batches failed during the run. Their names
  were grouped again and their paper credits restored before release.
- **Curation.** 4,685 entity operations and 3,275 relationship operations were applied. With
  the type guard and the one-type-per-pair rule they took the network from 7,319 to 6,054
  relationships.

## Quality control

The paper (Section 3.1 and the validation appendix) reports expert validation of the
canonical entities, the relationships, the harmonization (merge) decisions and the
synthesized summaries with the fidelity of their cited evidence, plus a paper-level
validation of extracted entities and relationships against their source papers. Agreement
is highest for measurement instruments and `measured_by` relationships. Among entities,
strict agreement is lowest for constructs (every construct was judged at least defensible);
merge decisions are least often endorsed for behavioral indicators; among relationships,
`causes` and `correlates` are lowest, and corrections almost always weaken the asserted
relationship. Two broad entities, the behavioral indicator Text generation and the construct
Mathematical reasoning, accounted for most harmonization disagreement; this release splits
both, so the paper's agreement figures were measured before that correction.

## Failure modes to keep in mind

1. **Behavioral indicators are the hardest category.** Deciding whether a mention is a
   task, a behavior or a construct is ambiguous for experts too; inspect the surface names
   of a behavior before relying on it.
2. **Over-claimed relation strength.** The pipeline sometimes assigns `causes` or
   `correlates` where the paper supports only `related` or `measured_by`.
3. **Umbrella entities.** Broad canonical names (text generation, reasoning, safety) collect
   members a reviewer may not endorse; the surface variants and per-paper definitions are
   kept so each merge can be inspected.
4. **Anthropomorphic phrasing.** Some summaries of cognitive constructs describe them as
   abilities; the summaries describe literature usage, not demonstrated properties.
5. **Text-driven evidence.** Snippets come from the paper text; figures and tables
   contribute weaker context than abstracts and method sections.

## Biases of the model system

- The three extraction models are frontier or near-frontier language models trained on web
  data and share a notion of what counts as a construct that may differ from measurement
  theory in the social sciences.
- Prompts and papers are in English.
- Model training cutoffs make very recent benchmarks less familiar than established ones.

## Reproduction

Running `pipeline/configs/lexis_v0.0.1.yaml` end to end needs API access to Google, OpenAI
and Together and downloads the source PDFs from the proceedings sites. Set
`harmonization.batch_retries` and `harmonization.on_batch_failure: stop` so that a failed
batch is retried or ends the run instead of dropping its names. Model outputs are not
deterministic across providers and dates, so a rerun reproduces the procedure, not the exact
artifact; the released artifact is `lexis/ai_construct_lexis_v0.0.1.json`.

## Licence

MIT (pipeline code). Source-paper text is processed under fair-use rationale; the artifact
ships only metadata and short verbatim quotations.
