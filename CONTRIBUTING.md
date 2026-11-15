# Contributing

The Lexis is meant to be maintained with the community. Contributions are made through
GitHub issues and pull requests on this repository.

## Report an error in an entry

Open an issue titled `[entry] <canonical name>` and say what is wrong: a merged name that
does not belong (name the surface variant and quote the paper), a wrong type (construct,
behavioral indicator, measurement instrument), a relationship a paper does not support
(name the paper and the claimed relationship), or a summary that misstates how the
literature uses the term (quote the sentence and the source that contradicts it).
Corrections are applied as curation operations (see `pipeline/aiconstructlexis/curate/overlay.py`
for the operation format) and listed in the changelog of the next release.

## Propose a missing entity or relationship

Open an issue titled `[missing] <name>` with at least two papers that use the term, the type
you propose, and, for a relationship, the papers and quotes that assert it.

## Submit empirical validity evidence

The Empirical Evidence page lists papers that empirically test constructs, instruments or
behavioral indicators. Fill in the form under "Suggest a paper" on that page, press
"Copy entry" and email the entry to <aiconstructlexis@gmail.com>.

## Add a venue

Add the venue to a copy of `pipeline/configs/lexis_v0.0.1.yaml`, run the pipeline
(`pipeline/README.md`), and open a pull request with the new paper list, the updated Lexis
and a changelog entry listing added, removed, renamed and re-typed entities. Set
`harmonization.seed_name_mapping` to the previous release's artifact so names stay stable
across releases.

## Code

Pipeline changes come with tests (`pipeline/tests`, run with `pytest`). A new stage keeps the
pattern of the existing ones: a module with plain functions, a standalone `main`, and an
entry in `pipeline/aiconstructlexis/pipeline.py`. Prompt changes are documented in the pull
request, because they change what the pipeline extracts.

## Review

Maintainers review contributions on the release cycle described in the paper: two scheduled
releases a year aligned with the major machine learning and NLP publication cycles, with
corrections of clear errors merged as they come.
