# Logical consistency
**Type:** Construct  
**Supporting papers:** 42  
**Also known as:** Logical robustness, Logical coherence, Solution consistency, Logicality, Reasoning coherence, Logical plausibility  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats logical consistency as internal non-contradiction: outputs, summaries, dialogues, or reasoning chains are described as logically structured, coherent, and free of discrepancies. A smaller line of work defines it more narrowly as whether responses to logically related inputs obey logic, for example when a statement and its negation receive semantically opposite answers, when conclusions follow from premises, or when decisions remain invariant across equivalent formulations. Other task-specific definitions shift the reference point from text alone to predictions on decomposed NLI sub-problems, beliefs over related claims, adherence of generated programs to domain knowledge, or similarity between agent and human operational logic.

**Space of facets.** Most papers use nearby labels for closely similar ideas, especially logical coherence and logical robustness, and a few rename the same theme as solution consistency or reasoning coherence. One evaluation framework places logical robustness inside a broader logical thinking category alongside logical correctness and logical efficiency, while a narrower variant, logical plausibility, targets whether a sub-query is consistent with the prior reasoning context. The same label is also used at different units of analysis, from plot and theme consistency in summaries to chain-of-thought steps, sub-problem predictions, belief trees, generated programs, and application-switching behavior.

**Space of measurement.** Papers link the construct to 4 measurement instruments and 4 behavioral indicators. The linked instruments cover model-based evaluation, direct judging, and dataset-based checks: FLASK is used through its logical thinking category, including logical correctness, logical robustness, and logical efficiency; human evaluation asks annotators to choose the most logical rationale; LLM-as-a-judge uses DeepSeek R1 and ERNIE Bot 4.0 to score outputs for logical consistency, clarity, and lack of ambiguity; and SNLI operationalizes it as consistency between original instances and their sub-problems. These operationalizations mostly match the dominant non-contradiction framing, though the SNLI setup narrows it to agreement under logically necessary constraints rather than general output quality.

**Links.** Several papers connect logical consistency to neighboring reasoning constructs and application settings. It is related to logical reasoning, and papers also relate it to fact-checking and to improving consistency with domain knowledge in generated programs. Papers claim a causal relationship from logical consistency to hallucination and to factuality, though some phrasing is looser: one paper says a logically consistent LLM is less likely to hallucinate, another says hallucination stems from optimizing for likelihood rather than truth or logical consistency, and another says factuality can be improved using consistency across beliefs while a separate paper calls factuality and consistency intimately related. In the reverse direction, one survey claims a causal relationship from self-reflection to logical consistency, and no correlational link is reported.

## Sources

**Logical robustness** (1 paper: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf))
> The degree to which a response remains logically consistent and generally applicable throughout its reasoning process without contradictions.

**Logical consistency** (8 papers: [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf), [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf), [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf), [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf), [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf), [Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](https://aclanthology.org/2025.acl-long.169.pdf), [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf))
> The absence of internal contradictions or discrepancies within the plot, character development, or themes of a generated summary.

**Logical coherence** (6 papers: [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [The Lawyer That Never Thinks: Consistency and Fairness as Keys to Reliable AI](https://aclanthology.org/2025.acl-long.491.pdf), [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf), [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.250.pdf), [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf), [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLM Communication](https://aclanthology.org/2025.naacl-long.203.pdf))
> The quality of a model's generated output being logically structured, consistent, and free from contradictions.

**Solution consistency** (1 paper: [Step-by-Step Reasoning for Math Problems via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf))
> The degree to which the model maintains logical coherence and correctness throughout the entire reasoning process.

**Logicality** (1 paper: [LongReward: Improving Long-context Large Language Models with AI Feedback](https://aclanthology.org/2025.acl-long.187.pdf))
> The extent to which a model's response is internally consistent and free from logical errors or contradictions.

**Reasoning coherence** (1 paper: [SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models](https://aclanthology.org/2025.emnlp-main.27.pdf))
> The degree to which a model's reasoning process maintains logical consistency and structural integrity across long-form outputs, especially when generating spoken responses.

**Logical plausibility** (1 paper: [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf))
> The degree to which intermediate sub-queries or reasoning steps are logically consistent with the prior reasoning context.

## Relationships

### Logical consistency →
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > A logically consistent LLM is less likely to hallucinate since its response is unlikely to change due to the logical manipulation of the prompt.
  - [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf)
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Factuality** (construct): *causes*, 2 papers
  > A growing body of research explores improving LLMs’ factuality using the logical consistency across their beliefs (Dalvi et al., 2021; Tafjord et al., 2022; Mitchell et al., 2022; Jung et al., 2022; Hase et al., 2023; Kassner et al., 2023; Akyürek et al., 2024).
  - [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > "For human evaluation, 100 questions were sampled from each dataset, with annotators selecting the most logical rationale among those generated by ToT, GoT, and our method"
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > We use DeepSeek R1 and ERNIE Bot 4.0 to quantitatively evaluate model outputs before and after training, focusing on logical consistency, clarity, and lack of ambiguity (Section 5)
  - [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **SNLI** (measurement instrument): *measured_by*, 1 paper
  > we evaluate their logical consistency between each original SNLI instance and its corresponding sub-problems.
  - [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf)
- **FLASK** (measurement instrument): *measured_by*, 1 paper
  > we employ FLASK (Ye et al., 2024), a fine-grained evaluation protocol for model-based evaluation, which exhibits a high correlation with human-based evaluation. Specifically, we focus on the ‘logical thinking’ category in FLASK, which encompasses three aspects: logical correctness, logical robustness, and logical efficiency.
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)

### → Logical consistency
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > Multi-round self-reflection that encourages a single LLM to critically evaluate its previous responses has demonstrated the effectiveness of deliberation in improving logical coherence and qualities (Section 4.2.1)
  - [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf)

### Associated with
- **Logical reasoning** (construct), 2 papers
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: Logical Thinking (Logical Correctness, Logical Robustness, Logical Efficiency)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
  - [LogicTree: Structured Proof Exploration for Coherent and Rigorous Logical Reasoning with Large Language Models](https://aclanthology.org/2025.emnlp-main.1054.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > "We assess and improve the logical consistency of LLMs in propositional logic queries and logic rules, particularly in the context of fact-checking."
  - [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > By iterative preference alignment, the code generator learns to improve the logic consistency with the domain knowledge. (Abstract)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf)
