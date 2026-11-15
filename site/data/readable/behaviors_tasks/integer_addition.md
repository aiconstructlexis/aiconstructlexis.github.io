# Integer addition
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Addition, Multi-digit addition, Two-integer addition, Numerical addition  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats integer addition as generating the sum of integer inputs, usually written as digit sequences or arithmetic expressions. It is often formulated over two integers or two multi-digit numbers, though some definitions extend it to two or more operands. Where the success criterion is made explicit, papers describe it as producing the correct sum, and some work further frames the task as a diagnostic centered on per-digit addition and carry propagation.

**Variants.** Papers study several variants of the task. Some distinguish decimal addition by carry conditions, including with or without carry propagation and explicit easy versus hard carry settings, and one line of work also varies forward versus reverse digit order. Other variants include multi-digit, digit-by-digit addition with step-by-step calculations, two-integer addition under symbolic remapping, natural-language prompts, multilingual in-context examples, and settings with varying numbers of digits; the only linked behavioral indicator is carry propagation, treated in one paper as a core component alongside digit-wise addition.

**Space of elicitation and scores.** No measurement instrument is linked to it. When elicitation is described, papers use numerical expressions, digit sequences, or natural-language prompts, and when scoring is stated it is usually whether the model generates the correct sum. A smaller line of work elicits step-by-step digit-place calculations rather than only the final answer.

**What it is taken as evidence of.** Across the recorded links, integer addition appears alongside six constructs, and the links are spread across several framings rather than a single agreed one. The prevailing linkage is that integer addition is related to length generalization, with papers describing little to no length generalization on addition and work that targets extrapolation beyond training length. Separate papers also report that algorithmic reasoning, chain-of-thought reasoning, and compositional generalization are related to integer addition, while integer addition is related to mathematical reasoning and one other construct.

## Sources

**Integer addition** (3 papers: [Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure](https://proceedings.neurips.cc/paper_files/paper/2024/file/27aa3a0e6d63db269977bb2df5607cb8-Paper-Conference.pdf), [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf), [How do autoregressive transformers solve full addition?](https://aclanthology.org/2025.emnlp-main.643.pdf))
> The task of calculating the sum of two or more integer operands, presented as a sequence of digits.

**Addition** (2 papers: [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf), [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf))
> Performing decimal addition of two multi-digit numbers, either in forward or reverse digit order, with or without carry propagation.

**Multi-digit addition** (1 paper: [Can Language Models Learn to Skip Steps?](https://proceedings.neurips.cc/paper_files/paper/2024/file/504fa7e518da9d1b53a233ed20a38b46-Paper-Conference.pdf))
> The arithmetic task of adding two numbers with multiple digits, often performed by generating step-by-step calculations for each digit place.

**Two-integer addition** (1 paper: [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf))
> The observable task of computing the sum of two integers, either in standard numeric form or under symbolic remapping, serving as a diagnostic for algorithmic reasoning.

**Numerical addition** (1 paper: [Everything Everywhere All at Once: LLMs can In-Context Learn Multiple Tasks in Superposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25a/xiong25a.pdf))
> Generating the correct sum of two numbers when presented with arithmetic expressions in numerical form.

## Relationships

### Associated with
- **Length generalization** (construct), 2 papers
  > Standard Transformers trained from scratch on addition and other arithmetic tasks exhibit little to no length generalization (Section 1)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > what architectural design choices, dataset characteristics, and training pipeline variants are required to learn a many-step reasoning process like multi-digit addition? (Section 1)
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Compositional generalization** (construct), 1 paper
  > These findings reveal a core limitation in LLMs’ compositional generalization for elementary arithmetic. (Contributions)
  - [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf)
- **Pattern matching** (construct), 1 paper
  > These findings demonstrate that current LLMs address elementary addition via pattern matching, not robust rule induction... (Abstract)
  - [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf)
- **Carry propagation** (behavioral indicator), 1 paper
  > The task isolates a single algorithm with two components, digit-wise addition and carry propagation... (Our diagnostic lens: two-integer addition.)
  - [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf)
- **Algorithmic reasoning** (construct), 1 paper
  > “To study algorithmic reasoning in a sterile laboratory setting, the academic community focuses on simple arithmetic test problems like addition.”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > “we focus on simple arithmetic test problems like addition”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
