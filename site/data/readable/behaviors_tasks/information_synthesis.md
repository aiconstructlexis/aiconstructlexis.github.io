# Information synthesis
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Information integration, Information aggregation, Aggregation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as combining information that is scattered across a long document, a full context, or multiple sources into a single answer or other unified output. Most definitions describe collecting and synthesizing information from various parts of long or multiple documents, or integrating information from sources such as web pages and knowledge graphs, to produce a coherent answer, ordering, or unified output. A smaller line of work frames it as aggregating patient information from conversation history so that understanding of the patient condition can be updated.

**Variants.** Papers use several near-names for the same general behavior, most often information aggregation or aggregation, alongside information synthesis and information integration. The variants studied are usually long-context ones, including sorting or ordering, word extraction, and tasks involving frequency analysis or summarization over distributed spans. Another recurring setting is answering complex questions by querying structured data sources and synthesizing information from different sources, while one specialized variant focuses on clinical dialogue, where question-answer pairs are appended to a conversation log and the gathered patient information is aggregated over time.

**Space of elicitation and scores.** Papers link this behavior to three measurement instruments: 2WikiMultiHopQA, RULER, and ZeroSCROLLS. In the recorded descriptions, 2WikiMultiHopQA assesses cross-document reasoning and information integration using Wikipedia data, RULER includes Aggregation as one of its task domains, and ZeroSCROLLS is used through an Information Aggregation task, BookSumSort.

## Sources

**Information integration** (1 paper: [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf))
> Aggregating gathered patient information from conversation history to update understanding of the patient condition.

**Information aggregation** (2 papers: [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf), [MagicPIG: LSH Sampling for Efficient LLM Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d50d824ae819d5a961c1d8edc15e833-Paper-Conference.pdf))
> The task of collecting and synthesizing information from various parts of a long document or multiple documents to perform a task like sorting or ordering.

**Information synthesis** (1 paper: [CRAG - Comprehensive RAG Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1435d2d0fca85a84d83ddcb754f58c29-Paper-Datasets_and_Benchmarks_Track.pdf))
> The process of integrating and combining information from multiple different sources, such as web pages and knowledge graphs, to generate a coherent answer.

**Aggregation** (2 papers: [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf), [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf))
> Combining information scattered throughout a document into a unified output.

## Relationships

### Information synthesis →
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > “RULER (Hsieh et al., 2024): a synthetic benchmark with 13 tasks categorized into 4 domains: Needle-in-a-Haystack (Retrieval), Multi-Hop Tracing, Aggregation, and Question Answering.”
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **ZeroSCROLLS** (measurement instrument): *measured_by*, 1 paper
  > "we choose seven tasks from ZeroSCROLLS [34], spanning all four task categories: ④ Information Aggregation (BookSumSort)"
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > ...and two multi-hop QA datasets: Adversarial HotpotQA (Yang et al., 2018), and 2WikiMultihopQA (Ho et al., 2020), which assess cross-document reasoning and information integration using Wikipedia data. (Section 4.1)
  - [Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://aclanthology.org/2025.emnlp-main.549.pdf)
