# APPS
**Type:** Measurement instrument  
**Supporting papers:** 31  
**Also known as:** APPs  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats APPS as an algorithmic programming or code generation benchmark or dataset. Definitions usually describe natural language programming problems paired with test cases and solutions, often Python solutions, and several papers specify 10,000 problems split evenly between training and test sets across introductory, interview, and competition levels. Some authors instead foreground competitive programming, program synthesis, or code synthesis with public or hidden unit tests, and several evaluations use subsets such as 500 interview-level problems, 500 sampled test questions, or the competition split of 1,000 problems.

**What it is claimed to measure.** Papers most commonly use APPS to measure code generation, with smaller lines of work using it to measure code debugging and clarifying question generation. Papers link it to 3 behavioral indicators and 1 construct: code generation, code debugging, clarifying question generation, and functional correctness. The claims mostly converge on code generation, while the construct-level use is concentrated on functional correctness through execution against test cases.

**Space of uses.** No measurement instrument is linked to APPS. In practice, papers usually benchmark it alongside other code datasets, most often HumanEval, MBPP, CodeContests, Codeforces, and LiveCodeBench, and they position it as a main code evaluation benchmark or as an additional coding-domain check; some papers also report results with pass@k or pass@1. Several papers narrow it to specific settings, such as interview-level samples or competition-level challenges, when focusing evaluation on harder problems or limiting evaluation size.

## Sources

**APPS** (13 papers: [$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf), [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf), [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), [LLM-Assisted Code Cleaning For Training Accurate Code Generators](https://proceedings.iclr.cc/paper_files/paper/2024/file/41137f3997ade899893ccd3973592d4b-Paper-Conference.pdf), [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf), [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf), [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf), [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf), [GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852c8254bc6d904c09db9921157f59b-Paper-Datasets_and_Benchmarks_Track.pdf), [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf), [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf), [kGym: A Platform and Dataset to Benchmark Large Language Models on Linux Kernel Crash Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e9ed2a28af7d9085180e3817b2c9a57-Paper-Datasets_and_Benchmarks_Track.pdf))
> Algorithmic Programming Problems benchmark containing natural language problem descriptions and test cases for evaluating code generation systems.

**APPs** (1 paper: [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf))
> A programming benchmark used to evaluate code generation across problems of varying difficulty.

## Relationships

### → APPS
- **Code generation** (behavioral indicator): *measured_by*, 14 papers
  > In line with prior RL-based works (Le et al., 2022; Shojaee et al., 2023; Liu et al., 2023), we evaluate B-Coder on the challenging code contests benchmark APPS (Hendrycks et al., 2021). (Section 5)
  - [$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
  - [DeFT: Decoding with Flash Tree-attention for Efficient Tree-structured LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6df53f082619d02b9fad64a022e5de3-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [RethinkMCTS: Refining Erroneous Thoughts in Monte Carlo Tree Search for Code Generation](https://aclanthology.org/2025.emnlp-main.410.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
- **Code debugging** (behavioral indicator): *measured_by*, 2 papers
  > We evaluate our NL-DEBUGGING framework on two widely used code datasets: APPS (Hendrycks et al., 2021) and Codeforces (Team, 2024). (Section 4.1.1)
  - [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Clarifying question generation** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate all question-generating strategies on... the more challenging APPS (Hendrycks et al., 2021) benchmark with competition-level coding challenges
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
- **Functional correctness** (construct): *measured_by*, 1 paper
  > Generated codes are evaluated against (private) test cases to check the execution correctness (Hendrycks et al., 2021; Chen et al., 2021; Li et al., 2022) (Section 3.1).
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
