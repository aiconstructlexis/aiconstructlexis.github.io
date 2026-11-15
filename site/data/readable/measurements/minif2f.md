# miniF2F
**Type:** Measurement instrument  
**Supporting papers:** 28  
**Also known as:** minif2f, MiniF2F, miniF2F-test  

## State of the Field

**What it is.** Across papers, miniF2F is most commonly described as a benchmark or dataset for formal theorem proving, often for neural theorem proving, used to evaluate whether models can generate proofs verifiable by a theorem prover. Definitions usually portray it as formal mathematical problems or statements drawn from competition mathematics, often high-school or Olympiad-level; several descriptions give 488 items split into 244 validation and 244 test problems, and some say it spans multiple formal systems or four formal languages. Papers also mention a miniF2F-test variant for Lean-based evaluation, while a smaller line of work describes it as standalone competition problems that do not require external context, and one description extends it to Olympiad and undergraduate-style coursework.

**What it is claimed to measure.** Across surveyed uses, papers use miniF2F to measure 4 constructs and 3 behavioral indicators. The most frequently linked behavioral indicators are Formal theorem proving, Theorem proving, and Autoformalization, and the most frequently linked constructs are Mathematical reasoning, Generalization, Autoformalization ability, and Formal reasoning. The measurement claims are spread across several related targets rather than centered on one: papers report using miniF2F to evaluate theorem-proving capabilities, whole-proof generation and formal proof writing, Lean4 reasoning capabilities, autoformalization and mathematical reasoning, and generalization to out-of-domain theorems.

**Space of uses.** Papers usually position miniF2F as a standard, popular, or widely recognized benchmark for model comparison, often as a main evaluation set. They frequently use it alongside ProofNet, and more occasionally alongside PISA, PutnamBench, LeanDojo, or CoqGym; among explicitly linked instruments, it is related to 1 other instrument, PutnamBench, through a comparison that contrasts PutnamBench's wider undergraduate coverage with miniF2F's reliance on high-school mathematics. Several studies also fix a proof-assistant setting, mentioning Lean 4, the Lean interactive theorem prover, or the Isabelle part of miniF2F.

**Concerns raised.** The concerns that appear in papers are about scope and difficulty. One line of work describes miniF2F as standalone competition problems that do not require external context, and another says its statements primarily consist of basic arithmetic operations and elementary mathematical objects, using that contrast to present newer benchmarks as more challenging. A related comparison with PutnamBench similarly frames miniF2F as generally relying on high-school mathematics while PutnamBench covers a wider variety of undergraduate problems.

## Sources

**miniF2F** (9 papers: [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf), [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf), [MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e118ba9ee76c20df728b42a35fb4704-Paper-Conference.pdf), [Magnushammer: A Transformer-Based Approach to Premise Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5f5f22e3e09f4424592ffb06840ab0-Paper-Conference.pdf), [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf), [QDTSynth: Quality-Driven Formal Theorem Synthesis for Enhancing Proving Performance of LLMs](https://aclanthology.org/2025.acl-long.714.pdf), [ProofAug: Efficient Neural Theorem Proving via Fine-grained Proof Structure Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bp/liu25bp.pdf), [Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions](https://aclanthology.org/2025.emnlp-main.90.pdf), [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf))
> Benchmark for formal theorem proving that evaluates models on their ability to generate proofs verifiable by a theorem prover.

**minif2f** (1 paper: [Learning Formal Mathematics From Intrinsic Motivation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf))
> A benchmark for formal theorem proving, containing problems from olympiad-level mathematics translated into multiple formal systems.

**MiniF2F** (1 paper: [ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf))
> A benchmark dataset of formal theorem proving problems derived from high-school mathematics competitions, used to evaluate neural theorem proving performance.

**miniF2F-test** (2 papers: [Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf), [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf))
> A benchmark dataset (mini Formal-to-Formal) used for evaluating language model-based theorem provers in the Lean interactive theorem prover.

## Relationships

### → miniF2F
- **Theorem proving** (behavioral indicator): *measured_by*, 3 papers
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 2 papers
  > “The miniF2F dataset is specifically curated for evaluating LLM abilities in autoformalization and mathematical reasoning.”
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
  - [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf)
- **Formal theorem proving** (behavioral indicator): *measured_by*, 2 papers
  > In this section, we evaluate the theorem-proving capabilities of DeepSeek-Prover-V1.5 using two distinct benchmarks: miniF2F (Zheng et al., 2022), which encompasses high-school level exercises and competition problems, and ProofNet (Azerbayev et al., 2023), which pertains to undergraduate-level theorems. (Section 5)
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)
- **Autoformalization** (behavioral indicator): *measured_by*, 2 papers
  > Herald translator achieves a 96.7% accuracy (Pass@128) on formalizing statements in the miniF2F-test and a 23.5% accuracy on our internal graduate-level textbook dataset... (ABSTRACT)
  - [Herald: A Natural Language Annotated Lean 4 Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c2bb821410066459be64d03a4dc5719-Paper-Conference.pdf)
  - [Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions](https://aclanthology.org/2025.emnlp-main.90.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > The FORMALALIGN model exhibits consistent performance across four diverse datasets, demonstrating its ability to generalize its autoformalization evaluation capabilities. Particularly noteworthy are the model's AS scores of 66.39% and 64.61% on the challenging MiniF2F-Valid and MiniF2F-Test datasets, respectively.
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **Autoformalization ability** (construct): *measured_by*, 1 paper
  > “Our extensive experiments on the MATH and miniF2F datasets demonstrate that our approach significantly enhances autoformalization accuracy”
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Formal reasoning** (construct): *measured_by*, 1 paper
  > In this paper, we assess MA-LoT’s Lean4 reasoning capabilities on the MiniF2F-Test and Valid1 datasets (Zheng et al., 2021; Yang et al., 2024b; Wang et al., 2024). (Section 3.1.1)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)

### Associated with
- **PutnamBench** (measurement instrument), 1 paper
  > Compared to MINIF2F (Zheng et al., 2021) and FIMO (Liu et al., 2023), which generally rely on high-school mathematics, PUTNAMBENCH incorporates a wider variety of problems which require definitions of the standard undergraduate mathematics curriculum.
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
