# Methodology

Overview: The pipeline first found candidate passages, then asked the model to judge whether those passages really matched the smart-buy definition.

## How The RAG Pipeline Worked

Each document was split into overlapping chunks of about `2,200` characters, with `250` characters of overlap.

For each smart buy, candidate chunks were retrieved in two ways:

- **Lexical retrieval:** weighted phrase searches looked for intervention-specific cues and synonyms. Stronger cues counted more than weaker cues.
- **Semantic retrieval:** embeddings from `text-embedding-3-small` were used to find chunks that were close in meaning to short descriptions of the intervention, even if they did not use the exact search terms.

The pipeline kept the top lexical and semantic hits, added nearby chunks for context, and capped the candidate text sent to the model at `10` chunks per smart buy.

The model review then happened in two stages:

- `gpt-4.1-mini` made the first-pass classification.
- `gpt-4.1` reviewed positives and uncertain negatives.

The model had to return a structured JSON decision with a label, confidence score, rationale, and a short verbatim quote from the retrieved chunks. If the quoted evidence was not actually present in the retrieved text, the positive label was rejected.

## Language Handling

The English run used English definitions, lexical cues, and semantic retrieval queries.

For French and Spanish, we created language-specific configurations with translated retrieval cues and category definitions. These were tested on small pilot runs before the full run. We tightened the French and Spanish rules where pilot review showed obvious false positives, especially for categories that can blur into nearby concepts:

- generic remediation versus targeted instruction by learning level
- generic teacher training versus structured pedagogy
- parent monitoring or school updates versus information for schooling decisions
- generic family support versus parent-directed early stimulation

The final trilingual figure combines the completed English, French, and Spanish RAG outputs.

## Validation

The validation checks were positive-side checks: we reviewed cases that the method had flagged as smart-buy mentions and judged whether they were real hits. This estimates precision, not recall.

In the main English validation sample, `49` of `53` scored positives were judged correct, giving positive-side precision of `92.5%`. A later focused French spot-check looked at pre-primary and merit-scholarship positives, the categories that seemed easiest to overstate. Combining the English validation and that French spot-check, `61` of `69` scored positives were judged correct, or `88.4%`.

The Spanish run was also manually inspected after completion. Most travel and merit positives looked reasonable, while pre-primary remained broad and the information category looked more permissive. The trilingual chart uses the completed Spanish `v2` output, not a later rerun after that audit.

## Main Caveats

The method is designed to find plausible mentions, not to prove implementation. Sector plans are high-level documents and may omit programmes that governments are actually running.

The validation checks tell us that most reviewed positives were real, but they do not tell us how many true mentions the method missed. This is especially relevant for interventions that may be described in very country-specific language.

Some categories are broader than their short labels. For example, the pre-primary category captures quality-related preschool language, and the merit category can include performance-linked awards or incentives, not only formal scholarship schemes.

Finally, because the sample includes many specialist documents as well as broad national sector plans, the figure should be read as the share of education-planning documents mentioning each concept, not the share of governments formally adopting each smart buy.

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
