# Creak
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** CREAK  

## State of the Field

**What it is.** Across the surveyed papers, the prevailing usage treats Creak as a fact-checking dataset or benchmark. Definitions describe it as evaluating verification of claims against a knowledge graph using Wikidata, while a smaller framing presents CREAK as a benchmark for fact-checking and commonsense reasoning that assesses whether statements are supported by commonsense knowledge.

**What it is claimed to measure.** Papers link Creak to 2 constructs and 1 behavioral indicator. The most common claim is that it measures fact checking, with papers describing it as a fact-checking or fact verification dataset; some also use it to measure commonsense reasoning, and a single paper reports it as measuring factual reasoning.

**Space of uses.** No measurement instrument is linked to it. In use, papers pair it with FEVER in fact verification settings, and with StrategyQA and CSQA2 in evaluations described as containing many questions about entity knowledge and commonsense reasoning; one paper also places it under a "Factual Reasoning Task."

## Sources

**Creak** (1 paper: [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf))
> A fact-checking dataset for evaluating the verification of claims against a knowledge graph, using Wikidata.

**CREAK** (1 paper: [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf))
> A benchmark for fact-checking and commonsense reasoning that assesses whether statements are supported by commonsense knowledge.

## Relationships

### → Creak
- **Fact checking** (behavioral indicator): *measured_by*, 3 papers
  > and one fact-checking dataset: Creak (Onoe et al., 2021).
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 2 papers
  > We evaluate our UniCoTT over CREAK (Onoe et al., 2021), StrategyQA (Geva et al., 2021) and CSQA2 (Talmor et al., 2021) datasets, which contain a large number of questions about entity knowledge and commonsense reasoning (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Factual reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments across three types of tasks: (1) Factual Reasoning Task. We evaluate our UniCoTT over CREAK (Onoe et al., 2021), StrategyQA (Geva et al., 2021) and CSQA2 (Talmor et al., 2021) datasets (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
