# Overconfidence
**Type:** Construct  
**Supporting papers:** 34  
**Also known as:** Over-confidence, Overconfident generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats overconfidence as a latent or dispositional tendency for a model's stated, predicted, or posterior confidence to exceed its actual accuracy or correctness. This framing appears in descriptions of confidence scores being higher than accuracy, accuracy within confidence bins being lower than the corresponding confidence, and assertive but incorrect responses on unfamiliar topics, ambiguous inputs, or out-of-distribution cases. Smaller variants narrow the phenomenon to particular settings, such as exposure bias during auto-regressive decoding, fine-tuning on small datasets, or self-consistent but incorrect generations. A minority usage applies the same name to strategic reasoning, describing a player that overlooks potential risks in pursuit of greater rewards.

**Space of facets.** Papers use the near-synonymous labels over-confidence, overconfidence, and overconfident generation, but they do not always point to exactly the same object. Most uses stay within miscalibration, sometimes explicitly contrasting over-confident with under-confident predictions through calibration language, while others specialize it to verbalized confidence, overly peaked output distributions, assertive answers beyond the model's knowledge, or self-consistent hallucinations. One paper instead uses the term for risk-taking in game-theoretic play, so the clearest axis of variation is whether overconfidence is treated as a mismatch between confidence and accuracy or as a behavioral tendency in strategic choice.

**Space of measurement.** No measurement instrument is linked to overconfidence. Papers instead operationalize it directly in outputs and confidence estimates, most often by comparing confidence with accuracy or correctness, for example through confidence bins and calibration plots, through verbalized confidence elicitation, through posterior or token probabilities during auto-regressive decoding, or through entropy-based views of overly peaked output distributions. These operationalizations mostly match the dominant definition, and overconfidence is linked to 3 behavioral indicators, most often hallucination, with confidence correction and confidence estimation appearing as related indicators.

**Links.** Calibration is the most recurrent linked construct: several papers claim a causal relationship from overconfidence to calibration, while others treat overconfidence as related to calibration or report that it correlates with calibration. A smaller recurring line claims a causal relationship from overconfidence to hallucination. Single-paper causal claims also run from overconfidence to context faithfulness, from factuality to overconfidence, and from world knowledge to overconfidence. Three additional single-paper links treat overconfidence as related to further confidence or knowledge-boundary notions.

## Sources

**Over-confidence** (1 paper: [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf))
> A latent property where the model's confidence in its predictions exceeds its actual accuracy, particularly exacerbated during auto-regressive decoding due to exposure bias.

**Overconfidence** (9 papers: [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf), [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf), [GTBench: Uncovering the Strategic Reasoning Capabilities of LLMs via Game-Theoretic Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/3191170938b6102e5c203b036b7c16dd-Paper-Conference.pdf), [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf), [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf), [Calibrated Language Models and How to Find Them with Label Smoothing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25w/huang25w.pdf), [When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity](https://aclanthology.org/2025.emnlp-main.426.pdf))
> A dispositional trait where a model's predicted confidence is systematically higher than its actual accuracy, particularly after fine-tuning.

**Overconfident generation** (1 paper: [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf))
> A latent tendency of a model to produce highly confident but incorrect outputs, particularly in cases where multiple consistent hallucinations are generated, evading standard consistency checks.

## Relationships

### Overconfidence →
- **Calibration** (construct): *causes*, 5 papers
  > Fine-tuned large language models (LLMs) often exhibit overconfidence, particularly when trained on small datasets, resulting in poor calibration and inaccurate uncertainty estimates.
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [Calibrated Language Models and How to Find Them with Label Smoothing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25w/huang25w.pdf)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > tuning LLMs on data containing unseen knowledge can encourage models to be overconfident, leading to hallucinations (Section 2).
  - [Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://aclanthology.org/2025.acl-long.804.pdf)
  - [Identifying and Answering Questions with False Assumptions: An Interpretable Approach](https://aclanthology.org/2025.emnlp-main.1228.pdf)
- **Context faithfulness** (construct): *causes*, 1 paper
  > overconfidence, resulting in a substantial setback for the context-faithfulness of LLMs. (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)

### → Overconfidence
- **Factuality** (construct): *causes*, 1 paper
  > factuality enhancement can lead LLMs to become overly confident in their parametric knowledge (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **World knowledge** (construct): *causes*, 1 paper
  > Specifically, data aligned with LLMs’ prior knowledge would induce overconfidence, while new knowledge improves calibration. (Abstract)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)

### Associated with
- **Confidence estimation** (behavioral indicator), 1 paper
  > The performance of Med-LVLMs in uncertainty estimation is unsatisfactory, revealing a poor understanding of their medical knowledge limits. Additionally, these models tend to exhibit overconfidence, thereby increasing the risk of misdiagnoses. (Sec 1)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Confidence correction** (behavioral indicator), 1 paper
  > This suggests that even after the model has become sufficiently accurate, it undergoes a phase of overconfidence before recalibrating its predictions. We refer to this as a “confidence correction phase” in the final layers.
  - [Calibration Across Layers: Understanding Calibration Evolution in LLMs](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **Knowledge boundary awareness** (construct), 1 paper
  > Overconfidence is a fraction of incorrect answers where the method was confident about self-knowledge reflecting how often the method incorrectly assumes that the model possesses the required knowledge when it does not.
  - [Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home](https://aclanthology.org/2025.acl-long.319.pdf)
