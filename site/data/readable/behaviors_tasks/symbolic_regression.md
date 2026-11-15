# Symbolic regression
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** In the usage in the papers, symbolic regression is treated as a search task over compact or succinct programmatic mathematical expressions that explain a dataset of input-output examples. The formulations in the same paper make success depend on producing a programmatic hypothesis that is compact and that best explains the dataset, including hypotheses written in a flexible, domain-specific programming language. As one study puts it, the task is to find "succinct programmatic hypotheses" that "best explain a dataset" (Symbolic Regression with a Learned Concept Library).

**Variants.** The papers mostly keep a single task name, symbolic regression, often abbreviated as SR, rather than splitting it into named sub-tasks. One paper frames the hypothesis space as a flexible, domain-specific programming language, and another paper relates symbolic regression to code generation by formulating SR as a program synthesis problem. A separate discussion also places SR in settings that seek transparent models in fields such as physics, biology, and finance.

**Space of elicitation and scores.** No measurement instrument is linked to symbolic regression. In the papers, it is operationalized through the task description itself, namely searching for compact or succinct programmatic hypotheses that best explain a dataset, rather than through a named instrument.

**What it is taken as evidence of.** The links do not present symbolic regression as a direct indicator of multiple constructs. Instead, it is related to a single construct, Interpretability and explainability: one paper states that SR's flexibility allows it to achieve "both high accuracy and interpretability" and describes this as useful where transparent, understandable models are sought. Beyond that related claim, the papers do not show alternative construct linkages.

## Sources

**Symbolic regression** (1 paper: [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf))
> The task of searching for a compact, programmatic mathematical expression that best explains a given dataset of input-output examples.

## Relationships

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > We formulate symbolic regression (SR) as a program synthesis [6] problem. (Section 2)
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **Interpretability and explainability** (construct), 1 paper
  > This flexibility allows SR to achieve both high accuracy and interpretability, making it especially valuable in fields such as physics (Udrescu et al., 2020), biology (Brunton et al., 2016), and finance (Liu & Guo, 2023), where uncovering transparent, understandable models is crucial for scientific discovery and informed decision-making.
  - [RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a8e70828c01059631f913442ae31e6-Paper-Conference.pdf)
