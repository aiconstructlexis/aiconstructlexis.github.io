# BIG-Bench Logical Deduction
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** Logical deduction, Logical Deduction  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats BIG-Bench Logical Deduction as a BigBench task or benchmark for deduction. Definitions describe it as testing deductive reasoning from a set of premises, evaluating logical reasoning capabilities, and, in one description, as a symbolic reasoning benchmark for deduction over structured premises. Papers also refer to it simply as Logical Deduction or as Deduction from the BigBench collaborative benchmark.

**What it is claimed to measure.** Papers use it to measure logical reasoning and symbolic reasoning, and the linked construct set contains two constructs; no behavioral indicator is linked to it. One framing places it among logical reasoning tasks, while another uses it within a symbolic reasoning evaluation, so the measurement claims span both of those constructs rather than a single reported target.

**Space of uses.** Papers include it within broader reasoning suites. One logical reasoning evaluation pairs it with AR-LSAT, ZebraLogic, FOLIO, and other reasoning tasks, while another symbolic reasoning setup pairs it with Date Understanding and other BigBench datasets. Papers also relate it to one other measurement instrument, BIG-Bench Hard, by describing BBH as a collection that includes tasks such as logical deduction.

## Sources

**Logical deduction** (2 papers: [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf), [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf))
> A task from the BigBench benchmark that tests the ability to perform deductive reasoning from a set of premises.

**Logical Deduction** (1 paper: [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf))
> A benchmark for evaluating logical reasoning capabilities.

## Relationships

### → BIG-Bench Logical Deduction
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > We evaluate CLOVER on seven logical reasoning tasks: AR-LSAT (Zhong et al., 2022), ZebraLogic (Lin et al., 2025), Logic grid puzzle (Puzzle), Symbol interpretation (Symbol), and Logical deduction (Deduction) from the BigBench collaborative benchmark (Srivastava et al., 2022), FOLIO (Han et al., 2022), and ProofWriter (Tafjord et al., 2021). (Section 4.1)
  - [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf)
- **Symbolic reasoning** (construct): *measured_by*, 1 paper
  > Symbolic Reasoning. We select four datasets from BigBench (Srivastava et al., 2022) for testing, including Date Understanding, Penguin, Colored Objects and Logical Deduction. (Section 4.1)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)

### Associated with
- **BIG-Bench Hard** (measurement instrument), 2 papers
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
