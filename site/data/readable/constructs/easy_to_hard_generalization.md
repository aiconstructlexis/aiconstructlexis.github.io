# Easy-to-hard generalization
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Simple-to-hard generalization, Transferability, Logical extrapolation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats easy-to-hard generalization as generalizing from easier, simpler, or smaller training cases to harder, larger, or more complex unseen cases, often with no direct supervision on the harder cases. Definitions differ on whether this is a latent model ability or a training and evaluation paradigm: some describe it as "the latent ability" to perform on more complex instances, while others describe a setup where human annotation is provided only for easier tasks, or where models are trained on SIMPLE examples and evaluated on HARD examples. A narrower formulation recasts the same pattern as transferability from simpler circuits to circuits with more components.

**Space of facets.** Papers use several nearby labels for overlapping uses, including simple-to-hard generalization, logical extrapolation, and transferability. The main organizing axis is task difficulty or size: one paper explicitly says simple-to-hard generalization is a type of length generalization, while another frames the phenomenon as solving problems of greater size and difficulty than those in training. Another distinction is scope, with broader formulations spanning arithmetic, maze, string manipulation, text, and image settings, alongside a circuits-specific formulation.

**Space of measurement.** Operationalization is sparse in the linked measures: papers link the construct to 1 measurement instrument and no behavioral indicators. The only linked instrument is MATH, described as a much harder dataset used to evaluate easy-to-hard generalization, so the reported measurement is a harder-task dataset evaluation. That operationalization matches the dominant definitions' focus on performance transfer to harder instances, but it is narrower than definitions that also discuss other task families.

**Links.** It is related to 3 constructs. The most common related construct is Length generalization: papers connect the construct to solving longer, larger, or more difficult instances than those seen in training, and one paper states that simple-to-hard generalization is a type of length generalization. It is also related to Modality imbalance, in work contrasting stronger text generalization with failures on images, and to Mathematical reasoning, where a paper selects that domain to evaluate easy-to-hard generalization.

## Sources

**Easy-to-hard generalization** (1 paper: [Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25d/lee25d.pdf))
> The ability of a model to learn to solve difficult problems by training on solutions to simpler problems, without requiring direct supervision on the harder instances.

**Simple-to-hard generalization** (1 paper: [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf))
> The latent ability of a model to generalize from training on simpler instances of a task to performing well on more complex, unseen instances, particularly involving longer or more intricate reasoning chains.

**Transferability** (1 paper: [LaMAGIC2: Advanced Circuit Formulations for Language Model-Based Analog Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25b/chang25b.pdf))
> The model's ability to generalize its performance from training on simpler circuits to generating more complex circuits with a larger number of components.

**Logical extrapolation** (1 paper: [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf))
> The ability to solve problems that are larger and more complex than those seen in the training data.

## Relationships

### Easy-to-hard generalization →
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > We evaluate these verifiers on the GSM8K test set as well as their easy-to-hard generalization on much harder MATH dataset (Hendrycks et al., 2021) (Section 4)
  - [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf)

### Associated with
- **Length generalization** (construct), 2 papers
  > “we investigate whether these models are capable of logical extrapolation—can they solve problems of greater size and difficulty than those that appear in their training set?”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)
- **Modality imbalance** (construct), 1 paper
  > We observe that current models can S2H generalize on text – when trained to read short sequences from small LaTeX-formatted tables, the models can read longer paths from larger tables, also provided in LaTeX code. However, they fail to length-generalize on images. To address the generalization gap and imbalanced learning of different modalities, our goal is to transfer the generalization behavior from text to image modality. (Figure 1)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > "we select mathematical reasoning to evaluate easy-to-hard generalization ability"
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
