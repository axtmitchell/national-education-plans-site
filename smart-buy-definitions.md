# How We Defined Each Smart Buy (note to do: get rid of strict mentions, include french and spanish, include your validation attempt in here, just very simply, we reviewed a sample of x/y of the positive hits and agreed with the model xx% of the time). 

## Method At A Glance

1. **Broad retrieval.** A broader retrieval step combined weighted lexical cues with semantic query phrases.
2. **LLM review.** A model reviewed the retrieved chunks and labeled a category TRUE only when the evidence clearly matched the definition.

## Smart Buy Definitions

We defined the smart buys to the LLM below:

- `Information for schooling decisions`: families or learners are given decision-relevant information on school quality or on the costs and benefits of schooling.
- `Structured pedagogy`: a package combining teacher-facing classroom guidance, such as lesson plans or teacher guides, with ongoing support such as coaching, mentoring, or training.
- `Targeted instruction`: teaching or grouping students by their current learning level rather than by grade alone.
- `Parent-directed early stimulation`: parenting or caregiver support for very young children that clearly focuses on stimulation and child development.
- `Quality pre-primary education`: improving the quality of preschool or kindergarten education for children ages 3 to 5, not just expanding access.
- `Reducing travel barriers`: reducing the distance, time, or cost of getting children to school, for example through transport support or school-proximity measures.
- `Merit-based scholarships`: scholarships or financial incentives that are clearly tied to merit or performance.
- `School-based deworming`: school-based mass deworming in places where worm burden is a relevant concern.

## Click By Category

