# Methodology

Overview: The pipeline first found candidate passages, then asked the model to judge whether those passages really matched the smart-buy definition.

## How The RAG Pipeline Worked

Each document was split into overlapping chunks of about `2,200` characters, with `250` characters of overlap.

For each smart buy, candidate chunks were retrieved in two ways:

- **Lexical retrieval:** weighted phrase searches looked for intervention-specific cues and synonyms. Stronger cues counted more than weaker cues.
- **Semantic retrieval:** embeddings from `text-embedding-3-small` were used to find chunks that were close in meaning to short descriptions of the intervention, even if they did not use the exact search terms.

The pipeline kept the top lexical and semantic hits, added nearby chunks for context.

The model review then happened in two stages:

- `gpt-4.1-mini` made the first-pass classification.
- `gpt-4.1` reviewed positives and uncertain negatives.

The model had to return a structured JSON decision with a label, confidence score, rationale, and a short verbatim quote from the retrieved chunks.

## Validation

The validation checks were positive-side checks: we reviewed cases that the method had flagged as smart-buy mentions and judged whether they were real hits. This estimates precision, not recall.

In the validation sample, `61` of `69` (88%) scored positives were judged correct.

## Reproduction Files

Main classifier:

- `code/14_llm_rag_classify.py`

Language-specific configurations:

- `code/best_buy_configs/french_rag_v1.py`
- `code/best_buy_configs/spanish_rag_v2.py`

Completed RAG outputs:

- `output/nep_counted_llm_rag_full.dta`
- `output/nep_counted_llm_rag_french_full_v1.dta`
- `output/nep_counted_llm_rag_spanish_full_v2.dta`

Figure code:

- `code/20_blog_figure_refresh.py`
- `code/27_rag_french_combined_graphs.py`

More detailed method notes:

- [RAG method](rag-method.md)
- [RAG validation](rag-validation.md)
- [Smart-buy definitions and prompts](smart-buy-definitions.md)
