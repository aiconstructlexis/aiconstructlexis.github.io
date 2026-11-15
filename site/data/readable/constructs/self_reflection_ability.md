# Self-reflection ability
**Type:** Construct  
**Supporting papers:** 42  
**Also known as:** Reflection, Reflection capability, Self-reflection, Iterative reflection capability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats self-reflection ability as a latent capability of an agent or model to review prior attempts or generated solutions, analyze its own performance, often especially failures, and use that review to refine later behavior, strategy, or responses. A common variant makes the output explicit as useful verbal feedback from prior experience for subsequent task improvement, while a narrower framing treats it as self-correction or verification during reasoning, including identifying and fixing errors or confirming conclusions with new insights. A smaller line of work describes it less as a stable ability and more as an iterative or multi-round process of critical self-evaluation, sometimes emphasizing repeated revision without degradation from redundancy, drift, or stubbornness.

**Space of facets.** Papers use several closely related labels, including reflection, reflection capability, self-reflection, and iterative reflection capability, for overlapping ideas centered on reviewing prior outputs and improving subsequent ones. Within that family, some authors narrow the construct to multi-round self-reflection, some to generating verbal feedback from experience, some to reflection on generated solutions during reasoning, and some to iterative response refinement across multiple cycles. One paper also singles out "reflection quality" at the step level, asking whether each reflection step drives the question toward correctness.

**Space of measurement.** No measurement instrument is linked to this construct, and papers link it to one behavioral indicator, Self-correction. In practice, the construct is described through behaviors such as generating useful verbal feedback from prior experiences, explicitly reflecting on environmental feedback, critically evaluating previous responses, identifying and fixing errors or confirming conclusions, selecting the most plausible solution, and revising responses over multiple rounds. These observable descriptions largely mirror the main definitions, which also focus on reviewing prior outputs and improving later ones.

**Links.** Papers link this construct in two ways. One paper reports that Self-correction is related to self-reflection ability, using "reflection quality" to examine whether each reflection step drives the question toward correctness. One paper also claims a causal relationship from self-reflection ability to Reasoning quality, stating that models with a reflection mechanism demonstrate superior chain-of-thought quality.

## Sources

**Reflection** (1 paper: [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.892.pdf))
> The model's ability to review prior attempts and refine future behavior based on that review.

**Reflection capability** (2 papers: [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf), [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf))
> The degree of an agent's proficiency in generating useful verbal feedback from prior experiences to improve subsequent task performance.

**Self-reflection** (4 papers: [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf), [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf))
> The latent ability of an agent to analyze its own performance, particularly failures, and generate feedback to improve its strategy in subsequent attempts.

**Iterative reflection capability** (1 paper: [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf))
> The latent ability of a model to effectively refine its responses over multiple cycles of self-evaluation and revision, avoiding degradation due to redundancy, drift, or stubbornness.

## Relationships

### Self-reflection ability →
- **Reasoning quality** (construct): *causes*, 1 paper
  > “Models with reflection mechanism demonstrate a superior CoT quality”
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)

### Associated with
- **Self-correction** (behavioral indicator), 1 paper
  > “Reflection Quality ... analyzes whether each reflection step drives the question towards correctness.”
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
