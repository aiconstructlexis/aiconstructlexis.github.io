# AGIEval
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** AgiEval, AGIeval, AGIEVAL, AGI Eval, Agi-Eval  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats AGIEval as a human-centric benchmark for evaluating foundation models or language models on standardized exams. Most definitions describe it as drawing on exam questions such as the Gaokao, SAT, GRE, law school admission tests, college admission tests, and civil service examinations, and some papers specify fields like English, Math, Law, and Logic. A smaller line of work describes it more broadly as an aggregated benchmark for overall model capabilities or artificial general intelligence across a wide range of tasks and skills, and one paper calls it a bilingual benchmark for exam performance.

**What it is claimed to measure.** The recorded measurement claims are concentrated rather than spread across many targets: papers link AGIEval to 1 construct, Generalization, and to no behavioral indicators. One paper reports that Generalization is measured by AGIEval, using all English tasks in zero-shot settings, while many descriptions more broadly say the benchmark evaluates general abilities, overall model performance, reasoning capabilities, knowledge, or general world knowledge.

**Space of uses.** Papers use AGIEval alongside other general benchmarks, including MMLU, BBH, ARC-C, ARC-E, and BoolQ, with other benchmark names also appearing. It is often positioned as a general evaluation or downstream assessment benchmark, for example as an additional testbed where methods are also tested or where English exam tasks are run in zero-shot settings; one paper also cites it as a prior general evaluation suite and as a model for collecting exam questions.

## Sources

**AgiEval** (5 papers: [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf), [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf), [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf), [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf))
> A benchmark designed to evaluate foundation models on human-centric tasks, derived from standardized exams like the Gaokao (Chinese college entrance exam) and American law school admission tests.

**AGIEval** (6 papers: [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [ITALIC: An Italian Culture-Aware Natural Language Benchmark](https://aclanthology.org/2025.naacl-long.68.pdf), [Capture the Key in Reasoning to Enhance CoT Distillation Generalization](https://aclanthology.org/2025.acl-long.21.pdf), [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf), [A Comprehensive Literary Chinese Reading Comprehension Dataset with an Evidence Curation Based Solution](https://aclanthology.org/2025.emnlp-main.177.pdf))
> A benchmark for evaluating the general abilities of foundation models on human-centric standardized exams.

**AGIeval** (1 paper: [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf))
> A benchmark for evaluating foundational models on human-centric standardized tests to measure general model performance.

**AGIEVAL** (1 paper: [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf))
> AGIEVAL, a benchmark referenced as a prior general evaluation suite and as an inspiration for the paper's question-collection approach.

**AGI Eval** (1 paper: [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf))
> An aggregated benchmark dataset designed to assess the overall capabilities of language models across a wide range of tasks.

## Relationships

### → AGIEval
- **Generalization** (construct): *measured_by*, 1 paper
  > Additionally, to verify generalization, we perform all English tasks in AGIEval (Zhong et al., 2023) using zero-shot settings, which presents a collection of human-centric standardized exams.
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
