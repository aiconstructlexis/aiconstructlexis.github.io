# Ranking
**Type:** Behavioral indicator  
**Supporting papers:** 47  
**Also known as:** Image reranking, Code reranking, Website reranking, Document reranking, Zero-shot reranking, Zero-shot re-ranking, Passage re-ranking, Document re-ranking, Listwise reranking, Passage reranking, Re-ranking, Information reranking, Candidate re-ranking, Candidate refinement, Reranking, Text ranking, Document ranking, Item ranking  

## State of the Field

**Space of definitions.** Across the literature, the prevailing usage is reranking rather than generic ranking: papers most often describe the behavior as taking an initial retrieval set and reordering documents, passages, images, code snippets, websites, or other candidates by relevance to a query, usually to place the most relevant item first or improve the top-ranked results. Common task formulations assign relevance, satisfaction, or scalar scores and then reorder the list, while some setups ask for an ordered list of document IDs or use binary relevance judgments before reordering. A smaller line of work uses ranking more broadly for ordering candidate outputs from best to worst based on quality criteria, for arranging items or map regions by queried values, or for selecting the best generation from a candidate set.

**Variants.** Variants span document, passage, text, item, image, code, website, and candidate-entity reranking, along with listwise reranking and candidate refinement. Most remain query-relevance tasks after a first retrieval stage, though some specialize by setting, such as zero-shot reranking without task-specific fine-tuning, multimodal reranking for multimodal queries, financial document reranking, person-retrieval re-ranking after query refinement, and map-region ranking by legend values. Related work also connects ranking to question answering and information extraction by formulating reranking as QA or IE tasks, and one paper claims a causal relationship from ranking to cross-modal retrieval, reporting that zero-shot rerankers can further boost retrieval accuracy in multimodal tasks.

**Space of elicitation and scores.** Papers link ranking to 5 measurement instruments, all through measured_by relations: BEIR, CodeSearchNet, HELMET, MS MARCO, and MTEB. These are benchmark or dataset evaluations in retrieval and reranking settings: BEIR is used to evaluate a re-ranker, CodeSearchNet is a text-to-code retrieval benchmark whose top results are passed to a reranker, HELMET includes passage re-ranking among its task types, MS MARCO is used for reranking retrieved passages, and MTEB includes reranking alongside retrieval and related tasks. Within these evaluations, quoted passages also mention metrics such as MAP and MRR@100.

**What it is taken as evidence of.** The linked evidence does not converge on a single construct that ranking is taken to reflect. The linked constructs are generative ability and natural language understanding, and both are described only as related to ranking. One paper relates ranking to generative ability by saying reranking via generative capabilities lets a model improve on its embedding performance on most retrieval datasets, while another relates passage reranking to natural language understanding by describing it as harnessing LLM language understanding capabilities; in both cases, the recorded link is related rather than measured_by or causes.

## Sources

