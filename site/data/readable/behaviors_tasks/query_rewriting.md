# Query rewriting
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Query rephrasing, Prompt rewriting, Prompt polishing, Query reformulation, Query paraphrasing, Query refinement  

## State of the Field

**Space of definitions.** Across papers, the most common framing is rewriting an input query so it better fits a downstream step: authors describe clarifying ambiguous expressions, supplementing semantic information, reformulating for a later retrieval round, or rewriting according to an explicit constraint such as a required aspect and value. Some definitions narrow this to ambiguity-resolving paraphrases that preserve intent, including what one paper calls "abbreviation replacement and ambiguity elimination of the original query," while others emphasize enrichment, for example adding visual details, stylistic elements, or aesthetic expectations. A smaller line of work applies the same behavior to prompts rather than search queries, describing structured keyword prompts, polished prompts that remove stylistic bias and conflicting information, or rephrased prompts that preserve meaning, sometimes while maintaining or improving faithfulness to the original prompt and sometimes to make malicious intent less detectable.

**Variants.** Papers use several nearby names for this behavior, most often query rewriting, query reformulation, prompt rewriting, query paraphrasing, and prompt polishing, with query rephrasing and query refinement as additional labels. The settings vary: online shopping rewrites a query to match an aspect and value, text-to-SQL rewrites it to align semantically with schemas, multi-hop QA and multimodal search reformulate follow-up queries for another retrieval round, conversational work clarifies context-dependent questions into standalone ones, and text-to-image work rewrites or polishes prompts. In these settings, several papers claim a causal relationship from Query rewriting to Information retrieval, one paper claims a causal relationship from Query rewriting to Image generation, and one paper reports it is related to Thought generation.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, TopiOCQA, and they describe that link as related rather than stating that the behavior is measured by it. In that use, TopiOCQA is a resource consisting of multi-turn conversational queries with context-dependent questions, where the rewriting behavior appears as clarifying the original question into a standalone question.

**What it is taken as evidence of.** Papers connect Query rewriting to three constructs, but not in one uniform way. It is reported as related to Disambiguation ability and to Reasoning, and one paper claims a causal relationship from In-context learning to Query rewriting. Rather than centering on a single agreed construct link, the papers distribute it across these different relations.

## Sources

**Query rephrasing** (1 paper: [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf))
> The task of rewriting a user's search query, typically using an LLM, to enrich it with additional visual details, stylistic elements, and aesthetic expectations.

**Query rewriting** (3 papers: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf), [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf), [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf))
> The task of modifying a given user query based on a specified constraint, such as an aspect and value.

**Prompt rewriting** (3 papers: [AP-Adapter: Improving Generalization of Automatic Prompts on Unseen Text-to-Image Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf), [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf))
> The task of transforming a natural language description into a more effective, structured prompt (e.g., a keyword-based prompt) for a generative model.

**Prompt polishing** (1 paper: [Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf))
> The task of rewriting user-written text prompts to remove stylistic biases, platform-specific keywords, and conflicting information.

**Query reformulation** (2 papers: [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf))
> The task of modifying or rewriting a query for a subsequent retrieval step, typically by incorporating information from previously retrieved documents to focus on unresolved aspects of the original question.

**Query paraphrasing** (1 paper: [UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.693.pdf))
> Rewriting a user query using synonymous expressions or clearer formulations to resolve ambiguity while preserving intent, such as rephrasing 'Who was the spouse of Anna Karina from 1968 to 1974?' as 'Anna Karina spouse from 1968 to 1974'.

**Query refinement** (1 paper: [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf))
> The observable action of modifying or improving a search query or internal prompt when the initial results are unsatisfactory.

## Relationships

### Query rewriting →
- **Information retrieval** (behavioral indicator): *causes*, 3 papers
  > We find that using this rephrased query in retrieval drastically boosts the aesthetic quality more than we ever expected.
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Image generation** (behavioral indicator): *causes*, 1 paper
  > The goal of the LLM is to “rewrite” the prompt passed into the T2I model, such that the final generated image improves in quality, while maintaining or improving the faithfulness to the original text prompt. (Section 4.4)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)

### → Query rewriting
- **In-context learning** (construct): *causes*, 1 paper
  > we leverage the ICL capability of large language models (LLMs) [23, 30] to generate automatic keyword prompts similar to manually crafted prompts (Section 1).
  - [AP-Adapter: Improving Generalization of Automatic Prompts on Unseen Text-to-Image Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### Associated with
- **Disambiguation ability** (construct), 1 paper
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Reasoning** (construct), 1 paper
  > We find that utilizing the reasoning ability of large language models (LLMs) to rephrase the search query and extend the aesthetic expectations can make up for this shortcoming. (Abstract)
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
- **Thought generation** (behavioral indicator), 1 paper
  > Thought-concat appends the current thought t(i) to the query, constructing the updated query as q(i+1) = [t(i); q(i)], where [a; b] denotes the concatenation of a and b. (Section 4.2.4)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **TopiOCQA** (measurement instrument), 1 paper
  > We employ TopiOCQA (Adlakha et al., 2022) and QReCC (Anantha et al., 2021), both of which consist of multi-turn conversational queries. These datasets contain context-dependent questions...requiring disambiguation based on prior conversation turns. Hence, in the sub-task, LLM clarifies the original question into a standalone question. (Section 3)
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf)
