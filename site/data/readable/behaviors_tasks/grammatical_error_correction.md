# Grammatical error correction
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Grammar correction, Text correction, Proofreading, Grammar error correction, Grammar checking  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a correction task: taking text or a sentence with grammatical errors and producing a corrected, more grammatically accurate, often error-free version. Most formulations stress both detection and correction, and some explicitly describe the output as rewriting erroneous text into corrected text; one paper states that systems should "detect and correct all grammatical errors in the sentence and produce an error-free sentence as the output," and some descriptions make the edits explicit as insertion, deletion, re-ordering, or substitution. A smaller set broadens the target beyond grammar to spelling, punctuation, awkward phrases, typos, and certain semantic errors, while one proofreading formulation specifies correction without explanations or analysis and one grammar-checking formulation emphasizes outputs that preserve most of the input.

**Variants.** Papers use several nearby names for this behavior, most often grammatical error correction or grammar correction, with smaller variants such as grammar error correction, grammar checking, proofreading, and text correction. The settings span multilingual GEC, Chinese GEC, English sentence correction, and a text-correction task described as having clearly defined correction answers. Some Chinese formulations make the subtypes of edits explicit, listing missing, redundant, substitution, and word-order errors, or insertion, deletion, re-ordering, and substitution operations.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, MERLIN. Papers describe MERLIN as a dataset used for grammar correction in the original-language setting, specifically for Italian, so the recorded operationalization is via a task dataset.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects, and instead link it to three constructs. It is related to In-context learning, with multilingual GEC described as using an in-context learning approach, and it is related to Multilingual ability, with multilingual GEC discussed in the context of language learning across different languages. A separate claim records a causal relationship from Grammatical error correction to Interpretability and explainability, citing example-based GEC systems that can enhance system interpretability by providing illustrative examples.

## Sources

**Grammatical error correction** (2 papers: [CLEME2.0: Towards Interpretable Evaluation by Disentangling Edits for Grammatical Error Correction](https://aclanthology.org/2025.acl-long.10.pdf), [Leveraging What's Overfixed: Post-Correction via LLM Grammatical Error Overcorrection](https://aclanthology.org/2025.emnlp-main.1431.pdf))
> The observable process of detecting and correcting grammatical errors in a given text, producing a revised version that is more grammatically accurate.

**Grammar correction** (2 papers: [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf))
> Identifying and generating the correct form of a given input that contains grammatical errors.

**Text correction** (1 paper: [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> Detecting and correcting errors in text, including typos and other modifications needed to match a reference answer.

**Proofreading** (1 paper: [LLMs can be easily Confused by Instructional Distractions](https://aclanthology.org/2025.acl-long.957.pdf))
> Reviewing and correcting grammar, spelling, and punctuation errors in a text without providing explanations or analysis.

**Grammar error correction** (1 paper: [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf))
> The task of identifying and correcting grammatical errors in a given text.

**Grammar checking** (1 paper: [BanditSpec: Adaptive Speculative Decoding via Bandit Algorithms](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25h/hou25h.pdf))
> Generating outputs that closely preserve the input while correcting or checking grammatical form.

## Relationships

### Grammatical error correction →
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > One advantage of example-based GEC systems is that they can enhance system interpretability by providing learners with illustrative examples (Kaneko et al., 2022). (Section 2.1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
- **MERLIN** (measurement instrument): *measured_by*, 1 paper
  > Therefore, we used datasets collected in the original languages for Grammar Correction, namely ... Merlin (Boyd et al., 2014) for Italian... (Section 4.1)
  - [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > Our work extends the use of LLMs in multilingual GEC through an easy-to-use in-context learning approach. (Section 2.1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Multilingual ability** (construct), 1 paper
  > Given the need for language learning across different languages, multilingual GEC has become an important area of research. (Section 1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
