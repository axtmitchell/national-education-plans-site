# Worked Example: Targeted Instruction

This page gives a step-by-step example of how the broader method looked for mentions of targeted instruction in the plan corpus.

## 1. Split Each Document Into Chunks

Each plan is split into overlapping chunks of text:

- roughly `2200` characters per chunk
- roughly `250` characters of overlap

This makes long plans easier to search and helps preserve nearby context when a relevant passage falls near a chunk boundary.

## 2. Score Each Chunk In Two Ways

### 2a. Lexical Score

Each chunk gets a weighted lexical score based on search terms.

`lexical score = sum of (term weight × number of matches in that chunk)`

Strong terms get more weight than weaker ones.

#### English lexical cues

High-weight terms:

- `TaRL`
- `teaching at the right level`
- `grouped/grouping by learning level`
- `level-appropriate`

Medium-weight terms:

- `learning level`
- `ability grouping`

Low-weight terms:

- `catch-up`
- `remedial`

#### French lexical cues

High-weight terms:

- `enseignement au bon niveau`
- `groupes de niveau`
- `regroupement des élèves par niveau`
- `par niveau d’apprentissage`
- `selon leur niveau d’apprentissage`

Medium-weight terms:

- `niveaux d’apprentissage`
- `instruction ciblée par niveau`
- `groupes de niveau`

This is only a retrieval score. A high lexical score does not by itself make a document a true hit.

### 2b. Semantic Similarity Score

Each chunk also gets a semantic similarity score. This is based on embeddings rather than exact wording.

The method creates:

- an embedding vector for each chunk
- an embedding vector for a small number of short query phrases

It then checks which chunk vectors are closest in meaning to the query vectors.

The embedding model is doing the representation step here. The closeness check itself is ordinary vector math.

#### English query phrases

- `Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade`
- `targeted instruction after assessment with regrouping by current learning level`

#### French query phrases

- `enseignement au bon niveau avec regroupement des eleves par niveau d apprentissage plutot que par classe`
- `instruction ciblee fondee sur une evaluation diagnostique et un regroupement par niveau`

This is still retrieval, not the final judgment.

## 3. Decide Which Chunks Go To The LLM

There is no single semantic-score cutoff such as “everything above 0.7 passes.”

Instead, the method keeps the highest-ranked chunks:

- the top `8` lexical hits with lexical score above zero
- the top `8` semantic hits
- the union of those chunks, reranked using `lexical score + semantic score`
- neighboring chunks for context

At most `10` chunks are then sent to the LLM for that category.

So the cutoff is mostly rank-based rather than threshold-based.

## 4. Ask The LLM To Make The Judgment

Only after retrieval does the LLM decide whether the selected text really describes targeted instruction by learning level.

### English rule

Count a chunk as `TRUE` only when it clearly describes targeted instruction by learning level rather than by grade alone.

Definition used:

`Targeted instruction by learning level (TaRL-style), not by grade only.`

### French rule

Count a chunk as `TRUE` only when teaching or student grouping is explicitly organized by assessed learning level rather than age or grade alone.

Definition used:

`Targeted instruction by learning level (TaRL-style), not generic remediation or catch-up support.`

Important French hard negatives:

- generic remediation or catch-up support
- screening or diagnostic assessment alone
- support for struggling students without regrouping by learning level
- catch-up classes delivered by grade, not by current learning level

## 5. Verification Step

A cheaper model, `gpt-4.1-mini`, does the first pass.

A stronger model, `gpt-4.1`, then re-checks:

- all positives
- any negatives with confidence below `0.60`

The model must also provide a short verbatim quote from the retrieved text as evidence. If the quote is not actually present in the retrieved chunks, the hit is rejected.

## Plain-English Summary

For targeted instruction, the broader method does not ask the LLM to read the whole plan from scratch. It first uses weighted search terms and embedding-based similarity to find the most relevant chunk-sized passages. The LLM then judges only those passages, using a stricter category definition and requiring an exact evidence quote.
