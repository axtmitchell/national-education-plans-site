# Figure 1 Word-Search Rules

Before matching, text is lowercased, accents are stripped, and minor punctuation variants are ignored.

`n` is the number of LMIC plans in this corpus containing that phrase or rule. Counts overlap.

## Learning Crisis

- English: `learning crisis` (`n=12`), `learning poverty` (`n=8`)
- French: `crise des apprentissages` or `crise de l apprentissage` (`n=0`), `pauvrete des apprentissages` or `pauvrete de l apprentissage` (`n=0`)
- Spanish: `crisis de aprendizaje` or `crisis del aprendizaje` (`n=0`), `pobreza de aprendizaje` (`n=0`)

## Foundational Learning

- English: `foundational literacy` (`n=16`), `foundational numeracy` (`n=0`), `fln` (`n=3`)
- Spanish: `habilidades fundacionales` (`n=0`), `lectoescritura` within 35 characters of `matematicas`, `matematico`, or `matematica` (`n=3`)
- French: `litteratie` within 25 characters of `numeratie` (`n=3`), `competences fondamentales` within 35 characters of `lecture` and `calcul` or `mathematiques` (`n=3`)

No broader `Basic skills` terms and no primary-school context screen are used in this graph.
