# Overfitting
**Type:** Construct  
**Supporting papers:** 24  
**Also known as:** Overadaptation, Reward model over-optimization  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats overfitting as learning the training data too closely, including its noise, artifacts, formatting details, exact wording, or other specifics, so performance on new, unseen, or out-of-domain data degrades. Several definitions phrase this as a latent tendency or training state, while one paper gives a more directly observable version, where training performance continues to improve but eval or validation loss starts to rise. A narrower line of work specializes the idea to supervised fine-tuning, calling it overadaptation: fine-tuned models overly focus on downstream task data, lose pretrained knowledge, and generalize worse. Another specialized framing is reward model over-optimization, defined as better in-domain accuracy together with stagnating or degrading performance on out-of-distribution prompts or responses and loss of alignment to the true preference distribution.

**Space of facets.** Papers systematize the concept mostly by training regime and mechanism. The main variants are broad model overfitting, overadaptation in supervised fine-tuning, and reward model over-optimization; the second is explicitly described as overfitting to downstream task data, and the third as overfitting of a reward model to its train set. Some authors further pin the mechanism to memorization, describing overfitting as exact reproduction of responses or as memorizing full contexts at the expense of learning reusable subcontext statistics. This leaves the term covering both a general failure to generalize and narrower memorization-based patterns.

**Space of measurement.** Operationalization is mostly indirect and aligns with the dominant definition: papers detect overfitting through worsening generalization, such as poorer performance on unseen or out-of-domain data, increasing validation or eval loss despite continued training improvement, or a validation-loss U-curve. More specific operationalizations include exact reproduction of responses, out-of-domain splits used to assess whether a model suffers from overfitting, a procedure for detecting overfitting during training based on long-context memorization rather than subcontext statistics, and, for reward models, rising accuracy on Dtrain and DID while D∼Prompt, D∼Response, and D∼Mutual stagnate or degrade. Papers link the construct to 1 measurement instrument and 1 behavioral indicator, HumanEval and pre-training data detection, but these appear as related links rather than measured_by claims.

**Links.** Across relationship claims, overfitting is most often connected to generalization. Several papers claim a causal relationship from overfitting to generalization, often in language of reduced generalizability or poor generalization, while some others simply relate the two; a smaller cluster of papers also relates overfitting to robustness, describing resistance to overfitting as accompanying greater robustness. Elsewhere, one paper claims a causal relationship from memorization to overfitting, another from overfitting to model collapse, and single papers relate overfitting to pre-training data detection, HumanEval, and weak-to-strong generalization.

## Sources

**Overfitting** (10 papers: [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf), [Understanding Transformers via N-Gram Statistics](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1c446eebd9a317dd0e96b16908c821a-Paper-Conference.pdf), [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf), [Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets](https://aclanthology.org/2025.naacl-long.171.pdf), [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf), [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf))
> The phenomenon where a model learns the training data too closely, capturing noise and specific artifacts, which harms its ability to generalize to new data.

**Overadaptation** (1 paper: [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf))
> The latent tendency of a fine-tuned model to overfit to downstream task data, resulting in degraded generalization and loss of pretrained knowledge, analogous to harmful overfitting in statistical learning.

**Reward model over-optimization** (1 paper: [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf))
> A phenomenon where a reward model overfits to its training data, leading to increased accuracy on in-domain examples but degraded performance on out-of-distribution prompts or responses.

## Relationships

### Overfitting →
- **Generalization** (construct): *causes*, 8 papers
  > helping to mitigate overfitting, resulting in models that are more robust and generalise better to new data
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [In-Context Learning and Occam’s Razor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/elmoznino25b/elmoznino25b.pdf)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf)
- **Model collapse** (construct): *causes*, 1 paper
  > this phenomenon arises as the model gradually overfits to patterns found in synthetic data, which may not fully represent the richness or variability of real-world data. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)

### → Overfitting
- **Memorization** (construct): *causes*, 1 paper
  > This result suggests that some of the reason for overﬁtting is due to partial memorization of the test set. (Section 5.4)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Robustness** (construct), 2 papers
  > In contrast, mixed-domain models exhibit greater resistance to overfitting, suggesting potential improvements in domain-specific model robustness; (ABSTRACT)
  - [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf)
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Pre-training data detection** (behavioral indicator), 1 paper
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **HumanEval** (measurement instrument), 1 paper
  > This indicates some level of overfitting to HUMANEVAL.
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Weak-to-strong generalization** (construct), 1 paper
  > Although weak-to-strong generalization exhibiting certain generalization capabilities, strong models exhibit significant overfitting in weak-to-strong generalization: Due to the strong fit ability of strong models, erroneous labels from weak supervisors may lead to overfitting in strong models. (Section 1)
  - [How to Mitigate Overfitting in Weak-to-strong Generalization?](https://aclanthology.org/2025.acl-long.784.pdf)
