# Syntactic correctness
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Syntax correctness  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage describes syntactic correctness as a model's ability or capability to generate code or queries that follow the grammar and structure of a target language and are free of syntax errors. Most definitions apply this broad conformance framing across HTML, CSS, JavaScript, SQL, and Verilog, while some papers express it through outcome criteria such as avoiding linter-detected errors or producing code that can be successfully compiled. As WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation puts it, models can still "struggle with maintaining logical structure and syntactic correctness," which matches the recurring focus on rule-following outputs.

**Space of facets.** The papers mainly use two names, "syntactic correctness" and "syntax correctness," for the same general idea. Rather than dividing it into many subtypes, they position it alongside other output properties, especially semantic accuracy or meaningfulness, logical coherence or structure, and functional accuracy. In this usage, syntax is treated as one dimension of generated code or query quality that is distinct from whether the output is semantically accurate or functionally correct.

**Space of measurement.** No measurement instrument is linked to it, and it is linked to 1 behavioral indicator, Text-to-SQL. Papers operationalize it directly through task-specific checks: absence of syntax errors, proper SQL clause arrangement and operator usage, avoidance of linter-detected errors, and compile-based success rates. In DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model, syntax correctness is measured by "the proportion of code samples that successfully compile," and these checks are stated in the same terms as the definitions, namely conformance to the target language's rules.

**Links.** The recorded links are limited. One paper reports that Cross-programming-language generalization is related to Syntactic correctness, citing syntactic correctness rates in programming languages beyond Python as evidence of cross-language generalizability; this is the 1 linked construct. Another paper treats Syntactic correctness as related to Text-to-SQL, stating that generated queries should maintain both semantic accuracy and syntactic correctness.

## Sources

**Syntactic correctness** (3 papers: [WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation](https://aclanthology.org/2025.emnlp-main.1276.pdf), [Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf), [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf))
> The ability to generate code that is free of syntax errors and adheres to the rules of the target programming languages like HTML, CSS, and JavaScript.

**Syntax correctness** (1 paper: [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf))
> The model's capability to generate Verilog code that adheres to the language's grammatical and structural rules, allowing it to be successfully compiled.

## Relationships

### Associated with
- **Cross-programming-language generalization** (construct), 1 paper
  > Interestingly, even though phi-1 and phi-1.5 have not trained on PLs other than Python, they can still achieve an average of 49.1% and 72.0% syntactically correctness rate in other PLs, respectively, compared with 97.0% and 98.7% achieved on Python. It indicates the cross-language generalizability of LLMs. (Section 4.2.1)
  - [CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution](https://aclanthology.org/2025.acl-long.1158.pdf)
- **Text-to-SQL** (behavioral indicator), 1 paper
  > This ensures that the generated queries maintain both semantic accuracy (correctly capturing user intentions) and syntactic correctness (following proper SQL structure). (Section 1. Introduction)
  - [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf)
