# Model collapse
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Distributional fidelity  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage describes model collapse as degradation in model performance tied to synthetic or self-generated training data, often over successive generations or iterative self-improvement. In this framing, papers mention worsening generalization, failure to improve with more data, and outputs becoming increasingly deterministic. Smaller lines of work use the same term for different phenomena: reduced token diversity over layers until tokens converge to a consensus state, or rapid collapse during training under unstable optimization. One theoretical paper also reframes the issue through distributional fidelity, the capacity to preserve the statistical properties of the true data distribution across generations.

**Space of facets.** Rather than a shared subtype scheme, papers use the term for several loci of failure: degradation from synthetic data in the training corpus, degradation within self-consuming or self-improvement loops, an internal transformer phenomenon where tokens cluster to a single consensus state, and a training-time collapse under a particular loss. The main disagreement is therefore about what collapses, overall performance and generalization, diversity of self-generated data and outputs, internal token representations, or the optimization process. Distributional fidelity appears as an alternative framing, with collapse prevention said to depend on preserving true-distribution statistics across generations and managing error propagation.

**Space of measurement.** Papers operationalize model collapse with 3 measurement instruments and 2 behavioral indicators. The named instruments are BabiStories, HelpSteer2, and MNIST, used in empirical confirmations or demonstrations of collapse, including shallow networks on MNIST, GPT-2 models on BabiStories, and Gemma2 fine-tuning on HelpSteer2 under different data replacement schemes. The linked behavioral indicators are misinformation generation and news summarization. Overall, these operationalizations mostly follow the synthetic-data degradation framing: they look for degraded task behavior or problematic outputs, and one HelpSteer2 setup reports collapse when previous data are replaced after each fitting iteration but not when new synthetic data accumulate with earlier real and synthetic data.

**Links.** Multiple papers claim a causal relationship from model collapse to Generalization, describing compromised ability to generalize to real-world data and effects on generalization error. Single-paper claims also link model collapse causally to Linguistic diversity, via loss of distributional tails and homogenized language, and to an additional output-related behavior. In the other direction, one paper claims a causal relationship from Overfitting to model collapse, and another from Recursive stability to model collapse, stating that under a recursive stability condition and a non-negligible level of real data, collapse can be avoided. Related, non-causal links connect model collapse to Semantic drift and to another task setting.

## Sources

**Model collapse** (3 papers: [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf), [Consensus Is All You Get: The Role of Attention in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abella25a/abella25a.pdf), [Superficial Self-Improved Reasoners Benefit from Model Merging](https://aclanthology.org/2025.emnlp-main.301.pdf))
> A latent degradation in model performance caused by training on synthetic data, characterized by worsening generalization and failure to improve with more data.

**Distributional fidelity** (1 paper: [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf))
> The capacity of a generative model to preserve the statistical properties of the true data distribution across successive generations of data synthesis.

## Relationships

### Model collapse →
- **Generalization** (construct): *causes*, 2 papers
  > Consequently, the model’s ability to generalize to real-world data is compromised, as it increasingly relies on the distorted distribution provided by prior AI generations rather than learning accurate representations of the real world. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Misinformation generation** (behavioral indicator): *causes*, 1 paper
  > If synthetic data is used in training these models, even in small quantities, the model can start producing “gibberish” or nonsensical outputs, contains misinformation, or reflect stereotypes. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **MNIST** (measurement instrument): *measured_by*, 1 paper
  > Our theoretical results are empirically confirmed with experiments in: • Toy settings, including random projections model on Gaussian data, and shallow networks fully trained on the MNIST dataset (Deng, 2012). (Section 1.1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **BabiStories** (measurement instrument): *measured_by*, 1 paper
  > Our theoretical results are empirically confirmed with experiments in: ... • Realistic setting of GPT-2 models trained on BabiStories (Zhang et al., 2024a) (Section 1.1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **HelpSteer2** (measurement instrument): *measured_by*, 1 paper
  > Fine-tuning Google’s Gemma2 models on Nvidia’s HelpSteer 2 dataset demonstrates that model collapse occurs if previous data are replaced after each model-fitting iteration (left), whereas model collapse is avoided if new synthetic data instead accumulate with previous real and synthetic data (right).
  - [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kazdan25a/kazdan25a.pdf)
- **Linguistic diversity** (construct): *causes*, 1 paper
  > “The loss of the distributional tails during early model collapse can reduce linguistic innovation and cognitive diversity ... due to homogenized language.”
  - [Large Language Models Threaten Language's Epistemic and Communicative Foundations](https://aclanthology.org/2025.emnlp-main.1457.pdf)

### → Model collapse
- **Overfitting** (construct): *causes*, 1 paper
  > this phenomenon arises as the model gradually overfits to patterns found in synthetic data, which may not fully represent the richness or variability of real-world data. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **Recursive stability** (construct): *causes*, 1 paper
  > Theorem 1 demonstrates that under a recursive stability condition and a non-negligible constant level of real data, model collapse can be avoided across a variety of model architectures.
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)

### Associated with
- **Semantic drift** (construct), 1 paper
  > Semantic drift and model collapse are linked in a loop of human and LLM language production
  - [Large Language Models Threaten Language's Epistemic and Communicative Foundations](https://aclanthology.org/2025.emnlp-main.1457.pdf)
- **News summarization** (behavioral indicator), 1 paper
  > We experiment with practical tasks – computing matrix eigenvalues with transformers and news summarization with LLMs – which both exhibit model collapse when trained on generated data
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
