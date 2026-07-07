# Methodology

## Overview

Each sector plan document was split into overlapping chunks of about `2,200` characters, with `250` characters of overlap.

For each smart buy, candidate chunks were retrieved in two ways:

- **Lexical retrieval:** weighted phrase searches looked for intervention-specific cues and synonyms. Stronger cues counted more than weaker cues. See "Lexical Cues And Semantic Queries" below
- **Semantic retrieval:** embeddings from Open AI's `text-embedding-3-small` were used to find chunks that were close in meaning to short descriptions of the intervention, even if they did not use the exact search terms.

The pipeline kept the top lexical and semantic hits, added nearby chunks for context.

Then, the model review then happened in two stages:

- `gpt-4.1-mini` made the first-pass classification.
- `gpt-4.1` reviewed positives and uncertain negatives.

The model had to return a structured JSON decision with a label, confidence score, rationale, and a short verbatim quote from the retrieved chunks.

## Validation

The validation checks were positive-side checks: we reviewed cases that the method had flagged as smart-buy mentions and judged whether they were real hits.

In the validation sample, `61` of `69` (88%) scored positives were judged correct.

## Retrieval Settings

- Text chunk size: `2,200` characters
- Chunk overlap: `250` characters
- Lexical candidates kept per smart buy per document: top `8` chunks with lexical score above zero
- Semantic candidates kept per smart buy per document: top `8` chunks by embedding similarity
- Candidate chunks sent to the model: at most `10`, after ranking the lexical/semantic union and adding neighbouring chunks for context
- Embedding model: Open AI's `text-embedding-3-small`
- Triage model: `gpt-4.1-mini`
- Verification model: `gpt-4.1`
- Verification rule: all positives and negatives with confidence below `0.60` were sent to the stronger model

Lexical score for a chunk was calculated as `sum(weight x number_of_regex_matches)` across the cue list for that smart buy. Semantic score was the maximum cosine similarity between the chunk embedding and the semantic query embeddings for that smart buy.

### Definitions Used By The Classifier

| Smart buy | Definition |
|---|---|
| Information (`bb_info`) | Providing information to families/learners on benefits, costs, or quality of education that changes schooling decisions. |
| Structured pedagogy (`bb_structped`) | Structured pedagogy packages with lesson plans/materials and ongoing teacher support. |
| Targeted instruction (`bb_targeted`) | Targeted instruction by learning level (TaRL-style), not by grade only. |
| Parent-directed early stimulation (`bb_parentstim`) | Parent-directed early childhood stimulation programs (0-36 months). |
| Quality pre-primary education (`bb_preprimary`) | Quality pre-primary education (ages 3-5). |
| Reducing travel barriers (`bb_travel`) | Reducing travel time/cost to school. |
| Merit scholarships / performance incentives (`bb_merit`) | Merit-based scholarships or performance-linked incentives. |
| School-based deworming (`bb_deworm`) | School-based mass deworming where worm-load is high. |

### Lexical Cues And Semantic Queries

<details>
<summary><strong>English</strong></summary>

#### Information (`bb_info`)

Lexical cues, shown as `(weight) regex`:

- `(3) \breturns?\s+to\s+education\b`
- `(3) \bschool\s+quality\b`
- `(3) \bcosts?\s+of\s+education\b`
- `(3) \bbenefits?\s+of\s+education\b`
- `(2) \binformation\b`
- `(2) \binforming\b`
- `(1) \bawareness\b`
- `(1) \bcareer guidance\b`

Semantic query phrases:

- `information on returns, costs, or school quality to influence schooling decisions`
- `parents and students informed about education benefits and costs`
- `school choice information for parents and students`
- `information campaign on education benefits costs and quality`

Hard negatives supplied to the classifier:

- `generic guidance, counselling, or awareness language without clear education costs, returns, or school-quality information`
- `generic stakeholder information about policies or grants without changing schooling decisions`

#### Structured pedagogy (`bb_structped`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bstructured pedagogy\b`
- `(3) \blesson plans?\b`
- `(3) \bteacher guides?\b`
- `(3) \bscripted lessons?\b`
- `(2) \blearning materials?\b`
- `(2) \bteacher mentoring\b`
- `(2) \bcoaching\b`

Semantic query phrases:

- `structured pedagogy lesson plans learning materials teacher coaching`
- `teacher guides scripted lessons and mentoring package`

#### Targeted instruction (`bb_targeted`)

Lexical cues, shown as `(weight) regex`:

