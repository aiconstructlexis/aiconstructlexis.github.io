# ProofWriter
**Type:** Measurement instrument  
**Supporting papers:** 13  

## State of the Field

**What it is.** Across the surveyed work, the prevailing framing is a deductive or logical reasoning benchmark, sometimes called a dataset, for logical inference over written or natural language rules and facts. Definitions variously describe first-order logic rules, small rule-bases composed of facts and rules, and tasks that determine whether a query can be proved, including multi-step deduction and proof construction under a closed-world assumption. Some papers emphasize generating natural language proofs for conclusions, while others highlight moderately complex logical structures such as conjunctions and disjunctions. A smaller strand refers to the ProofWriter family, which includes Birds-Electricity and ParaRules.

**What it is claimed to measure.** Papers use ProofWriter mainly to measure Logical reasoning, and the relationship claims mostly converge there: it is linked to 2 constructs, with Logical reasoning the dominant one and Chain-of-thought reasoning appearing in a smaller line of work that treats it as a multi-step reasoning dataset. The definitions align with this usage by describing it as assessing deductive reasoning abilities, logical inference, and implication elimination. No behavioral indicators are linked to it.

**Space of uses.** In use, papers commonly place ProofWriter inside benchmark suites rather than alone, pairing it with PrOntoQA most explicitly, and also with LogicNLI, FOLIO, GPQA, and ASDiv in broader evaluations. Among linked instruments, papers connect it to 1 other instrument, PrOntoQA, and one paper reports that both datasets use predefined templates for generating logic and corresponding natural language. Papers position it both as a logical reasoning benchmark and, in some evaluations, as a representation of logical reasoning within mixed sets that also include arithmetic or symbolic reasoning.

**Concerns raised.** One paper raises a concern about high similarity to PrOntoQA, reporting an anomalous result in which a model finetuned on ProofWriter performs best on PrOntoQA and attributing this to both datasets using predefined templates for logic and corresponding natural language.

## Sources

**ProofWriter** (6 papers: [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf), [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf), [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf), [Collaborative Beam Search: Enhancing LLM Reasoning via Collective Consensus](https://aclanthology.org/2025.emnlp-main.574.pdf))
> A deductive reasoning benchmark used to evaluate logical inference over written rules and facts.

## Relationships

### → ProofWriter
- **Logical reasoning** (construct): *measured_by*, 7 papers
  > ProofWriter (Tafjord et al., 2020): A logical reasoning dataset that, in contrast to PrOntoQA, uses real concepts for all assumptions. (Section 4.1)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > We evaluate our framework on four multi-step reasoning datasets: FOLIO (Han et al., 2022), ProofWriter (Tafjord et al., 2020), MMLU-Pro (Wang et al., 2024c) and GPQA (Rein et al., 2023) (Section 4.1).
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)

### Associated with
- **PrOntoQA** (measurement instrument), 1 paper
  > “The model finetuned on ProofWriter achieves the highest performance on ProntoQA. This anomaly could be attributed to the high similarity between ProntoQA and ProofWriter: Both datasets utilize predefined templates for generating logic and corresponding natural language.”
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
