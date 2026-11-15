# TyDi QA
**Type:** Measurement instrument  
**Supporting papers:** 23  
**Also known as:** TyDiQA, TydiQA, TYDIQA, Tydi QA  

## State of the Field

**What it is.** Papers most commonly describe TyDi QA as a multilingual question answering benchmark or dataset. The prevailing description is that it covers 11 typologically diverse languages, though one paper instead says it includes 9 kinds of languages; several papers also describe gold-passage or Wikipedia-based setups, including questions answered from a given article, single-hop evaluation with wiki contexts, answer-span identification in a passage, language-specific subsets such as ID, SW, and FI, and an Indonesian subset that one paper repurposes from reading comprehension to open-domain QA by removing context.

**What it is claimed to measure.** Papers link it to 2 constructs and 3 behavioral indicators. The prevailing measurement claim is multilingual ability, with papers explicitly saying they use TydiQA for multilingual ability or to assess multilinguality; a smaller line of work reports it as measuring general ability. On the behavioral side, papers use it to measure multilingual question answering most often, and also question answering and machine reading comprehension.

**Space of uses.** Papers often place it alongside MMLU, BBH, GSM8K, and TruthfulQA in broader evaluation batteries. They variously position it as a multilinguality check, as part of general-capability evaluation, and, in one task-specific use, the Indonesian subset is used for reading comprehension and then repurposed into open-domain QA by removing context; one paper also relates it to the Open LLM Leaderboard by adopting it as one of five tasks.

## Sources

**TyDiQA** (9 papers: [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf), [The Art of Saying No: Contextual Noncompliance in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/58e79894267cf72c66202228ad9c6057-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multilingual question answering benchmark included in the expanded evaluation set, with language-specific subsets used in evaluation.

**TydiQA** (3 papers: [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Fine-tuning with Reserved Majority for Noise Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b6898c70d5b328deaf2216aefd8f77a-Paper-Conference.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf))
> A benchmark for evaluating multilingual question answering capabilities across a diverse set of typologically different languages.

**TYDIQA** (2 papers: [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf))
> TyDi QA, a multilingual question-answering benchmark used here to evaluate instruction-tuned LLMs.

**TyDi QA** (3 papers: [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf), [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf), [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20 Indonesian Languages](https://aclanthology.org/2025.emnlp-main.881.pdf))
> A single-hop question answering benchmark evaluated with Wikipedia datastore contexts.

**Tydi QA** (1 paper: [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf))
> A question answering dataset covering 11 typologically diverse languages, requiring models to answer questions given a Wikipedia article.

## Relationships

### → TyDi QA
- **Multilingual ability** (construct): *measured_by*, 5 papers
  > We use Big Bench Hard (BBH; Suzgun et al. (2022)) as a testbed for reasoning ability, HumanEval (Chen et al., 2021) for coding ability, and TydiQA (Clark et al., 2020) for multilingual ability.
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
- **Multilingual question answering** (behavioral indicator): *measured_by*, 2 papers
  > TYDIQA (Clark et al., 2020) is a multilingual question-answer dataset that includes 9 kinds of languages.
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
  - [XLQA: A Benchmark for Locale-Aware Multilingual Open-Domain Question Answering](https://aclanthology.org/2025.emnlp-main.1466.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > TydiQA [7] Multilingual QA (Table 1)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate the general capabilities, we utilized GSM8K (EM) (Cobbe et al., 2021), BBH (EM) (Cobbe et al., 2021), MMLU (EM) (Hendrycks et al., 2020), TydiQA (F1) (Clark et al., 2020), and WikiText (ppl) (Merity et al., 2016), following Ivison et al. (2023). (Section 4)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > We adopt the Indonesian set from TyDi QA (Clark et al., 2020) for reading comprehension, which is based on Indonesian Wikipedia with human-written questions. (Section 3.3)
  - [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20 Indonesian Languages](https://aclanthology.org/2025.emnlp-main.881.pdf)

### Associated with
- **Open LLM Leaderboard** (measurement instrument), 1 paper
  > “We adopt ﬁve OpenLLM Leaderboard tasks as our benchmark for evaluation, including MMLU (Hendrycks et al., 2020), TruthfulQA (Lin et al., 2021), GSM (Cobbe et al., 2021), BBH (Suzgun et al., 2022), TydiQA (Clark et al., 2020).”
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
