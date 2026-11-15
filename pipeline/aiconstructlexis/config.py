"""Pipeline configuration.

A run is described by one YAML file (see ``configs/lexis_v0.0.1.yaml`` for the
configuration that produced the released Lexis, and ``configs/example_small.yaml`` for a
small worked example). ``load_config`` reads the file, fills in defaults, validates the
values and resolves every path relative to the directory the file lives in, so a config
can be run from any working directory.

Sections
--------
version        label written into the release artifact and output names
paths          work_dir (all intermediate outputs), pdf_dir (downloaded papers), log_dir
venues         the venues to process; each has an id, a conference, a year, a source and
               optionally its own extraction panel, a ready-made paper list or trials
prompts        name of the prompt set ("default", or a dotted module path)
screening      LLM relevance screening of the paper lists
extraction     the multi-model extraction panel and decoding settings
harmonization  LLM grouping of surface names into canonical entities
voting         majority-vote threshold, per-venue minimum paper count, pair-type rule
join           cross-venue LLM merge
curation       optional overlay of reviewer operations
summaries      per-entity summaries
export         where the site data, the readable mirror and the release artifact go
"""
from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

VENUE_SOURCES = ("proceedings", "openreview", "anthology", "pmlr")
PROVIDERS = ("openai", "google", "together")
SUMMARY_PROVIDERS = ("openai", "google")       # the summary stage uses these providers' batch APIs


class ConfigError(ValueError):
    """The configuration file is missing something or holds an invalid value."""


@dataclass
class ModelSpec:
    provider: str
    model: str
    label: str
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    price: Optional[List[float]] = None     # [USD per million input tokens, USD per million output tokens] for cost estimates

    def as_dict(self) -> Dict[str, Any]:
        d = {"provider": self.provider, "model": self.model, "label": self.label}
        if self.temperature is not None:
            d["temperature"] = self.temperature
        if self.max_tokens is not None:
            d["max_tokens"] = self.max_tokens
        if self.price is not None:
            d["price"] = list(self.price)
        return d


@dataclass
class VenueConfig:
    id: str
    conference: str
    year: int
    source: str = "proceedings"
    volume: Optional[str] = None            # PMLR volume number or Anthology volume id
    papers: Optional[Path] = None           # an existing paper list: skips ingest (and screening when it is already screened)
    trials_dir: Optional[Path] = None       # existing extraction trials: skips extraction
    models: Optional[List[ModelSpec]] = None  # per-venue extraction panel; default: extraction.models
    sample: Optional[int] = None            # download and process only a seeded sample of this many papers
    tracks: Optional[str] = None            # proceedings tracks to list (comma-separated; default: the conference's main tracks)


@dataclass
class PathsConfig:
    work_dir: Path = Path("runs/lexis")
    pdf_dir: Optional[Path] = None          # default: <work_dir>/pdfs
    log_dir: Path = Path("logs")


@dataclass
class ScreeningConfig:
    enabled: bool = True
    provider: str = "together"
    model: str = "openai/gpt-oss-120b"
    mode: str = "batch"                     # batch | sync
    workers: int = 8
    max_rpm: int = 3600
    poll_interval: int = 60


@dataclass
class ExtractionConfig:
    models: List[ModelSpec] = field(default_factory=list)
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    workers: int = 5
    max_papers: int = 0                     # 0 = all screened papers
    allow_partial: bool = False


@dataclass
class HarmonizationConfig:
    provider: str = "google"
    model: str = "gemini-2.5-pro"
    batch_size: int = 100
    batch_retries: int = 0
    on_batch_failure: str = "warn"          # warn | stop
    reasoning_effort: Optional[str] = None
    seed_name_mapping: Optional[Path] = None  # canonical names from a previous release, reused first


@dataclass
class VotingConfig:
    threshold: int = 2                      # models that must support a (entity, paper) or (pair, paper)
    min_papers: int = 2                     # per-venue: entities with fewer papers are dropped before the join
    survivor: str = "strictest"             # one relationship type per pair: strictest | majority
    type_guard: bool = True
    per_paper_resolution: bool = False
    keep_all_quotes: bool = False
    evidence_check: bool = False


