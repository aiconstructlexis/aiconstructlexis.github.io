# BabyAI
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across the papers, BabyAI is most commonly described as a procedurally generated, partially observable 2D gridworld for evaluating agent capabilities on tasks given as textual or visual goals, especially navigation and object manipulation. Some authors describe it more specifically as an interactive 20x20 grid with a limited sight range for text-based agent evaluation, while others frame it as a grid-world benchmark with discrete navigation and interaction actions where an agent completes an instruction, including evaluation on instructions rephrased with synonyms.

**What it is claimed to measure.** Papers link BabyAI to 3 behavioral indicators and no constructs. The prevailing measurement use is Navigation, with papers describing grid-world tasks in which agents navigate and interact with objects, and one paper referring to five types of navigation tasks. Smaller lines of work use it to measure Embodied planning and Instruction following, including natural language goal instructions such as Go to the tile (3,2) and Look behind the green locked door.

**Space of uses.** No measurement instrument is linked to it. Across the papers, BabyAI is used as an embodied or grid-world evaluation setting in both text-based and multimodal configurations: one paper places it under embodied evaluation, another reports visual-observation zero-shot use and says the approach operates across multiple modalities in BabyAI domains, and other descriptions center instruction completion in a discrete action space.

## Sources

**BabyAI** (3 papers: [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf), [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf), [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf))
> A procedurally-generated, partially-observable 2D gridworld environment used to evaluate agent capabilities on tasks specified by textual or visual goals, such as navigation and object manipulation.

## Relationships

### → BabyAI
- **Navigation** (behavioral indicator): *measured_by*, 1 paper
  > BabyAI [60]: BabyAI is a grid world task where an agent navigates and interacts with objects to complete an instruction.
  - [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf)
- **Embodied planning** (behavioral indicator): *measured_by*, 1 paper
  > Babyai for embodied planning (Section 4.2)
  - [AgentRM: Enhancing Agent Generalization with Reward Modeling](https://aclanthology.org/2025.acl-long.945.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > BabyAI is a grid world platform for instruction following where an agent receives natural language goal instructions such as: “Go to the tile (3,2)” or “Look behind the green locked door”. (Section 5)
  - [The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pouplin25a/pouplin25a.pdf)
