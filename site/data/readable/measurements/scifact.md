# SciFact
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across papers, the prevailing description is a scientific fact-checking dataset or benchmark in which claims are verified using evidence from research papers. Definitions commonly say the evidence comes from sentences in papers and may require citation context, while some papers instead describe verification against scientific abstracts or a corpus of research abstracts. One paper also reports a split of 809 training claims and 300 test claims.

**What it is claimed to measure.** Papers link SciFact to one behavioral indicator, fact checking, and one construct, domain knowledge. The dominant use is to measure fact checking, with several papers explicitly listing it as a fact-checking dataset or among popular fact-checking datasets. A smaller line of work uses it to measure domain knowledge by sampling claims from SciFact in the science domain to investigate domain-specific factual knowledge.

**Space of uses.** Papers relate SciFact to one other instrument, BEIR. Some authors place it inside the BEIR benchmark, and one paper selected it for a challenging subset based on high ratios of out-of-corpus terms. In evaluation setups, papers also use it alongside other datasets in broader fact-checking and medical evaluations.

## Sources

**SciFact** (4 papers: [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.334.pdf), [CORRECT: Context- and Reference-Augmented Reasoning and Prompting for Fact-Checking](https://aclanthology.org/2025.naacl-long.154.pdf), [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf), [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf))
> Scientific fact-checking dataset where claims are verified using evidence sentences from research papers, often requiring citation context.

## Relationships

### → SciFact
- **Fact checking** (behavioral indicator): *measured_by*, 5 papers
  > Besides, we also take into account the SCIFACT [26] dataset, notable for its inclusion of scientific claims (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [CORRECT: Context- and Reference-Augmented Reasoning and Prompting for Fact-Checking](https://aclanthology.org/2025.naacl-long.154.pdf)
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
  - [Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1295.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **Domain knowledge** (construct): *measured_by*, 1 paper
  > To investigate this further [how LLMs possess the capability to access domain-specific factual knowledge], we sample claims from PubHealth (Kotonya & Toni, 2020) in the public health domain and SciFact (Wadden et al., 2022) in the science domain. (Section 2.1)
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)

### Associated with
- **BEIR** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... SciFact (Wadden et al., 2020)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
