# Worked Example: Targeted Instruction (Short)

This is a short example of how the broader AI method looked for targeted instruction: teaching or grouping students by their current learning level rather than by grade alone.

## The short version

This was not a simple keyword search, but it was not a free-form AI read of whole documents either.

Instead, the method started very broad and looked for passages that seemed potentially relevant, using both search terms and meaning-based retrieval. It then asked a stronger model to decide whether those passages really described the intervention and to return a short quote as evidence.

We tightened the method when early review samples looked too loose, and we manually checked predicted positives at several stages. In the English validation sample, `49` of `53` scored positives were judged real hits (`92.5%`). Targeted instruction itself looked especially strong in that spot-check, although the review sample was small.

So the main claim is not that this method found every mention. The claim is that when it says a plan mentions targeted instruction, that is usually for a good reason.

## Short working definition

For this category, a passage counted as a hit only if it clearly described teaching or grouping students by their current learning level.

It did not count if the text only described:

- generic remediation
- catch-up support
- diagnostic assessment on its own

For the exact term lists, prompts, and fuller definitions, see [How We Defined Each Smart Buy](smart-buy-definitions.md).
