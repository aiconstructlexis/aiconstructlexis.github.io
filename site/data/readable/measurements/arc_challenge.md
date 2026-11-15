# ARC-Challenge
**Type:** Measurement instrument  
**Supporting papers:** 261  
**Also known as:** ARC Challenge, ARC-challenge, ARC-C, ARC-c, Arc-C, ARC (Challenge), Arc Challenge, Arc-Challenge, Arc-challenge, ArcChallenge, ARCC, ARC_C, Arc-c  

## State of the Field

**What it is.** Across papers, the prevailing description is the challenge subset of the AI2 Reasoning Challenge, a harder benchmark of difficult multiple-choice science questions, often grade-school level or drawn from scientific exams and standardized natural science tests, and often said to be hard for simple retrieval or word co-occurrence methods. Many definitions frame it as a harder split of ARC or ARC-Easy for question answering and reasoning, and papers variously describe it as 4-option MCQs, a closed-set reasoning dataset, a commonsense or scientific reasoning benchmark, and in one case an open-book QA dataset. Several papers note that the challenge test set has 1,172 examples or questions.

**What it is claimed to measure.** Papers use ARC-Challenge to measure a broad mix of targets, with 15 linked constructs and 12 linked behavioral indicators. The most common construct-level uses are commonsense reasoning, reasoning, and natural language understanding, while the recurring indicator-level uses are multiple-choice question answering and scientific question answering. The claims spread across many targets rather than converging on one framing.

**Space of uses.** The prevailing use is as one component of larger benchmark batteries rather than a standalone instrument, usually with zero-shot accuracy reporting, though some papers use 25-shot evaluation or 3-shot chain-of-thought prompting. It is related to three other measurement instruments, lm-evaluation-harness, OpenCompass, and OLMES, and papers commonly place it alongside ARC-Easy and other multiple-choice benchmarks in broader downstream, short-context, or generalization evaluations.

**Concerns raised.** The concerns that appear focus on contamination. One paper considered it as a source for an omni-modality benchmark suite but did not use it because of data contamination concerns, and another reports slight evidence of contamination with GPT-4-0613 when probing the dataset.

## Sources

**ARC Challenge** (4 papers: [Dynamic Sparse No Training: Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf))
> The challenge set of the AI2 Reasoning Challenge (ARC), a benchmark consisting of difficult, multiple-choice science questions that are hard to answer with simple retrieval or word co-occurrence.

