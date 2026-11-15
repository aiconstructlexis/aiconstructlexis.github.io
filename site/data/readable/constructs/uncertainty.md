# Uncertainty
**Type:** Construct  
**Supporting papers:** 18  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats uncertainty as unreliability, ambiguity, or lack of confidence in a model's prediction or generation. Many papers phrase it at the output level, as unreliable or inconsistent generations, low-confidence predictions, or variability across different answers to the same prompt, with one stating that uncertainty is typically defined over the different answers an LLM gives for the same prompt. Smaller strands shift the referent from ordinary predictions to evaluator judgments, to a model's internal or output-derived uncertainty about whether an answer is correct, or to latent unpredictability and information content in representations inferred from matrix entropy.

**Space of facets.** Papers place uncertainty beside several neighboring notions rather than giving one shared breakdown. In active learning it appears alongside learnability, diversity, and representativeness, in prompt-engineering work it is discussed alongside sensitivity and consistency, and in authorship verification it is expressed through indecision markers such as scores near 0.5 and many "MAYBE" intermediate labels. Across these usages, the same term covers both observable answer variability and latent properties read from internal states or representations, and some papers frame higher uncertainty as lower confidence in an original prediction.

**Space of measurement.** Papers link uncertainty to one measurement instrument and two behavioral indicators. The only linked instrument is Open LLM Leaderboard, but it is discussed as a leaderboard that does not take uncertainty into account rather than as a direct measure, and the linked behavioral indicators are Hallucination and Pairwise comparison. Direct operationalization is more varied: papers use entropy of the output probability distribution, different answers over multiple stochastic generations, probabilities of output tokens for evaluator judgments, final scores near 0.5 with a high share of "MAYBE" labels, internal-state or token-level density signals, and truncated matrix entropy across layers and heads; some also use uncertainty about whether an answer is correct as the basis for abstention. Most of these operationalizations target low confidence or unreliable outputs, while the matrix-entropy line targets representation-level information content and the importance of model components during inference.

**Links.** Several papers report that Hallucination correlates with Uncertainty, and one also describes them as related, with evidence phrased as uncertain outputs being indicative of hallucinations and hallucinations being tied to model uncertainty. One paper claims a causal relationship from Pairwise comparison to Uncertainty, stating that pairwise comparison can reduce or mitigate uncertainty in evaluation. One paper reports that Conformity correlates with Uncertainty, and another relates Calibration to Uncertainty through discussion of poorly calibrated confidence scores. Uncertainty is also related to Open LLM Leaderboard, which one paper says does not take uncertainty into account.

## Sources

**Uncertainty** (10 papers: [Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf), [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf), [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf), [UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective](https://aclanthology.org/2025.emnlp-main.209.pdf), [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf), [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf), [Conformity in Large Language Models](https://aclanthology.org/2025.acl-long.195.pdf))
> The degree to which the model's predictions are unreliable or ambiguous for a given video sample.

## Relationships

### → Uncertainty
- **Hallucination** (behavioral indicator): *correlates*, 3 papers
  > we go beyond merely understanding knowledge refusal, and find SAE latents, seemingly representing uncertainty, that are predictive of incorrect answers.
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **Pairwise comparison** (behavioral indicator): *causes*, 1 paper
  > Compared to single-answer grading, pairwise comparison reduces the influence of subjective bias by directly comparing the relative merits of model outputs, thereby mitigating the uncertainty in evaluation to some extent. (Section 4.5)
  - [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf)
- **Conformity** (construct): *correlates*, 1 paper
  > Notably, we are the first to show that LLMs are more likely to conform when they are more uncertain in their own prediction. (Abstract)
  - [Conformity in Large Language Models](https://aclanthology.org/2025.acl-long.195.pdf)

### Associated with
- **Calibration** (construct), 1 paper
  > Recent work (Ren et al., 2023) shows that sequence-level confidence scores remain poorly calibrated with output quality, even after applying length normalization. (Section 2)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **Open LLM Leaderboard** (measurement instrument), 1 paper
  > Despite their usefulness, these leaderboards possess a significant limitation: They do not take into account the uncertainty of LLMs.
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
