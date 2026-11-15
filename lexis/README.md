# The Lexis data

`ai_construct_lexis_v0.0.1.json` is the released Lexis: one JSON object holding every
entity, every relationship, the corpus and the name mapping. The website's
`site/data/` directory is derived from it by the pipeline's export stage (all but
`empirical_evidence.json`, which is maintained by hand).

## Top level

| Key | Content |
| --- | --- |
| `metadata` | name, version, venues, paper counts by venue, entity counts (in scope), relationship counts (all, and between in-scope entities), paper count |
| `constructs`, `measurements`, `behaviors` | lists of entity records (below) |
| `relationships` | list of relationship records (below) |
| `papers` | the corpus: `[{conference, paper}]`, one entry per LLM-related paper |
| `paper_count_by_conference` | papers per venue |
| `name_mapping` | surface name (as extracted) → the canonical name of the entity that lists it; a surface name listed by several entities maps to the list of their names |

Venue ids: `iclr24`, `neurips24`, `iclr25`, `naacl25`, `acl25`, `icml25`, `emnlp25`.

## Entity record

| Field | Content |
| --- | --- |
| `canonical_name` | the entity's name |
| `original_names` | surface variants merged into it |
| `original_nodes` | per surface variant: `{definition, papers: [[venue, paper], ...]}`; the definition is the first one extracted for that surface name and `papers` the papers recorded with that name during harmonization, a subset of the entity's supporting papers (`papers` below lists them all). The v0.0.1 records do not say which of those papers the definition came from; the shipped pipeline records it as `definition_paper`, so later releases will |
| `source_snippets_evidence` | `[{original_name, paper, definition, source_snippets or snippet}]`: verbatim snippets per paper (the snippet key depends on the extraction output) |
| `papers`, `papers_by_conference` | supporting papers: `[{conference, paper}]`, and `{venue: [title, ...]}` |
| `paper_count`, `paper_count_by_conference` | their counts |
| `characterization` | the synthesized "State of the Field" summary (entities with at least three papers; a short deterministic description otherwise) |
| `characterization_sections` | the summary split into its sections: constructs `definition`, `systematization`, `measurement`, `links`; behaviors `definition`, `variants`, `measurement`, `evidence_of`; instruments `description`, `measures`, `usage`, `concerns` (entities with at least three papers) |
| `expert_removed`, `expert_removed_reason` | set when expert review judged the entity out of scope (a method, a metric, a property of data or of an attack rather than of a model). Such entities are kept for transparency and are not shown in the interface or counted in the release totals. |

A paper supports an entity when at least two of the three extraction models proposed one of
its surface names for that paper (`docs/MODEL_CARD.md` notes where one model's runs are
incomplete).

## Relationship record

| Field | Content |
| --- | --- |
| `source`, `target` | canonical entity names; for `measured_by` the target is always the instrument |
| `type` | `measured_by`, `related`, `causes` or `correlates` |
| `papers` | `[{conference, paper, type_share, claim_type}]`: the papers that assert the relationship; `type_share` is 1, or 0.5 when the models tied on direction; `claim_type` (present only on relationships whose papers disagreed on the type, those with `type_breakdown`) is the type that paper's own vote produced and may equal `type` |
| `papers_by_conference`, `paper_count`, `paper_count_by_conference` | the supporting papers by venue and their counts |
| `paper_weight` | sum of `type_share` over papers |
| `evidence`, `evidence_by_paper` | verbatim quotes: `evidence` holds up to ten distinct quotes, `evidence_by_paper` every quote as `[{conference, paper, quote}]` |
| `type_breakdown` | papers per claimed type, when papers disagreed on the type |
| `n_papers_split` | papers whose linking models gave more than one type |
| `consolidated_from` | relationships folded into this one so that each pair of entities carries one type (`[[source, type, target], ...]`) |

A pair of entities is linked in a paper when at least two models linked it, whatever types
they gave; the paper's type is the strictest any of them gave (causes > measured_by >
correlates > related). Across papers, each unordered pair keeps one type, again the
strictest; mutual `causes` relationships in both directions are kept. The relationship vote and
the entity vote are separate, so a relationship's papers need not be among its endpoints'
supporting papers.

## Site records

`site/data/constructs/`, `site/data/measurements/` and `site/data/behaviors_tasks/` hold one
`<slug>.json` per in-scope entity: the per-entity view the website reads, derived from the
entity record above: the canonical name and type, `names` (the surface variants), the
supporting papers by venue, `definitions` as `[{text, papers, original_name}]` (one entry
per surface name that carries a definition; `text` is the first definition extracted for
that name and `papers` the papers recorded with it), the relationships that
touch the entity with their papers and quotes, and the summary with its sections. Quotes and
definitions are reproduced as extracted. `site/data/readable/` holds the same records as
Markdown.

## Paper lists

`paper_lists/<venue>.json` holds every main-conference entry of the venue that was screened:
`[{title, url, is_LLM_paper, paper_id?}]`. Entries with `is_LLM_paper: true` were screened as
LLM-related (7,175); the artifact's `papers` list (7,173) is the corpus that was extracted;
`null` means no screening decision was recorded (two ACL 2025 entries).
