# Multilingual reasoning
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Multilingual Knowledge and Reasoning, Cross-lingual reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats multilingual reasoning as a model ability to perform reasoning tasks in multiple, often non-English, languages. Several definitions keep this task-focused framing, describing effective reasoning when queries are presented in different languages, while a smaller line of work casts it more explicitly as a latent ability, stressing consistency across languages and, in some cases, across cultural contexts. The main variation is between multilingual task performance and a broader notion of reasoning that remains consistent across linguistic and cultural contexts.

**Space of facets.** Most papers use "multilingual reasoning" for the same general idea, but adjacent labels appear. Some authors use "multilingual knowledge and reasoning," while others use "cross-lingual reasoning" to foreground direct comparison and maintained performance across linguistic boundaries; one survey source also describes code as a language-agnostic bridge for multilingual reasoning. The distinctions that recur are therefore between multilingual task performance, knowledge-and-reasoning wording, and cross-lingual consistency.

**Space of measurement.** Operationalization is benchmark-centered: papers link multilingual reasoning to 6 measurement instruments and no behavioral indicators. The most frequently linked instruments are MGSM, BIG-Bench Hard, MMLU, MMLU-ProX, and MMMLU, plus 1 other instrument; papers use them to evaluate multilingual mathematical reasoning, broader reasoning tasks, translated evaluation tracks, and direct cross-lingual comparisons. These operationalizations mostly match the dominant definitions by testing reasoning performance across languages, with MMLU-ProX explicitly framed for cross-lingual comparison and BIG-Bench Hard treating "Multilingual Knowledge and Reasoning" as one reasoning category.

**Links.** Papers link it to 2 constructs. One paper claims a causal relationship from Reasoning to multilingual reasoning, stating that built-in reasoning and language understanding capabilities are used to boost multilingual reasoning effects. Another paper reports that multilingual reasoning is related to Cross-lingual alignment, with the relationship described through aligning input semantics across languages.

## Sources

**Multilingual Knowledge and Reasoning** (1 paper: [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf))
> The latent ability to process and reason across multiple languages and cultural contexts.

**Multilingual reasoning** (4 papers: [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.577.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf))
> The ability of a model to perform reasoning tasks effectively when presented with queries in multiple, non-English languages.

**Cross-lingual reasoning** (1 paper: [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.79.pdf))
> The latent ability of a model to apply reasoning processes consistently across different languages, maintaining performance regardless of linguistic or cultural context.

## Relationships

### Multilingual reasoning →
- **MGSM** (measurement instrument): *measured_by*, 2 papers
  > We experimented MindMerger with the latest multilingual mathematical reasoning MGSM [Shi et al., 2023] (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.577.pdf)
- **X-CSQA** (measurement instrument): *measured_by*, 1 paper
  > In order to evaluate the diverse multilingual reasoning capabilities of the models, a challenging multilingual dataset X-CSQA [Lin et al., 2021] in commonsense reasoning task...were used. (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
- **MMLU-ProX** (measurement instrument): *measured_by*, 1 paper
  > It enables comprehensive evaluation of LLMs’ cross-lingual reasoning abilities and lays a foundation for the development of more inclusive LLMs in the future. (Introduction)
  - [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.79.pdf)
- **MMMLU** (measurement instrument): *measured_by*, 1 paper
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)

### → Multilingual reasoning
- **Reasoning** (construct): *causes*, 1 paper
  > utilize the built-in reasoning and language understanding capabilities of LLMs... to boost the multilingual reasoning effects.
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)

### Associated with
- **Cross-lingual alignment** (construct), 1 paper
  > Our analysis on cross-attention behaviour in Mufu-finetuned models provides evidence that the method extends LLM's capability in multilingual reasoning. That is, given any Mufu-style prompt, the finetuned models are capable of ... aligning the input semantics across languages...
  - [Mufu: Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf)
