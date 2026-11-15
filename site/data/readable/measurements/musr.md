# MuSR
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** MUSR  

## State of the Field

**What it is.** Across papers, MuSR is most commonly described as a benchmark from the Open LLM Leaderboard for reasoning-oriented evaluation, especially reasoning over social or multi-step scenarios. Some definitions specify Open LLM Leaderboard v2, while others refer to the Open LLM Leaderboard more generally. One paper calls it "the semi-symbolic MUSR" and notes that "All tasks are multiple-choice" (Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?), and papers describing its domains mention murder mysteries, object placement, and team assignment.

**What it is claimed to measure.** Papers link MuSR to 6 constructs, with commonsense reasoning the most frequent linked construct, followed by chain-of-thought reasoning, logical reasoning, physical world understanding, and social reasoning; no behavioral indicators are linked to it. The measurement claims are spread across several reasoning-oriented constructs rather than one: one description ties its domains to commonsense reasoning about physical and social situations, another says it is designed to assess multistep reasoning, and a separate paper places it with formal logic "to a lesser degree."

**Space of uses.** Papers usually position MuSR as one benchmark within broader evaluation suites for model performance. Among linked instruments, papers relate it to Open LLM Leaderboard and Human evaluation, and in evaluation setups they often report it alongside MMLU-Pro, GPQA, and BBH, with other benchmarks included as well.

**Concerns raised.** The clearest concern papers make explicit is whether "the answers derived from F actually match what can be derived from our narratives." One study reports a human evaluation of dataset quality for that check.

## Sources

**MUSR** (3 papers: [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf), [SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf), [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://aclanthology.org/2025.emnlp-main.1516.pdf))
> A benchmark included in Open LLM Leaderboard v2 for evaluating reasoning over social or multi-step scenarios.

**MuSR** (1 paper: [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf))
> A benchmark from the Open LLM Leaderboard used to evaluate reasoning-oriented performance.

## Relationships

### → MuSR
- **Commonsense reasoning** (construct): *measured_by*, 3 papers
  > “The domains we address here, murder mysteries, object placement, and team assignment, involve commonsense reasoning about physical (Bisk et al., 2020) and social situations (Sap et al., 2019), theory-of-mind, and more.”
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
  - [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://aclanthology.org/2025.emnlp-main.1516.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Physical world understanding** (construct): *measured_by*, 1 paper
  > “The domains we address here, murder mysteries, object placement, and team assignment, involve commonsense reasoning about physical (Bisk et al., 2020) and social situations (Sap et al., 2019), theory-of-mind, and more.”
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Social reasoning** (construct): *measured_by*, 1 paper
  > “The domains we address here, murder mysteries, object placement, and team assignment, involve commonsense reasoning about physical (Bisk et al., 2020) and social situations (Sap et al., 2019), theory-of-mind, and more.”
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Theory of mind** (construct): *measured_by*, 1 paper
  > “The domains we address here, murder mysteries, object placement, and team assignment, involve commonsense reasoning about physical (Bisk et al., 2020) and social situations (Sap et al., 2019), theory-of-mind, and more.”
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > “On datasets that require math (MATH, GSM8K) or formal logic (ContextHub, MuSR to a lesser degree)”
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > Given that MUSR is designed to assess multistep reasoning, this suggests that models excelling in structured reasoning tasks also tend to perform well in frame-semantic parsing. (Section 4.7)
  - [Can LLMs Extract Frame-Semantic Arguments?](https://aclanthology.org/2025.emnlp-main.1557.pdf)

### Associated with
- **Open LLM Leaderboard** (measurement instrument), 1 paper
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument), 1 paper
  > To validate that the answers derived from F actually match what can be derived from our narratives, we conducted a human evaluation of dataset quality. (Section 5.1)
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
