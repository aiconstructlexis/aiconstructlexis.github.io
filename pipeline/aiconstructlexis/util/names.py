"""Names and orderings shared across the pipeline stages and the site.

``slugify`` must stay in step with the site's JavaScript (network_graph.js and
explorer.js compute the same slug to fetch an entity's file): "+" is spelled out
so that "HumanEval+" and "HumanEval" get different files.
"""
from __future__ import annotations

import re

ENTITY_TYPES = ("constructs", "measurements", "behaviors")
SITE_SUBDIR = {"constructs": "constructs", "measurements": "measurements", "behaviors": "behaviors_tasks"}
TYPE_SINGULAR = {"constructs": "construct", "measurements": "measurement", "behaviors": "behavior"}

# The extraction prompt's four relationship types, strictest claim first. The relationship
# vote and the pair-type consolidation both pick the strictest type by this order.
STRICTNESS = ["causes", "measured_by", "correlates", "related"]

# Where the export stage writes inside the website directory.
DATA_SUBDIR = "data"                 # entity records, graph bundle, paper URLs, analysis bundle, layout
READABLE_SUBDIR = "data/readable"    # Markdown mirror of the entity records
LAYOUT_SUBDIR = "data"               # layout.json of the interactive network


def slugify(name: str) -> str:
    """File-name slug of a canonical entity name."""
    s = (name or "").strip().lower().replace("+", "_plus_")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "unknown"
