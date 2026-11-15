# Verbalized confidence
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Verbal Confidence, Verbalization  

## State of the Field

**What it is.** Across the surveyed definitions, the prevailing usage treats verbalized confidence as a direct self-report protocol: the model or LLM judge is prompted to express confidence in its own answer or judgment. Papers variously describe it as a baseline confidence measure, a black-box self-evaluation procedure, or an evaluation protocol. Most descriptions frame the output as a scalar value, while one definition allows a numerical or categorical confidence rating alongside the answer, and one paper refers to a "Verb. 1S top-1" variant.

**What it is claimed to measure.** Papers link it to 2 constructs and 1 behavioral indicator. The dominant claim is that it measures Confidence, with definitions repeatedly describing it as prompting the model to self-report confidence or subjective belief strength. A smaller usage applies Verbalization to measure Hallucination by replacing a hallucination detection module with it, while Instruction following ability is not measured by it but is reported as related to it.

**Space of uses.** No measurement instrument is linked to it. Papers most often position it as a baseline or black-box self-evaluation method that directly asks for confidence through prompts; one description says it uses a prompt for the model to self-report its confidence level, and another reports using average confidence across all samples. In a hallucination setting, one study uses Verbalization alongside Trained Probes and Hybrid Consistency as an existing method substituted into a detection module.

**Concerns raised.** One paper relates it to Instruction following ability and says verbalization-based methods are largely restricted by high computational costs during inference and by the requirement for the model's instruction-following capability.

## Sources

**Verbalized confidence** (2 papers: [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [From Evidence to Belief: A Bayesian Epistemology Approach to Language Models](https://aclanthology.org/2025.naacl-long.531.pdf))
> A baseline confidence measure obtained by directly prompting an LLM judge to express its confidence in its own judgment as a scalar value.

**Verbal Confidence** (1 paper: [Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b1cfc8ede53f452cabf8b9cf4eef76-Paper-Conference.pdf))
> A black-box self-evaluation procedure that asks the model to express confidence in its own answer.

**Verbalization** (1 paper: [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf))
> An evaluation protocol that measures a model's confidence by directly prompting it to self-report its confidence level.

## Relationships

### → Verbalized confidence
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Furthermore, we replace the hallucination detection module in DSSP-RAG with two existing methods: Trained Probes, Verbalization and Hybrid Consistency (Hyb-Cons). (Section 4.3.3)
  - [Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://aclanthology.org/2025.emnlp-main.549.pdf)
- **Confidence** (construct): *measured_by*, 1 paper
  > We first consider two types of existing confidence measure—... (2) verbalized confidence
  - [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf)

### Associated with
- **Instruction following ability** (construct), 1 paper
  > While consistency-based and verbalization-based methods have demonstrated their effectiveness in recent LMs, their utilization is largely restricted due to their high computational costs during inference and the requirement for LM’s instruction-following capability. (Section 2.2)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
