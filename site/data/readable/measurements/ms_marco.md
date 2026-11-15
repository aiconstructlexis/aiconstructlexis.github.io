# MS MARCO
**Type:** Measurement instrument  
**Supporting papers:** 22  
**Also known as:** MSMARCO, MSMarco, MARCO QA, MS MARCO QA, MS-Marco  

## State of the Field

**What it is.** The prevailing usage treats MS MARCO as a large-scale retrieval, question answering, or machine reading comprehension benchmark built from queries or questions and passages, sometimes with ground-truth answers. Several papers narrow it to particular components, such as only the question-and-answer pairs or the passage set, and one description says the public dev split has 101.09k examples, each with a simple question and 10 relevant passages. Variants and subsets also appear, including MARCO QA, msmarco-passages, MS MARCO Dev, and the TREC Deep Learning subsets DL19 and DL20, and one use frames the task as answering real-user Bing queries from 10 retrieved passages.

**What it is claimed to measure.** Claims about what it measures are spread across several targets rather than centered on one: papers link MS MARCO to three behavioral indicators and two constructs. The linked behavioral indicators are Open-domain question answering, Information retrieval, and Ranking, and the linked constructs are Retrieval effectiveness and Robustness. In the recorded relationships, papers use it to measure open-domain question answering in simple open QA and MARCO QA settings, to measure Information retrieval and Robustness with a subset in non-Wikipedia scenarios, and to measure Ranking and Retrieval effectiveness in retrieval benchmark evaluations.

**Space of uses.** In practice, papers use MS MARCO both for training and for evaluation: one line fine-tunes retrievers with only its question-and-answer pairs, others annotate utility on the passage set or study rerankers on passage-ranking versions of the dataset, and others evaluate document retrieval, passage ranking, or in-domain RAG with it. It is also used alongside BEIR, TREC DL19, DL20, WikiText-V2, and NQ, with other QA datasets appearing in the same evaluation suites. Papers variously position it as an in-domain retrieval benchmark, an out-of-domain dataset for passage ranking, a subset for non-Wikipedia retrieval experiments, and a source of examples for search-and-retrieve hallucination studies.

## Sources

**MS MARCO** (6 papers: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf), [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [Utility-Focused LLM Annotation for Retrieval and Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.88.pdf), [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf))
> A question answering dataset used for retriever fine-tuning, specifically the question-and-answer pairs.

**MSMARCO** (1 paper: [PICASO: Permutation-Invariant Context Composition with State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0730b81dbc16cce7e85b519cb7fe5a8d-Paper-Conference.pdf))
> The Microsoft Machine Reading Comprehension (MSMARCO) dataset, a large-scale collection of queries and passages used for evaluating reading comprehension and information retrieval tasks.

**MSMarco** (1 paper: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf))
> A passage-ranking benchmark used to evaluate reranker judges in a retrieval setting.

**MARCO QA** (1 paper: [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf))
> The MS MARCO Question Answering (MARCO QA) dataset, a large-scale benchmark for reading comprehension and question answering.

**MS MARCO QA** (1 paper: [Utility-Focused LLM Annotation for Retrieval and Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.88.pdf))
> A dataset containing ground-truth answers for queries in the MS MARCO retrieval set, used for evaluating in-domain RAG performance.

**MS-Marco** (1 paper: [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf))
> A large-scale machine reading comprehension dataset containing user queries and relevant text passages, used for evaluating document retrieval.

## Relationships

### → MS MARCO
- **Open-domain question answering** (behavioral indicator): *measured_by*, 2 papers
  > The open-domain QA tasks consist of NQ (Kwiatkowski et al., 2019), MARCO QA (Bajaj et al., 2016) and TriviaQA (Joshi et al., 2017), which require models to retrieve factual knowledge to help LLMs answer the given question.
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the model’s robustness in non-Wikipedia scenarios where high-quality text and titles are not available, we conduct experiments on a subset of MS MARCO [3]
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > “To evaluate the model’s robustness in non-Wikipedia scenarios where high-quality text and titles are not available, we conduct experiments on a subset of MS MARCO”
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Ranking** (behavioral indicator): *measured_by*, 1 paper
  > Re-ranking retrieved passages based on their relevance to the query is an important application of LCLMs (Sun et al., 2023). ... We use the MS MARCO dataset (Bajaj et al., 2018)
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Retrieval effectiveness** (construct): *measured_by*, 1 paper
  > We evaluate retrieval effectiveness using two retrieval benchmarks: MS MARCO (Bajaj et al., 2016) and BEIR (Thakur et al., 2021).
  - [ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance](https://aclanthology.org/2025.emnlp-main.963.pdf)
