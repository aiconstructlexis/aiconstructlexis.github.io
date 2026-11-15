# ProofNet
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** ProofNet-test  

## State of the Field

**What it is.** Across papers, the prevailing description is of a Lean benchmark for undergraduate or college-level mathematics, usually used for theorem proving or autoformalization. Definitions describe 371 exercises or informal-statement and formalization pairs from standard textbooks, with problems spanning areas such as real analysis, complex analysis, linear algebra, abstract algebra, and topology; some descriptions emphasize isolated or less context-dependent problems, and one paper instead treats it as a source dataset of high-quality mathematical proofs. Papers also refer to variants: ProofNet-test for formal statements of college-level questions, and ProofNet#, a corrected version kept close to the original while updating reference formalizations; descriptions variously specify Lean 3, Lean 4, or Lean-formatted problems.

**What it is claimed to measure.** Papers use ProofNet to measure 3 behavioral indicators and 2 constructs. Among behavioral indicators, the most common uses are autoformalization, formal theorem proving, and theorem proving, with papers describing evaluation by comparing predictions with ground truths, assessing theorem-proving capabilities, or reporting whole-proof generation performance on ProofNet-test. Among constructs, it is reported as measuring mathematical reasoning, and one paper also uses it to assess out-of-distribution generalization to out-of-domain theorems.

**Space of uses.** In use, papers usually position ProofNet as a standard comparison benchmark, frequently alongside miniF2F, and sometimes alongside PutnamBench, LeanEuclid, or FIMO. One paper directly relates it to PutnamBench, noting that both draw from the undergraduate curriculum but that ProofNet problems are generally from standard textbooks rather than mathematical competitions. A smaller line of work uses it as source material, either by collecting paired natural-language and Lean statements from it or by drawing on it as a high-quality proof dataset for training.

**Concerns raised.** One paper raises benchmark-reliability concerns by introducing ProofNet#, a meticulously corrected version of ProofNet, with 371 undergraduate-level problems whose reference formalizations were manually verified and fixed for formalization errors. The same paper says the corrected benchmark remains very close to ProofNet because only the reference formalizations are updated.

## Sources

**ProofNet** (7 papers: [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf), [One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ax/li25ax.pdf), [NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1586.pdf), [Reliable Evaluation and Benchmarks for Statement Autoformalization](https://aclanthology.org/2025.emnlp-main.907.pdf), [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf), [Lean Workbook: A large-scale Lean problem set formalized from natural language math problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/bf236666a2cc5f3ae05d2e08485efc4c-Paper-Datasets_and_Benchmarks_Track.pdf), [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf))
> ProofNet is a Lean theorem-proving benchmark used as a comparison benchmark for isolated or less context-dependent theorem proving.

**ProofNet-test** (1 paper: [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf))
> Benchmark consisting of formalized college-level mathematics problems used to assess advanced mathematical reasoning in LLMs.

## Relationships

### → ProofNet
- **Theorem proving** (behavioral indicator): *measured_by*, 2 papers
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **Autoformalization** (behavioral indicator): *measured_by*, 2 papers
  > In statement autoformalization, we follow prevalent benchmarks such as ProofNet (Azerbayev et al., 2023) and LeanEuclid (Murphy et al., 2024) to evaluate by comparing model predictions with ground-truths
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **Formal theorem proving** (behavioral indicator): *measured_by*, 2 papers
  > In this section, we evaluate the theorem-proving capabilities of DeepSeek-Prover-V1.5 using two distinct benchmarks: miniF2F (Zheng et al., 2022), which encompasses high-school level exercises and competition problems, and ProofNet (Azerbayev et al., 2023), which pertains to undergraduate-level theorems. (Section 5)
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
  - [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > While contemporary LLMs attain competitive performance on established formal mathematical reasoning benchmarks such as miniF2F ... and ProofNet (formal undergraduate-level mathematics (Azerbayev et al., 2023))... (Section 1)
  - [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > We also report the performance of the model trained only on LeanWorkbook for 24 iterations, excluding miniF2F-valid and proofnet-valid, demonstrating that the model trained with STP also generalizes to out-of-domain theorems. (Section 4.2)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)

### Associated with
- **PutnamBench** (measurement instrument), 1 paper
  > The PROOFNET benchmark (Azerbayev et al., 2023) also sources problems from the undergraduate curriculum, but these problems are generally from standard textbooks as opposed to mathematical competitions.
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
