# FiQA
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Papers most commonly treat FiQA as a retrieval benchmark within BEIR. Definitions variously describe it as a single-hop retrieval benchmark whose corpus consists of human-written responses to the search queries, as a dataset from the BEIR benchmark for financial question answering, and as a financial QA benchmark used for downstream evaluation; one paper also describes using it as a retrieval dataset for generating and evaluating adversarial passages in corpus-poisoning experiments.

**What it is claimed to measure.** Measurement claims are concentrated on one target: papers link FiQA to no constructs and to one behavioral indicator, financial question answering. In Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics and Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models, papers use it to measure financial question answering, including the label "FiQA (Maia et al., 2018), Financial QA."

**Space of uses.** Papers usually position FiQA within BEIR, and BEIR is the only linked measurement instrument through a related link. In use, papers include it among BEIR retrieval benchmarks, pair it with NFCorpus, SciFact, and SciDocs in a BEIROOC evaluation setup, use ROUGE-L for FiQA in one downstream evaluation setting, and use it to generate and evaluate adversarial passages in corpus-poisoning experiments.

## Sources

**FiQA** (4 papers: [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf), [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.334.pdf), [Tricking Retrievers with Influential Tokens: An Efficient Black-Box Corpus Poisoning Attack](https://aclanthology.org/2025.naacl-long.210.pdf), [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf))
> A BEIR dataset used as a single-hop retrieval benchmark where passages are human-written responses to search queries.

## Relationships

### → FiQA
- **Financial question answering** (behavioral indicator): *measured_by*, 2 papers
  > FIQA for financial question answering (Section 4.3).
  - [Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics](https://aclanthology.org/2025.emnlp-main.1307.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)

### Associated with
- **BEIR** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... FiQA (Maia et al., 2018)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
