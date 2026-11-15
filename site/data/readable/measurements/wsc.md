# WSC
**Type:** Measurement instrument  
**Supporting papers:** 32  
**Also known as:** Winograd  

## State of the Field

**What it is.** Most commonly, papers describe WSC, sometimes called Winograd, as the Winograd Schema Challenge, a benchmark or task for coreference resolution through ambiguous pronoun disambiguation, usually framed as requiring commonsense reasoning. Some definitions cast it more broadly as a reasoning benchmark for downstream evaluation, and one quoted passage says WSC contains multiple-choice questions. A smaller line of work treats Winograd as a language-modeling formulation of the SuperGLUE WSC task, and one paper uses a Winograd-schema-style direct-question prompt plus a one-shot variant, WSC-1sh.

**What it is claimed to measure.** Papers use WSC to measure 1 construct, Commonsense reasoning, and 3 behavioral indicators, most often Coreference resolution, then Downstream task performance and Language understanding task performance. The prevailing claims cluster around commonsense reasoning and coreference resolution: papers list WSC or Winograd among commonsense reasoning datasets and say it evaluates coreference resolution capabilities. Broader uses as a measure of downstream or language-understanding performance also appear, but as less central framings.

**Space of uses.** In practice, papers usually deploy WSC as one item in larger evaluation suites rather than as a standalone instrument. It is linked to 1 other instrument, SuperGLUE, and papers also place it alongside benchmarks such as Winogrande, PIQA, ARC-E or ARC-C, BoolQ, and COPA in zero-shot, downstream, NLU, OOD, and model-merging evaluations. Some papers position it explicitly as a SuperGLUE task, while one compares a standard WSC format with a one-shot variant.

## Sources

**WSC** (15 papers: [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [Making Language Models Robust Against Negation](https://aclanthology.org/2025.naacl-long.413.pdf), [Efficient and Accurate Prompt Optimization: the Benefit of Memory in Exemplar-Guided Reflection](https://aclanthology.org/2025.acl-long.37.pdf), [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf), [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf), [Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs](https://aclanthology.org/2025.emnlp-main.1527.pdf), [GRASP: Replace Redundant Layers with Adaptive Singular Parameters for Efficient Model Compression](https://aclanthology.org/2025.emnlp-main.1338.pdf), [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf), [MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models](https://aclanthology.org/2025.emnlp-main.935.pdf), [MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines](https://aclanthology.org/2025.emnlp-main.1022.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf), [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf), [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf))
> A coreference resolution benchmark requiring pronoun disambiguation.

**Winograd** (6 papers: [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf))
> Coreference resolution task involving pronoun disambiguation with linguistic and commonsense reasoning.

## Relationships

### → WSC
- **Commonsense reasoning** (construct): *measured_by*, 3 papers
  > For the text modality, we compare the zero-shot performance on some common sense reasoning tasks: PIQA (Bisk et al., 2020), ARC-Challenge, ARC-Easy (Clark et al., 2018), StoryCloze (Mostafazadeh et al., 2016), Winograd, and Winogrande (Sakaguchi et al., 2021). (Table 1)
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
  - [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Coreference resolution** (behavioral indicator): *measured_by*, 3 papers
  > “the Winograd Schema Challenge evaluates coreference resolution capabilities (WSC; Levesque et al., 2012)”
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > Language Understanding (LU): Lambada-OpenAI [44], Hellaswag-0-shot [65], Winograd-3-shots [30], and WinoGrande-5-shots [54].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)

### Associated with
- **SuperGLUE** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... WSC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
