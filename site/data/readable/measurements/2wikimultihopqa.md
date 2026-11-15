# 2WikiMultiHopQA
**Type:** Measurement instrument  
**Supporting papers:** 74  
**Also known as:** 2WikiMultihopQA, 2wikimultihopqa, 2WIKIMULTIHOPQA, 2WikiMQA, 2WikiMHQA, 2WikiMulti-hopQA, 2Wikimultihop, 2Wiki, 2Wiki-MultiHopQA, 2WikiHop, WikiMultiHopQA  

## State of the Field

**What it is.** Across papers, the prevailing description is a Wikipedia-based multi-hop question answering dataset or benchmark. Most definitions emphasize multi-document reasoning, with answers requiring models to combine information from multiple documents, evidence pieces, paragraphs, or sources; some add that it includes up to 5-hop questions synthesized from Wikipedia passages through manually designed templates. A smaller line of work narrows this to reasoning over two linked facts or entity-centric questions that combine information from two or more distinct Wikipedia articles, and one paper presents it as a more challenging benchmark with many comparison and composition questions. Some papers also refer to a LongBench form of the benchmark under the name 2WikiMQA.

**What it is claimed to measure.** Across papers, it is linked to 5 constructs and 4 behavioral indicators. The prevailing use is to measure multi-hop question answering and multi-hop reasoning. Papers also use it to measure question answering and chain-of-thought reasoning, while the remaining links spread across several other QA and reasoning framings.

**Space of uses.** It is most commonly used alongside HotpotQA and MuSiQue, and some papers also pair it with StrategyQA and Bamboogle. Papers usually position it as one item in a small set of multi-hop or complex QA benchmarks; some use it for unseen evaluation of RAG-tuned models, some for in-domain evaluation, and a smaller line uses its LongBench form for multi-document QA or multi-step reasoning. One paper also reports testing both single-step and chain-of-thought setups on it.

## Sources

**2WikiMultihopQA** (3 papers: [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf), [CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf), [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf))
> A multi-document, multi-hop question-answering dataset involving up to 5-hop questions synthesized from Wikipedia passages.

**2WikiMultiHopQA** (5 papers: [Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c27bf8d56d3d50c7aeaf7535dee975-Paper-Conference.pdf), [SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA](https://aclanthology.org/2025.naacl-long.300.pdf), [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf), [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> A dataset used for evaluating retrieval-augmented generation performance on question-answer pairs.

**2wikimultihopqa** (1 paper: [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf))
> A multi-hop question-answering dataset derived from Wikipedia, used as an unseen evaluation task for RAG-tuned models.

**2WIKIMULTIHOPQA** (1 paper: [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> A multi-hop question answering dataset that requires reasoning over multiple documents to find the answer.

**2WikiMQA** (4 papers: [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf), [Dynamic Chunking and Selection for Reading Comprehension of Ultra-Long Context in Large Language Models](https://aclanthology.org/2025.acl-long.1538.pdf), [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf), [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf))
> A multi-hop question answering benchmark used to assess multi-step reasoning over long contexts.

**2WikiMHQA** (1 paper: [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf))
> A multi-hop question answering dataset built from Wikipedia, requiring reasoning over multiple evidence documents.

**2WikiMulti-hopQA** (1 paper: [Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering](https://aclanthology.org/2025.acl-long.981.pdf))
> Multi-hop question answering dataset requiring reasoning over two linked facts, built from Wikipedia.

**2Wikimultihop** (1 paper: [Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs through Generation of Well-Formed Chains](https://aclanthology.org/2025.acl-long.1186.pdf))
> A challenging benchmark for multi-hop question answering where the knowledge graph is constructed from provided text passages and a large proportion of questions require reasoning types like comparison and composition.

**2Wiki** (1 paper: [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf))
> The 2WikiMultiHopQA (2Wiki) benchmark, a multi-hop open-domain question answering dataset used for in-domain evaluation.

**2Wiki-MultiHopQA** (1 paper: [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf))
> A multi-hop question answering benchmark dataset designed to test reasoning over multiple documents from Wikipedia.

**2WikiHop** (1 paper: [Gumbel Reranking: Differentiable End-to-End Reranker Optimization](https://aclanthology.org/2025.acl-long.354.pdf))
> A multi-hop question answering benchmark dataset built on Wikipedia, where answers require traversing through multiple documents.

**WikiMultiHopQA** (1 paper: [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf))
> WikiMultiHopQA is a dataset for evaluating multi-hop question answering, requiring models to synthesize information from multiple sources.

## Relationships

### → 2WikiMultiHopQA
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 17 papers
  > We evaluate our method’s retrieval capabilities primarily on two challenging multi-hop QA benchmarks, MuSiQue (answerable) [77] and 2WikiMultiHopQA [33]. (Section 3.1)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
  - [MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations](https://proceedings.neurips.cc/paper_files/paper/2024/file/e560a0b22e4432003d0dba63ff8dc457-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf)
  - [Inference Scaling for Long-Context Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b57471758783450408f5c9b70257d15b-Paper-Conference.pdf)
  - [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
  - [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1089.pdf)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)
  - [Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs through Generation of Well-Formed Chains](https://aclanthology.org/2025.acl-long.1186.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf)
  - [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 6 papers
  > When evaluated on multi-hop reasoning benchmarks, our approach achieves up to 95–100% accuracy on 2WikiMultiHopQA (Abstract).
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
  - [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf)
  - [TreeRare: Syntax Tree-Guided Retrieval and Reasoning for Knowledge-Intensive Question Answering](https://aclanthology.org/2025.emnlp-main.947.pdf)
  - [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf)
  - [SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA](https://aclanthology.org/2025.naacl-long.300.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 4 papers
  > Question Answering For this task, we consider the following datasets: 2WikiMultiHopQA [27], StrategyQA [28], MuSiQue [29], and HotpotQA [30] (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > To assess OmniKV’s performance in multi-step reasoning, we utilized 2WikiMQA (Ho et al., 2020) and HotpotQA (Yang et al., 2018) from LongBench. (Section 5)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > “Experiments across three complex question-answering datasets reveal that ASSISTRAG exhibits superior reasoning capabilities” and the datasets include “2WikiMultiHopQA [35]”
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Information synthesis** (behavioral indicator): *measured_by*, 1 paper
  > ...and two multi-hop QA datasets: Adversarial HotpotQA (Yang et al., 2018), and 2WikiMultihopQA (Ho et al., 2020), which assess cross-document reasoning and information integration using Wikipedia data. (Section 4.1)
  - [Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://aclanthology.org/2025.emnlp-main.549.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Multi-document question answering** (behavioral indicator): *measured_by*, 1 paper
  > The multi-document QA task involves "2Wiki-MultihopQA" from LongBench (Bai et al., 2023), comprising 200 samples. (Section 4.2)
  - [Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.457.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To evaluate the transferability of our approach, we conducted out-of-domain experiments by training the model on one dataset and testing it on another. We use the 2Wiki (2W), HotpotQA (HQ), and MuSiQue (MQ) datasets. (Section 6.6)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)

### Associated with
- **LongBench** (measurement instrument), 2 papers
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
