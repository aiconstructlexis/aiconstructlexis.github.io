# Problem solving
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Multi-task problem solving, Reasoning task solving, Real-world problem solving  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats problem solving as producing correct answers or solutions on benchmark tasks, often spanning commonsense, math, code, and other prompted tasks. Several definitions make correctness explicit, describing accuracy on diverse problems or on well-defined technical queries, while others define the behavior as devising and executing a sequence of steps or a program under constraints or examples. Smaller lines of work narrow it to structured logical or mathematical derivation, or to inductive reasoning in natural-language real-life scenarios such as item trading.

**Variants.** Papers use several labels for narrower settings, including multi-task problem solving for heterogeneous tasks across domains and question types, reasoning task solving for structured reasoning benchmarks, and real-world problem solving for abstract rules embedded in natural-language scenarios. The domains named around this behavior include commonsense, math, code, reasoning, coding, and communication, with some papers also singling out mathematical or logical problems and programming by example. In agentic settings, one paper relates problem solving to Task decomposition, describing a multi-stage procedure that begins by breaking a complex question into simpler steps, and another paper claims a causal relationship from Chain of thought to Problem solving by stating that intermediate reasoning steps can improve the final answer.

**Space of elicitation and scores.** Papers measure problem solving with 2 instruments: MMLU and Omni-MATH. MMLU is used for evaluating multi-task problem solving and is described as requiring diverse world knowledge and problem solving abilities. Omni-MATH is presented as a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing challenges to problem solving and complex reasoning.

**What it is taken as evidence of.** Papers link problem solving to 2 constructs, and both links are stated as related links rather than causal or measurement claims. One line relates it to Mathematical reasoning, with mathematical ability described as a measure of problem-solving and complex reasoning skills. Another relates it to Task generalization, where problem solving is examined alongside answerable judging, outcome judging, and process judging.

## Sources

**Problem solving** (3 papers: [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf))
> Producing correct answers to benchmark problems across commonsense, math, and code tasks.

**Multi-task problem solving** (1 paper: [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf))
> Solving a heterogeneous set of tasks spanning multiple domains and question types.

**Reasoning task solving** (1 paper: [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf))
> Completing structured problems requiring logical or mathematical derivation as part of general capability evaluation.

**Real-world problem solving** (1 paper: [MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b782a3462ee9d566291cff148333ea9b-Paper-Conference.pdf))
> An inductive reasoning task presented in a natural language format, where abstract rules are embedded within real-life scenarios like item trading.

## Relationships

### Problem solving →
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > MMLU (Hendrycks et al., 2021) for evaluating Multi-task Problem Solving (Section 4.2)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
  - [Organize the Web: Constructing Domains Enhances Pre-Training Data Curation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wettig25a/wettig25a.pdf)
- **Omni-MATH** (measurement instrument): *measured_by*, 1 paper
  > We introduce Omni-Math, a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing new challenges to the problem solving and complex reasoning capability of LLMs. (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)

### → Problem solving
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > Another line of work has shown that allowing LLMs to generate intermediate “reasoning” steps, or “chain-of-thoughts” (CoTs) can significantly improve their final answer (Wei et al., 2022; Nye et al., 2021; Zhou et al., 2023). (Section 5)
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)

### Associated with
- **Mathematical reasoning** (construct), 1 paper
  > Among these capabilities, mathematical ability serves as a fundamental measure of the problem-solving and complex reasoning skills of LLMs... (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Task generalization** (construct), 1 paper
  > horizontally, we examine the task generalization including problem solving, answerable judging, outcome judging, and process judging. (Section 1)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Task decomposition** (behavioral indicator), 1 paper
  > Solving real-world problems with LLM agents can be structured into a multi-stage procedure: • Decomposition of the problem: The procedure begins by breaking down a complex question into an actionable plan characterized by simpler steps. (Section 3).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
