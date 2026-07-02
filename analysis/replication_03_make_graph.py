#!/usr/bin/env python3
"""
Create the trilingual smart-buy income-group graph.

By default this uses the already completed published RAG outputs. Use
--source replication after running replication_02_run_rag.py to graph freshly
replicated labels instead.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import pandas as pd


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUTS = {
    "published": {
        "english": "output/nep_counted_llm_rag_full.dta",
        "french": "output/nep_counted_llm_rag_french_full_v1.dta",
        "spanish": "output/nep_counted_llm_rag_spanish_full_v2.dta",
    },
    "replication": {
        "english": "output/replication/rag/nep_counted_llm_rag_english.dta",
        "french": "output/replication/rag/nep_counted_llm_rag_french.dta",
        "spanish": "output/replication/rag/nep_counted_llm_rag_spanish.dta",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the trilingual broad RAG income graph")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--source", choices=sorted(INPUTS), default="published")
    parser.add_argument(
        "--output",
        default="figures/bb_mention_pct_by_income_rag_english_french_spanish_combined.png",
    )
    return parser.parse_args()


def load_blog_figure_module(project_root: Path):
    helper_path = project_root / "code" / "20_blog_figure_refresh.py"
    sys.path.insert(0, str(project_root / "code"))
    spec = importlib.util.spec_from_file_location("blog_figure_refresh", helper_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load helper module from {helper_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_inputs(project_root: Path, source: str) -> pd.DataFrame:
    frames = []
    for language, rel_path in INPUTS[source].items():
        path = project_root / rel_path
        df = pd.read_stata(path, convert_categoricals=False)
        df = df.dropna(axis=1, how="all")
        df["replication_language"] = language
        frames.append(df)
    return pd.concat(frames, ignore_index=True, sort=False)


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    output_path = project_root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    helpers = load_blog_figure_module(project_root)
    combined = read_inputs(project_root, args.source)
    helpers.build_broad_income_chart(combined, output_path)

    print(f"Wrote: {output_path}")
    print(f"Documents: {len(combined)}")
    print(f"Countries: {combined['country'].nunique(dropna=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
