# Semantic textual similarity
**Type:** Behavioral indicator  
**Supporting papers:** 20  
**Also known as:** Text similarity prediction, Text pair classification, Semantic similarity, Sentence similarity estimation, Sentence similarity, Semantic similarity judgment, Semantic text similarity, Sentence similarity assessment  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is a pairwise meaning-comparison task: authors usually describe it as estimating how similar or semantically equivalent two texts or sentences are, most often by producing a continuous score. The scoring form is commonly continuous, with examples ranging from 0 to 1 or 0 to 5, and one study asks a model to 'assess the similarity of the two sentences and provide a score from 0 to 1' (Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training). A smaller line of work uses categorical judgments instead, such as deciding whether pairs are paraphrases or semantically related, or whether meaning is preserved between a pre-dropout and post-dropout response.

**Variants.** Papers use nearby labels such as semantic textual similarity, semantic text similarity, sentence similarity, text similarity prediction, and pair classification. Some papers narrow the setting to financial texts, including headline-article and query-intent matching, while others place it in biomedical tasks or compare generated responses before and after neuron dropout. One paper also reports monolingual and cross-lingual sentence settings, alongside 'semantic text similarity and relatedness'.

**Space of elicitation and scores.** Papers link this behavior to 4 measurement instruments, with MTEB mentioned most often, followed by GLUE, STS12, and STS-B. These are described as benchmarks or datasets that include semantic similarity among other tasks, and some papers say STS evaluations directly measure whether embeddings capture fine-grained semantic similarity. Beyond benchmark-based evaluation, papers also elicit it through direct scoring prompts or model-based judgments, and one study prompts GPT-4o to decide whether a post-dropout response is still semantically similar to the original (Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs).

**What it is taken as evidence of.** Direct construct links are scarce. Among linked constructs, only Coherence appears, and it is linked as related rather than via a correlational or causal claim; the paper says that measuring semantic similarity through token-level embedding distances can overlook contextual information and reduce 'contextual semantic coherence', so the connection is framed as relatedness rather than as a shared construct claim.

## Sources

**Text similarity prediction** (1 paper: [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf))
> Predicting the semantic similarity score between two text sentences.

**Semantic similarity** (1 paper: [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf))
> The observable task of assessing the degree to which two pieces of text are similar in meaning.

**Text pair classification** (1 paper: [FinMTEB: Finance Massive Text Embedding Benchmark](https://aclanthology.org/2025.emnlp-main.179.pdf))
> The observable behavior of determining whether two financial texts are semantically related, such as assessing if a headline matches a news article or if a query matches user intent.

**Sentence similarity estimation** (1 paper: [Training LLMs to be Better Text Embedders through Bidirectional Reconstruction](https://aclanthology.org/2025.emnlp-main.216.pdf))
> The task of quantifying the degree of semantic similarity between two sentences, often on a continuous scale.

**Sentence similarity** (1 paper: [Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.321.pdf))
> Judging whether two sentences are semantically similar or paraphrases.

**Semantic similarity judgment** (1 paper: [Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs](https://aclanthology.org/2025.emnlp-main.595.pdf))
> The observable behavior of comparing two text responses to determine whether their meaning is preserved, used here to detect changes in model output after neuron dropout.

**Semantic textual similarity** (4 papers: [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf), [Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.213.pdf), [Modular Sentence Encoders: Separating Language Specialization from Cross-Lingual Alignment](https://aclanthology.org/2025.acl-long.108.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> The task of measuring the degree of semantic equivalence between two texts, typically on a continuous scale.

**Semantic text similarity** (1 paper: [MMTEB: Massive Multilingual Text Embedding Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0e3f908a2116ba529ad0a1530a3675-Paper-Conference.pdf))
> The task of determining how similar two pieces of text are in meaning, typically by assigning a continuous score.

**Sentence similarity assessment** (2 papers: [Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf))
> The observable task of determining the degree of semantic similarity between two sentences.

## Relationships

### Semantic textual similarity →
- **MTEB** (measurement instrument): *measured_by*, 3 papers
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
  - [Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.213.pdf)
- **STS12** (measurement instrument): *measured_by*, 2 papers
  > To validate this hypothesis and quantify their complementarity, we need to examine how these two embedding relate to one another. We approach this by conducting a Spearman correlation analysis using the STS12 dataset, which contains 6,216 sentence pairs. (Section 3.2)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > "the GLUE benchmark (Wang et al., 2019), which encompasses a diverse range of tasks, including question answering, sentiment analysis, and semantic textual similarity" (Section 6.2)
  - [A Memory Efficient Randomized Subspace Optimization Method for Training Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cj/chen25cj.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **STS-B** (measurement instrument): *measured_by*, 1 paper
  > Semantic Textual Similarity (STS): Directly measures the ability of embeddings to capture fine-grained semantic similarity. We use STSB, STS12 (both from MTEB (Muennighoff et al., 2023)) and SICK (from (Marelli et al., 2014)). (Section 4.1)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)

### Associated with
- **Coherence** (construct), 1 paper
  > Besides, these works typically measure semantic similarity via token-level embedding distances. Such approach overlooks contextual information, often leading to reduced contextual semantic coherence. (Section 1)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
