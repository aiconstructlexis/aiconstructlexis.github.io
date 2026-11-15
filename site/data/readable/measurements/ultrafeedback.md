# UltraFeedback
**Type:** Measurement instrument  
**Supporting papers:** 66  
**Also known as:** Ultrafeedback, Ultra-Feedback  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats UltraFeedback as a high-quality instruction or preference dataset for alignment work, built from scored candidate responses and used for instruction tuning. Definitions also describe it as a preference learning benchmark with annotated preference labels over instruction-response pairs, sometimes emphasizing fine-grained or multi-aspect evaluation around instruction following, truthfulness, honesty, and helpfulness. A smaller line of work frames it more specifically as a public benchmark for generative judges on preference prediction, and some papers refer to particular variants or subsets such as a development split or an auxiliary text generation setting.

**What it is claimed to measure.** Papers link UltraFeedback to 5 constructs and 2 behavioral indicators, so its reported measurement use is spread across several related targets rather than concentrated on one alone. The most frequent construct links are to helpfulness, honesty, instruction following ability, generalization, and truthfulness, and the recorded behavioral-indicator links are to instruction following and dialogue generation. In these relationships, papers use UltraFeedback as measuring these qualities or behaviors, often in multi-aspect alignment settings.

**Space of uses.** Papers position UltraFeedback both as training data and as an evaluation benchmark: it is used for instruction tuning, preference learning, training and evaluating reward models and aligned language models, testing generative judges on preference prediction, and running additional fine-grained text generation experiments. Some works use a development split for alignment evaluation or hyperparameter selection, while others use its prompts for best-of-n alignment experiments and RAFT-style finetuning. No other measurement instrument is linked to it.

## Sources

**Ultrafeedback** (3 papers: [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf), [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf))
> A high-quality instruction dataset built from scored candidate responses and used for instruction tuning.

**UltraFeedback** (5 papers: [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf), [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf), [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.51.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf))
> A public benchmark used to evaluate generative judges on preference prediction.

**Ultra-Feedback** (1 paper: [Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf))
> Ultra-Feedback dataset used for additional fine-grained text generation experiments.

## Relationships

### → UltraFeedback
- **Helpfulness** (construct): *measured_by*, 3 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
  - [Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.696.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 3 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
- **Honesty** (construct): *measured_by*, 2 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.696.pdf)
- **Instruction following ability** (construct): *measured_by*, 2 papers
  > we evaluate DISTILLM-2 for general purpose instruction-following task on AlpacaEval (Li et al., 2023), Evol-Instruct (Xu et al., 2024a), and UltraFeedback (Cui et al., 2024).
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
- **Truthfulness** (construct): *measured_by*, 1 paper
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Dialogue generation** (behavioral indicator): *measured_by*, 1 paper
  > We further conduct experiments on tasks such as conditional generation (IMDB) and dialogue (Anthropic HH, UltraFeedback). (Section 5)
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
