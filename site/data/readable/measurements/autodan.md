# AutoDAN
**Type:** Measurement instrument  
**Supporting papers:** 19  

## State of the Field

**What it is.** Across papers, the prevailing usage treats AutoDAN as an automated jailbreak attack procedure, most commonly a genetic algorithm, sometimes a hierarchical genetic algorithm, that searches for adversarial prompts intended to bypass LLM safety alignment. Definitions vary on how the attack is characterized: some call it white-box, gradient-based, query-based, instruction-based, or optimization-based, and some emphasize that it produces high-perplexity, human-readable, or stealthier prompts through controllable text generation or an added loss term. A smaller line of work instead treats AutoDAN as a public dataset for jailbreak detection, or as an attack represented within the EasyJailbreak dataset for transferability evaluation.

**What it is claimed to measure.** The reported measurement claims concentrate on a small set of targets. Papers use AutoDAN to measure one construct, adversarial robustness, and one behavioral indicator, jailbreak resistance, rather than a broad range of targets. In these uses, it appears as a jailbreak attack for evaluating robustness, with one paper explicitly reporting adversarial robustness as attack success rate and another evaluating robustness against state of the art jailbreak attacks including AutoDAN.

**Space of uses.** In use, papers most often place AutoDAN alongside other jailbreak or red-teaming methods, especially GCG and PAIR, and also TAP and CSRT. The dominant positioning is as a comparison or baseline attack, for example as a representative gradient-based method, a white-box attack, or an optimization-based attack in robustness studies. Among explicit instrument-level links, papers relate it to one instrument, CSRT, through a comparison against non-multilingual red-teaming baselines; some papers also use it in algorithmic attack suites, jailbreak detection datasets, or transferability tests on EasyJailbreak.

## Sources

**AutoDAN** (9 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf), [LLMScan: Causal Scan for LLM Misbehavior Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25al/zhang25al.pdf), [A Theoretical Understanding of Self-Correction through In-context Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/a399456a191ca36c7c78dff367887f0a-Paper-Conference.pdf), [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf), [Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf))
> A genetic-algorithm jailbreak procedure that generates adversarial prompts intended to bypass LLM safety alignment.

## Relationships

### → AutoDAN
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 1 paper
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Adversarial robustness** (construct): *measured_by*, 1 paper
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)

### Associated with
- **CSRT** (measurement instrument), 1 paper
  > We compare the CSRT to three non-multilingual red-teaming baselines (i.e., GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024), and PAIR (Chao et al., 2025)). (Section 4.3)
  - [Code-Switching Red-Teaming: LLM Evaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.657.pdf)