- `(3) \btarl\b`
- `(3) \bteaching at the right level\b`
- `(3) \bgroup(?:ed|ing)? by (?:learning )?level\b`
- `(3) \blevel-appropriate\b`
- `(2) \blearning levels?\b`
- `(2) \bability grouping\b`
- `(1) \bcatch[- ]?up\b`
- `(1) \bremedial\b`

Semantic query phrases:

- `Teaching at the Right Level TaRL grouping students by learning level`
- `level-appropriate targeted instruction catch-up by assessed level`

#### Parent-directed early stimulation (`bb_parentstim`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bparent(?:al)? education\b`
- `(3) \bparenting education\b`
- `(3) \bparenting lessons?\b`
- `(3) \bparent-directed early childhood stimulation\b`
- `(2) \bparenting\b`
- `(2) \bearly childhood stimulation\b`
- `(2) \bchild development\b`
- `(1) \bhome visit(?:ing)?\b`
- `(1) \bcaregiver(?:s)?\b`

Semantic query phrases:

- `parent-directed early childhood stimulation home visits caregivers`
- `parenting intervention for child stimulation ages 0 to 36 months`
- `parental education for child development and stimulation`
- `parenting lessons for caregivers of young children`

Hard negatives supplied to the classifier:

- `generic home visits with no clear parent-directed stimulation or child-development content`
- `generic parenting support or ECD references without stimulation or parent-training content`

#### Quality pre-primary education (`bb_preprimary`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bpre[- ]?primary\b`
- `(3) \bpreschool\b`
- `(3) \bkindergarten\b`
- `(2) \bearly childhood education\b`
- `(2) \becce\b`
- `(2) \bearly years?\b`
- `(2) \bteacher training\b`
- `(2) \btraining of teachers\b`
- `(2) \bprofessional preparation\b`

Semantic query phrases:

- `quality pre-primary education preschool ages 3 to 5`
- `kindergarten early years program`
- `teacher training for preschool or pre-primary education`
- `early childhood education quality improvement in preschool`

Hard negatives supplied to the classifier:

- `generic pre-primary access or enrolment language with no quality-improvement content`
- `generic quality language near ECE without a clear intervention`

#### Reducing travel barriers (`bb_travel`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool transport services?\b`
- `(3) \bschool transport\b`
- `(3) \bprovided with transport\b`
- `(3) \btravel time\b`
- `(2) \btransport(?:ation)?\b`
- `(2) \bdistance to school\b`
- `(2) \bschool proximity\b`
- `(2) \bcommunity schools?\b`
- `(1) \bremote areas?\b`

Semantic query phrases:

- `reduce travel time distance transport to school`
- `community schools school proximity transport assistance`
- `school transport services to get children to school`
- `transport to ferry children or students to school`

Hard negatives supplied to the classifier:

- `generic transport references not clearly about reducing distance, time, or cost barriers to schooling`

#### Merit scholarships / performance incentives (`bb_merit`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bmerit-based scholarships?\b`
- `(3) \bperformance-based financial aid\b`
- `(2) \bmerit\b`
- `(2) \bperformance-based\b`
- `(2) \bscholarships?\b`
- `(1) \bawards?\b`
- `(1) \bprizes?\b`

Semantic query phrases:

- `merit-based scholarship performance-based financial aid`
- `scholarship linked to academic achievement`
- `award or scholarship based on merit or performance`

Hard negatives supplied to the classifier:

- `generic selection on the basis of merit without scholarship, award, or financial support`

#### School-based deworming (`bb_deworm`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool-based de ?worming\b`
- `(3) \bde ?worming of school (?:pupils|students|children)\b`
- `(3) \bdeworm(?:ing)?\b`
- `(2) \bde worming\b`
- `(2) \bworm[- ]?load\b`
- `(1) \bantihelminthic\b`
- `(1) \bparasitic worms?\b`

Semantic query phrases:

- `school-based mass deworming worm-load high`
- `deworming treatment in schools for parasitic worms`
- `deworming of school pupils or students`

</details>

<details>
<summary><strong>French</strong></summary>

#### Information (`bb_info`)

Lexical cues, shown as `(weight) regex`:

