# FollowBench
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across the surveyed work, the dominant description is of a fine-grained constraint-following benchmark with five levels of difficulty, built from diverse, open-ended instructions and evaluated by strong LLMs such as GPT-4. Some authors frame it more specifically as a benchmark for complex, multi-constraint instruction-following tasks, while others describe it as covering more general instructions that require LLM-based judgment rather than simple code execution.

**What it is claimed to measure.** Papers link it to 3 constructs and 1 behavioral indicator. The prevailing use is to measure instruction following ability and complex instruction following ability, with instruction following also measured by it; one paper additionally uses it to measure generalization on more general instructions not verifiable by simple code executions. Overall, the recorded claims cluster around instruction following and its complex variant, with generalization appearing as a less common target.

**Space of uses.** Papers typically deploy it alongside other instruction-following benchmarks rather than on its own. It often appears with IFEval and CFBench, and also with ComplexBench, Multi-IF, and SysBench; papers position it as a widely-used or main benchmark for instruction-following, especially when the evaluation focuses on complex instructions with multiple constraints.

## Sources

**FollowBench** (3 papers: [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf), [MuSC: Improving Complex Instruction Following with Multi-granularity Self-Contrastive Training](https://aclanthology.org/2025.acl-long.523.pdf), [UltraIF: Advancing Instruction Following from the Wild](https://aclanthology.org/2025.emnlp-main.945.pdf))
> A fine-grained constraint-following benchmark with five levels of difficulty, containing diverse and open-ended instructions that require evaluation by strong LLMs.

## Relationships

### → FollowBench
- **Instruction following ability** (construct): *measured_by*, 2 papers
  > We evaluate our methods using two widely-used instruction-following benchmarks: IFEval (Zhou et al., 2023) and FollowBench (Jiang et al., 2024b) as main results (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Complex instruction following ability** (construct): *measured_by*, 2 papers
  > We mainly perform evaluations on three complex instruction-following benchmarks: CFBench (Zhang et al., 2024b), FollowBench (Jiang et al., 2024b) and ComplexBench (Wen et al., 2024) (Section 4.1).
  - [MuSC: Improving Complex Instruction Following with Multi-granularity Self-Contrastive Training](https://aclanthology.org/2025.acl-long.523.pdf)
  - [AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1628.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the trained models on several widely-used instruction-following benchmarks, including IFEval (Zhou et al., 2023), Multi-IF (He et al., 2024b), SysBench (Qin et al., 2024), FollowBench (Jiang et al., 2024), and CFBench (Zhang et al., 2024a). (Introduction)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > FollowBench is a fine-grained constraint-following benchmark with five levels of difficulty. It contains diverse and open-ended instructions requiring evaluation by strong LLMs, such as GPT-4, which can fully examine the generalization of AUTOIF to more general instructions not verifiable by simple code executions. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
