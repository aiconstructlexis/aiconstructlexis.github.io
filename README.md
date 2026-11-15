# AI Construct Lexis

The AI Construct Lexis makes the nomological network implied by published AI papers
explicit: the **constructs** papers claim to study (reasoning, safety, robustness, ...), the
**behavioral indicators** they observe (tasks and output patterns), the **measurement
instruments** they use (benchmarks, human studies, protocols), and the relationships the
papers assert among them, each grounded in verbatim evidence from the source text.

This repository is the public home of the Lexis. It holds the website, the released data,
the pipeline that builds the Lexis from conference proceedings, and the confirmatory
analyses reported in the paper.

| | |
| --- | --- |
| Website | <https://aiconstructlexis.github.io> |
| Release | v0.0.1 (November 2026) |
| Paper | *AI Construct Lexis: A Network of Constructs and Measurement Instruments Used in AI Evaluation.* NeurIPS 2026, Evaluations and Datasets track (to appear). |
| Contact | <aiconstructlexis@gmail.com> |

## What is in this repository

```
.
├── site/                         the website, served by GitHub Pages from this directory
│   ├── index.html                home page and entity explorer
│   ├── view_network.html         redirects to index.html, keeping the query (older links)
│   ├── network_graph.html        interactive network
│   ├── tools.html, tools_*.html  analysis support tools
│   ├── empirical_evidence.html   papers with empirical validity evidence
│   ├── assets/                   stylesheets, scripts, favicon
│   ├── config/                   display settings of the explorer and the tools
│   └── data/                     per-entity JSON of the in-scope entities, graph bundle and layout, paper URLs,
│                                 analysis bundle, readable/ Markdown mirror (written by the pipeline's export
│                                 stage); empirical_evidence.json is maintained by hand
├── lexis/                        the released Lexis (one JSON file) and the screened paper lists
├── pipeline/                     the extraction and harmonization pipeline (Python package, `lexis` CLI)
├── analysis/                     the confirmatory factor analyses of the paper's case studies
├── docs/                         data card and model card
├── CHANGELOG.md, CONTRIBUTING.md
└── LICENSE (code, MIT), LICENSE.content (data, CC BY 4.0)
```

## The data

`lexis/ai_construct_lexis_v0.0.1.json` is the Lexis: every canonical entity with its
surface variants, per-paper definitions, supporting papers by venue, source snippets and a
synthesized "State of the Field" summary, plus every relationship with its per-paper claims
and evidence quotes. `lexis/README.md` documents the schema; `docs/DATA_CARD.md` describes
scope, collection and known limitations.

| | |
| --- | --- |
| Venues | ICLR 2024, NeurIPS 2024, ICLR 2025, NAACL 2025, ACL 2025, ICML 2025, EMNLP 2025 |
| Papers | 7,173 main-conference papers (7,175 of 17,835 proceedings entries were screened as LLM-related; one ACL 2025 and one EMNLP 2025 paper are not in the corpus because the title read from their PDFs could not be matched to the proceedings entry) |
| Constructs | 919 in scope (plus 72 extracted entities that expert review marked out of scope); 686 with at least two supporting papers |
| Behavioral indicators | 899 in scope (plus 51); 683 with at least two papers |
| Measurement instruments | 1,356 in scope (plus 248); 1,177 with at least two papers |
| Relationships | 6,054, of which 5,479 link in-scope entities (measured_by 3,475 · related 1,265 · causes 674 · correlates 65) |

`lexis/paper_lists/<venue>.json` lists every proceedings entry that was screened, with its
title, URL and the screening decision; the corpus actually extracted is the `papers` list of
the artifact. The interface shows entities with at least two supporting papers
(`site/config/view_network.json`) and draws relationships reported in at least two papers on
the interactive network; single-paper entities and relationships are in the artifact.

## The pipeline

`pipeline/` is an installable Python package. One YAML file describes a run: venues and
their sources, the extraction panel, the vote thresholds, the harmonization and summary
models, and where the outputs go. `pipeline/configs/lexis_v0.0.1.yaml` is the configuration
that produced this release; `pipeline/configs/example_small.yaml` builds a small Lexis from
one venue. `pipeline/README.md` documents every stage and configuration key.

### Running the whole pipeline, step by step

The run has ten stages. Six run per venue (`ingest`, `screen`, `extract`, `simplify`,
`harmonize`, `vote`) and four run once over all venues (`join`, `curate`, `summarize`,
`export`). Each stage reads the previous stage's file from disk and writes its own, so a
run can be stopped and resumed at any stage, and `--venues` processes one venue at a time.

You need Python 3.11 or newer and API keys for the three providers the release used: Google
(Gemini 2.5 Pro for extraction, harmonization and the cross-venue merge), OpenAI (GPT-5.4 mini
for extraction, GPT-5.4 for the summaries) and Together (gpt-oss-120b for screening, Qwen for
extraction). The screening, extraction and summary stages submit batch jobs, which the
providers complete within their batch window (up to 24 hours each), and every model call is
paid. A full run also downloads the 7,175 screened-in PDFs.

