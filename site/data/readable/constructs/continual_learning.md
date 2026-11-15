# Continual learning
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Lifelong learning, Continuous learning capability  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats continual learning as a model or agent capacity to keep acquiring new skills or knowledge over time while preserving performance on earlier tasks and avoiding catastrophic forgetting. Several definitions phrase this as incremental learning from new or streaming data, often over a sequence of tasks, and one source says it lets a model "add new skills over time without catastrophic forgetting" (Transformer-Squared: Self-adaptive LLMs). Smaller lines of work use nearby labels, especially lifelong learning for ongoing acquisition through open-world interaction or through storing and reusing effective safety checks, while one paper narrows the construct to integrating updated information "without parameter updates" (Continuously Updating Digital Twins using Large Language Models).

**Space of facets.** Most papers systematize continual learning around sequential exposure: a model adapts to a sequence of tasks, streaming data, or episodes, and in one few-shot relation extraction formulation each task introduces new relations to be learned. One paper explicitly places few-shot continual relation extraction as a branch of continual information extraction. Naming varies, with continual learning, lifelong learning, and continuous learning capability used for overlapping ideas, but the scope shifts between general task-sequence adaptation, open-world interaction, safety-check reuse, and no-parameter-update integration of new information. Another paper frames effective continual learning as having two primary challenges, catastrophic forgetting and knowledge transfer, with knowledge transfer divided into forward transfer and backward transfer.

**Space of measurement.** Operationally, papers link continual learning to 4 measurement instruments, all benchmark or dataset based: HotpotQA, PG-19, SQuAD v1.1, and Super-NaturalInstructions. These instruments are used in continual fine-tuning setups, episodal continual learning, or named CL benchmarks, and one paper says performance is tracked across test sets for "learning against forgetting," so the operationalization is largely about adding new tasks or data while checking retention. Papers also link it to 3 behavioral indicators, with catastrophic forgetting appearing most often, alongside causal discovery and relation extraction.

**Links.** The most frequent link is to catastrophic forgetting. Several papers describe continual learning as related to catastrophic forgetting, and one paper claims a causal relationship from continual learning to catastrophic forgetting; the quoted language repeatedly frames continual learning as learning new tasks without forgetting old knowledge or as needing to mitigate forgetting. One paper also claims a causal relationship from causal discovery to continual learning, saying that newly discovered items and action-level causal discovery ensure lifelong learning through continuous engagement and adaptation. Beyond that, one paper relates continual learning to relation extraction, specifically few-shot continual relation extraction, and another relates it to knowledge transfer, including forward transfer and backward transfer.

## Sources

**Continual learning** (4 papers: [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf), [Learn to Memorize: Scalable Continual Learning in Semiparametric Models with Mixture-of-Neighbors Induction Memory](https://aclanthology.org/2025.acl-long.1385.pdf), [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf), [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf))
> The ability of a model to acquire new skills and knowledge over time from new data without degrading performance on previously learned tasks.

**Lifelong learning** (2 papers: [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf), [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399.pdf))
> The agent's capacity to continuously acquire and integrate new knowledge and skills from ongoing interaction with an open-world environment.

**Continuous learning capability** (1 paper: [Continuously Updating Digital Twins using Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/amad25a/amad25a.pdf))
> The latent ability of a model to integrate new information, such as updated data or knowledge, without requiring parameter updates or re-training, enabling persistent relevance in evolving environments.

## Relationships

### Continual learning →
- **Catastrophic forgetting** (behavioral indicator): *causes*, 6 papers
  > However, due to the continual learning process with limited data, FCRE models are often biased toward the current task, facing the challenges of overfitting (Hawkins, 2004) and Catastrophic forgetting (Thrun and Mitchell, 1995; Le et al., 2024a; Hai et al., 2024; Van et al., 2022; Phan et al., 2022). (Section 1)
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf)
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA... (Section 4.1)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA... (Section 4.1)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **PG-19** (measurement instrument): *measured_by*, 1 paper
  > We consider the problem of episodal continual learning (Kirkpatrick et al., 2017; Nguyen et al., 2017) where each episode’s data, yn, is one of 20 books from the PG19 (Rae et al., 2019) dataset
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 1 paper
  > We conducted experiments on two CL benchmarks, including SuperNI Benchmark (Wang et al., 2022a) and Long Sequence Benchmark (Razdaibiedina et al., 2023). (Section 4.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)

### → Continual learning
- **Causal discovery** (behavioral indicator): *causes*, 1 paper
  > Newly discovered items enable the execution of new unknown actions and the CD on these actions. This iterative process ensures the lifelong learning through continuous engagement and adaptation.
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)

### Associated with
- **Relation extraction** (behavioral indicator), 1 paper
  > Few-shot Continual Relation Extraction (FCRE) has emerged as a significant challenge in information extraction, necessitating that relation extraction (RE) systems can sequentially identify new relations with limited labeled samples. (Abstract)
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Knowledge transfer** (construct), 1 paper
  > Previous CL research posits that an effective CL method should address two primary challenges: 1) Catastrophic Forgetting (CF) ... and 2) Knowledge Transfer (KT), which includes both forward transfer and backward transfer. (Section 2.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
