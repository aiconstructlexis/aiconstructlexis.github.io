# MathVerse
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** MATHVERSE  

## State of the Field

**What it is.** Across papers, MathVerse is most commonly treated as a multimodal or visual math benchmark for evaluating mathematical reasoning with visual inputs, especially diagram understanding. Definitions variously emphasize geometry-related mathematical reasoning, broader multimodal mathematical problem solving, and whether models can interpret or "truly see" diagrams in visual math problems, and one description specifies 2,612 visual math problems. Papers also describe different formats within the benchmark, including multiple-choice questions and a Vision-Only mode where questions are presented in images, alongside text-dominant and vision-integrated presentations.

**What it is claimed to measure.** Papers use MathVerse to measure two constructs and one behavioral indicator. The prevailing measured construct is Mathematical reasoning, while smaller uses treat it as measuring Generalization and as supporting Chain of thought evaluation, with one paper reporting scores on "CoT evaluation and accuracy" on MathVerse. Overall, papers link it to a fairly concentrated set of targets rather than a broad spread of constructs.

**Space of uses.** Papers often place MathVerse inside broader multimodal evaluation suites alongside MathVista, DynaMath, MathVision, MMStar, and MMMU, as well as other reasoning benchmarks. It is also used as an added check in some studies: one paper says it evaluates on the "newly introduced MathVerse benchmark" to verify generalization ability, while another uses performance on MathVerse to confirm visual reasoning capability.

**Concerns raised.** A smaller line of work raises benchmark overlap as a concern, reporting that MathVerse and MathVision show "high redundancy" and a strong correlation with other benchmarks. Some papers also position it as part of the earlier static visual math benchmark line when contrasting it with DynaMath.

## Sources

**MathVerse** (6 papers: [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf), [Redundancy Principles for MLLMs Benchmarks](https://aclanthology.org/2025.acl-long.612.pdf), [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf), [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf))
> A multimodal benchmark used to assess generalization on geometry-related mathematical reasoning, including multiple-choice evaluation.

**MATHVERSE** (1 paper: [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf))
> A visual math benchmark referenced for comparison with DYNAMATH and as an example of prior static benchmarks.

## Relationships

### → MathVerse
- **Mathematical reasoning** (construct): *measured_by*, 2 papers
  > Benchmarks such as MATH-V (Wang et al., 2024a) and MATHVERSE (Zhang et al., 2024e) demonstrate the current limitations of VLMs in handling challenging mathematical problems and understanding mathematical diagrams. (Section 1)
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To verify the generalization ability of G-LLaVA, we also conduct evaluation on the newly introduced MathVerse benchmark (Zhang et al., 2024b). (Section 5.1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator): *measured_by*, 1 paper
  > As shown in Table 1 for the MathVerse benchmark, MAVIS-7B achieves the best overall scores in both CoT evaluation and accuracy among open-source MLLMs... (Section 4.2)
  - [MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf)
