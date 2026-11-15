# Knowledge retrieval
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** External knowledge retrieval  

## State of the Field

**Space of definitions.** Most definitions treat this behavior as querying or accessing external sources and incorporating the retrieved information into reasoning or answer generation. A narrower line of work frames it as fetching relevant medical facts, entities, and reasoning chains from structured knowledge graphs, and one study specifies the process as two steps, 'query generation and execution'.

**Variants.** Papers use both 'external knowledge retrieval' and 'knowledge retrieval'. The recurring settings are multi-hop or compositional questions, where retrieval may be iterative, for example by concatenating outputs from previous rounds with sub-step questions, or implemented as retrieve-then-read external acting; some work also precedes it with question decomposition into multiple sub-queries to facilitate retrieval across aspects. Other variants focus on domain-specific sources, including medical knowledge graphs that retrieve chains between anchor entities and search directions through hypothesis outputs, heterogeneous sources such as Wikidata, Wikipedia, tables, and domain resources, and external geographic knowledge used as supplementary clues for multi-hop reasoning.

**Space of elicitation and scores.** Papers link this behavior to 7 instruments overall. The prevailing operationalization is benchmark or dataset based: it is measured by BoolQ, LongBench, MKQA, MMAU, and MMLU, with 2 other linked instruments, one appearing in a related rather than measured_by link; across these uses, papers describe them as knowledge retrieval tasks, representative datasets, or benchmarks, and MMAU is presented as evaluating multimodal reasoning and knowledge-retrieval capabilities.

**What it is taken as evidence of.** Across construct links, papers do not converge on a single construct target. They connect this behavior to 4 constructs: one paper claims a causal relationship from knowledge retrieval to cross-lingual generalization, stating that retrieval requirements hinder transferability, while other papers relate it to in-context learning, knowledge manipulation, and multi-hop reasoning, for example by naming knowledge retrieval as one of two approaches used to explain the in-context learning mechanism and as one of four knowledge manipulation tasks.

## Sources

**External knowledge retrieval** (2 papers: [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf), [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.331.pdf))
> Accessing and incorporating information from external sources (e.g., documents, knowledge bases) to support reasoning and answer generation.

**Knowledge retrieval** (2 papers: [HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf))
> Fetching relevant medical facts, entities, and reasoning chains from structured knowledge graphs based on user queries and generated hypotheses.

## Relationships

### Knowledge retrieval →
- **MMAU** (measurement instrument): *measured_by*, 1 paper
  > We introduce the Massive Multi-Task Audio Understanding and Reasoning Benchmark (MMAU), a novel benchmark designed to evaluate the expert-level multimodal reasoning and knowledge-retrieval capabilities of large audio-language models (LALMs). (Section 3.1)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > "This benchmark is the most important because it shows both long context generation performance and knowledge retrieval performance"
  - [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf)
- **MKQA** (measurement instrument): *measured_by*, 1 paper
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Multi-hop question answering** (behavioral indicator): *causes*, 1 paper
  > due to the requirement for external knowledge in complex multi-hop questions (Mavi et al., 2024; Minaee et al., 2024), retrieval-augmented reasoning methods show more significant improvement compared to closed-book methods. (Section 5.1.1)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We consider a variety of tasks that cover both idealized cases where we know the task mechanisms and open-ended ones where only partial or approximate mechanisms are identified. These tasks fall into three categories: (2) knowledge retrieval tasks, including RAVEL (Huang et al., 2024) and MMLU (Hendrycks et al., 2021), whose mechanisms are only partially understood
  - [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf)
- **Cross-lingual generalization** (construct): *causes*, 1 paper
  > the requirement for knowledge retrieval significantly hinders the model’s cross-lingual transferability when solving reasoning tasks. (Section 4.1)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **RAVEL** (measurement instrument): *measured_by*, 1 paper
  > (2) knowledge retrieval tasks, including RAVEL (Huang et al., 2024) and MMLU (Hendrycks et al., 2021)... (Section 5.1)
  - [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf)

### → Knowledge retrieval
- **Question decomposition** (behavioral indicator): *causes*, 1 paper
  > This action FQD aims to break down the current question into multiple sub-queries to facilitate the retrieval of knowledge across various aspects (Section 3.2.2)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Hallucinations pose a significant hurdle to the adoption of language models, especially in domains where reliable knowledge retrieval is paramount (Dahl et al., 2024). (Section 1)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Knowledge manipulation** (construct), 1 paper
  > This paper investigates four fundamental knowledge manipulation tasks: retrieval (e.g., “What is person A’s attribute X?”), classification (e.g., “Is A’s attribute X even or odd?”), comparison (e.g., “Is A greater than B in attribute X?”), and inverse search (e.g., “Which person’s attribute X equals T?”). (Section Abstract)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **In-context learning** (construct), 1 paper
  > Broadly speaking, current research identifies two main approaches to explain the ICL mechanism (Dong et al., 2024; Li et al., 2024): 1) Meta-learning, 2) Knowledge retrieval.
  - [Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models](https://aclanthology.org/2025.naacl-long.417.pdf)
- **TriviaQA** (measurement instrument), 1 paper
  > we use the question data from question-answering training data, such as TriviaQA [23] and Natural Questions [27, 29], to obtain the covariance matrices whose pattern corresponds to the knowledge retrieving ability of the LLM (Section 3.3).
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **Multi-hop reasoning** (construct), 1 paper
  > Since complex questions often involve external geographic knowledge, we then adaptively retrieve it as supplementary clues and conduct multi-hop reasoning based on it.
  - [Answering Complex Geographic Questions by Adaptive Reasoning with Visual Context and External Commonsense Knowledge](https://aclanthology.org/2025.acl-long.1239.pdf)
