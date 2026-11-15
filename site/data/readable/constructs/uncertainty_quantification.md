# Uncertainty quantification
**Type:** Construct  
**Supporting papers:** 30  
**Also known as:** Reward uncertainty, Evaluation uncertainty, Response uncertainty, Reasoning uncertainty, Underspecification uncertainty, Uncertainty estimation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats uncertainty quantification, often under the label uncertainty estimation, as a model's ability to represent or infer how uncertain it is about its own predictions, often in calibration terms where "expressed confidence aligns with the actual probability of being correct." Many definitions keep this broad, referring to the reliability of predictions, responses, or internal states. A smaller line of work narrows the concept to specific loci, including evaluator judgments, reward-model predictions of human preference, the reasoning process, and underspecified user requests. The main variation is therefore between a general self-uncertainty capacity and scoped forms tied to prediction, evaluation, reasoning, or interaction context.

**Space of facets.** Papers organize this family of terms into several subtypes: uncertainty in attention and prediction distributions, evaluation uncertainty, response uncertainty, reasoning uncertainty, reward uncertainty, and underspecification uncertainty. The broad label uncertainty estimation is also tied to self-evaluation, and confidence elicitation is used for estimating confidence in responses. Some subtype names cover different objects: response uncertainty is defined either as ambiguity in a response probability distribution or as variability across sampled outputs, and evaluation uncertainty is defined either as instability in evaluator judgments or as uncertainty about unobserved evaluation scores.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. In use, papers instead operationalize the construct with model-side quantities such as confidence compared with correctness, entropy of the predictive posterior, token probabilities, perplexity, logits and attention scores, Jensen-Shannon divergence over categorical attention, ensemble-based uncertainty, and variability across sampled outputs. These estimates are then used for routing or rejection, adaptive attention or gating, data selection and confidence sets, dynamic fusion, and conditional-threshold decisions.

**Links.** The only recorded construct link is to Truthfulness. One paper claims a causal relationship from uncertainty quantification to Truthfulness, describing it as "a prominent approach for eliciting truthful answers from large language models."

## Sources

**Uncertainty quantification** (3 papers: [LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf), [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf), [MoSEs: Uncertainty-Aware AI-Generated Text Detection via Mixture of Stylistics Experts with Conditional Thresholds](https://aclanthology.org/2025.emnlp-main.294.pdf))
> The model's ability to accurately represent its own uncertainty, where expressed confidence aligns with the actual probability of being correct.

**Uncertainty estimation** (7 papers: [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf), [Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pham25b/pham25b.pdf), [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf), [Semantic Exploration with Adaptive Gating for Efficient Problem Solving with Language Models](https://aclanthology.org/2025.acl-long.29.pdf), [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf), [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf), [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf))
> The ability to quantify ambiguity in attention or prediction distributions and use that estimate to adapt model processing.

**Reward uncertainty** (1 paper: [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf))
> The degree of confidence or ambiguity in a reward model's prediction of human preference, often estimated using ensembles.

**Evaluation uncertainty** (2 papers: [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf), [Active Evaluation Acquisition for Efficient LLM Benchmarking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bp/li25bp.pdf))
> The degree of instability or indecision in an LLM evaluator's judgments across inputs, settings, or domains.

**Response uncertainty** (2 papers: [Efficiently Learning at Test-Time: Active Fine-Tuning of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba942323c447c9bbb9d4b638eadefab9-Paper-Conference.pdf), [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf))
> The degree of ambiguity or lack of confidence in the model's predicted probability distribution for a response to a given prompt.

**Reasoning uncertainty** (1 paper: [Token Signature: Predicting Chain-of-Thought Gains with Token Decoding Feature in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ci/liu25ci.pdf))
> The degree of uncertainty in the model's reasoning process, especially when token probability trends suggest weaker alignment with successful reasoning.

**Underspecification uncertainty** (1 paper: [Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf))
> The latent uncertainty arising when a user's input does not fully specify the task or provide sufficient context, leading to ambiguity in the model's response generation.

## Relationships

### Uncertainty quantification →
- **Truthfulness** (construct): *causes*, 1 paper
  > Uncertainty quantification (UQ) is a prominent approach for eliciting truthful answers from large language models (LLMs).
  - [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf)
