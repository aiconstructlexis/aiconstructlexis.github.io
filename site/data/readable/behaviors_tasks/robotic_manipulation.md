# Robotic manipulation
**Type:** Behavioral indicator  
**Supporting papers:** 28  
**Also known as:** Robotic control, Visuo-motor control, Robot manipulation, Object rearrangement, Object transport, Tabletop manipulation, Low-level manipulation, Multi-step manipulation, Object sorting, Embodied robotic control, Long-horizon manipulation, Pick and stack  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats robotic manipulation as producing control actions, action trajectories, or other physical actions that let a robot interact with objects and alter its environment to accomplish a specified goal. Most definitions place it in real or simulated embodied settings and often condition it on visual, textual, or language instructions, including visuo-motor control and embodied robotic control. Many papers then instantiate it as named continuous-control or tabletop tasks such as reaching, pushing, picking, sweeping, peg insertion, or pick and place, while some papers formulate it as rearranging, transporting, sorting, or stacking objects. Success is usually expressed as achieving the task goal, though one transport formulation scores success by the ratio of target objects successfully transported.

**Variants.** Papers study several variants under related names, including robot manipulation, robotic control, visuo-motor control, tabletop manipulation, low-level manipulation, multi-step manipulation, and long-horizon manipulation. The settings range from simulated control and tabletop environments to real-world robot-arm tasks, and from single-robot behaviors such as opening drawers, sweeping, or sorting items by category to coordinated object rearrangement or transport, including multi-floor and container-using scenarios. Some work also includes mobile-manipulation settings where a robot must pick up a named object from a receptacle, and one paper relates long-horizon manipulation with general instructions to instruction following because such tasks implicitly encapsulate multiple subtasks.

**Space of elicitation and scores.** Papers link robotic manipulation to 2 measurement instruments. The more recurrent instrument is Meta-World, described as a robotic manipulation benchmark suite and as a tabletop manipulation benchmark with ML-45, while RLBench appears as another linked instrument and is described as a simulator of a Franka robot performing tabletop manipulation. Both are described as benchmark or simulator environments.

**What it is taken as evidence of.** Instead of linking it to one agreed construct, papers connect robotic manipulation to 7 constructs. The linked constructs are instruction understanding, physical world understanding, sequential decision-making, spatial reasoning, and spatiotemporal reasoning, plus 2 others. In the recorded relationships, separate papers claim causal relationships from instruction understanding, physical world understanding, and spatiotemporal reasoning to robotic manipulation, while robotic manipulation is reported as related to sequential decision-making and spatial reasoning.

## Sources

**Robotic control** (1 paper: [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf))
> Producing control actions in a simulated robotics environment to achieve task goals.

**Robot manipulation** (1 paper: [HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3bfee3bc6639c36e6e7b058db909f760-Paper-Conference.pdf))
> The observable act of a robot interacting with and physically altering its environment to achieve a specified goal.

**Visuo-motor control** (1 paper: [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf))
> Producing robot action trajectories for manipulation tasks from visual and textual task inputs.

**Robotic manipulation** (3 papers: [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf), [Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luu25a/luu25a.pdf), [UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf))
> Performing continuous control manipulation tasks such as reaching, pushing, picking, sweeping, and peg insertion.

**Object rearrangement** (1 paper: [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf))
> A complex, observable task requiring agents to move one or more objects from their initial locations to specified goal locations, often involving multiple steps and coordination.

**Object transport** (2 papers: [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf), [Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf))
> The task of moving one or more objects from a starting location to a specified destination within a simulated environment, potentially using containers.

**Tabletop manipulation** (1 paper: [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf))
> The task of physically interacting with and rearranging objects on a flat surface like a table.

**Multi-step manipulation** (1 paper: [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf))
> The execution of a sequence of actions based on visual input to achieve a specific goal.

**Object sorting** (1 paper: [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf))
> The task of grasping multiple objects and placing them into designated areas based on their category.

**Low-level manipulation** (1 paper: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf))
> Controlling a robotic arm through fine-grained 7D action vectors to perform object interactions such as picking up or stacking, requiring accurate spatial and visual perception.

**Embodied robotic control** (1 paper: [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf))
> Executing physical manipulation tasks (e.g., pick and place) guided by language instructions in a real or simulated environment.

**Long-horizon manipulation** (1 paper: [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf))
> Executing multi-step robotic tabletop tasks that require completing a sequence of subtasks over extended horizons.

**Pick and stack** (1 paper: [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf))
> A robotics manipulation task where the model must generate a plan to grasp an object and place it on top of another object.

## Relationships

### Robotic manipulation →
- **Meta-World** (measurement instrument): *measured_by*, 3 papers
  > we verify the efficacy of KALM on two robotics manipulation environments: CLEVR-Robot [14] and Meta-world [15] (Section 1).
  - [KALM: Knowledgeable Agents by Offline Reinforcement Learning from Large Language Model Rollouts](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4cdb4090e04816422afcbb08d4badcf-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf)
  - [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf)
- **RLBench** (measurement instrument): *measured_by*, 1 paper
  > RLBench ... a simulator of a Franka robot performing tabletop manipulation
  - [HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3bfee3bc6639c36e6e7b058db909f760-Paper-Conference.pdf)

### → Robotic manipulation
- **World modeling** (construct): *causes*, 1 paper
  > In addition, 3D-VLA [60] and Daydreamer [56] have also tried to introduce world models into robot manipulation to help the models free themselves from a large amount of trial and error and improve learning efficiency. (Section 1)
  - [PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf)
- **Instruction understanding** (construct): *causes*, 1 paper
  > The strong task instruction understanding and visual grounding capabilities of MLLMs [5, 4] have exhibited great promise for language-instructed multitask robotic manipulation [7, 8, 9].
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Physical world understanding** (construct): *causes*, 1 paper
  > Furthermore, we investigate how physical world understanding helps the deployment of embodied agents through extensive robotic manipulation experiments on MOKA (Liu et al., 2024a). (Section 1)
  - [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)
- **Spatiotemporal reasoning** (construct): *causes*, 1 paper
  > We hypothesize that this will effectively provide spatial and temporal relations necessary for improving manipulation tasks (Wen et al., 2023; Yuan et al., 2024). (1 INTRODUCTION)
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)

### Associated with
- **Instruction following** (behavioral indicator), 1 paper
  > "Long-horizon manipulation tasks with general instructions often implicitly encapsulate multiple sub-tasks, posing significant challenges in instruction following"
  - [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf)
- **Spatial reasoning** (construct), 1 paper
  > Pick and stack is a classic robotics task. ... This task demands advanced spatial reasoning
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **Visual grounding** (construct), 1 paper
  > The strong task instruction understanding and visual grounding capabilities of MLLMs [5, 4] have exhibited great promise for language-instructed multitask robotic manipulation [7, 8, 9].
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Sequential decision-making** (construct), 1 paper
  > Many of these tasks, such as natural language dialogue or robotic control, require complex sequential decision-making. (Section 1)
  - [Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9531a3e64e6167c7e1e671157082682-Paper-Conference.pdf)
