# Human preference evaluation
**Type:** Measurement instrument  
**Supporting papers:** 36  
**Also known as:** Human preference study, A/B testing, Side-by-side comparisons, Human pairwise comparison, Human pairwise evaluation, Human preference-based evaluation, Human preference voting, Human preference test, AB preference test, Human comparative evaluation, Moderation Preference Annotation, Pairwise comparisons  

## State of the Field

**What it is.** The prevailing usage is a pairwise human judgment protocol: evaluators see outputs from two models side by side and choose the better one, often with a tie or no-difference option. Papers describe closely related variants as human preference studies, A/B testing, side-by-side comparisons, human pairwise or comparative evaluation, preference voting, and AB preference tests, with task criteria tailored to the application, such as faithfulness, general response quality, translation quality, plausibility and consistency, argument quality, plan usefulness, or omission, fabrication, distortion, and temporal mismatch in captions. A smaller line of work uses the same label for non-pairwise ratings, including a 5-point Mean Opinion Score setup for naturalness and meaningfulness.

**What it is claimed to measure.** Papers link this protocol to 3 constructs and no behavioral indicators. The linked constructs, listed most often first, are Human preference alignment, Faithfulness, and Text generation quality, and the relationship is always that those constructs are measured by human preference evaluation. The measurement claims are therefore spread across several constructs rather than centered on one: papers use it to assess alignment with human preferences, to ask which description is more faithful to a table, and to judge the general quality of model responses.

**Space of uses.** No measurement instrument is linked to it. Papers usually position it as a direct human check on model outputs, with results reported as win rates, win:tie:lose ratios, or under Elo scoring; some descriptions place it alongside automatic evaluation metrics, RM scores, GPT-4 pairwise evaluation, or AlpacaEval. A smaller set of papers explicitly uses it to validate LLM-based evaluation or to complement results from model-scored benchmarks.

## Sources

**Human preference study** (3 papers: [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf), [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf), [Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.10.pdf))
> Human evaluation protocol where annotators rate which of two model descriptions is more faithful to a table.

**Human preference evaluation** (3 papers: [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [SHIFT: Selected Helpful Informative Frame for Video-guided Machine Translation](https://aclanthology.org/2025.emnlp-main.161.pdf))
> A human evaluation protocol where evaluators are presented with outputs from two models side-by-side and asked to choose which is significantly better or if there is no significant difference.

**A/B testing** (2 papers: [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf), [Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf))
> A human evaluation method where raters compare two model outputs (A and B) and choose the better one.

**Side-by-side comparisons** (1 paper: [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf))
> Human evaluation procedure in which outputs are compared directly to assess higher quality.

**Human pairwise comparison** (1 paper: [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf))
> An evaluation protocol where human experts assess hypothesis quality by selecting the better option from a pair of hypotheses or indicating no discernible difference.

**Human pairwise evaluation** (1 paper: [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf))
> A human judgment procedure in which annotators compare two responses and choose the preferred one using task-specific criteria.

**Human preference-based evaluation** (1 paper: [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf))
> A human evaluation protocol where annotators are shown outputs from two different models for the same input and are asked to choose the better one or declare a tie.

**Human preference voting** (1 paper: [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf))
> A human evaluation method where volunteers compare and vote on the quality of video captions generated by different models based on criteria like omission, fabrication, distortion, and temporal mismatch.

**Human preference test** (1 paper: [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf))
> A human evaluation protocol where participants listen to spoken dialog responses from two different models and choose the preferred one based on comprehensive criteria like naturalness, prosody, and semantic coherence.

**AB preference test** (1 paper: [SongCreator: Lyrics-based Universal Song Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/92a7a03e1c716970848a4a86cc8243ee-Paper-Conference.pdf))
> A human pairwise preference protocol in which listeners choose between two audio samples for a given task.

**Human comparative evaluation** (1 paper: [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.374.pdf))
> A human annotation procedure in which workers compare paired arguments and judge which one is superior or whether they are equally good or bad.

**Moderation Preference Annotation** (1 paper: [It Is Not Only the Negative that Deserves Attention! Understanding, Generation & Evaluation of (Positive) Moderation](https://aclanthology.org/2025.naacl-long.567.pdf))
> Pairwise human preference evaluation in which annotators choose between professional and generated moderation replies to the same user comment, assessing relative quality and preference.

**Pairwise comparisons** (1 paper: [A Good Plan is Hard to Find: Aligning Models with Preferences is Misaligned with What Helps Users](https://aclanthology.org/2025.emnlp-main.585.pdf))
> A human evaluation method where users select which of two plans they believe will help them solve a question more accurately or quickly, used to measure user preferences.

## Relationships

### → Human preference evaluation
- **Human preference alignment** (construct): *measured_by*, 2 papers
  > “Then, we conduct a human preference study.”
  - [Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf)
- **Faithfulness** (construct): *measured_by*, 1 paper
  > Annotators are tasked with rating which of the two descriptions is more faithful to the table. (Section 5)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > "We also conduct human evaluation on the general quality of the model responses on the combined test set described in Section 3.1"
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
