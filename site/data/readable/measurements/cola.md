# CoLA
**Type:** Measurement instrument  
**Supporting papers:** 35  
**Also known as:** GLUE-COLA, GLUE-CoLA  

## State of the Field

**What it is.** Across papers, CoLA is most commonly described as the Corpus of Linguistic Acceptability, usually framed as a GLUE task or benchmark for grammatical or linguistic acceptability. The prevailing usage treats it as a binary, often single-sentence classification task in which English sentences are judged as grammatically acceptable or unacceptable, or simply grammatically correct. Some papers use the surface names GLUE-COLA or GLUE-CoLA, and one definition instead describes GLUE-CoLA as a dataset of text from books and journal articles used in TDDBench.

**What it is claimed to measure.** Papers use CoLA to measure 3 constructs and 2 behavioral indicators. The dominant behavioral claim is that it measures grammatical acceptability judgment, with papers describing the task as deciding whether a sentence is acceptable or unacceptable; a smaller line of work also treats it as text classification. At the construct level, it is most often used to measure natural language understanding, and some papers also report it as measuring general ability and generalization, so its measurement claims are spread across several constructs rather than centered on one alone.

**Space of uses.** Most papers position CoLA as one task within larger evaluation suites, especially GLUE, which is the only linked instrument and is described as related to CoLA. Across the surveyed work, it is used for fine-tuning and development-set reporting, close-ended in-context learning on an out-of-domain dataset, downstream capability checks after editing, robustness testing under bit-flip errors, and as part of TDDBench for training data detection. Some papers also present it as an unseen task or as one of several general capability tests.

## Sources

**CoLA** (14 papers: [Fast-ELECTRA for Efficient Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e5f58d98523298cba093f658cfdf2d6-Paper-Conference.pdf), [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [ReLoRA: High-Rank Training Through Low-Rank Updates](https://proceedings.iclr.cc/paper_files/paper/2024/file/d6fdc308a3b0f017f16059e5888f3346-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf), [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf), [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf), [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf), [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf))
> The Corpus of Linguistic Acceptability benchmark, used here as a downstream grammatical acceptability evaluation.

**GLUE-COLA** (1 paper: [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf))
> The Corpus of Linguistic Acceptability, a task from the GLUE benchmark for determining if a sentence is grammatically correct.

**GLUE-CoLA** (1 paper: [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf))
> A dataset of text from books and journal articles, part of the GLUE benchmark, used in TDDBench to evaluate TDD algorithms.

## Relationships

### → CoLA
- **Natural language understanding** (construct): *measured_by*, 4 papers
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
- **Grammatical acceptability judgment** (behavioral indicator): *measured_by*, 4 papers
  > CoLA (Corpus of Linguistic Acceptability) (Warstadt et al., 2019) is a single-sentence classification task, where sentences are annotated as either grammatically acceptable or unacceptable (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In Table 3, we observe that ELICIT significantly improves model performance on unseen tasks (GLUE-COLA, BBQ Religion, Deepmind (Saxton et al., 2019), MMLU-Psychology, and BBH-Logical-Deduction-Five-objects) not present in its capability library. (Section 4.4).
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > Following Zhang et al. (2023b), we evaluate on a series of Text Classification datasets: CoLA (2 labels) (Warstadt et al., 2019)... (Section 3.1)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 5. CoLA (Corpus of Linguistic Acceptability) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurement instrument), 2 papers
  > In this context, our evaluation is conducted across 6 datasets from the GLUE: SST-2, MRPC, CoLA, QNLI, RTE, and STS-B. (Section 4.2)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