- `(3) \breturns?\s+to\s+education\b`
- `(3) \brendements?\s+de\s+l[\s'’]?education\b`
- `(3) \bschool\s+quality\b`
- `(3) \bqualit[eé]\s+de\s+l[\s'’]?ecole\b`
- `(3) \bcosts?\s+of\s+education\b`
- `(3) \bcouts?\s+de\s+l[\s'’]?education\b`
- `(3) \bbenefits?\s+of\s+education\b`
- `(3) \bb[eé]n[eé]fices?\s+de\s+l[\s'’]?education\b`
- `(3) \binformer?\s+les\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b`
- `(3) \binformation\s+aux\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b`
- `(3) \bcampagnes?\s+d[\s'’]?information\s+(?:aux|des)\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b`
- `(3) \bsensibilisation\s+des\s+(?:parents|familles|m[eé]nages)\b`
- `(2) \bchoix\s+scolaire\b`
- `(2) \bd[eé]cisions?\s+de\s+scolarisation\b`

Semantic query phrases:

- `provide parents families or students with information on education costs returns or school quality to influence enrolment or school choice`
- `family-facing information campaign on benefits costs or quality of schooling to shape decisions`
- `information aux parents ou familles sur les rendements les couts ou la qualite de l ecole pour influencer les decisions d inscription ou de maintien scolaire`
- `campagne ou diffusion d information aux menages sur le cout ou la qualite de l education pour orienter les choix scolaires`

Hard negatives supplied to the classifier:

- `internal cost tables, unit-cost calculations, or budget figures inside a plan without a family-facing information or disclosure mechanism`
- `generic communication or sensibilisation not clearly about informing households or learners on education benefits, costs, or school quality`
- `statements about what parents pay for schooling inside the document, without evidence that families are actively informed to shape schooling decisions`
- `parental engagement, suivi scolaire, school-life updates, or mobile monitoring tools that help parents track children already in school without providing decision-relevant information on returns, costs, or school quality`
- `communication with parents about attendance, school management, or real-time school monitoring rather than information intended to influence enrolment, continuation, or school choice`

#### Structured pedagogy (`bb_structped`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bstructured pedagogy\b`
- `(3) \bp[eé]dagogie structur[ée]e\b`
- `(3) \blesson plans?\b`
- `(3) \bplans?\s+de\s+le[cç]on\b`
- `(3) \bteacher guides?\b`
- `(3) \bguides?\s+de\s+l[\s'’]?enseignant\b`
- `(3) \bscripted lessons?\b`
- `(3) \ble[cç]ons?\s+script[ée]es\b`
- `(2) \bguides?\s+p[eé]dagogiques?\b`
- `(2) \bmanuels?\s+de\s+l[\s'’]?enseignant\b`
- `(2) \ble[cç]ons?\s+guid[ée]es\b`
- `(2) \bmentor(?:at)?\s+des\s+enseignant(?:e)?s\b`
- `(2) \baccompagnement p[eé]dagogique\b`

Semantic query phrases:

- `structured pedagogy package with lesson plans or teacher guides plus coaching or mentoring`
- `teacher guides scripted lessons and ongoing teacher support package`
- `pedagogie structuree avec plans de lecon ou guides de l enseignant et accompagnement des enseignants`
- `lecons scriptes guides pedagogiques et mentorat ou coaching des enseignants`

Hard negatives supplied to the classifier:

- `generic teacher training, methodology workshops, or capacity building without a clear package of lesson plans, teacher guides, or scripted lessons`
- `use or provision of manuals, modules, textbooks, or didactic materials alone without evidence of a structured pedagogy package`
- `generic pedagogical support, curriculum reform, or textbook provision without combined teacher-facing classroom guidance and ongoing support`

#### Targeted instruction (`bb_targeted`)

Lexical cues, shown as `(weight) regex`:

- `(3) \btarl\b`
- `(3) \bteaching at the right level\b`
- `(3) \benseignement au bon niveau\b`
- `(3) \bgroup(?:ed|ing)? by (?:learning )?level\b`
- `(3) \bgroup(?:es|ement)?\s+de\s+niveau\b`
- `(3) \bregroup(?:ement|er)?\s+des\s+[eé]l[eè]ves?\s+par\s+niveau\b`
- `(3) \bpar niveau d[\s'’]?apprentissage\b`
- `(3) \bselon (?:leur|le) niveau d[\s'’]?apprentissage\b`
- `(3) \blevel-appropriate\b`
- `(2) \blearning levels?\b`
- `(2) \bniveaux?\s+d[\s'’]?apprentissage\b`
- `(2) \bability grouping\b`
- `(2) \binstruction cibl[ée]e?\s+par\s+niveau\b`
- `(2) \bgroupes?\s+de\s+niveau\b`

