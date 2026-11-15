# Navigation
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Grid world navigation, Low-level navigation  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is goal-directed movement through an environment to reach a specified location, landmark, receptacle, or resource. Definitions commonly describe locating targets such as trees, cows, stones, underground resources, buildings, or receptacles, and another recurring formulation is simply reaching specific locations in a game environment. A smaller line of work uses the term more broadly for understanding spatial layouts and planning or describing routes between locations or to objects.

**Variants.** Papers study several named variants. In the Minecraft environment, navigation includes navigating on the ground, digging to a specific level, and exploring underground horizontally, while city-space work treats it as navigation sub-tasks that identify the nearest navigation point on a map and can be written as Navigation(building_1, west). Other variants are grid world navigation with up, down, left, and right actions, low-level navigation with translational, rotational, and camera-tilt controls, and room-to-room or object-retrieval navigation tasks.

**Space of elicitation and scores.** Papers link navigation to 3 measurement instruments: BabyAI, MineDojo, and TextWorld. These operationalize it as a grid world task where an agent navigates and interacts with objects to complete an instruction, a text-based game where the agent explores mazes and interacts with everyday objects through natural language, and MineDojo, where navigation is one of the behaviors the environment supports alongside harvest, combat, and craft.

**What it is taken as evidence of.** Papers do not directly present navigation as evidence of multiple constructs. The only linked construct is Long-horizon planning, which one paper reports as related to navigation by making navigation sub-tasks part of a plan and describing them as enabling efficient access to specific areas while narrowing the exploration scope. No other construct link is recorded.

## Sources

**Navigation** (4 papers: [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf), [MaestroMotif: Skill Design from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/2dc5a0faac8102fd47363795f71126ee-Paper-Conference.pdf), [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf), [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf))
> Moving through the Minecraft environment to locate targets such as trees, cows, stones, or underground resources.

**Grid world navigation** (1 paper: [LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ruoss25a/ruoss25a.pdf))
> Moving a player through a grid world with up, down, left, and right actions to reach a target location.

**Low-level navigation** (1 paper: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf))
> Executing precise movement and orientation adjustments in a simulated environment to reach a target location or object, using atomic actions like moving forward or rotating.

## Relationships

### Navigation →
- **BabyAI** (measurement instrument): *measured_by*, 1 paper
  > BabyAI [60]: BabyAI is a grid world task where an agent navigates and interacts with objects to complete an instruction.
  - [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf)
- **TextWorld** (measurement instrument): *measured_by*, 1 paper
  > An entirely text-based game with no visual component, where the agent has to explore mazes and interact with everyday objects through natural language
  - [BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0b1515be276f6ba82b4f2b25e50bef0-Paper-Conference.pdf)
- **MineDojo** (measurement instrument): *measured_by*, 1 paper
  > The behaviors that can be conducted in MineDojo primarily include navigation, harvest, combat, and craft.
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)

### Associated with
- **Long-horizon planning** (construct), 1 paper
  > Based on these requirements, a plan is created consisting of three distinct types of sub-tasks: ... (3) Navigation sub-tasks enable efficient access to specific areas, thereby narrowing the exploration scope. (Section 3.2)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
