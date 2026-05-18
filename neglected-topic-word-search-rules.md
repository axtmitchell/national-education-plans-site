# Figure 1 Word-Search Rules

This page gives the exact hard-coded phrase rules used for:

`government_neglected_topics_trends_lmic_multilingual_fln_explicit_equivalents_learning_crisis`

This graph does not use semantic search, embeddings, or LLM review.

Before matching, text is lowercased, accents are stripped, and minor punctuation variants are ignored.

## What The Two Lines Mean

- `Learning crisis` counts direct mentions of the learning-crisis idea.
- `FLN / explicit equivalents` counts only phrases that are already fairly self-explanatory on their own.

This graph does **not** use the broader `Basic skills` bucket, and it does **not** use the old rule that required a phrase to appear near primary-school language.

## Learning Crisis

Direct phrase hits only.

- English: `global learning crisis`, `learning crisis`, `learning poverty`
- French: `crise des apprentissages`, `crise de l apprentissage`, `crise des apprentissage`, `pauvrete des apprentissages`, `pauvrete de l apprentissage`
- Spanish: `crisis de aprendizaje`, `crisis del aprendizaje`, `pobreza de aprendizaje`

## FLN / Explicit Equivalents

Only self-contained FLN phrases or close equivalents count.

### English

- `foundational literacy`
- `foundational numeracy`
- `foundational literacy and numeracy`
- `fln`

### Spanish

- `habilidades fundacionales`
- `lectoescritura` when it appears together with nearby math wording such as `matemáticas`, `matemático`, or `matemática`

### French

- `littératie` together with `numératie`
- `compétences fondamentales` when the phrase itself also names reading and math, for example `lecture` with `calcul` or `mathématiques`

## Not Included In This Graph

These broader terms are not part of this graph’s FLN line:

- `basic literacy and numeracy`
- `habilidades básicas`
- `apprentissages fondamentaux`
- `aprendizajes fundamentales`

Those broader terms were used in earlier exploratory versions, but not in the final graph linked from the blog.
