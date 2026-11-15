# UltraInteract
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the definitions here, UltraInteract is described as multi-turn conversational data built around complex reasoning tasks. Papers differ in how they characterize its format and role: some describe a multi-turn RLHF dataset with dialogues that cover general chat scenarios and are used to evaluate conversational and instruction-following abilities, while another description presents it as a pairwise alignment dataset of multi-turn conversational data designed to evaluate and improve performance on complex reasoning tasks.

**What it is claimed to measure.** Recorded links do not spread across many named outcomes: UltraInteract is linked to 1 construct, Reasoning, and to no behavioral indicators. That construct link is reported as related rather than as a measured_by claim, while the definitions and quoted passages say papers use UltraInteract to evaluate conversational ability, instruction-following ability, and performance on complex reasoning tasks.

**Space of uses.** Papers use UltraInteract both as an evaluation benchmark and as training or alignment data. In one usage, a method is evaluated on responses to instructions with complex reasoning tasks that cover general chat scenarios, and in another, models are fine-tuned on UltraInteract as pairwise alignment data; no measurement instrument is linked to it.

## Sources

**UltraInteract** (2 papers: [Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/186094ef879dcbd5ef6879782916c309-Paper-Conference.pdf), [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf))
> A multi-turn RLHF dataset containing dialogues with complex reasoning tasks, used to evaluate a model's conversational and instruction-following abilities.

## Relationships

### Associated with
- **Reasoning** (construct), 1 paper
  > "We consider fine-tuning Mistral-7B and Mistral-8×7B models on UltraInteract [44], a pairwise alignment dataset specifically designed for complex reasoning tasks."
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
