# Multi-hop reasoning
**Type:** Construct  
**Supporting papers:** 112  
**Also known as:** Multihop reasoning, Two-hop reasoning, Associative reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats multi-hop reasoning as a latent ability to connect, integrate, or synthesize multiple pieces of evidence through sequential inference to answer a question or verify a claim. Most definitions agree on multiple steps and intermediate links, whether across documents and passages, tables and text, charts, rows in a table, or entity relations; one example describes extracting a marathon runner from raw text and linking that with a database to determine their place. A smaller line of work states the construct more procedurally, as producing a chain of logical inferences, decomposing questions into intermediate questions and answers, or iteratively retrieving evidence, and one paper narrows this further to two-hop reasoning as composing a→b and b→c into a→c.

**Space of facets.** Papers use both multi-hop reasoning and multihop reasoning for the same idea. The main distinctions are by hop count and connection type: one paper isolates two-hop reasoning as composing two factual associations, another labels associative reasoning as connecting disparate information through shared entities or concepts, and one chart benchmark says sequential reasoning evaluates multi-hop reasoning in a stepwise manner. Several papers also contrast it with single-hop or isolated-statement settings, describing connected reasoning over multiple documents, passages, triples, rows, or modalities rather than a single evidence item.

**Space of measurement.** Operationalization is dominated by benchmark datasets: papers link the construct to 19 measurement instruments, most commonly HotpotQA, MuSiQue, 2WikiMultiHopQA, StrategyQA, and CWQ. As operationalized, papers usually test whether models can combine multiple passages, documents, or hops to answer a question, sometimes with exact match or accuracy, and a smaller slice extends the same setup to knowledge-base, long-context, multimodal, table-text, temporal, and synthetic reasoning tasks. This largely mirrors the prevailing definitions, and papers additionally connect the construct to 5 behavioral indicators.

**Links.** No papers here claim a causal relationship. One paper reports that multi-hop reasoning correlates with Portability, noting that portability metrics decline as the number of hops increases, while several papers relate it to Implicit reasoning, including a formulation of implicit reasoning as solving multi-hop reasoning tasks in a single forward pass without chain of thought. Single papers also relate it to Sequential reasoning, Long-context understanding, and Fact checking, and other links place it in QA, retrieval, tool-use, and critique-based settings.

## Sources

