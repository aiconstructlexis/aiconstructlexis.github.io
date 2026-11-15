# Task interference
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Negative transfer, Inter-task interference, Parameter interference  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats task interference as a latent degradation phenomenon that appears when models are trained, fine-tuned, or merged across multiple tasks: performance on some tasks worsens because learning signals, shared parameters, or required representations conflict. Most definitions keep this broad framing, while some rename it as negative transfer, parameter interference, or inter-task interference and narrow the source of conflict to diverse or unrelated tasks or instances, checkpoint or source-model merging, or language-pair updates. Across definitions, the common element is performance degradation, while the point of emphasis shifts between conflict among tasks, among parameters, and among specific data or language slices.

**Space of facets.** Papers most often organize the construct by source and setting: multi-task learning with diverse mixtures of tasks, joint training of control and understanding tasks, model or checkpoint merging, and multilingual fine-tuning where updates for one language pair can hurt others. Within these framings, neighboring names are used for variants of the same general pattern, negative transfer when training on diverse or unrelated tasks or instances hurts performance instead of producing synergistic learning, parameter interference when constituent models or parameter updates conflict, and inter-task interference when one task's learned capability harms another. One paper also names a narrower case, "partial task interference."

**Space of measurement.** No measurement instrument is linked to it. Instead, papers operationalize it through observed performance degradation, for example when a generalist model underperforms a specialist model on most VL tasks, when merged models show performance loss or a gap relative to expert models, or when "competing control and understanding tasks degrade performance when trained jointly"; one analysis-oriented description says inter-task interference is measured by changes in internal activations induced by merging. It is linked to 2 behavioral indicators, catastrophic forgetting and object detection, but those links are presented as a related phenomenon and a claimed cause rather than as measured_by links.

**Links.** Across reported links, papers connect task interference to 3 constructs and 2 behavioral indicators. One paper claims a causal relationship from object detection to task interference, in a setting where learning distinct granularities such as instance-level perception and logical reasoning may lead to interference; other papers claim causal relationships from task interference to multimodal understanding and to multi-task ability, using language of degraded performance under joint training or unified model merging. Separate papers report that task interference is related to catastrophic forgetting, because fine-tuned task vectors lose generalization ability and interfere when merged, and is related to graceful forgetting, presented as an approach to the negative-transfer problem.

## Sources

**Task interference** (3 papers: [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf), [LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf), [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf))
> A latent phenomenon in multi-task learning where a model's performance on certain tasks degrades due to conflicting learning signals from being trained on a diverse mixture of other tasks.

**Negative transfer** (2 papers: [Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf), [Modeling Multi-Task Model Merging as Adaptive Projective Gradient Descent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25k/wei25k.pdf))
> A phenomenon where training on diverse or unrelated tasks or data instances leads to a degradation in model performance, as opposed to synergistic learning.

**Parameter interference** (2 papers: [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf), [MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation](https://aclanthology.org/2025.acl-long.762.pdf))
> A latent phenomenon in model merging where parameter conflicts between different source models cause performance degradation in the final unified model.

**Inter-task interference** (1 paper: [No Task Left Behind: Isotropic Model Merging with Common and Task-Specific Subspaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/marczak25a/marczak25a.pdf))
> The phenomenon where the process of learning or combining capabilities for one task negatively impacts performance on other tasks within a multi-task model.

## Relationships

### Task interference →
- **Multimodal understanding** (construct): *causes*, 1 paper
  > “task interference, where competing control and understanding tasks degrade performance when trained jointly.”
  - [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf)
- **Multi-task ability** (construct): *causes*, 1 paper
  > Model merging seeks to integrate task-specific expert models into a unified architecture while preserving multi-task generalization capabilities, yet parameter interference between constituent models frequently induces performance degradation. (Abstract)
  - [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf)

### → Task interference
- **Object detection** (behavioral indicator): *causes*, 1 paper
  > simultaneously learning to acquire knowledge at distinct granularities, such as the instance-level perception (e.g., object detection) and logical reasoning (e.g., VQA), may lead to significant interference. (Section 1)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)

### Associated with
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > Task interference is linked to catastrophic forgetting, as the individual task vectors lose a significant amount of generalization ability to other tasks after fine-tuning and merging them leads to interference among each other (Section 5.2).
  - [LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf)
- **Graceful forgetting** (construct), 1 paper
  > Some of the knowledge may actually bring detrimental effects to the fine-tuning tasks, which is also known as negative transfer. To address this problem, graceful forgetting has emerged as a promising approach. (Abstract)
  - [Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.666.pdf)
