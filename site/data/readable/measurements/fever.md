# FEVER
**Type:** Measurement instrument  
**Supporting papers:** 30  

## State of the Field

**What it is.** Across papers, FEVER is most commonly described as a fact verification benchmark or dataset of human-written claims about Wikipedia, paired with evidence from Wikipedia and labeled as Supported, Refuted, or NotEnoughInfo, though one definition gives the third label as neutral. Several papers present it under the full name Fact Extraction and VERification, while smaller usages describe it as a fact-checking task, a natural language inference benchmark, a KILT subset task, or a closed-book fact verification dataset. One paper further describes it as a large-scale resource with 185,000 annotated claims.

**What it is claimed to measure.** The prevailing usage is to treat FEVER as measuring fact checking: across papers it is linked to one behavioral indicator, Fact checking, and to no constructs. This matches the dominant framing of FEVER as a fact-checking or fact verification task, usually cast as three-class claim classification with evidence. Some papers also describe it as testing world knowledge and factuality, and one paper uses it for factual consistency.

**Space of uses.** Papers commonly use FEVER as an evaluation task: one study says it uses FEVER 'for all our experiments and comparison against previous methods,' and others report the standard three-class accuracy scheme for fact verification tasks. It also appears inside broader task collections, including the KILT subset, question-answering evaluations, and a RAG fine-tuning mixture with NQ, WoW, and MMLU. Across papers, FEVER is related to one other instrument, BEIR, through a paper that lists FEVER among BEIR's public datasets.

**Concerns raised.** One paper reports a robustness concern, stating that analysis using FEVER reveals that LLMs are brittle to small input changes (FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models).

## Sources

**FEVER** (14 papers: [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf), [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf), [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf), [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf), [Emergent Response Planning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25p/dong25p.pdf), [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf), [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf))
> The Fact Extraction and VERification (FEVER) benchmark is a dataset for fact verification, consisting of claims that need to be classified as Supported, Refuted, or NotEnoughInfo based on evidence from Wikipedia.

## Relationships

### → FEVER
- **Fact checking** (behavioral indicator): *measured_by*, 10 papers
  > We use the FEVER (Thorne et al., 2018) dataset for all our experiments and comparison against previous methods. (Section 4.1)
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
  - [AgentPro: Enhancing LLM Agents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.506.pdf)
  - [Adversarial Attacks Against Automated Fact-Checking: A Survey](https://aclanthology.org/2025.emnlp-main.1171.pdf)

### Associated with
- **BEIR** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... FEVER (Thorne et al., 2018)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
