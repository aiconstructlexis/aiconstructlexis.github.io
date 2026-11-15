# Grammatical acceptability judgment
**Type:** Behavioral indicator  
**Supporting papers:** 30  
**Also known as:** Syntactic well-formedness detection, Grammaticality judgment, Grammatical judgment, Linguistic acceptability, Linguistic acceptability judgment, Acceptability judgment  

## State of the Field

**Space of definitions.** Most papers describe this behavior as judging whether a sentence is grammatically correct, acceptable, or well formed. Many operationalizations use a direct acceptable versus unacceptable decision, often as single-sentence classification, while others use minimal pairs and count the model as correct when it picks the more acceptable sentence or assigns higher probability, likelihood, or MLM score to the acceptable member of the pair. A minority of definitions broaden the target from grammaticality alone to grammatical or semantic acceptability, or to whether a sentence would be acceptable to a native speaker.

**Variants.** Papers use several near-synonymous labels for this behavior, including linguistic acceptability judgment, grammaticality judgment, grammatical judgment, linguistic acceptability, acceptability judgment, and syntactic well-formedness detection. The main variants are CoLA-style single-sentence judgments and BLiMP or TurBLiMP style minimal-pair comparisons, alongside benchmark-specific formulations such as Bigram Shift and discriminative grammar judgment experiments. The behavior is also studied in different language settings, including English, Turkish, and Kalamang.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, CoLA. It is consistently presented as a single-sentence classification task for determining whether a sentence is grammatically acceptable or unacceptable, and papers use it under labels such as grammatical acceptability and linguistic acceptability.

**What it is taken as evidence of.** Across the linked work, syntactic competence is the only construct mentioned. Papers describe grammatical acceptability judgment as related to syntactic competence, for example by treating such tasks as probing grammatical knowledge or as settings where models can exploit grammatical information, rather than stating a direct measurement claim. No other construct link is reported.

## Sources

**Syntactic well-formedness detection** (1 paper: [Emergence of a High-Dimensional Abstraction Phase in Language Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/57568e093cbe0a222de0334b36e83cf5-Paper-Conference.pdf))
> The observable task of determining whether a given sentence adheres to the grammatical rules of a language.

**Linguistic acceptability judgment** (6 papers: [TopoNets: High performing vision and language models with brain-like topography](https://proceedings.iclr.cc/paper_files/paper/2025/file/6191ab7080c840f67eaf5dff7d5edfcb-Paper-Conference.pdf), [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [DTZO: Distributed Trilevel Zeroth Order Learning with Provable Non-Asymptotic Convergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiao25a/jiao25a.pdf))
> The task of determining whether a sentence is grammatically or semantically well-formed, as evaluated by benchmarks like BLiMP.

**Grammaticality judgment** (4 papers: [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf), [TurBLiMP: A Turkish Benchmark of Linguistic Minimal Pairs](https://aclanthology.org/2025.emnlp-main.834.pdf), [Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases](https://aclanthology.org/2025.acl-long.478.pdf), [Developmentally-plausible Working Memory Shapes a Critical Period for Language Acquisition](https://aclanthology.org/2025.acl-long.462.pdf))
> The task of determining whether a given sentence is grammatically correct according to the rules of a language, often by choosing between a correct and a corrupted version.

**Grammatical acceptability judgment** (4 papers: [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kantamneni25a/kantamneni25a.pdf))
> The task of classifying a sentence as either grammatically acceptable or unacceptable.

**Grammatical judgment** (3 papers: [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Sudden Drops in the Loss: Syntax Acquisition, Phase Transitions, and Simplicity Bias in MLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e8df255a03b383f30abe09203770213-Paper-Conference.pdf))
> The task of determining whether a sentence is grammatically correct.

**Linguistic acceptability** (2 papers: [Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.321.pdf), [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf))
> The task of judging whether a sentence is grammatically correct or acceptable to a native speaker.

**Acceptability judgment** (1 paper: [How to Make the Most of LLMs' Grammatical Knowledge for Acceptability Judgments](https://aclanthology.org/2025.naacl-long.380.pdf))
> The observable behavior of selecting or scoring one sentence as more grammatically acceptable than another in a minimal pair.

## Relationships

### Grammatical acceptability judgment →
- **CoLA** (measurement instrument): *measured_by*, 4 papers
  > CoLA (Corpus of Linguistic Acceptability) (Warstadt et al., 2019) is a single-sentence classification task, where sentences are annotated as either grammatically acceptable or unacceptable (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)

### Associated with
- **Syntactic competence** (construct), 2 papers
  > However, LLMs can exploit grammatical information, given an appropriate task—e.g. grammaticality judgment or IGT prediction—and more useful grammatical data in the form of our typological prompt, which achieves leading results on these linguistic tasks. (Section 6)
  - [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)
  - [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf)
