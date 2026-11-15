# WikiTQ
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** WikiTableQuestion, WikiTableQuestions, WTQ  

## State of the Field

**What it is.** Most papers describe WikiTQ, also written as WikiTableQuestions or WTQ, as a benchmark or dataset of Wikipedia, sometimes semi-structured or HTML, tables paired with natural-language questions for table-based question answering. The prevailing description emphasizes complex operations such as comparison, aggregation, and arithmetic, while some papers further frame it as short-form or short text span answering; one paper describes about 2100 HTML tables and about 22,033 questions, and another refers to a standard test set with 4,344 table-question pairs. A smaller line of work adapts it into training formats for table-language interleaved learning or column-embedding training, and one study uses a filtered hybrid version requiring semantic inference.

**What it is claimed to measure.** Papers link WikiTQ to one behavioral indicator, Table question answering, and one construct, Table reasoning. The prevailing usage is to measure Table question answering, with descriptions such as table QA, table-based question answering, or short-form QA over semi-structured tables. A smaller group of papers uses it to measure Table reasoning, describing it as a benchmark for table-based reasoning or table reasoning. The claims are concentrated rather than spread across many targets, because papers connect it only to those two linked concepts.

**Space of uses.** Across papers, the dominant use is as one benchmark in multi-dataset evaluation suites. Papers often place it alongside FeTaQA, TabFact, HiTab, WikiSQL, and TableBench, and describe it as commonly used, mainstream, or classic; some also use it for held-in or in-domain evaluation. A smaller line of work repurposes it for training, for example by incorporating it into table-language interleaved data or adapting it for column-embedding training.

## Sources

**WikiTQ** (7 papers: [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf), [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf), [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf), [Weaver: Interweaving SQL and LLM for Table Reasoning](https://aclanthology.org/2025.emnlp-main.1436.pdf))
> WikiTableQuestions, a benchmark of Wikipedia tables and natural-language questions requiring table reasoning such as comparison, aggregation, and arithmetic.

**WikiTableQuestion** (2 papers: [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf), [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.710.pdf))
> A table-question answering dataset adapted here into training formats for table-language interleaved learning.

**WikiTableQuestions** (4 papers: [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf), [TALON: A Multi-Agent Framework for Long-Table Exploration and Question Answering](https://aclanthology.org/2025.emnlp-main.1393.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf))
> A benchmark dataset for complex Table Question Answering tasks that require operations like aggregation, comparison, and arithmetic calculations.

**WTQ** (2 papers: [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf), [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf))
> A dataset for flat table question answering, sourced from Wikipedia, used as a held-in training and evaluation set.

## Relationships

### → WikiTQ
- **Table question answering** (behavioral indicator): *measured_by*, 8 papers
  > CABINET establishes new SoTA on three challenging table QA datasets (WikiTQ, FeTaQA and WikiSQL) significantly outperforming various strong baselines (§ 4.1). (Section 1)
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1549.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **Table reasoning** (construct): *measured_by*, 3 papers
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
