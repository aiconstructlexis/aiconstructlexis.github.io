# OlympiadBench
**Type:** Measurement instrument  
**Supporting papers:** 37  
**Also known as:** Olympiad Bench, Olympiad  

## State of the Field

**What it is.** Definitions split between two recurring descriptions: one line portrays it as an Olympiad-level benchmark for challenging mathematics problems, spanning high-school, college-level, and competition material, while another describes a bilingual multimodal version with 8,476 problems from Olympic-level mathematics and physics competitions. Across both descriptions, papers say it assesses advanced mathematical reasoning, and the multimodal framing adds high-level visual and logical reasoning. One paper also shortens the name to Olympiad and describes a challenging mathematical problem-solving dataset aimed at advanced reasoning and proof-like capabilities.

**What it is claimed to measure.** Papers link it to 3 constructs and 2 behavioral indicators. The most common use is to measure Mathematical reasoning, while smaller strands use it to measure Reasoning and Generalization; papers also report it as measuring Mathematical problem solving and Scientific problem solving. Overall, the reported targets spread across several reasoning-related abilities, but they most often center on mathematical reasoning.

**Space of uses.** Across evaluations, it is commonly used alongside MATH or MATH500, GSM8K, AIME 2024, AMC 2023, and College Math. Most papers position it as a harder benchmark within broader math suites, describing it as an advanced task, a more challenging dataset, or part of benchmarks of increasing difficulty. Some papers explicitly use it to test out-of-distribution performance or generalizability, and multimodal work reports results on the bilingual multimodal form.

## Sources

**Olympiad Bench** (3 papers: [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.843.pdf), [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf), [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf))
> Benchmark containing high-school and college-level mathematics problems from olympiad competitions, assessing advanced mathematical reasoning.

**Olympiad** (1 paper: [Fixing Distribution Shifts of LLM Self-Critique via On-Policy Self-Play Training](https://aclanthology.org/2025.acl-long.865.pdf))
> Challenging mathematical problem-solving dataset designed to assess advanced reasoning and proof-like capabilities.

**OlympiadBench** (4 papers: [Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning](https://aclanthology.org/2025.acl-long.257.pdf), [MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf), [Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs](https://aclanthology.org/2025.emnlp-main.75.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> Bilingual multimodal benchmark featuring 8,476 problems tailored to Olympic-level mathematics and physics competitions, assessing high-level visual and logical reasoning.

## Relationships

### → OlympiadBench
- **Mathematical reasoning** (construct): *measured_by*, 9 papers
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1068.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > To assess generalizability of our models to out-of-distribution problems, we evaluate on two additional benchmarks: MMLU-Pro Math (Wang et al., 2024b) and Olympiad Bench (He et al., 2024). (Section 4.1).
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We evaluate our method on a diverse set of reasoning tasks, including GSM8K (Cobbe et al., 2021b), MATH500 (Hendrycks et al., 2021), MMLU STEM (Hendrycks et al., 2020), OlympiadBench (He et al., 2024), GaoKao-2023-En (Liao et al., 2024), GPQA (Rein et al., 2023), and Minerva Math (Lewkowycz et al., 2022). (Section 3)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Scientific problem solving** (behavioral indicator): *measured_by*, 1 paper
  > scientific problems, including OlympiadBench (Olympiad) (He et al., 2024). (Section 4.1)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > Performance is evaluated on MATH500 (Lightman et al., 2023), Minerva Math (Lewkowycz et al., 2022), OlympiadBench (He et al., 2024), College Math (Tang et al., 2024) 3, AIME24, and AMC23 (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
