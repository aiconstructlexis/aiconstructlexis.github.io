# Entity disambiguation
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Named entity disambiguation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats entity disambiguation as selecting or identifying the correct entity when multiple entities share the same or similar name, surface form, or attributes. Most formulations make success the correct resolution of the referent from candidates or from a claim, often using contextual clues or clarifying information; one paper describes an agent that identifies ambiguities, gathers additional context, and summarizes the differences. Smaller lines of work cast it more narrowly as resolving ambiguous customer transaction references to the right order or product, or as an iterative claim-graph process where the system generates targeted questions and refines them through knowledge-base interaction.

**Variants.** Papers study this behavior in several settings. Common variants are knowledge-base entity selection in KBQA and claim-centered disambiguation when a claim mentions entities with similar names or attributes; another line studies Wikipedia inconsistency detection, where the agent distinguishes similarly named entities from retrieved evidence and clarifying context. A narrower application appears as named entity disambiguation in CRM queries, such as identifying a specific order within a stated time frame, and another frames it inside an interactive graph for deeper sub-claim verification; one related description presents entity identification as a question-answering module that extracts a specific entity.

**Space of elicitation and scores.** One measurement instrument is linked to this behavior, FEVEROUS. In the linked use, papers evaluate FEVEROUS claims on an Entity Disambiguation partition, alongside Multi-hop Reasoning and Numerical Reasoning partitions. No other measurement instrument is linked.

**What it is taken as evidence of.** Only one construct is linked to this behavior, Chain-of-thought reasoning. Papers describe that link as related rather than as a measurement or causal claim, noting that the challenge is amplified in multi-step reasoning, where entity disambiguation must span the entire verification process. Beyond that, papers do not link it to additional constructs.

## Sources

**Entity disambiguation** (4 papers: [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf), [Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models](https://aclanthology.org/2025.emnlp-main.1765.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf))
> The task of selecting the correct knowledge base entity from a set of candidates that share the same name or surface form.

**Named entity disambiguation** (1 paper: [CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.194.pdf))
> Resolving ambiguous customer-transaction references to the correct order or product mentioned in a query.

## Relationships

### Entity disambiguation →
- **FEVEROUS** (measurement instrument): *measured_by*, 1 paper
  > For consistency with prior work (Aly et al., 2021), we evaluate FEVEROUS claims on three key partitions: Multi-hop Reasoning, Entity Disambiguation, and Numerical Reasoning. (Section 4.1)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)

### Associated with
- **Chain-of-thought reasoning** (construct), 1 paper
  > This challenge is amplified in multi-step reasoning, where entity disambiguation must span the entire verification process. (Section 1)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > Entity Identification. This function acts as a question-answering module that extracts a specific entity. (Section 3.2)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
