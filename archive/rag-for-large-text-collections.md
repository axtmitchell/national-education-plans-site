# A Simple RAG Workflow for Large Text Collections

This note is a short plain-English summary of the retrieval-augmented generation (RAG) method I used to work through a large document collection. It should also transfer quite well to other corpora, such as conference transcripts.

## Why use this approach?

If you have hundreds of long documents, there is a gap between:

- a simple keyword search, which is fast but misses paraphrases and produces noise
- asking an LLM to read every full document, which is expensive and hard to audit

RAG sits in the middle. It first pulls the most relevant passages, then asks a model to judge only those passages.

## The basic workflow

1. Clean the text and split each document into manageable chunks.
2. For each topic or category, run a broad retrieval step to find chunks that might be relevant.
3. Send only those shortlisted chunks to a language model.
4. Ask the model to decide whether the text really matches the concept you care about.
5. Require the model to return a short quote as evidence.
6. Review a sample of positives and tighten the rules if the method is drifting.

That means the model is not doing a free-form reading of the whole corpus. It is doing a much narrower verification task on text that has already been screened.

## How the retrieval step worked

I used two retrieval signals together:

- a lexical search, using weighted phrases and synonyms
- a semantic search, using embeddings to find chunks that were close in meaning even when they used different words

The retrieval step was deliberately broad. Its job was to catch plausible candidates, not to make the final decision.

## How the ChatGPT API was used

I used the API in three places:

- `text-embedding-3-small` to turn chunks and query phrases into embeddings for semantic retrieval
- `gpt-4.1-mini` as a cheaper first-pass classifier on the shortlisted chunks
- `gpt-4.1` as a stronger second-pass verifier for positives and uncertain cases

In other words:

- embeddings helped find relevant passages
- the smaller model handled most of the routine screening
- the stronger model handled the tougher judgment calls

## What made the method more reliable

A few design choices mattered:

- the model only saw retrieved chunks, not whole documents
- it had to classify conservatively rather than guess
- it had to return a short verbatim quote as evidence
- I manually reviewed samples of flagged positives and tightened the rules where needed

So the aim was not to prove that every possible mention had been found. The aim was to make the positive hits interpretable and auditable.

## What it cost in this project

In this project, the completed broad RAG runs cost about:

- `$3.04` for `528` English plans
- `$4.00` for `155` French plans
- `$1.86` for `60` Spanish plans

That is about `$8.89` in total for `743` plans.

The exact cost will vary a lot by corpus size, chunking choices, the number of concepts you are screening for, and how often you send cases to the stronger model.

## Why this could work for conference transcripts

For transcripts, I would use the same basic logic:

- split each transcript into chunks
- retrieve candidate passages for the themes you care about
- have the model judge only those passages
- save the evidence quotes and review a sample

That usually works better than either raw keyword search or a single full-document prompt, especially when speakers use varied language to describe the same underlying idea.
