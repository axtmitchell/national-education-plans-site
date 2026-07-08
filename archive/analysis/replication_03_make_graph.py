#!/usr/bin/env python3
"""
Create the trilingual smart-buy income-group graph.

The default route uses the compact public label file in
data/replication/trilingual_rag_labels.csv. That makes the published figure
reproducible without re-downloading and re-processing the full Planipolis PDF
corpus.

To fully rerun the RAG classifier instead, run:

    python analysis/replication_01_clean_data.py --overwrite
    python analysis/replication_02_run_rag.py --yes-run-api
    python analysis/replication_03_make_graph.py --source replication

The --source published option is retained for the original local analysis
outputs, which are not included in this public repo.
"""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUTS = {
    "public": "data/replication/trilingual_rag_labels.csv",
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

LMIC = "Low & Middle Income"
HIC = "High Income"
PLOT_FONT = "Sofia Pro"
TEXT_DARK = "#1A272A"
FRAME_COLOR = "#1A272A"
GRID_COLOR = "#DFE0E2"
BAR_HEIGHT = 0.36
DPI = 220

CGD = {
    "teal": "#006970",
    "gold": "#FFB52C",
}

BEST_BUY_LABELS = {
    "bb_info": "Information",
    "bb_structped": "Structured Pedagogy",
    "bb_targeted": "Targeted Instruction",
    "bb_parentstim": "Child Stimulation",
    "bb_preprimary": "Preschool",
    "bb_travel": "Reduce Travel",
    "bb_merit": "Merit Scholarships",
    "bb_deworm": "Mass Deworming",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the trilingual broad RAG income graph")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--source", choices=sorted(INPUTS), default="public")
    parser.add_argument(
        "--output",
        default="figures/bb_mention_pct_by_income_rag_english_french_spanish_combined.png",
    )
    return parser.parse_args()


def income_group(series: pd.Series) -> pd.Series:
    out = pd.Series(LMIC, index=series.index)
    out.loc[series.eq("High income")] = HIC
    return out


def infer_complete_mask(df: pd.DataFrame, bb_cols: list[str]) -> pd.Series:
    if "rag_complete" in df.columns:
        return pd.to_numeric(df["rag_complete"], errors="coerce").fillna(0).eq(1)
    stage_cols = [f"{bb}_stage" for bb in bb_cols if f"{bb}_stage" in df.columns]
    if stage_cols:
        stage_filled = df[stage_cols].fillna("").astype(str).apply(lambda col: col.str.len() > 0)
        return stage_filled.all(axis=1)
    return pd.Series(True, index=df.index)


def read_inputs(project_root: Path, source: str) -> pd.DataFrame:
    required_cols = {"docid", "country", "year", "incomegroup", "rag_complete", *BEST_BUY_LABELS}
    source_spec = INPUTS[source]

    if isinstance(source_spec, str):
        path = project_root / source_spec
        if not path.exists():
            raise FileNotFoundError(
                f"Missing public label file: {path}. "
                "Download it from data/replication/ or use --source replication after rerunning RAG."
            )
        frame = pd.read_csv(path)
        missing = sorted(required_cols.difference(frame.columns))
        if missing:
            raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")
        return frame

    frames = []
    for language, rel_path in source_spec.items():
        path = project_root / rel_path
        if not path.exists():
            raise FileNotFoundError(
                f"Missing {language} input: {path}. "
                "Use --source public, or run replication_02_run_rag.py first."
            )
        frame = pd.read_stata(path, convert_categoricals=False).dropna(axis=1, how="all")
        missing = sorted(required_cols.difference(frame.columns))
        if missing:
            raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")
        frame["replication_language"] = language
        frames.append(frame)
    return pd.concat(frames, ignore_index=True, sort=False)


def prep_broad_work(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    bb_cols = [c for c in BEST_BUY_LABELS if c in df.columns]
    complete_mask = infer_complete_mask(df, bb_cols)
    work = df.loc[complete_mask].copy()
    work = work[work["incomegroup"].fillna("").ne("")].copy()
    work["income_group"] = income_group(work["incomegroup"])
    work["year_num"] = pd.to_numeric(work["year"], errors="coerce")
    work = work[work["year_num"].notna()].copy()
    for col in bb_cols:
        work[col] = pd.to_numeric(work[col], errors="coerce").fillna(0)
    return work, bb_cols


def style_axes(ax: plt.Axes) -> None:
    ax.grid(axis="x", color=GRID_COLOR, linewidth=1.0, alpha=0.8)
    ax.set_axisbelow(True)
    ax.set_facecolor("white")
    ax.tick_params(axis="both", colors=TEXT_DARK, labelsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.spines["bottom"].set_visible(True)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(FRAME_COLOR)
        ax.spines[spine].set_linewidth(1.0)
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontname(PLOT_FONT)
        tick.set_color(TEXT_DARK)


def save_grouped_bar_chart(table: pd.DataFrame, output_path: Path) -> None:
    chart = table.sort_values([LMIC, "label"], ascending=[False, True]).reset_index(drop=True)
    y = np.arange(len(chart))

    fig, ax = plt.subplots(figsize=(13, 7.6))
    ax.barh(y - BAR_HEIGHT / 2, chart[LMIC], height=BAR_HEIGHT, color=CGD["gold"], label=LMIC)
    ax.barh(y + BAR_HEIGHT / 2, chart[HIC], height=BAR_HEIGHT, color=CGD["teal"], label=HIC)

    ax.set_yticks(y)
    ax.set_yticklabels([textwrap.fill(str(x), width=24) for x in chart["label"]])
    ax.invert_yaxis()
    ax.set_xlim(0, 50)
    ax.set_xlabel("% of documents mentioning the smart buy", fontname=PLOT_FONT, fontsize=14, color=TEXT_DARK)
    style_axes(ax)

    legend = ax.legend(
        frameon=True,
        facecolor="white",
        edgecolor="white",
        loc="center right",
        bbox_to_anchor=(0.98, 0.50),
    )
    for text in legend.get_texts():
        text.set_fontname(PLOT_FONT)
        text.set_color(TEXT_DARK)
        text.set_fontsize(12)

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def build_broad_income_chart(df: pd.DataFrame, output_path: Path) -> None:
    work, bb_cols = prep_broad_work(df)
    grp = (
        work.groupby("income_group", dropna=False)[bb_cols]
        .mean()
        .mul(100)
        .transpose()
        .rename_axis("best_buy_code")
        .reset_index()
    )
    grp["label"] = grp["best_buy_code"].map(BEST_BUY_LABELS)
    table = grp[["label", LMIC, HIC]].copy()
    table[LMIC] = table.get(LMIC, 0)
    table[HIC] = table.get(HIC, 0)
    save_grouped_bar_chart(table, output_path)


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    output_path = project_root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    combined = read_inputs(project_root, args.source)
    build_broad_income_chart(combined, output_path)

    print(f"Wrote: {output_path}")
    print(f"Documents: {len(combined)}")
    print(f"Countries: {combined['country'].nunique(dropna=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
