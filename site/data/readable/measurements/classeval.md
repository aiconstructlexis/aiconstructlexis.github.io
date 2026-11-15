# ClassEval
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the surveyed papers, the dominant framing is of a benchmark for object-oriented, class-level code generation. Definitions describe it as assessing object-oriented programming skills and class-level code generation abilities, and some descriptions add that it is a manually crafted collection of 100 class-level Python code generation tasks. Papers also describe it as containing 100 standalone programming tasks from seven domains, and one evaluation setup further specifies 100 classes, 410 methods, an average of 33 tests per class, and 8 tests per method.

**What it is claimed to measure.** Papers use it to measure one behavioral indicator, code generation, and do not link it to any constructs. The prevailing claim is specifically class-level code generation: papers state that they evaluate code LLMs on class-level code generation using ClassEval and list it with other benchmarks for code generation, so the reported measurement role converges on that single indicator rather than spreading across multiple targets.

**Space of uses.** In use, papers usually place it within broader benchmark suites, listing it alongside LiveCodeBench, BigCodeBench, HumanEval, MBPP, and DevEval. Papers also position it as prior work in code evaluation and as an evaluation set for code LLMs when assessing class-level generation.

## Sources

**ClassEval** (3 papers: [ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation](https://aclanthology.org/2025.acl-long.494.pdf), [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf), [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf))
> Benchmark designed to assess object-oriented programming skills and class-level code generation abilities.

## Relationships

### → ClassEval
- **Code generation** (behavioral indicator): *measured_by*, 2 papers
  > We evaluate code LLMs on class-level code generation using ClassEval [13], a collection of 100 class-level Python code generation tasks, covering 100 classes and 410 methods, with an average of 33 tests per class and 8 tests per method. (Section 3.2)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
