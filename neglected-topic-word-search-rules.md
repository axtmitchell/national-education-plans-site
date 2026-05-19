# Figure 1 Word-Search Rules

Before matching, text is lowercased, accents are stripped, and minor punctuation variants are ignored.
`n` is the number of LMIC plans in this corpus containing that phrase or rule. Counts overlap.

## Learning Crisis

- English: `global learning crisis` (`n=2`), `learning crisis` (`n=12`), `learning poverty` (`n=8`)
- French: `crise des apprentissages` (`n=1`), `crise de l apprentissage` (`n=0`), `crise des apprentissage` (`n=1`), `pauvrete des apprentissages` (`n=0`), `pauvrete de l apprentissage` (`n=0`)
- Spanish: `crisis de aprendizaje` (`n=0`), `crisis del aprendizaje` (`n=0`), `pobreza de aprendizaje` (`n=0`)

## Foundational Learning

### English

- `foundational literacy` (`n=16`)
- `foundational numeracy` (`n=0`)
- `fln` (`n=3`)

### Spanish

- `habilidades fundacionales` (`n=0`)
- `lectoescritura` with nearby `matematicas`, `matematico`, or `matematica` (`n=3`)

### French

- `litteratie` together with `numeratie` (`n=3`)
- `competences fondamentales` with `lecture` and `calcul` or `mathematiques` (`n=3`)
