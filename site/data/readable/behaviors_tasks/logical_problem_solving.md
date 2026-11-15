# Logical problem solving
**Type:** Behavioral indicator  
**Supporting papers:** 15  
**Also known as:** Multi-step deduction, Logical step generation, Deductive question answering, Boolean expression evaluation, Conclusion generation, Non-rulebreaker acceptance, Logical reasoning, Logical inference, Logical deduction  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as solving questions or problems that require logical deduction from stated facts, premises, rules, or propositions. Most formulations score success by whether the model reaches the answer or conclusion that follows, must be true, or has the correct truth value, while some papers require the model to generate a valid proof, a reasoning path, or intermediate logical steps rather than only select or verify an answer. A smaller line of work further frames it as generating a conclusion from premises or accepting a conclusion only when it is logically valid and factually consistent with those premises.

**Variants.** Papers study this behavior under several labels and settings, most commonly as logical reasoning or logical deduction, and also as multi-step deduction, logical inference, and deductive question answering. Common variants use provided facts to derive a hypothesis or connect facts to a conclusion through intermediate steps; other variants use passages, ontology-derived logical problems, or formal rule application such as implication elimination. Less commonly, papers instantiate it as computing boolean truth values, SAT-style deduction via unit propagation, identifying valid argument structures such as formal fallacies, or contrasting generated conclusions with acceptance of valid non-rulebreaking conclusions.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, PrOntoQA, which papers describe as a dataset of logical reasoning problems derived from ontologies. It is the only linked dataset used to evaluate this kind of logical problem solving.

**What it is taken as evidence of.** No construct is linked to this behavior, so papers do not make an explicit claim about which construct it indicates.

## Sources

**Logical problem solving** (2 papers: [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf), [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf))
> The observable task of answering a question or solving a problem that requires logical deduction.

**Multi-step deduction** (1 paper: [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf))
> The observable task of generating a sequence of logical steps to derive a given hypothesis from a set of provided facts.

**Logical step generation** (1 paper: [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf))
> The observable task of producing intermediate reasoning steps that connect facts to a conclusion.

**Deductive question answering** (1 paper: [Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf))
> Answering a question based on a provided passage of text, requiring logical deduction from the given facts.

**Boolean expression evaluation** (1 paper: [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf))
> The task of computing the truth value of a given logical boolean expression.

**Conclusion generation** (1 paper: [RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25a/chan25a.pdf))
> Producing a conclusion from given premises rather than only deciding whether a proposed conclusion should be accepted.

**Non-rulebreaker acceptance** (1 paper: [RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25a/chan25a.pdf))
> The observable behavior of accepting a conclusion that is both logically valid and factually consistent with the premises.

**Logical reasoning** (4 papers: [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf))
> The observable behavior of solving tasks requiring deduction, inference, or identification of valid argument structures, such as in formal fallacies or logical deduction tasks.

**Logical inference** (1 paper: [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf))
> The observable task of determining whether a given conclusion is correct or must be true based on a provided context and set of rules.

**Logical deduction** (2 papers: [Can Transformers Reason Logically? A Study in SAT Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25d/pan25d.pdf), [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf))
> Producing valid conclusions from a set of premises using formal logic, often involving rule application and inference chains.

## Relationships

### Logical problem solving →
- **PrOntoQA** (measurement instrument): *measured_by*, 1 paper
  > ProntoQA (Saparov & He, 2022) is a dataset consists of 9000 logical reasoning problems derived from ontologies - formal representations of relationships between concepts. (Section 4.1.1)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)
