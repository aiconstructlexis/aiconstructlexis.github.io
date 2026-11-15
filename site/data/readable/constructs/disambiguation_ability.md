# Disambiguation ability
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Ambiguity resolution, Word sense understanding, Disambiguation, Disambiguation capability, Sensitivity to sense boundaries, Ambiguity understanding  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a latent capacity to resolve ambiguity by using context to choose among multiple plausible interpretations. Most definitions cast it as a property of the model and vary mainly in what is being disambiguated, including ambiguous questions, word senses, entity names, translations, vague instructions, and superlative readings. A smaller framing defines it as sensitivity to same-sense versus different-sense boundaries that should mirror human judgments, and some papers extend the construct to explaining word senses in context.

**Space of facets.** Papers use several near-synonymous labels, including ambiguity resolution, word sense understanding, disambiguation capability, ambiguity understanding, and sensitivity to sense boundaries, for overlapping phenomena. One survey organizes disambiguation work into query rewriting, long-form answer generation, and asking clarifying questions. At the same time, the same broad label spans distinct ambiguity types, from conditional question answering with possible clarifications, to same-sense versus different-sense judgments, to entity-name disambiguation and absolute versus relative superlative readings.

**Space of measurement.** Papers link the construct to 6 measurement instruments and 3 behavioral indicators. The most frequently linked instruments are BIG-Bench Hard, CondAmbigQA, DMDTEval, LLM-as-a-judge, and Multi30k, plus 1 other instrument. Operationalizations are mostly benchmark or dataset based, with one LLM-as-a-judge setup: BIG-Bench Hard includes disambiguation among diverse tasks, CondAmbigQA evaluates whether models recognize, interpret, and resolve ambiguity and penalizes producing only a single answer pair, DMDTEval scores disambiguation accuracy over ambiguous vocabulary, and multimodal translation evaluations test whether images help disambiguate sentences and sometimes focus on the model's most likely translation. Other work operationalizes the construct as categorical same-sense versus different-sense discrimination that mirrors human judgments.

**Links.** No correlation claims are reported. Papers claim a causal relationship from domain knowledge to disambiguation ability, with one translation paper arguing that scarce cross-domain knowledge leads to translation ambiguities, and another claims a causal relationship from reasoning to disambiguation ability in correctly understanding ambiguous instructions. A survey also relates disambiguation ability to query rewriting and long-form question answering, and relates clarifying question generation to disambiguation ability as part of three major policies for disambiguation work.

## Sources

**Ambiguity resolution** (1 paper: [CondAmbigQA: A Benchmark and Dataset for Conditional Ambiguous Question Answering](https://aclanthology.org/2025.emnlp-main.115.pdf))
> The model's capacity to recognize multiple valid interpretations of a query and generate responses that appropriately distinguish or address them based on contextual constraints.

**Word sense understanding** (1 paper: [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf))
> The latent ability of a model to grasp the meaning of a word in context, beyond mere pattern matching, enabling accurate disambiguation and explanation across diverse usages.

**Disambiguation capability** (1 paper: [Detect, Disambiguate, and Translate: On-Demand Visual Reasoning for Multimodal Machine Translation with Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.74.pdf))
> The underlying trait enabling a model to resolve ambiguous terms by leveraging multimodal context, particularly visual evidence, to select the correct translation.

**Sensitivity to sense boundaries** (1 paper: [Evaluating Contextualized Representations of (Spanish) Ambiguous Words: A New Lexical Resource and Empirical Analysis](https://aclanthology.org/2025.naacl-long.422.pdf))
> The extent to which a model distinguishes categorical same-sense versus different-sense contexts in a way that mirrors human judgments.

**Disambiguation** (1 paper: [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.428.pdf))
> The latent ability of a model to accurately distinguish between entities that share the same surface name but have different specific descriptors.

**Disambiguation ability** (1 paper: [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> The latent capacity of an LLM to correctly interpret and translate words with multiple meanings based on domain-specific context in multi-domain translation.

**Ambiguity understanding** (1 paper: [Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf))
> The ability of a model to correctly interpret language instructions that are vague, incomplete, or contain colloquialisms by integrating visual context and common sense.

## Relationships

### Disambiguation ability →
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > “These benchmarks are quite diverse and include tasks such as logical deduction, arithmetic, translation error detection, disambiguation, as well as general knowledge”
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Multi30k** (measurement instrument): *measured_by*, 1 paper
  > This makes it an ideal dataset to demonstrate the effectiveness of our DeDiT reasoning’s on-demand disambiguation capabilities. (Section 3.1)
  - [Detect, Disambiguate, and Translate: On-Demand Visual Reasoning for Multimodal Machine Translation with Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.74.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > Winogrande: a large-scale dataset focused on common sense reasoning, designed to improve and evaluate AI models on ambiguity resolution tasks (Sakaguchi et al., 2019) (Section 5.1).
  - [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf)
- **DMDTEval** (measurement instrument): *measured_by*, 1 paper
  > To this end, we present an evaluation and analysis of LLMs on disambiguation in multi-domain translation (DMDTEval), our systematic evaluation framework... (Abstract)
  - [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > Therefore, we design a prompt to evaluate the disambiguation capability of LLMs using GPT-4o-mini7. (Section 2.4)
  - [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **CondAmbigQA** (measurement instrument): *measured_by*, 1 paper
  > CondAmbigQA emphasises ambiguity resolution, explicitly capturing possible clarifications for ambiguous questions. This allows for a structured evaluation of how effectively models recognise, interpret, and resolve ambiguity by interpreting distinct possible meanings. (Section 3.4)
  - [CondAmbigQA: A Benchmark and Dataset for Conditional Ambiguous Question Answering](https://aclanthology.org/2025.emnlp-main.115.pdf)

### → Disambiguation ability
- **Reasoning** (construct): *causes*, 1 paper
  > Reasoning and reflection are crucial for the model to correctly understand ambiguous instructions. (Table 5)
  - [Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf)
- **Domain knowledge** (construct): *causes*, 1 paper
  > This scarcity limits their translation capabilities and prevents them from effectively acquiring cross-domain knowledge, which leads to translation ambiguities. (Section 1)
  - [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf)

### Associated with
- **Query rewriting** (behavioral indicator), 1 paper
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Long-form question answering** (behavioral indicator), 1 paper
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Clarifying question generation** (behavioral indicator), 1 paper
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
