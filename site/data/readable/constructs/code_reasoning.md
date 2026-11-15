# Code reasoning
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Long-range sequential reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats code reasoning as a latent model ability centered on program execution and code behavior. Most definitions describe it as reasoning about how programs behave, including analyzing behavior, logic, and properties, and one paper says this requires understanding both syntactic and semantic aspects of code. Some authors describe the same construct through observable tasks, especially predicting a snippet's output from a given input or inferring inputs from a known output. A smaller framing emphasizes long-range sequential reasoning, the capacity to process procedural steps whose order affects the final semantic meaning.

**Space of facets.** Papers break the construct into task families such as execution reasoning, code repair, and fill-in-the-blank challenges, and into directional forms of predicting outputs versus inferring inputs. One paper explicitly relates it to logical reasoning, describing code reasoning as a category of tasks that incorporates logical reasoning into code. Another uses long-range sequential reasoning as a more specific facet of semantic understanding in programs where the order of operations matters.

**Space of measurement.** Operationally, papers link code reasoning to 1 measurement instrument and no behavioral indicators. The linked instrument is CRUXEval, described as a benchmark for code reasoning, understanding and execution; its tasks assess whether a model can reason about the execution of simple Python programs by predicting the input given the output of a function, and vice versa. This measurement targets execution reasoning and bidirectional input-output inference, two recurring elements in the definitions, while broader task families such as code repair and fill-in-the-blank are described without separate linked instruments.

**Links.** Beyond measurement, papers link code reasoning to 3 constructs. One paper reports it is related to logical reasoning, framing it as a category of tasks that incorporates logical reasoning into code. One paper claims a causal relationship from Planning to Code reasoning, stating that enhanced planning capability boosts model performance on code reasoning, and another claims a causal relationship from Code reasoning to Test generation ability, attributing weak test-suite coverage to models struggling to reason about execution.

## Sources

**Code reasoning** (3 papers: [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf), [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf), [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf))
> The latent ability to reason about program execution and code behavior.

**Long-range sequential reasoning** (1 paper: [Can Large Language Models Understand Symbolic Graphics Programs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf))
> The capacity to process and understand the procedural steps in a program where the order of operations significantly affects the final semantic meaning.

## Relationships

### Code reasoning →
- **CRUXEval** (measurement instrument): *measured_by*, 3 papers
  > These tasks assess the model’s ability to reason about the execution of simple Python programs by asking it to predict the input given the output of a function and vice-versa (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
- **Test generation ability** (construct): *causes*, 1 paper
  > models struggle to generate high-coverage test suites, with the best model, GPT-4o, achieving an average coverage of only 35.2%. This is primarily due to models struggling to reason about execution
  - [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf)

### → Code reasoning
- **Planning** (construct): *causes*, 1 paper
  > Furthermore, the enhanced planning capability gained through HLP boosts model performance on code reasoning. (Abstract)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)

### Associated with
- **Logical reasoning** (construct), 1 paper
  > “Code reasoning is a category of tasks that incorporates logical reasoning into code”
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
