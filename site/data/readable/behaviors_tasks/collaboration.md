# Collaboration
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Cooperation, Collaborative discussion, Iterative discussion, Multi-turn discussion, Message exchange, Collaborative problem solving, Spontaneous cooperation, Cooperative perception, Collaborative task completion, Multi-agent coordination, Cooperative decision-making, Collective decision-making, Multi-agent cooperation, Multi-turn collaborative task completion, Cooperation efficiency, Collaborative decision-making  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats collaboration as an observable multi-agent process: agents exchange messages over several rounds, share opinions or feedback, and work toward a consensus, shared answer, joint output, or plan. Papers describe this as an "iterative discussion process aimed at reaching a consensus," as agents who "exchange messages before the verifier decides," or as interaction to jointly solve a problem. A smaller line of work uses the term for cooperative choice in games, where success is selecting actions such as Cooperate, Silent, or Option A that maximize mutual benefit, system reward, or collective welfare, sometimes without explicit communication. Other papers frame it by successful joint task completion or by cooperative perception in embodied settings.

**Variants.** Terminology varies, with recurring labels including cooperation, collaborative discussion, multi-turn discussion, collective decision-making, and collaborative task completion. The behavior is studied in medical decision-making and social science coding, in economic and social dilemma games, in embodied settings such as perception for manipulation, and in systems where outputs are aggregated across a communication topology. One paper also reports collaboration as related to plan generation, describing agents that collaboratively create and refine meta-plans through multi-turn discussion.

**Space of elicitation and scores.** Only one measurement instrument is linked to collaboration, AgentBench. One paper presents it as a benchmark comprising multiple tasks that require different LLMs within a system to cooperate and discuss. No other instrument is linked.

**What it is taken as evidence of.** The only construct linked to collaboration is Reasoning. The recorded relationship is causal from Reasoning to Collaboration, with one paper claiming that reasoning models "reduce cooperation and norm enforcement, favoring individual rationality." No other construct link is recorded, so papers do not present multiple construct framings for what collaboration reflects.

## Sources

**Cooperation** (2 papers: [GTBench: Uncovering the Strategic Reasoning Capabilities of LLMs via Game-Theoretic Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/3191170938b6102e5c203b036b7c16dd-Paper-Conference.pdf), [Moral Alignment for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2b1bad4756ceee8f408e16b8e6e4383-Paper-Conference.pdf))
> Choosing actions that maximize mutual benefit or system reward, such remaining silent in Prisoner's Dilemma.

**Collaborative discussion** (2 papers: [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf), [SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention](https://aclanthology.org/2025.acl-long.416.pdf))
> Multi-agent exchange of opinions and arguments to reach a shared medical answer.

**Multi-turn discussion** (1 paper: [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf))
> An interactive process where multiple agents exchange messages over several rounds to share information, provide feedback, and reach a consensus on a plan.

**Message exchange** (1 paper: [Neural Interactive Proofs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d55b8d2f6f6e6d130cbda350ff2a123c-Paper-Conference.pdf))
> Sending and receiving messages across rounds between prover and verifier agents before a final decision is made.

**Collaborative problem solving** (1 paper: [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf))
> The observable process of a team of two or more agents engaging in interaction to jointly solve a given problem.

**Iterative discussion** (1 paper: [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf))
> The observable, multi-turn conversational exchange between agents as they work on a task.

**Cooperative perception** (1 paper: [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf))
> The observable task where multiple agents collaborate to perceive the environment, such as one agent locating an object for another agent to manipulate.

**Spontaneous cooperation** (1 paper: [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf))
> Selecting cooperative actions without explicit communication that increase collective welfare.

**Collaborative task completion** (1 paper: [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://aclanthology.org/2025.emnlp-main.249.pdf))
> The observable outcome where two or more agents successfully work together to achieve a shared goal within the given constraints.

**Cooperative decision-making** (1 paper: [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf))
> The observable act of choosing to allocate resources or act in ways that benefit others at a cost to oneself in economic games.

**Collective decision-making** (1 paper: [Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems](https://aclanthology.org/2025.emnlp-main.623.pdf))
> The observable process by which multiple LLM agents interact through a communication topology to produce a final joint output or answer to a query.

**Multi-agent cooperation** (1 paper: [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf))
> The observable interaction where multiple distinct AI agents work together, communicate, and coordinate actions to solve a problem.

**Cooperation efficiency** (1 paper: [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf))
> The degree to which multiple agents coordinate their actions to complete a joint task with minimal redundancy and wasted effort.

**Collaborative decision-making** (1 paper: [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf))
> An observable process where multiple agents engage in discussion to jointly devise a strategy or plan of action.

## Relationships

### Collaboration →
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > AgentBench (Liu et al., 2023) and AgentGym (Xi et al., 2024) comprise multiple tasks requiring different LLMs within the system to cooperate and discuss
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)

### → Collaboration
- **Reasoning** (construct): *causes*, 1 paper
  > We find that reasoning models consistently reduce cooperation and norm enforcement, favoring individual rationality. (Abstract)
  - [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf)

### Associated with
- **Plan generation** (behavioral indicator), 1 paper
  > CaPo enables agents to collaboratively create and refine long-term, strategic, and coherent meta-plans through multi-turn discussions.
  - [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf)
