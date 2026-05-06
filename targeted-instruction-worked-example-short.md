# Worked Example: Targeted Instruction (Short)

This is a short worked example of how the broader method looked for targeted instruction: teaching or grouping students by their current learning level rather than by grade alone.

For the exact term lists and prompts, see [How We Defined Each Smart Buy](smart-buy-definitions.md).

## 1. Retrieve promising chunks of text

Each plan is split into chunk-sized passages. For targeted instruction, each chunk is then scored in two ways:

- **Weighted lexical cues.** Stronger phrases get more weight than weaker ones.
- **Semantic similarity.** The method also looks for chunks that are close in meaning to short query phrases, even if they do not use the exact wording.

Examples of lexical cues include:

- `TaRL`
- `teaching at the right level`
- `grouped by learning level`
- `level-appropriate`

An example semantic query phrase is:

- `Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade`

## 2. Keep only the best candidate chunks

The method does not use one magic score cutoff. Instead, it keeps the strongest lexical hits, the strongest semantic hits, combines them, and keeps a small number of the best-ranked chunks plus nearby context.

Those are the only passages sent forward to the LLM.

## 3. Ask the LLM to make the judgment

The LLM does not read the whole document from scratch. It only reads the retrieved chunks and decides whether they really describe targeted instruction by learning level.

For this category, the important distinction is between:

- real teaching or grouping by current learning level
- generic remediation, catch-up support, or diagnostic assessment on their own

## 4. Verification step

A cheaper model does the first pass, and a stronger model re-checks positives and uncertain negatives.

The model must also give a short verbatim quote from the retrieved text as evidence. If the quote is not actually present in the retrieved chunks, the hit is rejected.

## Plain-English takeaway

So the broader method is not just searching for the word `TaRL`, and it is not asking an LLM to guess from the whole plan. It first narrows the plan to a small set of relevant passages using weighted search terms and meaning-based retrieval. It then asks the model whether those passages really describe teaching by assessed learning level rather than generic remedial support.

That makes the method broader than a strict word search, but still more transparent and constrained than a free-form full-document LLM read.