@dataclass
class JoinConfig:
    provider: str = "google"
    model: str = "gemini-2.5-pro"
    batch_size: int = 500
    reasoning_effort: Optional[str] = None
    postmerge: bool = True                  # deterministic residual collapse after the union


@dataclass
class CurationConfig:
    overlay: Optional[Path] = None          # JSONL of reviewer operations; None = stage is a no-op


@dataclass
class SummariesConfig:
    enabled: bool = True
    provider: str = "openai"
    model: str = "gpt-5.4"
    reasoning_effort: str = "high"
    min_papers: int = 3
    poll_interval: int = 60
    check_retry: bool = True


@dataclass
class ExportConfig:
    site_dir: Optional[Path] = None         # the website root; None = no site export
    artifact_out: Optional[Path] = None     # where the release artifact JSON is copied
    readable: bool = True
    analysis_bundle: bool = True
    graph_layout: bool = True
    layout_seed: int = 7
    check: bool = True


@dataclass
class Config:
    version: str = "0.0.1"
    source_file: Optional[Path] = None
    paths: PathsConfig = field(default_factory=PathsConfig)
    venues: List[VenueConfig] = field(default_factory=list)
    prompts: str = "default"
    screening: ScreeningConfig = field(default_factory=ScreeningConfig)
    extraction: ExtractionConfig = field(default_factory=ExtractionConfig)
    harmonization: HarmonizationConfig = field(default_factory=HarmonizationConfig)
    voting: VotingConfig = field(default_factory=VotingConfig)
    join: JoinConfig = field(default_factory=JoinConfig)
    curation: CurationConfig = field(default_factory=CurationConfig)
    summaries: SummariesConfig = field(default_factory=SummariesConfig)
    export: ExportConfig = field(default_factory=ExportConfig)

    # ---- derived paths -------------------------------------------------------------
    @property
    def pdf_dir(self) -> Path:
        return self.paths.pdf_dir or (self.paths.work_dir / "pdfs")

    def venue_dir(self, venue_id: str) -> Path:
        return self.paths.work_dir / "venues" / venue_id

    @property
    def joint_dir(self) -> Path:
        return self.paths.work_dir / "joint"

    def venue(self, venue_id: str) -> VenueConfig:
        for v in self.venues:
            if v.id == venue_id:
                return v
        raise ConfigError(f"Unknown venue {venue_id!r}; configured: {[v.id for v in self.venues]}")

    def models_for(self, venue: VenueConfig) -> List[ModelSpec]:
        return venue.models or self.extraction.models

    def all_model_labels(self) -> List[str]:
        labels: List[str] = []
        for v in self.venues:
            for m in self.models_for(v):
                if m.label not in labels:
                    labels.append(m.label)
        return labels


# ---------------------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------------------

def _build(cls, data: Dict[str, Any], where: str):
    """Instantiate dataclass ``cls`` from a mapping, rejecting unknown keys."""
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise ConfigError(f"{where}: expected a mapping, got {type(data).__name__}")
    allowed = {f.name for f in fields(cls)}
    unknown = sorted(set(data) - allowed)
    if unknown:
        raise ConfigError(f"{where}: unknown key(s) {unknown}; allowed: {sorted(allowed)}")
    kwargs = {}
    for f in fields(cls):
        if f.name not in data:
            continue
        value = data[f.name]
        if f.type in ("Path", "Optional[Path]") and value is not None:
            value = Path(str(value))
        kwargs[f.name] = value
    return cls(**kwargs)


