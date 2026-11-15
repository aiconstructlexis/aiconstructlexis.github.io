# Epistemic uncertainty
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Epistemic Uncertainty, Weight uncertainty  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats epistemic uncertainty as the model's lack of knowledge about its own prediction, a reducible uncertainty that can decrease with more information or data. Several definitions stress that it reflects ambiguity or missing knowledge rather than token-level likelihood alone, and one definition describes it as model-specific uncertainty tied to lack of knowledge in the model's parameters. A smaller line narrows the term to uncertainty in model parameters or weights, modeled through a posterior distribution and expected to diminish with more data.

**Space of facets.** Papers systematize the concept mainly through contrasts and nearby labels. One recurring contrast separates it from lexical confidence, since next-token likelihood is described as lexical confidence rather than epistemic uncertainty, while another places it alongside knowledge-boundary language as model-specific uncertainty related to the parametric knowledge boundary. Some authors also use weight uncertainty for the parameter-focused version, so the term spans both a broad lack-of-knowledge framing and a narrower posterior-over-weights framing.

**Space of measurement.** No measurement instrument is linked to it. Instead, papers link it to 2 behavioral indicators, Hallucination and Out-of-distribution detection, and to 2 constructs, Generation diversity and Robustness. In practice, papers operationalize it indirectly: one paper treats differences among kpred and kconf as a form of epistemic uncertainty, while others use parameter or weight uncertainty as the operative quantity.

**Links.** Only a few links are reported. One paper claims a causal relationship from epistemic uncertainty to Hallucination, reporting that accounting for weight uncertainty can improve decoding and reduce hallucinations, and the same paper claims a causal relationship from epistemic uncertainty to Robustness, describing uncertainty-aware MBR as leading to more robust language generation. Papers also relate it to Generation diversity, with one report noting that performance is highly correlated with prediction diversity across combined models, and to Out-of-distribution detection, where it is described as an improved indicator.

## Sources

**Epistemic uncertainty** (3 papers: [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf), [Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf), [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf))
> The model's uncertainty about its own prediction that reflects ambiguity or lack of knowledge rather than token-level likelihood alone.

**Epistemic Uncertainty** (1 paper: [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf))
> Uncertainty in the model parameters that diminishes with more data, serving as an indicator of model uncertainty in predictions.

**Weight uncertainty** (1 paper: [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf))
> The uncertainty associated with the model's parameter estimates, modeled as a posterior distribution over the weights.

## Relationships

### Epistemic uncertainty →
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > Overall, we find strong evidence that accounting for weight uncertainty can improve decoding and reduce hallucinations when finetuning and pretraining from scratch, even without computational overhead. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > Overall, we find that the uncertainty-aware variant of MBR proposed in this paper leads to better and more robust language generation. (Section 5)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)

### Associated with
- **Generation diversity** (construct), 1 paper
  > The performance of uncertainty-aware MBR is highly correlated with the prediction diversity across the combined models. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Out-of-distribution detection** (behavioral indicator), 1 paper
  > “epistemic uncertainty providing an improved indicator for out-of-distribution detection.”
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
