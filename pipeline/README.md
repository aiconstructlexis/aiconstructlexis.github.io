# The Lexis pipeline

`aiconstructlexis` builds a Lexis from conference proceedings: it downloads the papers,
screens them for relevance, extracts constructs, behavioral indicators, measurement
instruments and their relationships with several language models, harmonizes the names,
keeps what the models agree on, merges across venues, applies reviewer corrections,
writes a summary per entity and exports the data the website reads.

One YAML file describes a run. `configs/lexis_v0.0.1.yaml` is the configuration of the
released Lexis; `configs/example_small.yaml` builds a small one from twenty papers of one
venue. Changing the venues, the models, the thresholds or the prompts is a config change,
not a code change.

## Install

Python 3.11 or newer.

```bash
pip install -e .            # from this directory; add [dev] for pytest, [openreview] for the OpenReview source
lexis version
```

API keys are read from the environment when a stage needs them:
`OPENAI_API_KEY`, `GOOGLE_API_KEY`, `TOGETHER_API_KEY`. The vote, curate and export stages
need no key; join needs the key of `join.provider` for the cross-venue merge.

## Run

```bash
lexis check-config configs/example_small.yaml       # validate and print the resolved config
lexis plan --config configs/example_small.yaml      # list the steps and the files they write
lexis run --config configs/example_small.yaml --stages ingest,screen
lexis run --config configs/example_small.yaml --dry-run                    # extraction request estimate, no model calls
lexis run --config configs/example_small.yaml       # everything
lexis run --config configs/example_small.yaml --stages join,curate,summarize,export   # resume from the joint stages
```

Every stage reads the previous stage's file from disk and writes its own, so a run can be
resumed from any stage, and a venue can be processed on its own with `--venues`.

`--dry-run` builds the extraction request files for the screened papers and prints the
request estimate per model, so it runs after `--stages ingest,screen`. It also prints a
cost estimate when the models carry a `price: [input_usd_per_million, output_usd_per_million]`;
the shipped configs carry no prices.

## Stages

Per venue (under `<work_dir>/venues/<venue id>/`):

