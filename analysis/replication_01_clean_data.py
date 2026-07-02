#!/usr/bin/env python3
"""
Prepare the trilingual input files used by the smart-buy RAG replication.

This script creates one cleaned input file per language in:

    output/replication/clean/

The English sample uses the final cleaned English file from the original
analysis. French and Spanish are rebuilt from the merged Planipolis text file
using the same no-English-counterpart logic used in the published analysis.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import pandas as pd


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare trilingual RAG input files")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--output-dir", default="output/replication/clean")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def run_builder(project_root: Path, sample: str, output_path: Path) -> None:
    cmd = [
        sys.executable,
        str(project_root / "code" / "26_build_language_rag_dataset.py"),
        "--sample",
        sample,
        "--output",
        str(output_path),
    ]
    subprocess.run(cmd, cwd=project_root, check=True)


def maybe_stop_if_exists(path: Path, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Rerun with --overwrite to replace it.")


def summarize(path: Path) -> dict[str, object]:
    df = pd.read_stata(path, convert_categoricals=False)
    return {
        "file": str(path),
        "rows": len(df),
        "countries": df["country"].nunique(dropna=True),
        "year_min": int(pd.to_numeric(df["year"], errors="coerce").min()),
        "year_max": int(pd.to_numeric(df["year"], errors="coerce").max()),
    }


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    output_dir = project_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "english": output_dir / "nep_data_filtered_english.dta",
        "french": output_dir / "nep_data_filtered_french_no_english_entry.dta",
        "spanish": output_dir / "nep_data_filtered_spanish_no_english_entry.dta",
    }

    for output_path in outputs.values():
        maybe_stop_if_exists(output_path, args.overwrite)

    shutil.copy2(project_root / "output" / "nep_data_filtered.dta", outputs["english"])
    run_builder(project_root, "french_no_english_entry", outputs["french"])
    run_builder(project_root, "spanish_no_english_entry", outputs["spanish"])

    summary = pd.DataFrame([{"language": lang, **summarize(path)} for lang, path in outputs.items()])
    summary_path = output_dir / "sample_summary.csv"
    summary.to_csv(summary_path, index=False)

    print(summary.to_string(index=False))
    print(f"Wrote summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
