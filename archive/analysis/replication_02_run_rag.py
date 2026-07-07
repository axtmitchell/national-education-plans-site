#!/usr/bin/env python3
"""
Run the smart-buy RAG classifier for the cleaned trilingual input files.

This script calls the production classifier once per language and writes labels,
caches, logs, review samples, and cost summaries under:

    output/replication/rag/

Because this step uses the OpenAI API, it prints the planned commands unless
--yes-run-api is supplied.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]

RUNS = {
    "english": {
        "input": "output/replication/clean/nep_data_filtered_english.dta",
        "output": "output/replication/rag/nep_counted_llm_rag_english.dta",
        "budget": "6.0",
        "config": None,
    },
    "french": {
        "input": "output/replication/clean/nep_data_filtered_french_no_english_entry.dta",
        "output": "output/replication/rag/nep_counted_llm_rag_french.dta",
        "budget": "5.0",
        "config": "code/best_buy_configs/french_rag_v1.py",
    },
    "spanish": {
        "input": "output/replication/clean/nep_data_filtered_spanish_no_english_entry.dta",
        "output": "output/replication/rag/nep_counted_llm_rag_spanish.dta",
        "budget": "3.0",
        "config": "code/best_buy_configs/spanish_rag_v2.py",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run trilingual smart-buy RAG labels")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--languages", nargs="+", choices=sorted(RUNS), default=sorted(RUNS))
    parser.add_argument("--yes-run-api", action="store_true", help="Actually run API calls")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def command_for(project_root: Path, language: str) -> list[str]:
    run = RUNS[language]
    output = project_root / run["output"]
    stem = output.with_suffix("")
    cmd = [
        sys.executable,
        str(project_root / "code" / "14_llm_rag_classify.py"),
        "--input",
        str(project_root / run["input"]),
        "--output",
        str(output),
        "--cache",
        str(stem.with_name(stem.name + "_cache.jsonl")),
        "--logs",
        str(stem.with_name(stem.name + "_logs.jsonl")),
        "--limit",
        "0",
        "--budget-usd",
        run["budget"],
        "--review-csv",
        str(stem.with_name(stem.name + "_review.csv")),
        "--review-per-bb",
        "8",
        "--checkpoint-every",
        "25",
    ]
    if run["config"]:
        cmd.extend(["--config-py", str(project_root / run["config"])])
    return cmd


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    (project_root / "output" / "replication" / "rag").mkdir(parents=True, exist_ok=True)

    commands = []
    for language in args.languages:
        output = project_root / RUNS[language]["output"]
        if output.exists() and not args.overwrite:
            print(f"Skipping {language}: {output} already exists. Use --overwrite to rerun.")
            continue
        commands.append((language, command_for(project_root, language)))

    if not commands:
        return 0

    for language, cmd in commands:
        print(f"\n[{language}]")
        print(" ".join(f"'{part}'" if " " in part else part for part in cmd))

    if not args.yes_run_api:
        print("\nDry run only. Rerun with --yes-run-api after checking OPENAI_API_KEY is set.")
        return 0

    for language, cmd in commands:
        print(f"\nRunning {language}...")
        subprocess.run(cmd, cwd=project_root, check=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
