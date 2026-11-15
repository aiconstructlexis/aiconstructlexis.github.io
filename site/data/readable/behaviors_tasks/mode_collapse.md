# Mode collapse
**Type:** Behavioral indicator  
**Supporting papers:** 7  

## State of the Field

**Space of definitions.** In the one definition, mode collapse is treated as an observable failure mode in knowledge distillation, where a student model's output distribution becomes overly focused on the teacher's dominant modes and ignores less frequent, potentially important information. The accompanying quoted passage uses the same framing, saying the student focuses only on the dominant modes of the teacher distribution, so the behavior is identified by this narrowed output distribution.

**Variants.** Most of the direct definitional detail comes from distillation, but some papers use the same label in broader generation settings. There it is described as LLMs repeatedly generating the same few completions, reduced across-input diversity under RLHF fine-tuning, or a learned model focusing on only a limited subset of the true data distribution.

**Space of elicitation and scores.** No measurement instrument is linked to it. The papers describe the behavior through concentration on dominant modes and reduced diversity, rather than through a named instrument that elicits or scores it.

**What it is taken as evidence of.** Papers connect mode collapse only to generation diversity. One paper claims a causal relationship from mode collapse to generation diversity, describing repeated generation of the same few completions as limiting diversity, while other papers describe mode collapse as related to reduced or across-input diversity without making the link causal.

## Sources

**Mode collapse** (1 paper: [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf))
> An observable failure mode in knowledge distillation where a student model's output distribution becomes overly focused on only the dominant modes of the teacher's distribution, ignoring less frequent but potentially important information.

## Relationships

### Mode collapse →
- **Generation diversity** (construct): *causes*, 3 papers
  > Large Language Models (LLMs) often suffer from mode collapse, repeatedly generating the same few completions even when many valid answers exist, limiting their diversity across a wide range of tasks.
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
  - [Representative Language Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/peale25a/peale25a.pdf)
