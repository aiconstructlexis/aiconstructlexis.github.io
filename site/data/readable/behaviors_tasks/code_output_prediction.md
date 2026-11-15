# Code output prediction
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Output prediction, Execution reasoning, Code execution prediction  

## State of the Field

**Space of definitions.** The prevailing usage treats this as a code reasoning task where the goal is to predict the final output or result of executing code from the program and its inputs. Definitions largely agree on output prediction as the core criterion, while a smaller framing broadens it to execution reasoning that also includes inferring inputs from outputs. Some papers explicitly cast the task as simulation: one says output prediction requires the model to "simulate a compiler" (Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment), and another describes verbally simulating execution by tracking each line, executed lines, variable changes, and the final output (SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning).

**Variants.** Papers use several closely related labels, including output prediction, execution reasoning, and code execution prediction. The main variants are predicting outputs from code and inputs, and a less common inverse form that infers inputs from outputs. Benchmark-linked task names include CRUXEval-O for output prediction, CRUXEval-I for input prediction, and the code execution task in LiveCodeBench.

**Space of elicitation and scores.** It is measured by two instruments: CRUXEval and LiveCodeBench. CRUXEval is used through its code-understanding tasks CruxEval-O and, in broader execution-reasoning setups, CruxEval-I; LiveCodeBench is used through its code execution task, LCB-Exec. Across these papers, measurement therefore operationalizes the behavior as output prediction, input prediction, or code execution on benchmark tasks.

**What it is taken as evidence of.** No construct is linked to it, so papers do not explicitly state what broader construct this behavior indicates.

## Sources

**Output prediction** (1 paper: [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf))
> Predicting the final output of a program given the program and its inputs.

**Execution reasoning** (1 paper: [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf))
> The observable task of predicting program outputs given inputs or inferring inputs given outputs, often involving step-by-step simulation.

**Code execution prediction** (1 paper: [CodeIO: Condensing Reasoning Patterns via Code Input-Output Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25t/li25t.pdf))
> The observable task of predicting the final output or result of executing a given piece of code.

## Relationships

### Code output prediction →
- **CRUXEval** (measurement instrument): *measured_by*, 3 papers
  > two code-understanding tasks—namely, CruxEval-I (input prediction) and CruxEval-O (output prediction) from CruxEval benchmark [6] (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **LiveCodeBench** (measurement instrument): *measured_by*, 1 paper
  > "For execution reasoning, we employ CRUXEval [37] and the code execution task in LiveCodeBench (LCB-Exec for short) [18]."
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
