# ARC-AGI
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across papers, ARC-AGI is most commonly described as the Abstraction and Reasoning Corpus, a grid-based benchmark where models infer a transformation rule from input-output examples and then produce the correct output for a new test grid. One definition says the original dataset contains 900 reasoning tasks. A smaller line of description refers to it more specifically as an ARC reasoning benchmark, a visual inductive reasoning benchmark, or a program synthesis benchmark designed to challenge core reasoning capabilities.

**What it is claimed to measure.** Papers link ARC-AGI to 7 constructs and no behavioral indicators. The prevailing use is to measure Reasoning and Generalization: papers describe it as designed to assess core knowledge and the ability to generalize in AI, and as a benchmark that challenges core reasoning capabilities. Other papers use it to measure Abstract reasoning, Core knowledge, and Inductive reasoning; overall, these claims are spread across several constructs rather than centered on one, with 2 additional construct links beyond these, one of them a related rather than measured_by connection.

**Space of uses.** No other measurement instrument is linked to it. Papers use ARC-AGI as the benchmark on which they verify effectiveness or report improvements, and they position it as a reasoning benchmark, a visual inductive reasoning benchmark, and, in one line of work, a testbed for program synthesis. One analysis also treats ARC tasks as "complex compositions of atomic operations for evaluation," connecting the benchmark to compositionality.

## Sources

**ARC-AGI** (1 paper: [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf))
> Abstraction and Reasoning Corpus (ARC-AGI), a benchmark of grid-based reasoning tasks where models infer a transformation rule from examples and produce the correct output for a test input.

## Relationships

### → ARC-AGI
- **Reasoning** (construct): *measured_by*, 3 papers
  > We demonstrate SOAR’s effectiveness on the Abstraction and Reasoning Corpus (ARC), a program synthesis benchmark specifically designed to challenge AI models’ core reasoning capabilities (Chollet, 2019).
  - [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pourcel25a/pourcel25a.pdf)
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
  - [Test-Time Training Provably Improves Transformers as In-context Learners](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gozeten25a/gozeten25a.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > The Abstraction and Reasoning Corpus (ARC-AGI), introduced by Chollet (2019) and designed to assess core knowledge and the ability to generalize in AI, exemplifies this difficulty. (Section 1)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Abstract reasoning** (construct): *measured_by*, 1 paper
  > The Abstraction and Reasoning Corpus (ARC-AGI) poses a significant challenge for large language models (LLMs), exposing limitations in their abstract reasoning abilities. (Abstract)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **Core knowledge** (construct): *measured_by*, 1 paper
  > The Abstraction and Reasoning Corpus (ARC-AGI), introduced by Chollet (2019) and designed to assess core knowledge and the ability to generalize in AI, exemplifies this difficulty. (Section 1)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **Inductive reasoning** (construct): *measured_by*, 1 paper
  > "We verify our pipeline’s effectiveness on the ARC visual inductive reasoning benchmark"
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **Program synthesis ability** (construct): *measured_by*, 1 paper
  > ARC was explicitly designed to resist pattern matching and require core reasoning, making it a strong testbed for program synthesis (Chollet, 2024).
  - [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pourcel25a/pourcel25a.pdf)

### Associated with
- **Compositionality** (construct), 1 paper
  > Therefore, we regard ARC tasks as complex compositions of atomic operations for evaluation. (Section 4.2)
  - [Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the ARC Task](https://aclanthology.org/2025.naacl-long.423.pdf)
