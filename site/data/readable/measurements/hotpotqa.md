# HotpotQA
**Type:** Measurement instrument  
**Supporting papers:** 180  
**Also known as:** HotPotQA, HOTPOTQA, Hotpot-QA, Hotpot_QA  

## State of the Field

**What it is.** Across papers, the prevailing usage is a multi-hop question answering benchmark or dataset whose questions require combining evidence across multiple supporting documents, passages, or paragraphs, usually from Wikipedia. Some authors instead describe it as multi-hop reading comprehension, multi-document QA, search-based or open-domain QA, and papers mention setups such as fullwiki, distractor, closed-book, inclusion in KILT or LongBench, and a version where retrieval difficulty is manipulated by paragraph ordering. Descriptions of the answer format also vary, with some papers calling it an open-ended task with long answers and others a closed-ended task with short entity or yes or no answers.

**What it is claimed to measure.** Papers use HotpotQA to measure a broad set of targets: it is linked to 9 constructs and 10 behavioral indicators. The leading construct links are to multi-hop reasoning and reasoning; among behavioral indicators, the most common links are to multi-hop question answering and question answering, with some work framing it as complex reasoning question answering. Overall, papers use it for several different reasoning and QA targets rather than a single construct alone.

**Space of uses.** HotpotQA is used both as a main evaluation benchmark and as a component inside other evaluation suites or environments. Papers also relate it to 2 other instruments, LongBench and HELMET, and several authors adapt it into agent or multi-turn settings, reconstruct environments from it, or use its evaluation script to score retrieval quality with F1, precision, and recall against referenced facts. Practical use also varies by split and protocol, including official validation used for testing when the test set is hidden, as well as distractor, fullwiki, train-hard, and variant-based setups.

**Concerns raised.** The main explicit concern raised in the papers is about validity for multi-hop reasoning: one paper describes HotpotQA as a much weaker test for multi-hop reasoning because of many spurious signals.

## Sources

**HotpotQA** (26 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf), [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf), [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf), [RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement](https://aclanthology.org/2025.naacl-long.361.pdf), [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf))
> HotpotQA is a multi-hop question answering benchmark used to evaluate answering questions that require combining multiple pieces of evidence.

**HotPotQA** (4 papers: [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf), [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf))
> A question answering benchmark that requires an agent to find and reason over multiple supporting documents from Wikipedia to answer complex questions.

**HOTPOTQA** (1 paper: [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> A question answering dataset that requires finding and reasoning over multiple supporting documents to answer complex questions.

**Hotpot-QA** (1 paper: [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf))
> A multi-document question answering dataset in which the model answers a question using multiple related Wikipedia paragraphs, with retrieval difficulty manipulated by paragraph ordering.

**Hotpot_QA** (1 paper: [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf))
> A question answering dataset that requires multi-hop reasoning across multiple supporting documents to find the answer.

## Relationships

### → HotpotQA
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 29 papers
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
- **Question answering** (behavioral indicator): *measured_by*, 15 papers
  > “HotPotQA provides a more challenging open-ended question answering task with long answers containing many tokens.”
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [How Do Large Vision-Language Models See Text in Image? Unveiling the Distinctive Role of OCR Heads](https://aclanthology.org/2025.emnlp-main.1032.pdf)
  - [PathwiseRAG: Multi-Dimensional Exploration and Integration Framework](https://aclanthology.org/2025.emnlp-main.1167.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 13 papers
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
- **Reasoning** (construct): *measured_by*, 5 papers
  > HotPotQA [49] features natural, multi-hop questions, which challenge an agent’s ability to perform reasoning and utilize search tools.
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To evaluate the transferability of our approach, we conducted out-of-domain experiments by training the model on one dataset and testing it on another. We use the 2Wiki (2W), HotpotQA (HQ), and MuSiQue (MQ) datasets. (Section 6.6)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **Tool use** (behavioral indicator): *measured_by*, 1 paper
  > HotPotQA [49] features natural, multi-hop questions, which challenge an agent’s ability to perform reasoning and utilize search tools.
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > We have conducted additional experiments on more realistic open-ended generations datasets, Hot-PotQA [57], Natural Question (NQ) [23], TriviaQA [21]. (Appendix D)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **Context retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We further conduct experiments on open-source LLMs based on Transformer, Mambda, and a hybrid architecture to show that for tasks that require stronger in-context retrieval capability, RNNs suffer more performance degradation compared to Transformers. ... To test our theory, we use the Hotpot-QA (Yang et al., 2018) dataset. (Section 6.2)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Open-domain question answering** (behavioral indicator): *measured_by*, 1 paper
  > we use three open-domain QA datasets for evaluation, namely PopQA (Mallen et al., 2023a), AmbigNQ (Min et al., 2020) and HotpotQA (Yang et al., 2018). (Section 4)
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **Complex reasoning question answering** (behavioral indicator): *measured_by*, 1 paper
  > HotpotQA (Yang et al., 2018) is a complex question answering dataset of multi-hop reasoning questions which cannot be answered by a single memorized fact, but instead require chaining facts together. (Section 3)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **Continual learning** (construct): *measured_by*, 1 paper
  > Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA... (Section 4.1)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > To assess OmniKV’s performance in multi-step reasoning, we utilized 2WikiMQA (Ho et al., 2020) and HotpotQA (Yang et al., 2018) from LongBench. (Section 5)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > World-knowledge tasks: TriviaQA (Joshi et al., 2017), Natural Questions (Kwiatkowski et al., 2019), HotpotQA (Yang et al., 2018), WebQuestions (Berant et al., 2013), ComplexWebQuestions (Talmor & Berant, 2018). (Section 5.1)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 2. HotpotQA (Yang et al., 2018): A multi-hop question answering benchmark that requires reason-ing across paragraphs from multiple Wikipedia pages”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Retrieval quality** (construct): *measured_by*, 1 paper
  > “For retrieval quality, we use the evaluation script provided by HotpotQA to measure the F1 score, precision, and recall between the retrieved chunks and referenced facts.”
  - [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > Comparison of decomposition approaches across benchmarks. Method ... Text Understanding ... HotpotQA (Table 2)
  - [Select-Then-Decompose: From Empirical Analysis to Adaptive Selection Strategy for Task Decomposition in Large Language Models](https://aclanthology.org/2025.emnlp-main.278.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Factual question answering** (behavioral indicator): *measured_by*, 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Complex reasoning** (construct): *measured_by*, 1 paper
  > “We conduct experiments on three representative agent tasks: Complex Reasoning (HotpotQA (Yang et al., 2018)), Embodied Decision (ALFWorld (Shridhar et al., 2020)), and Interactive Programming (InterCode (Yang et al., 2023))”
  - [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf)

### Associated with
- **LongBench** (measurement instrument), 2 papers
  > We also include HotpotQA (multi-document question answering) from LongBench... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **HELMET** (measurement instrument), 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
