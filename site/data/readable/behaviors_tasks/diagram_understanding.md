# Diagram understanding
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Diagram interpretation, Diagram comprehension, Diagram Understanding, Flowchart understanding, Scientific diagram analysis, Science diagram comprehension, Diagram and table interpretation  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats this behavior as interpreting a diagram and answering questions about its content. Several formulations further stress understanding the structure and meaning of diagram elements and their interrelations, and one paper characterizes the associated benchmark as targeting diagram interpretation and reasoning through syntactic parsing and semantic analysis. A smaller line broadens the scope beyond diagrams alone to other structured visuals, including charts, graphs, figures, and tables, while one paper places it within image recognition and reasoning cross capabilities.

**Variants.** Papers use several nearby names, including diagram interpretation, diagram comprehension, scientific diagram analysis, science diagram comprehension, flowchart understanding, and diagram and table interpretation. The variants most commonly stay with general, scientific, or schematic diagrams, while narrower settings focus on flowcharts, where questions target steps, decisions, or outcomes, for example asking which step is drawn with a diamond shape. Other variants extend the task to charts, graphs, technical illustrations, figures, and tables as broader structured visual formats.

**Space of elicitation and scores.** Papers measure this behavior with 4 instruments. AI2D is the most common, used to gauge diagram comprehension or understanding, and one paper describes it as a multiple-choice benchmark for science diagram comprehension. Smaller lines use MME-RealWorld for complex visual reasoning tasks that include diagrams, MMMU through sub-categories consisting exclusively of scientific diagrams, and MuirBench to evaluate the ability to understand information conveyed in diagram images.

**What it is taken as evidence of.** Papers rarely link this behavior to constructs. Only 1 construct is linked: Decision-making is related to diagram understanding in a flowchart setting, where one paper connects accurate interpretation of flowcharts to tasks such as automation, decision-making, and analysis. This link is framed as relatedness, not as a measurement, causal, or correlational claim.

## Sources

**Diagram interpretation** (1 paper: [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf))
> Interpreting the structure and meaning of diagram elements and their interrelations.

**Diagram comprehension** (1 paper: [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf))
> The observable task of understanding and answering questions about the content of a diagram.

**Diagram understanding** (1 paper: [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf))
> The task of interpreting and answering questions about scientific or schematic diagrams.

**Diagram Understanding** (1 paper: [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf))
> Interpreting visual diagrams as part of image recognition and reasoning cross capabilities.

**Flowchart understanding** (1 paper: [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf))
> Interpreting flowchart diagrams and answering questions about steps, decisions, or outcomes represented in the chart.

**Scientific diagram analysis** (1 paper: [Chain-of-region: Visual Language Models Need Details for Diagram Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/464012c83279e19be4cd42c25f341c92-Paper-Conference.pdf))
> The observable task of interpreting and answering questions about complex, structured images such as charts, graphs, and technical illustrations.

**Science diagram comprehension** (1 paper: [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf))
> The task of interpreting and answering questions about diagrams, charts, and figures from scientific contexts.

**Diagram and table interpretation** (1 paper: [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf))
> The task of extracting and understanding information presented in structured visual formats like diagrams, charts, and tables.

## Relationships

### Diagram understanding →
- **AI2D** (measurement instrument): *measured_by*, 4 papers
  > For domain-specific evaluations, we choose AI2D to gauge diagram comprehension (Section 5.2)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > [DIAGRAM UNDERSTANDING] aims to evaluate the ability of models to understand information conveyed in diagram images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > To align our research focus, we conduct experiments on several sub-categories of MMMU that consists exclusively of scientific diagrams (Section 4).
  - [Chain-of-region: Visual Language Models Need Details for Diagram Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/464012c83279e19be4cd42c25f341c92-Paper-Conference.pdf)
- **MME-RealWorld** (measurement instrument): *measured_by*, 1 paper
  > MME-RealWorld covers complex visual reasoning tasks derived from realistic applications across diverse domains (e.g., Autonomous Driving, Diagrams, OCR) (Section 4.1).
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)

### Associated with
- **Decision-making** (construct), 1 paper
  > Accurate interpretation of flowcharts is essential for tasks such as automation, decision-making, and analysis.
  - [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf)
