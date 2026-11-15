# WebQSP
**Type:** Measurement instrument  
**Supporting papers:** 23  
**Also known as:** WebQuestionsSP  

## State of the Field

**What it is.** Papers most commonly describe WebQSP as a benchmark dataset for knowledge base or knowledge graph question answering over Freebase or structured knowledge bases. Several definitions add that it is derived from WebQuestions and pairs natural language questions with SPARQL queries; some describe it as containing both single-hop and multi-hop questions, while others frame it more specifically as a multi-hop dataset or as a benchmark used to test I.I.D. generalization. A smaller number of descriptions mention questions from the Google Suggest API, answers from Freebase, or reasoning over a subset of Freebase.

**What it is claimed to measure.** Papers use WebQSP to measure two behavioral indicators and two constructs. The prevailing claim is that it measures Knowledge graph question answering, while a smaller line of work uses it for Multi-hop question answering. On the construct side, papers report it as measuring Multi-hop reasoning most often and Reasoning more generally less often, so the linked claims cluster around KGQA and reasoning-oriented targets.

**Space of uses.** In use, papers usually treat WebQSP as one of several benchmark KGQA datasets, most often alongside CWQ and often with GrailQA. Some also pair it with other QA benchmarks, and one paper includes it as part of the GraphQA benchmark. The surrounding descriptions position it as an in-domain, real-world, or additional dataset for comparative evaluation of reasoning performance.

## Sources

**WebQSP** (8 papers: [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf), [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf), [KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph](https://aclanthology.org/2025.acl-long.468.pdf), [KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25d/luo25d.pdf), [CompKBQA: Component-wise Task Decomposition for Knowledge Base Question Answering](https://aclanthology.org/2025.emnlp-main.16.pdf), [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf), [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf))
> WebQuestionsSP, a KBQA benchmark used to evaluate question answering over structured knowledge bases.

**WebQuestionsSP** (1 paper: [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf))
> WebQuestionsSP (WebQSP) is a benchmark dataset for knowledge base question answering derived from WebQuestions, with questions annotated with their corresponding SPARQL queries.

## Relationships

### → WebQSP
- **Knowledge graph question answering** (behavioral indicator): *measured_by*, 8 papers
  > To demonstrate the effectiveness of PoG on complex reasoning over knowledge graphs, we adopt three representative multi-hop KGQA datasets: CWQ, WebQSP, and GrailQA. (Section 4.1.1)
  - [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf)
  - [Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning](https://aclanthology.org/2025.acl-long.1202.pdf)
  - [Ontology-Guided Reverse Thinking Makes Large Language Models Stronger on Knowledge Graph Question Answering](https://aclanthology.org/2025.acl-long.741.pdf)
  - [Digest the Knowledge: Large Language Models empowered Message Passing for Knowledge Graph Question Answering](https://aclanthology.org/2025.acl-long.750.pdf)
  - [Enrich-on-Graph: Query-Graph Alignment for Complex Reasoning with LLM Enriching](https://aclanthology.org/2025.emnlp-main.390.pdf)
  - [RJE: A Retrieval-Judgment-Exploration Framework for Efficient Knowledge Graph Question Answering with LLMs](https://aclanthology.org/2025.emnlp-main.873.pdf)
  - [SAFE: Schema-Driven Approximate Distance Join for Efficient Knowledge Graph Querying](https://aclanthology.org/2025.emnlp-main.883.pdf)
  - [BYOKG-RAG: Multi-Strategy Graph Retrieval for Knowledge Graph Question Answering](https://aclanthology.org/2025.emnlp-main.1417.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 2 papers
  > We adopt two prominent and challenging KGQA benchmarks that necessitate multi-hop reasoning – WebQSP (Yih et al., 2016) and CWQ (Talmor & Berant, 2018).
  - [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf)
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 2 papers
  > We evaluated our method on different knowledge-intensive reasoning benchmark datasets, including two multi-hop KBQA datasets WebQSP (Yih et al., 2016) and QALD10-en (Usbeck et al., 2023) (Section 4.1)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We evaluate the reasoning ability of RoG on two benchmark KGQA datasets: WebQuestionSP (WebQSP) (Yih et al., 2016) and Complex WebQuestions (CWQ) (Talmor & Berant, 2018) (Section 5.1)
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
