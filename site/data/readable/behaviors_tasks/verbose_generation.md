# Verbose generation
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Overgeneration, Overly verbose generation, Verbose response generation, Response length generation, Unnecessarily lengthy output generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is outputs that are longer or wordier than needed for the prompt or task. Most definitions treat it as excessive length, often with redundant or irrelevant continuation; some add that it can continue until the maximum generation length and become incoherent, or that an answer may begin correctly but then keep going with unrelated content that lowers evaluation scores. Papers also frame the threshold relative to desired conciseness or task complexity, and one study describes models as producing "longer and more verbose captions than top human ones" (Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning).

**Variants.** Papers use several nearby names, most often overgeneration, overly verbose generation, verbose response generation, response length generation, and unnecessarily lengthy output generation. The behavior appears in settings such as captioning, general prompt answering, and cases where a model gives the correct answer first but then adds unrelated material. A smaller line of work treats it more neutrally as response length with measurable word counts that vary by model, prompt, and decoding settings.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it through conciseness judgments, comparisons against human or baseline outputs, measurable word counts, and score reductions such as lower F1 or ROUGE-L when correct answers are followed by irrelevant continuation.

**What it is taken as evidence of.** No construct is linked to it, so papers here do not present a shared view of what construct it indicates. The only recorded relation is that one paper claims a causal relationship from Reward hacking to Verbose generation, describing overly long content with meaningless repetitions in that account.

## Sources

**Verbose generation** (2 papers: [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e297fb6cd1690ee5b39c5bb4c58ad801-Paper-Datasets_and_Benchmarks_Track.pdf), [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf))
> An observable pattern where the model produces outputs that are longer or more wordy than necessary or desired.

**Overgeneration** (1 paper: [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf))
> Producing excessively long or verbose outputs, often continuing until the maximum generation length is reached, leading to incoherence.

**Overly verbose generation** (1 paper: [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf))
> Producing responses that are excessively long, often including redundant or irrelevant content, beyond what is necessary to answer the prompt.

**Verbose response generation** (1 paper: [Through the Valley: Path to Effective Long CoT Training for Small Language Models](https://aclanthology.org/2025.emnlp-main.251.pdf))
> The observable tendency of a model to produce outputs that are excessively long or wordy relative to the complexity of the task.

**Response length generation** (1 paper: [Analyzing and Modeling LLM Response Lengths with Extreme Value Theory: Anchoring Effects and Hybrid Distributions](https://aclanthology.org/2025.emnlp-main.1676.pdf))
> The observable production of text outputs with measurable word counts, varying in length based on model, prompt, and decoding settings.

**Unnecessarily lengthy output generation** (1 paper: [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf))
> Producing outputs that are longer than required, including irrelevant content after correct answers, which can reduce evaluation scores despite factual correctness.

## Relationships

### → Verbose generation
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > DPO suffers from reward hacking, causing the model’s expressive capability to decline and generating overly long content with meaningless repetitions. (Figure 1)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)
