# Pairwise comparison
**Type:** Behavioral indicator  
**Supporting papers:** 61  
**Also known as:** Pairwise rating, Preference judgment, LLM judging, Pairwise preference judgment, Pairwise preference selection, Pair-wise preference, Preference feedback generation, Binary response comparison, Arena-style comparison, Response pair judgment, LM-as-a-judge, Pairwise response evaluation, Response comparison, Plan verification, Binary preference selection, Correction verification, Pairwise ranking, Pairwise response comparison, Preference comparison, Pairwise preference classification, Pairwise evaluation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a head-to-head judgment over two candidate outputs for the same prompt, instruction, or question, where an evaluator chooses the better response. Most definitions frame success as selecting a winner or preferred response, while some explicitly allow a tie or win-tie-loss outcome and a smaller line treats it as a strictly binary winner-loser choice; one paper contrasts this with pointwise rating by stressing that items are judged relative to one another rather than independently. The criteria vary by study, including instruction satisfaction, helpfulness, correctness, harmlessness, a specified evaluation dimension, or which answer is less wrong, and the evaluator may be an LLM, a human annotator, or both.

**Variants.** Most papers study ordinary response comparison, under names such as response ranking, preference judgment, pairwise evaluation, or arena-style comparison. Smaller lines of work apply the same comparison pattern in multi-turn conversations, personalized long-form question answering, data-analysis outputs, scientific ideas, text-to-SQL generations, and cartoon captioning, while other papers specialize it to plan verification or correction verification, where the comparison is between two plans or between an original and modified sentence. Most formulations stay with two candidates, though one paper describes direct comparison among two or more candidates when verification scores are close, and another defines pairwise ranking over scored items more abstractly.

**Space of elicitation and scores.** Papers connect pairwise comparison to 7 measurement instruments overall. Direct measured_by links appear for AlpacaFarm, LLMBar, MT-Bench, and RewardBench, and papers describe MT-Bench, AlpacaFarm, and LLMBar as open-ended instruction-following benchmarks that primarily rely on pairwise comparison. Other instrument links, including AlpacaEval, are recorded as related rather than measured_by.

**What it is taken as evidence of.** Papers connect pairwise comparison to 3 constructs overall, and they do not converge on one shared construct label. One line of work treats it as related to positional bias, described as evaluators favoring one side in a pairwise comparison regardless of answer quality. Separately, one paper claims a causal relationship from pairwise comparison to uncertainty, reporting that it can mitigate evaluation uncertainty relative to single-answer grading, and another claims a causal relationship from pairwise comparison to alignment through collecting binary feedback over response pairs.

## Sources

