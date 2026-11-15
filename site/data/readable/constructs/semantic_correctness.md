# Semantic correctness
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats semantic correctness as preservation of meaning between an input and a generated structured output. Most commonly, papers describe it as whether the output accurately reflects the meaning and intent of a natural language question or problem description, and one recurring formulation makes this explicit as holding regardless of syntactic form or execution result equivalence. Some authors cast it as a latent ability of the model, while others define it as the degree to which a generated representation or program preserves meaning, constraints, or operational behavior, so the main variation is model ability versus property of the produced artifact and the reference standard used.

**Space of facets.** Papers use nearby formulations such as semantic equivalence, semantic match, and preservation of operational meaning and behavior to express the construct. They also contrast it with parseability, solvability, and execution result equivalence: one formulation asks whether a generated query "accurately represents the intent" of the question under contextual information, while another reports outputs that are parseable and solvable but not semantically correct.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Even so, papers make the operationalization concrete by judging whether a generated query semantically matches a question under contextual information, and by reporting semantically correct outputs separately from other outcomes: one study reports 96.1% parseable PDDL, 94.4% solvable PDDL, and 24.8% semantically correct PDDL. These operationalizations track the definitions by focusing on semantic match and preserved meaning rather than syntactic form alone.

## Sources

**Semantic correctness** (3 papers: [Planetarium: A Rigorous Benchmark for Translating Text to Structured Planning Languages](https://aclanthology.org/2025.naacl-long.560.pdf), [FLEX: Expert-level False-Less EXecution Metric for Text-to-SQL Benchmark](https://aclanthology.org/2025.naacl-long.228.pdf), [Guess & Sketch: Language Model Guided Transpilation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e4996c14d3674b5ca5c318829290783-Paper-Conference.pdf))
> The latent ability of a model to generate SQL queries that accurately reflect the meaning and intent of a natural language question, regardless of syntactic form or execution result equivalence.
