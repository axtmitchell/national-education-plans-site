# How The Topic Model Works

This note explains the process behind the topic charts used in the education-plans analysis.

## What this method is for

The topic-model workflow is different from the smart-buy analysis.

The smart-buy work starts with a known concept and asks whether a plan mentions it. The topic-model workflow is more exploratory. It asks a different question: if we do not pre-specify the categories, what broad themes tend to recur across education plans?

That makes it useful for:

- summarising the main themes that appear across plans
- comparing those themes across income groups or over time
- checking whether certain topics become more or less common in the corpus

## The basic idea

Instead of treating each plan as a single block of text, the workflow breaks plans into overlapping chunks, groups similar chunks together, and then reviews those groups by hand to turn them into a smaller set of interpretable themes.

In plain English, the process has four steps.

## 1. Split each plan into overlapping chunks

Education plans are long and usually cover many topics at once. A single document might discuss access, teacher policy, disability inclusion, digital learning, higher education, and emergency planning all in different sections.

If the model looked only at whole documents, those themes would blur together. Chunking helps the model recover the fact that one document can contain several distinct substantive discussions.

## 2. Turn the chunks into embeddings

Each chunk is converted into a numerical representation, or embedding, that captures its meaning. Chunks that talk about similar ideas should end up close together in that semantic space even if they do not use exactly the same words.

This is what lets the workflow group conceptually similar passages rather than relying only on literal keyword overlap.

## 3. Cluster similar chunks into raw topics

The model then groups nearby chunks into raw clusters. Each cluster is a candidate topic: a recurring type of language that appears across multiple plans.

At this stage, the output is still rough. Some clusters are substantively clear, while others reflect planning boilerplate, administrative language, or a mixture of several ideas.

## 4. Review and curate the raw topics

The raw clusters are not used directly in the final charts.

Instead, representative chunks from each cluster are reviewed by hand, noisy or unhelpful clusters are excluded, and the useful ones are translated into a smaller set of readable themes. That is how short labels such as `Access`, `Learning quality`, or `Emergency response` are produced.

So the final chart labels are not fully automatic machine-generated topics. They are curated summaries built from the raw model output.

## How the chart percentages are constructed

After curation, each document gets a weight for each theme.

For the bar charts, a plan is counted as mentioning a topic when that theme accounts for at least 15 percent of the document's topic weight. The bars therefore show how common substantive discussion of a topic is within a group of plans.

This also means the categories are not mutually exclusive. A single plan can count toward more than one topic if it contains meaningful discussion of several themes.

## What the short labels do and do not mean

The short topic labels are shorthand rather than perfectly crisp policy categories.

For example:

- `Learning quality` includes not only direct references to learning outcomes, but also teachers, pedagogy, curriculum, standards, and assessment
- `Higher education` can also pick up skills, research, and innovation language
- `Inclusion` is narrower and more targeted than `Access`, and usually refers to disability, girls' education, and support for excluded groups

So the charts should be read as a structured summary of what governments choose to talk about in education plans, not as a direct measure of spending, implementation, or impact.

## Strengths and limits

This approach is useful for broad thematic comparison, but it has limits.

It is good for:

- surfacing the most common themes in a large set of plans
- comparing broad emphases across groups of countries
- showing how themes shift over time

It is less good for:

- making precise claims about narrow concepts
- treating the labels as mutually exclusive categories
- measuring how much policy effort or funding governments devote to each area

The right way to read the topic charts, then, is as an organized picture of what governments discuss in official education planning documents.
