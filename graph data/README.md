# Downloadable Data

This folder contains public data files for the National Education Plans project.
The files are designed for chart replication and snippet-level document search.
They do **not** include full OCR text from the sector plans.

## Figure Data

- `Figure 1.csv`: broad smart-buy mentions by income group.
- `Figure 2 SP.csv`: structured pedagogy country-year mention snippets.
- `Figure 3 TARL.csv`: targeted instruction / TaRL country-year mention snippets.
- `Figure 4.csv`: multilingual foundational learning and learning-crisis trend data.

## Sector Plan Snippet Search Data

- `sector_plan_search_metadata.csv`: one row per OCR-readable plan document, with
  country, year, language, source links, text length, and rights-audit mode.
- `sector_plan_search_snippets.csv`: bounded public snippets for search and
  browsing. This includes opening excerpts and topic-match snippets, but omits
  any document marked `link_only` in the rights audit.
- `sector_plan_rights_audit.csv`: the document-level rights screening used to
  decide whether each plan should be full-text, snippet-search, manual-review,
  or link-only in public outputs.

## Publication Modes

- `full_text_ok_text_only`: explicit open licence found. Text-only reuse still
  requires attribution and licence notes.
- `manual_review_full_text_candidate`: possible reuse or public-domain signal,
  but needs human confirmation before publishing full OCR text.
- `snippet_search_ok`: use metadata, source links, search indexing, and short
  snippets only.
- `link_only`: restrictive language found; use metadata and source links only.
