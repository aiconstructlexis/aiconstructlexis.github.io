# CodeContests
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** CodeContests dataset, CodeContest  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats CodeContests as a benchmark dataset for competitive programming and code generation, commonly described as featuring challenging code competition problems. Some definitions further specify that each problem includes multiple human-written correct and incorrect solutions, while others describe it as requiring a code solution from a problem specified in natural language together with public test case descriptions. Papers also note variant uses, including splitting test problems into basic and advanced levels by difficulty tag and evaluating on selected subsets.

**What it is claimed to measure.** Papers most often use CodeContests to measure code generation, the most frequently linked behavioral indicator, and it is also linked to coding. On the construct side, papers report it as measuring algorithmic reasoning and functional correctness, so the claims span 2 behavioral indicators and 2 constructs. The linked targets remain tightly code-focused, with one paper placing it among complex algorithmic reasoning tasks and another describing evaluation against private test cases to check execution correctness.

**Space of uses.** No other measurement instrument is linked to it in papers. Papers usually place it within larger evaluation suites alongside HumanEval, MBPP, APPS, LiveCode, and Leetcode, and describe it as a popular or competitive benchmark in those comparisons. One paper additionally uses the CodeContests dataset as the source distribution for a code generation task.

## Sources

**CodeContests** (3 papers: [SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf), [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf), [RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gehring25a/gehring25a.pdf))
> A benchmark dataset featuring challenging programming problems from code competitions.

**CodeContests dataset** (1 paper: [Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf))
> A competitive programming dataset containing problems with multiple human-written correct and incorrect solutions, used as the source distribution (Dsrc) for the code generation task.

**CodeContest** (1 paper: [DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation](https://aclanthology.org/2025.acl-long.589.pdf))
> A benchmark dataset for code generation that includes test problems divided into basic and advanced levels based on their difficulty tags.

## Relationships

### → CodeContests
- **Code generation** (behavioral indicator): *measured_by*, 5 papers
  > “For Dsrc, we chose the CodeContests dataset (Li et al., 2022), a competitive programming problem dataset where each problem comes with multiple correct and incorrect solutions.”
  - [Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
  - [Improving Diversity in Language Models: When Temperature Fails, Change the Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verine25a/verine25a.pdf)
- **Algorithmic reasoning** (construct): *measured_by*, 1 paper
  > complex algorithmic reasoning tasks, such as those found in competitive programming benchmarks like CodeContests
  - [What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf)
- **Coding** (behavioral indicator): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Functional correctness** (construct): *measured_by*, 1 paper
  > Generated codes are evaluated against (private) test cases to check the execution correctness (Hendrycks et al., 2021; Chen et al., 2021; Li et al., 2022) (Section 3.1).
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
