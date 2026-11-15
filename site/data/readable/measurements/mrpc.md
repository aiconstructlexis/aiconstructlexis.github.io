# MRPC
**Type:** Measurement instrument  
**Supporting papers:** 36  

## State of the Field

**What it is.** Across the surveyed work, MRPC is most commonly described as the Microsoft Research Paraphrase Corpus, usually treated as a benchmark or dataset for paraphrase identification or detection between two sentences. Many papers place it within GLUE, while some frame it more specifically as a sentence-pair text classification task, a binary paraphrase detection task, or a test of whether two sentences are semantically equivalent. A few papers simply list it as one item in broader evaluation suites.

**What it is claimed to measure.** Papers link MRPC to 2 constructs and 1 behavioral indicator. The prevailing usage is to use it to measure paraphrase detection, often described as paraphrase identification or paraphrase tasks; a smaller line of work reports it as measuring natural language understanding or general ability. Overall, the measurement claims are concentrated on paraphrase detection rather than spread across many constructs.

**Space of uses.** In use, MRPC is usually positioned as one task inside a larger benchmark suite rather than a standalone instrument. The only linked instrument is GLUE, and papers often describe MRPC as a GLUE task or dataset used alongside SST-2, RTE, QQP, MNLI, and CoLA. Across the papers, it appears in evaluations of in-context learning, fine-tuning, compression, prompt tuning, and downstream capability after editing.

## Sources

**MRPC** (16 papers: [Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [In-Context Learning Learns Label Relationships but Is Not Conventional Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0db404e9cc9d282be6dfe8538352408c-Paper-Conference.pdf), [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf), [ReLoRA: High-Rank Training Through Low-Rank Updates](https://proceedings.iclr.cc/paper_files/paper/2024/file/d6fdc308a3b0f017f16059e5888f3346-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf), [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf), [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf), [Prompt Optimization with EASE? Efficient Ordering-aware Automated Selection of Exemplars](https://proceedings.neurips.cc/paper_files/paper/2024/file/dd8e7dae18cecd7c9137840161e1bf62-Paper-Conference.pdf), [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf), [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf))
> The Microsoft Research Paraphrase Corpus, a benchmark for detecting whether two sentences are paraphrases of each other.

## Relationships

### → MRPC
- **Paraphrase detection** (behavioral indicator): *measured_by*, 8 papers
  > paraphrasing: QQP, MRPC (Dolan & Brockett, 2005); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 2. MRPC (Microsoft Research Paraphrase Corpus) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurement instrument), 5 papers
  > MRPC in GLUE (Wang et al., 2019) (Section 4.1).
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
