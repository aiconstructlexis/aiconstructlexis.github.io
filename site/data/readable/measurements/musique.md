# MuSiQue
**Type:** Measurement instrument  
**Supporting papers:** 76  
**Also known as:** MUSIQUE, Musique, MusiQue, musique, MuSiQue-Ans  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats MuSiQue as a challenging multi-hop question answering dataset or benchmark built from composable pairs of single-hop questions, so models must connect multiple pieces of information across multiple paragraphs, passages, or documents. Many descriptions add that it supports up to four-hop reasoning or at least two reasoning steps, and several say it was designed to reduce reasoning shortcuts or require connected or disentangled reasoning. A smaller line of work refers to named variants or slices, including the answerable version, MuSiQue-Ans, 2-hop questions, and 3-hop or 4-hop portions; one definition also mentions adversarially written paragraphs, and another describes diverse domains with minimal lexical overlap.

**What it is claimed to measure.** Papers use MuSiQue to measure 3 constructs and 4 behavioral indicators. The dominant claims center on multi-hop reasoning and multi-hop question answering, and papers repeatedly use the benchmark to assess multi-step reasoning over complex information dependencies. More selectively, papers also report it as measuring question answering, generalization, and chain of thought, with 2 other linked targets beyond these.

**Space of uses.** Papers link MuSiQue to 1 other instrument, LongBench, and most commonly use it alongside HotpotQA and 2WikiMultiHopQA, often also with StrategyQA and Bamboogle. The prevailing role is as an evaluation benchmark for retrieval, reasoning, and question answering systems, though some papers use it as warm-up training data, as out-of-domain evaluation for transfer or generalization, or on specific subsets such as the answerable version or a 2-hop split.

**Concerns raised.** Descriptions repeatedly stress that MuSiQue is intentionally hard: several say it reduces reasoning shortcuts or requires connected or disentangled reasoning over multiple facts. Smaller descriptions mention adversarially written paragraphs, harder distracting content, and unanswerable questions, and one paper explicitly describes it as much more difficult than HotpotQA.

## Sources

**MuSiQue** (15 papers: [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf), [CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA](https://aclanthology.org/2025.naacl-long.300.pdf), [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [AMOR: A Recipe for Building Adaptable Modular Knowledge Agents Through Process Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4595e77b045971a654edc5e3cd31989-Paper-Conference.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf), [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf), [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf))
> MuSiQue is a challenging multi-hop question answering dataset where questions are constructed from composable pairs of single-hop questions, requiring models to connect multiple pieces of information.

**MUSIQUE** (1 paper: [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> A multi-hop question answering dataset that requires reasoning over multiple paragraphs to answer questions, featuring adversarially-written paragraphs to challenge models.

**Musique** (2 papers: [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf), [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf))
> A benchmark for multi-hop question answering, where a model must connect multiple pieces of information to arrive at the correct answer.

**musique** (1 paper: [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf))
> Multi-hop question answering dataset constructed to prevent reasoning shortcuts, with complex questions derived from single-hop questions linked by bridge entities, used for evaluating decomposition and downstream QA performance.

**MusiQue** (1 paper: [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf))
> Multi-hop question answering dataset requiring reasoning over diverse domains with minimal lexical overlap, designed to test true compositional reasoning.

**MuSiQue-Ans** (1 paper: [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf))
> A benchmark dataset for multi-hop question answering featuring complex, multi-step questions, also referred to as MuSiQue.

## Relationships

### → MuSiQue
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 16 papers
  > We evaluate our method’s retrieval capabilities primarily on two challenging multi-hop QA benchmarks, MuSiQue (answerable) [77] and 2WikiMultiHopQA [33]. (Section 3.1)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf)
  - [Inference Scaling for Long-Context Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b57471758783450408f5c9b70257d15b-Paper-Conference.pdf)
  - [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf)
  - [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
  - [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1089.pdf)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf)
  - [Understanding Synthetic Context Extension via Retrieval Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25ad/zhao25ad.pdf)
  - [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf)
  - [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf)
  - [KG-CQR: Leveraging Structured Relation Representations in Knowledge Graphs for Contextual Query Retrieval](https://aclanthology.org/2025.emnlp-main.824.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 11 papers
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
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > Question Answering For this task, we consider the following datasets: 2WikiMultiHopQA [27], StrategyQA [28], MuSiQue [29], and HotpotQA [30] (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022)... These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **Chain of thought** (behavioral indicator): *measured_by*, 1 paper
  > To examine how retrieval heads effect reasoning tasks, we test Mistrial-7B-Instruct-v0.2 on MMLU (Hendrycks et al., 2020), MuSiQue and GSM8K (Cobbe et al., 2021), with and without chain-of-thought (CoT) reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Open-domain question answering** (behavioral indicator): *measured_by*, 1 paper
  > TriviaQA, MuSiQue, PopQA are challenging open-domain question answering datasets where RAG systems are required to answer questions on factual knowledge. (Section 4)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)

### Associated with
- **LongBench** (measurement instrument), 2 papers
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering)... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
