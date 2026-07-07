#!/usr/bin/env python3
"""
Create the structured pedagogy and targeted instruction country-year graphs.

Run this after the replication RAG step:

    python analysis/replication_01_clean_data.py --overwrite
    python analysis/replication_02_run_rag.py --yes-run-api
    python analysis/replication_04_make_sp_tarl_country_graphs.py --source replication

By default, the script uses the already completed published RAG outputs so the
figures can be recreated without rerunning the API classifier.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]
LMIC = "Low & Middle Income"
DPI = 220

PLOT_FONT = "Sofia Pro"
TEXT_DARK = "#000000"
GRID_COLOR = "#DFE0E2"
FRAME_COLOR = "#5B666A"

INPUTS = {
    "published": {
        "English": "output/nep_counted_llm_rag_full.dta",
        "French": "output/nep_counted_llm_rag_french_full_v1.dta",
        "Spanish": "output/nep_counted_llm_rag_spanish_full_v2.dta",
    },
    "replication": {
        "English": "output/replication/rag/nep_counted_llm_rag_english.dta",
        "French": "output/replication/rag/nep_counted_llm_rag_french.dta",
        "Spanish": "output/replication/rag/nep_counted_llm_rag_spanish.dta",
    },
}

TOPICS = {
    "bb_structped": {
        "name": "Structured pedagogy",
        "slug": "structped",
        "title": "LMIC Plans Mentioning Structured Pedagogy",
    },
    "bb_targeted": {
        "name": "Targeted instruction / TaRL",
        "slug": "targeted",
        "title": "LMIC Plans Mentioning Targeted Instruction / TaRL",
    },
}

TIMELINE_EVENTS = {
    "bb_structped": [
        {
            "year": 2009,
            "label": '"Structured" reading packages\ntested in East Africa',
            "detail": (
                "Early EGRA-informed reading interventions in East Africa tested "
                "packages combining teacher training, instructional support, "
                "materials, books, and feedback on student reading."
            ),
            "source": "https://www.rti.org/sites/default/files/resources/early-reading-report_gove_cvelich.pdf",
            "callout_x": 0.19,
            "callout_y": -0.18,
            "arrow_rad": -0.22,
        },
        {
            "year": 2018,
            "label": "PRIMR ingredients study: SP package\nmost cost-effective",
            "detail": (
                "The Kenya Primary Math and Reading Initiative ingredients study "
                "found that the full package of professional development, coaching, "
                "student books, and structured teacher guides was the most effective "
                "and most cost-effective option."
            ),
            "source": "https://doi.org/10.1016/j.worlddev.2018.01.018",
            "callout_x": 0.47,
            "callout_y": -0.205,
            "arrow_rad": 0.22,
        },
        {
            "year": 2020,
            "label": 'SP a "Good Buy" in first\nGEEAP report',
            "detail": (
                "The Global Education Evidence Advisory Panel's first Smart Buys "
                "report listed structured pedagogy as a Good Buy."
            ),
            "source": (
                "https://www.worldbank.org/en/topic/teachingandlearning/publication/"
                "cost-effective-approaches-to-improve-global-learning"
            ),
            "callout_x": 0.71,
            "callout_y": -0.18,
            "arrow_rad": -0.2,
        },
        {
            "year": 2023,
            "label": 'SP a "Great Buy" in second\nGEEAP report',
            "detail": (
                "The Global Education Evidence Advisory Panel's updated Smart Buys "
                "report identified structured pedagogy support for teachers as a "
                "Great Buy."
            ),
            "source": "https://www.worldbank.org/en/news/press-release/2023/05/09/education-smart-buys-cost-effectively-supporting-teachers-and-parents-can-lead-to-significant-learning-improvements",
            "callout_x": 0.91,
            "callout_y": -0.205,
            "arrow_rad": 0.18,
        },
    ],
    "bb_targeted": [
        {
            "year": 2007,
            "label": "First Pratham remedial\nmodel RCT",
            "detail": (
                "Banerjee, Cole, Duflo, and Linden published randomized evidence "
                "on Pratham's remedial tutoring programme, an early precursor to "
                "teaching children at their current learning level."
            ),
            "source": "https://academic.oup.com/qje/article-abstract/122/3/1235/1879525",
            "callout_x": 0.12,
            "callout_y": -0.18,
            "arrow_rad": -0.24,
        },
        {
            "year": 2014,
            "label": '"Teaching at the right level" coined;\nstate-side scale-ups of TaRL in India',
            "detail": (
                "The Teaching at the Right Level framing appeared in public "
                "evidence discussions of Pratham's approach, alongside evidence "
                "from state-level scale-up evaluations in India."
            ),
            "source": "https://teachingattherightlevel.org/impact-and-learning/tarl-evidence/history-of-tarls-evidence-in-india/",
            "callout_x": 0.37,
            "callout_y": -0.205,
            "arrow_rad": 0.24,
        },
        {
            "year": 2020,
            "label": 'TaRL a "Good Buy" in first\nGEEAP report',
            "detail": (
                "The Global Education Evidence Advisory Panel's first Smart Buys "
                "report listed programmes that teach children at the right skill "
                "level as a Good Buy."
            ),
            "source": (
                "https://www.worldbank.org/en/topic/teachingandlearning/publication/"
                "cost-effective-approaches-to-improve-global-learning"
            ),
            "callout_x": 0.57,
            "callout_y": -0.18,
            "arrow_rad": -0.2,
        },
        {
            "year": 2023,
            "label": 'TaRL a "Great Buy" in second\nGEEAP report',
            "detail": (
                "The Global Education Evidence Advisory Panel's updated Smart Buys "
                "report identified Teaching at the Right Level / targeted "
                "instruction by learning level as a Great Buy."
            ),
            "source": "https://www.worldbank.org/en/news/press-release/2023/05/09/education-smart-buys-cost-effectively-supporting-teachers-and-parents-can-lead-to-significant-learning-improvements",
            "callout_x": 0.74,
            "callout_y": -0.205,
            "arrow_rad": 0.18,
        },
        {
            "year": 2024,
            "label": "RCT results of Zambia's\nnational TaRL program",
            "detail": (
                "A randomized evaluation of Zambia's national Catch Up programme "
                "reported positive learning effects from implementing Teaching at "
                "the Right Level through public systems."
            ),
            "source": "https://www.povertyactionlab.org/evaluation/targeting-foundational-skills-improve-learning-scale-zambia",
            "callout_x": 0.9,
            "callout_y": -0.29,
            "arrow_rad": -0.17,
        },
    ],
}

CGD_BASE_COLORS = [
    "#006970",
    "#FFB52C",
    "#2D99B5",
    "#BFDEE0",
    "#FEE8BF",
    "#85A5AD",
    "#394649",
    "#0B4C5B",
    "#00896C",
    "#D15553",
]

SHORT_LABELS = {
    "Afghanistan": "AFG",
    "Bangladesh": "BGD",
    "Cambodia": "KHM",
    "Chad": "TCD",
    "China": "CHN",
    "Congo": "COG",
    "Djibouti": "DJI",
    "Egypt": "EGY",
    "Ethiopia": "ETH",
    "Gambia": "GMB",
    "Grenada": "GRD",
    "Jamaica": "JAM",
    "Jordan": "JOR",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Lao People's Democratic Republic": "LAO",
    "Lebanon": "LBN",
    "Liberia": "LBR",
    "Madagascar": "MDG",
    "Maldives": "MDV",
    "Mauritius": "MUS",
    "Mozambique": "MOZ",
    "Myanmar": "MMR",
    "Nepal": "NPL",
    "Niger": "NER",
    "Pakistan": "PAK",
    "Rwanda": "RWA",
    "Sudan": "SDN",
    "Syrian Arab Republic": "SYR",
    "Timor-Leste": "TLS",
    "Tuvalu": "TUV",
    "Uganda": "UGA",
    "Vanuatu": "VUT",
    "Yemen": "YEM",
    "Zimbabwe": "ZWE",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the structured pedagogy and targeted instruction country-year graphs"
    )
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--source", choices=sorted(INPUTS), default="published")
    parser.add_argument("--figures-dir", default="figures")
    parser.add_argument("--tables-dir", default="output")
    return parser.parse_args()


def apply_reference_style() -> None:
    plt.rcParams["font.family"] = PLOT_FONT
    plt.rcParams["axes.labelsize"] = 15
    plt.rcParams["xtick.labelsize"] = 13
    plt.rcParams["ytick.labelsize"] = 13
    plt.rcParams["text.color"] = TEXT_DARK
    plt.rcParams["axes.labelcolor"] = TEXT_DARK
    plt.rcParams["xtick.color"] = TEXT_DARK
    plt.rcParams["ytick.color"] = TEXT_DARK
    plt.rcParams["axes.edgecolor"] = FRAME_COLOR
    plt.rcParams["axes.linewidth"] = 1.0


def style_axes(ax: plt.Axes) -> None:
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.9, alpha=0.6)
    ax.set_axisbelow(True)
    ax.set_facecolor("white")
    ax.tick_params(axis="x", colors=TEXT_DARK)
    ax.tick_params(axis="y", colors=TEXT_DARK)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(True)
    ax.spines["bottom"].set_color(FRAME_COLOR)
    ax.spines["bottom"].set_linewidth(1.0)
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontname(PLOT_FONT)
        tick.set_color(TEXT_DARK)


def income_group(series: pd.Series) -> pd.Series:
    out = pd.Series(LMIC, index=series.index)
    out.loc[series.eq("High income")] = "High Income"
    return out


def adjust_color(hex_color: str, factor: float) -> str:
    rgb = np.array(mcolors.to_rgb(hex_color))
    if factor >= 1:
        rgb = 1 - (1 - rgb) / factor
    else:
        rgb = rgb * factor
    return mcolors.to_hex(np.clip(rgb, 0, 1))


def build_country_palette(countries: list[str]) -> dict[str, str]:
    colors: list[str] = []
    factors = [1.0, 0.72, 1.35, 0.55]
    for factor in factors:
        for base_color in CGD_BASE_COLORS:
            colors.append(adjust_color(base_color, factor))
    return {country: colors[index % len(colors)] for index, country in enumerate(countries)}


def country_sort_key(country: str, country_year: pd.DataFrame) -> tuple[int, int, str]:
    rows = country_year[country_year["country"].eq(country)]
    first_year = int(rows["year_num"].min())
    total_mentions = int(rows["n_docs"].sum())
    return first_year, -total_mentions, country


def read_inputs(project_root: Path, source: str) -> pd.DataFrame:
    frames = []
    required_cols = {
        "docid",
        "title",
        "country",
        "year",
        "incomegroup",
        "rag_complete",
        "bb_structped",
        "bb_targeted",
    }
    for language, rel_path in INPUTS[source].items():
        path = project_root / rel_path
        if not path.exists():
            raise FileNotFoundError(
                f"Missing {language} input: {path}. "
                "Use --source published, or run replication_02_run_rag.py first."
            )
        frame = pd.read_stata(path, convert_categoricals=False).dropna(axis=1, how="all")
        missing = sorted(required_cols.difference(frame.columns))
        if missing:
            raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")
        frame["rag_language_group"] = language
        frames.append(frame)
    return pd.concat(frames, ignore_index=True, sort=False)


def keep_lmic_completed_documents(df: pd.DataFrame) -> pd.DataFrame:
    complete = pd.to_numeric(df["rag_complete"], errors="coerce").fillna(0).eq(1)
    filtered = df.loc[complete].copy()
    filtered = filtered[filtered["incomegroup"].fillna("").ne("")].copy()
    filtered["income_group"] = income_group(filtered["incomegroup"])
    filtered = filtered[filtered["income_group"].eq(LMIC)].copy()
    filtered["year_num"] = pd.to_numeric(filtered["year"], errors="coerce")
    filtered = filtered[filtered["year_num"].notna()].copy()
    filtered["year_num"] = filtered["year_num"].astype(int)
    filtered["country"] = filtered["country"].fillna("Unknown country").astype(str)
    return filtered


def make_country_year_table(df: pd.DataFrame, topic_col: str) -> pd.DataFrame:
    positives = df[pd.to_numeric(df[topic_col], errors="coerce").fillna(0).gt(0)].copy()
    country_year = (
        positives.groupby(["year_num", "country"], as_index=False)
        .agg(
            n_docs=("docid", "count"),
            titles=("title", lambda series: " | ".join(str(x) for x in series.dropna())),
            languages=(
                "rag_language_group",
                lambda series: ", ".join(sorted(set(str(x) for x in series.dropna()))),
            ),
        )
        .sort_values(["year_num", "country"])
        .reset_index(drop=True)
    )
    return country_year


def add_below_chart_event_callouts(ax: plt.Axes, events: list[dict[str, object]]) -> None:
    for event in events:
        year = int(event["year"])
        label = f"{year}\n{event['label']}"
        ax.annotate(
            label,
            xy=(year, -0.075),
            xycoords=ax.get_xaxis_transform(),
            xytext=(float(event.get("callout_x", 0.5)), float(event.get("callout_y", -0.25))),
            textcoords=ax.transAxes,
            ha="center",
            va="top",
            fontsize=13.5,
            fontname=PLOT_FONT,
            color=TEXT_DARK,
            linespacing=1.08,
            bbox={
                "boxstyle": "round,pad=0.32,rounding_size=0.06",
                "facecolor": "white",
                "edgecolor": GRID_COLOR,
                "linewidth": 1.0,
                "alpha": 0.98,
            },
            arrowprops={
                "arrowstyle": "-|>",
                "color": "#85A5AD",
                "linewidth": 1.6,
                "shrinkA": 6,
                "shrinkB": 2,
                "connectionstyle": f"arc3,rad={float(event.get('arrow_rad', 0.2))}",
            },
            annotation_clip=False,
            zorder=8,
        )


def save_country_stacked_chart(
    country_year: pd.DataFrame,
    topic_col: str,
    topic: dict[str, str],
    output_path: Path,
) -> None:
    if country_year.empty:
        raise ValueError(f"No positive rows found for {topic['name']}")

    is_targeted = topic_col == "bb_targeted"
    countries = sorted(
        country_year["country"].unique(),
        key=lambda country: country_sort_key(country, country_year),
    )
    palette = build_country_palette(countries)
    min_year = min(2000, int(country_year["year_num"].min()))
    max_year = max(2025, int(country_year["year_num"].max()))
    years = list(range(min_year, max_year + 1))
    pivot = (
        country_year.pivot(index="year_num", columns="country", values="n_docs")
        .reindex(index=years, columns=countries)
        .fillna(0)
    )

    fig_height = max(8.8, 5.8 + 0.12 * len(countries))
    fig, ax = plt.subplots(figsize=(15.6, fig_height))

    bottoms = np.zeros(len(years))
    for country in countries:
        values = pivot[country].to_numpy()
        ax.bar(
            years,
            values,
            bottom=bottoms,
            width=0.96,
            color=palette[country],
            edgecolor="none",
            linewidth=0,
        )
        bottoms += values

    for year in years:
        y_pos = 0
        for country in countries:
            value = int(pivot.loc[year, country])
            if value <= 0:
                continue
            label = SHORT_LABELS.get(country, country[:3].upper())
            text_color = (
                TEXT_DARK
                if palette[country] in {"#FEE8BF", "#BFDEE0", "#DFE0E2"}
                else "white"
            )
            for step in range(value):
                ax.text(
                    year,
                    y_pos + step + 0.5,
                    label,
                    ha="center",
                    va="center",
                    fontsize=10.2,
                    fontname=PLOT_FONT,
                    color=text_color,
                    fontweight="bold",
                    clip_on=True,
                )
            y_pos += value

    ax.set_title(
        topic["title"],
        loc="left",
        fontsize=22,
        fontname=PLOT_FONT,
        fontweight="bold",
        color=TEXT_DARK,
        pad=20,
    )
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(min_year - 0.7, max_year + 0.7)
    ax.set_ylim(0, max(3, float(pivot.sum(axis=1).max()) + 1))
    tick_years = [year for year in years if year % 2 == 0]
    ax.set_xticks(tick_years)
    ax.set_xticklabels([str(year) for year in tick_years], fontsize=17)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    style_axes(ax)
    ax.tick_params(axis="both", labelsize=17)
    add_below_chart_event_callouts(ax, TIMELINE_EVENTS[topic_col])
    fig.subplots_adjust(left=0.06, right=0.99, top=0.88, bottom=0.36 if is_targeted else 0.31)
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    figures_dir = project_root / args.figures_dir
    tables_dir = project_root / args.tables_dir
    figures_dir.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)

    apply_reference_style()
    combined = keep_lmic_completed_documents(read_inputs(project_root, args.source))

    timeline_rows = []
    for topic_col, topic in TOPICS.items():
        country_year = make_country_year_table(combined, topic_col)
        table_path = (
            tables_dir
            / f"bb_{topic['slug']}_country_year_mentions_english_french_spanish_combined.csv"
        )
        figure_path = (
            figures_dir
            / f"bb_{topic['slug']}_country_stacked_by_year_english_french_spanish_combined.png"
        )
        country_year.to_csv(table_path, index=False)
        save_country_stacked_chart(country_year, topic_col, topic, figure_path)
        for event in TIMELINE_EVENTS[topic_col]:
            timeline_rows.append(
                {
                    "topic": topic["name"],
                    "year": event["year"],
                    "label": str(event["label"]).replace("\n", " "),
                    "detail": event["detail"],
                    "source": event["source"],
                }
            )
        print(f"Wrote: {figure_path}")
        print(f"Wrote: {table_path}")

    timeline_path = tables_dir / "bb_sp_tarl_research_timeline_events_english_french_spanish_combined.csv"
    pd.DataFrame(timeline_rows).to_csv(timeline_path, index=False)
    print(f"Wrote: {timeline_path}")
    print(f"Documents in completed LMIC sample: {len(combined)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
