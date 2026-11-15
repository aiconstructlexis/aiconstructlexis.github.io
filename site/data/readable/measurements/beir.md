# BEIR
**Type:** Measurement instrument  
**Supporting papers:** 22  
**Also known as:** BEIR benchmark  

## State of the Field

**What it is.** Most commonly, papers describe BEIR as a diverse collection or suite of retrieval datasets for evaluating out-of-domain or zero-shot performance. Definitions vary in expansion and scope, calling it the "Benchmark for Evaluation of Information Retrieval", "Benchmarking-IR", or, in one paper, "Broad Evaluation of Information Retrieval", and they frame it as supporting retrieval, ranking, and re-ranking across domains. The reported coverage also varies by paper: one refers to 18 datasets from various domains, another to 14 public retrieval datasets excluding MS MARCO, another to 15 retrieval tasks, and one definition names Covid, SciFact, DBpedia, and NFCorpus.

**What it is claimed to measure.** Across the linked claims, papers use BEIR to measure two constructs, Generalization and Retrieval effectiveness, and two behavioral indicators, Information retrieval and Ranking. The dominant measurement claim is information retrieval, usually framed as zero-shot or out-of-domain retrieval performance, while a smaller line of work uses it to assess generalization. More specific uses, reported by individual papers, treat it as measuring retrieval effectiveness or evaluating ranking and re-ranking.

**Space of uses.** Papers usually position BEIR as a standard, popular, or widely used benchmark, including for dense retrievers, ranking models, and re-rankers. It is linked to seven other instruments overall, and relationship claims report it as related to FEVER, FiQA, MTEB, NFCorpus, and Natural Questions, plus 2 other instruments. Separate quoted passages also show BEIR being used in joint evaluation with other benchmarks.

**Concerns raised.** A smaller line of work notes that BEIR does not contain instructions, placing it alongside other standard retrieval benchmark suites that omit instructions.

## Sources

**BEIR** (4 papers: [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf), [Sliding Windows Are Not the End: Exploring Full Ranking with Long-Context Large Language Models](https://aclanthology.org/2025.acl-long.8.pdf), [Utility-Focused LLM Annotation for Retrieval and Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.88.pdf), [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.597.pdf))
> The Benchmark for Evaluation of Information Retrieval (BEIR) is a collection of diverse datasets used to measure a model's out-of-domain retrieval performance.

**BEIR benchmark** (1 paper: [REALM: Recursive Relevance Modeling for LLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1218.pdf))
> Broad Evaluation of Information Retrieval benchmark, a diverse collection of datasets including Covid, SciFact, DBpedia, and NFCorpus, used to evaluate zero-shot retrieval and re-ranking performance across domains.

## Relationships

### → BEIR
- **Information retrieval** (behavioral indicator): *measured_by*, 5 papers
  > “BEIR dataset [52] is a popular benchmark for evaluating dense retrievers’ zero-shot effectiveness”
  - [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
  - [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf)
  - [Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval](https://aclanthology.org/2025.emnlp-main.888.pdf)
  - [Randomly Removing 50% of Dimensions in Text Embeddings has Minimal Impact on Retrieval and Classification Tasks](https://aclanthology.org/2025.emnlp-main.1410.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > Our main evaluations are conducted on BEIR (Thakur et al., 2021) and MIRACL (Zhang et al., 2023), to assess the generalization of dense retrievers and multilingual retrieval capability. (Section 4.5).
  - [DRAMA: Diverse Augmentation from Large Language Models to Smaller Dense Retrievers](https://aclanthology.org/2025.acl-long.1457.pdf)
  - [Multi-view-guided Passage Reranking with Large Language Models](https://aclanthology.org/2025.emnlp-main.1459.pdf)
- **Retrieval effectiveness** (construct): *measured_by*, 1 paper
  > We evaluate retrieval effectiveness using two retrieval benchmarks: MS MARCO (Bajaj et al., 2016) and BEIR (Thakur et al., 2021).
  - [ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance](https://aclanthology.org/2025.emnlp-main.963.pdf)
- **Ranking** (behavioral indicator): *measured_by*, 1 paper
  > We further evaluate QRRETRIEVER as a re-ranker on the standard BEIR benchmark (Thakur et al., 2021). (Section 1)
  - [Query-Focused Retrieval Heads Improve Long-Context Reasoning and Re-ranking](https://aclanthology.org/2025.emnlp-main.1214.pdf)

### Associated with
- **MTEB** (measurement instrument), 1 paper
  > “Note that our model also attains the highest scores in 15 retrieval tasks (commonly referred to as BEIR (Thakur et al., 2021)), 11 clustering tasks, and 12 classification tasks in the MTEB benchmark.”
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
- **TREC-COVID** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including TREC-COVID”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **NFCorpus** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including TREC-COVID (Voorhees et al., 2021), NFCorpus (Boteva et al., 2016)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **SciFact** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... SciFact (Wadden et al., 2020)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **FiQA** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... FiQA (Maia et al., 2018)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **FEVER** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... FEVER (Thorne et al., 2018)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... NQ (Kwiatkowski et al., 2019)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
