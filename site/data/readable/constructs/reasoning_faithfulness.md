# Reasoning faithfulness
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Reasoning fidelity, Chain-of-thought faithfulness, Reasoning hallucinations  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats reasoning faithfulness as correspondence between an expressed reasoning path and what actually produces the answer: papers describe faithful reasoning as a generated path or trace that reflects the actual or internal decision process, rather than a hallucinated or misleading justification. A smaller line of work shifts the reference point from internal process to consistency or grounding, defining it as the final conclusion aligning with the generated chain, the reasoning remaining grounded in provided evidence rather than misleading annotations or shortcuts, or, in safety settings, explanations that are coherent, logically sound, and faithful to the input prompt. Nearby labels include chain-of-thought faithfulness for explicit reasoning traces and reasoning hallucinations for cases where apparently plausible steps do not match program logic.

**Space of facets.** Papers do not present a shared multi-part taxonomy, but they do separate the area into nearby labels and failure modes. Chain-of-thought faithfulness is used for explicit reasoning traces, reasoning fidelity for explanations attached to safety decisions, and reasoning hallucinations for inconsistencies between reported reasoning and generated programs; that last usage is further described as logical errors in code statements, missing or irrelevant steps, and correct steps that are misordered or improperly connected. Another recurring contrast is between faithful reasoning and cheating, or between conclusions that adhere to a prior reasoning chain and conclusions that do not.

**Space of measurement.** Only 1 linked measurement instrument appears, CTC. The recorded evaluation using it also mentions BARTScore, BLURT, and human-evaluated faithfulness scores, and a nearby safety-oriented operationalization uses GPT-4.1-mini as an LLM judge to assess whether an explanation faithfully reflects the input and correctly drives the safety prediction, with an Explanation Fidelity score defined as the fraction of reasoning sentences labeled coherent. The construct is also linked to 1 behavioral indicator, Hallucination, though the recorded relationship treats that as a cause rather than a measurement; overall, the operationalizations mostly score whether stated reasoning matches the answer basis or prompt content, with some emphasis on coherence.

**Links.** Beyond measurement, one paper reports that Reasoning is related to reasoning faithfulness, describing questions about whether models leverage reasoning tokens to generate answers as closely tied to this construct. One paper also claims a causal relationship from Hallucination to reasoning faithfulness, stating that models struggle with faithful reasoning due to hallucination. No correlational link is recorded.

## Sources

**Reasoning faithfulness** (4 papers: [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf), [From Reasoning to Answer: Empirical, Attention-Based and Mechanistic Insights into Distilled DeepSeek R1 Models](https://aclanthology.org/2025.emnlp-main.198.pdf), [SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation](https://proceedings.neurips.cc/paper_files/paper/2024/file/217bb44ab14621754db8a392163e6b07-Paper-Datasets_and_Benchmarks_Track.pdf))
> The degree to which a model's generated reasoning path accurately reflects the actual process leading to its answer, avoiding hallucinated or misleading justifications.

**Reasoning fidelity** (1 paper: [MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety](https://aclanthology.org/2025.emnlp-main.1392.pdf))
> The degree to which a model's generated explanation for a safety decision is coherent, logically sound, and faithfully reflects the content of the input prompt.

**Chain-of-thought faithfulness** (1 paper: [On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/deed907f507e526a8dd20896d2bd7c49-Paper-Conference.pdf))
> The degree to which a model's explicit reasoning trace accurately reflects the true basis of its outputs.

**Reasoning hallucinations** (1 paper: [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf))
> The latent tendency of LLMs to generate reasoning steps in natural language that are inconsistent with the logic of generated programs, manifesting as logical errors, missing steps, or misordered connections despite seemingly correct justifications.

## Relationships

### Reasoning faithfulness →
- **CTC** (measurement instrument): *measured_by*, 1 paper
  > "The evaluation assessed BARTScore, CTC, BLURT, and human-evaluated faithfulness scores."
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)

### → Reasoning faithfulness
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > LLMs still struggle with conducting faithful reasoning due to issues of lack of knowledge and hallucination (Section 1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > This question [Do LRMs actually leverage the reasoning tokens to generate answers?] is closely tied to active research areas including reasoning effectiveness (Ma et al., 2025), reasoning faithfulness (Chen et al., 2025), and model behavior monitoring (Baker et al., 2025). (Section 1)
  - [From Reasoning to Answer: Empirical, Attention-Based and Mechanistic Insights into Distilled DeepSeek R1 Models](https://aclanthology.org/2025.emnlp-main.198.pdf)
