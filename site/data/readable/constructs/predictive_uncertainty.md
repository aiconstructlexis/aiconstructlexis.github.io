# Predictive uncertainty
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Prediction uncertainty, Model uncertainty  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats predictive uncertainty as the model's confidence, or lack of confidence, in its predictions, usually at the next-token or output level and often tied to the entropy of the output probability distribution, with higher entropy marking greater uncertainty. Several papers phrase the same idea as ambiguity in next-token predictions that is resolved as generation proceeds, and one explicitly contrasts uncertainty over outputs with uncertainty over the parameters themselves. A smaller line of work uses closely related labels such as prediction uncertainty or model uncertainty for the latent confidence behind next-token predictions, and one paper applies the same framing to preference predictions near the decision boundary.

**Space of facets.** The main distinctions that appear are between sources and targets of uncertainty. One paper says predictive uncertainty can be decomposed into different sources of uncertainty, and another contrasts predictive uncertainty over outputs with weight uncertainty over parameters. Across papers, prediction uncertainty, predictive uncertainty, and model uncertainty are used for closely related notions, although one usage narrows the target from token or output predictions to preference predictions.

**Space of measurement.** Operationalization is mostly direct rather than via named instruments: no measurement instrument is linked to it, and the only linked behavioral indicator is hallucination. The recurring operationalization is entropy of the output or predictive distribution, sometimes with a confidence threshold that determines whether guidance is applied; other papers analyze how quickly and stably a model moves from initial ambiguity to confident predictions, use consistency rate across repeated runs to quantify uncertainty, or target samples whose predicted preference is closest to 0.5 by maximizing predictive entropy. These measurements largely mirror the dominant definitions by treating uncertainty as confidence or ambiguity in predictions, although one paper applies that logic to preference predictions rather than next-token generation.

**Links.** In the linked claims, one paper claims a causal relationship from predictive uncertainty to hallucination, stating that when a model is uncertain about the semantic meaning of the next tokens, it is likely to start hallucinating. Another paper reports that hallucination is positively correlated with model uncertainty. One paper also relates consistency to predictive uncertainty by using the most frequent response across multiple runs, summarized as a consistency rate, to quantify prediction uncertainty.

## Sources

**Prediction uncertainty** (2 papers: [Why and How LLMs Benefit from Knowledge Introspection in Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.352.pdf), [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf))
> The degree of confidence in a model's predictions, often measured by the entropy of its output probability distribution, where higher entropy indicates greater uncertainty.

**Predictive uncertainty** (2 papers: [Context-Aware Membership Inference Attacks against Pre-trained Large Language Models](https://aclanthology.org/2025.emnlp-main.370.pdf), [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf))
> The degree of ambiguity in the model's next-token predictions, which decreases more rapidly for memorized sequences as the model resolves uncertainty through recall.

**Model uncertainty** (2 papers: [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf), [Active Reward Modeling: Adaptive Preference Labeling for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25c/shen25c.pdf))
> The latent level of confidence a model has in its next-token predictions, inferred from the entropy of its output probability distribution, which influences where interventions are applied.

## Relationships

### Predictive uncertainty →
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > When an LLM is uncertain about the semantic meaning of the next tokens to generate, it is likely to start hallucinating. Thus, it has been suggested that predictive uncertainty is one of the main causes of hallucinations. (Abstract)
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
  - [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://aclanthology.org/2025.emnlp-main.976.pdf)

### Associated with
- **Consistency** (construct), 1 paper
  > “To evaluate the uncertainty of a model’s responses, a common approach is to calculate the most frequent response from multiple outputs generated by the model across multiple runs. This method quantifies the model’s prediction uncertainty using a metric known as the consistency rate (CR)”
  - [Exploring Response Uncertainty in MLLMs: An Empirical Evaluation under Misleading Scenarios](https://aclanthology.org/2025.emnlp-main.916.pdf)
