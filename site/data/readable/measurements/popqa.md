# PopQA
**Type:** Measurement instrument  
**Supporting papers:** 53  
**Also known as:** POPQA  

## State of the Field

**What it is.** Across papers, PopQA is most commonly described as an open-domain question-answering dataset or benchmark, often entity-centric and focused on rare entities, long-tail knowledge, or questions spanning a wide range of entity popularity. Some descriptions make this more concrete by calling it a large-scale resource with 14K questions or 14k entity-centric QA pairs, while a smaller line of work says it is derived from Wikidata triples or frames it as single-hop QA that is difficult to answer from parametric memory alone. Variants and formats also differ by use: one study uses a long-tail subset of 1,399 rare entity queries, and another turns its questions into a closed-book sentence-completion task.

**What it is claimed to measure.** Measurement claims center on 2 behavioral indicators, especially open-domain question answering and a broader question-answering framing. Papers also use PopQA to measure 4 constructs, most visibly factual knowledge, knowledge conflict resolution, memorization, and out-of-distribution generalization. Taken together, the construct-level uses are spread across several targets rather than concentrated on one.

**Space of uses.** Papers usually include PopQA in multi-dataset QA evaluations rather than using it alone. It is commonly used alongside TriviaQA and Natural Questions, and it also appears with WebQ, HotpotQA, and AmbigNQ. Smaller uses make it a testbed for knowledge conflict experiments, sample questions from it for self-contradiction evaluation, use it for out-of-domain evaluation, or test answering from retrieved background knowledge.

## Sources

**PopQA** (10 papers: [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.131.pdf), [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf))
> Open-domain question answering dataset focusing on rare entities, evaluating factual knowledge retrieval in long-tail scenarios.

**POPQA** (1 paper: [Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf))
> An entity-centric question answering dataset derived from Wikidata triples, used to evaluate LLMs on factual knowledge and memory consistency.

## Relationships

### → PopQA
- **Open-domain question answering** (behavioral indicator): *measured_by*, 8 papers
  > Short-form generations tasks include two open-domain question answering (QA) datasets, PopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017)... (Section 4.1)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > We adapt our approach to question answering as described at the end of Section 5. We focus on 1.5K randomly sampled questions from PopQA. (Section 6.3)
  - [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Knowledge conflict resolution** (construct): *measured_by*, 1 paper
  > We benchmark the current LLM’s ability to perform situated faithful reasoning on several question-answering tasks, including FreshQA (Vu et al., 2023), NaturalQA (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023).
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **Factual knowledge** (construct): *measured_by*, 1 paper
  > For factual knowledge, we use PopQA (Mallen et al., 2023), TriviaQA (Joshi et al., 2017), and Natural Questions (NQ) (Kwiatkowski et al., 2019). (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
- **Memorization** (construct): *measured_by*, 1 paper
  > Evaluation of continual learning capabilities across three key dimensions: factual memory (NaturalQuestions, PopQA), sense-making (NarrativeQA), and associativity (MuSiQue, 2Wiki, HotpotQA, and LV-Eval) (Figure 1).
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2022), and PopQA (Mallen et al., 2022). These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
