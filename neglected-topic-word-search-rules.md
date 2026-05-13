# Neglected-Topic Word-Search Rules

## Matching Notes

- Text is lowercased before matching.
- Accents are stripped before matching, so `éducation` is matched as `education`.
- Minor punctuation, spacing, and hyphen variants are allowed in code. The lists below show the readable phrase forms.
- For `Foundational literacy / numeracy`, the title and body text are checked together because the schooling stage is sometimes signaled in the title.

### Learning Crisis

The rule fires on any of these direct phrases:

- English: `global learning crisis`, `learning crisis`, `learning poverty`
- French: `crise des apprentissages`, `crise de l apprentissage`, `crise des apprentissage`, `pauvrete des apprentissages`, `pauvrete de l apprentissage`
- Spanish: `crisis de aprendizaje`, `crisis del aprendizaje`, `pobreza de aprendizaje`

### Foundational Literacy / Numeracy

This category has three layers.

Direct modern FLN phrases count on their own:

- English: `foundational literacy`, `foundational numeracy`, `foundational literacy and numeracy`, `fln`

Basic literacy-numeracy phrases count only when they appear in a nearby early-childhood, pre-primary, primary, or early-grade context:

- English: `literacy and numeracy`, `basic literacy and numeracy`, `reading writing arithmetic`, `reading writing numeracy`, `reading writing mathematics`, `reading writing math`
- French: `litteratie`, `numeratie`, `lecture ecriture calcul`, `lire ecrire compter`
- Spanish: `lectoescritura`, `lectura escritura calculo`

Broader basic-learning phrases also require a nearby early-childhood, pre-primary, primary, or early-grade context, plus nearby literacy-numeracy wording:

- French: `apprentissages fondamentaux`
- Spanish: `aprendizajes fundamentales`

Age or schooling-stage phrases checked for this category include:

- English: `early grade`, `early grades`, `early years`, `early primary`, `primary class`, `primary classes`, `primary stage`, `elementary`, `pre-primary`, `preschool`, `kindergarten`, `early childhood`, `lower primary`, `eced`, `grade 1`, `grade 2`, `grade 3`, `first years of school`
- French: `education de base`, `enseignement primaire`, `ecole primaire`, `primaire`, `elementaire`, `preprimaire`, `prescolaire`, `preelementaire`, `petite enfance`, `premier cycle`, `premieres annees`
- Spanish: `nivel primario`, `educacion primaria`, `primaria`, `preescolar`, `preprimaria`, `educacion inicial`, `primera infancia`, `primeros grados`, `primer ciclo`

The FLN rule also excludes nearby language that clearly points to older or broader populations rather than young learners:

- English: `adult literacy`, `adult education`, `adult learners`, `lifelong learning`, `non-formal education`, `nfe programme`, `prevocational`, `higher education`, `tertiary`
- French: `alphabetisation des adultes`, `education non formelle`, `formation des adultes`, `apprentissage tout au long de la vie`
- Spanish: `alfabetizacion de adultos`, `educacion de adultos`, `educacion no formal`, `aprendizaje a lo largo de la vida`

