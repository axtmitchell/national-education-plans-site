# RAG Validation Check

## What This Checks

This note reports a manual validation check of the positive predictions from the hybrid RAG smart-buy pipeline.

It is a `precision` check, not an overall accuracy check:

- we sampled predicted positives
- we manually judged whether each one was a real hit
- we report the share of reviewed positives that were true positives

Some rows were marked `maybe`. Those are shown separately and are not counted in the main precision denominator.

## Overall Result

From a positive-only validation sample of `57` rows:

- `49` were judged `yes`
- `4` were judged `no`
- `4` were judged `maybe`

Using only the rows judged `yes` or `no`:

- overall positive precision: `92.5%`
- overall false-positive rate: `7.5%`

## By Smart Buy

| Smart buy | Positive sample | Yes | No | Maybe | Scored positives | Precision | False-positive rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Information (`bb_info`) | 4 | 1 | 0 | 3 | 1 | 100.0% | 0.0% |
| Structured pedagogy (`bb_structped`) | 7 | 7 | 0 | 0 | 7 | 100.0% | 0.0% |
| Targeted instruction / TaRL (`bb_targeted`) | 4 | 3 | 0 | 1 | 3 | 100.0% | 0.0% |
| Parent stimulation (`bb_parentstim`) | 3 | 3 | 0 | 0 | 3 | 100.0% | 0.0% |
| Pre-primary (`bb_preprimary`) | 12 | 9 | 3 | 0 | 12 | 75.0% | 25.0% |
| Reduce travel (`bb_travel`) | 10 | 10 | 0 | 0 | 10 | 100.0% | 0.0% |
| Merit scholarships (`bb_merit`) | 12 | 11 | 1 | 0 | 12 | 91.7% | 8.3% |
| Mass deworming (`bb_deworm`) | 5 | 5 | 0 | 0 | 5 | 100.0% | 0.0% |

## Interpretation

The strongest categories in this validation sample were:

- `bb_structped`
- `bb_targeted`
- `bb_parentstim`
- `bb_travel`
- `bb_deworm`

The weaker categories were:

- `bb_preprimary`
- `bb_merit`

`bb_info` remains uncertain rather than clearly strong, because `3` of the `4` reviewed positives were marked `maybe`.

## Focused French Spot-Check For Pre-Primary And Merit

Because the later French extension added many new Francophone plans, I also did a small focused spot-check on the two categories that seemed easiest to mistrust on face value: `bb_preprimary` and `bb_merit`.

This was a manual review of the `8` positive review-sample rows for each category from:

- `output/nep_counted_llm_rag_french_full_v1_review.csv`

Where a short evidence quote felt too thin on its own, I also checked the surrounding document text in the full French `.dta` file before assigning a judgment.

| Smart buy | Positive sample | Yes | No | Positive-side precision | False-positive rate |
|---|---:|---:|---:|---:|---:|
| Pre-primary (`bb_preprimary`) | 8 | 7 | 1 | 87.5% | 12.5% |
| Merit scholarships / performance incentives (`bb_merit`) | 8 | 5 | 3 | 62.5% | 37.5% |

### What This Suggests

`bb_preprimary` looks imperfect but mostly real in the French run. The main false-positive pattern was preschool access or expansion language being treated as quality improvement. The clearest example was Côte d’Ivoire `2009`, where the model picked up expansion of `grande section` places for five-year-olds; that looks more like access than quality.

`bb_merit` looks materially shakier in the French run. The main problem was that the current category definition is broader than the short label makes it sound. The classifier was designed to count `merit-based scholarships or performance-linked incentives`, so prizes and awards to top-performing students were often counted as `TRUE`. If that broader definition is acceptable, some of these are defensible. But several French positives still looked too loose even under that broader definition, especially:

- a trainee-teacher bursary in Côte d’Ivoire `2009`
- scholarships for disadvantaged rural students in Congo `2021`
- larger subject-targeted scholarships in Guinea `2020`

So the main lesson is:

- `bb_preprimary`: broadly usable, but not perfectly clean
- `bb_merit`: should either be described more carefully or tightened further before being treated as a clean “merit scholarships” measure

## Method Note

Main files behind this check:

- RAG pilot dataset:
  - `output/nep_counted_llm_rag_pilot_80.dta`
- Manual review sample:
  - `output/nep_counted_llm_rag_pilot_80_manual_validation.csv`
- Focused French spot-check:
  - `output/french_preprimary_merit_manual_validation_2026-04-29.csv`
- Computed summary table:
  - `output/nep_counted_llm_rag_pilot_80_manual_validation_summary_full.csv`

This note should be described as:

- a manual validation of predicted positives from the RAG pipeline

It should not be described as:

- overall model accuracy
- recall
- a complete estimate of missed mentions
