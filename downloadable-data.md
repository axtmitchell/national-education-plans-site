# Downloadable Data

The public data files for this project live in the GitHub folder [`graph data`](<graph data/>).

## Chart Data

- [`Figure 1.csv`](<graph data/Figure 1.csv>): broad smart-buy mentions by income group.
- [`Figure 2 SP.csv`](<graph data/Figure 2 SP.csv>): structured pedagogy country-year mention snippets.
- [`Figure 3 TARL.csv`](<graph data/Figure 3 TARL.csv>): targeted instruction / TaRL country-year mention snippets.
- [`Figure 4.csv`](<graph data/Figure 4.csv>): multilingual foundational learning and learning-crisis trend data.

## Sector Plan Search Data

- [`sector_plan_search_metadata.csv`](<graph data/sector_plan_search_metadata.csv>) has one row per OCR-readable plan document, with title, country, year, language, source links, text length, and rights-audit mode.
- [`sector_plan_search_snippets.csv`](<graph data/sector_plan_search_snippets.csv>) provides bounded snippets for search and browsing. It includes opening excerpts and curated topic-match snippets, but excludes documents marked `link_only`.
- [`sector_plan_rights_audit.csv`](<graph data/sector_plan_rights_audit.csv>) records the document-level rights screening behind the public snippet choices.

The search data intentionally does not publish the full OCR corpus. Most documents are treated as snippet-search only: public metadata, source links, and short excerpts rather than a full-text mirror of the original PDFs.
