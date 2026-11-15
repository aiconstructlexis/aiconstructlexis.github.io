# NL4OPT
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** NL4Opt, NLP4OPT  

## State of the Field

**What it is.** Across the papers, closely related labels, NL4OPT, NL4Opt, and NLP4OPT, are used for what is most commonly described as a benchmark or benchmark dataset for turning natural language optimization problems into mathematical formulations. The prevailing description emphasizes question text in natural language, named entity recognition to extract entities and numerical values, and subsequent formulation into mathematical models. A narrower description presents it as a curated set of 244 linear programming problems used to evaluate autoformulation systems, while a smaller framing describes it as a dataset from the NL4Opt competition for solving optimization problems described in natural language.

**What it is claimed to measure.** Papers mainly use NL4OPT to evaluate whether models can construct or extract optimization formulations from natural language descriptions or questions. In that usage, it is reported as assessing named entity and numerical value extraction as part of formulating mathematical models, and a narrower description limits the task to linear programming autoformulation. Papers do not link it to named constructs or behavioral indicators.

**Space of uses.** In the quoted uses, NL4OPT appears mostly in multi-benchmark or multi-dataset evaluations. It is used alongside MAMO, IndustryOR, OptiBench, and OptMATH-Bench in one evaluation setup, where it is described as one of several established modeling benchmarks, and elsewhere it is included among collected optimization problem datasets and among real-world optimization and operation task datasets used for experiments.

## Sources

**NL4OPT** (2 papers: [OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3deb687c44d3687ace0729e5db3b4efd-Paper-Conference.pdf), [OptMATH: A Scalable Bidirectional Data Synthesis Framework for Optimization Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25o/lu25o.pdf))
> A benchmark that evaluates a model's ability to construct mathematical formulations from natural language questions, focusing on named entity recognition to extract entities and numerical values.

**NL4Opt** (1 paper: [LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf))
> A dataset from the NL4Opt competition focused on leveraging LLMs to solve optimization problems described in natural language.

**NLP4OPT** (1 paper: [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf))
> A benchmark dataset consisting of 244 linear programming problems described in natural language, used to evaluate autoformulation systems.
