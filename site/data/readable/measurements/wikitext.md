# WikiText
**Type:** Measurement instrument  
**Supporting papers:** 52  
**Also known as:** Wikitext  

## State of the Field

**What it is.** Across papers, WikiText is most commonly described as a language modeling benchmark or corpus built from Wikipedia text, often evaluated through perplexity on a held-out or validation split. Some definitions make this more specific by calling it high-quality encyclopedic text, in one case limited to articles marked Good or Featured by human editors, while others refer to Wikitext-2 or frame it as a long-context benchmark across different context lengths. A smaller line of work uses the name for training or calibration data rather than only evaluation, including pre-training on the corpus and using random segments from it for calibration or profiling.

**What it is claimed to measure.** Papers link WikiText to 5 constructs and 2 behavioral indicators. The most common measurement claims are for general ability and language modeling ability, followed by zero-shot generalization and confidence; another reported use is to measure long-form text generation, and the remaining recorded links are 1 other behavioral indicator and 1 related construct. Across these uses, the evidence is phrased in terms of perplexity, cross-entropy loss, likelihood, and prediction confidence, so papers use the benchmark for several different evaluation targets rather than a single one. One paper separately reports that WikiText is related to factual knowledge through encyclopedic data used to maintain general factual knowledge.

**Space of uses.** No measurement instrument is linked to WikiText through recorded relationships. In paper descriptions, it is commonly one part of a broader evaluation setup, appearing alongside MMLU, ARC-C, GSM8K, and BBH, while most often supplying held-out or validation text for perplexity reporting. Smaller uses are more auxiliary: papers use the validation split to measure activation sparsity and record preactivation distributions, use the corpus for pre-training or auxiliary language modeling during RL fine-tuning, use random segments for calibration and expert parallelism profiling, and in one case train on WikiText before evaluating on WikiSection.

## Sources

**WikiText** (12 papers: [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf), [ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf), [Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf), [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf), [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf), [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.509.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [DLP: Dynamic Layerwise Pruning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25l/chen25l.pdf), [BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.151.pdf))
> A benchmark dataset used to evaluate language modeling performance by measuring perplexity on a held-out validation set of natural text.

**Wikitext** (2 papers: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf), [ALinFiK: Learning to Approximate Linearized Future Influence Kernel for Scalable Third-Party LLM Data Valuation](https://aclanthology.org/2025.naacl-long.589.pdf))
> A language-model evaluation benchmark used here to assess long-context language modeling across different context lengths.

## Relationships

### → WikiText
- **General ability** (construct): *measured_by*, 3 papers
  > We adopt the Evaluation Harness framework (Gao et al., 2023) for general capability evaluation, including MMLU (5-shot, Hendrycks et al., 2020), ARC-C (Clark et al., 2018) and WIKITEXT (Merity et al., 2016) (Section 4).
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Language modeling ability** (construct): *measured_by*, 3 papers
  > “we examine the impact of these intervention strategies on both task performance and language modeling capability, with the latter measured using cross-entropy loss on the pre-training dataset (i.e, WikiText).”
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... Wikitext... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Long-form text generation** (behavioral indicator): *measured_by*, 1 paper
  > Long-text Generation: WikiText (Merity et al., 2016), and HelloBench (Que et al., 2024).
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **Confidence** (construct): *measured_by*, 1 paper
  > "WikiText (Merity et al., 2022) to assess the model’s prediction confidence" (Section 5.1, Datasets)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > We measure the zero-evaluation performance of trained GPT models on LAMBADA and WikiText using perplexity scores. (Section 5.2)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)

### Associated with
- **Factual knowledge** (construct), 1 paper
  > The world fact loss uses encyclopedic data (e.g., WikiText (Merity et al., 2017)) to maintain general factual knowledge. (Section 1).
  - [OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.emnlp-main.183.pdf)
