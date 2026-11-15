# FEVEROUS
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** Feverous  

## State of the Field

**What it is.** Across papers, FEVEROUS is most commonly described as a fact-verification or complex claim-verification dataset or benchmark built around mixed evidence. Definitions usually say it combines structured or semi-structured tables with unstructured text or sentences, often from Wikipedia, and several descriptions add complex or multi-hop reasoning, sometimes with evidence annotated at the sentence or table-cell level. A smaller line of work adapts it for open-domain table reasoning by restricting attention to table-only claims and framing the task as identifying relevant evidence tables.

**What it is claimed to measure.** Papers link FEVEROUS to 1 construct and 2 behavioral indicators. The prevailing use is to measure fact checking: papers describe it as a fact verification, claim verification, or fact-checking benchmark for deciding whether evidence supports or refutes claims. Smaller usages treat it as measuring table reasoning, through an open-domain adaptation, and entity disambiguation, through a reported FEVEROUS partition.

**Space of uses.** Papers do not link FEVEROUS to another measurement instrument. It is nevertheless used alongside other benchmarks, most commonly HOVER, and some papers also pair it with FEVER, Vitaminc, AVeriTeC, and SciFact. In those settings, authors usually position it as a benchmark for complex claim verification or fact verification.

## Sources

**FEVEROUS** (5 papers: [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf), [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf))
> FEVEROUS, a fact-verification dataset used here in an open-domain table reasoning setting requiring identification of relevant evidence tables.

**Feverous** (1 paper: [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf))
> A fact verification benchmark requiring models to verify claims using evidence from semi-structured tables and text, with complex reasoning.

## Relationships

### → FEVEROUS
- **Fact checking** (behavioral indicator): *measured_by*, 6 papers
  > FEVEROUS, on the other hand, is a fact-verification dataset that requires the identification of multiple relevant tables for reasoning and verifying factual questions.
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
  - [Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1295.pdf)
- **Table reasoning** (construct): *measured_by*, 1 paper
  > We adapted the dataset for open-domain table reasoning by filtering 323 examples from the validation set that rely solely on table data, using a corpus of 26,177 candidate tables from the FEVEROUS dataset.
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **Entity disambiguation** (behavioral indicator): *measured_by*, 1 paper
  > For consistency with prior work (Aly et al., 2021), we evaluate FEVEROUS claims on three key partitions: Multi-hop Reasoning, Entity Disambiguation, and Numerical Reasoning. (Section 4.1)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
