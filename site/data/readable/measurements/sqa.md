# SQA
**Type:** Measurement instrument  
**Supporting papers:** 20  

## State of the Field

**What it is.** Across papers, SQA is most commonly described as a science question answering or ScienceQA benchmark, usually multimodal: definitions mention science questions that require complex reasoning, often with diagrams, reasoning over text and diagrams, scientific knowledge, and, in one description, a focus on model reasoning capability. A smaller line of work uses the same acronym for sequential question answering over tabular data in multi-turn or logically related settings, and one paper uses it for a 3D question answering benchmark with over 33K question-answer pairs from 650 indoor scenes.

**What it is claimed to measure.** Papers link SQA to one behavioral indicator and one construct. The prevailing measurement claim is that it measures visual question answering, with papers explicitly evaluating methods on visual or image question-answering benchmarks including SQA; a smaller line of work reports it as measuring multimodal reasoning by listing it among multimodal benchmarks.

**Space of uses.** No measurement instrument is linked to it through recorded relationships. In use, papers usually include SQA as one benchmark within broader evaluation suites, often alongside VQAv2, VizWiz, GQA, and VQA, and, in one 3D-QA use, with ScanQA. When authors use the sequential-QA meaning of SQA, one paper positions it instead as a held-out table-based question dataset.

## Sources

**SQA** (9 papers: [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf), [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf), [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf), [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf), [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf), [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> The Science Question Answering (SQA) dataset, which involves answering science questions that require complex reasoning and often an accompanying diagram.

## Relationships

### → SQA
- **Visual question answering** (behavioral indicator): *measured_by*, 2 papers
  > we evaluate our method for pruning language models on various visual question-answering and reasoning benchmarks, including VQAv2 [17], SQA [37], and VQA [47]. (Section 7.3).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [$\gamma-$MoD: Exploring Mixture-of-Depth Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > We conduct extensive experiments on multiple challenging tasks such as arithmetic, knowledge reasoning, and multimodal benchmarks spanning GSM8K, MMLU, SQA, and VQA (Abstract).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
