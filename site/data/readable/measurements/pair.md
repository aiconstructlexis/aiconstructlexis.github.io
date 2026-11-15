# PAIR
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats PAIR as Prompt Automatic Iterative Refinement, a black-box jailbreak attack or procedure in which an attacker or red-teaming LLM automatically and iteratively generates or refines prompts until a target model is jailbroken. Several papers phrase this as a multi-turn conversation approach, a query-based attack, or a prompt-level jailbreak that uses prompt optimization, and some describe it more generally as an algorithmic attack method for generating jailbreak prompts. A smaller set of definitions departs from this framing, with one paper describing PAIR as population-based and another using the name for a Likert-style prompt that assesses whether a response "violates ethical, legal, or safety guidelines."

**What it is claimed to measure.** Papers link PAIR to one construct and two behavioral indicators. It is reported as measuring Jailbreaking and Jailbreak resistance, and one line of work also uses it to measure Harmlessness, including benchmark comparisons that report harmfulness scores and attack success rates under PAIR. Overall, the recorded links are narrow, covering those three targets.

**Space of uses.** It is commonly used alongside GCG and AutoDAN, and also with TAP and DeepInception, usually as one of several jailbreak attacks in evaluations of defenses, robustness, or safety vulnerabilities. Papers also position it in out-of-distribution safety evaluation and adaptive-attack testing, and one paper relates it to CSRT by comparing CSRT against PAIR as a non-multilingual red-teaming baseline.

## Sources

**PAIR** (11 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf), [The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25f/pan25f.pdf), [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf), [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf), [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf), [Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf))
> Prompt Automatic Iterative Refinement, a black-box jailbreak procedure in which an attacker LLM iteratively refines prompts until the target model is jailbroken.

## Relationships

### → PAIR
- **Jailbreaking** (behavioral indicator): *measured_by*, 2 papers
  > We also evaluated the effect of the jailbreaking attack PAIR (Chao et al., 2023) on a Llama-2-7b-chat model that had been subjected to the Q-Misalign attack at full precision. (Section 5.2)
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 1 paper
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including PAIR (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)

### Associated with
- **CSRT** (measurement instrument), 1 paper
  > We compare the CSRT to three non-multilingual red-teaming baselines (i.e., GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024), and PAIR (Chao et al., 2025)). (Section 4.3)
  - [Code-Switching Red-Teaming: LLM Evaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.657.pdf)
