# QMSum
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** SUM-QMSUM  

## State of the Field

**What it is.** Across the definitions, QMSum is most commonly described as a query-based, multi-domain meeting summarization dataset or benchmark, usually placed in SCROLL or SCROLLS. Papers generally describe meeting transcripts paired with summaries conditioned on specific questions about the dialogue, and one paper describes it as a human-annotated benchmark with 1,808 query-summary pairs over 232 meetings. Some authors add that it covers multiple domains or aggregates ICSI, AMI, and Parliament meetings, while a smaller framing under the label SUM-QMSUM treats it more generally as a benchmark for generating summaries of meeting transcripts.

**What it is claimed to measure.** Papers use QMSum to measure 2 constructs and 3 behavioral indicators. The behavioral uses cover text summarization, dialogue summarization, and query-focused summarization, while the construct uses are length generalization and long-context understanding. Taken together, these links span both summarization behaviors and broader long-context constructs.

**Space of uses.** As another measurement instrument, papers only explicitly relate QMSum to SCROLLS, and several definitions place it within SCROLL or SCROLLS, sometimes alongside GovReport, NarrativeQA, and Qasper. The prevailing use is as one task inside larger long-sequence or long-context evaluations. Some papers use it more narrowly, either only the "general queries" subset for global summarization, as a source of examples, to assess a summary component, or as source material for constructing CoPriva.

## Sources

**QMSum** (10 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf), [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf), [Graph of Records: Boosting Retrieval Augmented Generation for Long-context Summarization with Graphs](https://aclanthology.org/2025.acl-long.1159.pdf), [Keep Security! Benchmarking Security Policy Preservation in Large Language Model Contexts Against Indirect Attacks in Question Answering](https://aclanthology.org/2025.emnlp-main.345.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [Topic-Conversation Relevance (TCR) Dataset and Benchmarks](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd9b0883e4c9f0f0b3db673ce54dc8f2-Paper-Datasets_and_Benchmarks_Track.pdf))
> A query-based multi-domain meeting summarization dataset from the SCROLL benchmark.

**SUM-QMSUM** (1 paper: [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf))
> Summarization benchmark requiring models to generate summaries of meeting transcripts.

## Relationships

### → QMSum
- **Text summarization** (behavioral indicator): *measured_by*, 2 papers
  > Summarization. We pick two summarization datasets from SCROLLS. QMSum [93] is a query-based summarization dataset, formed by meeting transcripts from multiple domains
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... QMSum [105]. (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Dialogue summarization** (behavioral indicator): *measured_by*, 1 paper
  > dialogue summarization: samsum (Gliwa et al., 2019) and qmsum (Zhong et al., 2021) from LongBench (Bai et al., 2024)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
- **Query-focused summarization** (behavioral indicator): *measured_by*, 1 paper
  > QMSum (Zhong et al., 2021) is a human-annotated benchmark for a query-based multi-domain meeting summarization task, which consists of 1,808 query-summary pairs over 232 meetings in multiple domains. (Section 5.1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)

### Associated with
- **SCROLLS** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018), Qasper (Dasigi et al., 2021) and QMSum (Zhong et al., 2021). (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
