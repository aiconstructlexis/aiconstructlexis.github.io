# XNLI
**Type:** Measurement instrument  
**Supporting papers:** 39  

## State of the Field

**What it is.** Across the surveyed work, the prevailing framing treats XNLI as a multilingual or cross-lingual natural language inference benchmark built from sentence pairs or premise-hypothesis pairs, where models classify relations such as entailment, contradiction, and neutrality. Several definitions present it as a multilingual extension of MNLI or MultiNLI, but papers differ on scope: some describe 15 languages, others 14, and a few use alternative label wording such as "unrelated" or "Non-entailed." Some papers also work with specific portions or subsets, including the English portion, the Spanish portion, and sampled test examples.

**What it is claimed to measure.** Papers link XNLI to 4 constructs and 4 behavioral indicators. The dominant measurement claim is Natural language inference, with several papers using it for multilingual NLI or textual entailment evaluation. Beyond that, the construct-side links are spread across Cross-lingual generalization, Helpfulness, Multilingual understanding, and Semantic understanding, while papers also report additional behavioral-indicator uses rather than converging on one second target.

**Space of uses.** Papers do not report measurement-instrument relationships for XNLI. In use, they usually place it inside broader multilingual evaluation suites, alongside XCOPA, XWinograd, X-CSQA, TyDi QA, and XLSum, among other named datasets, for classification-task evaluation, zero-shot prompting, or general-capability checks. Some papers work with overlapping-language samples, randomly sampled test points, or the English and Spanish portions, and one paper pretrains on XNLI as indirect supervision.

## Sources

**XNLI** (18 papers: [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [MT-Ranker: Reference-free machine translation evaluation by inter-system ranking](https://proceedings.iclr.cc/paper_files/paper/2024/file/dbd6b295535e44f2b8ec0c3f1da7c509-Paper-Conference.pdf), [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf), [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf), [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf), [Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Robust, Adaptable Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f69eee2fafab3743a3d2ae5981c949f-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf), [Towards Robust Knowledge Representations in Multilingual LLMs for Equivalence and Inheritance based Consistent Reasoning](https://aclanthology.org/2025.naacl-long.394.pdf), [SMAB: MAB based word Sensitivity Estimation Framework and its Applications in Adversarial Text Generation](https://aclanthology.org/2025.naacl-long.463.pdf), [Soft Language Prompts for Language Transfer](https://aclanthology.org/2025.naacl-long.517.pdf), [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf), [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf))
> Cross-lingual Natural Language Inference dataset that assesses a model's ability to determine entailment, contradiction, or neutrality between sentence pairs in multiple languages.

## Relationships

### → XNLI
- **Natural language inference** (behavioral indicator): *measured_by*, 10 papers
  > a language understanding dataset XNLI [Conneau et al., 2018] in natural language inference (NLI) task were used. (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
  - [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.939.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Exploring morphology-aware tokenization: A case study on Spanish language modeling](https://aclanthology.org/2025.emnlp-main.1552.pdf)
  - [Discriminating Form and Meaning in Multilingual Models with Minimal-Pair ABX Tasks](https://aclanthology.org/2025.emnlp-main.1210.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > For the assessment of usefulness, we sample 30 examples in English and each language overlapping with MultiJail from XNLI (Conneau et al., 2018) and X-CSQA (Lin et al., 2021)... We calculate the average accuracy on both datasets to represent usefulness. (Section 4.3)
  - [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf)
- **Cross-lingual generalization** (construct): *measured_by*, 1 paper
  > Models are then fine-tuned on the XNLI dataset, for both cross-lingual zero-shot transfer from English and target language fine-tuning.
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > a language understanding dataset XNLI [Conneau et al., 2018] in natural language inference (NLI) task were used. (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Semantic understanding** (construct): *measured_by*, 1 paper
  > The two multilingual tasks evaluate MrT5's ability to understand high-level semantics... specifically, two cross-lingual benchmarks (XNLI and TyDi QA)
  - [MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf)
- **Machine translation** (behavioral indicator): *measured_by*, 1 paper
  > Machine translation uses the XNLI (Conneau et al., 2018) parallel corpus for 15 languages... (Section 3.3)
  - [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > To demonstrate a more natural instance of catastrophic forgetting, we consider what happens to a language model after we fine-tune on code. ... To test forgetting, we use the XNLI benchmark (Conneau et al., 2018) (Section 4.2)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Multilingual understanding** (construct): *measured_by*, 1 paper
  > We use the widely adopted XNLI dataset (Conneau et al., 2018) for evaluation, which assesses sentence understanding in multiple languages by determining the relationship between sentence pairs. (Section 3.3)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
