# Paraphrase detection
**Type:** Behavioral indicator  
**Supporting papers:** 42  
**Also known as:** Duplication detection, Semantic equivalence detection, Paraphrase identification, Semantic equivalence judgment, Duplicate question detection  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats paraphrase detection as deciding whether a pair of texts, most often two sentences, have the same meaning or are paraphrases of each other. This is usually framed as a binary judgment, for example yes or no, equivalent or not equivalent, or duplicate or not duplicate, and some papers broaden the pair from sentences to questions, documents, or responses. A smaller line of work defines the behavior through semantic equivalence by mutual entailment, uses a three-way semantic (in)equivalence setting under controlled lexical constraints, or reformulates the task as generating a sentence that supports or contradicts a given sentence instead of directly classifying the pair.

**Variants.** Papers use several nearby names for the same behavior, most commonly paraphrase detection or paraphrase identification, and less often duplication detection, duplicate question detection, semantic equivalence detection, or semantic equivalence judgment. The dominant setting is sentence or question pairs, but some work studies text snippets, questions or documents as duplicates, and response pairs judged equivalent by mutual entailment. There are also language- or setting-specific versions, including Filipino and German sentence pairs, Spanish PAWS-X evaluation, and semantic (in)equivalence tasks designed with controlled lexical constraints.

**Space of elicitation and scores.** Papers measure it with five instruments. The most frequently linked instruments are MRPC and QQP, followed by PAWS, GLUE, and PAWS-X. These are described as paraphrase or paraphrase identification datasets and benchmarks, with GLUE used as a broader benchmark that includes paraphrase tasks such as MRPC and QQP, and PAWS-X described as a cross-lingual adversarial dataset for paraphrase identification.

**What it is taken as evidence of.** The papers do not explicitly link paraphrase detection to any construct; the recorded links are only to measurement instruments.

## Sources

**Paraphrase detection** (13 papers: [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf), [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf), [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf), [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf), [LLäMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch](https://aclanthology.org/2025.acl-long.111.pdf), [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf))
> The observable task of determining whether two sentences are paraphrases of each other.

**Duplication detection** (1 paper: [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf))
> The task of identifying whether two questions or documents are semantically equivalent or duplicates.

**Paraphrase identification** (9 papers: [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [Batayan: A Filipino NLP benchmark for evaluating Large Language Models](https://aclanthology.org/2025.acl-long.1509.pdf), [Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases](https://aclanthology.org/2025.acl-long.469.pdf), [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf))
> The observable task of determining whether two sentences have the same meaning.

**Semantic equivalence detection** (1 paper: [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of determining whether two sentences convey the same meaning, potentially despite differences in their lexical and syntactic structure.

**Semantic equivalence judgment** (1 paper: [Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs](https://aclanthology.org/2025.emnlp-main.238.pdf))
> Determining whether two responses are semantically equivalent by mutual entailment.

**Duplicate question detection** (1 paper: [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf))
> The task of determining whether two questions have the same semantic meaning.

## Relationships

### Paraphrase detection →
- **MRPC** (measurement instrument): *measured_by*, 8 papers
  > paraphrasing: QQP, MRPC (Dolan & Brockett, 2005); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **QQP** (measurement instrument): *measured_by*, 6 papers
  > paraphrasing: QQP, MRPC (Dolan & Brockett, 2005); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1583.pdf)
- **PAWS** (measurement instrument): *measured_by*, 5 papers
  > PAWS ... Paraphrase Identification (Table 1: Dataset Statistics.)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > This benchmark we use covers paraphrase detection (MRPC, QQP), sentiment classification (SST-2), natural language inference (MNLI, RTE, QNLI), and linguistic acceptability (CoLA). (Section 4.3)
  - [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **PAWS-X** (measurement instrument): *measured_by*, 2 papers
  > For paraphrase identification, we used the Spanish portion of PAWS-X (Yang et al., 2019), a multilingual dataset containing adversarially constructed paraphrase pairs. (Section 5.2)
  - [Exploring morphology-aware tokenization: A case study on Spanish language modeling](https://aclanthology.org/2025.emnlp-main.1552.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