Semantic query phrases:

- `Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade`
- `targeted instruction after assessment with regrouping by current learning level`
- `enseignement au bon niveau avec regroupement des eleves par niveau d apprentissage plutot que par classe`
- `instruction ciblee fondee sur une evaluation diagnostique et un regroupement par niveau`

Hard negatives supplied to the classifier:

- `generic remediation, rattrapage, or support for struggling students without clear grouping or teaching by assessed learning level`
- `screening, depistage, or diagnostic assessment alone without instruction organized by learning level`
- `depistage ou remediation des eleves en difficulte sans regroupement par niveau d apprentissage ou enseignement au bon niveau`
- `generic catch-up classes or support for low-performing students delivered by grade, not by current learning level`

#### Parent-directed early stimulation (`bb_parentstim`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bparent(?:al)? education\b`
- `(3) \b[eé]ducation parentale\b`
- `(3) \bparenting education\b`
- `(3) \bparenting lessons?\b`
- `(3) \ble[cç]ons?\s+de\s+parentalit[eé]\b`
- `(3) \bparent-directed early childhood stimulation\b`
- `(3) \bstimulation pr[eé]coce\b`
- `(2) \bparenting\b`
- `(2) \bparentalit[eé]\b`
- `(2) \bearly childhood stimulation\b`
- `(2) \bstimulation de l[\s'’]?enfant\b`
- `(2) \bchild development\b`
- `(2) \bd[eé]veloppement de l[\s'’]?enfant\b`
- `(1) \bhome visit(?:ing)?\b`
- `(1) \bvisites?\s+[aà]\s+domicile\b`
- `(1) \bcaregiver(?:s)?\b`
- `(1) \baidant(?:e)?s?\b`

Semantic query phrases:

- `parent-directed early childhood stimulation home visits caregivers`
- `parenting intervention for child stimulation ages 0 to 36 months`
- `education parentale et stimulation precoce pour le developpement de l enfant`
- `programme de parentalite pour les aidants de jeunes enfants`

Hard negatives supplied to the classifier:

- `generic home visits with no clear parent-directed stimulation or child-development content`
- `generic parenting support or ECD references without stimulation or parent-training content`

#### Quality pre-primary education (`bb_preprimary`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bpre[- ]?primary\b`
- `(3) \bpr[eé][ -]?primaire\b`
- `(3) \bpreschool\b`
- `(3) \bpr[eé]scolaire\b`
- `(3) \bkindergarten\b`
- `(3) \bmaternelle\b`
- `(2) \bearly childhood education\b`
- `(2) \b[eé]ducation de la petite enfance\b`
- `(2) \becce\b`
- `(2) \bearly years?\b`
- `(2) \bteacher training\b`
- `(2) \bformation des enseignant(?:e)?s\b`
- `(2) \btraining of teachers\b`
- `(2) \bprofessional preparation\b`

Semantic query phrases:

- `quality pre-primary education preschool ages 3 to 5`
- `kindergarten early years program`
- `education preprimaire ou prescolaire de qualite pour les enfants de 3 a 5 ans`
- `amelioration de la qualite au prescolaire ou en maternelle`

Hard negatives supplied to the classifier:

- `generic pre-primary access or enrolment language with no quality-improvement content`
- `generic quality language near ECE without a clear intervention`

#### Reducing travel barriers (`bb_travel`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool transport services?\b`
- `(3) \bservices?\s+de\s+transport scolaire\b`
- `(3) \bschool transport\b`
- `(3) \btransport scolaire\b`
- `(3) \bprovided with transport\b`
- `(3) \bramassage scolaire\b`
- `(3) \btravel time\b`
- `(3) \btemps de trajet\b`
- `(2) \btransport(?:ation)?\b`
- `(2) \bdistance to school\b`
- `(2) \bdistance [aà] l[\s'’]?ecole\b`
- `(2) \bschool proximity\b`
- `(2) \bproximite de l[\s'’]?ecole\b`
- `(2) \bcommunity schools?\b`
- `(2) \b[eé]coles?\s+communautaires?\b`
- `(1) \bremote areas?\b`
- `(1) \bzones?\s+recul[ée]es\b`

Semantic query phrases:

- `reduce travel time distance transport to school`
- `community schools school proximity transport assistance`
- `reduction du temps de trajet ou de la distance jusqu a l ecole`
- `transport scolaire ou ecoles de proximite pour reduire les barriers d acces`

