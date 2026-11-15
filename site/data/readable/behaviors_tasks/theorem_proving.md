# Theorem proving
**Type:** Behavioral indicator  
**Supporting papers:** 37  
**Also known as:** Proof generation, Natural language proof generation, Formal proof generation, Tactic generation, Proof tactic generation, Proof trajectory generation, Tactic prediction, Proof-step generation, Whole-proof generation, Theorem proof generation, Constructive proof generation, Formal-to-formal proving, Formal proof synthesis, Proof step generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats theorem proving as producing a proof that establishes a given theorem, usually as a complete, formal, and verifiable sequence of proof steps inside a proof assistant. Papers often describe success as generating the full proof from the theorem statement, or searching for tactics and proof trajectories that complete the formal theorem, with correctness checked by a formal verifier or correctness checker. A smaller line of work narrows the behavior to single-step tactic prediction from a current proof state, while a few papers broaden it to human-readable natural language proofs or constructive proofs that establish a result by constructing an object that satisfies specified constraints. Some authors also phrase theorem proving as an ability to construct valid proof sequences, though the prevailing usage remains the observable proof production task.

**Variants.** Most variants stay in formal settings, especially proof assistants centered on Lean, and papers use labels such as proof generation, formal proof generation, formal-to-formal proving, and formal proof synthesis for producing complete proof terms or scripts. Another common cluster focuses on local actions within interactive proving, under names like tactic generation, proof tactic generation, tactic prediction, proof-step generation, and proof step generation, all centered on predicting the next tactic from the current proof state. Papers also distinguish whole-proof generation, where the entire proof text is produced in one pass and verified at the end, from stepwise or interactive generation. Less common variants include proof trajectory generation, natural language proof generation, theorem proof generation, and constructive proof generation in settings such as Olympiad inequalities and object-construction problems.

**Space of elicitation and scores.** Papers link theorem proving to 5 instruments overall. The measurement links are mainly benchmark-based: theorem proving is measured by PutnamBench and miniF2F most often, followed by ProofNet and LeanDojo, which papers describe as theorem-proving or domain-general evaluation benchmarks; Mathlib is also linked, but only as a related Lean mathematical library that theorem provers are trained on rather than as a measured_by link. Operationally, the scoring described in these papers relies on whether sampled whole proofs or stepwise tactics can be checked by formal verification.

**What it is taken as evidence of.** Papers do not converge on a single construct that theorem proving is taken to evidence. Only 2 constructs are linked at all, Abstraction and Long-horizon planning, and both links are recorded as related rather than as measurement or correlation claims: one paper says that in interactive theorem proving, abstractions can be encapsulated in new definitions, lemmas, and tactics, and another says the whole-proof generation model is trained to perform long-term planning for theorem proving. Outside construct links, one paper reports theorem proving is related to Autoformalization, and one paper claims a causal relationship from Long chain-of-thought generation to theorem proving.

## Sources

