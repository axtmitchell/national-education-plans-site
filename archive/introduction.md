# Introduction

This site asks a simple question: when governments write education plans, how often do they describe the kinds of interventions that research suggests improve learning?

The underlying analysis starts from UNESCO Planipolis documents. In the English or English-accessible sample, the main smart-buy analysis uses `528` plans from `101` countries spanning roughly three decades. We then compare a strict reviewed phrase search with a broader retrieval-and-LLM screen that tries to capture the same intervention ideas even when plans do not use the canonical labels.

The GitBook version is designed to be easier to edit in the browser than the earlier Quarto site. That means the emphasis here is on clean Markdown pages, simple navigation, and readable supporting notes rather than Quarto-specific styling or features.

## Main Sections

- [Findings overview](findings.md) gives the shortest route through the main results.
- [Government plans and smart buys](government-plans-smart-buys.md) is the main narrative findings page.
- [Methodology overview](methodology.md) explains how the strict and broad searches work.
- [Smart-buy definitions and prompts](smart-buy-definitions.md) records the exact search logic behind the broader method.

## What Changed In This Migration

The earlier site was Quarto-first. In this repo:

- Quarto-specific syntax has been removed or simplified where possible.
- Pages are now standard Markdown files.
- Figures used by the pages have been copied into `assets/figures/`.
- The navigation is controlled entirely through `SUMMARY.md`.