**ARC-challenge** (17 papers: [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf), [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf), [HIGGS: Pushing the Limits of Large Language Model Quantization via the Linearity Theorem](https://aclanthology.org/2025.naacl-long.543.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf), [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf), [Iterative Reasoning Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d37c9ad425fe5b65304d500c6edcba00-Paper-Conference.pdf), [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf), [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf), [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf), [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf), [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf), [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf), [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf), [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf))
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing difficult science questions, used to evaluate question answering ability in a zero-shot setting.

**ARC-Challenge** (13 papers: [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf), [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf), [SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators](https://proceedings.iclr.cc/paper_files/paper/2025/file/222a2a46018a1e7b55ba48ba11932d04-Paper-Conference.pdf), [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf), [Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](https://aclanthology.org/2025.acl-long.123.pdf), [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf), [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf))
> A multiple-choice reasoning dataset created from scientific exams used to evaluate closed-set reasoning performance.

**ARC-C** (30 papers: [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf), [An Orthogonal High-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.emnlp-main.951.pdf), [Direct Value Optimization: Improving Chain-of-Thought Reasoning in LLMs with Refined Values](https://aclanthology.org/2025.emnlp-main.668.pdf), [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf), [FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.735.pdf), [GRASP: Replace Redundant Layers with Adaptive Singular Parameters for Efficient Model Compression](https://aclanthology.org/2025.emnlp-main.1338.pdf), [HD-PiSSA: High-Rank Distributed Orthogonal Adaptation](https://aclanthology.org/2025.emnlp-main.330.pdf), [LoRACoE: Improving Large Language Model via Composition-based LoRA Expert](https://aclanthology.org/2025.emnlp-main.1594.pdf), [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf), [RLAE: Reinforcement Learning-Assisted Ensemble for LLMs](https://aclanthology.org/2025.emnlp-main.680.pdf), [Router-Tuning: A Simple and Effective Approach for Dynamic Depth](https://aclanthology.org/2025.emnlp-main.99.pdf), [Same Question, Different Words: A Latent Adversarial Framework for Prompt Robustness](https://aclanthology.org/2025.emnlp-main.1595.pdf), [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf), [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf), [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf), [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf), [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf), [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf), [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf), [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf))
> The AI2 Reasoning Challenge (Challenge Set), a multiple-choice question-answering dataset of difficult science questions intended to test commonsense reasoning.

**ARC-c** (3 papers: [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf), [Dynamic and Generalizable Process Reward Modeling](https://aclanthology.org/2025.acl-long.212.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf))
> An AI2 Reasoning Challenge evaluation set used for zero-shot commonsense question answering.

**Arc-Challenge** (1 paper: [OmnixR: Evaluating Omni-modality Language Models on Reasoning across Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa3e67220ca4cd50010165c950fc8056-Paper-Conference.pdf))
> A question-answering benchmark based on science questions, considered as a potential source for the Omni×R suite but ultimately not used due to data contamination concerns.

**Arc-challenge** (1 paper: [Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf))
> Benchmark dataset used to evaluate science question answering.

**Arc Challenge** (2 papers: [Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf), [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.291.pdf))
> A benchmark for commonsense reasoning that features challenging, grade-school-level science questions.

**ARC (Challenge)** (1 paper: [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf))
> AI2 Reasoning Challenge Challenge, a multiple-choice question-answering benchmark used to assess harder downstream reasoning performance.

**Arc-C** (1 paper: [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f48b5133e89854a9e97cc22a6db83f25-Paper-Conference.pdf))
> The AI2 Reasoning Challenge (Challenge Set), a benchmark of difficult, grade-school level science questions used to evaluate a model's question answering and reasoning abilities.

**ArcChallenge** (1 paper: [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf))
> ARC-Challenge benchmark used to evaluate LLM performance on science question answering.

**ARCC** (2 papers: [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf), [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf))
> The AI2 Reasoning Challenge - Challenge Set (ARCC) is a difficult subset of the ARC dataset, containing science questions that are hard to answer with simple retrieval-based methods.

**Arc-c** (1 paper: [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf))
> Open benchmark assessing commonsense reasoning through challenge sets in science questions.

**ARC_C** (2 papers: [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf))
> A benchmark from the Language Model Evaluation Harness used to evaluate zero-shot language understanding and reasoning.

## Relationships

### → ARC-Challenge
- **Commonsense reasoning** (construct): *measured_by*, 37 papers
  > For the text modality, we compare the zero-shot performance on some common sense reasoning tasks: PIQA (Bisk et al., 2020), ARC-Challenge, ARC-Easy (Clark et al., 2018), StoryCloze (Mostafazadeh et al., 2016), Winograd, and Winogrande (Sakaguchi et al., 2021). (Table 1)
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
  - [PB-LLM: Partially Binarized Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3ab228c4703c4459b1a600ebadc5732c-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
  - [Unleashing the Power of Task-Specific Directions in Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3d101702194a5a345d81cdee4fe966f-Paper-Conference.pdf)
  - [You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf)
  - [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
  - [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf)
  - [Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44efaa3b7a389ea56c7ee9d6589e800-Paper-Conference.pdf)
  - [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf)
  - [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf)
  - [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [SlimLLM: Accurate Structured Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25a/guo25a.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singular Value Decomposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25az/li25az.pdf)
  - [Prompt-based Depth Pruning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wee25a/wee25a.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [An Orthogonal High-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.emnlp-main.951.pdf)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs](https://aclanthology.org/2025.emnlp-main.481.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Reasoning** (construct): *measured_by*, 13 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 8 papers
  > We conduct experiments on MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and CommonsenseQA (CSQA) (Talmor et al., 2019), which are all MCQ benchmarks widely used for LLM evaluation.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
  - [Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2d80dc5b407e16b258abe3056402372-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1474.pdf)
  - [Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements](https://aclanthology.org/2025.emnlp-main.1362.pdf)
- **Natural language understanding** (construct): *measured_by*, 6 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 4 papers
  > Figure 4 shows the downstream performance on HellaSwag, MMLU Var3, ARC-Challenge, and SciQ. PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities.
  - [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf)
  - [Dynamic and Generalizable Process Reward Modeling](https://aclanthology.org/2025.acl-long.212.pdf)
- **General ability** (construct): *measured_by*, 3 papers
  > Concurrently, we assess the models’ general capabilities using representative NLP tasks including MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and GSM8K (Cobbe et al., 2021), ensuring that safety improvements do not come at the cost of overall performance.
  - [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Short-context ability** (construct): *measured_by*, 3 papers
  > We select 8 short-context tasks commonly used for evaluating the general capabilities of models. These include... ARC-Challenge (ARC-C)... (Section 4.1)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
- **Scientific question answering** (behavioral indicator): *measured_by*, 3 papers
  > Comprehensive Examination: ... ARC-C (0-shot) (Clark et al., 2018), collected from standardized natural science tests (Section 5.1).
  - [Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
- **Scientific reasoning** (construct): *measured_by*, 3 papers
  > we evaluate the proposed TOW on ... ARC-Challenge (Clark et al., 2018) for scientific reasoning.
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf)
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.759.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > Second, we consider standard academic benchmarks used to evaluate large language models, such as question answering or Cloze-style problems. We use the following datasets: ARC challenge (Clark et al., 2018)...
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **Zero-shot question answering** (behavioral indicator): *measured_by*, 2 papers
  > "we evaluate our method and other methods on five well-known zero-shot tasks: PIQA [4]; WinoGrande [33]; HellaSwag [45]; ARC-e and ARC-c [6]."
  - [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > World Knowledge (WK): Jeopardy-3-shots [3], ArcEasy-3-shots [13], ArcChallenge-3-shots [13], and WikiDataQA-3-shots [4]
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Knowledge** (construct): *measured_by*, 1 paper
  > For track 1, we adopt commonly used MMLU [16], Arc-eacy [3], and Arc-challenge [3] to evaluate the knowledge ability of LLMs.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Zero-shot classification** (behavioral indicator): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Few-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > Interestingly, CREAM improves over Llama2-7B on ARC-C and HellaSwag. This is because these two tasks are few-shot tasks with longer prompts...
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > Specifically, we calculate prediction accuracies on the following three benchmarks: (1) HellaSwag (Zellers et al., 2019): inference the most plausible continuation for daily events (70K problems); (2) WinoGrande (Sakaguchi et al., 2019): assesses commonsense reasoning (44K problems); (3) ARC-Challenge (Clark et al., 2018): complex reasoning and understanding of scientific concepts (7.8K problems)... to investigate the extent of forgetting
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Factual knowledge** (construct): *measured_by*, 1 paper
  > "Knowledge-Focused Tasks include ARC-Challenge and ARC-Easy (Clark et al., 2018), PIQA (Bisk et al., 2019), Winogrande (Sakaguchi et al., 2019), OpenBookQA (Mihaylov et al., 2018), and HellaSwag (Zellers et al., 2019). These benchmarks primarily assess factual knowledge"
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **Calibration** (construct): *measured_by*, 1 paper
  > We evaluate the ECE and Accuracy using four diverse datasets: MMLU, MedMCQA, OpenBookQA, Arc-Challenge... (Section 6.1)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **Analogical reasoning** (construct): *measured_by*, 1 paper
  > “ARC-Challenge (Clark et al., 2018) which uses a 4-choice format” and “ARC-Challenge centers on Analogical and Inductive Reasoning”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **Functional linguistic competence** (construct): *measured_by*, 1 paper
  > To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)) (Section 3.3)
  - [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Multilingual ability** (construct): *measured_by*, 1 paper
  > As shown in table 1, the resulting merged model surpasses each language-specific variant by up to 19% in accuracy on the ARC-Challenge dataset (Clark et al., 2018).
  - [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 2 papers
  > Table 2: Zero-shot performance on Language Model Evaluation Harness [56]... ARC_C
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **OpenCompass** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **OLMES** (measurement instrument), 1 paper
  > "We use the OLMES suite of 10 multiple choice question answering benchmarks (Gu et al., 2024): MMLU ... ARC Challenge (Clark et al., 2018), ARC Easy ..."
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
