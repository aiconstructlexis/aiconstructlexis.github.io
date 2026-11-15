# Cross-programming-language generalization
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Cross-lingual transferability, Cross-language generalization  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this construct as transfer across programming languages: a model or software-engineering system carries knowledge, skills, reasoning, or problem-solving performance from one programming language to another. The definitions mostly agree on that core idea, but vary in emphasis, with some framing it as an ability to apply what was learned in one language to tasks in another, and others framing it as the degree of performance transfer across programming languages and language-specific codebases, especially to other or unseen languages.

**Space of facets.** Papers use several near-equivalent labels for the same general idea, including cross-lingual transferability, cross-language generalization, and cross-language generalizability. The main variation is scope: some descriptions focus narrowly on transfer of learned knowledge or reasoning to other programming languages, while another extends the concept to language-specific codebases, non-Python settings, and more language-agnostic solutions that do not overfit to Python repositories.

**Space of measurement.** It is linked to no measurement instrument and no behavioral indicator. In the papers' own usage, it is nevertheless described through transferred performance across languages, for example whether a model trained mainly or solely on Python achieves Pass@1 in other languages, and whether it retains syntactic correctness when producing code in programming languages other than Python.

**Links.** One paper reports that it is related to syntactic correctness. The evidence is that models not trained on programming languages other than Python still produced syntactically correct code in other languages, though at lower rates than on Python, and the paper treats this as indicating cross-language generalizability.

## Sources

**Cross-lingual transferability** (1 paper: [McEval: Massively Multilingual Code Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dad66bb085bab14fbca07cfa4271f00b-Paper-Conference.pdf))
> The model's ability to apply knowledge and skills learned from one programming language to tasks in another programming language.

**Cross-language generalization** (2 papers: [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution](https://aclanthology.org/2025.acl-long.1158.pdf))
> The degree to which a software-engineering system transfers its problem-solving performance across programming languages and language-specific codebases.

## Relationships

### Associated with
- **Syntactic correctness** (construct), 1 paper
  > Interestingly, even though phi-1 and phi-1.5 have not trained on PLs other than Python, they can still achieve an average of 49.1% and 72.0% syntactically correctness rate in other PLs, respectively, compared with 97.0% and 98.7% achieved on Python. It indicates the cross-language generalizability of LLMs. (Section 4.2.1)
  - [CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution](https://aclanthology.org/2025.acl-long.1158.pdf)
