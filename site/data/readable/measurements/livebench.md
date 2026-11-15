# LiveBench
**Type:** Measurement instrument  
**Supporting papers:** 16  

## State of the Field

**What it is.** Across papers, the prevailing description is of a benchmark from Abacus AI that evaluates models on a large test set of questions with ground truth answers. Most descriptions stress a dynamic setup, with questions compiled from recent sources such as math competitions and the dataset updated periodically, while another description foregrounds coverage across data analysis, language, reasoning, math, instruction following, and coding and says it is built from periodically released exams and competitions to reduce contamination.

**What it is claimed to measure.** Papers use LiveBench to measure 4 constructs and 2 behavioral indicators. The linked constructs are Reasoning, Coding ability, Mathematical reasoning, and Natural language understanding, and the linked indicators are Data analysis and Instruction following; these measurement claims are spread across several capabilities named in papers' descriptions of the tasks.

**Space of uses.** Across papers, LiveBench is used alongside 6 other instruments. Papers report it as correlating with Arena-Hard, BIG-Bench Hard is related to it through harder, contamination-limited versions of earlier tasks, it is also reported to correlate with Chatbot Arena and HELM, and it is related to IFEval in the same earlier-task sense; one other benchmark uses the corresponding LiveBench datasets for reasoning and mathematics categories.

**Concerns raised.** The recurring concern in these descriptions is data contamination. Papers frame LiveBench as contamination-limited or as a dynamic benchmark that draws on recent sources and updates periodically to mitigate or reduce contamination.

## Sources

**LiveBench** (4 papers: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [DyCodeEval: Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ba/chen25ba.pdf), [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf), [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf))
> A benchmark from Abacus AI that evaluates models on a large test set of questions with ground truth answers.

## Relationships

### → LiveBench
- **Reasoning** (construct): *measured_by*, 2 papers
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)
- **Chatbot Arena** (measurement instrument): *correlates*, 1 paper
  > LiveBench has a 0.91 and 0.88 correlation with ChatBot Arena and Arena-Hard, respectively.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *correlates*, 1 paper
  > LiveBench has a 0.91 and 0.88 correlation with ChatBot Arena and Arena-Hard, respectively.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Coding ability** (construct): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **HELM** (measurement instrument): *correlates*, 1 paper
  > LiveBench and HELM are strongly correlated (Table 1).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator): *measured_by*, 1 paper
  > LiveBench (White et al., 2024) contains 6 problem categories: data analysis, language, reasoning, math, instruction following, and coding. (Section 4.2)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)

### Associated with
- **JudgeBench** (measurement instrument), 1 paper
  > For the Reasoning and Mathematics categories, we use the corresponding LiveBench datasets. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument), 1 paper
  > LiveBench... contains harder, contamination-limited versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **IFEval** (measurement instrument), 1 paper
  > LiveBench... contains harder, contamination-limited versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
