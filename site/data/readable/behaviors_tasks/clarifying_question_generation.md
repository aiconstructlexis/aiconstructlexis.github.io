# Clarifying question generation
**Type:** Behavioral indicator  
**Supporting papers:** 12  
**Also known as:** Asking clarifying questions, Clarification question asking, Clarification seeking, Clarification question generation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this behavior as producing a clarifying or follow-up question when a user's request, instruction, or query is ambiguous or underspecified, so the model elicits more information rather than directly answering or proceeding. Several papers describe it as asking to resolve ambiguity, while others narrow it to eliciting missing task specifications that distinguish among multiple compatible solutions, or to identifying multiple possible interpretations in a database schema context. A smaller line of work also counts asking about missing, ambiguous, or incorrect information before tool use, including seeking user confirmation before deleting potentially critical files, and some work frames success as generating "the most informative question."

**Variants.** Papers use several near-synonymous labels, including asking clarifying questions, clarification question asking, clarifying question generation, and clarification seeking. The behavior appears in general user requests, tool or API use when required details or arguments are missing or appear incorrect, database-schema settings where the assistant seeks clarification about multiple interpretations, and agent settings that request confirmation before sensitive actions. Some formulations center on disambiguating among compatible solutions, while others center on proactively requesting extra information before continuing.

**Space of elicitation and scores.** Only one measurement instrument is linked to it: APPS. Papers use APPS as a benchmark to evaluate question-generating strategies on competition-level coding challenges, and no other measurement instrument is linked to this behavior.

**What it is taken as evidence of.** Three constructs are linked to it, with mixed relationship types rather than a single recurring framing. Papers relate clarifying question generation to Ambiguity handling and to Disambiguation ability, while a separate paper claims a causal relationship from Metacognition to Clarifying question generation, stating that generating effective clarifying questions requires "a form of meta-cognitive reasoning."

## Sources

**Asking clarifying questions** (1 paper: [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf))
> The act of generating a question in response to a user's query to resolve ambiguity and elicit more information.

**Clarification question asking** (1 paper: [Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ffd05ca3cf3985f4572af015b4cfc1e-Paper-Conference.pdf))
> Producing a clarifying question instead of directly answering when the user request is ambiguous or underspecified.

**Clarifying question generation** (1 paper: [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf))
> Producing questions intended to elicit missing task specifications that distinguish among multiple compatible solutions.

**Clarification seeking** (2 papers: [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf), [Are Large Language Models Ready for Multi-Turn Tabular Data Analysis?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aj/li25aj.pdf))
> The observable behavior of an LM agent requesting additional information from the user when instructions are ambiguous or underspecified.

**Clarification question generation** (1 paper: [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf))
> Producing a follow-up question that identifies and disambiguates multiple possible interpretations of a user query in the context of a database schema.

## Relationships

### Clarifying question generation →
- **APPS** (measurement instrument): *measured_by*, 1 paper
  > We evaluate all question-generating strategies on... the more challenging APPS (Hendrycks et al., 2021) benchmark with competition-level coding challenges
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)

### → Clarifying question generation
- **Metacognition** (construct): *causes*, 1 paper
  > Yet, generating effective clarifying questions requires LLM agents to engage in a form of meta-cognitive reasoning, an ability LLMs may presently lack.
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)

### Associated with
- **Ambiguity handling** (construct), 1 paper
  > In this work, we develop LLMs that can ask clarifying questions to resolve ambiguity in their users’ requests. (Section 1)
  - [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf)
- **Disambiguation ability** (construct), 1 paper
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
