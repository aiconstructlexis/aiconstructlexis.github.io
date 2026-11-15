# ARC-Easy
**Type:** Measurement instrument  
**Supporting papers:** 198  
**Also known as:** ARC Easy, ARC-easy, Arc-easy, ArcEasy, ARC-E, ARC-e, ARC_e, ARC (Easy), Arc Easy, ARCE, Arc-e, ARC_E  

## State of the Field

**What it is.** Across papers, ARC-Easy is most commonly described as the easy split or easy set of the AI2 Reasoning Challenge, a multiple-choice science question-answering benchmark, often framed as grade-school or elementary-level science questions and frequently used in zero-shot evaluation. Several definitions say the easier questions can be answered with simple retrieval or text-matching, while others describe them as testing basic factual knowledge or reasoning. As one appendix notes, the easy subset "consists of 5,197 of the relatively easier reasoning questions" within an ARC collection of 7,787 items (LLM Circuit Analyses Are Consistent Across Training and Scale).

**What it is claimed to measure.** Papers link ARC-Easy to 10 constructs and 10 behavioral indicators, so its reported measurement role is broad rather than confined to one target. The prevailing usage is as a measure of commonsense reasoning, with recurring links to reasoning and natural language understanding; smaller lines of work also use it to measure general ability, world knowledge, benchmark overfitting, emergent abilities, factual knowledge, functional linguistic competence, and out-of-distribution generalization. On the behavioral side, it is most often reported as evaluating multiple-choice question answering, downstream task performance, machine reading comprehension, scientific question answering, and zero-shot question answering, with additional links to classification, language understanding task performance, question answering, zero-shot classification, and zero-shot task performance.

**Space of uses.** Most papers position ARC-Easy as one component of broader zero-shot or downstream evaluation batteries, commonly alongside PIQA, ARC-Challenge, HellaSwag, and WinoGrande, and sometimes BoolQ. It is also related to 3 evaluation suites, OLMES, OpenCompass, and lm-evaluation-harness. While the dominant usage is zero-shot multiple-choice evaluation, one paper also lists an ArcEasy-3-shots variant under world knowledge.

**Concerns raised.** Concern-focused discussion is limited, but a smaller line of work includes ARC-Easy in evaluations of data contamination and uses it to measure benchmark overfitting.

## Sources

**ARC Easy** (4 papers: [Dynamic Sparse No Training: Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf))
> AI2 Reasoning Challenge Easy subset used as a zero-shot question-answering benchmark.

**ARC-easy** (3 papers: [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf), [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf))
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing easier science questions, used to evaluate question answering ability in a zero-shot setting.

