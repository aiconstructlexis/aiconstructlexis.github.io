# Structured reasoning
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Structural reasoning  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats structured reasoning as a latent ability to carry out organized, explicit, multi-step reasoning while respecting formal or structural constraints. Most definitions emphasize step-wise decomposition, multi-step dependencies, or graph-like reasoning paths, and some add the use of external structured evidence or semantically rich knowledge. A smaller line of work narrows the construct to particular settings such as planning, text assessment, navigation, biological perturbation reasoning, or microservice call-graph generation, and definitions differ on whether it is framed as an internal reasoning capacity or as the ability to produce outputs that satisfy structural constraints such as valid DAGs and temporal ordering.

**Space of facets.** Papers describe structured reasoning through explicit reasoning structures. It appears as sequences of causally linked steps, graphs of interconnected reasoning steps, divergent reasoning with retrieved knowledge in a graph-like framework, and structural chain-of-thought forms such as multi-chain, tree, and graph reasoning. The terminology is not fully uniform: some authors use "structural reasoning" for non-linear tree or graph paths and constraint-adhering generation, while others use "structured reasoning" for formal, step-wise, and graph-based reasoning.

**Space of measurement.** In linked operationalizations, papers connect structured reasoning to 1 measurement instrument, the Abstraction and Reasoning Corpus, and no behavioral indicators. ARC is used as a benchmark and is described as "designed as a benchmark for human-like structured reasoning." The only linked operationalization is therefore benchmark-based; no linked human evaluation, LLM-as-a-judge, probe, or behavioral indicator appears.

**Links.** Several papers claim a causal relationship from structured reasoning to interpretability and explainability. Their recorded evidence says structured reasoning has been explored to enhance explainability, and that explicitly encoding reasoning steps makes verification "interpretable and executable." Papers also report that causal reasoning is related to structured reasoning through graphs of interconnected steps that draw on causality theory, and that program synthesis ability is related to structured reasoning in work describing programming by example as a general paradigm for structured reasoning and data transformation tasks.

## Sources

**Structured reasoning** (4 papers: [Leveraging Environment Interaction for Automated PDDL Translation and Planning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/44af065477781e7f8a8589b14a62c489-Paper-Conference.pdf), [STRICTA: Structured Reasoning in Critical Text Assessment for Peer Review and Beyond](https://aclanthology.org/2025.acl-long.1107.pdf), [GIVE: Structured Reasoning of Large Language Models with Knowledge Graph Inspired Veracity Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25o/he25o.pdf), [FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models](https://aclanthology.org/2025.emnlp-main.338.pdf))
> The ability to reason in a way that respects formal constraints and multi-step dependencies in planning problems.

**Structural reasoning** (2 papers: [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf), [Large Language Models as Realistic Microservice Trace Generators](https://aclanthology.org/2025.emnlp-main.4.pdf))
> The ability to follow and generate complex, non-linear reasoning paths, such as those structured as trees or graphs.

## Relationships

### Structured reasoning →
- **Interpretability and explainability** (construct): *causes*, 2 papers
  > To enhance the accuracy and explainability of natural language reasoning, structured reasoning has been frequently explored as an alternative. (Introduction)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1549.pdf)
- **Abstraction and Reasoning Corpus** (measurement instrument): *measured_by*, 1 paper
  > As one example, consider the Abstraction and Reasoning Corpus (ARC) [14], which was designed as a benchmark for human-like structured reasoning.
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)

### Associated with
- **Causal reasoning** (construct), 1 paper
  > STRICTA breaks down the assessment into a graph of interconnected reasoning steps drawing on causality theory (Pearl, 1995).
  - [STRICTA: Structured Reasoning in Critical Text Assessment for Peer Review and Beyond](https://aclanthology.org/2025.acl-long.1107.pdf)
- **Program synthesis ability** (construct), 1 paper
  > Beyond grid puzzles, PBE is a general paradigm for structured reasoning and data transformation tasks
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
