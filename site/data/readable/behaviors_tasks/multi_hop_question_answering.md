# Multi-hop question answering
**Type:** Behavioral indicator  
**Supporting papers:** 86  
**Also known as:** Multi-hop QA, Multihop question answering, Two-hop relational question answering, Multi-hop factual recall, Multi-hop tracing, Compositional question answering, Multi-hop reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats multi-hop question answering as answering complex questions by finding, retrieving, and combining multiple pieces of information, usually across multiple documents, passages, or other sources, and then producing a final answer. Most definitions emphasize reasoning over distributed evidence, sometimes described as logically connecting relevant information from multiple documents or integrating multiple passages or facts through relational reasoning. A smaller line of work makes the intermediate process explicit: models generate sub-questions or intermediate question-answer pairs until the final answer, or compose a fixed chain such as two relational facts from a provided context.

**Variants.** Papers study several variants of this behavior. Common settings include open-domain multi-hop QA across different documents, long-context versions that require combining information from multiple parts of a long context or multiple pages, and decomposition-based or compositional settings built from interdependent sub-questions. Smaller variants are named multi-hop tracing, multi-hop factual recall after knowledge edits, two-hop relational question answering, and multi-hop KGQA.

**Space of elicitation and scores.** Papers measure it with 10 instruments. The most commonly used ones are HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle, and MQuAKE, and these are mostly benchmark datasets for open-domain or complex multi-hop question answering, although MQuAKE is framed as a knowledge editing dataset built from chains of single-hop subquestions. Other linked instruments cover multi-article QA, multi-hop knowledge graph QA, long-context subtasks, and related complex QA settings. Where scoring is stated, MQuAKE work uses Multi-hop Accuracy and Hop-wise Answering Accuracy.

**What it is taken as evidence of.** Papers link this behavior to 5 constructs: context faithfulness, information integration, multi-hop reasoning, portability, and reasoning. Across papers, these links are not presented as a single shared construct, and they are framed as related to rather than as one agreed interpretation. The linked work connects multi-hop question answering to integrating information between passages, to multi-hop and multi-step reasoning, and in knowledge-editing settings also to context faithfulness and portability.

## Sources