**Ranking** (3 papers: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf), [Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction](https://aclanthology.org/2025.emnlp-main.569.pdf), [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf))
> Ranking a list of items according to their relevance to a query, one of the five task types included in Shopping MMLU.

**Reranking** (5 papers: [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf), [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf), [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf), [A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](https://aclanthology.org/2025.acl-long.241.pdf), [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf))
> The process of re-evaluating and re-ordering an initial set of retrieved candidates to improve the precision of the top-ranked results.

**Image reranking** (1 paper: [INQUIRE: A Natural World Text-to-Image Retrieval Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4ad9c75f0d60ed75700f020adb3f705-Paper-Datasets_and_Benchmarks_Track.pdf))
> The process of re-ordering an initial set of retrieved images using a more sophisticated model to improve the final ranking's relevance to a query.

**Code reranking** (1 paper: [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf))
> The process of re-ordering an initial list of retrieved code snippets to improve the relevance of the final ranking.

**Website reranking** (1 paper: [MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf))
> Selecting the most informative website from retrieved search results for downstream answer extraction.

**Document reranking** (4 papers: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf), [FinMTEB: Finance Massive Text Embedding Benchmark](https://aclanthology.org/2025.emnlp-main.179.pdf), [Gumbel Reranking: Differentiable End-to-End Reranker Optimization](https://aclanthology.org/2025.acl-long.354.pdf), [RankCoT: Refining Knowledge for Retrieval-Augmented Generation through Ranking Chain-of-Thoughts](https://aclanthology.org/2025.acl-long.629.pdf))
> Ranking retrieved documents so that the most relevant document is placed first.

**Zero-shot reranking** (1 paper: [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf))
> The observable behavior of performing a reranking task using a model that has not been specifically fine-tuned for that task, relying instead on its pre-trained capabilities activated through prompting.

**Zero-shot re-ranking** (1 paper: [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf))
> Ranking a set of retrieved documents by their relevance to a query without task-specific fine-tuning.

**Passage re-ranking** (2 papers: [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf), [Query-Focused Retrieval Heads Improve Long-Context Reasoning and Re-ranking](https://aclanthology.org/2025.emnlp-main.1214.pdf))
> Ranking a set of retrieved passages by relevance to a query and outputting an ordered list of document IDs.

**Document re-ranking** (1 paper: [REALM: Recursive Relevance Modeling for LLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1218.pdf))
> The process of reordering a list of candidate documents based on their estimated relevance to a query, typically following an initial retrieval stage.

**Listwise reranking** (1 paper: [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.125.pdf))
> The model reorders a list of passages by considering their relative positions and relevance simultaneously, producing a full ranking rather than pairwise or pointwise scores.

**Passage reranking** (1 paper: [Multi-view-guided Passage Reranking with Large Language Models](https://aclanthology.org/2025.emnlp-main.1459.pdf))
> The task of assigning fine-grained relevance scores to a list of candidate passages for a given query to produce a re-ordered, more relevant list.

**Re-ranking** (1 paper: [Chat-Driven Text Generation and Interaction for Person Retrieval](https://aclanthology.org/2025.emnlp-main.266.pdf))
> The process of re-ordering an initial list of retrieved candidates based on additional information or a refined query to improve the final ranking.

**Information reranking** (1 paper: [LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1041.pdf))
> Reordering a list of retrieved documents based on their relevance to a query, particularly in scenarios requiring reasoning beyond surface-level matching.

**Candidate re-ranking** (1 paper: [MedLinkDE – MedDRA Entity Linking for German with Guided Chain of Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1609.pdf))
> The process of reordering an initial list of candidate entities to place the most accurate or relevant entity at the top.

**Candidate refinement** (1 paper: [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf))
> The process of filtering and prioritizing a list of potential attribute matches to create a smaller, more relevant set for final evaluation.

**Text ranking** (1 paper: [The Ranking Blind Spot: Decision Hijacking in LLM-based Text Ranking](https://aclanthology.org/2025.emnlp-main.1116.pdf))
> The observable behavior of ordering documents or passages by relevance to a given query, as performed by LLMs in information retrieval settings.

**Document ranking** (1 paper: [Multi-Conditional Ranking with Large Language Models](https://aclanthology.org/2025.naacl-long.146.pdf))
> The task of ordering a large collection of documents in a monotonic order of relevance based on a single query.

**Item ranking** (1 paper: [Multi-Conditional Ranking with Large Language Models](https://aclanthology.org/2025.naacl-long.146.pdf))
> The observable action of arranging a given set of items into a specific order based on one or more instructions.

## Relationships

### Ranking →
- **Cross-modal retrieval** (behavioral indicator): *causes*, 1 paper
  > We find that MLLMs can be used as zero-shot rerankers to further boost retrieval accuracy in challenging tasks that require the understanding of multimodal queries, such as ... composed image retrieval. (Section 6)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **MTEB** (measurement instrument): *measured_by*, 1 paper
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **CodeSearchNet** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we employ the CodeSearchNet and AdvTest text-to-code retrieval benchmarks... the top 100 results from our code retriever are passed to the reranker, with evaluation conducted using MRR@100.
  - [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf)
- **MS MARCO** (measurement instrument): *measured_by*, 1 paper
  > Re-ranking retrieved passages based on their relevance to the query is an important application of LCLMs (Sun et al., 2023). ... We use the MS MARCO dataset (Bajaj et al., 2018)
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **HELMET** (measurement instrument): *measured_by*, 1 paper
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **BEIR** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate QRRETRIEVER as a re-ranker on the standard BEIR benchmark (Thakur et al., 2021). (Section 1)
  - [Query-Focused Retrieval Heads Improve Long-Context Reasoning and Re-ranking](https://aclanthology.org/2025.emnlp-main.1214.pdf)

### Associated with
- **Generative ability** (construct), 1 paper
  > We ﬁnd that reranking via the generative capabilities of GRITLM 7B allows it to improve on its embedding performance on most retrieval datasets. (Section 4)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > To leverage the instruction following abilities in modern LLMs, we formulate the re-ranking task into either question answering (QA) or information extraction (IE) tasks, which are more commonly seen by LLMs. (Section 3.1)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Information extraction** (behavioral indicator), 1 paper
  > To leverage the instruction following abilities in modern LLMs, we formulate the re-ranking task into either question answering (QA) or information extraction (IE) tasks, which are more commonly seen by LLMs. (Section 3.1)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Natural language understanding** (construct), 1 paper
  > Passage reranking aims to assign fine-grained relevance scores to candidate passages – typically retrieved by a first-stage retriever (Robertson et al., 1994; Karpukhin et al., 2020) – by harnessing the language understanding capabilities of large language models (LLMs) (Section 1).
  - [Multi-view-guided Passage Reranking with Large Language Models](https://aclanthology.org/2025.emnlp-main.1459.pdf)
