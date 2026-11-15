"""The pipeline: stages, their inputs and outputs, and the order they run in.

Per venue (``venues/<id>/`` under the work directory):

    ingest     papers.json                      paper list (title, url, pdf path) and PDFs
    screen     papers.json (in place)           is_LLM_paper flag per paper
    extract    extraction/                      per-model trials and extraction.json
    simplify   simplified.json                  parsed entities and relationships per paper and model
    harmonize  harmonized.json                  canonical entities (LLM grouping), deterministic
               name_mapping.json                relationship aggregation, residual surface variants
                                                collapsed; name_mapping.json seeds the next release
    vote       harmonized.json (in place)       (entity, paper) credits that >= threshold models support;
               harmonized.multi_paper.json      entities with >= min_papers papers

Joint (``joint/``):

    join       union.json -> merged.json -> voted.json
                 union across venues, LLM cross-venue merge, joint entity vote, relationship
                 vote, one type per pair, orphan definitions dropped
    curate     curated.json, curated.report.json   reviewer operations applied (optional)
    summarize  summarized.json                  per-entity summaries plus checks (optional)
    export     ai_construct_lexis_v<version>.json, site data
                                                release artifact, per-entity JSON, graph bundle,
                                                readable Markdown, analysis bundle, graph layout

Every stage reads the previous stage's file from disk and writes its own, so a run can be
resumed from any stage with ``--stages``. Stage functions take plain paths and values; the
mapping from the config to those values lives here and nowhere else.
"""
from __future__ import annotations

import json
import logging
import shutil
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional

from aiconstructlexis.config import Config, VenueConfig

logger = logging.getLogger(__name__)

VENUE_STAGES = ("ingest", "screen", "extract", "simplify", "harmonize", "vote")
JOINT_STAGES = ("join", "curate", "summarize", "export")
STAGES = VENUE_STAGES + JOINT_STAGES


class StageError(RuntimeError):
    """A stage could not run (missing input, failed step)."""


# ---------------------------------------------------------------------------------------
# file layout
# ---------------------------------------------------------------------------------------

class Layout:
    """Where each stage reads and writes, derived from the config."""

    def __init__(self, cfg: Config):
        self.cfg = cfg

    # per venue
    def papers(self, v: VenueConfig) -> Path:
        return self.cfg.venue_dir(v.id) / "papers.json"

    def extraction_dir(self, v: VenueConfig) -> Path:
        return self.cfg.venue_dir(v.id) / "extraction"

    def trials_dir(self, v: VenueConfig) -> Path:
        return v.trials_dir or (self.extraction_dir(v) / "trials")

    def extraction(self, v: VenueConfig) -> Path:
        own = self.extraction_dir(v) / "inputs" / "extraction.json"
        if v.trials_dir is not None and not own.is_file():
            # Trials made by an earlier run keep their extraction.json beside them.
            beside = Path(v.trials_dir).parent / "inputs" / "extraction.json"
            if beside.is_file():
                return beside
        return own

    def simplified(self, v: VenueConfig) -> Path:
        return self.cfg.venue_dir(v.id) / "simplified.json"

    def harmonized(self, v: VenueConfig) -> Path:
        return self.cfg.venue_dir(v.id) / "harmonized.json"

    def multi_paper(self, v: VenueConfig) -> Path:
        return self.cfg.venue_dir(v.id) / "harmonized.multi_paper.json"

    # joint
    @property
    def union(self) -> Path:
        return self.cfg.joint_dir / "union.json"

    @property
    def merged(self) -> Path:
        return self.cfg.joint_dir / "merged.json"

    @property
    def voted(self) -> Path:
        return self.cfg.joint_dir / "voted.json"

    @property
    def curated(self) -> Path:
        return self.cfg.joint_dir / "curated.json"

    @property
    def summarized(self) -> Path:
        return self.cfg.joint_dir / "summarized.json"

    @property
    def artifact(self) -> Path:
        return self.cfg.joint_dir / f"ai_construct_lexis_v{self.cfg.version}.json"

    def latest_network(self, candidates: Optional[Iterable[Path]] = None) -> Path:
        """The joint network written last (by modification time) among the candidates present."""
        present = [p for p in (candidates or (self.summarized, self.curated, self.voted)) if p.is_file()]
        if not present:
            raise StageError(f"No joint network under {self.cfg.joint_dir}; run the join stage first")
        return max(present, key=lambda p: p.stat().st_mtime)


