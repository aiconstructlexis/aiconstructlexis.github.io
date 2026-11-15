# Table reasoning
**Type:** Construct  
**Supporting papers:** 17  
**Also known as:** Table-based reasoning, Table understanding, Visual table understanding, Column-level understanding, Table perception, Compositional condition understanding, Table structure understanding, Tabular reasoning  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats table reasoning as a latent ability to understand or comprehend structured tabular data and use it to answer natural language questions, prompts, or other complex queries. Closely related definitions describe it as querying, processing, connecting, and synthesizing table information, and some specify extraction, manipulation, or intermediate reasoning steps over the table. A smaller line of work narrows the scope to particular settings, such as open-domain, multi-table, visual, or complex-layout tables, so the main variation is between broad table understanding and more task- or format-specific versions.

**Space of facets.** Papers often use table reasoning, tabular reasoning, table understanding, and table-based reasoning for closely overlapping abilities. A smaller line of work splits the construct into more specific competencies, including multi-table reasoning and narrower abilities tied to column semantics, compositional conditions, and complex layouts. In visual settings, papers further decompose the space into perception and downstream querying or answering tasks.

**Space of measurement.** Operationalization is benchmark-centered: papers link table reasoning to 9 measurement instruments, most often WikiTQ, TabFact, BIG-Bench Hard, BIRD, and FEVEROUS. These are described as tabular benchmarks or task collections used to evaluate question answering, fact verification, open-domain table reasoning, large-table settings, and other tabular tasks, with several other named benchmarks also appearing. Papers also link the construct to 5 behavioral indicators spanning question answering, computation, extraction, structure recognition, and query translation, so the operationalizations mostly follow task-centered definitions while also reaching into structure-oriented behaviors.

**Links.** Among the non-measurement links, papers relate table reasoning to 6 constructs and 5 behavioral indicators, and all of these are recorded as related rather than causal or correlational links. Several papers relate it to table question answering and mathematical reasoning, and other papers relate it to logical reasoning, natural language understanding, and arithmetic computation. Papers also describe additional related reasoning styles and table-specific skills.

## Sources

**Table reasoning** (2 papers: [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf))
> The latent ability of a model to comprehend, query, and synthesize information from structured tabular data to address natural language prompts.

**Table-based reasoning** (1 paper: [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf))
> The capacity to solve questions or verification problems by extracting and manipulating information from tables through intermediate reasoning steps.

**Table understanding** (3 papers: [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf), [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf), [GRIT: Guided Relational Integration for Efficient Multi-Table Understanding](https://aclanthology.org/2025.emnlp-main.1118.pdf))
> The latent ability of a language model to comprehend and process information presented in a structured tabular format.

**Visual table understanding** (1 paper: [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf))
> The model's latent ability to comprehend the structure, content, and semantics of tables presented in a visual format, such as a document image.

**Column-level understanding** (1 paper: [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf))
> The ability to interpret the semantic meaning of table columns and their relationships, such as identifying primary and foreign keys.

**Table perception** (1 paper: [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf))
> The ability to visually recognize and represent table structures and contents from table images.

**Compositional condition understanding** (1 paper: [Compositional Condition Question Answering in Tabular Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25o/jiang25o.pdf))
> The latent ability to interpret and reason over multiple interdependent conditions in a question when retrieving or computing answers from tabular data.

**Table structure understanding** (1 paper: [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf))
> The latent ability of an LLM to interpret and reason over complex table layouts, including hierarchical, nested, and concise structures, beyond simple flat tables.

**Tabular reasoning** (4 papers: [DETQUS: Decomposition-Enhanced Transformers for QUery-focused Summarization](https://aclanthology.org/2025.naacl-long.138.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf))
> The latent ability to understand, connect, and synthesize information from structured tabular data to answer complex queries.

## Relationships

### Table reasoning →
- **WikiTQ** (measurement instrument): *measured_by*, 3 papers
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **TabFact** (measurement instrument): *measured_by*, 2 papers
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
- **FEVEROUS** (measurement instrument): *measured_by*, 1 paper
  > We adapted the dataset for open-domain table reasoning by filtering 323 examples from the validation set that rely solely on table data, using a corpus of 26,177 candidate tables from the FEVEROUS dataset.
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **FeTaQA** (measurement instrument): *measured_by*, 1 paper
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **HiTab** (measurement instrument): *measured_by*, 1 paper
  > ROT is evaluated on three widely used table reasoning datasets: WikiTableQuestions (Pasupat and Liang, 2015), HiTab (Cheng et al., 2022), and TableBench (Wu et al., 2024) (Section 3.1)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **TableBench** (measurement instrument): *measured_by*, 1 paper
  > ROT is evaluated on three widely used table reasoning datasets: WikiTableQuestions (Pasupat and Liang, 2015), HiTab (Cheng et al., 2022), and TableBench (Wu et al., 2024) (Section 3.1)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)
- **BIRD** (measurement instrument): *measured_by*, 1 paper
  > To verify the scalability of TableRAG for larger tables, we build two new benchmarks sourced from the real-world Arcade [26] and BIRD-SQL [7] datasets.
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)

### Associated with
- **Table question answering** (behavioral indicator), 2 papers
  > Table-based reasoning with large language models (LLMs) is a promising direction to tackle many table understanding tasks, such as table-based question answering and fact veriﬁcation. (ABSTRACT)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Mathematical reasoning** (construct), 2 papers
  > Secondly, table reasoning tasks often require numerical reasoning, data preparation, or key cell identification.
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Table structure recognition** (behavioral indicator), 1 paper
  > Visual Table Understanding (VTU) generally encompasses four subtasks: Table Detection (TD), which locates tables within document images; Table Structure Recognition (TSR), which parses the structure of tables in table-centric images; Table Querying (TQ), which recognizes the structure of a table from an entire image at a given location, a task that remains underexplored in the previous works; and Table Question Answering (TQA), which answers questions based on table contents. (Introduction)
  - [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf)
- **Logical reasoning** (construct), 1 paper
  > Tabular reasoning presents an inherently challenging problem, requiring logical, mathematical, and textual reasoning over unstructured queries and structured tables
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > Table reasoning presents distinct challenges compared to text-only tasks: it requires interpreting diverse cell contents, aligning data across the table, and performing multi-step reasoning with aggregation and numerical operations (Deng et al., 2024; Wu et al., 2025). (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Semantic understanding** (construct), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Information extraction** (behavioral indicator), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Arithmetic computation** (behavioral indicator), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Temporal reasoning** (construct), 1 paper
  > Third, we note a marked increase in arithmetic and temporal reasoning capabilities. The model becomes more adept at performing arithmetic calculations over table entries and reasoning over temporal sequences, both of which are crucial for table reasoning tasks. (Section 4.6)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Text-to-SQL** (behavioral indicator), 1 paper
  > To investigate this, we focus on NL2SQL, a pivotal task in table understanding where LLMs translate natural language queries into SQL, given a specific database (Section 1).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **Natural language understanding** (construct), 1 paper
  > Tabular reasoning involves interpreting natural language queries about tabular data, which presents a unique challenge of combining language understanding with structured data analysis.
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
