# ANLI
**Type:** Measurement instrument  
**Supporting papers:** 13  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats ANLI as Adversarial Natural Language Inference, a benchmark or dataset for natural language inference, often described as large scale and collected through an iterative, adversarial human-and-model-in-the-loop process. Several definitions stress that it was created to be challenging, with one describing the primary aim as making state-of-the-art models fail, and another framing it as a textual entailment task for natural language understanding and reasoning. Some authors also describe open-domain questions enhanced through an iterative adversarial procedure and report using its challenging subsets for evaluation. A table caption in one paper uses ANLI as a label alongside adversarial attacks, but most definitions describe a benchmark dataset.

**What it is claimed to measure.** Papers use ANLI mainly to measure Natural language inference: it is linked to one behavioral indicator, Natural language inference, and the relationship is recorded as measured_by. A smaller line of work uses it to measure Commonsense reasoning, where it is linked to one construct with a measured_by relationship. The recorded claims are therefore concentrated rather than spread across many targets, with one paper saying that MNLI and ANLI benchmark a model's understanding of entailment, contradiction, and neutrality across genres and adversarially selected examples, while another includes ANLI among datasets used for commonsense reasoning.

**Space of uses.** Papers often place ANLI in broader evaluation suites. It appears alongside GLUE, SQuADv1.1, SuperGLUE, and MNLI, and one study explicitly groups it with other classification benchmarks. Some authors use its challenging subsets for open-domain evaluation, and another pairs it with another NLI dataset for natural language inference evaluation.

## Sources

**ANLI** (8 papers: [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf), [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.8.pdf), [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf), [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf))
> Adversarial Natural Language Inference, included as a classification benchmark in the expanded evaluation set.

## Relationships

### → ANLI
- **Natural language inference** (behavioral indicator): *measured_by*, 2 papers
  > MNLI (Multi-Genre Natural Language Inference) and ANLI (Adversarial Natural Language Inference) benchmark a models understanding of entailment, contradiction, and neutrality across genres and adversarially selected examples.
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > For commonsense reasoning, we use ... ANLI [39], a dataset for natural language understanding and reasoning. (Section 5.1)
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
