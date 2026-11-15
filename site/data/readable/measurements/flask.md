# FLASK
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across papers, the prevailing framing is FLASK as a fine-grained benchmark or evaluation protocol for particular LLM skill sets. Definitions vary in emphasis: some describe a benchmark for fine-grained evaluation, others a model-based protocol for assessing generated text such as rationales across dimensions like logical thinking, and one defines it more concretely as 200 test prompts paired with 2000 responses from Alpaca-7B, Vicuna-13B, Bard, and GPT-3.5-Turbo-0613 to assess LLM-as-a-judge performance across diverse outputs. A smaller line of work treats it as a benchmark for judge models on single-instance rating tasks, and one usage focuses on its logical thinking category, covering logical correctness, logical robustness, and logical efficiency.

**What it is claimed to measure.** Papers use FLASK to measure 4 constructs and no behavioral indicators, and the reported targets are spread across those constructs rather than centered on one recurring claim. The linked constructs are Insightfulness, Text generation quality, Logical consistency, and Logical reasoning. One paper describes FLASK as offering "12 skill-specific scores," while another uses its logical thinking category to evaluate logical consistency and logical reasoning.

**Space of uses.** In use, papers position FLASK both as a stand-alone fine-grained benchmark and as one component in broader evaluation suites. One paper evaluates response quality with "AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks," while another uses FLASK specifically for model-based evaluation of rationales and notes that it has high correlation with human-based evaluation. Papers also relate it to 3 other instruments, GSM8K, LLM-as-a-judge, and MMLU: in one paper, MMLU and GSM8K are among the datasets used to collect instruction and reference-answer pairs, and another definition explicitly uses FLASK to assess LLM-as-a-judge performance.

## Sources

**FLASK** (4 papers: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [TRACT: Regression-Aware Fine-tuning Meets Chain-of-Thought Reasoning for LLM-as-a-Judge](https://aclanthology.org/2025.acl-long.147.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf))
> A benchmark designed for fine-grained evaluation of particular LLM skill sets.

## Relationships

### → FLASK
- **Insightfulness** (construct): *measured_by*, 1 paper
  > FLASK, on the other hand, offers a more granular evaluation with 12 skill-specific scores... Specifically, our methodology shows improvement in robustness, correctness, insightfulness
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Logical consistency** (construct): *measured_by*, 1 paper
  > we employ FLASK (Ye et al., 2024), a fine-grained evaluation protocol for model-based evaluation, which exhibits a high correlation with human-based evaluation. Specifically, we focus on the ‘logical thinking’ category in FLASK, which encompasses three aspects: logical correctness, logical robustness, and logical efficiency.
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > Specifically, we focus on the ‘logical thinking’ category in FLASK, which encompasses three aspects: logical correctness, logical robustness, and logical efficiency. (Section 5.4)
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)

### Associated with
- **MMLU** (measurement instrument), 1 paper
  > We first collect input (instruction) and output (reference answer) pairs from various English NLP datasets, both multi-task datasets (e.g. MMLU (Hendrycks et al., 2020))... (Section 3.2)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **GSM8K** (measurement instrument), 1 paper
  > We first collect input (instruction) and output (reference answer) pairs from various English NLP datasets, ... and single-task datasets (e.g. GSM8K (Cobbe et al., 2021)). (Section 3.2)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > “FLASK (Fine-grained Language Model Evaluation based on Alignment SKill Sets), a fine-grained evaluation protocol for both human-based and model-based evaluation”
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
