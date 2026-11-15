# General reasoning
**Type:** Construct  
**Supporting papers:** 9  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats general reasoning as a latent or unobservable model ability to logically process information, solve problems, and understand relationships across diverse or non-specialized domains. A narrower framing appears in one paper, where it is defined as solving individual reasoning tasks or examples without necessarily capturing the common patterns or generic facts shared across multiple examples. The main axis of disagreement is scope: a broad cross-domain capability versus an example-level ability defined in contrast to extracting shared structure across examples.

**Space of facets.** Papers do not present a rich internal breakdown of general reasoning. Instead, they mainly locate it by contrast: one paper separates it from abstract reasoning, stating that general reasoning focuses on each single example whereas abstract reasoning considers examples supported by a generic fact as a whole, and the same work reports a substantial discrepancy between the two performances. Other papers contrast it with specialized tasks requiring proprietary or domain-specific knowledge, and with math reasoning as a distinct task category.

**Space of measurement.** Papers operationalize general reasoning with 8 linked measurement instruments, and the linked instruments are all benchmarks; there is also 1 linked behavioral indicator, but it appears in a separate causal claim rather than as a benchmark measure. The most frequently linked instruments are BIG-Bench Hard, CommonsenseQA, and MMLU, with other linked benchmarks including DROP and HellaSwag. In practice, papers use benchmark performance on tasks explicitly described as general reasoning, such as 5-shot MMLU, 3-shot Chain-of-Thought BIG-Bench Hard, commonsense benchmarks said to emphasize general reasoning capabilities, and DROP as "a general reasoning task." These operationalizations mostly match the broad task-solving framing, while one definition draws a sharper boundary against abstract reasoning by centering single-example solution rather than generic facts across examples.

**Links.** Beyond measurement, one paper claims a causal relationship from Logic puzzle solving to General reasoning, saying that distilling long chains of thought from Knights and Knaves logic puzzles helps a model "acquire general reasoning skills" (Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings). Separately, Abstract reasoning is related to General reasoning: one paper reports "a substantial discrepancy between their general reasoning and abstract reasoning performances" (Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance). No correlational links are reported.

## Sources

**General reasoning** (3 papers: [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Synergistic Weak-Strong Collaboration by Aligning Preferences](https://aclanthology.org/2025.acl-long.995.pdf), [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf))
> The latent ability to solve individual reasoning tasks or examples without necessarily capturing the common patterns or generic facts underlying multiple examples.

## Relationships

### General reasoning →
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > Finally, to evaluate general reasoning, we test the model on two benchmarks: an easy task, 5-shot MMLU (Hendrycks et al., 2020)... (Section 2.3)
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
  - [AnyMAC: Cascading Flexible Multi-Agent Collaboration via Next-Agent Prediction](https://aclanthology.org/2025.emnlp-main.584.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 2 papers
  > Finally, to evaluate general reasoning, we test the model on two benchmarks: ...and a more challenging task, 3-shot Chain-of-Thought (CoT) Big Bench Hard (BBH) (Suzgun et al., 2022). (Section 2.3)
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
  - [Compute-Constrained Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 2 papers
  > To evaluate the generalization ability of our method and mitigate the risk of catastrophic forgetting, we conduct experiments on commonsense and reasoning datasets, including CSQA (Talmor et al., 2018), Hellaswag (Zellers et al., 2019), and MMLU-pro (Wang et al., 2024). (Section 5.6)
  - [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf)
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the generalization ability of our method and mitigate the risk of catastrophic forgetting, we conduct experiments on commonsense and reasoning datasets, including CSQA (Talmor et al., 2018), Hellaswag (Zellers et al., 2019), and MMLU-pro (Wang et al., 2024). (Section 5.6)
  - [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the generalization ability of our method and mitigate the risk of catastrophic forgetting, we conduct experiments on commonsense and reasoning datasets, including CSQA (Talmor et al., 2018), Hellaswag (Zellers et al., 2019), and MMLU-pro (Wang et al., 2024). (Section 5.6)
  - [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf)
- **DROP** (measurement instrument): *measured_by*, 1 paper
  > We compare training the language world model with policy (FTA-P) with the baseline (Llama-3.1-8B SFT on the same dataset) in several benchmarks, including math500 (Hendrycks et al., 2021), gsm8k (Cobbe et al., 2021), AIME and Drop (Dua et al., 2019), where the first three are mathematical reasoning tasks, and the fourth is a general reasoning task. (Section 4.3.1)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > It evaluates VLMs on both breadth and depth of subject knowledge, as well as on their expert-level reasoning and understanding. (Section 5.1)
  - [Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.97.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 1 paper
  > To demonstrate our method’s generalizability beyond mathematical reasoning, we conduct additional evaluations on the CommonsenseQA and StrategyQA benchmarks, which emphasize general reasoning capabilities.
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)

### → General reasoning
- **Logic puzzle solving** (behavioral indicator): *causes*, 1 paper
  > In the first stage, we "warm up" the model by distilling Long CoTs from a toy domain, namely, Knights & Knaves (K&K) logic puzzles to acquire general reasoning skills. (Abstract)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)

### Associated with
- **Abstract reasoning** (construct), 1 paper
  > Our findings reveal a substantial discrepancy between their general reasoning and abstract reasoning performances. (Abstract)
  - [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf)
