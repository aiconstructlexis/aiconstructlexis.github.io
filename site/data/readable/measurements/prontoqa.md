# PrOntoQA
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** ProntoQA  

## State of the Field

**What it is.** Most papers treat PrOntoQA, sometimes written ProntoQA, as a synthetic benchmark for logical or multi-step reasoning. Definitions differ in emphasis: some describe data points that assign hierarchical relationships among objects and ask whether a multi-step reasoning chain is correct, while others describe question-answering examples with explicit chains of thought, or a synthetic first-order logic benchmark with problems derived from ontologies and axioms over structured knowledge.

**What it is claimed to measure.** Across papers, the prevailing use is to measure logical reasoning. It is linked to two constructs, Logical reasoning and the broader Reasoning, and to two behavioral indicators, Logical problem solving and Question answering; most claims center on logical reasoning, while a smaller line frames it as measuring general reasoning, and isolated papers use it for logical problem solving or as question-answering examples.

**Space of uses.** Papers usually position it as one benchmark among several for logical or deductive reasoning evaluation, and some explicitly use it for out-of-distribution evaluation. Among linked instruments, it is related to ProofWriter, and one paper says performance transfer between them may reflect their high similarity, noting that both datasets use predefined templates for logic and corresponding natural language.

**Concerns raised.** The clearest practical limitation papers mention is availability: one paper excludes ProntoQA from an experiment because it lacks a publicly available training set. Another paper reports that a model finetuned on ProofWriter achieves the highest performance on PrOntoQA and attributes this anomaly to the datasets' high similarity and shared template-based generation.

## Sources

**PrOntoQA** (2 papers: [Initialization is Critical to Whether Transformers Fit Composite Functions by Reasoning or Memorizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/19c145aaad40927c51f4d10eaa339c20-Paper-Conference.pdf), [Collaborative Beam Search: Enhancing LLM Reasoning via Collective Consensus](https://aclanthology.org/2025.emnlp-main.574.pdf))
> A synthetic multi-step reasoning dataset where models must determine the correctness of a reasoning chain based on provided hierarchical relationships.

**ProntoQA** (2 papers: [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf), [RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25a/chan25a.pdf))
> A synthetic first-order logic reasoning benchmark used for comparison and out-of-distribution evaluation.

## Relationships

### → PrOntoQA
- **Logical reasoning** (construct): *measured_by*, 8 papers
  > PrOntoQA (Saparov and He, 2023): A dataset designed for logical reasoning. (Section 4.1)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > Reasoning tasks: PrOntoQA. PrOntoQA (Saparov and He, 2023) is a synthetic multi-step reasoning dataset where each data point assigns hierarchical relationships among objects and requires the model to determine whether a multi-step reasoning chain is correct. (Section 6)
  - [Initialization is Critical to Whether Transformers Fit Composite Functions by Reasoning or Memorizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/19c145aaad40927c51f4d10eaa339c20-Paper-Conference.pdf)
  - [An Analysis for Reasoning Bias of Language Models with Small Initialization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yao25g/yao25g.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > "The first dataset, PrOntoQA ... consists of question-answering examples"
  - [An Analysis for Reasoning Bias of Language Models with Small Initialization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yao25g/yao25g.pdf)
- **Logical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > ProntoQA (Saparov & He, 2022) is a dataset consists of 9000 logical reasoning problems derived from ontologies - formal representations of relationships between concepts. (Section 4.1.1)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)

### Associated with
- **ProofWriter** (measurement instrument), 1 paper
  > “The model finetuned on ProofWriter achieves the highest performance on ProntoQA. This anomaly could be attributed to the high similarity between ProntoQA and ProofWriter: Both datasets utilize predefined templates for generating logic and corresponding natural language.”
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
