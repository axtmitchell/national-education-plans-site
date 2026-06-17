# Worked Example: Targeted Instruction

This is a short worked example of how the retrieval-augmented generation (RAG) method looked for targeted instruction. We defined targeted instruction as teaching or grouping students by their current learning level rather than by grade alone.

This page is meant as an overview. For the exact term lists and prompts, see [How We Defined Each Smart Buy](smart-buy-definitions.md).

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

The method keeps:

- the top lexical hits
- the top semantic hits
- the union of those hits, reranked using the combined retrieval score
- neighboring chunks for context

The highest-ranked chunks are then sent to the LLM.

## 3. Ask the LLM to make the judgment

The LLM reads the retrieved chunks and decides whether they really describe targeted instruction by learning level.

The rule is:

- count `TRUE` only when the text clearly describes targeted instruction by learning level rather than by grade alone

## 4. Verification step

A cheaper model does the first pass, and a stronger model re-checks:

- all positives
- negatives with low confidence

The model must give a short verbatim quote from the retrieved text as evidence. Which is reviewed by the authors.