<details>
<summary><strong>Information for schooling decisions</strong> - Information on benefits, costs, or school quality that could shape choices</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(information campaign|targeted information|diagnostic feedback|providing information|information on the benefits|information on the costs|information on the quality)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \breturns?\s+to\s+education\b
(3) \bschool\s+quality\b
(3) \bcosts?\s+of\s+education\b
(3) \bbenefits?\s+of\s+education\b
(2) \binformation\b
(2) \binforming\b
(1) \bawareness\b
(1) \bcareer guidance\b
```

**Semantic retrieval query phrases**

```text
- information on returns, costs, or school quality to influence schooling decisions
- parents and students informed about education benefits and costs
- school choice information for parents and students
- information campaign on education benefits costs and quality
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \breturns?\s+to\s+education\b
(3) \brendements?\s+de\s+l[\s'’]?education\b
(3) \bschool\s+quality\b
(3) \bqualit[eé]\s+de\s+l[\s'’]?ecole\b
(3) \bcosts?\s+of\s+education\b
(3) \bcouts?\s+de\s+l[\s'’]?education\b
(3) \bbenefits?\s+of\s+education\b
(3) \bb[eé]n[eé]fices?\s+de\s+l[\s'’]?education\b
(3) \binformer?\s+les\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b
(3) \binformation\s+aux\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b
(3) \bcampagnes?\s+d[\s'’]?information\s+(?:aux|des)\s+(?:parents|familles|m[eé]nages|[eé]l[eè]ves?|apprenant(?:e)?s?)\b
(3) \bsensibilisation\s+des\s+(?:parents|familles|m[eé]nages)\b
(2) \bchoix\s+scolaire\b
(2) \bd[eé]cisions?\s+de\s+scolarisation\b
```

**Semantic retrieval query phrases**

```text
- provide parents families or students with information on education costs returns or school quality to influence enrolment or school choice
- family-facing information campaign on benefits costs or quality of schooling to shape decisions
- information aux parents ou familles sur les rendements les couts ou la qualite de l ecole pour influencer les decisions d inscription ou de maintien scolaire
- campagne ou diffusion d information aux menages sur le cout ou la qualite de l education pour orienter les choix scolaires
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_info
Definition: Providing information to families/learners on benefits, costs, or quality of education that changes schooling decisions.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic guidance, counselling, or awareness language without clear education costs, returns, or school-quality information", "generic stakeholder information about policies or grants without changing schooling decisions"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_info
Definition: Providing information directly to families, parents, or learners on the benefits, costs, or quality of schooling in order to inform whether, where, or how long children stay in school. Label TRUE only when the policy clearly disseminates decision-relevant information to households or learners; cost tables, budget data, parental monitoring tools, or generic school-life updates are not enough.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["internal cost tables, unit-cost calculations, or budget figures inside a plan without a family-facing information or disclosure mechanism", "generic communication or sensibilisation not clearly about informing households or learners on education benefits, costs, or school quality", "statements about what parents pay for schooling inside the document, without evidence that families are actively informed to shape schooling decisions", "parental engagement, suivi scolaire, school-life updates, or mobile monitoring tools that help parents track children already in school without providing decision-relevant information on returns, costs, or school quality", "communication with parents about attendance, school management, or real-time school monitoring rather than information intended to influence enrolment, continuation, or school choice"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Structured pedagogy</strong> - Classroom guidance plus ongoing teacher support</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(structured pedagogy|structured lesson plans|scripted lesson|direct instruction|teacher guide|teaching guide)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bstructured pedagogy\b
(3) \blesson plans?\b
(3) \bteacher guides?\b
(3) \bscripted lessons?\b
(2) \blearning materials?\b
(2) \bteacher mentoring\b
(2) \bcoaching\b
```

**Semantic retrieval query phrases**

```text
- structured pedagogy lesson plans learning materials teacher coaching
- teacher guides scripted lessons and mentoring package
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bstructured pedagogy\b
(3) \bp[eé]dagogie structur[ée]e\b
(3) \blesson plans?\b
(3) \bplans?\s+de\s+le[cç]on\b
(3) \bteacher guides?\b
(3) \bguides?\s+de\s+l[\s'’]?enseignant\b
(3) \bscripted lessons?\b
(3) \ble[cç]ons?\s+script[ée]es\b
(2) \bguides?\s+p[eé]dagogiques?\b
(2) \bmanuels?\s+de\s+l[\s'’]?enseignant\b
(2) \ble[cç]ons?\s+guid[ée]es\b
(2) \bmentor(?:at)?\s+des\s+enseignant(?:e)?s\b
(2) \baccompagnement p[eé]dagogique\b
```

**Semantic retrieval query phrases**

```text
- structured pedagogy package with lesson plans or teacher guides plus coaching or mentoring
- teacher guides scripted lessons and ongoing teacher support package
- pedagogie structuree avec plans de lecon ou guides de l enseignant et accompagnement des enseignants
- lecons scriptes guides pedagogiques et mentorat ou coaching des enseignants
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_structped
Definition: Structured pedagogy packages with lesson plans/materials and ongoing teacher support.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: []

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_structped
Definition: Structured pedagogy package with classroom guidance/materials plus teacher support. Label TRUE only when the intervention clearly combines at least two core package elements, such as lesson plans, teacher guides, scripted lessons, or teacher-facing materials together with training, coaching, or mentoring. Generic teacher training, manuals, modules, or materials alone are not enough.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic teacher training, methodology workshops, or capacity building without a clear package of lesson plans, teacher guides, or scripted lessons", "use or provision of manuals, modules, textbooks, or didactic materials alone without evidence of a structured pedagogy package", "generic pedagogical support, curriculum reform, or textbook provision without combined teacher-facing classroom guidance and ongoing support"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Targeted instruction</strong> - Teaching matched to a student's current learning level</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(teaching at the right level|tarl|targeted instruction|remedial education|differentiated instruction)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \btarl\b
(3) \bteaching at the right level\b
(3) \bgroup(?:ed|ing)? by (?:learning )?level\b
(3) \blevel-appropriate\b
(2) \blearning levels?\b
(2) \bability grouping\b
(1) \bcatch[- ]?up\b
(1) \bremedial\b
```

**Semantic retrieval query phrases**

```text
- Teaching at the Right Level TaRL grouping students by learning level
- level-appropriate targeted instruction catch-up by assessed level
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \btarl\b
(3) \bteaching at the right level\b
(3) \benseignement au bon niveau\b
(3) \bgroup(?:ed|ing)? by (?:learning )?level\b
(3) \bgroup(?:es|ement)?\s+de\s+niveau\b
(3) \bregroup(?:ement|er)?\s+des\s+[eé]l[eè]ves?\s+par\s+niveau\b
(3) \bpar niveau d[\s'’]?apprentissage\b
(3) \bselon (?:leur|le) niveau d[\s'’]?apprentissage\b
(3) \blevel-appropriate\b
(2) \blearning levels?\b
(2) \bniveaux?\s+d[\s'’]?apprentissage\b
(2) \bability grouping\b
(2) \binstruction cibl[ée]e?\s+par\s+niveau\b
(2) \bgroupes?\s+de\s+niveau\b
```

**Semantic retrieval query phrases**

```text
- Teaching at the Right Level TaRL grouping students by assessed learning level rather than grade
- targeted instruction after assessment with regrouping by current learning level
- enseignement au bon niveau avec regroupement des eleves par niveau d apprentissage plutot que par classe
- instruction ciblee fondee sur une evaluation diagnostique et un regroupement par niveau
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_targeted
Definition: Targeted instruction by learning level (TaRL-style), not by grade only.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: []

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_targeted
Definition: Targeted instruction by learning level (TaRL-style), not generic remediation or catch-up support. Label TRUE only when teaching or student grouping is explicitly organized by assessed learning level rather than age or grade only.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic remediation, rattrapage, or support for struggling students without clear grouping or teaching by assessed learning level", "screening, depistage, or diagnostic assessment alone without instruction organized by learning level", "depistage ou remediation des eleves en difficulte sans regroupement par niveau d apprentissage ou enseignement au bon niveau", "generic catch-up classes or support for low-performing students delivered by grade, not by current learning level"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Parent-directed early stimulation</strong> - Parent or caregiver support focused on early child development</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(parenting support|early childhood stimulation|parental guidance|early stimulation)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bparent(?:al)? education\b
(3) \bparenting education\b
(3) \bparenting lessons?\b
(3) \bparent-directed early childhood stimulation\b
(2) \bparenting\b
(2) \bearly childhood stimulation\b
(2) \bchild development\b
(1) \bhome visit(?:ing)?\b
(1) \bcaregiver(?:s)?\b
```

**Semantic retrieval query phrases**

```text
- parent-directed early childhood stimulation home visits caregivers
- parenting intervention for child stimulation ages 0 to 36 months
- parental education for child development and stimulation
- parenting lessons for caregivers of young children
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bparent(?:al)? education\b
(3) \b[eé]ducation parentale\b
(3) \bparenting education\b
(3) \bparenting lessons?\b
(3) \ble[cç]ons?\s+de\s+parentalit[eé]\b
(3) \bparent-directed early childhood stimulation\b
(3) \bstimulation pr[eé]coce\b
(2) \bparenting\b
(2) \bparentalit[eé]\b
(2) \bearly childhood stimulation\b
(2) \bstimulation de l[\s'’]?enfant\b
(2) \bchild development\b
(2) \bd[eé]veloppement de l[\s'’]?enfant\b
(1) \bhome visit(?:ing)?\b
(1) \bvisites?\s+[aà]\s+domicile\b
(1) \bcaregiver(?:s)?\b
(1) \baidant(?:e)?s?\b
```

**Semantic retrieval query phrases**

```text
- parent-directed early childhood stimulation home visits caregivers
- parenting intervention for child stimulation ages 0 to 36 months
- education parentale et stimulation precoce pour le developpement de l enfant
- programme de parentalite pour les aidants de jeunes enfants
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_parentstim
Definition: Parent-directed early childhood stimulation programs (0-36 months).

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic home visits with no clear parent-directed stimulation or child-development content", "generic parenting support or ECD references without stimulation or parent-training content"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_parentstim
Definition: Parent-directed early childhood stimulation programs (0-36 months).

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic home visits with no clear parent-directed stimulation or child-development content", "generic parenting support or ECD references without stimulation or parent-training content"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Quality pre-primary education</strong> - Pre-primary or preschool quality improvement for ages 3 to 5</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(preprimary education|preschool|school readiness|early years education|preschool teachers|nursery education|kindergarten)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bpre[- ]?primary\b
(3) \bpreschool\b
(3) \bkindergarten\b
(2) \bearly childhood education\b
(2) \becce\b
(2) \bearly years?\b
(2) \bteacher training\b
(2) \btraining of teachers\b
(2) \bprofessional preparation\b
```

**Semantic retrieval query phrases**

```text
- quality pre-primary education preschool ages 3 to 5
- kindergarten early years program
- teacher training for preschool or pre-primary education
- early childhood education quality improvement in preschool
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bpre[- ]?primary\b
(3) \bpr[eé][ -]?primaire\b
(3) \bpreschool\b
(3) \bpr[eé]scolaire\b
(3) \bkindergarten\b
(3) \bmaternelle\b
(2) \bearly childhood education\b
(2) \b[eé]ducation de la petite enfance\b
(2) \becce\b
(2) \bearly years?\b
(2) \bteacher training\b
(2) \bformation des enseignant(?:e)?s\b
(2) \btraining of teachers\b
(2) \bprofessional preparation\b
```

**Semantic retrieval query phrases**

```text
- quality pre-primary education preschool ages 3 to 5
- kindergarten early years program
- education preprimaire ou prescolaire de qualite pour les enfants de 3 a 5 ans
- amelioration de la qualite au prescolaire ou en maternelle
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_preprimary
Definition: Quality pre-primary education (ages 3-5).

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic pre-primary access or enrolment language with no quality-improvement content", "generic quality language near ECE without a clear intervention"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_preprimary
Definition: Quality pre-primary education (ages 3-5).

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic pre-primary access or enrolment language with no quality-improvement content", "generic quality language near ECE without a clear intervention"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Reducing travel barriers</strong> - Lowering distance, time, or transport barriers to schooling</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(school proximity|community schools|transport assistance|school transportation|providing transportation|access to schooling|remote areas|reduce distance to school)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bschool transport services?\b
(3) \bschool transport\b
(3) \bprovided with transport\b
(3) \btravel time\b
(2) \btransport(?:ation)?\b
(2) \bdistance to school\b
(2) \bschool proximity\b
(2) \bcommunity schools?\b
(1) \bremote areas?\b
```

**Semantic retrieval query phrases**

```text
- reduce travel time distance transport to school
- community schools school proximity transport assistance
- school transport services to get children to school
- transport to ferry children or students to school
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bschool transport services?\b
(3) \bservices?\s+de\s+transport scolaire\b
(3) \bschool transport\b
(3) \btransport scolaire\b
(3) \bprovided with transport\b
(3) \bramassage scolaire\b
(3) \btravel time\b
(3) \btemps de trajet\b
(2) \btransport(?:ation)?\b
(2) \bdistance to school\b
(2) \bdistance [aà] l[\s'’]?ecole\b
(2) \bschool proximity\b
(2) \bproximite de l[\s'’]?ecole\b
(2) \bcommunity schools?\b
(2) \b[eé]coles?\s+communautaires?\b
(1) \bremote areas?\b
(1) \bzones?\s+recul[ée]es\b
```

**Semantic retrieval query phrases**

```text
- reduce travel time distance transport to school
- community schools school proximity transport assistance
- reduction du temps de trajet ou de la distance jusqu a l ecole
- transport scolaire ou ecoles de proximite pour reduire les barriers d acces
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_travel
Definition: Reducing travel time/cost to school.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic transport references not clearly about reducing distance, time, or cost barriers to schooling"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_travel
Definition: Reducing travel time/cost to school.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic transport references not clearly about reducing distance, time, or cost barriers to schooling"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>Merit-based scholarships</strong> - Scholarships or financial incentives tied to performance</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(targeted scholarships|scholarships)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bmerit-based scholarships?\b
(3) \bperformance-based financial aid\b
(2) \bmerit\b
(2) \bperformance-based\b
(2) \bscholarships?\b
(1) \bawards?\b
(1) \bprizes?\b
```

**Semantic retrieval query phrases**

```text
- merit-based scholarship performance-based financial aid
- scholarship linked to academic achievement
- award or scholarship based on merit or performance
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bmerit-based scholarships?\b
(3) \bbourses?\s+au\s+m[eé]rite\b
(3) \bbourses?\s+d[\s'’]?excellence\b
(3) \bperformance-based financial aid\b
(2) \bmerit\b
(2) \bm[eé]rite\b
(2) \bperformance-based\b
(2) \bperformance\b
(2) \bscholarships?\b
(2) \bbourses?\b
(1) \bawards?\b
(1) \bprix\b
(1) \bprimes?\b
```

**Semantic retrieval query phrases**

```text
- merit-based scholarship performance-based financial aid
- scholarship linked to academic achievement
- bourses au merite ou bourses d excellence liees a la performance
- aide financiere ou prime liee aux resultats scolaires
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_merit
Definition: Merit-based scholarships or performance-linked incentives.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic selection on the basis of merit without scholarship, award, or financial support"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_merit
Definition: Merit-based scholarships or performance-linked incentives.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: ["generic selection on the basis of merit without scholarship, award, or financial support"]

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>
<details>
<summary><strong>School-based deworming</strong> - School delivery of deworming treatment</summary>

<details>
<summary>Show exact strict-screen terms</summary>

```text
(deworming)
```

</details>

<details>
<summary>Show English broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bschool-based de ?worming\b
(3) \bde ?worming of school (?:pupils|students|children)\b
(3) \bdeworm(?:ing)?\b
(2) \bde worming\b
(2) \bworm[- ]?load\b
(1) \bantihelminthic\b
(1) \bparasitic worms?\b
```

**Semantic retrieval query phrases**

```text
- school-based mass deworming worm-load high
- deworming treatment in schools for parasitic worms
- deworming of school pupils or students
```

</details>

<details>
<summary>Show French broad-retrieval terms</summary>

**Weighted lexical cues**

```text
(3) \bschool-based de ?worming\b
(3) \bd[eé]parasitage scolaire\b
(3) \bd[eé]parasitage de masse\b
(3) \bde ?worming of school (?:pupils|students|children)\b
(3) \bd[eé]parasitage des [eé]l[eè]ves\b
(3) \bdeworm(?:ing)?\b
(3) \bd[eé]parasitage\b
(2) \bde worming\b
(2) \bvermifugation\b
(2) \bworm[- ]?load\b
(2) \bcharge parasitaire\b
(1) \bantihelminthic\b
(1) \bparasitic worms?\b
(1) \bparasites? intestinaux\b
```

**Semantic retrieval query phrases**

```text
- school-based mass deworming worm-load high
- deworming treatment in schools for parasitic worms
- deparasitage scolaire de masse contre les parasites intestinaux
- traitement de deparasitage a l ecole pour les eleves
```

</details>

<details>
<summary>Show full classifier prompts</summary>

**English run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_deworm
Definition: School-based mass deworming where worm-load is high.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: []

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

**French run**

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: bb_deworm
Definition: School-based mass deworming where worm-load is high.

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: []

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

</details>

## How The Final Review Worked

The final review used the same general decision template across categories, but with category-specific definitions and hard negatives.

<details>
<summary>Show common decision template</summary>

```text
System:
You are a strict policy document classifier. Return only JSON matching schema.

User:
Best buy: <best_buy>
Definition: <definition>

Decision rules:
- Label TRUE when the evidence clearly matches the definition or clearly describes the same intervention idea.
- Evidence must be an exact quote from the provided chunks, <=25 words.
- Use only the quoted evidence and the provided chunks.
- If uncertain, set label=false.
- Do not use outside knowledge.

Hard negatives for this best buy: <hard_negative_list>

Document metadata: {"docid":"<docid>","title":"<title>","country":"<country>","year":"<year>","filename":"<filename>"}

Candidate evidence chunks:
[chunk 0] <retrieved text>
[chunk 1] <retrieved text>

Return: label, confidence, evidence, rationale.
In the rationale, briefly state which core components are present or missing.
```

</details>

## Source Files

- Strict regex macros: `code/06a_regex_macros.do` in the analysis project
- English broad retrieval and prompt code: `code/14_llm_rag_classify.py` in the analysis project
- French retrieval overrides: `code/best_buy_configs/french_rag_v1.py` in the analysis project
