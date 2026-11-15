# Omni-MATH
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** Omini-MATH, OmniMath, Omni-Math  

## State of the Field

**What it is.** Most papers describe Omni-MATH as a mathematics or mathematical reasoning benchmark with diverse topics and a broad range of difficulty, often emphasizing Olympiad-level or olympiad-style problems. A smaller line of work frames it more specifically as a benchmark focused on mathematical olympiad challenges. Some evaluation setups use sampled versions of the benchmark, including Omni-MATH-500 or a random subset of the full dataset, for efficient assessment.

**What it is claimed to measure.** Across papers, Omni-MATH is linked to two constructs and one behavioral indicator. The prevailing usage is to measure mathematical reasoning, with several papers evaluating models on Omni-MATH as a math reasoning benchmark. A smaller line of work reports it as measuring complex reasoning and problem solving capability, so the measurement claims are concentrated on mathematical reasoning rather than spread widely across many targets.

**Space of uses.** Papers commonly use Omni-MATH alongside GSM8K, MATH, AIME, OlympiadBench, and GPQA in broader reasoning evaluations. It is usually positioned as one benchmark within multi-benchmark suites, often as a challenging or Olympiad-level component; some papers use sampled subsets for efficient yet comprehensive assessment, and one paper uses OmniMATH-derived data as a ProcessBench subset for step-wise error detection on reasoning traces.

**Concerns raised.** The recurring concern papers mention is the computational demand of evaluating the full benchmark. In response, some authors report randomly sampling questions or using Omni-MATH-500 to maintain efficiency.

## Sources

**Omni-MATH** (2 papers: [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf), [TreeRL: LLM Reinforcement Learning with On-Policy Tree Search](https://aclanthology.org/2025.acl-long.604.pdf))
> Omni-MATH is a mathematics benchmark covering a broad spectrum of difficulty levels for evaluating math reasoning models.

**Omini-MATH** (1 paper: [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](https://aclanthology.org/2025.acl-long.232.pdf))
> Mathematical reasoning dataset from which 500 randomly sampled questions were used to evaluate model performance efficiently.

**OmniMath** (3 papers: [FastMCTS: A Simple Sampling Strategy for Data Synthesis](https://aclanthology.org/2025.acl-long.1190.pdf), [Dyve: Thinking Fast and Slow for Dynamic Process Verification](https://aclanthology.org/2025.emnlp-main.1136.pdf), [Examining False Positives under Inference Scaling for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.632.pdf))
> A comprehensive mathematical reasoning benchmark covering diverse topics and difficulty levels, including olympiad-style problems.

**Omni-Math** (1 paper: [RBench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25r/guo25r.pdf))
> A benchmark focused on employing mathematical olympiad challenges to evaluate mathematical reasoning.

## Relationships

### → Omni-MATH
- **Mathematical reasoning** (construct): *measured_by*, 5 papers
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) (Omni-Math, 2024).
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
- **Problem solving** (behavioral indicator): *measured_by*, 1 paper
  > We introduce Omni-Math, a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing new challenges to the problem solving and complex reasoning capability of LLMs. (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Complex reasoning** (construct): *measured_by*, 1 paper
  > We introduce Omni-Math, a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing new challenges to the problem solving and complex reasoning capability of LLMs. (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
