# MAWPS
**Type:** Measurement instrument  
**Supporting papers:** 29  
**Also known as:** mawps  

## State of the Field

**What it is.** Across papers, the dominant framing is MAWPS as a benchmark or dataset of math word problems, often described as arithmetic problems in natural language for evaluating arithmetic or mathematical reasoning; one paper further describes it as consisting of 2,373 elementary-level math word problems. A smaller set of definitions describes it as an out-of-distribution or out-of-domain benchmark repository, one definition says it categorizes and standardizes arithmetic word problems from other datasets, and one paper reports average results over SingleEQ, SingleOP, AddSub, and MultiArith under the collective term MAWPS.

**What it is claimed to measure.** Papers use MAWPS to measure 2 constructs and 1 behavioral indicator. The prevailing claim is that it measures Mathematical reasoning, with papers describing it as a math reasoning or arithmetic reasoning benchmark; less commonly, it is reported as measuring In-context learning and Mathematical problem solving, so the claims are concentrated on Mathematical reasoning rather than spread across many targets.

**Space of uses.** No other measurement instrument is linked to it, but papers commonly evaluate MAWPS alongside GSM8K and SVAMP, and also MATH, AQuA, and ASDiv, usually as one part of a broader suite of math benchmarks. Some papers position it more specifically as an out-of-distribution or out-of-domain evaluation, using MAWPS to test further generalization or reasoning ability beyond the training distribution.

## Sources

**MAWPS** (6 papers: [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/b84b9d1fe05c5e74d8f9466f063327a5-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf), [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [Superficial Self-Improved Reasoners Benefit from Model Merging](https://aclanthology.org/2025.emnlp-main.301.pdf))
> A benchmark dataset of math word problems designed to test a model's ability to solve arithmetic problems.

**mawps** (1 paper: [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf))
> An out-of-distribution benchmark repository of math word problems.

## Relationships

### → MAWPS
- **Mathematical reasoning** (construct): *measured_by*, 8 papers
  > We evaluate our models on popular math reasoning benchmarks, namely GSM8K, MATH, GSM-Hard [24], SVAMP [28], TabMWP [29], ASDiv [30], and MAWPS [31]. (Section 3.2)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > Second, GSM8K [9], MaWPS [33] are about math problem solving. (Section 4.1)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > We evaluate DiffuLLaMA’s math reasoning and in-context learning ability by evaluating on MAWPS (Koncel-Kedziorski et al., 2016) (Section 4.2).
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
