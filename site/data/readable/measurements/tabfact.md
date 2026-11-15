# TabFact
**Type:** Measurement instrument  
**Supporting papers:** 12  

## State of the Field

**What it is.** Across the surveyed work, TabFact is most commonly described as a benchmark or dataset for table-based fact verification over Wikipedia tables, pairing tables with textual statements and asking whether each statement is supported, entailed or true, or instead refuted or false, by the table. Several papers also call it a large-scale dataset, and some describe a specific evaluation subset, the test-small set with 2,024 statements or test samples from 298 tables. A smaller line of work presents it as a public TableQA resource, describing pairs of content-related question and answer or yes or no answers for TQA evaluation.

**What it is claimed to measure.** Papers use TabFact to measure 2 behavioral indicators and 1 construct. The prevailing measurement claim is fact checking, with papers explicitly using it for fact verification or TFV; a smaller but recurring usage treats it as measuring table question answering, including TableQA settings where the answer is yes or no. At the construct level, it is also reported as measuring table reasoning, so papers connect it both to specific behaviors and to a broader table reasoning construct.

**Space of uses.** Papers commonly use TabFact alongside WikiTQ, and more occasionally with FeTaQA, FinQA, HiTab, and TabMWP. It is usually positioned as one component of broader evaluations across multiple table tasks, while some work uses the test-small split specifically, one paper uses it as held-in training and evaluation data, and another generates synthetic larger-table variants from TabFact, ranging from 50 × 50 to 1000 × 1000, for scalability evaluation.

**Concerns raised.** One paper notes that, as a TableQA benchmark, TabFact features small web tables that fall within the context limits of most LMs. That paper also creates synthetic data from TabFact with larger table sizes for a scalability test.

## Sources

**TabFact** (10 papers: [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning](https://aclanthology.org/2025.acl-long.853.pdf), [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf), [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf), [Weaver: Interweaving SQL and LLM for Table Reasoning](https://aclanthology.org/2025.emnlp-main.1436.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf), [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf), [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf))
> A benchmark dataset for table-based fact verification, containing statements paired with Wikipedia tables, where the task is to determine if the statement is supported by the table.

## Relationships

### → TabFact
- **Fact checking** (behavioral indicator): *measured_by*, 4 papers
  > We evaluate our method on three datasets covering fact verification, short-form, and long-form question-answering tasks... (a) TabFact (Chen et al., 2019): A fact verification benchmark utilizing Wikipedia tables. (Section 3)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
  - [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf)
- **Table question answering** (behavioral indicator): *measured_by*, 3 papers
  > Existing TableQA benchmarks such as TabFact [2] and WikiTableQA [12] feature small web tables that fall within the context limits of most LMs (Section 4.1)
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)
  - [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Table reasoning** (construct): *measured_by*, 2 papers
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
