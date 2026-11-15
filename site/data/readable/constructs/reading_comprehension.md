# Reading comprehension
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Multiple-choice reading comprehension, Machine reading comprehension  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats reading comprehension as understanding or interpreting a written passage and extracting the information needed to answer questions or complete tasks. Many authors frame this as a latent ability, as in the claim that it requires "strong reading comprehension skills to interpret and extract accurate information," while a smaller line of work defines it more directly as the observable task of answering questions from a given context. The narrower task framing sometimes specifies answer formats such as multiple-choice selection or span extraction, and one variant also includes deciding whether a question can be answered using the passage.

**Space of facets.** Papers use the label at several levels of scope. Some treat it as a broad capability category, often listed alongside question answering, commonsense reasoning, world knowledge, mathematical reasoning, dialog, or conversational proficiency, while others name subtypes such as multiple-choice reading comprehension and machine reading comprehension. A few formulations broaden the category further, for example by grouping readability and natural language inference under reading comprehension, whereas another line narrows it to a "Comprehension" skill in question answering style evaluations.

**Space of measurement.** Operationalization is narrow in the linked measurements: papers connect the construct to 2 measurement instruments, RACE and OpenBookQA, and to no behavioral indicators. Both are benchmarks, with RACE described as a multiple-choice reading comprehension task or benchmark, and OpenBookQA said to assess "book comprehension ability." Beyond those named links, source descriptions make the measured behavior concrete as passage-based question answering in multiple-choice, exact-match-from-context, span-extraction, and answerability settings, and one machine reading comprehension setup evaluates answers on relevance, factuality, and completeness. These measurements mostly match the dominant definition of passage understanding, though some extend it to deciding whether a question is answerable from the passage or to rating answer quality dimensions.

**Links.** The papers only report measurement links for this construct. More than one paper says reading comprehension is measured by RACE, and one paper says it is measured by OpenBookQA; the accompanying evidence describes RACE as a multiple-choice reading comprehension task and OpenBookQA as assessing book comprehension ability. No paper reports a causal, correlational, or other related relationship involving reading comprehension.

## Sources

**Reading comprehension** (4 papers: [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf), [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf), [VMLU Benchmarks: A comprehensive benchmark toolkit for Vietnamese LLMs](https://aclanthology.org/2025.acl-long.563.pdf), [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf))
> Understanding and extracting information from written passages to answer questions or complete tasks.

**Multiple-choice reading comprehension** (1 paper: [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf))
> The observable task of answering questions about a given text by selecting the correct option from a predefined set of choices.

**Machine reading comprehension** (1 paper: [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf))
> The ability to understand a given text and answer questions based on it, evaluated on dimensions such as relevance, factuality, and completeness.

## Relationships

### Reading comprehension →
- **RACE** (measurement instrument): *measured_by*, 2 papers
  > “we also included the multiple-choice reading comprehension task RACE”
  - [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > “OpenbookQA (Mihaylov et al., 2018) can assess the book comprehension ability”
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
