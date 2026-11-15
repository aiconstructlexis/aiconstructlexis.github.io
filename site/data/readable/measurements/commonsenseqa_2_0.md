# CommonsenseQA 2.0
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** CSQA2  

## State of the Field

**What it is.** Across these papers, the prevailing description is a dataset for commonsense reasoning. Definitions differ in emphasis: one describes CSQA2 as containing "a large number of questions about entity knowledge and commonsense reasoning," while another presents CommonsenseQA 2.0 as a dataset for evaluating commonsense reasoning through multiple-choice questions.

**What it is claimed to measure.** Papers link it to 2 constructs and no behavioral indicators. The most common claim is that it measures Commonsense reasoning, with papers using it within commonsense QA evaluations, while a smaller line of work also treats it as measuring Factual reasoning.

**Space of uses.** Papers use it as one dataset in broader evaluation suites. In a factual reasoning setup, it appears alongside CREAK and StrategyQA, and in a commonsense QA suite it appears with CommonsenseQA, OpenBookQA, ARC-Easy, and several other datasets described as widely utilized.

## Sources

**CSQA2** (1 paper: [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf))
> A dataset for commonsense reasoning containing a large number of questions.

**CommonsenseQA 2.0** (1 paper: [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf))
> A dataset used to evaluate commonsense reasoning capabilities through multiple-choice questions.

## Relationships

### → CommonsenseQA 2.0
- **Commonsense reasoning** (construct): *measured_by*, 2 papers
  > We evaluate our UniCoTT over CREAK (Onoe et al., 2021), StrategyQA (Geva et al., 2021) and CSQA2 (Talmor et al., 2021) datasets, which contain a large number of questions about entity knowledge and commonsense reasoning (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Factual reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments across three types of tasks: (1) Factual Reasoning Task. We evaluate our UniCoTT over CREAK (Onoe et al., 2021), StrategyQA (Geva et al., 2021) and CSQA2 (Talmor et al., 2021) datasets (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
