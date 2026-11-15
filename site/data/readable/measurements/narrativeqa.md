# NarrativeQA
**Type:** Measurement instrument  
**Supporting papers:** 28  

## State of the Field

**What it is.** Across the surveyed work, the prevailing description of NarrativeQA is a long-context question-answering or reading-comprehension benchmark over narrative texts, usually entire books and movie scripts or transcripts. Papers describe question-answer pairs tied to full stories or long text segments, with the task framed as generating free-form answers from the text; one account says the questions are concatenated to text segments, while another says each example includes a full story and corresponding QA pairs. Some authors place it within SCROLL or SCROLLS, and one paper instead describes annotators reading novel summaries to write questions.

**What it is claimed to measure.** Papers link NarrativeQA to 2 behavioral indicators and 2 constructs. The most common use is to measure Question answering and Document question answering: it is described as an established QA dataset, a single-doc QA benchmark, and a long-document question-answering dataset about stories, books, or movie scripts. A smaller line of work uses it to measure Long-context understanding, including claims that it assesses comprehension of long-form narrative structures beyond simple content matching, and one paper also uses it to measure Length generalization through length extrapolation on long benchmarks. Overall, papers use it mainly for QA-oriented evaluation.

**Space of uses.** Papers commonly include NarrativeQA in multi-benchmark evaluations for long-context tasks, often alongside QASPER, QuALITY, TriviaQA, QMSum, and ContractNLI. It is used for zero-shot evaluation across different context lengths, F1-based long-sequence or long-document QA evaluation, and, in one case, generating agentic workflow traces from its 14.7K training QA pairs. Papers link it to 1 other instrument, SCROLLS, and one paper places it among long-context open-book QA tasks in that dataset.

## Sources

**NarrativeQA** (14 papers: [Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf), [NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/3adb85a348a18cdd74ce99fbbab20301-Paper-Conference.pdf), [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf), [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf), [E2LLM: Encoder Elongated Large Language Models for Long-Context Understanding and Reasoning](https://aclanthology.org/2025.emnlp-main.970.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf))
> A question-answering dataset where the task is to generate free-form answers based on provided text segments, such as stories or book chapters.

## Relationships

### → NarrativeQA
- **Question answering** (behavioral indicator): *measured_by*, 5 papers
  > NarrativeQA (NQA) (Koˇciský et al., 2018) is an established question answering dataset over entire books from Project Gutenberg3 and movie scripts from a list of websites.
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 4 papers
  > We use NarrativeQA (Koˇcisk´y et al., 2018) ... for evaluating long-document QA.
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf)
  - [Compute or Load KV Cache? Why Not Both?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25d/jin25d.pdf)
  - [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf)
- **Long-context understanding** (construct): *measured_by*, 2 papers
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... NarrativeQA [44]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)

### Associated with
- **SCROLLS** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018)... (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
