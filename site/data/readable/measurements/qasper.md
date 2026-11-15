# Qasper
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** QASPER  

## State of the Field

**What it is.** Across the surveyed work, Qasper is most commonly described as a question-answering benchmark or dataset over full NLP or research papers, used for retrieval, open-book QA, and answering from long scientific documents. Definitions consistently frame its contexts as full papers or scientific articles, and one study describes it as including 5,049 questions across 1,585 NLP papers, with each question probing information embedded in the full text. Several papers note that it contains extractive, abstractive, yes/no, and unanswerable questions, and some definitions add that questions may be unanswerable from the provided abstract or full text. A smaller line of work refers to it as part of SCROLL or SCROLLS, one paper uses a Qasper subset from LongBench, and another filters and augments QASPER to derive 493 questions for a derived evaluation.

**What it is claimed to measure.** Papers link Qasper to 2 constructs and 3 behavioral indicators, and the prevailing use is to measure question answering. Several papers use it for question answering over research or NLP papers, while smaller uses treat it as measuring document question answering and synthetic recall, and as measuring the constructs of long-context understanding and length generalization. Overall, the measurement claims are centered on QA, with additional long-context and length-extrapolation uses.

**Space of uses.** Papers commonly use Qasper alongside NarrativeQA, QuALITY, QMSum, ContractNLI, and within SCROLLS, usually as one element in broader long-context or open-book QA evaluations. They position it variously as a benchmark for dense scientific papers, a long-sequence or length-extrapolation test, and a retrieval setting where questions are gathered from Qasper. Some work also reuses a subset or filtered questions from QASPER in derived evaluations.

## Sources

**QASPER** (9 papers: [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf), [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf), [AMOR: A Recipe for Building Adaptable Modular Knowledge Agents Through Process Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4595e77b045971a654edc5e3cd31989-Paper-Conference.pdf), [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d74033a247989e8f6f3bf9e0c9629fb5-Paper-Datasets_and_Benchmarks_Track.pdf))
> QASPER is a question-answering benchmark over full NLP papers, used here to assess retrieval and answering over long scientific documents.

**Qasper** (5 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf), [Enhancing Retrieval-Augmented Generation via Evidence Tree Search](https://aclanthology.org/2025.acl-long.1175.pdf), [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf))
> A dataset from the SCROLL benchmark for question answering about scientific papers, where questions may be unanswerable from the provided abstract or full text.

## Relationships

### → Qasper
- **Question answering** (behavioral indicator): *measured_by*, 6 papers
  > Qasper (QASP) (Dasigi et al., 2021) is a question answering dataset over NLP papers filtered from the Semantic Scholar Open Research Corpus (S2ORC) (Lo et al., 2020).
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Cost-efficient Collaboration between On-device and Cloud Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25a/narayan25a.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including Qasper [18]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 3. QASPER (Dasigi et al., 2021): A document-grounded, information-seeking question answering dataset”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Synthetic recall** (behavioral indicator): *measured_by*, 1 paper
  > In long-context retrieval scenario where questions are gathered from Qasper (Dasigi et al., 2021), MoDification-7B-32k yields 10.3 on Qasper, which is competitive with 10.2 from LLaMA-2-7B-32k. (Section 5)
  - [MoDification: Mixture of Depths Made Easy](https://aclanthology.org/2025.naacl-long.265.pdf)

### Associated with
- **SCROLLS** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018), Qasper (Dasigi et al., 2021)... (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
