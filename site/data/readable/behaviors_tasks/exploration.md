# Exploration
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Action exploration  

## State of the Field

**Space of definitions.** Across the definitions, papers treat exploration as action exploration: selecting and trying different actions within a search or learning process to discover their outcomes and potential rewards. The accompanying quoted passages place this behavior in planning settings, asking whether LLMs can "enhance action exploration within MCTS planning" and describing integration with MCTS for "complex textual interactive tasks."

**Variants.** The main named variant is action exploration. Beyond that name, papers discuss it in MCTS planning and complex textual interactive tasks, and related work mentions text-based games and in-context exploration.

**Space of elicitation and scores.** No measurement instrument is linked to it. The only explicit elicitation claim in the linked evidence is that one paper claims a causal relationship from Chain of thought to Exploration, in a setup using an "enhanced" prompt that provides a hint to explore, summarizes interaction history, and asks for zero-shot chain-of-thought reasoning.

**What it is taken as evidence of.** Papers do not converge on a single construct connection for exploration. Among the two linked constructs, one paper reports that Exploration is related to Exploitation, described as maintaining a dynamic balance between the two, while one paper claims a causal relationship from Openness to Exploration, stating that agents high in Openness "engage in more extensive exploration."

## Sources

**Action exploration** (1 paper: [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf))
> The behavior of selecting and trying out different actions within a search or learning process to discover their outcomes and potential rewards.

## Relationships

### → Exploration
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > The single configuration that succeeds in our experiments involves a combination of GPT-4 and an “enhanced” prompt that (a) provides a suggestive hint to explore, (b) externally summarizes the history of interaction into per-arm averages, and (c) asks the LLM to use zero-shot chain-of-thought reasoning [74, 41]. (Introduction)
  - [Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf)
- **Openness** (construct): *causes*, 1 paper
  > agents exhibiting high Openness—characterized by curiosity, adventurousness, and a propensity for novel experiences—consistently engage in more extensive exploration, undertake more interactions, and achieve higher game scores. (Sec 1)
  - [Persona Dynamics: Unveiling the Impact of Persona Traits on Agents in Text-Based Games](https://aclanthology.org/2025.acl-long.1515.pdf)

### Associated with
- **Exploitation** (construct), 1 paper
  > maintaining a dynamic balance between exploration and exploitation is essential throughout the self-improving process. (Section 2.2)
  - [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://proceedings.iclr.cc/paper_files/paper/2025/file/c8db30c6f024a3f667232ed7ba5b6d47-Paper-Conference.pdf)
