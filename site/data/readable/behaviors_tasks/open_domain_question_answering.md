# Open-domain question answering
**Type:** Behavioral indicator  
**Supporting papers:** 38  
**Also known as:** Retrieval-augmented question answering  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is broad-topic question answering: models answer questions about a wide range of topics or general world knowledge, rather than a fixed domain. Most descriptions also make retrieval explicit, describing answers as synthesized from an external corpus, knowledge base, open web, or large-scale unstructured documents. A smaller line of work narrows this to retrieval-augmented question answering, where the model first retrieves relevant information or is given search documents as context, and some papers further treat the outputs as short-form answers, typically a short phrase or sentence, sometimes using only the provided documents.

**Variants.** Papers use several nearby labels, including open-domain QA, ODQA, retrieval-augmented question answering, and RAG QA. Most variants still center on broad-topic factual answering, while some papers focus on short-form generation with short-answer ground truth, conflicts between parametric knowledge and contextual knowledge, synthesis from open-web or large-scale unstructured documents, or answering only from provided search documents. One benchmark also places the task in low-resource Indonesian languages.

**Space of elicitation and scores.** This behavior is measured by 12 linked instruments, mostly QA datasets or benchmark suites. The most frequently linked are TriviaQA, Natural Questions, PopQA, WebQuestions, and MS MARCO, with several other instruments also linked. Scoring details are mostly left implicit by benchmark choice, though one paper reports using F1 because its open-domain QA datasets have short-answer ground truth.

**What it is taken as evidence of.** Papers do not link open-domain question answering to any construct, so no construct is reported as something this behavior indicates.

## Sources

**Open-domain question answering** (15 papers: [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf), [Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf), [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf), [Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf), [Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering](https://aclanthology.org/2025.acl-long.981.pdf), [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf), [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf))
> The task of answering questions about a wide range of topics, not limited to a specific domain or context.

**Retrieval-augmented question answering** (3 papers: [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf), [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf))
> The task of answering questions by first retrieving relevant information from an external knowledge source and then synthesizing an answer based on that information.

## Relationships

### Open-domain question answering →
- **TriviaQA** (measurement instrument): *measured_by*, 13 papers
  > We evaluate BTR on five knowledge-rich NLP tasks, including three open-domain question-answering tasks (NaturalQuestions (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), and WebQA (Berant et al., 2013)) (Section 2).
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Conformal Generative Modeling with Improved Sample Efficiency through Sequential Greedy Filtering](https://proceedings.iclr.cc/paper_files/paper/2025/file/c2a96d676ac2716615bf1ab7edd3f3d3-Paper-Conference.pdf)
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [Refine Knowledge of Large Language Models via Adaptive Contrastive Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd010aed9a0d7f56144bd5dcaa95b9e-Paper-Conference.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 10 papers
  > We evaluate BTR on five knowledge-rich NLP tasks, including three open-domain question-answering tasks (NaturalQuestions (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), and WebQA (Berant et al., 2013)) (Section 2).
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 8 papers
  > Moreover, in order to examine ToG on more generic tasks, we also prepare one open-domain QA dataset: WebQuestions (Berant et al., 2013);
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
- **PopQA** (measurement instrument): *measured_by*, 8 papers
  > Short-form generations tasks include two open-domain question answering (QA) datasets, PopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017)... (Section 4.1)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
- **MS MARCO** (measurement instrument): *measured_by*, 2 papers
  > The open-domain QA tasks consist of NQ (Kwiatkowski et al., 2019), MARCO QA (Bajaj et al., 2016) and TriviaQA (Joshi et al., 2017), which require models to retrieve factual knowledge to help LLMs answer the given question.
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 2 papers
  > We use the open domain question answering datasets WebQuestion (Berant et al., 2013), NaturalQA (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017) and SQuAD (Rajpurkar, 2016), as well as the complex multi-hop question answering datasets HotpotQA (Ho et al., 2020a) and 2WikiMultiHopQA (Ho et al., 2020b). (Section 4.2)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
- **TriviaQA-unfiltered** (measurement instrument): *measured_by*, 1 paper
  > Short-form generations tasks include two open-domain question answering (QA) datasets, PopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017)... (Section 4.1)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **AmbigNQ** (measurement instrument): *measured_by*, 1 paper
  > we use three open-domain QA datasets for evaluation, namely PopQA (Mallen et al., 2023a), AmbigNQ (Min et al., 2020) and HotpotQA (Yang et al., 2018). (Section 4)
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > we use three open-domain QA datasets for evaluation, namely PopQA (Mallen et al., 2023a), AmbigNQ (Min et al., 2020) and HotpotQA (Yang et al., 2018). (Section 4)
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **LoraxBench** (measurement instrument): *measured_by*, 1 paper
  > We introduce LORAXBENCH, a benchmark that focuses on low-resource languages of Indonesia and covers 6 diverse tasks: reading comprehension, open-domain QA, language inference, causal reasoning, translation, and cultural QA. (Abstract)
  - [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20 Indonesian Languages](https://aclanthology.org/2025.emnlp-main.881.pdf)
- **ParaRel** (measurement instrument): *measured_by*, 1 paper
  > ...and factual information from open-domain question answering (OQA) with the PARAREL (Elazar et al., 2021) dataset. (Section 4)
  - [Sheaf Discovery with Joint Computation Graph Pruning and Flexible Granularity](https://aclanthology.org/2025.emnlp-main.446.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 1 paper
  > TriviaQA, MuSiQue, PopQA are challenging open-domain question answering datasets where RAG systems are required to answer questions on factual knowledge. (Section 4)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
