# Table question answering
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Table-based question answering, Multi-table question answering, Tabular question answering, Free-form table QA, Short-form table QA  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage is answering a natural language question from table content and producing a natural language answer. Most descriptions ground the answer in a given table or in one or more provided tables, while smaller lines extend the task to multiple tables that must be retrieved and synthesized, or to mixed tabular-text data. Papers vary in the expected output: some emphasize concise, brief, or precise answers, others stress correct, accurate, or coherent answers, and one variant allows open-ended paragraph-length responses. Several definitions also note that the questions can require interpreting numerical or textual information, extracting and comparing table entries, or providing an arithmetic expression.

**Variants.** Papers use several names for variants. One paper explicitly distinguishes short-form table QA, with brief precise answers often involving extraction or aggregation of specific cell values, from free-form table QA, with open-ended answers grounded in tabular information. Other definitions introduce multi-table and multi-hop question answering, mixed tabular-text question answering in a financial conversational setting, and question answering over complex structures such as hierarchical or nested tables or over table images. Another formulation allows the table to be updated with new entries and paired with extra natural-language context or comparisons.

**Space of elicitation and scores.** Papers link this behavior to 8 measurement instruments. The most commonly linked are WikiTQ and FeTaQA, followed by TabFact, BIG-bench, and HiTab, with 3 other instruments linked less often. These instruments are described as benchmark datasets, benchmarks, or suites that evaluate table-grounded answers in different formats, including complex question answering over semi-structured Wikipedia tables in WikiTQ, free-form synthesis from multiple table sections in FeTaQA, yes or no verification from table content in TabFact, attribute questions from a given table in BIG-bench, and hierarchical TQA in HiTab.

**What it is taken as evidence of.** Papers link it to 2 constructs, and both links are recorded as related. The prevailing connection is that table question answering is related to table reasoning, where it is named as one of the table understanding or tabular reasoning tasks, while a smaller line reports that semantic reasoning is related to table question answering for tasks involving complex semantic reasoning and free-form responses. One paper also relates 2 other behaviors, question decomposition and self-verification, to table question answering as phases around sub-question TableQA reasoning and answer verification.

## Sources

**Table-based question answering** (2 papers: [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf))
> The observable task of generating a concise, natural language answer to a question using information found within one or more provided tables.

**Multi-table question answering** (1 paper: [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf))
> The task of generating a correct answer to a question by retrieving and synthesizing information from multiple provided tables.

**Table question answering** (7 papers: [LiveXiv - A Multi-Modal live benchmark based on Arxiv papers content](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa1373fe55b223c2dfe1fd29a277d7-Paper-Conference.pdf), [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf), [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf), [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf), [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf), [Compositional Condition Question Answering in Tabular Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25o/jiang25o.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf))
> Answering questions that require interpreting table content and associated numerical or textual information.

**Tabular question answering** (3 papers: [Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ffd05ca3cf3985f4572af015b4cfc1e-Paper-Conference.pdf), [RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1549.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf))
> Answering questions grounded in tabular or mixed tabular-text data, including cases requiring arithmetic or span extraction.

**Free-form table QA** (1 paper: [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf))
> Generating open-ended, paragraph-length answers grounded in tabular data, requiring synthesis and natural language generation.

**Short-form table QA** (1 paper: [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf))
> Answering questions with brief, precise answers based on information in a table, often requiring extraction and aggregation of specific cell values.

## Relationships

### Table question answering →
- **WikiTQ** (measurement instrument): *measured_by*, 8 papers
  > CABINET establishes new SoTA on three challenging table QA datasets (WikiTQ, FeTaQA and WikiSQL) significantly outperforming various strong baselines (§ 4.1). (Section 1)
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1549.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **FeTaQA** (measurement instrument): *measured_by*, 6 papers
  > CABINET establishes new SoTA on three challenging table QA datasets (WikiTQ, FeTaQA and WikiSQL) significantly outperforming various strong baselines (§ 4.1). (Section 1)
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf)
- **TabFact** (measurement instrument): *measured_by*, 3 papers
  > Existing TableQA benchmarks such as TabFact [2] and WikiTableQA [12] feature small web tables that fall within the context limits of most LMs (Section 4.1)
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)
  - [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **WikiSQL** (measurement instrument): *measured_by*, 1 paper
  > CABINET establishes new SoTA on three challenging table QA datasets (WikiTQ, FeTaQA and WikiSQL) significantly outperforming various strong baselines (§ 4.1). (Section 1)
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > Three reasoning tasks directly obtained from the BIG-Bench suite [50]: ... Penguins—where the task is to answer questions about penguins' attributes based on a given table
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > To address these limitations, we introduce TableEval, a new benchmark designed to evaluate LLMs on realistic TableQA tasks. (Abstract)
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)
- **HiTab** (measurement instrument): *measured_by*, 1 paper
  > Task Category: Table Question Answering (TQA), Task Name: Hierarchical TQA, Dataset: HiTab (2022) (Table 2)
  - [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf)
- **TabMWP** (measurement instrument): *measured_by*, 1 paper
  > "Lastly, we also test on a popular tabular question-answering dataset, TabMWP (Lu et al., 2023), that requires LLMs to use reasoning skills over tabular contexts."
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)

### Associated with
- **Table reasoning** (construct), 2 papers
  > Table-based reasoning with large language models (LLMs) is a promising direction to tackle many table understanding tasks, such as table-based question answering and fact veriﬁcation. (ABSTRACT)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Question decomposition** (behavioral indicator), 1 paper
  > Most LLM-based TableQA methods can be divided into three phases: question decomposition (Lewkowycz et al., 2022; Liu et al., 2022; Fu et al., 2022; Pasupat & Liang, 2015), sub-question TableQA reasoning and answer verification (Madaan et al., 2024; Ni et al., 2023).
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Self-verification** (behavioral indicator), 1 paper
  > Most LLM-based TableQA methods can be divided into three phases: question decomposition (Lewkowycz et al., 2022; Liu et al., 2022; Fu et al., 2022; Pasupat & Liang, 2015), sub-question TableQA reasoning and answer verification (Madaan et al., 2024; Ni et al., 2023).
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Semantic reasoning** (construct), 1 paper
  > We introduce Weaver , a novel methodology integrating SQL and LLM specifically designed for Table QA tasks involving complex semantic reasoning and free-form responses. (Section 2.1)
  - [Weaver: Interweaving SQL and LLM for Table Reasoning](https://aclanthology.org/2025.emnlp-main.1436.pdf)
