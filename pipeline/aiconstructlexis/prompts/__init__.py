"""Prompt sets.

The pipeline ships two prompt sets. ``aiconstructlexis.prompts.default`` is the release set:
every prompt of the released Lexis is the one it holds, except that part of the release run
extracted entities and relationships with ``aiconstructlexis.prompts.earlier``, the earlier
revision of the two extraction prompts (which venues, in docs/MODEL_CARD.md). ``earlier``
takes every other prompt from ``default``. ``load_prompts("default")`` and
``load_prompts("earlier")`` return those modules; ``load_prompts("my_package.my_prompts")``
imports any other module that defines the same constant names, so a differently prompted
pipeline can be run from the same config.
"""
from __future__ import annotations

import hashlib
import importlib
from types import ModuleType

DEFAULT_PROMPT_SET = "default"

REQUIRED_NAMES = (
    "SCREENING_PAPERS_PROMPT",
    "EXTRACT_ENTITIES_PROMPT",
    "EXTRACT_RELATIONSHIPS_PROMPT",
    "AGGREGATE_CONSTRUCTS_PROMPT",
    "AGGREGATE_MEASUREMENTS_PROMPT",
    "AGGREGATE_BEHAVIORS_PROMPT",
    "MERGE_GROUPS_PROMPT",
    "CHARACTERIZE_ENTITIES_PROMPT",
    "CHARACTERIZE_TYPE_GUIDANCE",
    "CHARACTERIZE_SECTION_LABELS",
    "build_aggregate_grouping_prompt",
)


class PromptSetError(RuntimeError):
    """A prompt set is missing or does not define the names the pipeline needs."""


def load_prompts(name: str | None = None) -> ModuleType:
    """Return the prompt module for ``name``: "default", or a dotted module path."""
    name = name or DEFAULT_PROMPT_SET
    mod_name = f"{__name__}.{name}" if "." not in name else name
    try:
        mod = importlib.import_module(mod_name)
    except ModuleNotFoundError as e:
        if e.name == mod_name:
            raise PromptSetError(f"Prompt set {name!r} ({mod_name}) cannot be imported.") from e
        raise
    missing = [n for n in REQUIRED_NAMES if not hasattr(mod, n)]
    if missing:
        raise PromptSetError(f"Prompt set {name!r} does not define: {', '.join(missing)}")
    return mod


def get_prompt(name: str | None, constant: str):
    """Return one prompt constant from a prompt set."""
    mod = load_prompts(name)
    try:
        return getattr(mod, constant)
    except AttributeError:
        raise PromptSetError(f"Prompt set {name or DEFAULT_PROMPT_SET!r} does not define {constant}") from None


def prompt_sha256(text: str, length: int = 16) -> str:
    """Short, stable fingerprint of a prompt text, recorded next to every output it produced."""
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:length]


def describe_prompt(name: str | None, constant: str) -> dict:
    """{'prompt_set', 'module', 'name', 'sha256'} for one prompt constant."""
    mod = load_prompts(name)
    text = get_prompt(name, constant)
    return {
        "prompt_set": name or DEFAULT_PROMPT_SET,
        "module": mod.__name__,
        "name": constant,
        "sha256": prompt_sha256(text if isinstance(text, str) else repr(text)),
    }