def _need(path: Path, produced_by: str) -> Path:
    if not Path(path).is_file():
        raise StageError(f"Missing {path} (produced by the {produced_by} stage)")
    return Path(path)


def _copy(src: Path, dst: Path) -> Path:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() != dst.resolve():
        shutil.copyfile(src, dst)
    return dst


# ---------------------------------------------------------------------------------------
# per-venue stages
# ---------------------------------------------------------------------------------------

def stage_ingest(cfg: Config, lay: Layout, v: VenueConfig) -> Path:
    out = lay.papers(v)
    if out.is_file():
        logger.info("[%s] ingest: %s is present; nothing to do (delete it to list the venue again)", v.id, out)
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf_dir = cfg.pdf_dir / v.id
    if v.papers is not None:
        from aiconstructlexis.ingest import download_listed
        logger.info("[%s] ingest: downloading the papers of the given list %s", v.id, v.papers)
        return download_listed(paper_list_json=_need(v.papers, "config"), out_json=out, pdf_dir=pdf_dir,
                               sample=v.sample)
    if v.source in ("proceedings", "openreview"):
        from aiconstructlexis.ingest import download_venue
        download_venue(conference=v.conference, year=v.year, out_json=out, pdf_dir=pdf_dir, source=v.source,
                       tracks=v.tracks, sample=v.sample)
    elif v.source == "anthology":
        from aiconstructlexis.ingest import download_anthology
        download_anthology(venue=v.conference, year=v.year, out_json=out, pdf_dir=pdf_dir, volume=v.volume,
                           sample=v.sample)
    elif v.source == "pmlr":
        from aiconstructlexis.ingest import download_pmlr
        download_pmlr(volume=int(v.volume), conference=v.conference, year=v.year, out_json=out, pdf_dir=pdf_dir,
                      sample=v.sample)
    else:
        raise StageError(f"Unknown venue source {v.source!r}")
    return out


def _already_screened(path: Path) -> bool:
    try:
        papers = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    items = papers if isinstance(papers, list) else list(papers.values())
    return bool(items) and all("is_LLM_paper" in p for p in items if isinstance(p, dict))


def stage_screen(cfg: Config, lay: Layout, v: VenueConfig) -> Path:
    papers = _need(lay.papers(v), "ingest")
    if not cfg.screening.enabled:
        if not _already_screened(papers):
            # Without screening every listed paper is in scope.
            items = json.loads(papers.read_text(encoding="utf-8"))
            for p in (items if isinstance(items, list) else items.values()):
                if isinstance(p, dict):
                    p.setdefault("is_LLM_paper", True)
            papers.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
            logger.info("[%s] screen: disabled; every listed paper is kept", v.id)
        else:
            logger.info("[%s] screen: disabled", v.id)
        return papers
    if _already_screened(papers):
        logger.info("[%s] screen: every paper already carries is_LLM_paper; nothing to do", v.id)
        return papers
    from aiconstructlexis.screen import screen_papers
    s = cfg.screening
    screen_papers(input_json=papers, output_json=papers, provider=s.provider, model=s.model, mode=s.mode,
                  prompts=cfg.prompts, workers=s.workers, max_rpm=s.max_rpm, poll_interval=s.poll_interval,
                  conference=v.conference)
    return papers


