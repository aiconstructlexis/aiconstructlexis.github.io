# Multi-task ability
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Multi-task capability, Multi-task learning  

## State of the Field

**Space of definitions.** Available definitions consistently treat multi-task ability as a model-level ability to perform multiple tasks effectively within a single model. The broad agreement is on cross-task performance, but the scope varies: one definition explicitly casts it as the latent ability of a merged model to retain task performance after specialist models are combined, while another uses the broader multi-task learning framing of performing well on multiple, distinct tasks simultaneously, often through shared knowledge between them. One study describes the merged-model version as creating models that "effectively maintain multi-task capabilities."

**Space of facets.** Papers do not provide a richer subtype scheme, but they use nearby labels such as "multi-task capability" and "multi-task learning" for closely related usages. One usage is specific to model merging, where combining multiple models into one should enable the model to perform multiple tasks, while another places it on the seen-task side of a distinction between "seen (i.e., multi-task learning) and unseen (i.e., zero-shot generalization) tasks."

**Space of measurement.** Operationalization is benchmark-based. Papers link the construct to two measurement instruments, Super-NaturalInstructions and SuperGLUE, described in one study as "two publicly available multitasking benchmarks," and no behavioral indicators are linked. This keeps measurement at the level of performance across multiple tasks, which matches the shared emphasis in the definitions.

**Links.** A paper claims a causal relationship from task interference to multi-task ability, reporting that parameter interference between constituent models "frequently induces performance degradation" when model merging aims to preserve multi-task generalization capabilities.

## Sources

**Multi-task capability** (1 paper: [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf))
> The latent ability of a merged model to retain and perform multiple tasks effectively after combining specialist models.

**Multi-task learning** (1 paper: [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf))
> The ability of a model to perform well on multiple, distinct tasks simultaneously, often by sharing knowledge between them.

## Relationships

### Multi-task ability →
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 1 paper
  > “we conducted experiments on two publicly available multitasking benchmarks: SuperGLUE (Wang et al., 2019) and Super Natural-Instructions (Super NI) (Wang et al., 2022).”
  - [Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a692a24dbc744fca340b9ba33bc6522-Paper-Conference.pdf)
- **SuperGLUE** (measurement instrument): *measured_by*, 1 paper
  > “we conducted experiments on two publicly available multitasking benchmarks: SuperGLUE (Wang et al., 2019) and Super Natural-Instructions (Super NI) (Wang et al., 2022).”
  - [Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a692a24dbc744fca340b9ba33bc6522-Paper-Conference.pdf)

### → Multi-task ability
- **Task interference** (construct): *causes*, 1 paper
  > Model merging seeks to integrate task-specific expert models into a unified architecture while preserving multi-task generalization capabilities, yet parameter interference between constituent models frequently induces performance degradation. (Abstract)
  - [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf)
