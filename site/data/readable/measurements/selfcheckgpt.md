# SelfCheckGPT
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** Self-CKGPT  

## State of the Field

**What it is.** Across papers, the prevailing description is a suite or method for hallucination detection: it samples multiple stochastic responses from a model and checks their consistency or support for the original answer to assess veracity, often in zero-resource black-box or gray-box settings. Some authors narrow this to a baseline for self-consistency or zero-resource fact-checking, and a smaller line of work instead describes it as a benchmark or dataset for hallucination correction, assessing whether a model can rectify factual inconsistencies. One paper also uses the variant name Self-CKGPT for the consistency-based baseline.

**What it is claimed to measure.** Papers link it to 3 behavioral indicators and no constructs. The linked indicators are Knowledge editing, Hallucination, and Hallucination detection, so the reported uses are distributed across several behavioral targets rather than tied to a construct. In these links, papers use it to evaluate the ability to correct hallucination in knowledge editing, to assess hallucination or response veracity, and to measure hallucination detection through inconsistency among sampled responses.

**Space of uses.** No measurement instrument is linked to it. In use, papers commonly position it as a baseline or comparison point among hallucination metrics, for example alongside SBERT, INSIDE, InterrogateLLM, Lexical Similarity, and EigenScore in zero-shot detection settings. A smaller line of work uses it as a benchmark for hallucination correction in knowledge editing.

## Sources

**SelfCheckGPT** (6 papers: [LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf), [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.276.pdf), [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf), [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf), [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1719.pdf), [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf))
> A suite of hallucination detection methods that analyzes multiple stochastically sampled responses from a model to assess the veracity of a given response, often in a black-box or gray-box setting.

**Self-CKGPT** (1 paper: [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf))
> A consistency-based baseline method for hallucination detection that assesses the consistency of a model's own generated responses.

## Relationships

### → SelfCheckGPT
- **Knowledge editing** (behavioral indicator): *measured_by*, 3 papers
  > “we also evaluate its ability to correct Hallucination in SelfCheckGPT [48].”
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf)
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1719.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 2 papers
  > and also evaluate its ability to correct Hallucination in SelfCheckGPT [48]. (Section 3.1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf)
- **Hallucination detection** (behavioral indicator): *measured_by*, 2 papers
  > We compare the proposed AGSER approach with SBERT (Reimers and Gurevych, 2019), SelfCheckGPT (Manakul et al., 2023), INSIDE (Chen et al., 2024) and InterrogateLLM (Yehuda et al., 2024) in zero-shot hallucination detection.
  - [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf)
  - [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf)
