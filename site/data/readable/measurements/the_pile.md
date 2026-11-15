# The Pile
**Type:** Measurement instrument  
**Supporting papers:** 44  
**Also known as:** Pile  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats The Pile as a large, diverse text corpus for language model pre-training. Definitions also describe it as an open-source English corpus for training and evaluation, as a validation or test corpus for next-token prediction, perplexity, and recall-related analyses, and as a source of subsets or splits for domain-specific studies. Some authors further specify coverage such as encyclopedic text, books, social media, code, reviews, and domains like arXiv, GitHub, and PubMed, while others refer to particular variants such as a deduplicated version or selected subsets.

**What it is claimed to measure.** Papers link The Pile to 3 constructs and 1 behavioral indicator. The construct links are to General ability, Long-context understanding, and Specialization, and the behavioral-indicator link is to Pre-training data detection. These claims are spread across several targets rather than centered on one: papers use losses on the Pile to measure general ability, refer to long-context understanding on Pile, treat Pile subsets as target specialization sets, and list Pile among benchmark datasets for detecting pre-training data.

**Space of uses.** Among recorded instrument links, papers relate The Pile to 2 other instruments, Books3 and Pile-CC, in work that trains on mixtures built from Pile subsets. More broadly, papers position it as both a pre-training corpus and an evaluation resource: models are trained from scratch on it, evaluated on its validation split or held-out subsets, and in narrower setups it is sampled for calibration data, random contexts, reconstruction and downstream evaluation data, empirical token-frequency estimates, co-occurrence counts, and domain-specialist datasets.

**Concerns raised.** One survey notes a possible overlap concern: ICAE is described as being trained and tested on The Pile, which may overlap with the training corpus of the LLM.

## Sources

**The Pile** (12 papers: [In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf), [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/06960915ba8674c7a898ec0b472b80ff-Paper-Conference.pdf), [Successor Heads: Recurring, Interpretable Attention Heads In The Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/2722a0ccf6acfe3d144fdbb0dedd80b5-Paper-Conference.pdf), [DEPT: Decoupled Embeddings for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/20ceffa1fcec0f882868e5b891e3e7fa-Paper-Conference.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [Geometric Signatures of Compositionality Across a Language Model's Lifetime](https://aclanthology.org/2025.acl-long.265.pdf), [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf), [Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups](https://aclanthology.org/2025.emnlp-main.942.pdf), [Confidence Regulation Neurons in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e21955c93dede886af1d0d362c756757-Paper-Conference.pdf), [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf))
> The Pile is a large text corpus used here as a pre-training dataset for language modeling comparisons.

**Pile** (6 papers: [Zoology: Measuring and Improving Recall in Efficient Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/448fc91f669c15d10364ee01d512cc10-Paper-Conference.pdf), [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf), [CartesianMoE: Boosting Knowledge Sharing among Experts via Cartesian Product Routing in Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.505.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [A Statistical and Multi-Perspective Revisiting of the Membership Inference Attack in Large Language Models](https://aclanthology.org/2025.acl-long.1114.pdf), [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf))
> The Pile language modeling dataset used here as a validation and test corpus for measuring next-token prediction and recall-related slices.

## Relationships

### → The Pile
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > Long-context understanding on Pile. (Figure 1)
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **Pre-training data detection** (behavioral indicator): *measured_by*, 1 paper
  > To verify the effectiveness of detection methods, we employ four common benchmark datasets for evaluations, including WikiMIA (Shi et al., 2024), ArXivTection (Duarte et al., 2024), BookTection (Duarte et al., 2024) BookMIA (Shi et al., 2024) and Pile (Maini et al., 2024). (Section 4.1)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > maintain the general-purpose ability (losses on the Pile) unchanged.
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **Specialization** (construct): *measured_by*, 1 paper
  > We consider 16 datasets from the PILE (Gao et al., 2020) as target specialization sets (Section 3)
  - [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf)

### Associated with
- **Pile-CC** (measurement instrument), 1 paper
  > We train 70M and 160M language models on the mixture of Github and Pile-CC subset from the Pile dataset (Section 3.1).
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **Books3** (measurement instrument), 1 paper
  > We train on the mixtures of GitHub, Pile-CC, and Books3 subset from the Pile for a total of 30B tokens (Section 3.2).
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