Hard negatives supplied to the classifier:

- `generic transport references not clearly about reducing distance, time, or cost barriers to schooling`

#### Merit scholarships / performance incentives (`bb_merit`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bmerit-based scholarships?\b`
- `(3) \bbourses?\s+au\s+m[eé]rite\b`
- `(3) \bbourses?\s+d[\s'’]?excellence\b`
- `(3) \bperformance-based financial aid\b`
- `(2) \bmerit\b`
- `(2) \bm[eé]rite\b`
- `(2) \bperformance-based\b`
- `(2) \bperformance\b`
- `(2) \bscholarships?\b`
- `(2) \bbourses?\b`
- `(1) \bawards?\b`
- `(1) \bprix\b`
- `(1) \bprimes?\b`

Semantic query phrases:

- `merit-based scholarship performance-based financial aid`
- `scholarship linked to academic achievement`
- `bourses au merite ou bourses d excellence liees a la performance`
- `aide financiere ou prime liee aux resultats scolaires`

Hard negatives supplied to the classifier:

- `generic selection on the basis of merit without scholarship, award, or financial support`

#### School-based deworming (`bb_deworm`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool-based de ?worming\b`
- `(3) \bd[eé]parasitage scolaire\b`
- `(3) \bd[eé]parasitage de masse\b`
- `(3) \bde ?worming of school (?:pupils|students|children)\b`
- `(3) \bd[eé]parasitage des [eé]l[eè]ves\b`
- `(3) \bdeworm(?:ing)?\b`
- `(3) \bd[eé]parasitage\b`
- `(2) \bde worming\b`
- `(2) \bvermifugation\b`
- `(2) \bworm[- ]?load\b`
- `(2) \bcharge parasitaire\b`
- `(1) \bantihelminthic\b`
- `(1) \bparasitic worms?\b`
- `(1) \bparasites? intestinaux\b`

Semantic query phrases:

- `school-based mass deworming worm-load high`
- `deworming treatment in schools for parasitic worms`
- `deparasitage scolaire de masse contre les parasites intestinaux`
- `traitement de deparasitage a l ecole pour les eleves`

</details>

<details>
<summary><strong>Spanish</strong></summary>

#### Information (`bb_info`)

Lexical cues, shown as `(weight) regex`:

- `(3) \breturns?\s+to\s+education\b`
- `(3) \b(?:rendimientos?|retornos?)\s+de\s+la\s+educaci[oó]n\b`
- `(3) \bschool\s+quality\b`
- `(3) \bcalidad\s+(?:escolar|de\s+la[s]?\s+escuela[s]?)\b`
- `(3) \bcosts?\s+of\s+education\b`
- `(3) \b(?:costos?|costes?)\s+de\s+la\s+educaci[oó]n\b`
- `(3) \bbenefits?\s+of\s+education\b`
- `(3) \bbeneficios?\s+de\s+la\s+educaci[oó]n\b`
- `(3) \binformar\s+(?:a\s+)?(?:los\s+)?(?:padres|familias|hogares|estudiantes|alumnos|alumnas|aprendices)\b`
- `(3) \binformaci[oó]n\s+(?:a|para|dirigida\s+a)\s+(?:los\s+)?(?:padres|familias|hogares|estudiantes|alumnos|alumnas|aprendices)\b`
- `(3) \bcampa[nñ]as?\s+de\s+informaci[oó]n\s+(?:a|para|dirigidas?\s+a|sobre)\s+(?:los\s+)?(?:padres|familias|hogares|estudiantes|alumnos|alumnas|aprendices)\b`
- `(3) \bsensibilizaci[oó]n\s+de\s+(?:los\s+)?(?:padres|familias|hogares)\b`
- `(2) \belecci[oó]n\s+(?:escolar|de\s+escuela)\b`
- `(2) \bdecisiones\s+de\s+escolarizaci[oó]n\b`

Semantic query phrases:

- `provide parents families or students with information on education costs returns or school quality to influence enrolment or school choice`
- `family-facing information campaign on benefits costs or quality of schooling to shape decisions`
- `informacion a los padres familias o alumnos sobre los rendimientos los costos o la calidad de la escuela para influir en las decisiones de matricula o continuidad`
- `campana o difusion de informacion a los hogares sobre el costo o la calidad de la educacion para orientar las elecciones escolares`

Hard negatives supplied to the classifier:

