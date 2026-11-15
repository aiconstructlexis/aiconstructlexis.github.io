# DailyDialog
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across the surveyed work, the prevailing description is of a dataset of human-written dialogues or human conversation transcripts about everyday life, used to evaluate dialogue generation or conversational performance. Definitions variously say it covers "various topics of daily life," consists of "transcripts of conversations between humans," or comprises sequences of everyday conversations. A minority description adds that it contains 13,118 dialogues annotated with 7 emotions for emotion recognition and dialogue generation.

**What it is claimed to measure.** Papers use DailyDialog to measure one behavioral indicator, Dialogue generation, and do not link it to any constructs. The claims converge on dialogue generation rather than several outcomes: papers describe "dialogue generation with the DailyDialog dataset" and report using it to "assess performance in conversation scenarios."

**Space of uses.** Papers position it both as a case-study setting and as one dataset within multi-dataset evaluations. One line of work describes "a single setting as a case study: dialogue generation with the DailyDialog dataset," while other work evaluates systems across diverse datasets or dialogue datasets that include DailyDialog alongside LaMP, MetaICL, DialogSum, Topical-Chat, and Wizard of Wikipedia, plus one other dialogue dataset. No paper links it to another measurement instrument.

## Sources

**DailyDialog** (5 papers: [Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf), [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf), [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf), [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf), [Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.495.pdf))
> A dataset of human-written dialogues covering various topics of daily life, used for evaluating dialogue generation systems.

## Relationships

### → DailyDialog
- **Dialogue generation** (behavioral indicator): *measured_by*, 2 papers
  > we focus on a single setting as a case study: dialogue generation with the DailyDialog (Li et al., 2017) dataset
  - [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf)
  - [Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf)
