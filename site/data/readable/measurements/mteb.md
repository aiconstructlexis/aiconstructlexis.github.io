# MTEB
**Type:** Measurement instrument  
**Supporting papers:** 32  

## State of the Field

**What it is.** Across papers, MTEB is most commonly described as a comprehensive, standard, or general-purpose suite for evaluating text embedding models. A recurring specification presents it as 56 English tasks across 7 types: classification, clustering, pair classification, reranking, retrieval, semantic textual similarity, and summarization. Some papers describe narrower or different slices, including ten STS tasks for sentence embeddings, or a holistic assessment of sentence representations across 8 task types. Some authors also refer to an MTEB leaderboard and collection of benchmarks when citing top or leading embedding models.

**What it is claimed to measure.** Papers use MTEB to measure 6 behavioral indicators and 3 constructs. The prevailing measurement claims concern information retrieval, semantic textual similarity, text clustering, text embedding, and pair classification, with 1 other behavioral indicator and 3 constructs also reported. Across those links, the reported uses are spread across multiple embedding-related behaviors rather than centered on a single target.

**Space of uses.** In use, papers often treat MTEB as the main embedding benchmark, either evaluating on the full 56 main datasets or on subsets such as retrieval datasets and ten STS tasks. It is linked to 1 other instrument, BEIR, and papers often discuss the two together as standard retrieval benchmark suites or relate BEIR retrieval tasks to MTEB. Some papers also use the MTEB leaderboard to cite top or leading models, and one paper uses general-purpose MTEB as a baseline against a domain-specific benchmark.

**Concerns raised.** A smaller line of work notes limits in the benchmark's use. One paper says that standard suites such as MTEB do not contain instructions, and another reports that higher MTEB performance does not guarantee better downstream performance.

## Sources

**MTEB** (9 papers: [Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf), [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.597.pdf), [Little Giants: Synthesizing High-Quality Embedding Data at Scale](https://aclanthology.org/2025.naacl-long.64.pdf), [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://aclanthology.org/2025.naacl-long.457.pdf), [Less Mature is More Adaptable for Sentence-level Language Modeling](https://aclanthology.org/2025.acl-long.573.pdf), [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf), [FinMTEB: Finance Massive Text Embedding Benchmark](https://aclanthology.org/2025.emnlp-main.179.pdf), [HLM-Cite: Hybrid Language Model Workflow for Text-based Scientific Citation Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/5635925cf9d2274f338eb0dd5971e845-Paper-Conference.pdf), [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf))
> The Massive Text Embedding Benchmark (MTEB) is a comprehensive evaluation suite used to assess the performance of text embedding models.

## Relationships

### → MTEB
- **Information retrieval** (behavioral indicator): *measured_by*, 4 papers
  > We evaluate 13 representative retrieval models, ranging from traditional bag-of-words models to large dense retrieval models, including the top performers from the retrieval set of the MTEB leaderboard (Muennighoff et al., 2023), BEIR (Thakur et al., 2021). (Section 4.1)
  - [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf)
  - [Repetition Improves Language Model Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9b0c9480b03f9a6bca24ed8c08ee058-Paper-Conference.pdf)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
  - [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf)
- **Text clustering** (behavioral indicator): *measured_by*, 3 papers
  > MTEB is a collection of 56 datasets that are grouped into different embedding tasks: classification, clustering, pair classification, reranking, retrieval, sentence similarity (STS), and summarization, with the goal of evaluating embeddings broadly. (Section 4.1)
  - [Repetition Improves Language Model Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9b0c9480b03f9a6bca24ed8c08ee058-Paper-Conference.pdf)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
  - [Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.213.pdf)
- **Semantic textual similarity** (behavioral indicator): *measured_by*, 3 papers
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
  - [Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.213.pdf)
- **Text embedding** (behavioral indicator): *measured_by*, 2 papers
  > Through systematic evaluation on 32 embedding tasks from the Massive Text Embedding Benchmark (MTEB) (Muennighoff et al., 2022), we find that intermediate layers often surpass the final layer by up to 16% in downstream accuracy.
  - [Layer by Layer: Uncovering Hidden Representations in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/skean25a/skean25a.pdf)
  - [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf)
- **Representation quality** (construct): *measured_by*, 1 paper
  > For embedding performance we evaluate using the 56 main datasets from MTEB (Muennighoff et al., 2023c). (Section 3.1)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Ranking** (behavioral indicator): *measured_by*, 1 paper
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Information retrieval ability** (construct): *measured_by*, 1 paper
  > our model, MM-Embed, ... surpassing the state-of-the-art text retrieval model, NV-Embed-v1, on the MTEB retrieval benchmark. (Section 1)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **Pair classification** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate MOEE on 6 task categories from the MTEB, including Classification, Clustering, Pair Classification, Re-ranking, Semantic Textual Similarity (STS), and Summarization. (Section 4.1)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To validate the effectiveness and generalization ability of our proposed method, we followed the data selection strategy of e5-mistral-7b-instruct (Wang et al., 2023) and used only a small portion of the MTEB training dataset for zero-shot training. (Section 4.3)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)

### Associated with
- **BEIR** (measurement instrument), 1 paper
  > “Note that our model also attains the highest scores in 15 retrieval tasks (commonly referred to as BEIR (Thakur et al., 2021)), 11 clustering tasks, and 12 classification tasks in the MTEB benchmark.”
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
