"""Packing entity names into LLM batches by token signature.

When N entity names are handed to an LLM in batches of size B, names that are surface
variants of each other, or that share a head noun, should land in the same batch so the
model sees the full set of merge candidates for a concept at once. Nothing here decides a
merge: the batches only determine what the model sees together.

No embeddings, no LLM calls:

1. Each name is reduced to a token signature: lowercased, hyphen-normalized, filler
   tokens dropped (ability/capability/capacity/skill/proficiency/performance, singular and
   plural), plurals stemmed, synonyms folded (comprehension/awareness -> understanding,
   identification -> recognition) and morphology folded (logical -> logic,
   mathematical -> math, multi/cross/x-modal -> multimodal).
2. Names with an identical signature form one group.
3. Groups are packed into batches with first-fit decreasing: large groups first, smaller
   groups fill the remaining space. A group larger than batch_size is split into
   consecutive batches.
4. Within each batch the names are sorted by (head noun, first token, signature), so
   thematic neighbours that are not surface variants ("Reasoning", "Mathematical
   reasoning") sit next to each other.

``make_batches(names, batch_size)`` returns a list of batches, each a list of indices into
``names``; the harmonization and join stages iterate these batches directly.
"""
from __future__ import annotations

import re
from collections import defaultdict
from typing import List, Sequence


# ---------------------------------------------------------------- token normalization

_UNICODE_HYPHENS = "‐‑‒–—―−"

_FILLER_TOKENS = {
    "ability", "abilities",
    "capability", "capabilities",
    "capacity", "capacities",
    "skill", "skills",
    "proficiency", "proficiencies",
    "performance",
}

_STOPWORDS = {"a", "an", "the", "of", "to", "for", "in", "on", "with", "by", "and", "or"}

_SYNONYM_REPLACE = {
    "comprehension": "understanding",
    "awareness": "understanding",
    "identification": "recognition",
    "logical": "logic",
    "numerical": "numeric",
    "mathematical": "math",
}


