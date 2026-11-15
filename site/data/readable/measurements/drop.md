# DROP
**Type:** Measurement instrument  
**Supporting papers:** 35  

## State of the Field

**What it is.** Across papers, DROP is most commonly described as the Discrete Reasoning Over Paragraphs reading comprehension benchmark or dataset, built around paragraph-level content and questions that require discrete reasoning such as addition, counting, arithmetic, and sorting. Some authors frame it more specifically as grounded question answering, open-book QA, or a generation task for phrase or numeric answers. One paper uses a decontextualized subset, and another says its queries mainly address History, Politics, Sports, Demographics, and Societal Issues.

**What it is claimed to measure.** In the surveyed work, papers use DROP to measure 6 constructs and 2 behavioral indicators, so the reported measurement claims are spread across several framings rather than concentrated on one. Across constructs, the prevailing links are to discrete reasoning and reasoning, with contextual understanding also present; on the behavioral side, it is linked to machine reading comprehension and question answering. Papers also report 3 other construct links, and some describe this use as testing reading comprehension abilities or question answering where models must ground answers in in-context documents.

**Space of uses.** No other measurement instrument is linked to DROP by recorded relationships, but papers often use it alongside broader benchmark suites, commonly with MMLU, BBH, GSM8K, MATH, and SQuAD. Most papers position it as one benchmark within a larger evaluation battery rather than as a standalone protocol. A smaller line of work adapts it through decontextualized subsets, few-shot or in-context settings, grounded-answer evaluation, or a subsampled training set.

## Sources

**DROP** (10 papers: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf), [A Survey of Post-Training Scaling in Large Language Models](https://aclanthology.org/2025.acl-long.140.pdf), [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf), [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf), [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf))
> A reading comprehension benchmark that requires discrete reasoning over paragraphs, such as addition, counting, or sorting.

## Relationships

### → DROP
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 3 papers
  > DROP [50] Task Reading comprehension with discrete reasoning (Table D.1).
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > Moreover, MINIMA achieves superior performance over baselines with respect to ... reasoning (DROP, BBH, GSM8K)...
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > We also evaluate question answering on SQuAD [70], NQ [46], TriviaQA [40], and Drop [20], where models must ground their answers in in-context documents. (Section 4.1.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **Discrete reasoning** (construct): *measured_by*, 2 papers
  > DROP [50] Task Reading comprehension with discrete reasoning (Table D.1).
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
  - [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > Please note that, among them, BBH, DROP, GSM8K, and MATH are ICL tasks with several independent in-context examples. (Section 3.1)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **Contextual understanding** (construct): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **General reasoning** (construct): *measured_by*, 1 paper
  > We compare training the language world model with policy (FTA-P) with the baseline (Llama-3.1-8B SFT on the same dataset) in several benchmarks, including math500 (Hendrycks et al., 2021), gsm8k (Cobbe et al., 2021), AIME and Drop (Dua et al., 2019), where the first three are mathematical reasoning tasks, and the fourth is a general reasoning task. (Section 4.3.1)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