- `internal cost tables, unit-cost calculations, or budget figures inside a plan without a family-facing information or disclosure mechanism`
- `generic communication or sensibilizacion not clearly about informing households or learners on education benefits, costs, or school quality`
- `generic statements about improving school quality or reducing education costs without a family-facing information or disclosure mechanism`
- `statements about what parents pay for schooling inside the document, without evidence that families are actively informed to shape schooling decisions`
- `parental engagement, seguimiento escolar, school-life updates, or mobile monitoring tools that help parents track children already in school without providing decision-relevant information on returns, costs, or school quality`
- `communication with parents about attendance, school management, or real-time school monitoring rather than information intended to influence enrolment, continuation, or school choice`

#### Structured pedagogy (`bb_structped`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bstructured pedagogy\b`
- `(3) \bpedagog[ií]a\s+estructurada\b`
- `(3) \blesson plans?\b`
- `(3) \bplanes?\s+de\s+(?:lecci[oó]n|clase|aula)\b`
- `(3) \bteacher guides?\b`
- `(3) \bgu[ií]as?\s+(?:del|para\s+el)\s+(?:docente|maestro|profesor)\b`
- `(3) \bscripted lessons?\b`
- `(3) \blecciones?\s+(?:guionadas|guiadas|estructuradas|con\s+gui[oó]n)\b`
- `(2) \bgu[ií]as?\s+pedag[oó]gicas?\b`
- `(2) \bmanuales?\s+(?:del|para\s+el)\s+(?:docente|maestro|profesor)\b`
- `(2) \bmentor[ií]a\s+(?:de|para)\s+(?:docentes|maestros|profesores)\b`
- `(2) \btutor[ií]a\s+(?:de|para)\s+(?:docentes|maestros|profesores)\b`
- `(2) \bacompa[nñ]amiento\s+pedag[oó]gico\b`

Semantic query phrases:

- `structured pedagogy package with lesson plans or teacher guides plus coaching or mentoring`
- `teacher guides scripted lessons and ongoing teacher support package`
- `pedagogia estructurada con planes de leccion o guias del docente y acompanamiento de los docentes`
- `lecciones guionadas guias pedagogicas y tutoria o mentoria de docentes`

Hard negatives supplied to the classifier:

- `generic teacher training, methodology workshops, or capacity building without a clear package of lesson plans, teacher guides, or scripted lessons`
- `use or provision of manuals, modules, textbooks, or didactic materials alone without evidence of a structured pedagogy package`
- `generic pedagogical support, curriculum reform, or textbook provision without combined teacher-facing classroom guidance and ongoing support`

#### Targeted instruction (`bb_targeted`)

Lexical cues, shown as `(weight) regex`:

- `(3) \btarl\b`
- `(3) \bteaching at the right level\b`
- `(3) \bense[nñ]anza\s+al\s+nivel\s+(?:adecuado|correcto|apropiado)\b`
- `(3) \bense[nñ]ar\s+al\s+nivel\s+(?:adecuado|correcto|apropiado)\b`
- `(3) \bgroup(?:ed|ing)? by (?:learning )?level\b`
- `(3) \bagrupa(?:ci[oó]n|miento)\s+por\s+nivel\b`
- `(3) \breagrupa(?:ci[oó]n|miento)?\s+(?:de\s+(?:estudiantes|alumnos|alumnas))?\s*por\s+nivel\b`
- `(3) \bpor\s+nivel\s+de\s+aprendizaje\b`
- `(3) \bseg[uú]n\s+(?:su|el)\s+nivel\s+de\s+aprendizaje\b`
- `(3) \blevel-appropriate\b`
- `(2) \blearning levels?\b`
- `(2) \bniveles?\s+de\s+aprendizaje\b`
- `(2) \bability grouping\b`
- `(2) \bagrupa(?:ci[oó]n|miento)\s+por\s+capacidad\b`
- `(2) \binstrucci[oó]n\s+focalizada\s+por\s+nivel\b`
- `(2) \bense[nñ]anza\s+focalizada\s+por\s+nivel\b`
- `(2) \bgrupos\s+de\s+nivel\b`

Semantic query phrases:

- `Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade`
- `targeted instruction after assessment with regrouping by current learning level`
- `ensenanza al nivel adecuado con reagrupacion de los estudiantes por nivel de aprendizaje en lugar de por grado`
- `instruccion focalizada basada en una evaluacion diagnostica y agrupacion por nivel`

Hard negatives supplied to the classifier:

