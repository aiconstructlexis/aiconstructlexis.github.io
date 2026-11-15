# Few-shot task performance
**Type:** Behavioral indicator  
**Supporting papers:** 42  
**Also known as:** Few-shot task solving, Few-shot learning, Few-shot inference  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this as observable downstream or benchmark performance when only a small number of examples are available, most often as in-context demonstrations in the prompt. Success is usually framed as answering, completing, or predicting correctly on those tasks, and papers commonly report it as accuracy or downstream performance. Some descriptions instead speak of an ability or capacity to learn or generalize from few examples, and a smaller line uses the label for settings with only a few labeled examples per class or very limited training data, including adaptation and forecasting setups.

**Variants.** A common variant appears in long-context evaluations, where few-shot learning is treated as one task category alongside question-answering, summarization, and code completion. Another recurring variant is time series forecasting with only 10% or the first 5 to 10% of time steps available for training. Other papers cast it as N-way-K-shot relation extraction or as tasks with only k labeled examples per class, and some descriptions emphasize using the provided examples to guide output generation or retrieve relevant QA pairs.

**Space of elicitation and scores.** Papers link this behavior to 7 measurement instruments. LongBench is the most common, usually treating few-shot learning as one category within a broader long-context benchmark; other linked instruments are the Abstraction and Reasoning Corpus, HellaSwag, ARC-Challenge, and LongBench-E, plus 2 other instruments. The linked instruments are mostly benchmarks, and papers also use an evaluation framework to average accuracy over seven few-shot tasks; scoring is commonly reported as accuracy or downstream task performance, sometimes in explicit 5-shot or 20-shot settings.

**What it is taken as evidence of.** Papers relate this behavior to 3 constructs, most commonly in-context learning, and also generalization and long-context understanding. In-context learning is described through few-shot performance, meaning accuracy on novel tasks when the prompt contains a few demonstrations. Other papers connect it to generalizing from minimal supervision or to understanding long contexts well enough to use a few examples for tasks such as classification, summarization, and reading comprehension. Overall, the construct link is distributed across multiple related constructs rather than only one.

## Sources

**Few-shot task performance** (1 paper: [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf))
> The observable performance of a model on a downstream task when provided with a small number of examples in its context.

**Few-shot task solving** (1 paper: [Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf))
> Answering or completing benchmark tasks when provided with only a small number of in-context examples.

**Few-shot learning** (8 papers: [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [HyperAttention: Long-context Attention in Near-Linear Time](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5aa940590399350401c57cdf52ce78-Paper-Conference.pdf), [Large Language Models to Enhance Bayesian Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/84b8d9fcb4e262fcd429544697e1e720-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf), [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf), [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf), [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf))
> Performing tasks based on a small number of in-context examples provided in the input, requiring generalization and pattern recognition within long contexts.

**Few-shot inference** (1 paper: [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf))
> Making predictions on downstream tasks using only a small number of labeled examples per class.

## Relationships

### Few-shot task performance →
- **LongBench** (measurement instrument): *measured_by*, 11 papers
  > “we further investigate the benefits of long context models for few-shot tasks using two additional datasets (Trec and SAMSum) from LongBench.”
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [ThinK: Thinner Key Cache by Query-Driven Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf)
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [Squeezed Attention: Accelerating Long Context Length LLM Inference](https://aclanthology.org/2025.acl-long.1568.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [DAC: A Dynamic Attention-aware Approach for Task-Agnostic Prompt Compression](https://aclanthology.org/2025.acl-long.952.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 2 papers
  > We test the following: 5-shot MMLU [14] and 20-shot HellaSwag [61] benchmarks. (Section 6.1)
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Abstraction and Reasoning Corpus** (measurement instrument): *measured_by*, 2 papers
  > "The ARC benchmark’s emphasis on generalization and few-shot learning"
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We test the following: 5-shot MMLU [14] and 20-shot HellaSwag [61] benchmarks. (Section 6.1)
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > Interestingly, CREAM improves over Llama2-7B on ARC-C and HellaSwag. This is because these two tasks are few-shot tasks with longer prompts...
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **LongBench-E** (measurement instrument): *measured_by*, 1 paper
  > we further test LongMamba on the LongBench-E dataset (Bai et al., 2023), which covers 13 long-context applications, such as coding and few-shot learning. (Section 6.2)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > We used the Language Model Evaluation Harness framework (Gao et al., 2023) to evaluate accuracy on seven few-shot tasks, and averaged them for performance comparison. (Section 3.1)
  - [Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 3 papers
  > "Prompting with task-specific demonstrations (i.e., in-context learning (Brown et al., 2020))"
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Which Attention Heads Matter for In-Context Learning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25e/yin25e.pdf)
- **Generalization** (construct), 2 papers
  > Humans exhibit remarkable few-shot learning capabilities, rapidly generalizing from a single task demonstration to related conditions by integrating the observed behavior with their internal world model.
  - [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ac50fd0a4eeeb1f077b17bb7c5353c3-Paper-Conference.pdf)
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Time series forecasting** (behavioral indicator), 1 paper
  > Based on the settings in Zhou et al. (2023), we present few-shot forecasting for 10% time steps in training datasets. (Section 4.2)
  - [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
- **Relation extraction** (behavioral indicator), 1 paper
  > Few-shot Continual Relation Extraction (FCRE) has emerged as a significant challenge in information extraction, necessitating that relation extraction (RE) systems can sequentially identify new relations with limited labeled samples. (Abstract)
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Long-context understanding** (construct), 1 paper
  > We evaluate our DSLA model on tasks requiring careful long-range interactions (Bai et al., 2024), including: ... (iii) Few-shot learning requires the model to comprehend a limited number of examples and effectively perform various tasks, including classification, summarization, and reading comprehension.
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
