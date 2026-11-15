# Language understanding task performance
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Text comprehension, Language understanding, Natural language understanding, Natural language understanding tasks  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is performance on collections of language understanding tasks, often framed through GLUE- or SuperGLUE-style evaluations. These tasks are described as classification, similarity and paraphrase, natural language inference, sentiment analysis, textual entailment, grammatical correctness, and question answering, all requiring comprehension of text inputs. A smaller line of work narrows the behavior to text comprehension, where success means answering questions or producing outputs that require understanding and integrating information from text.

**Variants.** Papers use several overlapping names for this behavior, including text comprehension, language understanding, natural language understanding, and natural language understanding tasks. The task families mentioned span single-sentence classification, similarity and paraphrase, natural language inference, paraphrase identification, semantic similarity judgment, sentiment analysis, textual entailment, grammatical correctness, and question answering. Some papers also instantiate it on specific understanding-oriented settings such as HotpotQA, XQuAD, and TextVQA.

**Space of elicitation and scores.** Papers measure it with 15 instruments. The instruments listed most often are GLUE and MMLU, followed by ARC-Challenge, ARC-Easy, and HellaSwag. The linked measures are mostly benchmark suites or datasets for language understanding evaluation, and one paper also refers to the lm-evaluation-harness project as a source of language benchmarks.

**What it is taken as evidence of.** No construct is linked to it in the reported relationships, so papers do not explicitly present this behavior as evidence of a construct here.

## Sources

**Text comprehension** (1 paper: [Select-Then-Decompose: From Empirical Analysis to Adaptive Selection Strategy for Task Decomposition in Large Language Models](https://aclanthology.org/2025.emnlp-main.278.pdf))
> Answering questions or producing outputs that require understanding and integrating information from text.

**Language understanding** (2 papers: [The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models](https://aclanthology.org/2025.emnlp-main.1143.pdf), [On the Analysis and Distillation of Emergent Outlier Properties in Pre-trained Language Models](https://aclanthology.org/2025.naacl-long.430.pdf))
> Performing a range of language understanding tasks such as those included in SuperGLUE.

**Natural language understanding** (3 papers: [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf))
> Performing classification, similarity, paraphrase, and inference tasks on text inputs.

**Natural language understanding tasks** (1 paper: [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf))
> A collection of observable tasks designed to test language comprehension, such as sentiment analysis, textual entailment, and grammatical correctness.

## Relationships

### Language understanding task performance →
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > we evaluate both the zero-shot and few-shot performance of the LLMs on Massively Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2021). (Section 4.1)
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > MDMs are only advantageous in language understanding tasks (surpassing ARMs and BERT on the GLUE metric (Wang et al., 2018)). (Section 3.3)
  - [Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e3b203e72c4e058de26d02a92a81844-Paper-Conference.pdf)
  - [On the Analysis and Distillation of Emergent Outlier Properties in Pre-trained Language Models](https://aclanthology.org/2025.naacl-long.430.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > Then we utilize popular language benchmarks provided in the open-sourced lm-evaluation-harness project [18] for evaluation
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **SuperGLUE** (measurement instrument): *measured_by*, 1 paper
  > The first benchmark, SuperGLUE, is a collection of eight challenging language understanding and reasoning tasks.
  - [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a comprehensive breakdown of downstream evaluation results for our models and multiple baselines on a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29] (Section 5).
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **WSC** (measurement instrument): *measured_by*, 1 paper
  > Language Understanding (LU): Lambada-OpenAI [44], Hellaswag-0-shot [65], Winograd-3-shots [30], and WinoGrande-5-shots [54].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > a language understanding dataset XNLI [Conneau et al., 2018] in natural language inference (NLI) task were used. (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **XQuAD** (measurement instrument): *measured_by*, 1 paper
  > Employing various benchmark tasks, including XQuAD (Artetxe et al., 2020) for understanding, MGSM (Shi et al., 2022) for reasoning, X-CSQA (Lin et al., 2021) for knowledge extraction, and XLSum for generation (Hasan et al., 2021)... (Section 2)
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 1 paper
  > “a standard set of commonsense reasoning and language understanding tasks: WinoGrande [33], HellaSwag [45], PIQA [2], ARC-Challenge and ARC-Easy [6], and LAMBADA [29].”
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks that involve spatial understanding and fine-grained features include ... text comprehension (TextVQA; Singh et al. 2019). (Section 5)
  - [Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > Comparison of decomposition approaches across benchmarks. Method ... Text Understanding ... HotpotQA (Table 2)
  - [Select-Then-Decompose: From Empirical Analysis to Adaptive Selection Strategy for Task Decomposition in Large Language Models](https://aclanthology.org/2025.emnlp-main.278.pdf)
