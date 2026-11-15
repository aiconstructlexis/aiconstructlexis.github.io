# Molecule captioning
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Molecular captioning, Molecular description generation, Molecule description generation, Molecule caption generation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats molecule captioning as generating a natural language description or caption from a molecular input, often a molecular structure. One paper states that "the input is a molecular structure and the model is expected to generate a corresponding description or annotation in natural language" (On LLM-Based Scientific Inductive Reasoning Beyond Equations). A smaller line of work broadens the target text to include names, or emphasizes that the generated text should accurately describe the molecule's properties, structure, and function.

**Variants.** Papers use several near-synonymous names for the same behavior, including molecule captioning, molecular captioning, molecule description generation, molecular description generation, and molecule caption generation. The task is studied with molecular structures or other molecular inputs, and some authors frame it as the inverse of another task, as a crossmodal alignment task, or as part of a context-aware model that integrates captioning with context embeddings.

**Space of elicitation and scores.** One measurement instrument is linked to this behavior: ChEBI-20. Papers use it to report performance on molecule description generation or molecule captioning, with one quote referring to "the performance of molecule captioning on ChEBI-20" and another describing ChEBI-20 as part of "testing the performance of molecule description generation."

**What it is taken as evidence of.** No construct is linked to it in the reported relationships, so the recorded relationships do not specify what construct it reflects.

## Sources

**Molecule captioning** (3 papers: [3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf), [On LLM-Based Scientific Inductive Reasoning Beyond Equations](https://aclanthology.org/2025.emnlp-main.476.pdf), [Towards 3D Molecule-Text Interpretation in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4af24e6ce753c181e703f3f0be3b5e20-Paper-Conference.pdf))
> The observable task of generating textual descriptions or names based on molecular input structures.

**Molecular captioning** (1 paper: [RetroInText: A Multimodal Large Language Model Enhanced Framework for Retrosynthetic Planning via In-Context Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2fbf1c9bc92e7ef2f6cab2e8a3e09af-Paper-Conference.pdf))
> The task of generating a natural language text description for a given molecule.

**Molecular description generation** (1 paper: [LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf))
> The task of generating a natural language text that accurately describes the properties, structure, and function of a given molecule.

**Molecule description generation** (1 paper: [Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d346d91999074dd8d6073d4c3b13733b-Paper-Conference.pdf))
> Producing textual descriptions of molecules from molecular inputs.

**Molecule caption generation** (1 paper: [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf))
> The task of generating a natural language description (caption) for a given molecular structure.

## Relationships

### Molecule captioning →
- **ChEBI-20** (measurement instrument): *measured_by*, 2 papers
  > For testing the performance of molecule description generation of LLaMo and previous models, we utilize ... both PubChem324k [3] and ChEBI-20 [8] for specialist models. (Appendix G)
  - [LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf)
  - [How to Make Large Language Models Generate 100% Valid Molecules?](https://aclanthology.org/2025.emnlp-main.1350.pdf)