def stage_extract(cfg: Config, lay: Layout, v: VenueConfig, dry_run: bool = False) -> Path:
    if v.trials_dir is not None:
        extraction = lay.extraction(v)
        if not extraction.is_file():
            raise StageError(f"[{v.id}] trials_dir {v.trials_dir} is set but no extraction.json was found at "
                             f"{extraction} or beside the trials; copy it there or unset trials_dir")
        logger.info("[%s] extract: using existing trials %s", v.id, v.trials_dir)
        return extraction
    papers = _need(lay.papers(v), "ingest/screen")
    from aiconstructlexis.extract import run_extraction
    e = cfg.extraction
    kwargs = dict(papers_json=papers, work_dir=lay.extraction_dir(v),
                  models=[m.as_dict() for m in cfg.models_for(v)],
                  temperature=e.temperature, workers=e.workers, max_papers=e.max_papers,
                  allow_partial=e.allow_partial, dry_run=dry_run, prompts=cfg.prompts,
                  conference=v.conference, vote_threshold=cfg.voting.threshold)
    if e.max_tokens is not None:
        kwargs["max_tokens"] = e.max_tokens
    return run_extraction(**kwargs)


def stage_simplify(cfg: Config, lay: Layout, v: VenueConfig) -> Path:
    from aiconstructlexis.extract.simplify import simplify
    return simplify(_need(lay.extraction(v), "extract"), lay.simplified(v))


def stage_harmonize(cfg: Config, lay: Layout, v: VenueConfig) -> Path:
    from aiconstructlexis.harmonize import aggregate_relationships, collapse_residuals, harmonize
    h = cfg.harmonization
    simplified = _need(lay.simplified(v), "simplify")
    out = lay.harmonized(v)
    harmonize(input_json=simplified, output_json=out, provider=h.provider, model=h.model,
              batch_size=h.batch_size, name_mapping=h.seed_name_mapping,
              name_mapping_out=cfg.venue_dir(v.id) / "name_mapping.json",
              batch_retries=h.batch_retries, on_batch_failure=h.on_batch_failure,
              reasoning_effort=h.reasoning_effort, prompts=cfg.prompts)
    aggregate_relationships(simplified_json=simplified, harmonized_json=out)
    collapse_residuals(harmonized_json=out, simplified_json=simplified)
    return out


def _venue_labels(cfg: Config, lay: Layout, v: VenueConfig) -> List[str]:
    """The trial labels of a venue: its extraction panel, or, for a venue that only brings
    existing trials, the model directories found under them."""
    labels = [m.label for m in cfg.models_for(v)]
    if labels:
        return labels
    tdir = lay.trials_dir(v)
    if not tdir.is_dir():
        return []
    return sorted(p.name for p in tdir.iterdir() if (p / "entity_trials.json").is_file())


def _all_labels(cfg: Config, lay: Layout) -> List[str]:
    labels: List[str] = []
    for v in cfg.venues:
        for label in _venue_labels(cfg, lay, v):
            if label not in labels:
                labels.append(label)
    return labels


def stage_vote(cfg: Config, lay: Layout, v: VenueConfig) -> Path:
    from aiconstructlexis.vote import filter_min_papers, vote_entities
    harmonized = _need(lay.harmonized(v), "harmonize")
    vote_entities(harmonized_json=harmonized, trials_dir=lay.trials_dir(v),
                  models=_venue_labels(cfg, lay, v), threshold=cfg.voting.threshold, drop_zero=True)
    return filter_min_papers(input_json=harmonized, output_json=lay.multi_paper(v), min_papers=cfg.voting.min_papers)


# ---------------------------------------------------------------------------------------
# joint stages
# ---------------------------------------------------------------------------------------

def _trials(cfg: Config, lay: Layout) -> Dict[str, Path]:
    return {v.id: lay.trials_dir(v) for v in cfg.venues}


def _relationship_vote(cfg: Config, lay: Layout) -> Callable[[Path, Path], Path]:
    """The relationship vote as a callable (also handed to the curation stage to re-vote)."""
    from aiconstructlexis.vote import vote_relationships
    vo = cfg.voting

    def run(network_json: Path, out_json: Path) -> Path:
        return vote_relationships(joint_json=network_json, trials=_trials(cfg, lay), models=_all_labels(cfg, lay),
                                  threshold=vo.threshold, out_json=out_json, per_paper_resolution=vo.per_paper_resolution,
                                  keep_all_quotes=vo.keep_all_quotes, type_guard=vo.type_guard,
                                  evidence_check=vo.evidence_check)
    return run


