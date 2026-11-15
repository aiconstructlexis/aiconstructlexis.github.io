# Preference ranking
**Type:** Behavioral indicator  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats preference ranking as comparing candidate responses and determining which output is preferred under human judgments. Most formulations are pairwise: papers describe choosing between two candidate responses, training models to assign higher likelihoods to the preferred response than to a dispreferred one, or assigning scalar rewards to two outputs and ordering them by the score difference. A broader definition also describes ranking or selecting a preferred output from a set of options according to human preferences.

**Variants.** Variants are mostly different ways of setting up the same preference comparison task. Papers variously frame it as prompts with pairs of human-ranked responses, as likelihood-based ordering of a preferred versus dispreferred response, and as reward-based ranking where each response receives a scalar score before comparison. A smaller framing describes ranking or selecting a preferred output from a larger set of options, and one paper reports the task across eight tasks.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument. The only named instrument is ArmoRM, which one paper relates to preference ranking by describing it as a reward model used to score and rank responses. Outside named instruments, scoring is also described through ranking accuracy and through ordering two responses by the difference between their scalar reward scores.

**What it is taken as evidence of.** Papers do not link this behavior to any construct.

## Sources

**Preference ranking** (4 papers: [Enhancing RLHF with Human Gaze Modeling](https://aclanthology.org/2025.emnlp-main.1559.pdf), [Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf), [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf))
> The observable task of ranking or selecting a preferred output from a set of options according to human judgments.

## Relationships

### Associated with
- **ArmoRM** (measurement instrument), 1 paper
  > “ArmoRM-Llama-3-8B-v0.1 (Wang et al., 2024a) is then employed as the reward model to score and rank these responses.”
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
