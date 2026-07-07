#!/usr/bin/env python3
"""
Build public, snippet-only data files for the GitBook site.

The source OCR corpus is intentionally not copied into the site repo. Instead,
this script writes:

- graph data/sector_plan_search_metadata.csv
- graph data/sector_plan_search_snippets.csv
"""

from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


SITE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SITE_ROOT.parent
DEFAULT_SOURCE = PROJECT_ROOT / "output" / "planipolis_merged_excel_text.csv"
DEFAULT_OUT_DIR = SITE_ROOT / "graph data"

SNIPPET_CHARS = 420
OPENING_CHARS = 420
MAX_TOPIC_SNIPPETS_PER_DOC = 6


@dataclass(frozen=True)
class TopicPattern:
    topic: str
    pattern: re.Pattern[str]


TOPIC_PATTERNS = [
    TopicPattern("Access and enrolment", re.compile(r"\b(access|enrol(?:l)?ment|out[- ]of[- ]school|dropout|retention)\b", re.I)),
    TopicPattern("Assessment and exams", re.compile(r"\b(assessment|examination|exam|learning assessment|student assessment)\b", re.I)),
    TopicPattern("Climate, crisis, or emergency", re.compile(r"\b(covid|pandemic|emergency|crisis|climate change|disaster|resilience)\b", re.I)),
    TopicPattern("Curriculum and materials", re.compile(r"\b(curriculum|textbook|learning materials?|teaching materials?|instructional materials?)\b", re.I)),
    TopicPattern("Digital and edtech", re.compile(r"\b(digital|ict|technology|edtech|computer|online learning|distance learning)\b", re.I)),
    TopicPattern("Disability and inclusion", re.compile(r"\b(disability|disabled|inclusive education|special education|inclusion|equity)\b", re.I)),
    TopicPattern("Early childhood and pre-primary", re.compile(r"\b(early childhood|pre[- ]?primary|pre[- ]?school|kindergarten|school readiness)\b", re.I)),
    TopicPattern("Finance and budgets", re.compile(r"\b(financ(?:e|ing)|budget|expenditure|cost(?:ing)?|funding)\b", re.I)),
    TopicPattern("Foundational literacy and numeracy", re.compile(r"\b(foundational literacy|foundational numeracy|fln|literacy and numeracy|reading and mathematics)\b", re.I)),
    TopicPattern("Gender and girls", re.compile(r"\b(gender|girls'? education|female students?|girls)\b", re.I)),
    TopicPattern("Learning crisis", re.compile(r"\b(learning crisis|learning poverty)\b", re.I)),
    TopicPattern("School infrastructure", re.compile(r"\b(classroom construction|school construction|infrastructure|latrines|water and sanitation|school facilities)\b", re.I)),
    TopicPattern("School meals and health", re.compile(r"\b(school feeding|school meals?|school lunch|school health|nutrition|deworming)\b", re.I)),
    TopicPattern("School safety and violence", re.compile(r"\b(school violence|gender[- ]based violence|bullying|corporal punishment|safeguarding|harassment)\b", re.I)),
    TopicPattern("Structured pedagogy", re.compile(r"\b(structured pedagogy|lesson plans?|teacher guides?|scripted lessons?|coaching|mentoring)\b", re.I)),
    TopicPattern("Targeted instruction / TaRL", re.compile(r"\b(tarl|teaching at the right level|targeted instruction|learning levels?|remedial|catch[- ]?up)\b", re.I)),
    TopicPattern("Teachers", re.compile(r"\b(teacher training|teacher development|professional development|teacher education|teacher support)\b", re.I)),
    TopicPattern("TVET and skills", re.compile(r"\b(tvet|technical and vocational|vocational|skills development|workforce skills)\b", re.I)),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build public metadata and snippet-search CSVs")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    text = text.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", text).strip()


def to_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def stable_doc_id(row: pd.Series) -> str:
    key = "|".join(
        clean_text(row.get(col))
        for col in [
            "source_row_number",
            "document_url",
            "source_page",
            "local_filename",
            "title",
            "countries",
            "year",
        ]
    )
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:10]
    return f"nep_{digest}"


