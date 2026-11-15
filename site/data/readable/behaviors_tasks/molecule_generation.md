# Molecule generation
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Molecular generation, Multi-conditional molecular generation, Molecule synthesis  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats molecule generation as producing a molecular structure or representation from a prompt, objective, natural-language description, or chemical context. Outputs are most often described as SMILES or SELFIES strings, though some papers use molecular graphs, and some papers make novelty explicit. Success is sometimes framed more narrowly as generating valid or drug-like molecules, chemically valid and structurally coherent SELFIES, molecules with target properties, or graphs that satisfy multiple constraints such as property values and structural features.

**Variants.** Variants appear under several names, most often molecular generation or molecule generation, with smaller strands calling it molecule synthesis or multi-conditional molecular generation. Papers study text-based generation from an input description, generation from natural-language descriptions, protein-target-based generation for criteria such as binding affinity and drug-likeness, and autoregressive SMILES generation by sampling token sequences. Other settings emphasize SELFIES generation and the production of synthetic, natural product, or drug-like molecules.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, QM9. The only explicit measurement evidence says molecule generation is measured on the QM9 dataset, and no other instrument is linked.

**What it is taken as evidence of.** No paper links molecule generation to a construct, so the recorded relationships do not specify what construct this behavior is taken to indicate.

## Sources

**Multi-conditional molecular generation** (1 paper: [Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6739d8df16b5bce3587ca5f18662a6aa-Paper-Conference.pdf))
> The observable task of generating a molecular graph that simultaneously satisfies multiple constraints, such as specific property values and structural features.

**Molecular generation** (2 papers: [Efficient Evolutionary Search Over Chemical Space with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/804b5e300c9ed4e3ea3b073f186f4adc-Paper-Conference.pdf), [Beam Enumeration: Probabilistic Explainability For Sample Efficient Self-conditioned Molecular Design](https://proceedings.iclr.cc/paper_files/paper/2024/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf))
> The task of producing novel molecular structures, often represented as SMILES or SELFIES strings, based on a given prompt or objective.

**Molecule generation** (4 papers: [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf), [LIDDIA: Language-based Intelligent Drug Discovery Agent](https://aclanthology.org/2025.emnlp-main.603.pdf), [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf), [Domain-Agnostic Molecular Generation with Chemical Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed7dd1e32cf9b0abf664bf0e891527e5-Paper-Conference.pdf))
> Generating a molecular representation from a prompt or chemical context.

**Molecule synthesis** (1 paper: [Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf))
> The task of generating valid molecular structures in a specified format, such as SMILES, based on examples.

## Relationships

### Molecule generation →
- **QM9** (measurement instrument): *measured_by*, 1 paper
  > The result of molecule generation on QM9 dataset.
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
