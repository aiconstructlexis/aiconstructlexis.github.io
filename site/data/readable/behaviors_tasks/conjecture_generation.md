# Conjecture generation
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Formal conjecture generation  

## State of the Field

**Space of definitions.** The defining paper treats this as a formal mathematical task: proposing new, related, and solvable conjectures from existing seed theorems and proofs. One source also describes it as producing "novel conjectures or exercises," often as variants of known results, and attempting to solve them. In that usage, the required output is explicitly not just new, but also related to prior material and solvable.

**Variants.** The cited work names the behavior "formal conjecture generation" and places it in a setting built around seed theorems, proofs, and generated conjectures. The wording also extends to exercises and to variants of known results. One paper further describes an iterative version in which the conjecturer is trained on previously generated conjectures that are "barely provable by the current prover," so the generated conjectures become increasingly challenging over time.

**Space of elicitation and scores.** No measurement instrument is linked to it, and the papers do not specify an instrument that elicits or scores it.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not explicitly treat it as evidence of a construct. Instead, papers report only related links to other behaviors: conjecture generation is related to formal theorem proving, and code generation is related to conjecture generation in a discussion of mathematical discovery and program synthesis.

## Sources

**Formal conjecture generation** (1 paper: [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf))
> The observable task of proposing new, related, and solvable mathematical statements (conjectures) based on existing seed theorems and proofs.

## Relationships

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > Conjecture generation is a crucial component in current evolutionary approaches to mathematical discovery... The basic idea is that because computer code is more interpretable than raw ML predictions, one can use an LLM to generate (human-interpretable) code that solves a mathematical task. This is often known as program synthesis. (Section 5).
  - [Machine Learning meets Algebraic Combinatorics: A Suite of Datasets Capturing Research-level Conjecturing Ability in Pure Mathematics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chau25a/chau25a.pdf)
- **Formal theorem proving** (behavioral indicator), 1 paper
  > “The conjecturer is trained iteratively on previously generated conjectures that are barely provable by the current prover, which incentivizes it to generate increasingly challenging conjectures over time.”
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
