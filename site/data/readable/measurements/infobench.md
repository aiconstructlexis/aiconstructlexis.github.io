# InfoBench
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the surveyed work, the prevailing description is an instruction-following benchmark for instruction adherence that decomposes complex instructions into simpler sub-instructions for granular evaluation. One paper adds that it contains 500 diverse instructions and 2,250 decomposed questions across multiple constraint categories, and describes a metric called Decomposed Requirements Following Ratio (DRFR) for assessing instruction-adherence capabilities. Some papers instead describe task-specific views of it: a direct scoring dataset with a 1 to 5 Likert scale and English Easy and Hard subsets, an Expert split used for fine-grained classification, and a benchmark for more general instructions that need LLM-based judgment.

**What it is claimed to measure.** Papers use InfoBench to measure one behavioral indicator, Instruction following, and two constructs, Cross-domain generalization and Instruction following ability. The most common claim is that it measures instruction following: papers describe it as assessing instruction-adherence capabilities and as an instruction benchmark that evaluates whether models comprehend and execute detailed directives, including clear, step-by-step guidance. A smaller line of work uses it as cross-domain validation, reporting that Instruction following ability and Cross-domain generalization are measured by InfoBench alongside other evaluations.

**Space of uses.** Papers commonly position InfoBench as one of several instruction-following evaluations, most often alongside IFEval, and some also mention Multi-IF, MT-Bench, and Arena-hard. In these uses, it is described as simulating real-world scenarios that require clear, step-by-step guidance, as a complex instruction-following dataset used for cross-domain validation, and as an evaluation set for more general instructions that need LLM-based judgment. Other papers use task-specific portions of it, including the Expert split for classification and the Easy and Hard subsets for direct scoring of LLM responses.

## Sources

**InfoBench** (5 papers: [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf), [Are Checklists Really Useful for Automatic Evaluation of Generative Tasks?](https://aclanthology.org/2025.emnlp-main.538.pdf), [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [UltraIF: Advancing Instruction Following from the Wild](https://aclanthology.org/2025.emnlp-main.945.pdf))
> A benchmark for instruction adherence that decomposes complex instructions into simpler sub-instructions for granular evaluation.

## Relationships

### → InfoBench
- **Instruction following** (behavioral indicator): *measured_by*, 2 papers
  > InfoBench (Qin et al., 2024) introduces a new metric called Decomposed Requirements Following Ratio (DRFR) for assessing the instruction-adherence capabilities of LLMs.
  - [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **Instruction following ability** (construct): *measured_by*, 1 paper
  > To explore AUTOIF on more natural Instruction-following scenario, we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
