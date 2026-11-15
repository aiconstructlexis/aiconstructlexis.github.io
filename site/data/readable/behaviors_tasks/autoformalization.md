# Autoformalization
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Formalization, Statement formalization, Natural language to formal language translation, Formal problem modeling, Statement autoformalization, Auto-formalization, Autoformalisation  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is translation from informal mathematical language into a formal representation, most often a machine-verifiable statement in a proof assistant or symbolic language. Most definitions focus on mathematical statements, though some broaden the task to math problems, solutions, or proofs; the target language is variously Lean or Lean4, Isabelle/HOL, SMT-LIB, first-order logic, or symbolic logic. Success is usually described as producing formal statements that are verifiable or provable, with some papers additionally requiring syntactic correctness, preservation of semantic meaning and mathematical constraints, internal consistency, or keeping only well-typed predictions.

**Variants.** Most work studies statement-level autoformalization, including informal statements written in natural language or natural language plus LaTeX, and one paper specifically highlights translating unconstrained natural language statements. Smaller strands treat it as formal problem modeling with variables and constraints, conversion of question-answering problems and their solutions into Lean4 theorem statements, translation of premises or sentences into first-order or symbolic logic as part of reasoning, or translation of written natural language proofs into formal proofs. Papers also place it alongside related behaviors: informalization is described as the inverse process that translates formal statements back into natural language, theorem proving is treated as a related application area, and one paper claims a causal relationship from information retrieval to autoformalization, saying retrievals are used to enhance it.

**Space of elicitation and scores.** Papers link autoformalization to 2 measurement instruments, ProofNet and miniF2F. The prevailing scoring setup is benchmark-based evaluation: ProofNet is described as a prevalent or human-curated benchmark where model predictions are compared with ground truths, while miniF2F appears as an existing autoformalization dataset or test used for formalizing statements and as a comparison point for other benchmarks.

**What it is taken as evidence of.** Papers link it to 2 constructs, Semantic alignment and Symbolic reasoning. These links are framed as related rather than as direct measurement claims: one paper says autoformalization faces challenges in ensuring semantic alignment between informal and formal languages, and another relates it to enhanced capabilities for symbolic reasoning. Across papers, there is no single construct that they consistently treat autoformalization as evidence of.

## Sources

**Formalization** (2 papers: [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf), [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf))
> The task of translating a natural language math problem into a formal symbolic representation (e.g., SMT-LIB).

**Autoformalization** (5 papers: [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf), [Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions](https://aclanthology.org/2025.emnlp-main.90.pdf), [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf), [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf), [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf))
> The observable task of translating a mathematical statement from a natural language description into a formal language representation, such as Isabelle/HOL.

**Statement formalization** (1 paper: [Reliable Evaluation and Benchmarks for Statement Autoformalization](https://aclanthology.org/2025.emnlp-main.907.pdf))
> The observable task of generating a formal language representation of a mathematical statement given its natural language counterpart.

**Natural language to formal language translation** (1 paper: [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf))
> Converting natural language math problems and their solutions into formal Lean4 theorem statements that preserve semantic meaning and mathematical constraints.

**Formal problem modeling** (1 paper: [VCSearch: Bridging the Gap Between Well-Defined and Ill-Defined Problems in Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.642.pdf))
> The observable behavior of translating a natural language math problem into a formal representation (e.g., SMT-Lib) with variables and constraints.

**Statement autoformalization** (1 paper: [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf))
> Translating an informal mathematical statement into a formal statement in a proof assistant language.

**Auto-formalization** (1 paper: [MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e118ba9ee76c20df728b42a35fb4704-Paper-Conference.pdf))
> The observable task of translating a mathematical proof written in natural language into a formal, machine-verifiable language like Lean.

**Autoformalisation** (2 papers: [Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations](https://aclanthology.org/2025.acl-long.867.pdf), [Theorem Prover as a Judge for Synthetic Data Generation](https://aclanthology.org/2025.acl-long.1448.pdf))
> The observable process of translating natural language sentences into a machine-verifiable formal language, such as symbolic logic.

## Relationships

### Autoformalization →
- **ProofNet** (measurement instrument): *measured_by*, 2 papers
  > In statement autoformalization, we follow prevalent benchmarks such as ProofNet (Azerbayev et al., 2023) and LeanEuclid (Murphy et al., 2024) to evaluate by comparing model predictions with ground-truths
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **miniF2F** (measurement instrument): *measured_by*, 2 papers
  > Herald translator achieves a 96.7% accuracy (Pass@128) on formalizing statements in the miniF2F-test and a 23.5% accuracy on our internal graduate-level textbook dataset... (ABSTRACT)
  - [Herald: A Natural Language Annotated Lean 4 Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c2bb821410066459be64d03a4dc5719-Paper-Conference.pdf)
  - [Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions](https://aclanthology.org/2025.emnlp-main.90.pdf)

### → Autoformalization
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > RAutoformalizer uses the retrievals to enhance autoformalization.
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)

### Associated with
- **Informalization** (behavioral indicator), 2 papers
  > several studies [19–21] explore the performance of LLMs for the inverse process of formalization, i.e., informalization, which translates formal statements back into natural language. (Section 2)
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **Semantic alignment** (construct), 1 paper
  > While promising, autoformalization faces challenges in ensuring semantic alignment between these languages. (Section 1)
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
- **Symbolic reasoning** (construct), 1 paper
  > To address this, we propose using auto-formalization agents equipped with enhanced capabilities for symbolic reasoning.
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Theorem proving** (behavioral indicator), 1 paper
  > As the bridge between informal and formal mathematics, autoformalization has three immediate applications: (1) data augmentation for neural theorem provers (Wu et al., 2022; Xin et al., 2024; Wang et al., 2025; Ren et al., 2025), (2) guiding theorem proving via informal proofs (Jiang et al., 2023), and (3) validating informal reasoning (Zhou et al., 2024a; Olausson et al., 2023). (Section 3)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
