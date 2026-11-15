# Formal theorem proving
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is producing a correct formal proof for a theorem in an interactive theorem prover such as Lean. One recurring task formulation asks models to prove a theorem with access to code from the theorem's repository, and the stated success criterion is a correct formal proof.

**Variants.** Papers study this behavior across several theorem settings and labels. miniF2F is described as covering high-school level exercises and competition problems, ProofNet as undergraduate-level theorems, and another description groups miniF2F and ProofNet among popular benchmarks focused on isolated competition problems; papers also refer to the behavior as theorem-proving capabilities, formal proof writing, and automated theorem proving with formal languages. A smaller line of work also relates formal theorem proving to premise selection and conjecture generation.

**Space of elicitation and scores.** Papers link formal theorem proving to four instruments overall. The most commonly linked are ProofNet and miniF2F, both described as benchmarks, with PutnamBench also used to evaluate theorem-provers; LeanDojo appears as a related tool for extracting training data from Lean 3 and 4 rather than as a direct measured-by link. Across the direct measurement links, papers operationalize the behavior through benchmark performance on high-school exercises, competition problems, undergraduate-level theorems, and evaluation with PutnamBench.

**What it is taken as evidence of.** Construct links are mixed rather than unified. The most frequent construct connection is to mathematical reasoning: papers claim a causal relationship from formal theorem proving to mathematical reasoning, describing Lean as effective in improving mathematical reasoning and formal theorem proving as one mathematical reasoning task. A smaller line of work treats formal theorem proving as related to reasoning more broadly, while another paper claims a causal relationship from generalization to formal theorem proving, so papers do not settle on a single construct link.

## Sources

**Formal theorem proving** (1 paper: [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf))
> Producing a correct formal proof for a theorem in an interactive theorem prover such as Lean.

## Relationships

### Formal theorem proving →
- **miniF2F** (measurement instrument): *measured_by*, 2 papers
  > In this section, we evaluate the theorem-proving capabilities of DeepSeek-Prover-V1.5 using two distinct benchmarks: miniF2F (Zheng et al., 2022), which encompasses high-school level exercises and competition problems, and ProofNet (Azerbayev et al., 2023), which pertains to undergraduate-level theorems. (Section 5)
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)
- **ProofNet** (measurement instrument): *measured_by*, 2 papers
  > In this section, we evaluate the theorem-proving capabilities of DeepSeek-Prover-V1.5 using two distinct benchmarks: miniF2F (Zheng et al., 2022), which encompasses high-school level exercises and competition problems, and ProofNet (Azerbayev et al., 2023), which pertains to undergraduate-level theorems. (Section 5)
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
  - [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *causes*, 2 papers
  > Lean provides a verifiable environment to explore theorem proving formally, which has been shown effective in improving mathematical reasoning (Xin et al., 2024; Ying et al., 2024b). As far as we know, we are the first public study to introduce formal mathematics data in pre-training, using a total amount of 0.2B lean-based synthesized data. (Section 4.1)
  - [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **PutnamBench** (measurement instrument): *measured_by*, 1 paper
  > We use PUTNAMBENCH to evaluate several established neural and symbolic theorem-provers.
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)

### → Formal theorem proving
- **Generalization** (construct): *causes*, 1 paper
  > “This emphasizes LeanAgent’s continuous generalizability and improvement, explaining its superior theorem-proving performance.”
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)

### Associated with
- **Premise selection** (behavioral indicator), 1 paper
  > A critical challenge in theorem proving is the effective selection of relevant premises (Irving et al., 2016; Tworkowski et al.). (Section: 2 PRELIMINARIES)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > Automated theorem proving with formal languages by LLMs stands at the forefront of reasoning research (Yang et al., 2024a), partly because it allows objective and reliable evaluation... Moreover, it arguably encapsulates the essence of advanced reasoning tasks while abstracting away the ambiguity of natural language, enabling meaningful studies on a relatively smaller scale. (Section 1)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **LeanDojo** (measurement instrument), 1 paper
  > "Theorem proving data extraction. Several tools extract training data from interactive theorem provers, including ... LeanDojo (Yang et al., 2023) for Lean 3 and 4."
  - [miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)
- **Conjecture generation** (behavioral indicator), 1 paper
  > “The conjecturer is trained iteratively on previously generated conjectures that are barely provable by the current prover, which incentivizes it to generate increasingly challenging conjectures over time.”
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