**Multi-hop question answering** (12 papers: [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf), [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://proceedings.iclr.cc/paper_files/paper/2024/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf), [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf))
> The task of answering a question that requires finding and combining multiple pieces of information, often by generating and answering a series of intermediate questions.

**Multi-hop QA** (1 paper: [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf))
> Producing answers that require integrating information from multiple passages or facts through relational reasoning.

**Multihop question answering** (1 paper: [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf))
> Generating answers to questions that require retrieving and synthesizing information from multiple sources or documents.

**Two-hop relational question answering** (1 paper: [Reason to Rote: Rethinking Memorization in Reasoning](https://aclanthology.org/2025.emnlp-main.437.pdf))
> The task of answering a question that requires composing two distinct relational facts from a provided context to find the correct entity.

**Multi-hop factual recall** (1 paper: [Locate-then-edit for Multi-hop Factual Recall under Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aq/zhang25aq.pdf))
> The observable task of answering a question that requires chaining together two or more pieces of factual information, particularly after one of the facts in the chain has been edited.

**Multi-hop tracing** (3 papers: [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.430.pdf), [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf))
> The task of following a chain of reasoning or references across multiple steps within a text to answer a question.

**Compositional question answering** (1 paper: [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.331.pdf))
> The task of answering a complex question that requires breaking it down into multiple, interdependent sub-questions and synthesizing their answers.

**Multi-hop reasoning** (2 papers: [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf), [Mitigating Heterogeneous Token Overfitting in LLM Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ae/liu25ae.pdf))
> Generating answers that require chaining multiple logical inferences from edited knowledge, such as answering 'Who is the first lady of the United States?' after editing the president.

## Relationships

### Multi-hop question answering →
- **HotpotQA** (measurement instrument): *measured_by*, 29 papers
  > In this case study, we explore the multi-hop question answering task with the HotPotQA (Yang et al., 2018) dataset in the open-domain “fullwiki” setting. (Section 7)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
  - [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations](https://proceedings.neurips.cc/paper_files/paper/2024/file/e560a0b22e4432003d0dba63ff8dc457-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
  - [SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf)
  - [Inference Scaling for Long-Context Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b57471758783450408f5c9b70257d15b-Paper-Conference.pdf)
  - [Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf)
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf)
  - [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
  - [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1089.pdf)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)
  - [AgentPro: Enhancing LLM Agents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.506.pdf)
  - [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf)
  - [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf)
  - [KG-CQR: Leveraging Structured Relation Representations in Knowledge Graphs for Contextual Query Retrieval](https://aclanthology.org/2025.emnlp-main.824.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 17 papers
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
- **MuSiQue** (measurement instrument): *measured_by*, 16 papers
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
- **Bamboogle** (measurement instrument): *measured_by*, 3 papers
  > To evaluate the ability of different models to answer complex questions, we selected four complex question answering datasets: ... (4) Bamboogle (Press et al., 2023) (Section 3.1).
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 2 papers
  > We conduct a comprehensive evaluation across multiple reasoning tasks, including multi-hop QA: StrategyQA (Geva et al., 2021) (Section 1)
  - [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf)
  - [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf)
- **MultiHop-RAG** (measurement instrument): *measured_by*, 2 papers
  > It includes 2,556 multi-hop questions requiring the integration of information from multiple articles to formulate comprehensive answers (Section 4.1).
  - [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)
- **MQuAKE** (measurement instrument): *measured_by*, 2 papers
  > MQUAKE (Multi-hop Question Answering for Knowledge Editing) is a knowledge editing dataset focusing on the abovementioned multi-hop question answering tasks proposed in Zhong et al. (2023), where every case of MQUAKE is a multi-hop question made by a chain of single-hop subquestions. (Section 2.1)
  - [MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/f782860c2a5d8f675b0066522b8c2cf2-Paper-Conference.pdf)
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **WebQSP** (measurement instrument): *measured_by*, 2 papers
  > We evaluated our method on different knowledge-intensive reasoning benchmark datasets, including two multi-hop KBQA datasets WebQSP (Yih et al., 2016) and QALD10-en (Usbeck et al., 2023) (Section 4.1)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > RULER reports the averaged accuracy on two multi-hop question answering subtasks from RULER. (Table 4)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)

### → Multi-hop question answering
- **Question decomposition** (behavioral indicator): *causes*, 1 paper
  > Question decomposition has been found to help large language models’ (LLMs) performance on complex question answering (QA) by breaking these questions into simpler sub-questions for answering.
  - [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf)
- **Knowledge retrieval** (behavioral indicator): *causes*, 1 paper
  > due to the requirement for external knowledge in complex multi-hop questions (Mavi et al., 2024; Minaee et al., 2024), retrieval-augmented reasoning methods show more significant improvement compared to closed-book methods. (Section 5.1.1)
  - [BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.211.pdf)

### Associated with
- **Multi-hop reasoning** (construct), 1 paper
  > Multi-hop question answering (MHQA) involves reasoning across multiple documents to answer complex questions. (Abstract)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Reasoning** (construct), 1 paper
  > we can increase the complexity of a question by making it a multi-hop question [23, 24], which can be used to test whether an LLM can think in multiple steps. (Section 3.3)
  - [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Information integration** (construct), 1 paper
  > standard multi-hop question answering (QA) also requires integrating information between passages in a retrieval corpus. (Section 1)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
- **Context faithfulness** (construct), 1 paper
  > We adopt a multi-hop editing task to measure context-faithfulness of LLMs in Section 4 by evaluating the accuracy of multi-hop question answering with fact edits. (Section 2.2)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Portability** (construct), 1 paper
  > The Portability Scores intend to measure the ability of LLMs to reason about the downstream effects of edited knowledge. Thus, we design the Efficacy Evaluation Questions with N hops (N = 1 ∼6) as Portability Evaluation Questions. (Section 2.2, Facet 3)
  - [Can Knowledge Editing Really Correct Hallucinations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/db93ccb6cf392f352570dd5af0a223d3-Paper-Conference.pdf)
