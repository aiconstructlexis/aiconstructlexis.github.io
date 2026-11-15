# Changelog

Releases follow semantic versioning. Patch releases correct entries and definitions; minor
releases add venues or entities; major releases change the schema. Each release reports
what was added, removed, renamed and re-typed relative to the previous one.

## v0.0.1 (November 2026)

First public release, accompanying the NeurIPS 2026 paper.

**Corpus.** 7,173 LLM-related main-conference papers from ICLR 2024 (513), NeurIPS 2024
(731), ICLR 2025 (1,365), NAACL 2025 (551), ACL 2025 (1,417), ICML 2025 (992) and EMNLP 2025
(1,604).

**Contents.**

| Type | In the release | Marked out of scope by expert review | Total extracted |
| --- | ---: | ---: | ---: |
| Constructs | 919 | 72 | 991 |
| Behavioral indicators | 899 | 51 | 950 |
| Measurement instruments | 1,356 | 248 | 1,604 |

Of these, 686 constructs, 683 behavioral indicators and 1,177 measurement instruments have
at least two supporting papers and are shown in the interface by default; single-paper
entities are in the artifact and not shown by default.

6,054 relationships (measured_by 3,798, related 1,387, causes 795, correlates 74), of which
5,479 link in-scope entities (measured_by 3,475, related 1,265, causes 674, correlates 65);
the remaining 575 touch an entity marked out of scope and are kept for transparency but not
shown. One relationship type per pair of entities (the strictest type any paper's vote
produced), each with its supporting papers, per-paper claim types and evidence quotes.

**Pipeline.** Three extraction models per paper with a vote that keeps what at least two
models support, at the canonical level; Gemini 2.5 Pro harmonization and cross-venue merge;
a pair-level relationship vote; expert curation of entities and relationships, folded into
the released artifact; and GPT-5.4 summaries for entities with at least three supporting
papers. The configuration is `pipeline/configs/lexis_v0.0.1.yaml`; the models and parameters
are in `docs/MODEL_CARD.md`.

**Website.** Entity explorer with per-entity pages, interactive network, analysis support
tools (confirmatory analysis, instrument overlap and separation, instrument profile, claim
checker) and an empirical evidence page.
