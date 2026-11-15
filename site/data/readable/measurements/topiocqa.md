# TopiOCQA
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Several papers describe TopiOCQA as a conversational search benchmark or dataset built around multi-turn information-seeking dialogues or queries. One definition specifies gold-standard passage retrieval and response generation labels, and other papers emphasize context-dependent questions that require disambiguation from prior turns; a smaller line of work frames it as a conversational question answering dataset or as a benchmark known for challenging topic shifts within conversations, where systems must decide whether to retain earlier context.

**What it is claimed to measure.** Recorded links tie TopiOCQA to 1 construct and 1 behavioral indicator. The prevailing measured_by claim centers on Generalization: a paper uses TopiOCQA to evaluate generalization ability by training on its training set and testing on QReCC, and vice versa. The only behavioral-indicator link uses different language, reporting TopiOCQA as related to Query rewriting because its context-dependent questions are used for clarifying an original question into a standalone question.

**Space of uses.** Across the papers, TopiOCQA is positioned as a widely used evaluation setting for conversational search, especially for query reformulation and retrieval in multi-turn interactions. It is most often used alongside QReCC, and some papers also pair it with TREC CAsT 2019, 2020, and 2021 and ORConvQA; uses include main benchmark evaluation, training data for a reward model, checks of sparse and dense retrieval, and assessment of generated content reliability via provided evidence or rationale. No measurement instrument is linked to it by a recorded relationship.

## Sources

**TopiOCQA** (6 papers: [UniConv: Unifying Retrieval and Response Generation for Large Language Models in Conversations](https://aclanthology.org/2025.acl-long.344.pdf), [AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.193.pdf), [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf), [ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1349.pdf), [ICR: Iterative Clarification and Rewriting for Conversational Search](https://aclanthology.org/2025.emnlp-main.496.pdf), [Learning Contextual Retrieval for Robust Conversational Search](https://aclanthology.org/2025.emnlp-main.602.pdf))
> Conversational search benchmark containing multi-turn information-seeking dialogues with gold-standard passage retrieval and response generation labels.

## Relationships

### → TopiOCQA
- **Generalization** (construct): *measured_by*, 1 paper
  > For the evaluation of generalization ability, we trained models on the TopiOCQA training set and evaluated them on the QReCC test set, and vice versa.
  - [ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1349.pdf)

### Associated with
- **Query rewriting** (behavioral indicator), 1 paper
  > We employ TopiOCQA (Adlakha et al., 2022) and QReCC (Anantha et al., 2021), both of which consist of multi-turn conversational queries. These datasets contain context-dependent questions...requiring disambiguation based on prior conversation turns. Hence, in the sub-task, LLM clarifies the original question into a standalone question. (Section 3)
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf)