def stage_join(cfg: Config, lay: Layout) -> Path:
    from aiconstructlexis.curate import drop_orphan_definitions
    from aiconstructlexis.join import build_joint_network, merge_joint_network
    from aiconstructlexis.vote import consolidate_pair_types, vote_joint_entities
    inputs = {v.id: _need(lay.multi_paper(v), "vote") for v in cfg.venues}
    cfg.joint_dir.mkdir(parents=True, exist_ok=True)
    build_joint_network(inputs=inputs, output_json=lay.union, postmerge=cfg.join.postmerge)
    j = cfg.join
    merge_joint_network(input_json=lay.union, output_json=lay.merged, provider=j.provider, model=j.model,
                        batch_size=j.batch_size, reasoning_effort=j.reasoning_effort, prompts=cfg.prompts)
    vote_joint_entities(joint_json=lay.merged, trials=_trials(cfg, lay), models=_all_labels(cfg, lay),
                        threshold=cfg.voting.threshold)
    _relationship_vote(cfg, lay)(lay.merged, lay.voted)
    consolidate_pair_types(input_json=lay.voted, survivor=cfg.voting.survivor)
    drop_orphan_definitions(input_json=lay.voted, output_json=lay.voted)
    return lay.voted


def stage_curate(cfg: Config, lay: Layout) -> Path:
    voted = _need(lay.voted, "join")
    if cfg.curation.overlay is None:
        logger.info("curate: no overlay configured; the voted network is used as is")
        return _copy(voted, lay.curated)
    from aiconstructlexis.curate import apply_overlay
    from aiconstructlexis.vote import consolidate_pair_types
    revote = _relationship_vote(cfg, lay)
    apply_overlay(network_json=voted, overlay_jsonl=_need(cfg.curation.overlay, "config"), out_json=lay.curated,
                  report_json=lay.curated.with_suffix(".report.json"),
                  rerun_vote=lambda net_json, out_json: revote(net_json, out_json))
    consolidate_pair_types(input_json=lay.curated, survivor=cfg.voting.survivor)
    return lay.curated


def stage_summarize(cfg: Config, lay: Layout, source: Optional[Path] = None) -> Path:
    src = source or lay.latest_network((lay.curated, lay.voted))
    if not cfg.summaries.enabled:
        logger.info("summarize: disabled")
        return _copy(src, lay.summarized)
    from aiconstructlexis.summarize.characterize import characterize
    from aiconstructlexis.summarize.checks import check_characterizations
    s = cfg.summaries
    characterize(input_json=src, output_json=lay.summarized, provider=s.provider, model=s.model,
                 reasoning_effort=s.reasoning_effort, min_papers=s.min_papers, poll_interval=s.poll_interval,
                 prompts=cfg.prompts)
    # The check pass runs for every provider; its retry goes through the OpenAI Responses API,
    # so retries are enabled only for the openai provider.
    check_characterizations(input_json=src, output_json=lay.summarized, min_papers=s.min_papers,
                            retry=s.check_retry and s.provider == "openai", model=s.model,
                            reasoning_effort=s.reasoning_effort)
    return lay.summarized


def stage_export(cfg: Config, lay: Layout, source: Optional[Path] = None) -> Path:
    from aiconstructlexis.export import (build_analysis_bundle, build_graph_layout, check_site_export,
                                         export_site_data, write_readable, write_release_artifact)
    network = source or lay.latest_network()
    ex = cfg.export
    artifact = lay.artifact
    write_release_artifact(network_json=network, out_json=artifact, version=cfg.version,
                           venues=[v.id for v in cfg.venues])
    if ex.artifact_out is not None:
        _copy(artifact, ex.artifact_out)
    if ex.site_dir is None:
        return artifact
    site = ex.site_dir
    export_site_data(network_json=artifact, site_dir=site,
                     paper_lists=[lay.papers(v) for v in cfg.venues if lay.papers(v).is_file()],
                     prompts=cfg.prompts)
    if ex.readable:
        write_readable(site_dir=site)
    if ex.analysis_bundle:
        build_analysis_bundle(network_json=artifact, site_dir=site)
    if ex.graph_layout:
        build_graph_layout(site_dir=site, seed=ex.layout_seed)
    if ex.check:
        problems = check_site_export(site_dir=site, network_json=artifact, analysis_bundle=ex.analysis_bundle,
                                     graph_layout=ex.graph_layout, readable=ex.readable)
        if problems:
            raise StageError("site export check failed:\n  " + "\n  ".join(problems[:20]))
    return artifact