**Multi-hop reasoning** (12 papers: [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf), [MultiChartQA: Benchmarking Vision-Language Models on Multi-Chart Problems](https://aclanthology.org/2025.naacl-long.566.pdf), [Hybrid Graphs for Table-and-Text based Question Answering using LLMs](https://aclanthology.org/2025.naacl-long.39.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf), [ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.193.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf), [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf))
> The latent ability of a model to connect and infer information across multiple pieces of evidence that are not directly linked, requiring sequential logical steps to arrive at an answer.

**Multihop reasoning** (3 papers: [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf), [SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf), [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf))
> The latent ability to trace and verify logical relationships across multiple entities and facts in a text, especially when indirect connections are required to detect inconsistencies.

**Two-hop reasoning** (1 paper: [Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25m/feng25m.pdf))
> The latent ability to compose two factual associations (a → b and b → c) to infer a distant relationship (a → c), where one fact is newly learned and the other is pre-existing.

**Associative reasoning** (1 paper: [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf))
> The latent ability of a model to connect disparate pieces of information through shared entities or concepts to answer complex, multi-hop queries.

## Relationships

### Multi-hop reasoning →
- **HotpotQA** (measurement instrument): *measured_by*, 13 papers
  > "HotpotQA [85] is a Wikipedia-based multi-hop QA dataset. It requires reasoning across multiple passages to find the answer."
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf)
  - [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf)
  - [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf)
  - [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf)
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
  - [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf)
  - [TreeRare: Syntax Tree-Guided Retrieval and Reasoning for Knowledge-Intensive Question Answering](https://aclanthology.org/2025.emnlp-main.947.pdf)
  - [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 11 papers
  > We experiment with MuSiQue (Trivedi et al., 2022), a hard multi-hop reasoning dataset created via composable pairs of single-hop questions... (Section 3.1)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf)
  - [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf)
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
  - [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf)
  - [TreeRare: Syntax Tree-Guided Retrieval and Reasoning for Knowledge-Intensive Question Answering](https://aclanthology.org/2025.emnlp-main.947.pdf)
  - [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 6 papers
  > When evaluated on multi-hop reasoning benchmarks, our approach achieves up to 95–100% accuracy on 2WikiMultiHopQA (Abstract).
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
  - [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf)
  - [TreeRare: Syntax Tree-Guided Retrieval and Reasoning for Knowledge-Intensive Question Answering](https://aclanthology.org/2025.emnlp-main.947.pdf)
  - [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf)
  - [SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA](https://aclanthology.org/2025.naacl-long.300.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 5 papers
  > Multi-Hop Reasoning: We experiment with MuSiQue (Trivedi et al., 2022), a hard multi-hop reasoning dataset created via composable pairs of single-hop questions, and StrategyQA (Geva et al., 2021) with open-domain questions that demand some strategy to solve. (Section 3.1)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
  - [Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://aclanthology.org/2025.emnlp-main.150.pdf)
  - [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [Forward Knows Efficient Backward Path: Saliency-Guided Memory-Efficient Fine-tuning of Large Language Models](https://aclanthology.org/2025.acl-long.459.pdf)
- **WebQSP** (measurement instrument): *measured_by*, 2 papers
  > We adopt two prominent and challenging KGQA benchmarks that necessitate multi-hop reasoning – WebQSP (Yih et al., 2016) and CWQ (Talmor & Berant, 2018).
  - [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf)
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **GrailQA** (measurement instrument): *measured_by*, 2 papers
  > To evaluate the performance of our framework on multi-hop knowledge-intensive reasoning tasks, we conduct tests using four KBQA datasets: CWQ (Talmor & Berant, 2018), WebQSP (Yih et al., 2016), GrailQA (Gu et al., 2021), and SimpleQA (Bordes et al., 2015). (Section 5).
  - [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **CWQ** (measurement instrument): *measured_by*, 2 papers
  > We adopt two prominent and challenging KGQA benchmarks that necessitate multi-hop reasoning – WebQSP (Yih et al., 2016) and CWQ (Talmor & Berant, 2018).
  - [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf)
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **Portability** (construct): *correlates*, 2 papers
  > Portability Metrics Decline with Increasing Number of Hops... This phenomenon can be attributed to the escalating complexity of reasoning required to accurately apply the edited knowledge across multiple interconnected facts.
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **MQuAKE** (measurement instrument): *measured_by*, 1 paper
  > experiments show that CaKE enables more accurate and consistent use of edited knowledge across related reasoning tasks, achieving an average improvement of 20% in multi-hop reasoning accuracy on the MQuAKE dataset (Abstract).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > Through TACT, the model is implicitly required to address information extraction (IE) challenges such as... multi-hop reasoning... (Section 1)
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CLUTRR** (measurement instrument): *measured_by*, 1 paper
  > CLUTRR [41] is a deductive reasoning dataset requiring multi-hop reasoning over family relationships. (Section 4).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > "RULER generates synthetic tasks across multiple categories, including multi-hop reasoning and document tracing, and measures the model’s accuracy."
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our approach on four standard KBQA datasets, all of which require multi-hop reasoning: ComplexWebQuestions (CWQ), WebQuestionsSP (WebQSP), WebQuestions, and GrailQA (Section 5).
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **MultiHop-RAG** (measurement instrument): *measured_by*, 1 paper
  > Assessment of multi-hop reasoning performance on various benchmarks, including HotpotQA (Yang et al., 2018), MuSiQue (Trivedi et al., 2022), and MultiHopRAG (Tang and Yang, 2024), using the EM metric.
  - [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf)
- **NovelHopQA** (measurement instrument): *measured_by*, 1 paper
  > NOVELHOPQA offers a controlled diagnostic setting to test multi-hop reasoning at scale. (Abstract)
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1328.pdf)
- **HybridQA** (measurement instrument): *measured_by*, 1 paper
  > HybridQA (Chen et al., 2020) A multi-hop QA dataset involving both tabular and textual information. (Section 5.1.1)
  - [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.710.pdf)
- **DRISHTIKON** (measurement instrument): *measured_by*, 1 paper
  > “These were augmented into three reasoning categories: Common Sense Cultural... Multi-hop Reasoning, combining multiple cultural aspects”
  - [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > We evaluate QRRETRIEVER on two long-context, multi-hop reasoning tasks: LongMemEval (Wu et al., 2025a) and CLIPPER (Pham et al., 2025). (Section 1)
  - [Query-Focused Retrieval Heads Improve Long-Context Reasoning and Re-ranking](https://aclanthology.org/2025.emnlp-main.1214.pdf)
- **ComplexTempQA** (measurement instrument): *measured_by*, 1 paper
  > “Questions in COMPLEXTEMPQA require advanced reasoning skills, including event/entity matching, multi-hop inference, cross-time comparisons, and temporal ordering.”
  - [ComplexTempQA: A 100m Dataset for Complex Temporal Question Answering](https://aclanthology.org/2025.emnlp-main.463.pdf)

### Associated with
- **Implicit reasoning** (construct), 2 papers
  > This property aligns closely with our focus on multi-hop reasoning and underscores the need for implicit reasoning capability (Section 1).
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [Language models can learn implicit multi-hop reasoning, but only if they have lots of training data](https://aclanthology.org/2025.emnlp-main.490.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > ...we conduct experiments using Llama2-70B [2], GPT-3.5 [1], and GPT-4 [3] on various contextually aware multi-hop reasoning tasks, including claim verification [12], question answering [13], and reading comprehension [14] (Section 1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > ...we conduct experiments using Llama2-70B [2], GPT-3.5 [1], and GPT-4 [3] on various contextually aware multi-hop reasoning tasks, including claim verification [12], question answering [13], and reading comprehension [14] (Section 1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Sequential reasoning** (construct), 1 paper
  > Sequential Reasoning evaluates the model’s ability to perform multi-hop reasoning, interpreting charts in a stepwise manner. (Section 1)
  - [MultiChartQA: Benchmarking Vision-Language Models on Multi-Chart Problems](https://aclanthology.org/2025.naacl-long.566.pdf)
- **Critique ability** (construct), 1 paper
  > “To answer multi-hop reasoning questions, self-critique involves prompting the LLM to generate subquestions and answer them using retrieved passages in a step-by-step manner.”
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **Multi-hop question answering** (behavioral indicator), 1 paper
  > Multi-hop question answering (MHQA) involves reasoning across multiple documents to answer complex questions. (Abstract)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Long-context understanding** (construct), 1 paper
  > These results affirm that long-context capacity alone is not enough—multi-hop reasoning remains an open challenge. (Section 5)
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1328.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > We propose SCRIBE, a framework for multi-hop tool reasoning, where models must flexibly call tools and self-reflect to generate high-quality responses. (Section 1)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Knowledge retrieval** (behavioral indicator), 1 paper
  > Since complex questions often involve external geographic knowledge, we then adaptively retrieve it as supplementary clues and conduct multi-hop reasoning based on it.
  - [Answering Complex Geographic Questions by Adaptive Reasoning with Visual Context and External Commonsense Knowledge](https://aclanthology.org/2025.acl-long.1239.pdf)
