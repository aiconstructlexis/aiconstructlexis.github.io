# Problem-solving ability
**Type:** Construct  
**Supporting papers:** 28  
**Also known as:** Problem-solving, Generalized problem solving, Complex problem solving, Problem-solving capability, Number puzzle solving, Multimodal problem solving  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats problem-solving ability as a broad capability to solve complex or unfamiliar tasks by devising and executing a strategy toward a goal or correct answer. Many definitions keep this general, describing the capacity to handle challenging situations, solve tasks across disciplines, or be "capable of generalized problem solving as humans do." A smaller line of work narrows the term to competitive mathematics that requires non-trivial insight, to tool-aided task solving, or to multimodal settings where text and images must be integrated, and some authors define it more directly through benchmark performance, distinguishing it from data generation ability and from error detection.

**Space of facets.** Papers do not present a single formal taxonomy, but they do use adjacent labels such as generalized problem solving, problem-solving capability, and multimodal problem solving. The construct is frequently positioned alongside reasoning-focused concepts: algorithmic reasoning is said to play a role in problem-solving, and mathematical reasoning is described as a benchmark for advanced reasoning and problem-solving abilities. Some papers also separate it from neighboring capacities, treating it as different from data generation ability and, when a gold answer is provided, from error detection.

**Space of measurement.** It is linked to 4 measurement instruments and 2 behavioral indicators. The measurement space is centered on question-based benchmarks, with MMLU used most often, followed by MMLU-Pro, MathQA, and PutnamBench; papers describe these as gauging general problem-solving across diverse subjects, testing real-world text understanding and complex problem solving, testing numerical reasoning in word problems, and requiring broad mathematical proficiency. These operationalizations mostly treat the construct as success on challenging tasks, while some definitions frame it more as devising and executing a solution strategy.

**Links.** Papers also link the construct to 3 constructs and 2 behavioral indicators. One paper claims a causal relationship from self-improvement to problem-solving ability, describing post-training self-improvement as enhancing problem-solving capabilities, and the same line of work also claims a causal relationship from self-correction to problem-solving ability, while noting that post-prompting strategies are limited by intrinsic self-correction capabilities. Separately, one paper reports that error localization is weakly correlated with problem-solving ability, and papers describe algorithmic reasoning and mathematical reasoning as related to it.

## Sources

**Problem-solving** (4 papers: [PUZZLES: A Benchmark for Neural Algorithmic Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e5d1eaadeed651ba1021c09149db4b92-Paper-Datasets_and_Benchmarks_Track.pdf), [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf), [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf), [DIDS: Domain Impact-aware Data Sampling for Large Language Model Training](https://aclanthology.org/2025.emnlp-main.215.pdf))
> The ability to devise and execute a strategy to move from an initial state to a desired goal state, particularly in complex and unfamiliar domains.

**Problem-solving ability** (4 papers: [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf), [Evaluating Language Models as Synthetic Data Generators](https://aclanthology.org/2025.acl-long.320.pdf), [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf), [LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.553.pdf))
> The general capability to solve complex problems, particularly those found in competitive mathematics that require non-trivial insight.

**Generalized problem solving** (1 paper: [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf))
> The broad capacity to solve unfamiliar problems across settings rather than relying on narrow memorized patterns.

**Problem-solving capability** (1 paper: [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf))
> The general ability of an LLM to solve complex tasks effectively, especially when aided by external tools.

**Multimodal problem solving** (1 paper: [Can Large Language Models Win the International Mathematical Games?](https://aclanthology.org/2025.emnlp-main.488.pdf))
> Solving problems that require integrating information from both text and images, such as interpreting diagrams to compute geometric properties.

## Relationships

### Problem-solving ability →
- **MMLU** (measurement instrument): *measured_by*, 3 papers
  > MMLU (Hendrycks et al., 2021) Problem-solving across disciplines. (Table 2)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **PutnamBench** (measurement instrument): *measured_by*, 1 paper
  > PUTNAMBENCH requires significant problem-solving ability and proficiency in a broad range of topics taught in undergraduate mathematics courses.
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > MMLU-Pro: An enhanced version of the Massive Multitask Language Understanding (MMLU) benchmark, featuring challenging questions across 14 categories like physics, law, history, and so on to test real-world text understanding and complex problem solving (Section 2.2)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **MathQA** (measurement instrument): *measured_by*, 1 paper
  > It consists of questions that test numerical reasoning and problem-solving skills, requiring models to both understand the text of a word problem and perform mathematical operations to arrive at the correct solution. (Section 3.2.1)
  - [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf)

### → Problem-solving ability
- **Self-improvement** (construct): *causes*, 1 paper
  > Self-improvement through post-training methods such as iterative preference learning has been acclaimed for enhancing the problem-solving capabilities (e.g., mathematical reasoning) of Large Language Models (LLMs) without human intervention. (ABSTRACT)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > ...post-prompting strategies are limited by the model’s intrinsic self-correction capabilities, thereby failing to significantly enhance problem-solving capabilities. (Section 2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Error localization** (behavioral indicator): *correlates*, 1 paper
  > A chi-squared test for independence confirms that error localization and problem-solving accuracy are weakly correlated (p > 0.01; ϕ < 0.2) across models and prompts (Section 4.2)
  - [LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.553.pdf)

### Associated with
- **Algorithmic reasoning** (construct), 1 paper
  > Algorithmic reasoning is a fundamental cognitive ability that plays a pivotal role in problem-solving and decision-making processes. (Abstract)
  - [PUZZLES: A Benchmark for Neural Algorithmic Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e5d1eaadeed651ba1021c09149db4b92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > Mathematical reasoning has emerged as a critical benchmark to measure the advanced reasoning and problem-solving abilities of the Large Language Models (LLMs) (Section 1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