def _models(items: Any, where: str) -> List[ModelSpec]:
    if items is None:
        return []
    if not isinstance(items, list):
        raise ConfigError(f"{where}: expected a list of models")
    out: List[ModelSpec] = []
    seen = set()
    for i, m in enumerate(items):
        spec = _build(ModelSpec, m, f"{where}[{i}]")
        if spec.provider not in PROVIDERS:
            raise ConfigError(f"{where}[{i}]: provider must be one of {PROVIDERS}, got {spec.provider!r}")
        if not spec.label or not spec.label.replace("_", "").isalnum():
            raise ConfigError(f"{where}[{i}]: label {spec.label!r} must be alphanumeric/underscore (it names a directory)")
        if spec.label in seen:
            raise ConfigError(f"{where}[{i}]: duplicate model label {spec.label!r}")
        seen.add(spec.label)
        out.append(spec)
    return out


def _resolve(path: Optional[Path], base: Path) -> Optional[Path]:
    if path is None:
        return None
    path = Path(path).expanduser()
    return path if path.is_absolute() else (base / path).resolve()


def load_config(path: str | Path) -> Config:
    """Read, validate and resolve a YAML configuration file."""
    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise ConfigError(f"Config file not found: {path}")
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    if not isinstance(raw, dict):
        raise ConfigError(f"{path}: top level must be a mapping")
    return config_from_dict(raw, base_dir=path.parent, source_file=path)


def config_from_dict(raw: Dict[str, Any], base_dir: Path | None = None, source_file: Path | None = None) -> Config:
    base = Path(base_dir or Path.cwd()).resolve()
    known = {"version", "paths", "venues", "prompts", "screening", "extraction", "harmonization",
             "voting", "join", "curation", "summaries", "export"}
    unknown = sorted(set(raw) - known)
    if unknown:
        raise ConfigError(f"unknown top-level key(s) {unknown}; allowed: {sorted(known)}")

    cfg = Config(version=str(raw.get("version", "0.0.1")), source_file=source_file)
    cfg.prompts = str(raw.get("prompts", "default"))
    cfg.paths = _build(PathsConfig, raw.get("paths"), "paths")
    cfg.screening = _build(ScreeningConfig, raw.get("screening"), "screening")
    ext_raw = dict(raw.get("extraction") or {})
    models_raw = ext_raw.pop("models", None)
    cfg.extraction = _build(ExtractionConfig, ext_raw, "extraction")
    cfg.extraction.models = _models(models_raw, "extraction.models")
    cfg.harmonization = _build(HarmonizationConfig, raw.get("harmonization"), "harmonization")
    cfg.voting = _build(VotingConfig, raw.get("voting"), "voting")
    cfg.join = _build(JoinConfig, raw.get("join"), "join")
    cfg.curation = _build(CurationConfig, raw.get("curation"), "curation")
    cfg.summaries = _build(SummariesConfig, raw.get("summaries"), "summaries")
    cfg.export = _build(ExportConfig, raw.get("export"), "export")

    venues_raw = raw.get("venues") or []
    if not isinstance(venues_raw, list) or not venues_raw:
        raise ConfigError("venues: at least one venue is required")
    ids = set()
    for i, v in enumerate(venues_raw):
        v = dict(v or {})
        models_raw = v.pop("models", None)
        venue = _build(VenueConfig, v, f"venues[{i}]")
        venue.models = _models(models_raw, f"venues[{i}].models") or None
        if not venue.id or not venue.id.replace("_", "").isalnum():
            raise ConfigError(f"venues[{i}]: id {venue.id!r} must be alphanumeric/underscore")
        if venue.id in ids:
            raise ConfigError(f"venues[{i}]: duplicate id {venue.id!r}")
        ids.add(venue.id)
        if venue.source not in VENUE_SOURCES:
            raise ConfigError(f"venues[{i}]: source must be one of {VENUE_SOURCES}, got {venue.source!r}")
        if venue.source in ("pmlr", "anthology") and not venue.volume:
            raise ConfigError(f"venues[{i}] ({venue.id}): source {venue.source!r} needs a volume")
        venue.year = int(venue.year)
        venue.papers = _resolve(venue.papers, base)
        venue.trials_dir = _resolve(venue.trials_dir, base)
        cfg.venues.append(venue)

    # paths
    cfg.paths.work_dir = _resolve(cfg.paths.work_dir, base)
    cfg.paths.pdf_dir = _resolve(cfg.paths.pdf_dir, base)
    cfg.paths.log_dir = _resolve(cfg.paths.log_dir, base)
    cfg.harmonization.seed_name_mapping = _resolve(cfg.harmonization.seed_name_mapping, base)
    cfg.curation.overlay = _resolve(cfg.curation.overlay, base)
    cfg.export.site_dir = _resolve(cfg.export.site_dir, base)
    cfg.export.artifact_out = _resolve(cfg.export.artifact_out, base)

    validate(cfg)
    return cfg