- `generic remediation, nivelacion, refuerzo, or support for struggling students without clear grouping or teaching by assessed learning level`
- `screening or diagnostic assessment alone without instruction organized by learning level`
- `nivelacion o refuerzo de estudiantes con dificultades sin reagrupacion por nivel de aprendizaje o ensenanza al nivel adecuado`
- `generic catch-up classes or support for low-performing students delivered by grade, not by current learning level`

#### Parent-directed early stimulation (`bb_parentstim`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bparent(?:al)? education\b`
- `(3) \beducaci[oó]n\s+parental\b`
- `(3) \beducaci[oó]n\s+de\s+padres\b`
- `(3) \bparenting lessons?\b`
- `(3) \blecciones?\s+de\s+crianza\b`
- `(3) \bescuelas?\s+de\s+padres\b`
- `(3) \bparent-directed early childhood stimulation\b`
- `(3) \bestimulaci[oó]n\s+(?:temprana|precoz)\b`
- `(3) \bestimulaci[oó]n\s+de\s+la\s+primera\s+infancia\b`
- `(2) \bparenting\b`
- `(2) \bcrianza\b`
- `(2) \bparentalidad\b`
- `(2) \bearly childhood stimulation\b`
- `(2) \bchild development\b`
- `(2) \bdesarrollo\s+(?:infantil|del\s+ni[nñ]o|de\s+la\s+ni[nñ]ez)\b`
- `(1) \bhome visit(?:ing)?\b`
- `(1) \bvisitas?\s+(?:domiciliarias|a\s+domicilio|al\s+hogar)\b`
- `(1) \bcaregiver(?:s)?\b`
- `(1) \bcuidadores?(?:as?)?\b`

Semantic query phrases:

- `parent-directed early childhood stimulation home visits caregivers`
- `parenting intervention for child stimulation ages 0 to 36 months`
- `educacion parental y estimulacion temprana para el desarrollo del nino`
- `programa de crianza para cuidadores de ninos pequenos`

Hard negatives supplied to the classifier:

- `generic orientation, guidance, or communication to parents or tutors without explicit stimulation, child-development content, home visiting, or caregiver training`
- `general family participation, parent-school engagement, or escuela de padres language without clear focus on early stimulation or parenting practices for very young children`
- `generic early childhood or preschool services that mention parents but do not clearly train caregivers in stimulation, responsive caregiving, or child development`

#### Quality pre-primary education (`bb_preprimary`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bpre[- ]?primary\b`
- `(3) \bpre[- ]?primaria\b`
- `(3) \bpreschool\b`
- `(3) \bpreescolar\b`
- `(3) \bkindergarten\b`
- `(3) \bjard[ií]n\s+(?:de\s+(?:infantes|infancia|ni[nñ]os)|infantil)\b`
- `(2) \bearly childhood education\b`
- `(2) \beducaci[oó]n\s+(?:de\s+la\s+primera\s+infancia|inicial|infantil)\b`
- `(2) \becce\b`
- `(2) \bearly years?\b`
- `(2) \bteacher training\b`
- `(2) \bformaci[oó]n\s+(?:docente|de\s+(?:docentes|maestros|profesores))\b`
- `(2) \bcapacitaci[oó]n\s+(?:docente|de\s+(?:docentes|maestros|profesores))\b`
- `(2) \btraining of teachers\b`
- `(2) \bprofessional preparation\b`

Semantic query phrases:

- `quality pre-primary education preschool ages 3 to 5`
- `kindergarten early years program`
- `educacion preescolar o preprimaria de calidad para ninos de 3 a 5 anos`
- `mejora de la calidad en preescolar o jardin de infantes`

Hard negatives supplied to the classifier:

- `generic pre-primary access or enrolment language with no quality-improvement content`
- `generic quality language near ECE without a clear intervention`

#### Reducing travel barriers (`bb_travel`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool transport services?\b`
- `(3) \bservicios?\s+de\s+transporte\s+escolar\b`
- `(3) \bschool transport\b`
- `(3) \btransporte\s+escolar\b`
- `(3) \bprovided with transport\b`
- `(3) \btravel time\b`
- `(3) \btiempo\s+de\s+(?:viaje|trayecto|desplazamiento)\b`
- `(2) \btransport(?:ation)?\b`
- `(2) \btransporte\b`
- `(2) \bdistance to school\b`
- `(2) \bdistancia\s+(?:a|hasta|hacia)\s+la\s+escuela\b`
- `(2) \bschool proximity\b`
- `(2) \bproximidad\s+(?:a|de)\s+la\s+escuela\b`
- `(2) \bcommunity schools?\b`
- `(2) \bescuelas?\s+comunitarias?\b`
- `(1) \bremote areas?\b`
- `(1) \b(?:zonas|[aá]reas)\s+remotas\b`