# ---------------------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------------------

def select_stages(stages: Optional[Iterable[str]]) -> List[str]:
    if not stages:
        return list(STAGES)
    wanted = []
    for s in stages:
        for part in str(s).split(","):
            part = part.strip()
            if not part:
                continue
            if part not in STAGES:
                raise StageError(f"Unknown stage {part!r}; stages are: {', '.join(STAGES)}")
            wanted.append(part)
    return [s for s in STAGES if s in wanted]


def plan(cfg: Config, stages: Optional[Iterable[str]] = None, venues: Optional[Iterable[str]] = None) -> List[str]:
    """Human-readable list of the steps a run would take."""
    lay = Layout(cfg)
    chosen = select_stages(stages)
    vs = [cfg.venue(x) for x in venues] if venues else list(cfg.venues)
    lines = []
    for v in vs:
        for s in chosen:
            if s in VENUE_STAGES:
                target = {"ingest": lay.papers(v), "screen": lay.papers(v), "extract": lay.extraction(v),
                          "simplify": lay.simplified(v), "harmonize": lay.harmonized(v), "vote": lay.multi_paper(v)}[s]
                lines.append(f"{v.id:>12}  {s:<9} -> {target}")
    for s in chosen:
        if s in JOINT_STAGES:
            target = {"join": lay.voted, "curate": lay.curated, "summarize": lay.summarized, "export": lay.artifact}[s]
            lines.append(f"{'joint':>12}  {s:<9} -> {target}")
    return lines


def run(cfg: Config, stages: Optional[Iterable[str]] = None, venues: Optional[Iterable[str]] = None,
        dry_run: bool = False) -> Dict[str, Path]:
    """Run the selected stages for the selected venues. Returns the path each stage wrote."""
    lay = Layout(cfg)
    chosen = select_stages(stages)
    if dry_run:
        # A dry run estimates the extraction requests; it must not download, screen or merge anything.
        if "extract" not in chosen:
            raise StageError("--dry-run applies to the extract stage; include it in --stages or omit --stages")
        chosen = ["extract"]
        logger.info("dry run: only the extract stage runs, without model calls")
    vs = [cfg.venue(x) for x in venues] if venues else list(cfg.venues)
    written: Dict[str, Path] = {}
    cfg.paths.work_dir.mkdir(parents=True, exist_ok=True)
    for v in vs:
        for s in chosen:
            if s not in VENUE_STAGES:
                continue
            logger.info("=== %s / %s", v.id, s)
            if s == "ingest":
                written[f"{v.id}/ingest"] = stage_ingest(cfg, lay, v)
            elif s == "screen":
                written[f"{v.id}/screen"] = stage_screen(cfg, lay, v)
            elif s == "extract":
                written[f"{v.id}/extract"] = stage_extract(cfg, lay, v, dry_run=dry_run)
            elif s == "simplify":
                written[f"{v.id}/simplify"] = stage_simplify(cfg, lay, v)
            elif s == "harmonize":
                written[f"{v.id}/harmonize"] = stage_harmonize(cfg, lay, v)
            elif s == "vote":
                written[f"{v.id}/vote"] = stage_vote(cfg, lay, v)
    last: Optional[Path] = None   # the joint network written by the previous stage of this run
    for s in chosen:
        if s not in JOINT_STAGES:
            continue
        logger.info("=== joint / %s", s)
        if s == "join":
            last = written["join"] = stage_join(cfg, lay)
        elif s == "curate":
            last = written["curate"] = stage_curate(cfg, lay)
        elif s == "summarize":
            last = written["summarize"] = stage_summarize(cfg, lay, source=last)
        elif s == "export":
            written["export"] = stage_export(cfg, lay, source=last)
    return written
