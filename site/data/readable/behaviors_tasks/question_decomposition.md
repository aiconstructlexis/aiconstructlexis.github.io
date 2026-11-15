# Question decomposition
**Type:** Behavioral indicator  
**Supporting papers:** 49  
**Also known as:** Subquestion decomposition, Sub-question generation, Query decomposition, Query graph construction, Subproblem decomposition, Intermediate question generation, Subquestion generation, Sub-query generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as breaking a complex question or query into simpler intermediate units, most often a sequence of sub-questions that can be answered step by step before reaching a final answer. Several definitions make the target output answerable subquestions explicit, sometimes with corresponding sub-answers, and one multi-hop formulation says the model generates intermediate questions and answers until arriving at the final answer. A smaller line of work uses query- or subproblem-centered wording instead of question-centered wording, and one paper reframes decomposition as analyzing a question into structural tokens and replaceable entity placeholders to form a reusable template for similar questions.

**Variants.** Common labels are question decomposition, subquestion decomposition, query decomposition, sub-question generation, and query graph construction, with several other less common labels. The main variants differ in representation: some papers use plain sequences of subquestions, some generate subquestion-answer pairs, and some organize sub-queries into a directed acyclic graph that represents dependencies or a reasoning plan. The settings mentioned include multi-hop questions, retrieval-augmented decomposition steps, and multi-hop or medical reasoning.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead elicit the behavior directly in generation, for example by prompting models to decompose a question into subquestions, asking a generator to produce multiple sub-questions and corresponding sub-answers, or having a query graph builder decompose an input query into sub-queries and construct a directed acyclic graph. No separate scoring instrument is linked in the papers.

**What it is taken as evidence of.** Papers connect it to 3 constructs, but they do not converge on a single construct it reflects. The linked constructs are Chain-of-thought reasoning, Knowledge reasoning, and Reasoning: some papers report a related link to Reasoning, one reports that Chain-of-thought reasoning is related to Question decomposition, and another claims a causal relationship from Question decomposition to Knowledge reasoning, describing decomposition as used "for more accurate answer inference."

## Sources

**Question decomposition** (3 papers: [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf), [T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.185.pdf), [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf))
> Breaking a complex question into a sequence of simpler sub-questions.

**Subquestion decomposition** (1 paper: [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf))
> Breaking down a complex question into simpler, answerable subquestions to guide stepwise reasoning.

**Sub-question generation** (1 paper: [Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.354.pdf))
> The process of decomposing a main question into multiple sub-questions as intermediate reasoning steps.

**Query decomposition** (2 papers: [Single LLM, Multiple Roles: A Unified Retrieval-Augmented Generation Framework Using Role-Specific Token Optimization](https://aclanthology.org/2025.emnlp-main.243.pdf), [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf))
> The process of breaking down a complex user query into a set of simpler, more manageable sub-queries.

**Query graph construction** (1 paper: [Single LLM, Multiple Roles: A Unified Retrieval-Augmented Generation Framework Using Role-Specific Token Optimization](https://aclanthology.org/2025.emnlp-main.243.pdf))
> The task of decomposing a query into sub-queries and organizing them into a directed acyclic graph representing dependencies and a reasoning plan.

**Subproblem decomposition** (1 paper: [PathwiseRAG: Multi-Dimensional Exploration and Integration Framework](https://aclanthology.org/2025.emnlp-main.1167.pdf))
> Breaking down a complex query into smaller, logically structured subproblems that can be processed independently or in sequence.

**Intermediate question generation** (1 paper: [Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://proceedings.iclr.cc/paper_files/paper/2024/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf))
> Producing sub-questions as part of a decomposition strategy for answering complex, multi-hop questions.

**Subquestion generation** (1 paper: [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf))
> The behavior of decomposing a complex question into a series of simpler, intermediate questions to be answered sequentially.

**Sub-query generation** (1 paper: [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf))
> Producing intermediate questions that decompose a complex query into smaller, answerable components during a reasoning process.

## Relationships

### Question decomposition →
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > QD provides noticeable improvements over MTR on multi-table retrieval tasks, for instance, in Top-2 retrieval, precision is improved from 65.3 to 72.3 and recall is improved from 62.3 to 64.7 in the 2-table subset. (Section 4.2)
  - [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf)
- **Knowledge reasoning** (construct): *causes*, 1 paper
  > since questions in knowledge-intensive reasoning tasks can often be a complex composite problems that are challenging to solve directly, a structured knowledge utilizer is used to perform question decomposition... for more accurate answer inference.
  - [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf)
- **Multi-hop question answering** (behavioral indicator): *causes*, 1 paper
  > Question decomposition has been found to help large language models’ (LLMs) performance on complex question answering (QA) by breaking these questions into simpler sub-questions for answering.
  - [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf)
- **Knowledge retrieval** (behavioral indicator): *causes*, 1 paper
  > This action FQD aims to break down the current question into multiple sub-queries to facilitate the retrieval of knowledge across various aspects (Section 3.2.2)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)

### Associated with
- **Data analysis** (behavioral indicator), 1 paper
  > most existing table QA datasets focus on obtaining specific information, our data analysis queries can be complex and requires query decomposition and reasoning. (Section 6)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reasoning** (construct), 1 paper
  > WebPlanner first decomposes the user question into sequential or parallel search tasks via reasoning on the graph and determines the next step based on the search feedback (Sec. 2.1).
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **Table question answering** (behavioral indicator), 1 paper
  > Most LLM-based TableQA methods can be divided into three phases: question decomposition (Lewkowycz et al., 2022; Liu et al., 2022; Fu et al., 2022; Pasupat & Liang, 2015), sub-question TableQA reasoning and answer verification (Madaan et al., 2024; Ni et al., 2023).
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > multi-step reasoning methods (Uehara et al., 2022; Wang et al., 2022b; Khan et al., 2023; Yao et al., 2023; Besta et al., 2024) have been proposed that decompose the main question into several sub-question-answer pairs (sub-QAs) and subsequently utilize them to derive the final answer. (Section 1)
  - [Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.354.pdf)
- **Text-to-SQL** (behavioral indicator), 1 paper
  > The Query Agent QAgent generates a SQL query qij and resulting tables Rij (qij(D) = Rij) to answer the subquestions using the database information and schema (Section 4.2)
  - [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf)