**ARC-Easy** (5 papers: [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators](https://proceedings.iclr.cc/paper_files/paper/2025/file/222a2a46018a1e7b55ba48ba11932d04-Paper-Conference.pdf), [GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.255.pdf), [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf), [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf))
> Science question answering dataset with easier multiple-choice questions that test basic factual knowledge.

**Arc-easy** (2 papers: [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf), [Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf))
> The easy set from the AI2 Reasoning Challenge (ARC), containing science questions that are answerable with simple retrieval and reasoning.

**ArcEasy** (1 paper: [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf))
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing easier science questions that can be answered with simple retrieval and text-matching.

**ARC-E** (12 papers: [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf), [Why and How LLMs Benefit from Knowledge Introspection in Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.352.pdf), [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf), [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf), [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf), [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf), [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf), [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf), [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf))
> The AI2 Reasoning Challenge (Easy Set), a multiple-choice question-answering dataset of science questions intended to test commonsense reasoning.

**ARC-e** (3 papers: [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf), [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf))
> An AI2 Reasoning Challenge evaluation set used for zero-shot commonsense question answering.

**ARC_e** (1 paper: [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf))
> The AI2 Reasoning Challenge (ARC) Easy Set, a collection of multiple-choice science questions designed to test reasoning.

**Arc Easy** (1 paper: [Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf))
> A benchmark for commonsense reasoning that features easier, grade-school-level science questions, complementing the Arc Challenge set.

**ARC (Easy)** (1 paper: [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf))
> A multiple-choice question answering benchmark (AI2 Reasoning Challenge) focusing on easy questions.

**ARCE** (1 paper: [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf))
> The AI2 Reasoning Challenge (ARCE) is a multiple-choice question answering benchmark focusing on science questions for elementary and middle school students.

**Arc-e** (1 paper: [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf))
> The AI2 Reasoning Challenge (Easy Set), a benchmark of grade-school science questions that are simpler than its challenge counterpart.

**ARC_E** (1 paper: [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf))
> AI2 Reasoning Challenge (Easy) dataset containing science questions that require reasoning to answer correctly.

## Relationships

### → ARC-Easy
- **Commonsense reasoning** (construct): *measured_by*, 34 papers
  > For the text modality, we compare the zero-shot performance on some common sense reasoning tasks: PIQA (Bisk et al., 2020), ARC-Challenge, ARC-Easy (Clark et al., 2018), StoryCloze (Mostafazadeh et al., 2016), Winograd, and Winogrande (Sakaguchi et al., 2021). (Table 1)
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [PB-LLM: Partially Binarized Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3ab228c4703c4459b1a600ebadc5732c-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
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
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
  - [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf)
  - [Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44efaa3b7a389ea56c7ee9d6589e800-Paper-Conference.pdf)
  - [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf)
  - [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [SlimLLM: Accurate Structured Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25a/guo25a.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singular Value Decomposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25az/li25az.pdf)
  - [Prompt-based Depth Pruning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wee25a/wee25a.pdf)
  - [An Orthogonal High-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.emnlp-main.951.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Reasoning** (construct): *measured_by*, 7 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Explaining Modern Gated-Linear RNNs via a Unified Implicit Attention Formulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **Natural language understanding** (construct): *measured_by*, 4 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 3 papers
  > "We also re-examined data collected during the Pythia training runs [5] on the SciQ [73], PIQA [8], WinoGrande [60], and ARC Easy [18] datasets. Each of these consist of a wide range of questions with multiple-choice answers"
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > “These models are trained further and evaluated on downstream tasks: ... ARC-e (Clark et al., 2018)”
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **World knowledge** (construct): *measured_by*, 2 papers
  > World Knowledge (WK): Jeopardy-3-shots [3], ArcEasy-3-shots [13], ArcChallenge-3-shots [13], and WikiDataQA-3-shots [4]
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 2 papers
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Zero-shot question answering** (behavioral indicator): *measured_by*, 2 papers
  > "we evaluate our method and other methods on five well-known zero-shot tasks: PIQA [4]; WinoGrande [33]; HellaSwag [45]; ARC-e and ARC-c [6]."
  - [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... 4K context: arc easy
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Scientific question answering** (behavioral indicator): *measured_by*, 2 papers
  > ARC Easy (Clark et al., 2018) Simple science questions. (Table 2)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > We conduct a comparative evaluation of PPC-GPT on QA datasets. Specifically, we include... ARC-E... (Section 5.1)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **Zero-shot classification** (behavioral indicator): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Emergent abilities** (construct): *measured_by*, 1 paper
  > These benchmarks assess different aspects of LLM emergent abilities: Lambada evaluates contextual comprehension... ARC-easy tests basic science knowledge and fundamental reasoning
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **Factual knowledge** (construct): *measured_by*, 1 paper
  > "Knowledge-Focused Tasks include ARC-Challenge and ARC-Easy (Clark et al., 2018), PIQA (Bisk et al., 2019), Winogrande (Sakaguchi et al., 2019), OpenBookQA (Mihaylov et al., 2018), and HellaSwag (Zellers et al., 2019). These benchmarks primarily assess factual knowledge"
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **Benchmark overfitting** (construct): *measured_by*, 1 paper
  > We evaluate the impact of data contamination using a mix of seven different benchmarks: ARC-Easy (Clark et al., 2018), Social-I-QA (Sap et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), BoolQ (Clark et al., 2019), MMLU (Hendrycks et al., 2021), and HellaSwag (Zellers et al., 2019). (Section 3.2)
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Functional linguistic competence** (construct): *measured_by*, 1 paper
  > To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)) (Section 3.3)
  - [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **OpenCompass** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **OLMES** (measurement instrument), 1 paper
  > "We use the OLMES suite of 10 multiple choice question answering benchmarks (Gu et al., 2024): MMLU ... ARC Easy (Clark et al., 2018), PIQA ..."
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
