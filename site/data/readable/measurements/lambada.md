# LAMBADA
**Type:** Measurement instrument  
**Supporting papers:** 103  
**Also known as:** Lambada, LAMBADA-standard  

## State of the Field

**What it is.** Across papers, the prevailing usage treats LAMBADA as a language modeling or word-prediction benchmark or dataset in which models predict the final word of a passage or sentence from full passage, paragraph, or broad discourse context. Definitions repeatedly frame it as testing long-range dependencies, long-context recall, contextual comprehension, or text understanding, and one paper describes it as a collection of narrative passages designed for discourse-based prediction. A smaller line of work instead labels it a reading comprehension benchmark, and papers also refer to variants such as LAMBADA (OpenAI) and LAMBADA-standard (LS).

**What it is claimed to measure.** Papers use LAMBADA to measure 8 constructs and 5 behavioral indicators, so its reported target is spread across several framings rather than concentrated on one. The most recurrent links are that papers use it to measure Commonsense reasoning, Language modeling ability, Natural language understanding, Downstream task performance, and Zero-shot task performance, with the remaining links covering 5 other constructs and 3 other behavioral indicators.

**Space of uses.** Most commonly, papers include LAMBADA as one item in broader zero-shot or downstream evaluation suites rather than as a standalone check, alongside PTB, WikiText-2, WikiText103, and HellaSwag, among others. They often report accuracy, perplexity, or both on it, and several papers run it without fine-tuning; a smaller line of work uses it as a validation task for language model pre-training. At the instrument level, papers only relate LAMBADA to lm-evaluation-harness, which they use to conduct evaluations that include it.

## Sources

**LAMBADA** (26 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [Efficient Streaming Language Models with Attention Sinks](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf), [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.509.pdf), [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [CartesianMoE: Boosting Knowledge Sharing among Experts via Cartesian Product Routing in Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.505.pdf), [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf), [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf), [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf), [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf), [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf), [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf), [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf))
> A language modeling task that evaluates the ability to predict the last word in a sentence requiring broad discourse context, used here to test length prediction reliability.

**Lambada** (3 papers: [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf), [Mamba-Shedder: Post-Transformer Compression for Efficient Selective Structured State Space Models](https://aclanthology.org/2025.naacl-long.195.pdf))
> A reading comprehension benchmark included in the expanded evaluation set.

**LAMBADA-standard** (1 paper: [MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf))
> The standard version of the LAMBADA dataset for evaluating a model's ability to predict the final word of a text passage.

## Relationships

### → LAMBADA
- **Commonsense reasoning** (construct): *measured_by*, 4 papers
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 3 papers
  > exceeding the performance of AR models in text quality and on the LAMBADA natural language understanding benchmark.
  - [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Language modeling ability** (construct): *measured_by*, 3 papers
  > We chose the LAMBADA dataset (Paperno et al., 2016) for evaluation, as it tests a model’s ability to predict the final word of a passage, directly assessing language modeling capability without relying on specific knowledge, making it suitable for comparing models with small-scale training. (Section 6.3.2)
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **Contextual understanding** (construct): *measured_by*, 2 papers
  > These benchmarks assess different aspects of LLM emergent abilities: Lambada evaluates contextual comprehension, testing the model’s ability to understand long-range dependencies in text. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > We evaluate Spectra Suite models using eight distinct common-sense and reasoning benchmarks consisting of tasks from logical and reasoning questions to grounded and physical commonsense tasks: Arc Easy, Arc Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), HellaSWAG (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PIQA (Bisk et al., 2019), LAMBADA (Paperno et al., 2016), LogiQA (Liu et al., 2021), all under zero-shot settings. (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... Lambada... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... lambada
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 2 papers
  > We measure the zero-evaluation performance of trained GPT models on LAMBADA and WikiText using perplexity scores. (Section 5.2)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > "We evaluate the pre-trained base models on 17 tasks across different general domains which include: MMLU (Hendrycks et al., 2020), Arc-Easy, Arc-Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), SciQ (Welbl et al., 2017), RTE (Dagan et al., 2005), BBH (Suzgun et al., 2022), LAMBADA"
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate our models on the LAMBADA dataset and report accuracy and perplexity for zero-shot generation in Figure 4.
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > “a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29].”
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 2 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
