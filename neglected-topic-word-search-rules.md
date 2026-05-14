# Neglected-Topic Word-Search Rules

This page records the exact hard-coded phrase logic used for the current multilingual comparison graph:

`government_neglected_topics_trends_lmic_multilingual_modern_fln_basic_skills_learning_crisis`

This graph is a phrase screen rather than a broad retrieval system. It does not use semantic search, embeddings, or LLM review.

## How To Read The Graph

The current graph has three series:

- `Modern FLN vocabulary`: direct modern terms such as `foundational literacy`, `foundational numeracy`, and `fln`
- `Basic skills`: older wording for early reading, writing, and math skills
- `Learning crisis`: direct phrases such as `learning crisis` and `learning poverty`

The earlier broader `Foundational literacy / numeracy` line combined the first two. In other words:

`Foundational literacy / numeracy = Modern FLN vocabulary + Basic skills`

That is why the older broad FLN line can look very similar to the `Basic skills` line in years when modern FLN terminology is still rare.

## What This Page Is Showing

- Text is lowercased before matching.
- Accents are stripped before matching, so `éducation` is matched as `education`.
- Minor punctuation, spacing, and hyphen variants are allowed in code. The lists below show the readable phrase forms.
- The rules below are all hard-coded phrase rules.
- For `Modern FLN vocabulary` and `Basic skills`, the title and body text are checked together because the schooling stage is sometimes signaled in the title.

## Exact Rules By Series

### Learning Crisis

This line uses direct phrase hits only.

- English: `global learning crisis`, `learning crisis`, `learning poverty`
- French: `crise des apprentissages`, `crise de l apprentissage`, `crise des apprentissage`, `pauvrete des apprentissages`, `pauvrete de l apprentissage`
- Spanish: `crisis de aprendizaje`, `crisis del aprendizaje`, `pobreza de aprendizaje`

### Modern FLN Vocabulary

This line counts only direct modern FLN terms.

- English: `foundational literacy`, `foundational numeracy`, `foundational literacy and numeracy`, `fln`

### Basic Skills

This line is meant to capture older wording for the same general idea.

A document counts on the `Basic skills` line only if all of these are true:

1. It contains one of the phrase families below.
2. That phrase appears near language pointing to early-childhood, pre-primary, primary, or early-grade learning.
3. It is not clearly about adults, non-formal learning, tertiary education, or other older-learner contexts.

#### Step 1: Phrase Families

These phrase families can trigger the `Basic skills` line:

- English: `literacy and numeracy`, `basic literacy and numeracy`, `reading writing arithmetic`, `reading writing numeracy`, `reading writing mathematics`, `reading writing math`
- French: `litteratie`, `numeratie`, `lecture ecriture calcul`, `lire ecrire compter`
- Spanish: `lectoescritura`, `lectura escritura calculo`

These broader phrase families can also count, but only if they appear near both young-learner language and nearby literacy / numeracy wording:

- French: `apprentissages fondamentaux`
- Spanish: `aprendizajes fundamentales`

#### Step 2: Young-Learner Or Primary-Stage Context

The code then looks for nearby age or schooling-stage language such as:

- English: `early grade`, `early grades`, `early years`, `early primary`, `primary class`, `primary classes`, `primary stage`, `elementary`, `pre-primary`, `preschool`, `kindergarten`, `early childhood`, `lower primary`, `eced`, `grade 1`, `grade 2`, `grade 3`, `first years of school`
- French: `education de base`, `enseignement primaire`, `ecole primaire`, `primaire`, `elementaire`, `preprimaire`, `prescolaire`, `preelementaire`, `petite enfance`, `premier cycle`, `premieres annees`
- Spanish: `nivel primario`, `educacion primaria`, `primaria`, `preescolar`, `preprimaria`, `educacion inicial`, `primera infancia`, `primeros grados`, `primer ciclo`

#### Step 3: Exclusions

The rule excludes nearby language that clearly points to older or broader populations rather than young learners:

- English: `adult literacy`, `adult education`, `adult learners`, `lifelong learning`, `non-formal education`, `nfe programme`, `prevocational`, `higher education`, `tertiary`
- French: `alphabetisation des adultes`, `education non formelle`, `formation des adultes`, `apprentissage tout au long de la vie`
- Spanish: `alfabetizacion de adultos`, `educacion de adultos`, `educacion no formal`, `aprendizaje a lo largo de la vida`

## Short Version

If you only want the quick interpretation:

- `Modern FLN vocabulary` is the newer explicit jargon.
- `Basic skills` is the older wording for early reading, writing, and math.
- `Learning crisis` is its own direct phrase search.
- No part of this graph uses semantic search or AI judgment.

## Related Page

For the broader mixed page that also includes the multilingual strict smart-buy phrase screen, see [Multilingual phrase rules](multilingual-strict-phrases.md).
