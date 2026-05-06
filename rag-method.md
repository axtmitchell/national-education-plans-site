# How We Use RAG To Find Smart Buys In Education Plans

## Why We Built This

We wanted a way to identify mentions of the GEEAP/FCDO education smart buys across a large corpus of national education plans without relying only on simple keyword search.

A pure word search is too brittle. It can miss cases where a plan describes the same intervention in different language, and it can also produce false positives when a phrase is too broad.

A single full-document LLM pass is also not ideal. It is relatively expensive, can struggle with very long documents, and can sometimes over-read generic policy language as a smart-buy mention.

So we built a hybrid retrieval-and-verification workflow.

## The Method In Plain English

For each document, we split the text into smaller chunks. For each smart buy, we then search those chunks in two ways.

First, we use a weighted lexical search. This is based on a broad set of phrase families developed from earlier broad-search work and manual review. Stronger cues get more weight than weaker ones.

Second, we use semantic retrieval with embeddings. This lets us find chunks that are close in meaning to the intervention idea even when the exact wording is different.

We combine the best hits from those two retrieval steps, keep the surrounding chunks for context, and then send only those candidate passages to the LLM.

The LLM works in two stages:

- a cheaper model does the first pass
- a stronger model reviews positives and uncertain cases

The model is asked not just whether the text uses the canonical smart-buy label, but whether it describes the same intervention idea. It must ground that judgment in a verbatim quote from the retrieved text.

## Why This Is Better Than Our Earlier Attempts

This workflow is designed to balance recall, precision, and cost.

Compared with a strict word search, it is better at finding near-equivalent descriptions. Compared with a single full-document LLM call, it is more conservative and more auditable because the model only sees the most relevant passages and has to cite evidence.

In other words, the retrieval stage finds likely passages, and the LLM stage makes the judgment call.

## Validation Check

Before scaling to the full corpus, we manually reviewed a positive-only validation sample from an 80-document pilot.

In this review, `maybe` was treated as `yes`. That reflects the fact that some high-income-country cases do not fit the smart-buy framing perfectly, but are still close enough in intervention logic to count as acceptable matches for this purpose.

Across `57` reviewed positive predictions:

- `53` were judged `yes` or `maybe`
- `4` were judged `no`

That gives:

- positive-side precision: `93.0%`
- false-positive rate: `7.0%`

## Validation By Smart Buy

| Smart buy | Positive sample | Yes or maybe | No | Precision | False-positive rate |
|---|---:|---:|---:|---:|---:|
| Information (`bb_info`) | 4 | 4 | 0 | 100.0% | 0.0% |
| Structured pedagogy (`bb_structped`) | 7 | 7 | 0 | 100.0% | 0.0% |
| Targeted instruction / TaRL (`bb_targeted`) | 4 | 4 | 0 | 100.0% | 0.0% |
| Parent stimulation (`bb_parentstim`) | 3 | 3 | 0 | 100.0% | 0.0% |
| Pre-primary (`bb_preprimary`) | 12 | 9 | 3 | 75.0% | 25.0% |
| Reduce travel (`bb_travel`) | 10 | 10 | 0 | 100.0% | 0.0% |
| Merit scholarships (`bb_merit`) | 12 | 11 | 1 | 91.7% | 8.3% |
| Mass deworming (`bb_deworm`) | 5 | 5 | 0 | 100.0% | 0.0% |

## How We Read These Results

The validation suggests that the method is working well for most categories.

The strongest categories in this sample were:

- structured pedagogy
- targeted instruction / TaRL
- parent stimulation
- reduce travel
- deworming

Merit scholarships also looked strong.

The weakest category was pre-primary, where some predicted positives were judged too broad. That means this category should be interpreted with a bit more caution than the others.

## Important Caveat

This is a validation of predicted positives, not a full accuracy score.

So this check tells us something useful about precision, but it does not tell us recall. The system may still miss some true mentions that are phrased in unusual ways.

That said, this hybrid RAG approach is a much more defensible middle ground than either:

- relying only on keyword search
- or asking an LLM to read each whole document in one shot

## Files Behind This Note

- Pilot dataset:
  - `output/nep_counted_llm_rag_pilot_80.dta`
- Manual validation sheet:
  - `output/nep_counted_llm_rag_pilot_80_manual_validation.csv`
- Yes-or-maybe summary:
  - `output/nep_counted_llm_rag_pilot_80_manual_validation_yesmaybe_summary.csv`
