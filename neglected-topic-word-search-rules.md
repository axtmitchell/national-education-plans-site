# Figure 1 Word-Search Rules

## How To Read The Graph

The current graph has three series:

- `Modern FLN vocabulary`: direct modern terms such as `foundational literacy`, `foundational numeracy`, and `fln`
- `Basic skills`: older wording for early reading, writing, and math skills
- `Learning crisis`: direct phrases such as `learning crisis` and `learning poverty`

The earlier broader `Foundational literacy / numeracy` line combined the first two. In other words:

`Foundational literacy / numeracy = Modern FLN vocabulary + Basic skills`

That is why the older broad FLN line can look very similar to the `Basic skills` line in years when modern FLN terminology is still rare.

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

These two phrases are treated differently because they are more vague than the phrase families above. On their own, they do not automatically mean early reading, writing, or math. They could just mean something like `core learning` or `fundamental learning` in a broader sense.

So the code uses them only as a fallback rule. They count only when the surrounding text also makes clear that the document is talking about:

- young learners or primary-stage schooling
- reading, writing, literacy, numeracy, calculation, or math

Example:

- This would count: `apprentissages fondamentaux ... ecriture, lecture et calcul ... premieres annees du primaire`
- This would not count on this rule alone: `aprendizajes fundamentales para la vida`

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
