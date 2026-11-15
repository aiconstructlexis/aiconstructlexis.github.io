# Contradiction detection
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Document-level self-contradiction detection, Contradiction identification, Conflict detection, Answer conflict detection, Corpus-level inconsistency detection, Contradiction checking  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is detecting logical inconsistency or contradiction between statements, facts, or assertions. Most formulations ask whether a pair or collection contains any contradiction, for example whether two generated sentences are contradictory in context, whether a multi-sentence document has any internal contradiction, or whether a fact is contradicted by another fact in the same corpus. A smaller line of work casts the behavior as selecting the contradictory pair itself, such as choosing the testimony and evidence that contradict each other in a multiple-choice space, while other papers formalize conflict as a state that entails both φ and ¬φ or as the appearance of an empty clause in a reduced formula.

**Variants.** Authors study this behavior under several task-specific names, most often as conflict detection, contradiction detection, document-level self-contradiction detection, corpus-level inconsistency detection, and contradiction checking. The settings range from sentence pairs, multi-sentence documents, and atomic facts in a corpus to multilingual answers that are semantically inconsistent with an English reference, retrieved external knowledge that contradicts a model's internal knowledge, and story world states where overlapping validity intervals make facts incompatible. Other variants place the contradiction inside structured reasoning problems, including testimony versus evidence, contract clauses versus legal provisions, multi-agent assertions, and partial assignments in SAT solving.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead operationalize the behavior directly, usually as a contradiction judgment over sentence pairs, facts, documents, or clause-provision pairs; some formulations make the output the contradictory pair itself, and one corpus-level version is explicitly defined as binary classification over atomic facts.

**What it is taken as evidence of.** Only one construct is linked to this behavior. That construct is Knowledge conflict resolution, and the recorded claim is only that contradiction detection is related to it: one paper describes a framework that can identify and resolve detailed points of knowledge conflict.

## Sources

**Document-level self-contradiction detection** (1 paper: [Think Wider, Detect Sharper: Reinforced Reference Coverage for Document-Level Self-Contradiction Detection](https://aclanthology.org/2025.emnlp-main.67.pdf))
> The task of identifying whether a multi-sentence document contains any internal contradictions.

**Contradiction identification** (1 paper: [TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games](https://aclanthology.org/2025.emnlp-main.101.pdf))
> The observable task of selecting a pair of testimony and evidence that logically contradict each other based on narrative context.

**Conflict detection** (3 papers: [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf), [Can Transformers Reason Logically? A Study in SAT Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25d/pan25d.pdf), [Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement](https://aclanthology.org/2025.naacl-long.63.pdf))
> Observably identifying logical inconsistencies between assertions, either within a single agent or across the multi-agent system.

**Answer conflict detection** (1 paper: [XLQA: A Benchmark for Locale-Aware Multilingual Open-Domain Question Answering](https://aclanthology.org/2025.emnlp-main.1466.pdf))
> Identifying cases where model responses differ semantically across languages for the same question, indicating potential locale sensitivity.

**Corpus-level inconsistency detection** (1 paper: [Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models](https://aclanthology.org/2025.emnlp-main.1765.pdf))
> The task of identifying, for a given fact from a corpus, whether there exists at least one other fact within the same corpus that contradicts it.

**Contradiction checking** (1 paper: [Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective](https://aclanthology.org/2025.naacl-long.151.pdf))
> The observable behavior of detecting whether retrieved external knowledge contradicts the LLM's internal knowledge about a query.

**Contradiction detection** (2 papers: [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [FactTrack: Time-Aware World State Tracking in Story Outlines](https://aclanthology.org/2025.naacl-long.144.pdf))
> The observable behavior of identifying whether two sentences generated by a language model are logically inconsistent within a given context.

## Relationships

### Associated with
- **Knowledge conflict resolution** (construct), 1 paper
  > We introduce MICRO-ACT, a framework that enables Large Language Models (LLMs) to automatically identify and resolve detailed points of knowledge conflict. (Section 4)
  - [Micro-Act: Mitigate Knowledge Conflict in Question Answering via Actionable Self-Reasoning](https://aclanthology.org/2025.acl-long.909.pdf)
