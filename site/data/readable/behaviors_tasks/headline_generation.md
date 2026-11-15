# Headline generation
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** News headline generation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats headline generation as producing a short title from a source text, commonly described as concise and relevant, and sometimes as engaging. Some authors narrow the task to news articles, and one ablation uses it as an alternate content choice by instructing the model to produce a news headline rather than a tweet. Success is described in terms such as generating concise, contextually accurate headlines and assessing performance on annotated data.

**Variants.** Papers use both the broader label headline generation and the narrower news headline generation. Studied settings include minority-language headline generation in Tibetan, Uyghur, and Mongolian, and some work examines it alongside summarization across four configurations.

**Space of elicitation and scores.** One measurement instrument is linked to this behavior: LaMP, which includes LaMP-4, news headline generation, and is used to measure it. Beyond that linked instrument, some evaluations use high-quality annotated data and report ROUGE-L scores for generated headlines.

**What it is taken as evidence of.** No constructs are linked to headline generation, and papers do not connect it to a broader construct in the recorded relationships.

## Sources

**Headline generation** (2 papers: [CMHG: A Dataset and Benchmark for Headline Generation of Minority Languages in China](https://aclanthology.org/2025.emnlp-main.622.pdf), [COSMMIC: Comment-Sensitive Multimodal Multilingual Indian Corpus for Summarization and Headline Generation](https://aclanthology.org/2025.acl-long.427.pdf))
> The observable task of producing a concise and relevant title for a given body of text.

**News headline generation** (1 paper: [Anecdoctoring: Automated Red-Teaming Across Language and Place](https://aclanthology.org/2025.emnlp-main.964.pdf))
> The task of creating a concise title for a news article, used as an alternative content format in an ablation study.

## Relationships

### Headline generation →
- **LaMP** (measurement instrument): *measured_by*, 1 paper
  > "Specifically, we include LaMP-1 (citation identification), LaMP-2 (movie tagging), LaMP-3 (Amazon product rating), LaMP-4 (news headline generation) and LaMP-5 (scholarly title generation)"
  - [PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711.pdf)
