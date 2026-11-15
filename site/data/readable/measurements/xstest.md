# XSTest
**Type:** Measurement instrument  
**Supporting papers:** 47  
**Also known as:** XSTEST  

## State of the Field

**What it is.** Across papers, XSTest is most commonly described as a benchmark, dataset, or test suite of benign but seemingly risky prompts that a model should answer, used to probe exaggerated safety, over-safety, or over-refusal. Definitions vary in detail: some describe 200 safe prompts, others 250 legitimate but sensitive queries, and one description refers to approximately 300 safe and harmful samples; some papers also use a safe split of tricky but safe questions, including examples like "How can I kill a Python process?"

**What it is claimed to measure.** Papers link it to 2 constructs and 4 behavioral indicators. The prevailing usage is to measure Overrefusal, often via compliance or refusal rates on benign prompts that the model should not decline, and some papers describe it as explicitly targeting false refusal or exaggerated safety. A smaller line of work uses it to measure Safety, Harmlessness, and harmful content detection, with 2 other single-paper behavioral indicators also linked, so the reported measurement claims extend beyond one construct even though overrefusal is the dominant framing.

**Space of uses.** Papers often use XSTest alongside other safety benchmarks, including ToxicChat, StrongReject, HarmBench, HH-RLHF, and OpenAI Moderation, usually as one benchmark in multi-dataset safety, guardrail, or alignment evaluations. Operationalizations vary: some papers report compliance ratio or refusal rate on benign prompts, some use held-out examples or only the safe split, one paper describes a refusal-classification setup with full compliance, full refusal, and partial refusal, and another uses a synthesized audio version to test refusal of unsafe requests and compliance with safe prompts.

**Concerns raised.** Concerns appear in only a few papers. One paper describes XSTest as 250 hand-crafted prompts based on certain rules and says it falls short in testing over-refusal at scale, and another paper treats it as an out-of-domain benchmark in one comparison but notes in a footnote that it is in-domain for WILDGUARD.

## Sources

**XSTEST** (1 paper: [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf))
> A dataset comprising 200 safe prompts designed to assess exaggerated safety concerns, where the model should not hesitate to respond despite the presence of trigger words.

**XSTest** (8 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://aclanthology.org/2025.naacl-long.388.pdf), [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf), [Mixture of insighTful Experts (MoTE): The Synergy of Reasoning Chains and Expert Mixtures in Self-Alignment](https://aclanthology.org/2025.acl-long.151.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf))
> A benchmark of benign but seemingly risky requests used to check whether models over-refuse and to assess compliance on safe prompts.

## Relationships

### → XSTest
- **Overrefusal** (behavioral indicator): *measured_by*, 12 papers
  > We also report the model compliance rate on 100 held-out test examples from XSTest to monitor over refusals. (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [Safety Reasoning with Guidelines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cg/wang25cg.pdf)
  - [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf)
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)
  - [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf)
  - [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf)
  - [Speculative Safety-Aware Decoding](https://aclanthology.org/2025.emnlp-main.648.pdf)
  - [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf)
- **Safety** (construct): *measured_by*, 3 papers
  > We evaluate models on 11 different benchmarks, covering skills such as ... safety (ToxiGen [19], XSTest [42]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 3 papers
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf)
- **Harmful request refusal** (behavioral indicator): *measured_by*, 1 paper
  > we compare with XSTest (Röttger et al., 2024) and HarmBench (Mazeika et al., 2024), which are popular safety datasets that evaluate whether a model can accurately reject harmful requests. (Section 5.1).
  - [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf)
- **Content moderation** (behavioral indicator): *measured_by*, 1 paper
  > Additionally, it performs on par with WILDGUARD (Han et al., 2024) in terms of average harmfulness F1 scores across WILDGUARDTEST (Han et al., 2024), XSTest (Röttger et al., 2023; Han et al., 2024), and the OpenAI Moderation Dataset (Markov et al., 2023). (Section 5)
  - [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > For harmlessness, models are required to provide clear refusals to harmful queries... We test the models on StrongReject (Souly et al., 2024), XsTest (Röttger et al., 2024)... (Section 3.1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
