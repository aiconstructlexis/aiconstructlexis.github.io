# Contextual reasoning
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Context-specific reasoning, Context-aware reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats contextual reasoning as an ability to use surrounding context, rather than literal keyword matching or other surface cues, to infer what is relevant. Most definitions describe it broadly as understanding instruction, semantic, situational, or code context and then inferring objects, judgments, or vulnerabilities, and one paper says deontic judgments are "logical and context-sensitive" and require reasoning about social norms, conditional obligations, and moral exceptions. A smaller line of work uses nearby labels for narrower settings, including inferring user interests and multi-subject relations within a query context, or reasoning over sequences by selectively focusing on relevant context. Definitions differ mainly in what counts as context and in whether the construct is presented as a latent ability, a task requirement, or an architecture-associated capability.

**Space of facets.** Instead of a single taxonomy, papers use several nearby framings for related capabilities. One cluster centers on contextual understanding for instruction following, deontic or compliance judgments, and vulnerability analysis, where the relevant context includes situational or functional relations, social norms, roles and transmission principles, or surrounding code and path-sensitive information. Another paper speaks of "contextual reasoning primitives" built from provided context, variable bindings, or sequence structure, and nearby labels narrow the scope further to query-bound inference over user interests and multi-subject relations, or selective focus on relevant sequence context.

**Space of measurement.** Papers link contextual reasoning to three measurement instruments and no behavioral indicators. The linked operationalizations are all benchmark-style datasets: LongBench, using Single-Doc QA and Multi-Doc QA to assess contextual reasoning; MemeReaCon, described as specifically constructed to evaluate the fine-grained contextual reasoning needed to understand memes in online posts; and PubMedQA, where long-context QA samples and perplexity on long answers are used to assess it. Taken together, these measures operationalize the construct through question answering over single, multiple, or long documents, and through contextual meme understanding, which matches the common emphasis on inferring from surrounding context.

## Sources

**Contextual reasoning** (4 papers: [Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction](https://proceedings.iclr.cc/paper_files/paper/2024/file/accb5f309ec092a6787a1879ad5f2a5f-Paper-Conference.pdf), [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/582d4e27fa24168f3af1f4582655034b-Paper-Conference.pdf), [Deontological Keyword Bias: The Impact of Modal Expressions on Normative Judgments of Language Models](https://aclanthology.org/2025.acl-long.360.pdf), [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf))
> The ability to understand the context within an instruction and infer relevant objects based on situational or functional relationships, rather than literal keyword matching.

**Context-specific reasoning** (1 paper: [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent ability to infer user interests, understand specialized field descriptions, and deduce relationships involving multiple subjects within a specific query context.

**Context-aware reasoning** (1 paper: [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf))
> The ability to reason about sequences by selectively focusing on relevant context, a key feature of the Mamba architecture.

## Relationships

### Contextual reasoning →
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > For LongBench, we use datasets from the Single-Doc QA and Multi-Doc QA categories to assess contextual reasoning.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
- **PubMedQA** (measurement instrument): *measured_by*, 1 paper
  > we select the PubMedQA dataset and derive long-context QA samples to evaluate the effectiveness of HMT. Two metrics are employed: for long answers, we compute the PPL to assess the contextual reasoning of HMT (Section 5.1)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **MemeReaCon** (measurement instrument): *measured_by*, 1 paper
  > MemeReaCon occupies a unique position by being the first benchmark, to our knowledge, specifically constructed to evaluate the fine-grained contextual reasoning required to understand memes as they are used in online posts. (Section 2)
  - [MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.176.pdf)
