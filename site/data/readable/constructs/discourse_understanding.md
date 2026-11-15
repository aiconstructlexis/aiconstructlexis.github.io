# Discourse understanding
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Discourse comprehension, Dialogue structure understanding  

## State of the Field

**Space of definitions.** A recurring framing treats discourse understanding as understanding the relations and organization that make text coherent: papers describe it as understanding how a text is organized and how its parts contribute to overall meaning and coherence, or as a latent model ability to infer and generate coherent continuations from discourse relations, with one paper noting that such relations involve "longer spans and complex reasoning." Other papers use differently scoped versions of the construct: one defines it as interpreting and reasoning over lengthy, complex narratives to answer questions that require a cohesive understanding of the whole text, while another uses a related label for comprehending and using reply dependency structure in multi-turn dialogue for semantic interpretation and information extraction. Across these definitions, the main differences are whether the construct is framed as a latent model ability or as a task, and whether it targets text organization, discourse relations across argument spans, whole-narrative reasoning, or dialogue reply structure.

**Space of facets.** Papers do not present a single shared breakdown of the construct, but they do use nearby labels for task-specific variants, including discourse comprehension and dialogue structure understanding. The construct is tied in different papers to argumentative flow and logic flow through discourse structure analysis, to discourse relations signaled by connectives across argument spans, to understanding longer and more complex discourse such as long stories, and to reply relationships in conversations. These usages are distinguished by the setting and the named structure to be understood.

**Space of measurement.** No measurement instrument is linked to this construct, and no behavioral indicator is linked to it. The papers instead describe it through task formulations and capabilities, such as interpreting lengthy, complex narratives, generating coherent continuations from discourse relations, and understanding dialogue reply relationships, but they do not connect the construct to a benchmark, human evaluation, LLM-as-a-judge setup, probe, or analysis.

## Sources

**Discourse comprehension** (1 paper: [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf))
> The ability to understand how a text is organized and how its parts contribute to overall meaning and coherence.

**Discourse understanding** (2 papers: [Discursive Circuits: How Do Language Models Understand Discourse Relations?](https://aclanthology.org/2025.emnlp-main.1657.pdf), [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf))
> The latent ability of a language model to infer and generate coherent continuations based on discourse relations signaled by connectives, integrating context and relational semantics across argument spans.

**Dialogue structure understanding** (1 paper: [Task-aware Contrastive Mixture of Experts for Quadruple Extraction in Conversations with Code-like Replies and Non-opinion Detection](https://aclanthology.org/2025.emnlp-main.207.pdf))
> The latent ability to comprehend and utilize the reply dependency structure in multi-turn dialogues for improved semantic interpretation and information extraction.
