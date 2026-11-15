# NFCorpus
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** NFCORPUS, NF-Corpus  

## State of the Field

**What it is.** Across the surveyed papers, the prevailing usage treats NFCorpus, also written NFCORPUS or NF-Corpus, as an information retrieval dataset or benchmark, often described more specifically as medical information retrieval. Definitions add that it contains queries in simple English and technical documents extracted from PubMed, and one paper states that its test split has 323 queries and the corpus has 3.6k documents. Some papers describe it more generally as a retrieval dataset from BEIR used for query generation and retrieval or for generating and evaluating adversarial passages, while another frames it as a medical dataset for domain-specific factual questions involving single entities.

**What it is claimed to measure.** Papers link NFCorpus to two behavioral indicators, Factual question answering and Information retrieval, and to no constructs. One paper uses it to measure information retrieval in long-document retrieval scenarios, reporting recall and precision on NFCORPUS, while the same paper also says that SQUAD, NFCORPUS, and SCI-DOCS contain factual questions involving single entities. In the linked relationships, the measurement claims stay at the level of behavioral indicators rather than constructs.

**Space of uses.** Most commonly, papers use NFCorpus as one dataset within broader evaluation suites rather than in isolation. It appears alongside Natural Questions in corpus-poisoning experiments, alongside Dragonball, SQUAD, and SCI-DOCS in filtered long-document RAG experiments, and as one of the public datasets in BEIR; the only linked measurement instrument is BEIR, to which one paper relates NFCorpus explicitly. One paper also highlights it as the dataset with the highest unseen query term ratio when evaluating query generation and retrieval.

**Concerns raised.** One paper notes a limitation specific to its own filtering setup: because NFCORPUS is a medical-information dataset, its LLM filtering mechanism may have limitations in processing the semantic information of professional academic terms.

## Sources

**NFCorpus** (2 papers: [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.334.pdf), [Tricking Retrievers with Influential Tokens: An Efficient Black-Box Corpus Poisoning Attack](https://aclanthology.org/2025.naacl-long.210.pdf))
> A retrieval dataset used to generate and evaluate adversarial passages in the corpus-poisoning experiments.

**NFCORPUS** (1 paper: [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> Medical information retrieval dataset used to evaluate performance on domain-specific factual questions involving single entities.

**NF-Corpus** (1 paper: [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf))
> A medical information retrieval benchmark dataset containing queries in simple English and technical documents extracted from PubMed.

## Relationships

### → NFCorpus
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Experimental results across four datasets—Dragonball, SQUAD, NFCORPUS, and SCI-DOCS demonstrate that SAKI-RAG achieves better recall and precision compared to other RAG frameworks in long-document retrieval scenarios (Abstract).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Factual question answering** (behavioral indicator): *measured_by*, 1 paper
  > the SQUAD, NFCORPUS, and SCI-DOCS datasets consist of factual questions involving single entities (Section 4.1).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)

### Associated with
- **BEIR** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including TREC-COVID (Voorhees et al., 2021), NFCorpus (Boteva et al., 2016)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
