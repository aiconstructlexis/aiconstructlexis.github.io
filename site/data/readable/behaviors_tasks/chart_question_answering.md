# Chart question answering
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Chart-based question answering, Figure question answering, Figure-based question answering  

## State of the Field

**Space of definitions.** A prevalent framing treats it as answering a natural language question using information contained in a chart, often by analyzing the visual chart and its underlying data, with the answer produced as a direct textual response that may be numerical, categorical, or textual. Closely related definitions broaden the task to figure question answering over figures, charts, plots, and diagrams, while some papers make the reasoning demand explicit by describing arithmetic, logical, or statistical processing over the visualized data, including multi-step visual and logical reasoning.

**Variants.** Papers use several nearby labels, including chart question answering, chart-based question answering, figure question answering, and figure-based question answering. The settings range from chart images to broader figures and diagrams, and from specific chart types such as bar, line, and pie charts to multiple charts and plots; some formulations place it within visual question answering, while another has an LLM answer questions about a generated chart in relation to user objectives.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, ChartQA. The linked claim presents it as "ChartQA (Masry et al., 2022) | Figure QA," which matches the broader figure question answering framing used in some papers.

**What it is taken as evidence of.** It is linked to 3 constructs, Reasoning, Multimodal perception, and Local reasoning, and all of these links are related-to claims rather than explicit measurement claims. The relationship language describes chart question answering as a multimodal task used to evaluate reasoning capabilities, especially multimodal perception ability and local reasoning ability.

## Sources

**Chart-based question answering** (1 paper: [AMACE: Automatic Multi-Agent Chart Evolution for Iteratively Tailored Chart Generation](https://aclanthology.org/2025.emnlp-main.1089.pdf))
> Generating textual responses to questions by analyzing a visual chart and its underlying data.

**Chart question answering** (2 papers: [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf))
> Generating answers to natural language questions based on information presented in a chart, including numerical, categorical, or textual responses.

**Figure question answering** (3 papers: [F2TEval: Human-Aligned Multi-Dimensional Evaluation for Figure-to-Text Task](https://aclanthology.org/2025.emnlp-main.195.pdf), [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf))
> Answering questions about information contained in a figure.

**Figure-based question answering** (1 paper: [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf))
> The task of answering questions that require interpreting data presented in figures, diagrams, or charts.

## Relationships

### Chart question answering →
- **ChartQA** (measurement instrument): *measured_by*, 1 paper
  > "ChartQA (Masry et al., 2022) | Figure QA"
  - [F2TEval: Human-Aligned Multi-Dimensional Evaluation for Figure-to-Text Task](https://aclanthology.org/2025.emnlp-main.195.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > "Chart question answering (CQA) has become a critical multimodal task for evaluating the reasoning capabilities of vision-language models."
  - [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf)
- **Multimodal perception** (construct), 1 paper
  > "Chart question answering (Ma et al., 2024; Qin et al., 2022) is a prominent multimodal task designed to evaluate the reasoning capabilities of vision-language models, especially their multimodal perception ability and local reasoning ability."
  - [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf)
- **Local reasoning** (construct), 1 paper
  > "Chart question answering (Ma et al., 2024; Qin et al., 2022) is a prominent multimodal task designed to evaluate the reasoning capabilities of vision-language models, especially their multimodal perception ability and local reasoning ability."
  - [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf)