def _stem_plural(word: str) -> str:
    if len(word) > 3 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("ses"):
        return word[:-2]
    if len(word) > 1 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _normalize_to_tokens(name: str) -> List[str]:
    """Return the ordered list of content tokens for a name."""
    if not name:
        return []
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    # Treat hyphens, slashes, underscores as spaces. Drop other punctuation.
    s = re.sub(r"[-_/]", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    # Collapse "multi modal" / "cross modal" / "x modal" -> "multimodal"
    s = re.sub(r"\b(multi|cross|x)\s+modal\b", "multimodal", s)
    # Collapse "vis(io|ual) linguistic" -> "vision language"
    s = re.sub(r"\b(visio|visual)\s+linguistic\b", "vision language", s)
    raw_tokens = [t for t in s.split() if t]
    out: List[str] = []
    for t in raw_tokens:
        if t in _STOPWORDS or t in _FILLER_TOKENS:
            continue
        # Stem plurals
        t = _stem_plural(t)
        # Synonym/morphology folding
        t = _SYNONYM_REPLACE.get(t, t)
        out.append(t)
    return out


def signature(name: str) -> str:
    """Order-independent normalized signature; names sharing this signature are
    surface variants of the same concept."""
    return " ".join(sorted(set(_normalize_to_tokens(name))))


def head_noun(name: str) -> str:
    """The 'thematic family' key: last content token after normalization."""
    toks = _normalize_to_tokens(name)
    return toks[-1] if toks else ""


# ---------------------------------------------------------------- signature groups


def group_by_token_signature(names: Sequence[str]) -> List[int]:
    """Return a list of group ids parallel to `names`.

    Two names share a group only when they have an identical normalized token
    signature. This catches true surface variants (e.g. "Reasoning ability" /
    "Reasoning capabilities" / "Reasoning skills" all reduce to the signature
    `reasoning`) without building transitive mega-groups through common head nouns.
    A name with an empty signature is a group of its own.

    Broader thematic locality (putting all "X reasoning" or all "Hallucination X"
    items next to each other) is left to the batch packing, which sorts the items of
    a batch by head noun and first token.
    """
    first_index: dict[str, int] = {}
    ids: List[int] = []
    for i, nm in enumerate(names):
        sig = signature(nm)
        ids.append(first_index.setdefault(sig, i) if sig else i)
    return ids


def _sort_key(name: str) -> tuple:
    """Sort key that keeps thematically related names adjacent.

    Order: head noun, first content token, normalized signature, raw name.
    With this ordering, all items ending in "reasoning" form one block, and within
    that block items starting with the same modifier are adjacent ("Mathematical
    reasoning" near "Multi-step reasoning"; "Hallucination" is adjacent to
    "Hallucination resistance" via first-token).
    """
    toks = _normalize_to_tokens(name)
    if not toks:
        return ("", "", "", name.lower())
    head = toks[-1]
    first = toks[0]
    sig = " ".join(sorted(set(toks)))
    return (head, first, sig, name.lower())


# ---------------------------------------------------------------- batch packing


def pack_groups_into_batches(
    group_ids: Sequence[int],
    batch_size: int,
    min_batch_size: int = 0,
) -> List[List[int]]:
    """Pack name indices into batches that keep each signature group together.

    Strategy: bucket the indices by group id, sort the groups from largest to
    smallest, then run first-fit-decreasing into bins of capacity batch_size.
    Groups bigger than batch_size are split into chunks of batch_size each (those
    chunks stay together in their own batches).

    Args:
      group_ids:   parallel array of group id per name
      batch_size:  target/maximum batch size
      min_batch_size: pack tiny groups together to avoid sub-min batches

    Returns:
      list of batches; each batch is a list of name indices.
    """
    if not group_ids:
        return []

    # Bucket name indices by group id, preserving original order within a group
    by_group: dict[int, list[int]] = defaultdict(list)
    for i, g in enumerate(group_ids):
        by_group[g].append(i)
    groups: list[list[int]] = sorted(
        by_group.values(), key=lambda g: -len(g)
    )

    batches: list[list[int]] = []
    pending: list[list[int]] = []  # small groups waiting to fill a batch

    for group in groups:
        if len(group) >= batch_size:
            # Big group: split into contiguous chunks of batch_size
            for start in range(0, len(group), batch_size):
                batches.append(group[start : start + batch_size])
            continue
        # Small/medium group: try to combine with pending small groups
        pending.append(group)
        # Greedy: fill a batch from pending whenever it would overflow
        running = sum(len(g) for g in pending)
        if running >= batch_size:
            # Pack pending using FFD
            pending.sort(key=lambda g: -len(g))
            current: list[int] = []
            leftover: list[list[int]] = []
            for g in pending:
                if len(current) + len(g) <= batch_size:
                    current.extend(g)
                else:
                    leftover.append(g)
            if current:
                batches.append(current)
            pending = leftover

    # Flush remaining pending groups
    if pending:
        pending.sort(key=lambda g: -len(g))
        current: list[int] = []
        for g in pending:
            if len(current) + len(g) <= batch_size:
                current.extend(g)
            else:
                if current:
                    batches.append(current)
                current = list(g)
        if current:
            batches.append(current)

    # Optional: combine tail batches that are below min_batch_size
    if min_batch_size and len(batches) >= 2:
        merged: list[list[int]] = []
        for b in batches:
            if merged and len(merged[-1]) < min_batch_size and \
               len(merged[-1]) + len(b) <= batch_size:
                merged[-1].extend(b)
            else:
                merged.append(b)
        batches = merged

    return batches


def make_batches(names: Sequence[str], batch_size: int,
                 min_batch_size: int = 0) -> List[List[int]]:
    """Build batches that put thematically related names together.

    Two-phase strategy:
      1. Group by exact normalized signature (surface variants): small tight
         groups; pack these into batches first using FFD so each signature group
         stays intact in a single batch.
      2. Within the assembled batches, *sort* by (head_noun, first_token,
         signature) so adjacent batch items are thematically related even
         when they aren't surface variants of each other.

    The two phases together: surface variants are guaranteed in the same
    batch (phase 1), and broader thematic neighbours are co-located within
    each batch (phase 2 sort).
    """
    group_ids = group_by_token_signature(names)
    raw_batches = pack_groups_into_batches(group_ids, batch_size, min_batch_size)
    # Phase 2: sort indices within each batch by thematic locality
    sorted_batches: List[List[int]] = []
    for batch in raw_batches:
        sorted_batch = sorted(batch, key=lambda i: _sort_key(names[i]))
        sorted_batches.append(sorted_batch)
    return sorted_batches


def main(argv=None) -> int:
    """Print the batches for a list of names (a JSON list, or one name per line)."""
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Pack entity names into batches that keep surface variants and "
                    "thematic neighbours together."
    )
    parser.add_argument("names_file", help="JSON list of names, or a text file with one name per line")
    parser.add_argument("--batch-size", type=int, default=100, help="Maximum names per batch (default: 100)")
    args = parser.parse_args(argv)

    text = open(args.names_file, encoding="utf-8").read()
    try:
        names = json.loads(text)
        if not isinstance(names, list):
            raise ValueError("expected a JSON list of names")
    except json.JSONDecodeError:
        names = [line.strip() for line in text.splitlines() if line.strip()]

    for i, batch in enumerate(make_batches(names, batch_size=args.batch_size)):
        print(json.dumps({"batch": i, "names": [names[j] for j in batch]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
