# JudgeBench
**Type:** Measurement instrument  
**Supporting papers:** 9  

## State of the Field

**What it is.** Across the papers, JudgeBench is usually presented as a benchmark for evaluating LLM-based judges on challenging or difficult response pairs, and one definition also describes it as testing the robustness and accuracy of LLM-as-a-Judge systems across challenging evaluation cases. The prevailing description says it spans knowledge, reasoning, mathematics, and coding, and one definition adds that it uses responses from strong models like GPT-4o. Smaller descriptions frame it more generally as challenging questions for various reasoning tasks, or as an additional case study for judge behavior and agreement under uncertainty.

**What it is claimed to measure.** Papers link JudgeBench to three constructs and no behavioral indicators. The most common claim is that it measures factuality: papers say its focus is on evaluating the factual and logical correctness of complex responses to challenging questions, and they note that it includes response pairs involving factual correctness. A smaller line of work treats it as measuring reasoning, through difficult response pairs that require advanced reasoning abilities, and evaluation ability, through challenging response pairs spanning knowledge, reasoning, math, and coding.

**Space of uses.** In use, papers relate JudgeBench to four other instruments, namely LiveBench, LiveCodeBench, MMLU-Pro, and RewardBench. One paper describes its knowledge category with MMLU-Pro, its reasoning and mathematics categories with LiveBench, and its coding category with LiveCodeBench, while another paper positions it as a complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning. Other papers include it in broader benchmark suites and as an additional case study for judge behavior and agreement under uncertainty.

## Sources

**JudgeBench** (4 papers: [Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf), [Crowd Comparative Reasoning: Unlocking Comprehensive Evaluations for LLM-as-a-Judge](https://aclanthology.org/2025.acl-long.252.pdf), [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf), [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://aclanthology.org/2025.emnlp-main.138.pdf))
> A benchmark referenced as an additional case study for evaluating judge behavior and agreement under uncertainty.

## Relationships

### → JudgeBench
- **Factuality** (construct): *measured_by*, 2 papers
  > the focus of JudgeBench is on evaluating the factual and logical correctness of complex responses to challenging questions. (Figure 1)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
  - [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://aclanthology.org/2025.acl-long.775.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > we introduce JudgeBench, a benchmark designed to evaluate LLM-based judges on difficult response pairs that require advanced reasoning abilities. (Section 1)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Evaluation ability** (construct): *measured_by*, 1 paper
  > JudgeBench is a recent benchmark that evaluates LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. (Section 3)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)

### Associated with
- **MMLU-Pro** (measurement instrument), 1 paper
  > We use MMLU-Pro for the Knowledge category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **LiveBench** (measurement instrument), 1 paper
  > For the Reasoning and Mathematics categories, we use the corresponding LiveBench datasets. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **LiveCodeBench** (measurement instrument), 1 paper
  > LiveCodeBench is a contamination-free dataset for coding tasks, containing over 300 challenging questions sourced from coding contests like LeetCode, AtCoder, and Codeforces. We select this dataset for the Coding category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **RewardBench** (measurement instrument), 1 paper
  > Thus, JudgeBench offers a valuable complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning. (Section 4.3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
