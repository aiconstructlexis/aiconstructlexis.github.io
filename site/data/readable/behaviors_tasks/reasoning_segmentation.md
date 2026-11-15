# Reasoning segmentation
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats reasoning segmentation as generating a pixel-level segmentation mask for an object or region in an image from a complex instruction or textual query, where identifying the target requires reasoning. The definitions are closely aligned, and one paper adds that the task 'demands higher capabilities in instruction comprehension.' Success is described as producing the pixel-level mask.

**Variants.** The papers use closely related names for the same behavior, including reasoning segmentation and Reasoning Segmentation (RS). A narrower characterization appears in one paper's relationship statement, which says that 'RS has reasoning ability, but only allows single object localization,' tying the task to single-object localization. Another paper discusses it alongside referring segmentation as a task setting where the approach is applied.

**Space of elicitation and scores.** One measurement instrument is linked to reasoning segmentation: ReasonSeg. Papers describe ReasonSeg as a benchmark dataset or benchmark for reasoning segmentation, and one quote says it 'evaluates the reasoning ability of the model.' Reported use includes benchmark scoring such as GIoU on ReasonSeg.

**What it is taken as evidence of.** Papers connect reasoning segmentation to one construct, Reasoning. That link is recorded as a related relationship rather than a causal or correlational one, but the language is consistent: one paper states that 'RS has reasoning ability,' and another says the benchmark is used to examine a model's reasoning capabilities. No other construct linkage appears, so the framing centers on reasoning.

## Sources

**Reasoning segmentation** (2 papers: [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf), [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf))
> The task of generating a pixel-level segmentation mask for an object or region in an image based on a complex, reasoning-based instruction.

## Relationships

### Reasoning segmentation →
- **ReasonSeg** (measurement instrument): *measured_by*, 3 papers
  > "ReasonSeg [31] evaluates the reasoning ability of the model"
  - [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
  - [MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8661ab3440964c27794607f0ea73624-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > RS has reasoning ability, but only allows single object localization. (Figure 2)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
- **Object localization** (behavioral indicator), 1 paper
  > RS has reasoning ability, but only allows single object localization. (Figure 2)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
