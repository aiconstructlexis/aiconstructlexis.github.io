# Protein property prediction
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Fluorescence prediction, Stability prediction, Thermostability prediction, Solubility prediction, Metal ion binding prediction, Biophysical property prediction, Subcellular localization prediction, Mammalian cell expression prediction, Protein function prediction  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats the concept as predicting a protein property, label, or function from amino acid sequence. Most formulations are either continuous regression tasks, such as fluorescence intensity, thermostability, melting temperature, or optimal temperature for catalysis, or discrete prediction tasks, such as solubility, metal ion binding, mammalian cell expression, or cellular compartment. A smaller extension treats it as protein function prediction in a setting where experimentally verified annotations are unavailable during training and final evaluation follows a curation phase based on newly published functions. Where papers specify the prediction granularity, they describe sequence-level or protein-level outputs, and one paper explicitly reports stability as sequence-level regression measured by Spearman coefficient.

**Variants.** The variants are heterogeneous but remain sequence-based in their formulations. Common named variants include fluorescence, stability or thermostability, solubility, metal ion binding, and subcellular localization, with localization described as a protein-level label for compartments such as nucleus or extracellular space. Other named variants include mammalian cell expression in CHO cells, broader biophysical property prediction, and protein function prediction.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. Operationalization is described directly through task format: several papers use regression for fluorescence, stability or thermostability, and other biophysical properties, several use binary classification for solubility, metal ion binding, and mammalian cell expression, and one paper describes subcellular localization as a protein-level label. One paper also specifies sequence-level stability scoring with a Spearman coefficient.

**What it is taken as evidence of.** No construct is linked to this behavior as something it measures or indicates. The papers describe it through task definitions only, and do not record an explicit construct that it is taken to indicate.

## Sources

**Fluorescence prediction** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> A regression task to predict the fluorescence intensity of a protein.

**Stability prediction** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> A regression task to predict the thermostability of a protein.

**Thermostability prediction** (1 paper: [From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf))
> Predicting the melting temperature of a protein based on its sequence, used as a continuous regression task.

**Solubility prediction** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> A binary classification task to predict whether a protein will be soluble when expressed.

**Metal ion binding prediction** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> A binary classification task to determine whether a protein sequence binds to metal ions.

**Biophysical property prediction** (1 paper: [A new framework for evaluating model out-of-distribution generalisation for the biochemical domain](https://proceedings.iclr.cc/paper_files/paper/2025/file/b84adff45775e92a45f0cd87c37f5ce9-Paper-Conference.pdf))
> The task of predicting physical or chemical properties of proteins based on their sequence, such as the optimal temperature for catalysis.

**Subcellular localization prediction** (1 paper: [From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf))
> Predicting the cellular compartment (e.g., nucleus, extracellular space) where a protein is localized based on its sequence.

**Mammalian cell expression prediction** (1 paper: [From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf))
> A binary classification task to determine whether a given protein can be successfully expressed in a specific host cell line (e.g., Chinese hamster ovary cells).

**Protein function prediction** (1 paper: [Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sculley25a/sculley25a.pdf))
> Predicting the biological function of proteins based on their amino acid sequences, in the absence of experimentally verified annotations during training.
