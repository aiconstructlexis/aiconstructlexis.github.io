# Prompt injection
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Indirect prompt injection, Indirect prompt attack  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats prompt injection as behavior in which a model or agent follows malicious instructions inserted by an adversary, either in an input prompt or in third-party or tool-retrieved content. Definitions largely agree on the outcome: the system is redirected from the user’s or intended goal, with papers describing it as executing an attacker-specified task, taking unauthorized actions, or deviating from intended behavior.

**Variants.** Several papers distinguish direct and indirect forms. Direct prompt injection is described as malicious instructions placed in inputs sent to the model, while indirect prompt injection, sometimes called an indirect prompt attack, refers to instructions embedded in emails, documents, retrieved text, tool outputs, or other external sources the agent accesses; some papers also note harms such as data exfiltration, influencing outputs for other users, or redirecting the agent to unauthorized actions.

**Space of elicitation and scores.** Only 1 linked measurement instrument is reported: AgentDojo. Papers describe AgentDojo as a dynamic environment for testing prompt injection attacks, so the linked operationalization is a testing environment for the attack behavior.

**What it is taken as evidence of.** No linked constructs are reported for prompt injection. In these papers, it is described as an attack behavior, but no recorded relationship explicitly treats it as evidence of a broader construct.

## Sources

**Prompt injection** (2 papers: [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf), [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf))
> Introducing malicious instructions into tool outputs or other context so that the agent follows the attacker’s goal instead of the user’s.

**Indirect prompt injection** (2 papers: [Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?](https://proceedings.iclr.cc/paper_files/paper/2025/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf), [MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25z/zhu25z.pdf))
> Following malicious or unintended instructions embedded in external content such as emails, documents, or retrieved text.

**Indirect prompt attack** (1 paper: [Gandalf the Red: Adaptive Security for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pfister25a/pfister25a.pdf))
> An observable attack where a malicious actor manipulates external data sources that an LLM accesses, causing the model to deviate from its intended behavior.

## Relationships

### Prompt injection →
- **AgentDojo** (measurement instrument): *measured_by*, 1 paper
  > AgentDojo (Debenedetti et al., 2024) offers a dynamic environment for testing prompt injection attacks, and AgentHarm (Andriushchenko et al., 2024) measures the potential harm from agents executing malicious tasks.
  - [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf)
