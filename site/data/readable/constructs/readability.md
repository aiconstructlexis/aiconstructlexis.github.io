# Readability
**Type:** Construct  
**Supporting papers:** 22  
**Also known as:** Human-readability, Cognitive effort during reading, Understandability, Human readability  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats readability as how easy generated or revised text is for people to read and understand, often expressed as clarity, accessibility, or being "not too technical for laymen." Many definitions tie it to surface or linguistic difficulty, mentioning sentence length, word complexity, vocabulary, or lexical and syntactic complexity. Smaller strands use the label differently: adversarial-prompt papers use human-readability for coherent, human-like prompts that remain understandable enough to evade filters, while other papers define readability through subtitle constraints or as latent reading effort inferred from reading behavior.

**Space of facets.** Different papers organize the construct around different targets: general-audience accessibility and reader feedback, formal text properties such as sentence structure and vocabulary, and in one code-translation paper, stylistic consistency through variable naming, code structure, and function signatures. The term overlaps with understandability and accessibility, and one evaluation framework places readability under User Alignment rather than treating it as a standalone quality. Papers also contrast it with task goals in some settings, as a patent-claim revision study explicitly reports 'Readability (↓)' and notes that better revisions can become denser and less readable.

**Space of measurement.** Readability is linked to 1 measurement instrument, Human evaluation, and to 1 behavioral indicator, Text simplification. The linked instrument is a human-rating setup, and papers use it through direct judgments or pairwise comparisons of readability and nearby axes such as understandability. Papers also operationalize readability with automatic or analytic proxies, especially Flesch Reading Ease Score, Gunning Fog index, and CPL/CPS, with other readability tests and reading-behavior analyses appearing as well; most of these are introduced as ways to assess how understandable text is, though the subtitle-constraint use and the patent-revision 'Readability (↓)' use are more task-specific.

**Links.** Among the 2 linked constructs, one paper claims a causal relationship from Human preference alignment to Readability, stating that aligning with aggregated client preference can improve professionalism and readability, while another paper relates readability to User Alignment. Another paper claims a causal relationship from Text simplification to Readability, reporting that simplified inputs lead to translations rated as more understandable. Readability is also related to Text generation quality in work that evaluates text quality with Flesch score and semantic similarity, and no correlation claim is reported.

## Sources

**Readability** (11 papers: [Lived Experience Not Found: LLMs Struggle to Align with Experts on Addressing Adverse Drug Reactions from Psychiatric Medication Use](https://aclanthology.org/2025.naacl-long.553.pdf), [MoDS: Moderating a Mixture of Document Speakers to Summarize Debatable Queries in Document Collections](https://aclanthology.org/2025.naacl-long.20.pdf), [Patent-CR: A Dataset for Patent Claim Revision](https://aclanthology.org/2025.naacl-long.116.pdf), [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf), [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [JRE-L: Journalist, Reader, and Editor LLMs in the Loop for Science Journalism for the General Audience](https://aclanthology.org/2025.naacl-long.335.pdf), [A-TASC: Asian TED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.157.pdf), [Function-to-Style Guidance of LLMs for Code Translation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cb/zhang25cb.pdf), [Genre Matters: How Text Types Interact with Decoding Strategies and Lexical Predictors in Shaping Reading Behavior](https://aclanthology.org/2025.emnlp-main.379.pdf), [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf))
> The quality of generated text being easy to read and understand, as judged by human evaluators.

**Human-readability** (1 paper: [AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf))
> The quality of a generated text, such as an adversarial prompt, being semantically coherent and appearing as if written by a human, making it difficult to distinguish from benign inputs.

**Cognitive effort during reading** (1 paper: [Genre Matters: How Text Types Interact with Decoding Strategies and Lexical Predictors in Shaping Reading Behavior](https://aclanthology.org/2025.emnlp-main.379.pdf))
> The latent level of mental processing load a reader experiences while comprehending a text, inferred from eye movement patterns and modulated by text type, word-level features, and decoding strategies.

**Understandability** (1 paper: [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf))
> The quality of a generated text being clear and easy to comprehend by a human reader.

**Human readability** (1 paper: [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf))
> The extent to which generated adversarial prompts remain understandable and natural enough to avoid detection by readability-based filters.

## Relationships

### Readability →
- **Human evaluation** (measurement instrument): *measured_by*, 3 papers
  > “To assess our proposed method, we employ both automatic metrics and human evaluation on measures including readability...”
  - [JRE-L: Journalist, Reader, and Editor LLMs in the Loop for Science Journalism for the General Audience](https://aclanthology.org/2025.naacl-long.335.pdf)
  - [Accelerating Unbiased LLM Evaluation via Synthetic Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25v/zhou25v.pdf)
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf)

### → Readability
- **Human preference alignment** (construct): *causes*, 2 papers
  > By aligning the LLM with the aggregated client preference, we can improve the professionalism and readability of LLM’s generated content. (Section 1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Text simplification** (behavioral indicator): *causes*, 1 paper
  > the human evaluation results confirm that translations from simplified inputs are rated as more fluent, understandable, and better at preserving the meaning of the reference translation. (Section 5.3)
  - [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf)

### Associated with
- **Text generation quality** (construct), 1 paper
  > Text quality is measured by absolute perplexity difference (|∆PPL|), Flesch reading ease score (Flesch), and semantic similarity (Sim) between the attacked and original text. Lower detection accuracy (↓) indicates better evasion, while higher Flesch and Sim scores (↑) reflect better readability and semantic preservation.
  - [TempParaphraser: “Heating Up” Text to Evade AI-Text Detection through Paraphrasing](https://aclanthology.org/2025.emnlp-main.1607.pdf)
