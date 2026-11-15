# MineDojo
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the definitions, the prevailing usage is as a Minecraft-based simulation suite for embodied-agent research, often also described as a benchmark or research framework. Papers consistently describe it as containing thousands of open-ended, natural language-specified or language-prompted tasks, with task content commonly framed around navigation, harvesting, combat, and crafting. A smaller difference in wording is whether authors call it a benchmark or a framework, and some work uses selected long-horizon tasks from it rather than the full suite.

**What it is claimed to measure.** Papers link it to one construct and one behavioral indicator. The construct claim is Generalization: one paper reports that validating a single model on diverse challenging tasks in MineDojo indicates promising generalization. The behavioral indicator claim is Navigation, and the benchmark is also described as supporting behaviors such as navigation, harvest, combat, and craft, though only Navigation is explicitly linked as a measured behavior.

**Space of uses.** No measurement instrument is linked to it. In practice, papers use it to validate embodied-agent methods: one study evaluates in both MineDojo and Mineflayer environments, and another validates on selected long-horizon tasks from MineDojo. Papers also describe it as suitable for studying open-ended and generally capable embodied agents.

## Sources

**MineDojo** (2 papers: [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf), [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf))
> Simulation suite and benchmark for open-ended embodied agents in Minecraft, featuring thousands of natural language-specified tasks across navigation, harvesting, combat, and crafting.

## Relationships

### → MineDojo
- **Navigation** (behavioral indicator): *measured_by*, 1 paper
  > The behaviors that can be conducted in MineDojo primarily include navigation, harvest, combat, and craft.
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We validate our method in both MineDojo (Fan et al., 2022) and Mineflayer (PrismarineJS., 2013) environments. The experimental results suggest that our method completes diverse challenging tasks with a single model, indicating its promising generalization. (Section 1)
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)
