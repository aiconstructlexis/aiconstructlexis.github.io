# CollegeMath
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** College Math  

## State of the Field

**What it is.** Most descriptions frame CollegeMath as a college-level mathematical reasoning benchmark, often presented as a more challenging or out-of-domain evaluation set beyond high school material. Papers variously describe it as college-level math problems, advanced topics beyond the high school curriculum, or an out-of-domain benchmark for generalization; one description in DART-Math specifies 2,818 test problems drawn from 9 textbooks across 7 domains such as linear algebra and differential equations. A smaller line of description differs: Logits-Based Finetuning calls it "a mathematical reasoning dataset created using MathScale, containing two million math question-answer pairs."

**What it is claimed to measure.** Papers use CollegeMath mainly to measure mathematical reasoning. Across recorded relationships it measures 2 constructs and 1 behavioral indicator: mathematical reasoning is the prevailing target, while a smaller number of papers use it to measure generalization and mathematical problem solving. The reported measurement claims therefore center on reasoning, with only limited extension to other targets.

**Space of uses.** Papers typically use CollegeMath inside multi-benchmark evaluations, commonly alongside GSM8K, MATH or MATH500, and OlympiadBench, among other math benchmarks. It is usually positioned as a harder, college-level benchmark within suites that range from elementary or competition math up to Olympiad problems, and several papers explicitly use it for out-of-domain or generalization checks. Some papers also present it as one of a small number of especially challenging datasets for testing model performance on advanced or diverse mathematical problems.

## Sources

**CollegeMath** (4 papers: [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://aclanthology.org/2025.acl-long.367.pdf), [Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.745.pdf), [MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf), [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf))
> Out-of-domain benchmark assessing mathematical problem-solving at the college level, used to evaluate generalization beyond training data.

**College Math** (4 papers: [Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](https://aclanthology.org/2025.acl-long.658.pdf), [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf), [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> College-level mathematical reasoning benchmark assessing advanced topics beyond high school curriculum, used to evaluate out-of-domain generalization.

## Relationships

### → CollegeMath
- **Mathematical reasoning** (construct): *measured_by*, 11 papers
  > For mathematical reasoning, the performance is evaluated on the test set of MATH (Hendrycks et al., 2021b), GSM8K (Cobbe et al., 2021a), and College Math (Tang et al., 2024) by Accuracy. (Section 4.1)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf)
  - [Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning](https://aclanthology.org/2025.acl-long.417.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://aclanthology.org/2025.acl-long.367.pdf)
  - [Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](https://aclanthology.org/2025.acl-long.658.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.745.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > CollegeMath (Tang et al., 2024): This test set contains 2818 college-level mathematical problems extracted from 9 textbooks across 7 domains such as linear algebra and differential equations, testing generalization on complex mathematical reasoning in diverse domains. (Section 4.1)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > Performance is evaluated on MATH500 (Lightman et al., 2023), Minerva Math (Lewkowycz et al., 2022), OlympiadBench (He et al., 2024), College Math (Tang et al., 2024) 3, AIME24, and AMC23 (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
