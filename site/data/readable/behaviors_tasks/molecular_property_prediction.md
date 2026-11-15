# Molecular property prediction
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Functional group detection, Molecular toxicity prediction, Property prediction, Pharmaceutical property prediction  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is a prediction task on a given molecule: models take molecular inputs such as structure, graph, description, or string representations like SMILES and produce a chemical, physical, or biological property of that molecule. Most formulations use regression or classification outputs, for example continuous physical properties, toxicity, blood-brain barrier penetration, or assay labels, while some also treat a textual property description as a valid output. One line of work explicitly separates computed property prediction, scored by extracting a numerical value from generated text, from descriptive property prediction, scored with text similarity against ground truth; a narrower formulation recasts the behavior as yes or no functional group detection.

**Variants.** Variants span regression for continuous physical properties, classification for molecule labels, ADMET-style pharmaceutical prediction, quantum-property tasks around orbital energies and the HOMO-LUMO gap, and yes or no functional group detection. Some authors also distinguish 3D-dependent from 3D-independent settings, and papers sometimes use broader names such as property prediction or narrower toxicity-focused versions.

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments. MoleculeNet is the more common instrument and is described as a benchmark for molecular property prediction tasks, while QM9 appears as a dataset for computed property prediction. For scoring, one paper uses MAE after extracting a predicted numerical value from generated text for computed variants, and text similarity metrics for descriptive variants. In elicitation, one paper claims a causal relationship from Chain of thought to molecular property prediction, saying that Chain-of-Thought improves reasoning ability by decomposing complex SMILES processing into stepwise sub-tasks.

**What it is taken as evidence of.** The papers do not explicitly treat molecular property prediction as evidence of any linked construct, so they do not state a shared view of what broader construct this behavior reflects.

## Sources

**Molecular property prediction** (6 papers: [3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf), [Representations Shape Weak-to-Strong Generalization: Theoretical Insights and Empirical Predictions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xue25d/xue25d.pdf), [Molecular String Representation Preferences in Pretrained LLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.56.pdf), [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf), [Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d346d91999074dd8d6073d4c3b13733b-Paper-Conference.pdf), [Exploiting Edited Large Language Models as General Scientific Optimizers](https://aclanthology.org/2025.naacl-long.270.pdf))
> The task of generating a numerical value or a textual description for a specific chemical or physical property of a given molecule.

**Functional group detection** (1 paper: [Hierarchical Graph Tokenization for Molecule-Language Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cf/chen25cf.pdf))
> Determining whether a specific functional group (e.g., hydroxide, carboxylic acid) is present in a given molecular structure, typically in response to a yes/no question.

**Molecular toxicity prediction** (1 paper: [UniTox: Leveraging LLMs to Curate a Unified Dataset of Drug-Induced Toxicity from FDA Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/16659e412de3965fa195ddb9f2c4b356-Paper-Datasets_and_Benchmarks_Track.pdf))
> Predicting drug toxicity from molecular structure using machine learning models trained on UniTox labels.

**Property prediction** (1 paper: [LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf))
> The task of predicting specific numerical chemical or physical properties of a molecule, such as orbital energies.

**Pharmaceutical property prediction** (1 paper: [A new framework for evaluating model out-of-distribution generalisation for the biochemical domain](https://proceedings.iclr.cc/paper_files/paper/2025/file/b84adff45775e92a45f0cd87c37f5ce9-Paper-Conference.pdf))
> The task of predicting biophysical attributes of small molecules, such as their absorption, distribution, metabolism, excretion, and toxicity (ADMET).

## Relationships

### Molecular property prediction →
- **MoleculeNet** (measurement instrument): *measured_by*, 5 papers
  > We evaluate SMI-EDITOR on the MoleculeNet (Wu et al., 2017) benchmark and compare its performance with baseline models. (Section 4.2)
  - [SMI-Editor: Edit-based SMILES Language Model with Fragment-level Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b750c4189f19d0cd71375e9e17f83f-Paper-Conference.pdf)
  - [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf)
  - [ExLM: Rethinking the Impact of $\texttt[MASK]$ Tokens in Masked Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25q/zheng25q.pdf)
  - [Molecular String Representation Preferences in Pretrained LLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.56.pdf)
  - [Pre-trained Models Perform the Best When Token Distributions Follow Zipf's Law](https://aclanthology.org/2025.emnlp-main.1421.pdf)
- **QM9** (measurement instrument): *measured_by*, 1 paper
  > We use three datasets to evaluate the performance of 3D-MolT5 on computed property prediction task: QM9 (Ruddigkeit et al., 2012; Fang et al., 2023), PubChemQC (Maho, 2015; Xu et al., 2021), and PubChem (Kim et al., 2019).
  - [3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf)

### → Molecular property prediction
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > Chain-of-Thought (CoT) improves the reasoning ability of LLMs in molecular property prediction by decomposing complex SMILES data processing into stepwise sub-tasks, overcoming the limitations of direct question-answering approaches. (Section 3.3)
  - [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf)
