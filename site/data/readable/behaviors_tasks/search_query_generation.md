# Search query generation
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Query generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as producing search queries so a retriever, search engine, or other knowledge source can fetch external information, most often in retrieval-augmented setups. Papers usually condition the query on a question together with context, partial context, or the current reasoning state, and they commonly frame success as generating effective or relevant queries rather than imprecise or under-specified ones. A smaller line of work broadens it to formal or natural-language queries over structured and unstructured sources, and one paper frames query generation in reverse, as generating a question or query from a given response.

**Variants.** Papers use both the names query generation and search query generation. Common variants include generating a single query, multiple queries, or k queries, sometimes at each retrieval hop; inputs range from note content, forecasting questions and their background, to question answering context in domains such as sports. Another variant targets heterogeneous sources by producing SPARQL, SQL, or natural-sentence queries.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, SAFE. The recorded link is related rather than measured_by: one paper describes SAFE as using an LLM in a process that includes sending search queries to Google Search.

## Sources

**Query generation** (3 papers: [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf), [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf))
> The observable production of search queries by a model, particularly in the context of retrieval-augmented generation, where queries are used to fetch external knowledge.

**Search query generation** (5 papers: [DecoupleSearch: Decouple Planning and Search via Hierarchical Reward Modeling](https://aclanthology.org/2025.emnlp-main.222.pdf), [Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf), [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf), [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf))
> Producing search queries from the current reasoning state to retrieve external documents.

## Relationships

### Associated with
- **SAFE** (measurement instrument), 1 paper
  > SAFE utilizes an LLM to... comprising sending search queries to Google Search...
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
