# Worked Example: Targeted Instruction

This is a short worked example of how the broader method looked for targeted instruction: teaching or grouping students by their current learning level rather than by grade alone.

This page is meant as an overview, not a full technical appendix. For the exact term lists and prompts, see [How We Defined Each Smart Buy](smart-buy-definitions.md).

## 1. Retrieve promising chunks of text

Each plan is split into overlapping chunks of text, roughly paragraph-sized.

For targeted instruction, each chunk is scored in two ways:

- **Weighted lexical cues.** Stronger phrases get more weight than weaker ones.
- **Semantic similarity.** The method also looks for chunks that are close in meaning to short query phrases, even if they do not use the exact wording.

Examples of stronger lexical cues include:

- English: `TaRL`, `teaching at the right level`, `grouped by learning level`, `level-appropriate`
- French: `enseignement au bon niveau`, `regroupement des élèves par niveau`, `par niveau d’apprentissage`

Examples of weaker cues include:

- English: `catch-up`, `remedial`
- French: `instruction ciblée par niveau`, `niveaux d’apprentissage`

Examples of semantic query phrases include:

- `Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade`
- `enseignement au bon niveau avec regroupement des eleves par niveau d apprentissage plutot que par classe`

The semantic step uses embeddings: the model turns both chunks and query phrases into vectors, and the method then keeps the chunks whose vectors are closest in meaning.

## 2. Keep only the top-ranked chunks

There is no single semantic-score cutoff such as “everything above 0.7 passes.”

Instead, the method keeps:

- the top lexical hits
- the top semantic hits
- the union of those hits, reranked using the combined retrieval score
- neighboring chunks for context

Only a small number of the highest-ranked chunks are then sent to the LLM.

## 3. Ask the LLM to make the judgment

The LLM does not read the whole plan from scratch. It only reads the retrieved chunks and decides whether they really describe targeted instruction by learning level.

The English rule is:

- count `TRUE` only when the text clearly describes targeted instruction by learning level rather than by grade alone

The French rule is slightly stricter:

- count `TRUE` only when teaching or student grouping is explicitly organized by assessed learning level
- do **not** count generic remediation, catch-up support, screening, or diagnostic assessment on their own

## 4. Verification step

A cheaper model does the first pass, and a stronger model re-checks:

- all positives
- negatives with low confidence

The model must give a short verbatim quote from the retrieved text as evidence. If the quote is not actually present in the retrieved chunks, the hit is rejected.

## Plain-English takeaway

So the broader method does not simply search for the word `TaRL`, and it does not ask an LLM to guess from the whole document. It first narrows the plan to the most relevant chunk-sized passages, then asks the model whether those passages really describe teaching by assessed learning level rather than generic remediation.
