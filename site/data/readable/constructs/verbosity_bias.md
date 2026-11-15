# Verbosity bias
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Length Bias, Length bias  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage describes verbosity bias, often also called length bias, as a quality-insensitive preference for longer or more verbose responses. Most definitions place that preference in reward models, judges, or LLM-based evaluators, using formulations such as favoring outputs based on sequence length rather than true quality or preferring longer responses over more succinct ones of equal content. A smaller line extends the same idea to the model or reward signal itself, and one paper describes the observed phenomenon more narrowly as systematically different rewards for longer versus shorter responses, adding that it may be mainly an artifact of bias in naive evaluations.

**Space of facets.** The papers mostly do not subdivide it further. Instead, they usually place it within broader families of bias: reward-model work presents sequence length as one prevalent bias among others, evaluator-focused work groups verbosity bias with self-enhancement bias, and one LLM-as-a-Judge discussion also lists position bias and limited capability in grading math and reasoning questions. The main terminological variation is between length bias in reward-model and DPO settings and verbosity bias in evaluator settings, even though both labels describe preference for longer responses independent of quality; some papers also frame it as a dataset bias, while others call it an inherent bias of LLMs or reward models.

**Space of measurement.** Explicit measurement links are limited: papers link verbosity bias to 1 measurement instrument, the benchmark AlpacaEval 2.0, and to 1 behavioral indicator, reward hacking, but not through a direct measured_by claim. In practice, papers operationalize it by checking whether more verbose responses are ranked first, by comparing raw and LC win rates in settings designed to mitigate model verbosity, or by examining whether reward models assign different rewards to longer versus shorter responses. This operationalization matches the dominant definitions, which also focus on preference for length or verbosity irrespective of quality.

**Links.** One paper reports a related link from human preference alignment to verbosity bias in DPO, describing a length bias problem caused by unbalanced length preference from the non-uniform length distribution of chosen and rejected responses. One paper claims a causal relationship from verbosity bias to reward hacking, stating that when biased reward models are used in RLHF, the model can learn to exploit those biases rather than improve genuine task performance. Another paper reports a related link from AlpacaEval 2.0 to verbosity bias, arguing that higher LC win rates for short cheats show the benchmark is not robust to length cheat.

## Sources

**Length bias** (3 papers: [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf), [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/reber25a/reber25a.pdf), [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf))
> A disposition of a reward model to favor outputs based on their sequence length rather than their true quality.

**Length Bias** (1 paper: [Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf))
> A latent tendency for the model or reward signal to prefer longer responses over more succinct ones of equal content.

**Verbosity bias** (3 papers: [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf), [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf), [Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics](https://aclanthology.org/2025.emnlp-main.1307.pdf))
> The tendency of an LLM-based evaluator to prefer longer, more verbose responses, irrespective of their actual quality.

## Relationships

### Verbosity bias →
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > when biased RMs are employed in RLHF, these biases can be further amplified (Zheng et al., 2023b), with the LLM learning to exploit these biases rather than improving genuine task performance—a phenomenon known as reward hacking. (Section 1)
  - [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf)

### Associated with
- **Human preference alignment** (construct), 1 paper
  > Despite its advantages, DPO suffers from a length bias problem, which is caused by the unbalanced length preference due to the non-uniform length distribution of chosen and rejected responses. (Section 1)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurement instrument), 1 paper
  > Additionally, the LC win rates of our cheats are generally higher than the raw win rates because of their short length, which highlights that AlpacaEval 2.0 is also not robust to length cheat.
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)
