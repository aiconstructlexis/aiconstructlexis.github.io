# QQP
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Across papers, QQP is most commonly described as the Quora Question Pairs dataset or benchmark, a paraphrase or duplicate-question task in which a pair of questions is labeled for semantic equivalence. Definitions repeatedly frame it as deciding whether two questions are paraphrases, duplicates, or semantically equivalent, and one description specifies more than 400,000 question pairs with a binary paraphrase label. A smaller line of work describes it more broadly as sentence paraphrase judgment, and one paper uses an adversarially perturbed form for robustness testing.

**What it is claimed to measure.** The prevailing use links QQP to one behavioral indicator, paraphrase detection, and papers do not link it to any construct. Relationship claims describe it as measuring paraphrase detection or paraphrase identification, including formulations such as duplicate-question detection and deciding whether two questions are "equivalent" or "not equivalent". The recorded claims therefore converge on a single behavioral target rather than spreading across multiple constructs.

**Space of uses.** In use, papers most often position QQP as part of GLUE, which is its only linked instrument, and evaluate it alongside other GLUE tasks such as MRPC, QNLI, SST-2, and MNLI. They typically use it as one task inside broader evaluation suites, reporting QQP accuracy, fine-tuning performance, or in-context learning results, and some papers specifically mention the QQP dev set or adversarially perturbed examples.

## Sources

**QQP** (13 papers: [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf), [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf), [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf), [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf), [ReLoRA: High-Rank Training Through Low-Rank Updates](https://proceedings.iclr.cc/paper_files/paper/2024/file/d6fdc308a3b0f017f16059e5888f3346-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf), [Interpret and Improve In-Context Learning via the Lens of Input-Label Mappings](https://aclanthology.org/2025.acl-long.196.pdf), [Does Low Rank Adaptation Lead to Lower Robustness against Training-Time Attacks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25f/liang25f.pdf), [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf), [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf))
> A paraphrase identification benchmark used to evaluate whether two questions are semantically equivalent.

## Relationships

### → QQP
- **Paraphrase detection** (behavioral indicator): *measured_by*, 6 papers
  > paraphrasing: QQP, MRPC (Dolan & Brockett, 2005); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1583.pdf)

### Associated with
- **GLUE** (measurement instrument), 3 papers
  > We first evaluate the language understanding tasks from the GLUE benchmark(Wang et al., 2018) including MNLI, SST2, QNLI and QQP using the RoBERTa model.
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
