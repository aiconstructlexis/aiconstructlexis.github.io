# Factual knowledge
**Type:** Construct  
**Supporting papers:** 49  
**Also known as:** Factual recall, Knowledge recall, Fact recall, Long-term knowledge recall, Factual knowledge recall, Factual knowledge retrieval, Parametric knowledge retrieval  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats factual knowledge as a latent store, or extent, of encoded world facts that a model can accurately retrieve from its parameters or pretraining when queried. Closely related labels, including factual recall, fact recall, knowledge recall, factual knowledge retrieval, and parametric knowledge retrieval, mostly preserve this retrieval-centered framing. Smaller variations narrow the construct to specific factual associations or subject-relation-object triples, or emphasize whether retrieval is independent of current context versus used within a given task or query; as one paper notes, "the correct fact was present in the pretraining data but the model hallucinated" (HALoGEN: Fantastic LLM Hallucinations and Where to Find Them).

**Space of facets.** Papers use several near-synonymous names for overlapping ideas: factual knowledge, factual recall, fact recall, knowledge recall, long-term knowledge recall, factual knowledge recall, factual knowledge retrieval, and parametric knowledge retrieval. The same label is not used uniformly: knowledge recall can refer to retrieving world knowledge for visual question answering, recalling newly edited knowledge, or restating injected knowledge in its original form after knowledge injection. Other distinctions separate long-term or parametric knowledge that is absent from the prompt from broader real-world knowledge useful across tasks, and editing-oriented work represents facts as subject-relation-object triples; one study also reports that high-level concepts are more accessible than low-level details.

**Space of measurement.** Operationalization is almost entirely benchmark-based. Papers link the construct to 10 measurement instruments, most often MMLU, then CounterFact, Natural Questions, TriviaQA, and ARC-Challenge, plus 5 others; no behavioral indicators or linked constructs are attached to it. These instruments operationalize retrieval as accuracy on question answering benchmarks, knowledge-focused multiple-choice tasks, time-sensitive queries, and fact completion or model-editing tests. This mostly matches the dominant retrieval-based definitions, though some definitions describe the ability as independent of question format while the measurements instantiate it through particular QA or benchmark settings.

**Links.** Beyond measurement, one paper relates factual knowledge to WikiText, describing encyclopedic data such as WikiText as part of a "world fact loss" used to maintain general factual knowledge.

## Sources

**Factual knowledge** (6 papers: [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf), [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf), [HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://aclanthology.org/2025.acl-long.71.pdf), [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf))
> The extent to which a model has encoded and can accurately retrieve factual information about the world.

**Factual recall** (1 paper: [Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25k/guo25k.pdf))
> The latent ability of a model to retrieve and express specific factual associations.

**Knowledge recall** (4 papers: [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [Uncovering Overfitting in Large Language Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/c592fc7e6207f82560ed45fece8d6937-Paper-Conference.pdf), [Memorizing is Not Enough: Deep Knowledge Injection Through Reasoning](https://aclanthology.org/2025.acl-long.1392.pdf), [Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries](https://aclanthology.org/2025.emnlp-main.815.pdf))
> The model's ability to retrieve and use stored factual information or world knowledge to inform its responses in tasks like general visual question answering.

**Fact recall** (4 papers: [Position: Enough of Scaling LLMs! Lets Focus on Downscaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25c/goel25c.pdf), [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf))
> The ability of a model to store and retrieve factual information from its parameters.

**Long-term knowledge recall** (1 paper: [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf))
> The latent ability to access and retrieve stored factual knowledge about the world, such as historical, scientific, or geographical facts, independent of the current context.

**Factual knowledge recall** (1 paper: [Tracing and Dissecting How LLMs Recall Factual Knowledge for Real World Questions](https://aclanthology.org/2025.acl-long.1133.pdf))
> The latent ability of a model to access and utilize stored factual information relevant to a given context during reasoning.

**Factual knowledge retrieval** (1 paper: [Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf))
> The model's ability to access and retrieve stored factual information when prompted.

**Parametric knowledge retrieval** (1 paper: [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf))
> The latent ability of a model to retrieve factual knowledge that has been encoded during pre-training, independent of the current input context.

## Relationships

### Factual knowledge →
- **MMLU** (measurement instrument): *measured_by*, 6 papers
  > Factual knowledge: We use the Massive Multitask Language Understanding dataset (MMLU (Hendrycks et al., 2021)) to assess the factual knowledge of LLMs and report 5-shot results. (Section 4.1)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
  - [Compute-Constrained Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf)
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 2 papers
  > The CounterFact dataset is used to test the model’s factual knowledge of data from Wikipedia. (Section 5.1)
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 2 papers
  > For factual knowledge, we use PopQA (Mallen et al., 2023), TriviaQA (Joshi et al., 2017), and Natural Questions (NQ) (Kwiatkowski et al., 2019). (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > For factual knowledge, we use PopQA (Mallen et al., 2023), TriviaQA (Joshi et al., 2017), and Natural Questions (NQ) (Kwiatkowski et al., 2019). (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
  - [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
- **TimeQA** (measurement instrument): *measured_by*, 1 paper
  > We consider TimeQA (Chen et al., 2021) since it contains complex queries that require challenging time-sensitive knowledge. (Section 3.1)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 1 paper
  > For factual knowledge, two popular model editing datasets Zero-Shot Relation Extraction (ZSRE) (Levy et al., 2017) and COUNTERFACT (Meng et al., 2022) were adopted in our experiments. (Section 5.2)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **PopQA** (measurement instrument): *measured_by*, 1 paper
  > For factual knowledge, we use PopQA (Mallen et al., 2023), TriviaQA (Joshi et al., 2017), and Natural Questions (NQ) (Kwiatkowski et al., 2019). (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > "Knowledge-Focused Tasks include ARC-Challenge and ARC-Easy (Clark et al., 2018), PIQA (Bisk et al., 2019), Winogrande (Sakaguchi et al., 2019), OpenBookQA (Mihaylov et al., 2018), and HellaSwag (Zellers et al., 2019). These benchmarks primarily assess factual knowledge"
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > "Knowledge-Focused Tasks include ARC-Challenge and ARC-Easy (Clark et al., 2018), PIQA (Bisk et al., 2019), Winogrande (Sakaguchi et al., 2019), OpenBookQA (Mihaylov et al., 2018), and HellaSwag (Zellers et al., 2019). These benchmarks primarily assess factual knowledge"
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)

### Associated with
- **WikiText** (measurement instrument), 1 paper
  > The world fact loss uses encyclopedic data (e.g., WikiText (Merity et al., 2017)) to maintain general factual knowledge. (Section 1).
  - [OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.emnlp-main.183.pdf)
