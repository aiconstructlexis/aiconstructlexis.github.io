# Code summarization
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Linguistic description generation, Code documentation, Docstring completion, Code commenting  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats code summarization as generating a concise natural language description or specification of a given program, function, code block, or snippet, centered on the code's functionality, intent, or behavior. Some authors broaden the output to documentation, docstrings, or comments that explain what the code does and how it works, and one definition explicitly includes side effects and special cases. A smaller framing also allows symbolic summaries, such as function names, and one study phrases the task as writing a short sentence about the function of an incomplete code snippet. Related work on hallucination in this task defines hallucination as summaries that do not accurately capture the input code's intent and implementation details.

**Variants.** Most commonly among the alternative labels, papers refer to code documentation; other papers use docstring completion, code commenting, linguistic description generation, and PL-to-NL generation. The settings span existing source code, code blocks, functions, incomplete code snippets, and IR functions. A smaller variant uses symbolic summaries such as function names rather than only natural language descriptions.

**Space of elicitation and scores.** The only linked measurement instrument is CodeXGLUE, which papers describe as a benchmark used for code summarization. The recorded measurement link comes from work that uses CodeXGLUE for this task, with the original summarization data downsampled.

**What it is taken as evidence of.** Papers link code summarization to one construct, Semantic understanding, and they do so through a related link. In that usage, generating concise summaries of IR functions is described as a proxy for whether a model can capture functional intent, behavior, and output, revealing its capacity to reason about function-level semantics. No other construct link is stated across the papers.

## Sources

**Linguistic description generation** (1 paper: [Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25o/zheng25o.pdf))
> The observable action of generating a natural language summary of a given piece of code that describes its functionality.

**Code documentation** (2 papers: [Position: Future Research and Challenges Remain Towards AI for Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gu25e/gu25e.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf))
> Writing documentation that explains what code does and how it works, including side effects and special cases.

**Code summarization** (5 papers: [SPE Attention: Making Attention Equivariant to Semantic-Preserving Permutation for Code Processing](https://aclanthology.org/2025.emnlp-main.332.pdf), [ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](https://aclanthology.org/2025.acl-long.1480.pdf), [GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding](https://aclanthology.org/2025.acl-long.676.pdf), [LEANCODE: Understanding Models Better for Code Simplification of Pre-trained Large Language Models](https://aclanthology.org/2025.acl-long.78.pdf), [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf))
> The observable behavior of producing natural language or symbolic summaries (such as function names) that capture the intent or behavior of a code block.

**Docstring completion** (1 paper: [Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/916ee60e315531d6b3954af8a8dc3437-Paper-Conference.pdf))
> A code-related task that involves generating a documentation string (docstring) for a given function or code block.

**Code commenting** (1 paper: [CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.7.pdf))
> The task of generating explanatory comments or documentation for existing source code.

## Relationships

### Code summarization →
- **CodeXGLUE** (measurement instrument): *measured_by*, 1 paper
  > for the other four tasks, we use the CodeXGLUE (Lu et al., 2021) benchmark. Among these tasks’ data, we downsampled the original data of code summarization and clone detection due to computation constraints... (Section 4.1.2)
  - [GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding](https://aclanthology.org/2025.acl-long.676.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > in the context of code summarisation, hallucination can be defined as a condition in which the generated summary does not accurately capture the intent and implementation details of the given input code. (Section 1)
  - [ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](https://aclanthology.org/2025.acl-long.1480.pdf)
- **Semantic understanding** (construct), 1 paper
  > This task complements Task 2 by shifting the focus toward semantic understanding. In this setting, LLMs are required to generate concise natural language summaries of IR functions. ... Summarization serves as a proxy to evaluate whether the model can accurately capture functional intent, behavior, and output—ultimately revealing its capacity to reason about function-level semantics. (Section 3.1)
  - [Can Large Language Models Understand Intermediate Representations in Compilers?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25p/jiang25p.pdf)
