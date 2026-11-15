# Controlled sentiment generation
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Sentiment control, Sentiment expression, Sentiment generation, Sentiment, Sentiment revising, Sentiment steering  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is controlling the emotional tone of generated text so it follows a target sentiment, most often positive or negative, sometimes explicitly given a context. Definitions variously call this sentiment control, steering, expression, or generation, but they largely agree that success means the output conveys the requested polarity; one study describes "controlling the sentiment in generated text," and another presents "zero-shot sentiment steering" by replacing a token with "positive" or "negative" (Unveiling and Manipulating Prompt Influence in Large Language Models). A smaller line of work frames it as revising existing text, such as removing negative sentiment, or continuing from an initial sentiment state with the opposite sentiment.

**Variants.** Papers study several named variants, including sentiment control, sentiment steering, sentiment expression, sentiment generation, sentiment revising, and sentiment polarity control. A recurring setting uses movie reviews with positive and negative targets, though some work steers toward tones such as happy or angry, some forces continuations to switch to the opposite sentiment, and some focuses on revising sensitive-topic responses to remove negative sentiment. One study also frames the task as balancing positive sentiment and conciseness in generated movie reviews (MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment).

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments. The most frequent is IMDb, explicitly described as a large movie review dataset and used for controlled sentiment generation, including subsets with separate positive and negative sentiment control; SST-5 is also used for sentiment steering. Across these uses, movie review resources are the recurrent way papers elicit or assess the behavior.

**What it is taken as evidence of.** Papers do not link this behavior to any construct, so they do not explicitly treat it as evidence of a named construct here.

## Sources

**Sentiment control** (3 papers: [Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/294fd30f8cbb89ce328d5a01fef47fb4-Paper-Conference.pdf), [Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf), [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf))
> Generating text that adheres to a specific sentiment polarity (e.g., positive or negative) given a context.

**Sentiment expression** (1 paper: [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf))
> The generation of text that conveys a specific emotional tone, such as positive or negative sentiment.

**Sentiment generation** (1 paper: [MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25af/wang25af.pdf))
> The task of generating text, such as movie reviews, that exhibits a specific emotional tone like positive sentiment.

**Sentiment** (1 paper: [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf))
> The underlying emotional or affective tone (e.g., positive or negative) that a model's generated text is intended to convey.

**Sentiment revising** (1 paper: [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf))
> The task of altering the emotional tone of a model's generated text, such as removing negative sentiment when discussing sensitive topics.

**Sentiment steering** (2 papers: [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf), [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf))
> The task of controlling the emotional tone (e.g., positive or negative) of the generated text.

## Relationships

### Controlled sentiment generation →
- **IMDb** (measurement instrument): *measured_by*, 4 papers
  > For controlled sentiment generation task, we employ the IMDB dataset (Maas et al., 2011), which is a large movie review dataset. (Section 4)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf)
  - [MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25af/wang25af.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **SST-5** (measurement instrument): *measured_by*, 1 paper
  > using Stanford Sentiment Treebank (SST5) (Socher et al., 2013) for sentiment steering (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
