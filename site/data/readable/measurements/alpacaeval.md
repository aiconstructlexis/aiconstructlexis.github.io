# AlpacaEval
**Type:** Measurement instrument  
**Supporting papers:** 122  
**Also known as:** Alpaca Eval, Alpaca-Eval, Alpaca-Eval v1.0, alpaca-eval, AlpacaEval v1.0, AlpacaEval 1.0  

## State of the Field

**What it is.** Across papers, AlpacaEval is most commonly described as an automatic, LLM-based benchmark or evaluation framework for instruction-following and open-ended text generation. The prevailing setup compares a model's outputs pairwise against a reference, usually text-davinci-003, with GPT-4 judging and a win rate reported; many descriptions also refer to an accompanying leaderboard or dataset of 805 prompts or instructions from diverse domains, while one paper instead treats it as an out-of-distribution evaluation test set drawn from open-source instruction-following and dialogue data. Papers distinguish v1.0, where the default setup computes win rate against text-davinci-003, and some also mention length-controlled AlpacaEval 2 or AlpacaEval 2.0; smaller uses draw on the helpful_base subset of 129 prompts or on 17701 human annotations.

**What it is claimed to measure.** Papers link AlpacaEval to 13 constructs and 5 behavioral indicators, so claims about what it measures are broad. The dominant use is to measure instruction following, phrased either as instruction following ability or instruction following, and it is also frequently used to measure text generation quality, fluency, helpfulness, and human preference alignment. The remaining links spread across 8 other constructs and 4 other behavioral indicators, with one of those behavioral links recorded as related to pairwise comparison rather than measured_by.

**Space of uses.** Most papers use AlpacaEval alongside other automatic benchmarks, most often MT-Bench, and some also pair it with Vicuna-bench, Arena-Hard-Auto, the Open LLM Leaderboard, and TruthfulQA. It is usually positioned as a headline automatic check, often through leaderboard win rate or pairwise judging, though some papers use its prompts or subsets for auxiliary evaluation, such as helpful_base prompts for helpfulness, its instructions for fluency scoring, or validation sets for preference-data evaluation, and a smaller line uses AlpacaEval as a fine-tuning or downstream task. Papers also link it to 1 other measurement instrument, AlpacaEval 2.0, and some explicitly separate the original setup from length-controlled AlpacaEval 2.

**Concerns raised.** Some papers describe AlpacaEval's score as a proxy for human evaluation, because the pairwise decision is made by an evaluator model such as GPT-4 or ChatGPT. Descriptions also vary on whether it is framed as an automated judge-based benchmark or, in one definition, as human preference evaluation with crowdworker judgments.

## Sources