def year_int(value: object) -> str:
    try:
        return str(int(float(value)))
    except Exception:
        return ""


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def compact_snippet(text: str, start: int, end: int, max_chars: int = SNIPPET_CHARS) -> str:
    if not text:
        return ""
    center = (start + end) // 2
    half = max_chars // 2
    left = max(0, center - half)
    right = min(len(text), center + half)
    snippet = text[left:right].strip()
    snippet = re.sub(r"^\S+\s+", "", snippet) if left > 0 else snippet
    snippet = re.sub(r"\s+\S+$", "", snippet) if right < len(text) else snippet
    prefix = "..." if left > 0 else ""
    suffix = "..." if right < len(text) else ""
    return f"{prefix}{snippet}{suffix}"


def opening_excerpt(text: str) -> str:
    if not text:
        return ""
    snippet = text[:OPENING_CHARS].strip()
    snippet = re.sub(r"\s+\S+$", "", snippet) if len(text) > OPENING_CHARS else snippet
    suffix = "..." if len(text) > OPENING_CHARS else ""
    return f"{snippet}{suffix}"


def topic_snippets(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for topic in TOPIC_PATTERNS:
        match = topic.pattern.search(text)
        if not match:
            continue
        snippet = compact_snippet(text, match.start(), match.end())
        key = re.sub(r"\W+", " ", snippet.lower())[:160]
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            {
                "snippet_type": "topic_hit",
                "topic": topic.topic,
                "matched_text": match.group(0),
                "snippet_text": snippet,
            }
        )
        if len(rows) >= MAX_TOPIC_SNIPPETS_PER_DOC:
            break
    return rows


def load_source(source_path: Path) -> pd.DataFrame:
    source = pd.read_csv(source_path, low_memory=False)
    source = source[source["ocr_has_text"].map(to_bool)].copy()
    source["text_clean"] = source["text"].map(clean_text)
    source = source[source["text_clean"].str.len().gt(0)].reset_index(drop=True)
    source["source_row_number"] = range(1, len(source) + 1)
    return source


def build_public_files(df: pd.DataFrame, out_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    metadata_rows: list[dict[str, object]] = []
    snippet_rows: list[dict[str, object]] = []

    for _, row in df.iterrows():
        doc_id = stable_doc_id(row)
        text = row["text_clean"]
        base = {
            "doc_id": doc_id,
            "title": clean_text(row.get("title")),
            "country": clean_text(row.get("countries")),
            "year": year_int(row.get("year")),
            "languages": clean_text(row.get("languages")),
            "resource_type": clean_text(row.get("ressource_type")),
            "planipolis_page_url": clean_text(row.get("link")),
            "document_url": clean_text(row.get("documents")),
            "local_filename": clean_text(row.get("local_filename")),
            "source_row_number": int(row.get("source_row_number")),
        }
        metadata_rows.append(
            {
                **base,
                "word_count": word_count(text),
                "text_chars": len(text),
            }
        )

        snippets = [
            {
                "snippet_type": "opening_excerpt",
                "topic": "Opening excerpt",
                "matched_text": "",
                "snippet_text": opening_excerpt(text),
            }
        ]
        snippets.extend(topic_snippets(text))
        for number, snippet_data in enumerate(snippets, start=1):
            if not snippet_data["snippet_text"]:
                continue
            snippet_rows.append(
                {
                    "snippet_id": f"{doc_id}_{number:02d}",
                    **base,
                    **snippet_data,
                }
            )

    metadata = pd.DataFrame(metadata_rows).sort_values(["country", "year", "title", "doc_id"])
    snippets = pd.DataFrame(snippet_rows).sort_values(["country", "year", "title", "snippet_id"])

    out_dir.mkdir(parents=True, exist_ok=True)
    metadata.to_csv(out_dir / "sector_plan_search_metadata.csv", index=False)
    snippets.to_csv(out_dir / "sector_plan_search_snippets.csv", index=False)
    return metadata, snippets


def main() -> int:
    args = parse_args()
    df = load_source(Path(args.source))
    metadata, snippets = build_public_files(df, Path(args.out_dir))
    print(f"Wrote {len(metadata)} metadata rows")
    print(f"Wrote {len(snippets)} snippet rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
