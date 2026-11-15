# Task adaptation
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Task-specific adaptation, Task adaptability  

## State of the Field

**Space of definitions.** Across papers, the construct is used for several kinds of model adjustment rather than one settled meaning. The prevailing usages split between adaptation to a downstream task through parameter modification or structured weight changes, often with preservation of general capabilities from pretraining, and inference-time behavior adaptation through injected vectors instead of parameter updates. Smaller lines of work cast it as continual adaptation to new tasks in a sequential setting while retaining previously learned knowledge, or as adjustment of neuronal representations to capture task-specific input patterns in an orthogonal subspace. The main disagreements are whether adaptation happens through parameter updates or without them, whether it is framed at the level of behavior, weights, or neuronal representations, and whether it targets a single downstream task or a sequence of new tasks.

**Space of facets.** When papers unpack the construct, they usually do so by the locus or mechanism of adaptation. Some describe task-specific directions in the pre-trained weight matrix that change under fine-tuning for a task, while another decomposes task-specific representations into complementary neuronal subspaces that regulate input sensitivity and task adaptability, with the orthogonal complementary subspace described as representing novel task-specific adaptations. Other work frames the construct through inference-time intervention built from latent representations, or through continual adaptation with dynamic capacity and retention of previously learned knowledge. The labels Task adaptation, Task-specific adaptation, and Task adaptability are therefore used for related but not identical formulations.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to the construct. Papers instead discuss it through adaptation procedures or analyses, including injected vectors at inference time, LoRA construction or parameter modification for downstream tasks, task-specific directions in weight space, and neuronal-subspace decomposition, but none of these are recorded as named measures.

**Links.** Papers do not report causal, correlational, or other related links for this construct, and it is not linked to any other construct.

## Sources

**Task adaptation** (2 papers: [Beyond Demonstrations: Dynamic Vector Construction from Latent Representations](https://aclanthology.org/2025.emnlp-main.297.pdf), [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf))
> The latent property of adapting an LLM’s behavior at inference time to a task using injected vectors rather than parameter updates.

**Task-specific adaptation** (2 papers: [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [Text-to-LoRA: Instant Transformer Adaption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/charakorn25a/charakorn25a.pdf))
> The latent ability of a model to adjust its parameters effectively for a particular downstream task while preserving general capabilities from pretraining.

**Task adaptability** (1 paper: [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf))
> The latent ability of a model to adjust its neuronal representations to capture task-specific input patterns introduced during fine-tuning, particularly in the orthogonal subspace relative to pre-trained weights.
