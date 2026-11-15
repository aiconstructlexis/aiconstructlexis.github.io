# Semantic parsing
**Type:** Behavioral indicator  
**Supporting papers:** 20  
**Also known as:** Query parsing, Prompt parsing, Intent and slot filling, Task-oriented dialogue parsing, Task-oriented semantic parsing, Logical form generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats it as translating natural language into a structured, machine-executable form. Most definitions use questions, utterances, instructions, observations, or user requests as inputs, and logical forms, programs, queries, database commands, API calls, or standardized JSON as outputs. Papers agree on the unstructured-to-structured mapping, while differing on the target format, including canonical logical representations, intent and slot structures, and structured fields such as instruction, question, URL, data, and categories.

**Variants.** Variants span task-oriented, dialogue, and knowledge-oriented settings. Papers name intent and slot filling, task-oriented dialogue parsing, and task-oriented semantic parsing, where the output updates dialogue state or yields machine-readable forms such as API calls; other recurring variants are logical form generation for SPARQL, SQL, S-expressions, first-order logic, Lisp, abstract syntax trees, and executable graph queries. A smaller line of work studies query or prompt parsing into JSON with predefined keys or distinct components for downstream agents, and one paper uses semantic parsing to extract ground rules from observations or instructions in embodied tasks.

**Space of elicitation and scores.** Papers explicitly link one measurement instrument, MTOP, and describe it as a semantic parsing benchmark. No other measurement instrument is linked.

**What it is taken as evidence of.** The only linked construct is Knowledge base awareness, and one paper claims a causal relationship from Knowledge base awareness to semantic parsing, stating that awareness of the environment makes an agent more effective in generating optimal logical forms. No other construct is linked. The only linked behavioral indicator is Code generation: one paper claims a causal relationship from semantic parsing to code generation, while another treats the two as related by describing semantic interpretation as translation into executable code.

## Sources

**Query parsing** (1 paper: [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf))
> The action of converting an unstructured natural language user query into a structured format with distinct components.

**Semantic parsing** (5 papers: [NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf), [STARE at the Structure: Steering ICL Exemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.746.pdf), [Behavioural vs. Representational Systematicity in End-to-End Models: An Opinionated Survey](https://aclanthology.org/2025.acl-long.1537.pdf), [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf), [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf))
> The task of translating natural language inputs, such as observations or instructions, into a structured, programmatic, or logical form.

**Prompt parsing** (1 paper: [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf))
> Converting unstructured user task descriptions into structured JSON format with standardized keys to extract requirements for downstream agents.

**Intent and slot filling** (1 paper: [STARE at the Structure: Steering ICL Exemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.746.pdf))
> A semantic parsing task common in dialogue systems where the goal is to identify the user's overall goal (intent) and extract specific pieces of information (slots).

**Task-oriented dialogue parsing** (1 paper: [STARE at the Structure: Steering ICL Exemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.746.pdf))
> A semantic parsing task focused on interpreting user utterances within a goal-oriented conversation to update a dialogue state or execute an action.

**Task-oriented semantic parsing** (1 paper: [Grammar Pruning: Enabling Low-Latency Zero-Shot Task-Oriented Language Models for Edge AI](https://aclanthology.org/2025.emnlp-main.858.pdf))
> Converting natural-language user requests into structured machine-readable representations such as API calls.

**Logical form generation** (3 papers: [CompKBQA: Component-wise Task Decomposition for Knowledge Base Question Answering](https://aclanthology.org/2025.emnlp-main.16.pdf), [Zero and Few-shot Semantic Parsing with Ambiguous Inputs](https://proceedings.iclr.cc/paper_files/paper/2024/file/eae78bf2712f222f101bd7d12f875a57-Paper-Conference.pdf), [KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25d/luo25d.pdf))
> The task of converting a natural language question into a structured, executable query such as SPARQL or S-Expression.

## Relationships

### Semantic parsing →
- **MTOP** (measurement instrument): *measured_by*, 2 papers
  > MTOP [22] Semantic Parsing (Table 1)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf)
- **Code generation** (behavioral indicator): *causes*, 2 papers
  > we integrate structure-based prompt parsing and multi-stage verification to ensure the quality of resulting solutions and instructions prior to actual code implementation, thereby improving overall performance.
  - [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf)
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf)

### → Semantic parsing
- **Knowledge base awareness** (construct): *causes*, 1 paper
  > The agent’s awareness of the environment makes it more effective in generating optimal logical forms compared to end-to-end methods. (Proposition 4.1)
  - [KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25d/luo25d.pdf)