Semantic query phrases:

- `reduce travel time distance transport to school`
- `community schools school proximity transport assistance`
- `reduccion del tiempo de viaje o de la distancia hasta la escuela`
- `transporte escolar o escuelas de proximidad para reducir las barreras de acceso`

Hard negatives supplied to the classifier:

- `generic transport references not clearly about reducing distance, time, or cost barriers to schooling`

#### Merit scholarships / performance incentives (`bb_merit`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bmerit-based scholarships?\b`
- `(3) \bbecas?\s+(?:por|de|basadas?\s+en\s+el)\s+m[eé]rito\b`
- `(3) \bbecas?\s+de\s+excelencia\b`
- `(3) \bperformance-based financial aid\b`
- `(3) \bayuda\s+(?:econ[oó]mica|financiera)\s+(?:por|basada\s+en\s+el)\s+(?:desempe[nñ]o|rendimiento)\b`
- `(2) \bmerit\b`
- `(2) \bm[eé]rito\b`
- `(2) \bperformance-based\b`
- `(2) \bperformance\b`
- `(2) \bscholarships?\b`
- `(2) \bbecas?\b`
- `(1) \bawards?\b`
- `(1) \bpremios?\b`

Semantic query phrases:

- `merit-based scholarship performance-based financial aid`
- `scholarship linked to academic achievement`
- `becas por merito o becas de excelencia ligadas al desempeno`
- `ayuda financiera o premio vinculado a los resultados escolares`

Hard negatives supplied to the classifier:

- `generic references to student performance, learning outcomes, or excellence without scholarships, awards, or financial support tied to that performance`
- `teacher merit, merit-based promotion, or staffing competitions without student scholarships, prizes, or financial incentives`
- `generic scholarships, grants, or student support with no clear merit or performance condition`

#### School-based deworming (`bb_deworm`)

Lexical cues, shown as `(weight) regex`:

- `(3) \bschool-based de ?worming\b`
- `(3) \bdesparasitaci[oó]n\s+escolar\b`
- `(3) \bdesparasitaci[oó]n\s+(?:masiva|en\s+masa)\b`
- `(3) \bde ?worming of school (?:pupils|students|children)\b`
- `(3) \bdesparasitaci[oó]n\s+de\s+(?:estudiantes|alumnos|ni[nñ]os)\b`
- `(3) \bdeworm(?:ing)?\b`
- `(3) \bdesparasitaci[oó]n\b`
- `(2) \bde worming\b`
- `(2) \bvermifugaci[oó]n\b`
- `(2) \bworm[- ]?load\b`
- `(2) \bcarga\s+parasitaria\b`
- `(1) \bantihelminthic\b`
- `(1) \bantihelm[ií]ntico\b`
- `(1) \bparasitic worms?\b`
- `(1) \bpar[aá]sitos\s+intestinales\b`

Semantic query phrases:

- `school-based mass deworming worm-load high`
- `deworming treatment in schools for parasitic worms`
- `desparasitacion escolar masiva contra parasitos intestinales`
- `tratamiento de desparasitacion en la escuela para los estudiantes`

</details>

### Generic LLM Prompt

The same prompt template was used for the triage and verification models. The stronger model received the same candidate chunks and rules when a case needed verification.

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: {best_buy}
Definition: {definition}

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: {hard_negatives_json}

Document metadata: {document_metadata_json}

Candidate evidence chunks:
{retrieved_chunks}

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

## Reproduction Files

1. `analysis/replication_01_clean_data.py`
   - prepares the input files under `output/replication/clean/`
2. `analysis/replication_02_run_rag.py`
3. `analysis/replication_03_make_graph.py`
4. `analysis/replication_04_make_sp_tarl_country_graphs.py`
   - combines the labelled English, French, and Spanish outputs and writes the country-stacked structured pedagogy and targeted instruction / TaRL graphs, plus the supporting country-year and research-timeline CSVs

The second script uses the OpenAI API. By default it prints the commands it would run; pass `--yes-run-api` to actually call the API. The third and fourth scripts can also use the already completed published RAG outputs with `--source published`, which is their default.
