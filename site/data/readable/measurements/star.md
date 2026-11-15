# STAR
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, the prevailing usage treats STAR as a video question answering benchmark for situated or situational reasoning in real-world videos. Definitions commonly describe it as targeting reasoning about social interactions and events, and one description further says it contains questions about interaction, sequence, prediction, and feasibility. A smaller line of work also places it among multi-choice QA benchmarks and uses it as a source for referred video question answering.

**What it is claimed to measure.** Papers use STAR to measure 3 constructs and 1 behavioral indicator. The most common reported use is measuring video question answering, while individual papers also use it to measure causal reasoning, temporal reasoning, and visual reasoning. In those papers, STAR is described as part of datasets that demand both causal and temporal reasoning abilities, and as one of the datasets used for visual reasoning tasks, so construct claims are spread across several reasoning targets rather than concentrated on one construct.

**Space of uses.** Papers usually use STAR alongside other video question answering instruments, most often NExT-QA and IntentQA, and sometimes Egoschema; some authors specifically evaluate zero-shot video question answering on it. It is typically positioned as one component of a broader benchmark suite, including sets of popular benchmarks, collections of multi-choice QA benchmarks, and broader VideoQA evaluations. No measurement instrument is linked to it through a formal relationship.

## Sources

**STAR** (4 papers: [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A Video Question-Answering benchmark that requires situational reasoning about social interactions and events.

## Relationships

### → STAR
- **Video question answering** (behavioral indicator): *measured_by*, 3 papers
  > We evaluate ReasVQA on three popular benchmarks, and our results establish new state-of-the-art performance with significant improvements of +2.9 on NExT-QA, +7.3 on STAR, and +5.9 on IntentQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
- **Visual reasoning** (construct): *measured_by*, 1 paper
  > We demonstrate the effectiveness of our framework on diverse visual reasoning tasks from the ACRE, CATER, Something-Else and STAR datasets (Abstract).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **Causal reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
