# Replication Data

This folder contains compact, analysis-ready data for reproducing the public smart-buy figures without re-downloading Planipolis PDFs or publishing the full extracted text corpus.

## Files

- `trilingual_rag_labels.csv`: document-level English, French, and Spanish RAG labels used in the smart-buy figures. It includes plan metadata, source URLs, binary smart-buy labels, confidence scores, evidence snippets, and model review stages. It intentionally omits full plan text.
- `trilingual_rag_labels_summary.csv`: row counts and basic coverage by language.

## Why This Is Not The Full Raw Corpus

The original Planipolis download, OCR, and text-extraction pipeline produced large local files, including CSVs over 100 MB and full-text Stata files close to GitHub's per-file limit. The compact label file is the public reproduction input: it is enough to rebuild the published figure-level analyses from the final classifications, while source links and short snippets preserve auditability.

To rerun the classifier from raw text, see the scripts in `archive/analysis/`. That route requires the local Planipolis text extraction outputs and OpenAI API access.
