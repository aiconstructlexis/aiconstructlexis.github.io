"""Precompute the layout of the interactive network page (network_graph.html).

Reads the graph the site export writes (``<site_dir>/data/graph.bundle.json``)
and writes ``<site_dir>/data/layout.json`` with two kinds of layout:

- Levels ("50", "150"): the N most-cited entities that have relationships, laid out with
  ForceAtlas2 and then spread so their labels do not overlap. The page opens on the
  smallest level, where every name is readable at a glance.
- The full map: communities (Louvain), ForceAtlas2 (LinLog mode, then a short anti-overlap
  pass), community labels, and shelves for small groups and entities with no relationships.

The page loads the bundle for content (names, definitions, edges) and this file for
positions only, so rerun this stage whenever the bundle changes. The page still opens with
a stale layout: entities missing from it are placed next to their neighbors and a note says so.

The output is deterministic for a given input, seed and parameters. Requires numpy and
networkx >= 3.0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import math
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import networkx as nx
import numpy as np
from aiconstructlexis.util.names import DATA_SUBDIR, LAYOUT_SUBDIR

logger = logging.getLogger(__name__)

SCHEMA = "lexis-graph-layout/1"
GENERATOR = "aiconstructlexis.export.graph_layout"
TYPE_ORDER = ["construct", "behavior", "measurement"]


def node_key(node: dict) -> str:
    """Entities are keyed by ``id`` when the bundle provides one, otherwise by name."""
    return str(node.get("id") or node["name"])


def layout_size(paper_count: int) -> float:
    """Node radius in layout units, roughly proportional to the rendered size."""
    return 1.0 + 1.1 * math.sqrt(max(paper_count, 1))


# --------------------------------------------------------------------------- #
# ForceAtlas2 (Jacomy et al. 2014), O(n^2) repulsion in row blocks.
# Fine for a few thousand nodes; memory stays bounded by the block size.
# --------------------------------------------------------------------------- #
def forceatlas2(pos, src, dst, weight, mass, size, *, iterations, scaling, gravity,
                linlog, adjust_sizes, community=None, community_pull=0.0, block=512):
    n = len(pos)
    prev = np.zeros_like(pos)
    speed, speed_eff = 1.0, 1.0
    mm_all = mass
    for _ in range(iterations):
        force = np.zeros_like(pos)

        # Repulsion: kr * (deg_i + 1)(deg_j + 1) / d
        for s in range(0, n, block):
            e = min(s + block, n)
            d = pos[s:e, None, :] - pos[None, :, :]
            dist = np.sqrt((d ** 2).sum(-1))
            mm = mm_all[s:e, None] * mm_all[None, :]
            with np.errstate(divide="ignore", invalid="ignore"):
                if adjust_sizes:
                    eff = dist - size[s:e, None] - size[None, :]
                    f = np.where(eff > 0, scaling * mm / (eff * dist), 100.0 * scaling * mm / dist)
                else:
                    f = scaling * mm / (dist ** 2)
            f[~np.isfinite(f)] = 0.0
            rows = np.arange(s, e)
            f[rows - s, rows] = 0.0
            force[s:e] += (d * f[..., None]).sum(1)

        # Attraction along edges (linear, or log for LinLog).
        d = pos[src] - pos[dst]
        dist = np.sqrt((d ** 2).sum(-1))
        if adjust_sizes:
            dist = np.maximum(dist - size[src] - size[dst], 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            if linlog:
                raw = np.sqrt((d ** 2).sum(-1))
                f = -weight * np.log1p(dist) / raw
            else:
                f = -weight * (dist > 0)
        f[~np.isfinite(f)] = 0.0
        np.add.at(force, src, d * f[:, None])
        np.add.at(force, dst, -d * f[:, None])

        # Gravity toward the origin.
        r = np.sqrt((pos ** 2).sum(-1))
        with np.errstate(divide="ignore", invalid="ignore"):
            g = np.where(r > 0, gravity * mass / r, 0.0)
        force -= pos * g[:, None]

        # Optional pull toward the community centroid (keeps clusters compact).
        if community is not None and community_pull > 0:
            k = community.max() + 1
            cnt = np.bincount(community, minlength=k).astype(float)
            cx = np.bincount(community, weights=pos[:, 0], minlength=k) / np.maximum(cnt, 1)
            cy = np.bincount(community, weights=pos[:, 1], minlength=k) / np.maximum(cnt, 1)
            cen = np.stack([cx, cy], 1)[community]
            force -= community_pull * mass[:, None] * (pos - cen)

        # Adaptive speed (Gephi's swing / traction rule).
        swinging = mass * np.sqrt(((force - prev) ** 2).sum(-1))
        traction = 0.5 * mass * np.sqrt(((force + prev) ** 2).sum(-1))
        tot_swing, tot_traction = swinging.sum(), traction.sum()
        opt_jitter = 0.05 * math.sqrt(n)
        jitter = max(math.sqrt(opt_jitter), min(10.0, opt_jitter * tot_traction / n ** 2))
        if tot_traction > 0 and tot_swing / tot_traction > 2.0:
            if speed_eff > 0.05:
                speed_eff *= 0.5
            jitter = max(jitter, 1.0)
        target = jitter * speed_eff * tot_traction / tot_swing if tot_swing > 0 else speed
        if tot_swing > jitter * tot_traction:
            if speed_eff > 0.05:
                speed_eff *= 0.7
        elif speed < 1000:
            speed_eff *= 1.3
        speed = speed + min(target - speed, 0.5 * speed)

        if adjust_sizes:
            df = np.sqrt((force ** 2).sum(-1))
            factor = 0.1 * speed / (1.0 + np.sqrt(speed * swinging))
            with np.errstate(divide="ignore", invalid="ignore"):
                factor = np.where(df > 0, np.minimum(factor * df, 10.0) / df, 0.0)
        else:
            factor = speed / (1.0 + np.sqrt(speed * swinging))
        pos += force * factor[:, None]
        prev = force
    return pos


def principal_axis_align(pos):
    """Rotate so the long axis is horizontal (screens are wide); fix the sign deterministically."""
    c = pos - pos.mean(0)
    _, vecs = np.linalg.eigh(np.cov(c.T))
    rot = vecs[:, ::-1]
    out = c @ rot
    for k in range(2):  # skew toward positive so reruns do not mirror
        if (out[:, k] ** 3).sum() < 0:
            out[:, k] *= -1
    return out


def place_shelf(keys, nodes_by_key, top, width, spacing):
    """Entities with no relationships: one block per entity type, side by side under the map,
    filled row by row with the most-cited first. Returns positions and a label anchor per block."""
    out, shelves = {}, []
    by_type = defaultdict(list)
    for k in keys:
        by_type[nodes_by_key[k].get("type", "construct")].append(k)
    types = [t for t in TYPE_ORDER + sorted(set(by_type) - set(TYPE_ORDER)) if by_type.get(t)]
    if not types:
        return out, shelves
    gap = spacing * 3
    usable = width - gap * (len(types) - 1)
    total = sum(len(by_type[t]) for t in types)
    x = -width / 2
    for t in types:
        members = sorted(by_type[t], key=lambda k: (-nodes_by_key[k].get("paper_count", 0), k))
        block_w = max(spacing * 4, usable * len(members) / total)
        cols = max(1, int(block_w / spacing))
        for i, k in enumerate(members):
            out[k] = (x + (i % cols + 0.5) * spacing, top - (i // cols + 0.5) * spacing)
        shelves.append({"type": t, "count": len(members), "x": round(x, 1), "y": round(top + spacing * 0.9, 1)})
        x += block_w + gap
    return out, shelves


LEVELS = (50, 150)
LEVEL_BOX = (900.0, 600.0)   # target width and height in screen pixels for the smallest level


def label_font_px(radius: float) -> float:
    """Matches labelFontSize() in network_graph.js."""
    return 11 + min(4.5, radius / 5)


def level_radius(paper_count: int, n: int) -> float:
    """Node radius in screen pixels at a level; matches levelNodeSize() in network_graph.js."""
    return min(4.0 + 0.55 * math.sqrt(max(paper_count, 1)), 18.0) if n <= 60 else \
        min(3.0 + 0.45 * math.sqrt(max(paper_count, 1)), 15.0)


def level_layout(keys, nodes_by_key, pair_w, seed):
    """ForceAtlas2 on the induced subgraph, then push label boxes apart.

    Works in screen pixels: each node is a box covering its circle and its label to the
    right. Each round rescales the two axes toward the target box (more area for bigger
    levels) and removes overlaps, so the layout keeps a screen-like aspect instead of
    growing into a tall column."""
    n = len(keys)
    idx = {k: i for i, k in enumerate(keys)}
    pairs = [(idx[a], idx[b], w) for (a, b), w in pair_w.items() if a in idx and b in idx]
    src = np.array([a for a, b, w in pairs], dtype=np.int64)
    dst = np.array([b for a, b, w in pairs], dtype=np.int64)
    weight = np.array([w for a, b, w in pairs])
    mass = 1.0 + np.bincount(np.concatenate([src, dst]), minlength=n)
    radius = np.array([level_radius(nodes_by_key[k].get("paper_count", 1), n) for k in keys])
    width = np.array([0.55 * label_font_px(r) * len(nodes_by_key[k]["name"]) for k, r in zip(keys, radius)])
    pos = np.random.default_rng(seed).normal(0, 100.0, size=(n, 2))
    pos = forceatlas2(pos, src, dst, weight, mass, radius, iterations=600, scaling=10.0, gravity=1.0,
                      linlog=False, adjust_sizes=False)
    pos = principal_axis_align(pos)
    grow = math.sqrt(n / LEVELS[0])
    box_w, box_h = LEVEL_BOX[0] * grow, LEVEL_BOX[1] * grow

    def boxes(p):
        half_h = np.maximum(radius, 9.0) + 3.0
        return np.stack([p[:, 0] - radius - 3, p[:, 1] - half_h, p[:, 0] + radius + 5 + width + 3, p[:, 1] + half_h], 1)

    for _ in range(12):
        b = boxes(pos)
        extent = np.array([b[:, 2].max() - b[:, 0].min(), b[:, 3].max() - b[:, 1].min()])
        pos = (pos - pos.mean(0)) * (np.array([box_w, box_h]) / extent) ** 0.6
        for _ in range(300):
            b = boxes(pos)
            ox = np.minimum(b[:, None, 2], b[None, :, 2]) - np.maximum(b[:, None, 0], b[None, :, 0])
            oy = np.minimum(b[:, None, 3], b[None, :, 3]) - np.maximum(b[:, None, 1], b[None, :, 1])
            overlap = (ox > 0) & (oy > 0)
            np.fill_diagonal(overlap, False)
            if not overlap.any():
                break
            cx, cy = (b[:, 0] + b[:, 2]) / 2, (b[:, 1] + b[:, 3]) / 2
            sx = np.sign(cx[:, None] - cx[None, :] + 1e-9)
            sy = np.sign(cy[:, None] - cy[None, :] + 1e-9)
            along_x = overlap & (ox * 0.6 < oy)
            along_y = overlap & ~(ox * 0.6 < oy)
            pos[:, 0] += np.where(along_x, sx * ox / 2, 0).sum(1) * 0.5
            pos[:, 1] += np.where(along_y, sy * oy / 2, 0).sum(1) * 0.5
    pos -= pos.mean(0)
    return {k: (round(float(pos[i, 0]), 1), round(float(pos[i, 1]), 1)) for i, k in enumerate(keys)}


def build_graph_layout(site_dir: str | Path, seed: int = 7, iterations: int = 400, scaling: float = 2.0,
                       gravity: float = 1.0, community_pull: float = 0.0012, resolution: float = 1.0,
                       min_labeled_community: int = 12, max_label_spread: float = 12.0,
                       input_json: str | Path | None = None, output_json: str | Path | None = None) -> Dict[str, Any]:
    """Compute the layout of ``<site_dir>/data/graph.bundle.json`` and write
    ``<site_dir>/data/layout.json``.

    ``iterations``, ``scaling`` and ``gravity`` drive the main ForceAtlas2 pass;
    ``community_pull`` adds attraction toward each community's centroid (0 = plain
    ForceAtlas2); ``resolution`` is the Louvain resolution. Communities smaller than
    ``min_labeled_community``, or whose mean distance from their centroid divided by
    sqrt(size) exceeds ``max_label_spread``, get no map label (the main component spans
    [-1000, 1000]). ``input_json`` / ``output_json`` override the two default paths.
    Returns the layout dictionary that was written.
    """
    site = Path(site_dir)
    in_path = Path(input_json) if input_json else site / DATA_SUBDIR / "graph.bundle.json"
    out_path = Path(output_json) if output_json else site / LAYOUT_SUBDIR / "layout.json"

    t0 = time.time()
    raw = in_path.read_bytes()
    bundle = json.loads(raw)
    nodes = bundle["nodes"]
    nodes_by_key = {node_key(n): n for n in nodes}
    name_to_key = {n["name"]: node_key(n) for n in nodes}

    # Undirected weighted graph; parallel edges (several types or both directions) are summed.
    pair_w = Counter()
    for e in bundle["edges"]:
        a, b = name_to_key.get(e["source"]), name_to_key.get(e["target"])
        if a is None or b is None or a == b:
            continue
        pair_w[tuple(sorted((a, b)))] += 1.0 + math.log(max(e.get("paper_count", 1), 1))
    G = nx.Graph()
    for (a, b), w in pair_w.items():
        G.add_edge(a, b, weight=w)
    connected = sorted(G.nodes, key=lambda k: (-nodes_by_key[k].get("paper_count", 0), k))
    isolates = sorted(set(nodes_by_key) - set(connected))

    # Communities. Louvain with a fixed seed is deterministic.
    comms = nx.community.louvain_communities(G, weight="weight", resolution=resolution, seed=seed)
    comms = sorted(comms, key=lambda c: (-len(c), min(c)))
    comm_of = {k: i for i, c in enumerate(comms) for k in c}

    # ForceAtlas2 on the largest component. LinLog mode separates regions; a light pull toward
    # each community's centroid keeps them legible as areas on the map.
    components = sorted(nx.connected_components(G), key=lambda c: (-len(c), min(c)))
    giant = sorted(components[0], key=lambda k: (-nodes_by_key[k].get("paper_count", 0), k))
    H = G.subgraph(giant)
    idx = {k: i for i, k in enumerate(giant)}
    n = len(giant)
    src = np.array([idx[a] for a, b in H.edges], dtype=np.int64)
    dst = np.array([idx[b] for a, b in H.edges], dtype=np.int64)
    weight = np.array([H[a][b]["weight"] for a, b in H.edges])
    mass = np.array([H.degree(k) + 1.0 for k in giant])
    size = np.array([layout_size(nodes_by_key[k].get("paper_count", 1)) for k in giant])
    community = np.array([comm_of[k] for k in giant], dtype=np.int64)

    # Seeded start: each community around its own point on a circle (fast, stable convergence).
    rng = np.random.default_rng(seed)
    k = len(comms)
    angles = np.array([2 * math.pi * i / max(k, 1) for i in range(k)])
    radii = np.array([300.0 * math.sqrt(1 + i) for i in range(k)])
    centers = np.stack([np.cos(angles) * radii, np.sin(angles) * radii], 1)
    pos = centers[community] + rng.normal(0, 50.0, size=(n, 2))

    t1 = time.time()
    fa2 = dict(scaling=scaling, gravity=gravity, linlog=True, community=community)
    pos = forceatlas2(pos, src, dst, weight, mass, size, iterations=iterations,
                      adjust_sizes=False, community_pull=community_pull, **fa2)
    pos = forceatlas2(pos, src, dst, weight, mass, size, iterations=max(50, iterations // 4),
                      adjust_sizes=True, community_pull=community_pull / 2, **fa2)
    t2 = time.time()
    pos = principal_axis_align(pos)

    # Normalize: the main component fits in [-1000, 1000] on its long axis.
    pos *= 1000.0 / max(np.abs(pos).max(), 1e-9)
    positions = {key: (float(pos[i, 0]), float(pos[i, 1])) for i, key in enumerate(giant)}

    # Small components: a compact grid of tight rings under the main component.
    ymin = float(pos[:, 1].min())
    small = components[1:]
    cell = 56.0
    cols = max(1, math.ceil(math.sqrt(len(small) * 4)))
    grid_top = ymin - 70.0
    for j, comp in enumerate(small):
        members = sorted(comp, key=lambda m: (-nodes_by_key[m].get("paper_count", 0), m))
        cx = (j % cols - (min(cols, len(small)) - 1) / 2) * cell
        cy = grid_top - (j // cols) * cell
        r = 3.0 + 3.5 * len(members)
        for i, m in enumerate(members):
            t = math.pi / 2 + 2 * math.pi * i / len(members)
            positions[m] = (cx + r * math.cos(t), cy + r * math.sin(t))
    rows = math.ceil(len(small) / cols) if small else 0
    small_groups = {"count": len(small), "x": 0.0, "y": round(grid_top + cell * 0.55, 1)} if small else None
    # Entities without relationships: a shelf below that (hidden on the page by default).
    shelf_pos, shelves = place_shelf(isolates, nodes_by_key, top=grid_top - rows * cell - 60.0,
                                     width=2000.0, spacing=26.0)
    positions.update(shelf_pos)

    # Levels: the N most-cited entities with relationships (ties broken by name).
    ranked = sorted(connected, key=lambda k: (-nodes_by_key[k].get("paper_count", 0), k))
    t3 = time.time()
    levels = {str(n): level_layout(ranked[:n], nodes_by_key, pair_w, seed) for n in LEVELS if n < len(ranked)}
    t4 = time.time()

    # Community summaries. A region is named by its two most-cited constructs or behavioral
    # indicators (instruments only as a fallback), so a label describes the area rather than
    # implying one entity owns it.
    communities = []
    for i, c in enumerate(comms):
        members = sorted(c, key=lambda m: (-nodes_by_key[m].get("paper_count", 0), m))
        concepts = [m for m in members if nodes_by_key[m].get("type") != "measurement"]
        names = [nodes_by_key[m]["name"] for m in (concepts or members)[:2]]
        pts = np.array([positions[m] for m in members])
        w = np.array([math.sqrt(max(nodes_by_key[m].get("paper_count", 1), 1)) for m in members])
        cx, cy = (pts * w[:, None]).sum(0) / w.sum()
        spread = float(np.sqrt(((pts - [cx, cy]) ** 2).sum(-1)).mean())
        # Label anchor: the mean of the densest quarter of members, so the label sits on the
        # region's core even when the community has outliers elsewhere on the map.
        dist = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(-1))
        dens = (dist < 0.35 * np.median(dist) + 1e-9).sum(1)
        core = pts[dens >= np.quantile(dens, 0.75)]
        ax, ay = core.mean(0)
        types = Counter(nodes_by_key[m].get("type") for m in members)
        # Scattered communities would put a label over empty space or someone else's region.
        labeled = (len(members) >= min_labeled_community
                   and spread / math.sqrt(len(members)) <= max_label_spread)
        communities.append({
            "id": i,
            "label": " \u00b7 ".join(names) if labeled else None,
            "size": len(members),
            "x": round(float(ax), 1),
            "y": round(float(ay), 1),
            "spread": round(spread, 1),
            "types": {t: types.get(t, 0) for t in TYPE_ORDER},
            "top": [nodes_by_key[m]["name"] for m in members[:6]],
        })

    try:
        source_path = str(in_path.resolve().relative_to(site.resolve()))
    except ValueError:
        source_path = in_path.name
    out = {
        "schema": SCHEMA,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": GENERATOR,
        "source": {
            "path": source_path,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "node_count": len(nodes),
            "edge_count": len(bundle["edges"]),
        },
        "params": {
            "seed": seed, "iterations": iterations, "louvain_resolution": resolution,
            "scaling": scaling, "gravity": gravity, "community_pull": community_pull,
            "algorithm": "Louvain communities; ForceAtlas2 LinLog with community pull, then anti-overlap",
            "edge_weight": "sum over relationship types of 1 + ln(paper_count)",
        },
        "key": "id" if any("id" in nd for nd in nodes) else "name",
        "isolated_count": len(isolates),
        # level -> key -> [x, y] in screen pixels at the intended zoom (page scales them to fit)
        "levels": {n: {k: [x, y] for k, (x, y) in lv.items()} for n, lv in levels.items()},
        "shelves": shelves,
        "small_groups": small_groups,
        "communities": communities,
        # key -> [x, y, community id or -1 for entities with no relationships]
        "nodes": {key: [round(x, 1), round(y, 1), comm_of.get(key, -1)] for key, (x, y) in positions.items()},
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))

    labeled = [c for c in communities if c["label"]]
    logger.info("%d entities (%d connected, %d without relationships), %d linked pairs",
                len(nodes), len(connected), len(isolates), G.number_of_edges())
    logger.info("%d communities, %d labeled; largest: %s", len(comms), len(labeled),
                ", ".join(f"{c['label']} ({c['size']})" for c in labeled[:8]))
    logger.info("levels %s in %.1fs; map layout %.1fs; total %.1fs -> %s",
                ", ".join(levels), t4 - t3, t2 - t1, time.time() - t0, out_path)
    return out


def main(argv: List[str] | None = None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    ap = argparse.ArgumentParser(description="Precompute the layout of the interactive network page.")
    ap.add_argument("--site", type=Path, required=True,
                    help="site directory: reads data/graph.bundle.json, writes data/layout.json")
    ap.add_argument("--input", type=Path, default=None, help="override the input graph bundle")
    ap.add_argument("--output", type=Path, default=None, help="override the output layout file")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--iterations", type=int, default=400, help="main ForceAtlas2 iterations")
    ap.add_argument("--scaling", type=float, default=2.0, help="ForceAtlas2 repulsion (scaling ratio)")
    ap.add_argument("--gravity", type=float, default=1.0, help="ForceAtlas2 gravity")
    ap.add_argument("--community-pull", type=float, default=0.0012,
                    help="extra attraction toward the community centroid (0 = plain ForceAtlas2)")
    ap.add_argument("--resolution", type=float, default=1.0, help="Louvain resolution")
    ap.add_argument("--min-labeled-community", type=int, default=12,
                    help="communities smaller than this get no map label")
    ap.add_argument("--max-label-spread", type=float, default=12.0,
                    help="communities whose mean distance from their centroid, divided by sqrt(size), "
                         "exceeds this get no label (the main component spans [-1000, 1000])")
    ap.add_argument("--log-dir", default="logs")
    args = ap.parse_args(argv)
    setup_logging(run_name="export_graph_layout", log_dir=args.log_dir)
    build_graph_layout(args.site, seed=args.seed, iterations=args.iterations, scaling=args.scaling,
                       gravity=args.gravity, community_pull=args.community_pull, resolution=args.resolution,
                       min_labeled_community=args.min_labeled_community, max_label_spread=args.max_label_spread,
                       input_json=args.input, output_json=args.output)


if __name__ == "__main__":
    main()
