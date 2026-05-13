# Neglected-Topic Word-Search Rules

This page records the exact phrase logic used for the multilingual neglected-topic trend chart.

The chart is still a phrase screen rather than a broad retrieval system. It does not use semantic search or LLM review.

## Matching Notes

- Text is lowercased before matching.
- Accents are stripped before matching, so `éducation` is matched as `education`.
- Minor punctuation, spacing, and hyphen variants are allowed in code. The lists below show the readable phrase forms.
- For `Foundational literacy / numeracy`, the title and body text are checked together because the schooling stage is sometimes signaled in the title.

## Exact Rules By Topic

### School Violence

The rule fires on any of these direct phrases:

- English: `school-related gender-based violence`, `gender-based violence in schools`, `school violence`, `violence in school`, `violence in schools`, `anti-bullying`, `bullying`, `corporal punishment`, `safeguarding`, `abuse in school`, `abuse in schools`, `harassment in school`, `harassment in schools`
- French: `violence scolaire`, `violences scolaires`, `violence en milieu scolaire`, `violences en milieu scolaire`, `violence dans le milieu scolaire`, `violence a l ecole`, `harcelement scolaire`, `harcelement en milieu scolaire`, `chatiment corporel`, `chatiments corporels`, `violence basee sur le genre en milieu scolaire`, `violence sexuelle en milieu scolaire`, `abus en milieu scolaire`
- Spanish: `violencia escolar`, `violencia en la escuela`, `violencia en las escuelas`, `violencias en el entorno educativo`, `acoso escolar`, `castigo corporal`, `violencia basada en genero en el entorno educativo`, `violencia de genero en la escuela`, `violencia de genero en las escuelas`

### School Meals

The rule fires on any of these direct phrases:

- English: `school meal`, `school meals`, `school feeding`, `school breakfast`, `school lunch`, `school nutrition`, `take-home ration`, `mid-day meal`, `midday meal`, `school canteen`
- French: `cantine scolaire`, `cantines scolaires`, `alimentation scolaire`, `repas scolaire`, `repas scolaires`, `programme d alimentation scolaire`
- Spanish: `alimentacion escolar`, `alimentacion complementaria escolar`, `desayuno escolar`, `almuerzo escolar`, `merienda escolar`, `comedor escolar`, `comedores escolares`, `nutricion escolar`

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

### Lead Exposure

The rule fires on any of these direct phrases:

- English: `lead exposure`, `exposure to lead`, `lead poisoning`, `blood lead`, `lead paint`, `lead contamination`, `lead contaminated`, `lead in drinking water`, `lead hazard`
- French: `exposition au plomb`, `intoxication au plomb`, `empoisonnement au plomb`, `saturnisme`, `peinture au plomb`, `contamination au plomb`, `plomb dans l eau potable`
- Spanish: `exposicion al plomo`, `intoxicacion por plomo`, `envenenamiento por plomo`, `pintura con plomo`, `pinturas con plomo`, `contaminacion por plomo`, `plomo en el agua potable`

In the current corpus, these lead phrases mostly hit environmental and safeguards annex language rather than core education-priority discussion.

## Related Page

For the broader mixed page that also includes the multilingual strict smart-buy phrase screen, see [Multilingual phrase rules](multilingual-strict-phrases.md).