1. Install the package and check the command.

   ```bash
   pip install -e 'pipeline[dev]'
   lexis version
   ```

2. Put the API keys in the environment.

   ```bash
   export GOOGLE_API_KEY=... OPENAI_API_KEY=... TOGETHER_API_KEY=...
   ```

3. Choose a configuration. To rebuild the release without overwriting the released files,
   copy `pipeline/configs/lexis_v0.0.1.yaml`, give the copy its own `version` and
   `paths.work_dir`, and point `export.site_dir` at a copy of `site/` and
   `export.artifact_out` at a new path (the release configuration writes into `site/` and
   `lexis/`). To try the pipeline first, use `pipeline/configs/example_small.yaml`: one
   venue, twenty papers, no summaries.

   ```bash
   cp pipeline/configs/lexis_v0.0.1.yaml pipeline/configs/my_run.yaml
   ```

4. Validate the configuration and list the steps it implies.

   ```bash
   lexis check-config pipeline/configs/my_run.yaml
   lexis plan --config pipeline/configs/my_run.yaml
   ```

5. Ingest and screen. With the shipped paper lists (`papers:` in each venue entry) the
   ingest stage downloads the PDFs of the papers screened as LLM-related and the screen
   stage has nothing to do; remove `papers:` to list the proceedings and screen all 17,835
   entries yourself (ICLR is listed through OpenReview, which needs
   `pip install -e 'pipeline[openreview]'`).

   ```bash
   lexis run --config pipeline/configs/my_run.yaml --stages ingest,screen
   ```

6. Estimate the extraction before paying for it. The dry run builds the request files and
   prints the number of requests per model (and a cost estimate when the models carry a
   `price`).

   ```bash
   lexis run --config pipeline/configs/my_run.yaml --dry-run
   ```

7. Extract, simplify, harmonize and vote, venue by venue. Extraction runs two passes per
   model (entities, then relationships among them) and caches its outputs per paper and
   model, so an interrupted stage picks up where it stopped.

   ```bash
   lexis run --config pipeline/configs/my_run.yaml --stages extract,simplify,harmonize,vote
   ```

8. Join the venues, apply curation, write the summaries and export. The curate stage copies
   the voted network through when the configuration names no `curation.overlay`.

   ```bash
   lexis run --config pipeline/configs/my_run.yaml --stages join,curate,summarize,export
   ```

   `lexis run --config pipeline/configs/my_run.yaml` with no `--stages` runs all ten stages
   in order.

9. Check the export against the artifact and look at the result.

   ```bash
   lexis check-export <site_dir> <artifact>
   ```

   ```bash
   cd <site_dir> && python3 -m http.server 8000 --bind 127.0.0.1
   ```

Outputs land under `paths.work_dir` (`runs/` at the repository root for the shipped
configurations, ignored by git): `venues/<venue id>/` for the per-venue stages and `joint/`
for the rest. Model outputs are not deterministic across providers and dates, so a rerun
reproduces the procedure, not the exact released artifact (`docs/MODEL_CARD.md`,
"Reproduction").

## The analysis

`analysis/` holds the confirmatory factor analyses of the paper's two case studies
(Reasoning, Safety) with their data and a README that states the expected output. They do
not depend on the pipeline:

```bash
python -m venv analysis/.venv && source analysis/.venv/bin/activate && pip install -r analysis/requirements.txt
```

```bash
cd analysis && python reasoning_cfa.py && python safety_cfa.py
```

## Website

`site/` is plain HTML, CSS and JavaScript with no build step. To run it locally:

```bash
cd site && python3 -m http.server 8000 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8000/>.

## Citation

Olawale Salaudeen, Florian E. Dorner, Tom Sühr, Sang Truong, Haoran Zhang, Patrick G.
Bissett, James Fox, Marzyeh Ghassemi, Tom Hartvigsen, Peter Hase, Augustin Kelava, Suhas
Mahesh, Margaret Mitchell, Jamelle Watson-Daniels, Sanmi Koyejo, and Angelina Wang (2026).
*AI Construct Lexis: A Network of Constructs and Measurement Instruments Used in AI Evaluation.*
Advances in Neural Information Processing Systems (NeurIPS), Evaluations and Datasets Track.
To appear.

## Licences

Code (the pipeline, the analysis scripts and the website code) is released under the
[MIT License](LICENSE). The data (the Lexis and the screened paper lists in `lexis/`, the
exported entity records and their readable mirror in `site/data/`) and the documentation are
released under [CC BY 4.0](LICENSE.content). The benchmark exports under `analysis/data/`
keep the terms of their sources (`analysis/data/README.md`). The Lexis stores derived
metadata and short verbatim quotations from the source papers; it does not redistribute
paper text.