| Stage | Reads | Writes | What happens |
| --- | --- | --- | --- |
| `ingest` | the venue's source (proceedings site, OpenReview, ACL Anthology, PMLR), or a given paper list whose PDFs are fetched | `papers.json`, PDFs | main-conference papers only (for NeurIPS the main track and the Datasets and Benchmarks track); title, URL and PDF path per paper. An OpenReview submission without a decision reply or an accepting `venueid` counts as accepted only when its venue string names the decision or a presentation format (accept, poster, spotlight, oral) and not a submission, withdrawal, rejection or desk rejection |
| `screen` | `papers.json` | `papers.json` (`is_LLM_paper` added) | one yes/no relevance decision per paper, batch or synchronous, from the first pages of the PDF (the venue's main-body page limit plus one or two pages of buffer: NeurIPS, ICML and the *ACL venues 10, ICLR 11, other venues 12; references and appendices are not read). A paper whose request fails is left without a verdict and carries `screen_error`, and the next run screens it again; only a PDF with no extractable text is recorded as not LLM-related without a model call (`screen_note` "empty_pdf") |
| `extract` | `papers.json`, PDFs | `extraction/trials/<label>/`, `extraction/inputs/extraction.json`, `run_report.json` | two passes per model (entities, then relationships among them) over the same pages as screening; per paper, an entity is kept when at least `voting.threshold` models propose it (2 in the release, whatever the panel size) and relationships are kept from every model for the later pair vote; outputs are cached per paper and model |
| `simplify` | `extraction.json` | `simplified.json` | parsed entities and relationships per paper and model, raw text dropped |
| `harmonize` | `simplified.json` | `harmonized.json`, `name_mapping.json` | an LLM groups surface names into canonical entities per type; relationships are aggregated onto the canonical names deterministically; residual surface variants are collapsed deterministically; `name_mapping.json` maps surface names to canonical names |
| `vote` | `harmonized.json`, trials | `harmonized.json`, `harmonized.multi_paper.json` | a (entity, paper) credit needs `voting.threshold` models that proposed any surface name of the entity for that paper; entities with fewer than `voting.min_papers` papers are dropped |

Joint (under `<work_dir>/joint/`):

| Stage | Writes | What happens |
| --- | --- | --- |
| `join` | `union.json`, `merged.json`, `voted.json` | union across venues at canonical name; an LLM merge of semantic duplicates across venues; the joint entity vote; the relationship vote (a pair counts for a paper when `voting.threshold` models link it, the paper's type is the strictest any of them gave, `measured_by` points at the instrument); one type per pair of entities; definitions without papers dropped |
| `curate` | `curated.json`, `curated.report.json` | reviewer operations from `curation.overlay` (alias moves, renames, merges, splits, removals, type changes, summary corrections, retracted, re-typed or moved claims) applied, then the relationship vote and the type guard again; without an overlay the voted network is copied |
| `summarize` | `summarized.json` | one summary request per entity with at least `summaries.min_papers` papers through the provider's batch API; a check pass rewords phrases that refer to the model's input rather than to the papers ("across the provided sources" becomes "across the papers") and retries summaries with hard problems once (OpenAI provider) |
| `export` | `ai_construct_lexis_v<version>.json`, site data | the release artifact (process fields removed, release metadata added), per-entity JSON and readable Markdown of the in-scope entities (those not flagged `expert_removed`), graph bundle, paper URLs, analysis bundle, graph layout, and a check that the site's data holds exactly the artifact's in-scope entities and their relationships to one another, plus every file the pages read |

Each stage is also a module with its own command line, for use outside a config-driven run,
for example:

```bash
python -m aiconstructlexis.extract.multi_model --help
python -m aiconstructlexis.vote.relationships --help
python -m aiconstructlexis.export.site_data --help
```

## Configuration

Paths in a config are relative to the config file. The sections:

| Section | Keys |
| --- | --- |
| `version` | label written into the artifact and output names |
| `paths` | `work_dir`, `pdf_dir` (default `<work_dir>/pdfs`), `log_dir` |
| `prompts` | `default`, or a dotted module path to a module defining the same prompt constants |
| `venues[]` | `id`, `conference`, `year`, `source` (`proceedings`, `openreview`, `anthology`, `pmlr`), `volume` (Anthology volume id or PMLR volume), optional `papers` (an existing paper list, screened or not: its PDFs are downloaded instead of listing the venue), `sample` (process a seeded sample of this many papers), `tracks` (proceedings tracks to list), `trials_dir` (the `trials/` folder of an earlier extraction), `models` (a per-venue extraction panel) |
| `screening` | `enabled` (when false, every listed paper is kept), `provider`, `model`, `mode` (`batch` on the Together batch API, or `sync`), `workers`, `max_rpm`, `poll_interval` |
| `extraction` | `models[]` (`provider`, `model`, `label`, optional per-model `temperature`, `max_tokens` and `price` as USD per million input and output tokens for the dry-run estimate), `temperature`, `max_tokens`, `workers` (threads for PDF text extraction and batch polling), `max_papers`, `allow_partial` |
| `harmonization` | `provider`, `model`, `batch_size`, `batch_retries`, `on_batch_failure`, `reasoning_effort`, `seed_name_mapping` (a previous release's artifact, or a `{surface name: canonical name}` JSON file; its canonical names are reused before the LLM sees new names) |
| `voting` | `threshold` (models that must support an (entity, paper) or (pair, paper); 2 in the release), `min_papers` (per-venue floor on an entity's papers before the join; 2), `survivor` (`strictest` or `majority`: which type a pair keeps across papers; `strictest`), `type_guard` (`measured_by` only from a construct or behavior to an instrument, a reversed one is flipped and any other becomes `related`; `causes` touching an instrument is dropped; `correlates` joins two instruments or two non-instruments, and an instrument with a construct or behavior becomes `related`; on), `per_paper_resolution` (resolve a raw endpoint name through the paper's own memberships before spelling; off), `keep_all_quotes` (keep every linking model's quote per paper in `evidence_by_paper[*].quotes`, nothing is discarded either way; off), `evidence_check` (record whether the displayed quote names both endpoints; filters nothing; off) |
| `join` | `provider`, `model`, `batch_size` (names per merge batch; a pass across batches runs only when a type has at most this many groups), `reasoning_effort`, `postmerge` (deterministic residual collapse after the union; on) |
| `curation` | `overlay` (JSONL of reviewer operations: `move_alias`, `remove_alias`, `split`, `merge`, `rename`, `set_type`, `remove_entity`, `restore_entity`, `set_summary`, `retract_claim`, `retype`, `move_claim`, `add_claim`; the format is documented in `aiconstructlexis/curate/overlay.py`) |
| `summaries` | `enabled`, `provider` (`openai` or `google`), `model`, `reasoning_effort`, `min_papers`, `poll_interval`, `check_retry` (OpenAI only) |
| `export` | `site_dir`, `artifact_out`, `readable`, `analysis_bundle`, `graph_layout`, `layout_seed`, `check` |

Model `label`s name the per-model trial directories; keep them stable across runs so the
cache is reused. A cache made with a different model or prompt is refused.

## Prompts

The prompts that produced the release are in `aiconstructlexis/prompts/default.py`; print
them with `lexis prompts`. The extraction prompts were revised once during the release run;
`aiconstructlexis/prompts/earlier.py` holds the earlier revision (print it with
`lexis prompts --set aiconstructlexis.prompts.earlier`). Screening and
extraction outputs record the fingerprint of the prompt that produced them. To run a
differently prompted pipeline, point `prompts:` at a module that defines the same constants.

## Reproducing the release

`configs/lexis_v0.0.1.yaml` lists the seven venues with the screened paper lists of the
release (`../lexis/paper_lists/`), the extraction panels submitted per venue (`docs/MODEL_CARD.md`
notes the batches that were not collected), and the
harmonization, vote and summary settings. Running it downloads the 7,175 screened-in PDFs
(all 17,835 proceedings PDFs if `papers:` is removed so that screening reruns) and makes
paid API calls to three providers. The reviewer corrections of the release are folded into
the released artifact rather than distributed as an overlay, so the curate stage is a no-op
in this configuration. Model outputs are not deterministic across providers and dates, so a
rerun reproduces the procedure, not the exact released artifact; the released artifact is
`../lexis/ai_construct_lexis_v0.0.1.json`, and `lexis check-export ../site ../lexis/ai_construct_lexis_v0.0.1.json`
verifies that the website data in this repository matches it.

## Layout

```
aiconstructlexis/
  cli.py            the lexis command
  config.py         configuration schema, loading and validation
  pipeline.py       stage order, file layout, config -> stage calls
  prompts/          the prompt set
  providers/        LLM client factories
  util/             logging, JSON repair, PDF text, name helpers
  ingest/           proceedings, OpenReview, ACL Anthology and PMLR downloaders
  screen/           relevance screening
  extract/          multi-model extraction, batch helpers, simplification
  harmonize/        LLM grouping, batch packing by token signature, relationship aggregation, residual collapse
  vote/             entity votes, relationship vote, pair-type consolidation, minimum-paper filter
  join/             cross-venue union and LLM merge
  curate/           curation overlay and cleanup
  summarize/        per-entity summaries and checks
  export/           site data, readable Markdown, analysis bundle, graph layout, export check, release artifact
tests/              pytest suite (no API calls; model clients are faked)
configs/            the release configuration and a small example
```

## Tests

```bash
pip install -e '.[dev]'
pytest
```
