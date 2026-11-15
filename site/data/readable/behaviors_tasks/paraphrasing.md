# Paraphrasing
**Type:** Behavioral indicator  
**Supporting papers:** 39  
**Also known as:** Text rephrasing, Rewriting, Text paraphrasing, Query rephrasing, Profile diversification, Paraphrase generation, Machine paraphrasing, Rephrasing  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats paraphrasing as rewriting an input text in different words or structures while preserving its original meaning, semantic equivalence, or full meaning. This usage appears for documents, sentences, mixed text segments, queries, and profiles, with success usually described as changing wording, syntax, lexical form, or other surface form without changing the semantics. A smaller set of formulations adds task-specific constraints, such as preserving class label, leaving persuasive style unspecified, or using paraphrasing as a pretraining or augmentation task; one multi-turn setup instructs agents to paraphrase the received text "without modifying its meaning" (When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings).

**Variants.** Papers use several nearby names for the behavior, most commonly text rephrasing, rewriting, text paraphrasing, query rephrasing, and paraphrase generation. The behavior is studied in ordinary sentence or document rewriting, but also in recursive chunk-level rewriting, user or item profile rewriting, and query augmentation. Recurring settings include watermark or detector evasion, translation input rewriting, style transfer, plagiarism and data augmentation, and iterative rephrasing across turns or rounds.

**Space of elicitation and scores.** No measurement instrument is linked to paraphrasing. Papers instead usually elicit it with direct prompts to paraphrase or rephrase an input, and some use named paraphrasers such as DIPPER or the T5-based Parrot paraphraser. Where scoring is described, one paper refers to MRPC with human annotations for semantic equivalence, and another defines evasion by whether a watermark is no longer retained after a paraphrasing attack.

**What it is taken as evidence of.** At the construct level, papers only connect paraphrasing to Semantic preservation, and they do so as a related link rather than as a direct measurement claim; one paper states that paraphrase-based pretraining enables rewriting "without changing the semantics." Beyond constructs, papers also relate paraphrasing to De-identification and Instruction following, and one paper, Optimizing Adaptive Attacks against Watermarks for Language Models, claims a causal relationship from paraphrasing to Watermark removal through a paraphrasing attack. No other construct is linked.

## Sources

**Paraphrasing** (11 papers: [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf), [PaLD: Detection of Text Partially Written by Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d799b1d6a5e43546e67e7afdeffc067d-Paper-Conference.pdf), [Measuring and Benchmarking Large Language Models' Capabilities to Generate Persuasive Language](https://aclanthology.org/2025.naacl-long.506.pdf), [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf), [B4: A Black-Box Scrubbing Attack on LLM Watermarks](https://aclanthology.org/2025.naacl-long.460.pdf), [Style Transfer with Multi-iteration Preference Optimization](https://aclanthology.org/2025.naacl-long.135.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [Evaluating the Evaluation of Diversity in Commonsense Generation](https://aclanthology.org/2025.acl-long.1181.pdf), [Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite Attacks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25c/cheng25c.pdf), [BTC-SAM: Leveraging LLMs for Generation of Bias Test Cases for Sentiment Analysis Models](https://aclanthology.org/2025.emnlp-main.763.pdf), [Few-Shot Detection of Machine-Generated Text using Style Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e54a2592e3f51b9bed625a780310424-Paper-Conference.pdf))
> Reproducing the content of a document in different words, used here as a pretraining task to align retrieval features with text.

**Text rephrasing** (2 papers: [When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbdea7859f1d2fc10f2c9e79b8f5ae54-Paper-Conference.pdf), [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf))
> Producing a paraphrase of an input text while preserving its meaning.

**Rewriting** (2 papers: [LLMs can be easily Confused by Instructional Distractions](https://aclanthology.org/2025.acl-long.957.pdf), [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.357.pdf))
> The task of rephrasing a given text to alter its structure or wording while preserving its original semantic meaning.

**Text paraphrasing** (1 paper: [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf))
> The observable act of generating a new text that preserves the semantic meaning of an original text but uses different wording or structure.

**Query rephrasing** (1 paper: [DocReRank: Single-Page Hard Negative Query Generation for Training Multi-Modal RAG Rerankers](https://aclanthology.org/2025.emnlp-main.436.pdf))
> Modifying the phrasing of a query while preserving its original meaning to test for reliance on semantic rather than surface-level cues.

**Profile diversification** (1 paper: [EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.894.pdf))
> The observable behavior of an LLM rephrasing a given user or item profile to generate multiple semantically similar but textually distinct versions for data augmentation.

**Paraphrase generation** (3 papers: [PlagBench: Exploring the Duality of Large Language Models in Plagiarism Generation and Detection](https://aclanthology.org/2025.naacl-long.384.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf))
> The model produces semantically equivalent variations of input sentences, used to expand diagnostic datasets while preserving meaning.

**Machine paraphrasing** (1 paper: [On the Reliability of Watermarks for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d78e9e4316e1714fbb0f20be66f8044c-Paper-Conference.pdf))
> The observable act of using a language model to rewrite or rephrase a given text, often with the goal of altering its surface form while preserving meaning.

**Rephrasing** (1 paper: [LLM as a Broken Telephone: Iterative Generation Distorts Information](https://aclanthology.org/2025.acl-long.371.pdf))
> The task of rewriting a given document to use different wording while preserving its original meaning, used as an alternative iterative task.

## Relationships

### Paraphrasing →
- **Watermark removal** (behavioral indicator): *causes*, 1 paper
  > The evasion rate is calculated as the fraction of watermarked text that does not retain the watermark after applying the paraphrasing attack. (Section 6.2)
  - [Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf)

### Associated with
- **De-identification** (behavioral indicator), 1 paper
  > Additionally, we make use of the state-of-the-Art 11B transformer-based paraphrasing model Dipper (Krishna et al., 2024) to baseline the anonymizing effect of pure text paraphrasing. (Sec. 5)
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Semantic preservation** (construct), 1 paper
  > “We pre-train DiffuSeq using the paraphrase dataset, which enables it to rewrite the input without changing the semantics.”
  - [DiffusionAttacker: Diffusion-Driven Prompt Manipulation for LLM Jailbreak](https://aclanthology.org/2025.emnlp-main.1128.pdf)