**AlpacaEval** (34 papers: [#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf), [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf), [Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/639a9a172c044fbb64175b5fad42e9a5-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf), [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf), [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf), [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf), [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf), [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.443.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf), [Vulnerability-Aware Alignment: Mitigating Uneven Forgetting in Harmful Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25w/chen25w.pdf), [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf), [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf), [Distributional Preference Alignment of LLMs via Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/file/bce96750dcb64f3257ceabadf0b9c9bf-Paper-Conference.pdf), [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf), [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf), [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf), [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf), [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf), [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf), [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf), [The Art of Saying No: Contextual Noncompliance in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/58e79894267cf72c66202228ad9c6057-Paper-Datasets_and_Benchmarks_Track.pdf), [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf), [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> An automatic evaluation framework that uses GPT-4 to judge the quality of model outputs and compute a pairwise win rate against a reference model.

**Alpaca Eval** (1 paper: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf))
> A benchmark that uses LLMs as judges to evaluate model performance, particularly for instruction-following capabilities.

**Alpaca-Eval** (2 papers: [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf), [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf))
> An LLM-based evaluation framework that uses GPT-4 to judge the quality of model outputs in open-ended conversation tasks by comparing them to reference responses.

**Alpaca-Eval v1.0** (1 paper: [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf))
> An evaluation suite for assessing instruction-following capabilities, which uses GPT-4 as a judge to calculate a win rate against a baseline model.

**alpaca-eval** (1 paper: [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf))
> An evaluation suite used to compare the instruction-following capabilities of models.

**AlpacaEval 1.0** (1 paper: [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf))
> Open-ended generation benchmark where model outputs are evaluated against text_davinci_003 by GPT-4.

## Relationships

### → AlpacaEval
- **Instruction following** (behavioral indicator): *measured_by*, 12 papers
  > To evaluate the instruction-following ability, we employ the three most widely recognized benchmarks, including AlpacaEval (Li et al., 2023), MT-bench (Zheng et al., 2023) and Vicuna-bench (Chiang et al., 2023).
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Learning to Keep a Promise: Scaling Language Model Decoding Parallelism with Learned Asynchronous Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25a/jin25a.pdf)
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Improving Task Diversity in Label Efficient Supervised Finetuning of LLMs](https://aclanthology.org/2025.emnlp-main.1093.pdf)
- **Instruction following ability** (construct): *measured_by*, 5 papers
  > We reproduce the experiment of fine-tuning Llama-2-7B-chat on Alpaca [Qi et al., 2024] and find that the instruction-following ability, measured by AlpacaEval [Li et al., 2023a], does not improve after fine-tuning (Table 8). (Section 5)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
  - [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf)
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
  - [Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea13534ee239bb3977795b8cc855bacc-Paper-Conference.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
- **Text generation quality** (construct): *measured_by*, 4 papers
  > The AlpacaEval dataset released by Dubois et al. (2023) is used to evaluate the overall quality of generations. (Section 3.3)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [Learning to Keep a Promise: Scaling Language Model Decoding Parallelism with Learned Asynchronous Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25a/jin25a.pdf)
- **Human preference alignment** (construct): *measured_by*, 3 papers
  > For assessing human preferences, recent studies have focused on building crowdsourced battle platforms with human ratings as the primary evaluation metric. Typical platforms include Chatbot Arena (Zheng et al., 2023), MT-Bench (Zheng et al., 2023), and AlpacaEval (Li et al., 2023b). (Section 1)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
- **Helpfulness** (construct): *measured_by*, 3 papers
  > For models tuned on benign data, we also tested helpfulness on AlpacaEval [29]. (Section 5, Response to RQ2)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Improving Factuality with Explicit Working Memory](https://aclanthology.org/2025.acl-long.548.pdf)
  - [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf)
- **Utility preservation** (construct): *measured_by*, 3 papers
  > To measure model utility on benign tasks, we used AlpacaEval (Dubois et al., 2024). (Section 5.1)
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
  - [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1248.pdf)
- **Fluency** (construct): *measured_by*, 3 papers
  > Fluency (Flu): To measure the generation quality of models, we adopt the instructions in AlpacaEval [31], and report the weighted average of bi- and tri-gram entropies [71; 42]. (Section 3.3.2)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Catastrophic Failure of LLM Unlearning via Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf)
  - [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > To evaluate the LLM’s general performance in short-text tasks, we measure its WinRate against the text-davinci-003 model using 100 queries from AlpacaEval and 80 queries from VicunaEval. (Section 5.1)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
  - [UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eafca59fcbabb555fdb5373e2f34385e-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 2 papers
  > “For fine-tuning task, we consider SST2(Socher et al., 2013), AGNEWS(Zhang et al., 2015), GSM8K(Cobbe et al., 2021) and AlpacaEval (Li et al., 2023a) as the user fine-tuning task.”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > To evaluate out-of-distribution (OOD) generalisation, we specify ... one or more out-of-distribution (OOD) test sets for each task... For instruction following, the ID test set is a new test set ... For the first OOD test sets, we use the AlpacaEval evaluation test set (Section 5.1).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > “We prompt the trained models to answer 805 questions from the AlpacaEval dataset”
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Alignment** (construct): *measured_by*, 1 paper
  > improves alignment performance of Zephyr-7B-SFT model by 8% (relative) on AlpacaEval, compared against training on vanilla DPO objective. (Abstract)
  - [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.452.pdf)
- **Controllability** (construct): *measured_by*, 1 paper
  > For evaluating steering, we use the instructions from the Alpaca-Eval dataset (Li et al., 2023).
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Conversational ability** (construct): *measured_by*, 1 paper
  > In the General Benchmark pipeline, we evaluate our models using two widely recognized benchmarks: AlpacaEval (Li et al., 2023) and MT-Bench (Zheng et al., 2023), which assess the model’s comprehensive conversational abilities across various questions. (Section 6)
  - [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf)
- **Textual reasoning** (behavioral indicator): *measured_by*, 1 paper
  > To assess the model’s pure text reasoning ability, we use AlpacaEval (Li et al., 2023a). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Coherence** (construct): *measured_by*, 1 paper
  > “We collect a random subset of 50 tasks ... from the Alpaca-Eval dataset ... An LLM-as-a-Judge then scores the output on how well it followed the instructions and how coherent it was.”
  - [Precise In-Parameter Concept Erasure in Large Language Models](https://aclanthology.org/2025.emnlp-main.960.pdf)
- **Factuality** (construct): *measured_by*, 1 paper
  > We further report AlpacaEval (Li et al., 2023b) win-rate, the fraction of pairwise comparisons a system wins against the ALL-SFT baseline, providing a human-preference proxy for factual quality. (Section 4.2)
  - [CYCLE-INSTRUCT: Fully Seed-Free Instruction Tuning via Dual Self-Training and Cycle Consistency](https://aclanthology.org/2025.emnlp-main.258.pdf)

### Associated with
- **Pairwise comparison** (behavioral indicator), 1 paper
  > AlpacaEval is a popular pairwise comparison framework that employs GPT-4-Turbo as the fixed baseline model. (Section 1)
  - [Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf)
- **AlpacaEval 2.0** (measurement instrument), 1 paper
  > “AlpacaEval is done with the AlpacaEval2 library”
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
