# Collective intelligence
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Collaborative intelligence  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats collective intelligence as a group-level advantage or capacity that emerges when multiple agents collaborate and do better than a single or isolated agent. One recurring version describes a latent advantage from agents jointly refining artifacts instead of relying on a single reasoning stream, while another says a multi-agent system can "surpass individual agent performance through coordinated collaboration and operator composition" (Multi-agent Architecture Search via Agentic Supernet). A closely aligned variant appears under the name collaborative intelligence, emphasizing effective combination of diverse, heterogeneous agents so the group achieves better problem solving than isolated agents.

**Space of facets.** The papers mostly organize the construct around a common contrast: collective or collaborative performance versus a single reasoning stream, singular-aspect reasoning, or isolated agents. They also use two near-overlapping names, collective intelligence and collaborative intelligence, with the latter stressing heterogeneous agents that "seamlessly collaborate to achieve greater intelligence and capabilities." Beyond these contrasts and naming choices, the definitions do not introduce further named facets or subtypes.

**Space of measurement.** The measurement space is sparse in the papers: no measurement instrument and no behavioral indicator are linked to the construct. As a result, operationalization is only implicit in the descriptions, through claims about multiple agents jointly refining artifacts, coordinated collaboration and operator composition, and better problem solving than isolated agents. No named benchmark, human evaluation, LLM-as-a-judge setup, or probe is tied to it here, so there is no separate measurement scheme to compare with the definitions.

**Links.** Only one linked construct appears in the relationships: one paper claims a causal relationship from collective intelligence to Robustness. It states that leveraging "the collective intelligence of both models" makes generated code "more robust and accurate" (DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation). No correlational or other related links are recorded.

## Sources

**Collective intelligence** (2 papers: [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf), [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf))
> The latent advantage that arises when multiple agents jointly refine artifacts rather than relying on a single reasoning stream.

**Collaborative intelligence** (1 paper: [Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c27bf8d56d3d50c7aeaf7535dee975-Paper-Conference.pdf))
> The capacity of a multi-agent system to combine diverse agents effectively so that the group achieves better problem solving than isolated agents.

## Relationships

### Collective intelligence →
- **Robustness** (construct): *causes*, 1 paper
  > By doing so, DebateCoder effectively leverages the collective intelligence of both models, making the generated code more robust and accurate. (Section 1)
  - [DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation](https://aclanthology.org/2025.acl-long.589.pdf)
