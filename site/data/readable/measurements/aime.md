# AIME
**Type:** Measurement instrument  
**Supporting papers:** 19  

## State of the Field

**What it is.** Across definitions, papers most commonly treat AIME as the American Invitational Mathematics Examination, used as a benchmark or dataset for advanced mathematical reasoning or problem solving. It is also described as a challenging high school mathematics competition. Some papers specify particular slices rather than the exam in general: one uses the AIMO validation set with 90 questions from AIME 22, 23, and 24, another evaluates on AIME 2025, Parts I and II, and one reference describes AIME as 15 competition math problems.

**What it is claimed to measure.** Papers link AIME to two constructs and two behavioral indicators. The prevailing use is to measure mathematical reasoning, with several papers describing it as a math reasoning benchmark; it is also reported as measuring reasoning more generally. Among behavioral indicators, papers link it to mathematical problem solving and, in one paper, to chain of thought.

**Space of uses.** No measurement instrument is linked to it. In reported evaluations, papers usually place AIME in broader benchmark suites alongside Omni-MATH, MATH, GPQA, math500, and gsm8k, and they commonly position it as a challenging or widely used benchmark for mathematical reasoning; one paper uses AIME 24 specifically in a chain-of-thought reasoning evaluation.

## Sources

**AIME** (3 papers: [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](https://aclanthology.org/2025.acl-long.232.pdf), [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf), [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf))
> American Invitational Mathematics Examination benchmark used to assess advanced mathematical problem-solving abilities with 90 validation questions from AIME 22, 23, and 24.

## Relationships

### → AIME
- **Mathematical reasoning** (construct): *measured_by*, 3 papers
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We also extend experiments on two more challenging reasoning benchmarks, GPQA (Rein et al., 2024) and AIME (Mathematical Association of America, 2024), further verifying the generality of our findings and methods. (Section 8)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > "Other benchmarks relevant to today’s frontier models include AIME with 15 competition math problems"
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **Chain of thought** (behavioral indicator): *measured_by*, 1 paper
  > We assess both models on the challenging American Invitational Mathematics Examination (AIME 24) benchmark. (Section 3.3, Chain-of-Thought Reasoning Evaluation).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
