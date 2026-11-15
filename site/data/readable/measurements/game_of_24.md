# Game of 24
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** Game 24, Game24  

## State of the Field

**What it is.** Across papers, Game of 24 is most commonly described as a mathematical reasoning benchmark in which a model or agent must combine four given numbers with basic arithmetic operations to produce an expression or equation that evaluates to 24. Definitions usually add that each of the four numbers is used exactly once, and one paper identifies it as a task from 4nums.com. A smaller line of work also frames it as a reasoning and search benchmark, a planning benchmark, or a mathematical puzzle, and papers refer to it as Game of 24, Game 24, or Game24.

**What it is claimed to measure.** Papers link it to five constructs and two behavioral indicators. The prevailing usage is as a measure of mathematical reasoning, and other papers use it to measure reasoning, planning, decision-making, and logical reasoning. Among behavioral indicators, papers use it to measure mathematical problem solving, while one paper relates it to self-verification by stating that verification is easier than solving on problems such as Game of 24. Overall, the measurement claims are spread across several reasoning-oriented targets rather than centered on only one.

**Space of uses.** Papers do not link it to another measurement instrument, but they often evaluate it alongside GSM8K and MATH as part of broader reasoning evaluations. Some also use it with WebShop and ToolBench for decision-making evaluations, or place it among other reasoning problems with formal notions of correctness. Several papers position it as a problem with well-defined rules and transition dynamics, and one paper describes it as particularly useful when verification is easier than solving.

## Sources

**Game of 24** (3 papers: [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf), [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf), [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf))
> A mathematical reasoning and search benchmark in which an agent must combine four numbers with arithmetic operations to obtain 24.

**Game 24** (1 paper: [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf))
> A mathematical reasoning benchmark where the goal is to form an equation that evaluates to 24 using a given set of integers.

**Game24** (1 paper: [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf))
> Planning and reasoning benchmark where models must use four numbers and basic arithmetic operations to reach 24, evaluating combinatorial search and planning ability.

## Relationships

### → Game of 24
- **Mathematical reasoning** (construct): *measured_by*, 5 papers
  > Besides, we include a challenging mathematical reasoning task, Game of 24 Yao et al. (2024), where the goal is to use four numbers and basic arithmetic operations (addition, subtraction, multiplication, and division) to obtain 24 in 1 equation. (Section 4)
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **Reasoning** (construct): *measured_by*, 3 papers
  > We study Game of 24 (Yao et al., 2023), a reasoning problem where the transition dynamics and rules are well-defined and readily available.
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
  - [On the self-verification limitations of large language models on reasoning and planning tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3c5e56274140e0420baa3916c529210-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 3 papers
  > The task is that given four cards drawn from a deck of poker, use basic arithmetic operations to combine the card values to reach 24.
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Planning** (construct): *measured_by*, 2 papers
  > To illustrate these limitations, we conducted experiments using the Game of 24, a simple yet illustrative planning problem with a depth of 3 and a maximum breadth of 48. (Section 3.2)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
- **Decision-making** (construct): *measured_by*, 1 paper
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > the performance comparison on the Game of 24 validates the effectiveness of the FoT in the mathematical and logical reasoning task. (Section 4.6)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)

### Associated with
- **Self-verification** (behavioral indicator), 1 paper
  > It is particularly useful for problems where verification is significantly easier than solving the problem itself, e.g., the Game of 24 (Yao et al., 2024). (Section 2.2)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
