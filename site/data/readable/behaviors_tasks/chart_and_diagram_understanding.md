# Chart and diagram understanding
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Chart interpretation, Chart understanding, Chart reasoning, Data extraction, Information positioning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as interpreting charts, plots, or graphs and extracting information from them, often with some reasoning over the displayed data. Some descriptions make the task broader by emphasizing answering questions about charts or deriving insights from visual data representations, including visual and logical reasoning over charts. A narrower strand defines success as locating specific values, labels, time ranges, legends, or color mappings, and one paper explicitly notes that annotators verify references to chart elements such as trends, labels, and time ranges.

**Variants.** Papers use several nearby labels, most often chart understanding and chart interpretation, with smaller variants called chart reasoning, information positioning, and data extraction. The studied settings range from general charts and plots to financial charts such as K-line, line, bar, and pie charts, with one paper also naming candlestick chart analysis, and to charts used for scientific insights. Some work narrows the behavior to query-based retrieval of chart elements, while another variant focuses on extracting legend values and handling color mappings.

**Space of elicitation and scores.** Papers link this behavior to 5 measurement instruments: AI2D, CharXiv, ChartQA, MMC, and MathVista. Several are explicitly presented as benchmarks that include chart understanding, MathVista is described as an evaluation suite whose benchmarks are designed to test chart understanding, and CharXiv is presented as a measure of progress on chart understanding.

**What it is taken as evidence of.** Across the papers, no construct is linked to this behavior, so the papers do not specify a broader construct that it is taken to evidence.

## Sources

**Chart interpretation** (2 papers: [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [VisFinEval: A Scenario-Driven Chinese Multimodal Benchmark for Holistic Financial Understanding](https://aclanthology.org/2025.emnlp-main.1229.pdf))
> The task of extracting and reasoning about data presented in graphical charts.

**Chart understanding** (4 papers: [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf), [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf), [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895.pdf), [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf))
> Interpreting charts or plots and extracting information from them.

**Chart reasoning** (1 paper: [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf))
> Interpreting and deriving insights from visual data representations like graphs and charts.

**Data extraction** (1 paper: [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf))
> The latent capability to accurately perceive and retrieve numerical, categorical, or textual information from visual representations like legends and color mappings.

**Information positioning** (1 paper: [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf))
> Locating and extracting specific data points or elements from a chart based on a query, such as values, labels, or time ranges.

## Relationships

### Chart and diagram understanding →
- **ChartQA** (measurement instrument): *measured_by*, 1 paper
  > 2) OCR/document/chart understanding: OCRBench (Liu et al., 2023f), DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022); (Section 2.1)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **CharXiv** (measurement instrument): *measured_by*, 1 paper
  > We hope that CharXiv facilitates future research on MLLM chart understanding by providing a more realistic and faithful measure of progress. (Abstract)
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MathVista** (measurement instrument): *measured_by*, 1 paper
  > Many benchmarks in the popular MathVista evaluation suite [60] are designed to test chart understanding. (Sec 1)
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AI2D** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks that involve spatial understanding and fine-grained features include ... chart understanding (AI2D; Kembhavi et al. 2016)... (Section 5)
  - [Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf)
- **MMC** (measurement instrument): *measured_by*, 1 paper
  > The models are tested across seven benchmarks: ...MMC (chart understanding)... (Section 3)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
