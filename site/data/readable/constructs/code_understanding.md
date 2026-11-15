# Code understanding
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Code comprehension, Verilog understanding, Cross-file understanding, Program semantics understanding, Program comprehension, Code-level understanding, Cross-file dependency understanding, Long-range sequential reasoning, Cross-language understanding  

## State of the Field

**Space of definitions.** Most commonly, papers treat code understanding as a latent model ability centered on interpreting code syntax, semantics, logic, structure, functionality, and behavior, sometimes summarized as knowledge of the syntax and semantics of code. Nearby labels such as code comprehension, program comprehension, and program semantics understanding are used for largely the same ability, often with added emphasis on predicting execution outcomes, capturing implicit logic and data types, or going beyond static text patterns to execution effects and dynamic states. A smaller line of work narrows the idea to specific settings, including Verilog, cross-file and cross-file dependency handling, cross-language mapping, neural architecture search code, and long-range sequential reasoning, so the main variation is between broad general understanding and context-specific forms.

**Space of facets.** Across papers, the construct is organized more by scope and task family than by a single shared taxonomy. Code understanding, code comprehension, program comprehension, and program semantics understanding are often treated as overlapping names, while narrower variants carve out repository-level cross-file understanding, cross-language understanding, Verilog understanding, and code-level understanding tied to executable neural architecture search code. Papers also describe the construct through task families such as code summarization, bug detection, clone detection, code retrieval, and code question answering, and one paper presents long-range sequential reasoning as part of semantic understanding of programs.

**Space of measurement.** Papers link the construct to one measurement instrument and three behavioral indicators. The only explicit instrument link is LeetCode, used in a fill-in-the-blank setup described as evaluating code comprehension; beyond that benchmark link, papers operationalize the construct through code-to-text explanation, execution-based prediction of outcomes, code question answering, and repository-level cross-file implementation. These operationalizations mostly match the dominant semantic framing, because they test explanation, behavior prediction, or context integration rather than syntax alone.

**Links.** The recorded links are sparse and mostly single-paper claims. One paper claims a causal relationship from code understanding to code explanation, describing code understanding as something that can be composed with language generation to enable code-to-text output, and another claims a causal relationship from code understanding to abstract reasoning in program verification. Separate papers report that code navigation is related to code understanding, that code understanding is related to long-context understanding in tasks requiring reasoning across multiple files, and that clone detection is related to code understanding.

## Sources

**Code understanding** (8 papers: [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [Lemur: Integrating Large Language Models in Automated Program Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c86142265c5e2c900613dd1d031cb90-Paper-Conference.pdf), [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [CoRAC: Integrating Selective API Document Retrieval with Question Semantic Intent for Code Question Answering](https://aclanthology.org/2025.naacl-long.628.pdf), [Surge: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors](https://aclanthology.org/2025.emnlp-main.162.pdf))
> The latent ability to interpret the syntax, semantics, and functionality of programming code, enabling explanation and reasoning about code behavior.

**Code comprehension** (2 papers: [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf))
> The model's underlying ability to understand the semantics and predict the outcome of a given piece of code.

**Verilog understanding** (1 paper: [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf))
> The latent ability of a model to comprehend Verilog code and summarize its high-level functionality in natural language.

**Cross-file understanding** (1 paper: [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://aclanthology.org/2025.emnlp-main.314.pdf))
> The ability to track and integrate information distributed across multiple files in a code repository when implementing a target function.

**Program semantics understanding** (1 paper: [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf))
> The latent ability of a model to grasp the meaning, behavior, and execution effects of code beyond static text patterns.

**Program comprehension** (1 paper: [LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf))
> The latent ability of a model to understand the semantic properties, structures, and relationships within source code.

**Code-level understanding** (1 paper: [RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ji25a/ji25a.pdf))
> The latent ability of the LLM to comprehend and reason about neural architecture search tasks through executable code representations of network construction and zero-cost proxy computation.

**Cross-file dependency understanding** (1 paper: [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf))
> The latent ability to comprehend and correctly manage dependencies, references, and interactions between multiple code files within a single project.

**Long-range sequential reasoning** (1 paper: [Can Large Language Models Understand Symbolic Graphics Programs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf))
> The capacity to process and understand the procedural steps in a program where the order of operations significantly affects the final semantic meaning.

**Cross-language understanding** (1 paper: [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.362.pdf))
> The model's ability to comprehend and map semantic and structural equivalences between different programming languages.

## Relationships

### Code understanding →
- **Code explanation** (behavioral indicator): *causes*, 1 paper
  > can we compose an augmenting model’s code understanding capability with an anchor LLM’s language generation capability to enable code-to-text generation capability? (Section 1)
  - [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)
- **Abstract reasoning** (construct): *causes*, 1 paper
  > This decomposition requires high-level reasoning that is difficult to automate using conventional formal methods, but plausibly could be performed by LLMs, with their documented code-understanding capability. (Section 2)
  - [Lemur: Integrating Large Language Models in Automated Program Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c86142265c5e2c900613dd1d031cb90-Paper-Conference.pdf)
- **LeetCode** (measurement instrument): *measured_by*, 1 paper
  > "Fill in the Blank evaluates a model’s code comprehension ability... We collected approximately 2,000 coding problems from LeetCode"
  - [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf)

### Associated with
- **Code navigation** (behavioral indicator), 1 paper
  > One important challenge in code understanding is code navigation: finding where relevant functionality is implemented. (Section 2.4)
  - [Position: Future Research and Challenges Remain Towards AI for Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gu25e/gu25e.pdf)
- **Long-context understanding** (construct), 1 paper
  > We evaluate our DSLA model on tasks requiring careful long-range interactions (Bai et al., 2024), including: ... (ii) Code Understanding, which require reasoning across multiple code files to answer complex questions
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **Clone detection** (behavioral indicator), 1 paper
  > This paper explores State Space Models (SSMs) as a promising alternative for code understanding tasks such as retrieval, classification, and clone detection. (Abstract)
  - [CodeSSM: Towards State Space Models for Code Understanding](https://aclanthology.org/2025.emnlp-main.1735.pdf)