**Theorem proving** (4 papers: [Proving Theorems Recursively](https://proceedings.neurips.cc/paper_files/paper/2024/file/9de7a49945898da86e062e7029baa284-Paper-Conference.pdf), [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf), [Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gulati25a/gulati25a.pdf), [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf))
> The observable task of generating a complete and formally verifiable sequence of proof steps that successfully proves a given theorem statement.

**Proof generation** (5 papers: [Lean Workbook: A large-scale Lean problem set formalized from natural language math problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/bf236666a2cc5f3ae05d2e08485efc4c-Paper-Datasets_and_Benchmarks_Track.pdf), [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf), [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf), [Hierarchical Attention Generates Better Proofs](https://aclanthology.org/2025.acl-long.856.pdf), [QDTSynth: Quality-Driven Formal Theorem Synthesis for Enhancing Proving Performance of LLMs](https://aclanthology.org/2025.acl-long.714.pdf))
> The observable task of searching for or generating proof tactics and trajectories to complete a formal theorem.

**Natural language proof generation** (1 paper: [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf))
> The observable behavior of producing a human-readable, text-based proof for a mathematical problem.

**Tactic generation** (1 paper: [Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/06b35bf96174d97bae899d915a8b7210-Paper-Conference.pdf))
> The observable behavior of producing a specific proof step or transformation (a 'tactic') to apply to a mathematical goal.

**Formal proof generation** (3 papers: [Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/06b35bf96174d97bae899d915a8b7210-Paper-Conference.pdf), [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf), [MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e118ba9ee76c20df728b42a35fb4704-Paper-Conference.pdf))
> The behavior of producing a proof in a formal language, such as Lean, that can be automatically verified for correctness by a proof system.

**Proof tactic generation** (1 paper: [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf))
> The observable action of a language model producing a single, one-step proof tactic (a command for a formal prover like Lean) given a current proof state.

**Tactic prediction** (1 paper: [Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf))
> The behavior of generating the next formal proof step, or "tactic," given the current proof state in an interactive theorem prover.

**Proof trajectory generation** (1 paper: [Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf))
> Sampling sequences of proof states, thoughts, and tactics that form candidate theorem-proving attempts.

**Whole-proof generation** (2 papers: [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf), [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf))
> A specific strategy for formal proof generation where the model generates the entire proof code from the theorem statement in a single pass, with verification performed only at the end.

**Proof-step generation** (2 papers: [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf), [ProofAug: Efficient Neural Theorem Proving via Fine-grained Proof Structure Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bp/liu25bp.pdf))
> An interactive strategy for formal proof generation where the model predicts a single subsequent tactic based on an intermediate tactic state, which is then verified before the next step is generated.

**Theorem proof generation** (1 paper: [AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf))
> The task of generating mathematical proofs for given theorems.

**Constructive proof generation** (1 paper: [MathConstruct: Challenging LLM Reasoning with Constructive Proofs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balunovic25a/balunovic25a.pdf))
> The observable task of generating a mathematical object, such as a set, matrix, or graph, that satisfies a set of specified constraints to prove a mathematical result.

**Formal-to-formal proving** (1 paper: [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf))
> The observable task of generating a sequence of code-like proof steps (tactics) within a proof assistant to prove a formal mathematical statement, also known as tactic prediction.

**Formal proof synthesis** (1 paper: [ProofAug: Efficient Neural Theorem Proving via Fine-grained Proof Structure Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bp/liu25bp.pdf))
> The task of generating a complete, verifiable formal proof for a given theorem statement within a specific proof assistant system.

**Proof step generation** (1 paper: [Magnushammer: A Transformer-Based Approach to Premise Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5f5f22e3e09f4424592ffb06840ab0-Paper-Conference.pdf))
> The observable action of producing a single, valid step, such as applying a tactic with selected premises, within a formal proof.

## Relationships

### Theorem proving →
- **PutnamBench** (measurement instrument): *measured_by*, 3 papers
  > “We use PUTNAMBENCH to evaluate several neural and symbolic theorem-provers.”
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **miniF2F** (measurement instrument): *measured_by*, 3 papers
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **ProofNet** (measurement instrument): *measured_by*, 2 papers
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **LeanDojo** (measurement instrument): *measured_by*, 1 paper
  > Recent neural theorem provers are domain-agnostic and evaluated on benchmarks targeting this level [Level 3, proving simple theorems automatically in a domain-general fashion], e.g., CoqGym (Yang & Deng, 2019), LeanDojo (Yang et al., 2023), MiniF2F (Zheng et al., 2022), and PutnamBench (Tsoukalas et al., 2024). (Section 5.2)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)

### → Theorem proving
- **Long chain-of-thought generation** (behavioral indicator): *causes*, 1 paper
  > The emergent Lean reasoning ability in the Long CoT enables the model to write a better-structured proof based on its high-level plan than direct proof generation. (Section 2.3.1)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)

### Associated with
- **Mathlib** (measurement instrument), 1 paper
  > Most neural theorem provers based on Lean are primarily trained on Lean’s mathematical library, Mathlib.
  - [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf)
- **Abstraction** (construct), 1 paper
  > In interactive theorem proving, abstractions can be encapsulated in new definitions, lemmas, and tactics. (Section 4.2)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **Long-horizon planning** (construct), 1 paper
  > "the whole-proof generation model is trained to perform long-term planning for theorem proving"
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Autoformalization** (behavioral indicator), 1 paper
  > As the bridge between informal and formal mathematics, autoformalization has three immediate applications: (1) data augmentation for neural theorem provers (Wu et al., 2022; Xin et al., 2024; Wang et al., 2025; Ren et al., 2025), (2) guiding theorem proving via informal proofs (Jiang et al., 2023), and (3) validating informal reasoning (Zhou et al., 2024a; Olausson et al., 2023). (Section 3)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
