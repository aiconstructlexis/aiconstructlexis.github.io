# Factual question answering
**Type:** Behavioral indicator  
**Supporting papers:** 48  
**Also known as:** Factual query answering, Single-fact question answering, Truthful Answering, Truthful question answering, Simple QA, Fact-based question answering, Faithfulness enhancement, Fact-seeking question answering, Factoid question answering, Trivia question answering  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is answering direct questions with precise, factually correct information, often drawing on world knowledge or other objective, verifiable facts. Definitions commonly expect short or direct answers about items such as dates, locations, entities, attributes, or the correct object for a subject-relation prompt, and some benchmark-oriented formulations describe success as providing factually accurate answers on evaluation sets. A smaller line of work narrows the behavior to direct queries based on provided facts, to questions answerable with a single supporting fact, or to answers that are factual while avoiding misconceptions, hallucinated content, or other incorrect material.

**Variants.** Papers use several nearby labels for this behavior, including factoid question answering, factual query answering, fact-based question answering, simple QA, and truthful question answering, with several other narrower labels appearing as well. The studied settings range from open-domain factual prompts to queries derived from subject-relation-object triplets and updated knowledge, questions learned from documents that include short-form and yes/no answers, and extraction of specific facts from a given text or long context. Some papers further specialize the task to one-supporting-fact cases, geography and notable-individual questions in Chinese, Italian, and Arabic, Polish-context factual queries, or text-based factual question answering with visual assistance or misleading images.

**Space of elicitation and scores.** Papers measure this behavior with 7 instruments, most often benchmark datasets such as TriviaQA, Natural Questions, HotpotQA, NFCorpus, and SQuAD v1.1, plus 2 other instruments. These instruments are used as factual or factoid QA evaluations, and the scoring described in papers is usually benchmark-style correctness metrics: exact match appears repeatedly, TriviaQA is also reported with F1, and some multilingual evaluations use regular-expression answer extraction followed by exact match.

**What it is taken as evidence of.** Papers relate this behavior to 2 constructs, Factuality and Memorization, rather than consistently tying it to only one construct. One paper relates factual question answering to Factuality by describing gains in "factual accuracy" as measured by factual QA benchmarks, while another relates it to Memorization by stating that simple QA evaluates the ability to recall and retrieve factual knowledge accurately.

## Sources

**Factual question answering** (10 papers: [How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf), [CollabEdit: Towards Non-destructive Collaborative Knowledge Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/47eb71e8e778dc9def7780baa7b35687-Paper-Conference.pdf), [Where is the answer? An empirical study of positional bias for parametric knowledge extraction in language model](https://aclanthology.org/2025.naacl-long.58.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [From English to Second Language Mastery: Enhancing LLMs with Cross-Lingual Continued Instruction Tuning](https://aclanthology.org/2025.acl-long.1121.pdf), [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf), [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> The observable behavior of providing a precise, factually correct answer to a question requiring world knowledge.

**Factual query answering** (2 papers: [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf), [Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/880ee6e23b6ee548ebcccafe0ef0f513-Paper-Conference.pdf))
> The observable behavior of responding to a direct query about a problem state based on provided facts.

**Single-fact question answering** (1 paper: [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf))
> The observable task of answering questions that require only one supporting fact.

**Truthful Answering** (1 paper: [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf))
> The observable task of providing factually accurate answers as evaluated on benchmarks.

**Truthful question answering** (1 paper: [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf))
> The observable behavior of providing answers that are factually correct and avoid common misconceptions.

**Simple QA** (1 paper: [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf))
> Generating answers to questions that require retrieving and recalling a single fact or entity from a knowledge source.

**Fact-based question answering** (2 papers: [WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thede25a/thede25a.pdf), [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf))
> Producing correct answers to factual questions based on updated knowledge, where each question is derived from a subject-relation-object triplet.

**Faithfulness enhancement** (1 paper: [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf))
> Generating outputs that are more factually grounded and less hallucinatory in response to prompts requesting information.

**Fact-seeking question answering** (1 paper: [FacLens: Transferable Probe for Foreseeing Non-Factuality in Fact-Seeking Question Answering of Large Language Models](https://aclanthology.org/2025.emnlp-main.937.pdf))
> The task in which an LLM answers questions that ask for objective, verifiable information such as dates, locations, or entities, typically with short and precise responses.

**Factoid question answering** (5 papers: [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf), [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [From Low Rank Gradient Subspace Stabilization to Low-Rank Weights: Observations, Theories, and Applications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jaiswal25a/jaiswal25a.pdf), [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf), [Towards Robust Knowledge Representations in Multilingual LLMs for Equivalence and Inheritance based Consistent Reasoning](https://aclanthology.org/2025.naacl-long.394.pdf))
> The task of answering questions that have a single, concise factual answer, often requiring the retrieval of a few targeted facts.

**Trivia question answering** (1 paper: [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412.pdf))
> The task of providing a correct, factual answer to a question about trivia.

## Relationships

### Factual question answering →
- **TriviaQA** (measurement instrument): *measured_by*, 3 papers
  > For factual question answering, we use the TriviaQA dataset (Joshi et al., 2017) with a 10K testing set
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > Our evaluations cover factual question answering (NaturalQuestions (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017)) (Section 4.2).
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > The TruthfulQA dataset (Lin et al., 2021a) assesses the model’s capability in providing factual responses. (Section 2.3)
  - [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > the SQUAD, NFCORPUS, and SCI-DOCS datasets consist of factual questions involving single entities (Section 4.1).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **NFCorpus** (measurement instrument): *measured_by*, 1 paper
  > the SQUAD, NFCORPUS, and SCI-DOCS datasets consist of factual questions involving single entities (Section 4.1).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **SimpleQA** (measurement instrument): *measured_by*, 1 paper
  > Factuality: SimpleQA (Wei et al., 2024) and FreshQA-2025-04-28 (Vu et al., 2023), two factuality benchmarks that evaluate the ability of language models to answer fact-seeking questions. (Section 3.2)
  - [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)

### Associated with
- **Memorization** (construct), 1 paper
  > “Simple QA primarily evaluates the ability to recall and retrieve factual knowledge accurately.”
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Factuality** (construct), 1 paper
  > memory layers improve the factual accuracy of language models by over 100% as measured by factual QA benchmarks (Section 1).
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
