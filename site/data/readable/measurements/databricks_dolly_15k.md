# Databricks Dolly-15k
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** Databricks-Dolly-15k, Dolly, Dolly-15k, Databricks-dolly 15k  

## State of the Field

**What it is.** Across papers, the prevailing framing is an instruction-following dataset, often described as open-source and based on human-generated records, and used to fine-tune large language models for instruction following or dialogue generation. Some authors instead present it as an evaluation task or benchmark dataset, including use in decoding experiments, Diff-eRank computation, and federated LLM fine-tuning across multiple NLP tasks. Papers also describe its contents with some specificity: one account says it contains 15,000 human-written instruction-response pairs, another says it includes categories such as brainstorming, classification, closed QA, generation, information extraction, open QA, and summarization, and one paper uses a 500-sample test split.

**What it is claimed to measure.** Papers link it to 1 construct and 2 behavioral indicators overall. The direct measurement claims span both a construct and a behavioral indicator: papers use it to measure Helpfulness, in work that selects Dolly samples to assess whether LLMs retain usefulness after fine-tuning, and Dialogue generation, where Dolly is treated as the dialogue generation task. One additional paper reports that Databricks Dolly-15k is related to Refusal through poisoned versions of the dataset, rather than using it to measure refusal.

**Space of uses.** Papers position it both as training data and as an evaluation set. It appears in supervised or benign fine-tuning, downstream adaptation, generalization tests across data styles, decoding evaluation, computation of Diff-eRank and reduced loss, and federated LLM fine-tuning experiments. No measurement instrument is linked to it in the recorded relationships, but papers use it alongside Alpaca, XSum, WMT18, BeaverTails, and Flan datasets.

## Sources

**Databricks-Dolly-15k** (1 paper: [Multi-Draft Speculative Sampling: Canonical Decomposition and Theoretical Limits](https://proceedings.iclr.cc/paper_files/paper/2025/file/04cdf500730af7733a6b13cbbc230206-Paper-Conference.pdf))
> An instruction-following dataset used as an evaluation task for decoding experiments.

**Dolly** (3 papers: [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf), [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf), [Priority on High-Quality: Selecting Instruction Data via Consistency Verification of Noise Injection](https://aclanthology.org/2025.emnlp-main.1048.pdf))
> An open-source dataset of human-generated instruction-following records used to fine-tune large language models for instruction following and dialogue generation.

**Dolly-15k** (2 papers: [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf), [Diff-eRank: A Novel Rank-Based Metric for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/45cc967d7899616f51993b7b363d35b5-Paper-Conference.pdf))
> An instruction-following dataset with records across categories like brainstorming and question answering, used for supervised fine-tuning to evaluate attack durability.

**Databricks-dolly 15k** (1 paper: [pFedGPT: Hierarchically Optimizing LoRA Aggregation Weights for Personalized Federated GPT Models](https://aclanthology.org/2025.emnlp-main.239.pdf))
> A benchmark dataset used for federated LLM fine-tuning experiments across multiple NLP tasks.

## Relationships

### → Databricks Dolly-15k
- **Dialogue generation** (behavioral indicator): *measured_by*, 1 paper
  > ...and Dolly (Conover et al., 2023) datasets as the dialogue generation task. (Section 3.3)
  - [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > to assess whether LLMs retain usefulness after fine-tuning, we select 15k general-domain samples equally from Alpaca (Taori et al., 2023), BeaverTails, and Dolly (Conover et al., 2023). (Section 5.1)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)

### Associated with
- **Refusal** (behavioral indicator), 1 paper
  > For AutoPoison-refusal, we first generate poisoned datasets by replacing the generation targets in GPT-4-LLM and Databricks-Dolly-15k with two refusal outputs... (Section A.1)
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
