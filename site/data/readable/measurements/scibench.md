# SciBench
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across the papers, SciBench is most commonly described as a benchmark suite for scientific reasoning or college-level scientific problem solving. Most definitions emphasize complex, multi-step scientific questions, and one paper says the objective is to answer questions that require integrating knowledge, reasoning over evidence, and applying scientific principles (Fleet of Agents: Coordinated Problem Solving with Large Language Models). Subject coverage is described differently across papers, with some referring to physics, chemistry, and biology, another to physics, chemistry, and mathematics, and another focusing on a math-related subset with calculus, differential equations, and statistics.

**What it is claimed to measure.** Across the papers, SciBench is linked to three constructs and three behavioral indicators. The prevailing construct link is scientific reasoning, while smaller lines of work report it as measuring chemical reasoning and out-of-distribution generalization; on the behavioral side, papers use it for mathematical problem solving, scientific problem solving, and scientific question answering. These measurement claims therefore span several labels rather than one single wording, and one paper explicitly uses SciBench as a benchmark from a "totally different distribution compared to training data" to verify generalization.

**Space of uses.** Papers do not link SciBench to any other measurement instrument. In use, it commonly appears as one benchmark within broader evaluation suites, for example alongside Game of 24, Mini-Crosswords, WebShop, MATH, and TheoremQA, and one definition describes it as a source dataset for synthesis and evaluation. Some papers narrow to subsets of the benchmark, either four chemical reasoning datasets or a math-related subset covering calculus, differential equations, and statistics.

## Sources

**SciBench** (6 papers: [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf), [ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.808.pdf), [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf), [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf), [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf), [SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02ee6b7295f720407b56c457b34c54d5-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark suite for scientific reasoning that includes complex, multi-step questions across physics, chemistry, and biology.

## Relationships

### → SciBench
- **Scientific reasoning** (construct): *measured_by*, 2 papers
  > Tree-Search policy which are compared on college-level scientific reasoning benchmark under three LLMs, such as CoT and ToT, as shown in Table 4. We also evaluated under the same search budget on MATH and SciBench
  - [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > We applied MACM to two datasets, SciBench [16] and TheoremQA [5], which claim their difficulty surpasses the middle school level of the MATH dataset, reaching the Undergraduate Level. (Section 4.3)
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **Chemical reasoning** (construct): *measured_by*, 1 paper
  > Our experiments are conducted on four chemical reasoning datasets from SciBench (Wang et al., 2024a) with GPT-3.5, GPT-4 (OpenAI et al., 2024), and open-source models like Llama3 (Llama Team, 2024).
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
- **Scientific question answering** (behavioral indicator): *measured_by*, 1 paper
  > SciBench (Wang et al., 2024a) is a benchmark suite of scientific reasoning tasks, where the objective is to answer complex, multi-step scientific questions that require integrating knowledge, reasoning over evidence, and applying scientific principles. (Section 4.4. SciBench)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Scientific problem solving** (behavioral indicator): *measured_by*, 1 paper
  > SciBench (Wang et al., 2024a) assesses college-level scientific problem-solving abilities. (Section 4.2)
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
