# Methodology Overview

The site uses two layers of measurement.

First, there is a conservative strict phrase search. This is the lower-bound screen that looks for relatively direct mentions of the smart buys.

Second, there is a broader retrieval-and-verification workflow. This broader layer combines weighted lexical search terms, embedding-based semantic retrieval, and final LLM review of the retrieved text.

## What To Read Next

- [Strict and broad smart-buy mentions](strict-and-broad-smart-buy-mentions.md) explains how the strict and broad figures fit together.
- [RAG method](rag-method.md) gives the plain-English explanation of the broader workflow.
- [RAG validation](rag-validation.md) reports the positive-side validation checks.
- [Smart-buy definitions and prompts](smart-buy-definitions.md) records the exact terms, prompts, and category definitions.
- [Worked example: targeted instruction](targeted-instruction-worked-example.md) walks through one category step by step.

## Design Principle

The main goal of the broader method is not to let an LLM read entire plans from scratch. Instead, the retrieval stage first narrows each document to the most relevant chunks, and only then asks the model to decide whether those chunks really describe the intervention.

That makes the broader screen more auditable, cheaper, and easier to validate than a single full-document LLM pass.