**Pairwise comparison** (6 papers: [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf), [Crowd Comparative Reasoning: Unlocking Comprehensive Evaluations for LLM-as-a-Judge](https://aclanthology.org/2025.acl-long.252.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60.pdf), [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf), [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e297fb6cd1690ee5b39c5bb4c58ad801-Paper-Datasets_and_Benchmarks_Track.pdf))
> Comparing two model-generated responses and selecting a winner, loser, or tie.

**Response ranking** (1 paper: [Beyond the Surface: Measuring Self-Preference in LLM Judgments](https://aclanthology.org/2025.emnlp-main.86.pdf))
> Selecting which of two candidate responses is better in a comparative judgment setting.

**Pairwise rating** (1 paper: [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf))
> A comparison procedure in which documents are judged relative to one another rather than rated independently.

**Preference judgment** (2 papers: [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf), [Tuning LLM Judge Design Decisions for 1/1000 of the Cost](https://raw.githubusercontent.com/mlresearch/v267/main/assets/salinas25a/salinas25a.pdf))
> The observable task of comparing two candidate answers to a prompt and selecting the preferred one.

**LLM judging** (1 paper: [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf))
> Using an LLM as a judge to compare model responses and produce win-tie-loss style judgments.

**Pairwise preference judgment** (1 paper: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf))
> Selecting one of two model outputs as better according to explicit or implicit criteria.

**Pairwise preference selection** (1 paper: [How to Evaluate Reward Models for RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf))
> Choosing one of two responses as preferred in a head-to-head comparison.

**Pair-wise preference** (1 paper: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf))
> Choosing a winner between two candidate responses or models.

**Preference feedback generation** (1 paper: [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf))
> The observable task of providing a comparative judgment between two responses to a given prompt, indicating which one is preferred.

**Binary response comparison** (1 paper: [Interpreting Language Reward Models via Contrastive Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/3538a22cd3ceb8f009cc62b9e535c29f-Paper-Conference.pdf))
> Choosing one of two candidate responses to the same prompt as the preferred response.

**Arena-style comparison** (1 paper: [Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf))
> Comparing two model responses to the same prompt and selecting which response is better.

**Response pair judgment** (1 paper: [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf))
> Selecting which of two candidate responses is better or more correct, optionally with a tie option.

**LM-as-a-judge** (1 paper: [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf))
> The task of using a language model to evaluate and select the better of two candidate responses for a given prompt or question.

**Pairwise response evaluation** (1 paper: [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf))
> The task of taking an instruction and a pair of model-generated responses as input and producing a judgment indicating which response is better.

**Response comparison** (1 paper: [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf))
> The behavior of directly comparing two or more candidate responses to determine which is correct, particularly when verification scores are close.

**Plan verification** (1 paper: [Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://aclanthology.org/2025.emnlp-main.1658.pdf))
> Comparing two versions of a plan and selecting the one judged to be superior in terms of correctness, completeness, or safety.

**Binary preference selection** (1 paper: [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf))
> The task of comparing a pair of model-generated responses and choosing the one that is better according to some criteria.

**Correction verification** (1 paper: [Evolving Chinese Spelling Correction with Corrector-Verifier Collaboration](https://aclanthology.org/2025.emnlp-main.1477.pdf))
> Judging whether a proposed correction is better than the original sentence or whether both versions are incorrect.

**Pairwise ranking** (1 paper: [Loss Functions and Operators Generated by f-Divergences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/roulet25a/roulet25a.pdf))
> The task of determining the relative order of two items based on their assigned scores.

**Pairwise response comparison** (1 paper: [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf))
> The task of evaluating two model-generated responses to the same query and determining which one is better, or if they are of equal quality.

**Preference comparison** (1 paper: [Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/7423902b5534e2b267438c85444a54b1-Paper-Conference.pdf))
> The observable act of selecting one of two model outputs as more preferred, based on criteria such as helpfulness or harmlessness, used to train reward models.

**Pairwise preference classification** (1 paper: [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf))
> The task of classifying which of two text samples (e.g., conversational responses) is preferable according to a specific criterion, such as harmlessness.

**Pairwise evaluation** (1 paper: [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf))
> The task where an evaluator model is presented with two candidate outputs for a given instruction and must choose the better one.

## Relationships

### Pairwise comparison →
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > “open-ended instruction-following benchmarks (MT-Bench, Alpacafarm, and LLMBar), which primarily rely on pairwise comparison task.”
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
- **Uncertainty** (construct): *causes*, 1 paper
  > Compared to single-answer grading, pairwise comparison reduces the influence of subjective bias by directly comparing the relative merits of model outputs, thereby mitigating the uncertainty in evaluation to some extent. (Section 4.5)
  - [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > A key recipe to achieve alignment involves presenting pairs of responses and collecting binary feedback (e.g., preferred, less preferred) based on the comparative quality of these responses. (Section 1)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 1 paper
  > LM-as-a-judge. We benchmark our method on 23 datasets in the RewardBench4 (Lambert et al., 2024b) that can be categorized into four types: Chat, Chat-Hard, Safety, and Reasoning.
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **AlpacaFarm** (measurement instrument): *measured_by*, 1 paper
  > “open-ended instruction-following benchmarks (MT-Bench, Alpacafarm, and LLMBar), which primarily rely on pairwise comparison task.”
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
- **LLMBar** (measurement instrument): *measured_by*, 1 paper
  > “open-ended instruction-following benchmarks (MT-Bench, Alpacafarm, and LLMBar), which primarily rely on pairwise comparison task.”
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)

### Associated with
- **Positional bias** (construct), 2 papers
  > Positional bias (Wang et al., 2024a; Zheng et al., 2023; Wu & Aji, 2023; Chen et al., 2024) occurs when human or LLM evaluators tend to favor one side in a pairwise comparison, regardless of answer quality. (Section 4.5)
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > We explore two typical LLM-as-a-judge methods: Pairwise comparison (Section 2.1)
  - [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument), 1 paper
  > LMSYS Chatbot Arena leverages (240,000) crowdsourced questions and (90,000) crowdsourced human votes to construct pair-wise win-rates
  - [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf)
- **AlpacaEval** (measurement instrument), 1 paper
  > AlpacaEval is a popular pairwise comparison framework that employs GPT-4-Turbo as the fixed baseline model. (Section 1)
  - [Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf)
- **Error localization** (behavioral indicator), 1 paper
  > "Disagreements between candidate solutions strongly signal the potential locations of their errors."
  - [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf)
