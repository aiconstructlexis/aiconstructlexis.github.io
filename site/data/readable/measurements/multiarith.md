# MultiArith
**Type:** Measurement instrument  
**Supporting papers:** 36  
**Also known as:** Multi-Arith  

## State of the Field

**What it is.** Across papers, MultiArith is most commonly described as a benchmark dataset of arithmetic word problems, often grade-school or general math word problems that require multiple operations or multi-step reasoning. Some definitions frame it more broadly as a quantitative or mathematical reasoning dataset, and one paper describes it as a subset of MAWPS containing multi-step mathematical word problems. A few papers add corpus details, reporting either a data size of 600 or a split of train: 420 and test: 180.

**What it is claimed to measure.** Papers link MultiArith to 2 constructs, Mathematical reasoning and Robustness, and to 1 behavioral indicator, Mathematical problem solving. The prevailing usage is to measure Mathematical reasoning, with papers using it to verify mathematical reasoning capacity or assess arithmetic reasoning tasks. A smaller line of work uses it to measure Robustness through out-of-domain evaluation, and it is also used to measure Mathematical problem solving on general benchmark suites.

**Space of uses.** No measurement instrument is linked to it. In practice, papers usually evaluate MultiArith alongside GSM8K and, in smaller benchmark suites, SVAMP, AddSub, SingleEq, and AQuA. Authors variously position it as a standard arithmetic benchmark, as a transfer check for prompts optimized on GSM8K, as a distribution-shift or out-of-distribution dataset, and in one study as the in-distribution dataset for mathematical reasoning.

## Sources

**MultiArith** (13 papers: [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf), [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf), [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [AdaDHP: Fine-Grained Fine-Tuning via Dual Hadamard Product and Adaptive Parameter Selection](https://aclanthology.org/2025.acl-long.467.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf), [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf), [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf), [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf))
> A dataset containing arithmetic word problems used to evaluate quantitative reasoning.

**Multi-Arith** (1 paper: [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf))
> A benchmark dataset for evaluating arithmetic reasoning on problems that require multiple operations.

## Relationships

### → MultiArith
- **Mathematical reasoning** (construct): *measured_by*, 14 papers
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > For mathematical reasoning, we assess model robustness on three out-of-domain (OOD) benchmarks: ... and (3) MultiArith (Section 4.1).
  - [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf)