def validate(cfg: Config) -> None:
    """Cross-field checks that a mapping-level build cannot express."""
    for name, section in (("screening", cfg.screening), ("harmonization", cfg.harmonization),
                          ("join", cfg.join), ("summaries", cfg.summaries)):
        if section.provider not in PROVIDERS:
            raise ConfigError(f"{name}.provider must be one of {PROVIDERS}, got {section.provider!r}")
    if cfg.screening.mode not in ("batch", "sync"):
        raise ConfigError(f"screening.mode must be 'batch' or 'sync', got {cfg.screening.mode!r}")
    if cfg.screening.enabled and cfg.screening.mode == "batch" and cfg.screening.provider != "together":
        raise ConfigError("screening.mode 'batch' runs on the Together batch API; set screening.provider to "
                          "'together' or screening.mode to 'sync'")
    if cfg.summaries.enabled and cfg.summaries.provider not in SUMMARY_PROVIDERS:
        raise ConfigError(f"summaries.provider must be one of {SUMMARY_PROVIDERS}, got {cfg.summaries.provider!r}")
    if cfg.harmonization.on_batch_failure not in ("warn", "stop"):
        raise ConfigError("harmonization.on_batch_failure must be 'warn' or 'stop'")
    if cfg.voting.survivor not in ("strictest", "majority"):
        raise ConfigError("voting.survivor must be 'strictest' or 'majority'")
    if cfg.voting.threshold < 1:
        raise ConfigError("voting.threshold must be at least 1")
    if cfg.voting.min_papers < 1:
        raise ConfigError("voting.min_papers must be at least 1")
    if cfg.summaries.min_papers < 1:
        raise ConfigError("summaries.min_papers must be at least 1")
    for v in cfg.venues:
        panel = cfg.models_for(v)
        if not panel and v.trials_dir is None:
            raise ConfigError(f"venue {v.id}: no extraction models configured (extraction.models or venues[].models)")
        if panel and len(panel) < cfg.voting.threshold:
            raise ConfigError(f"venue {v.id}: {len(panel)} model(s) cannot reach voting.threshold={cfg.voting.threshold}")
    if cfg.export.site_dir is None and cfg.export.artifact_out is None:
        raise ConfigError("export: set site_dir and/or artifact_out, or run without the export stage")
    for label, path in (("harmonization.seed_name_mapping", cfg.harmonization.seed_name_mapping),
                        ("curation.overlay", cfg.curation.overlay)):
        if path is not None and not Path(path).is_file():
            raise ConfigError(f"{label}: file not found: {path}")
    for v in cfg.venues:
        if v.sample is not None and v.sample < 1:
            raise ConfigError(f"venue {v.id}: sample must be at least 1")
        for m in cfg.models_for(v):
            if m.price is not None and (len(m.price) != 2 or any(x < 0 for x in m.price)):
                raise ConfigError(f"model {m.label}: price must be [input USD per million tokens, output USD per million tokens]")


def to_dict(obj: Any) -> Any:
    """Plain-data view of a config (for `lexis check-config`)."""
    if is_dataclass(obj):
        return {f.name: to_dict(getattr(obj, f.name)) for f in fields(obj)}
    if isinstance(obj, list):
        return [to_dict(x) for x in obj]
    if isinstance(obj, Path):
        return str(obj)
    return obj
