# Jailbreak resistance
**Type:** Behavioral indicator  
**Supporting papers:** 12  
**Also known as:** Jailbreak attack resistance  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats jailbreak resistance as a model's observable refusal to comply with prompts meant to bypass safety filters or safety constraints and elicit harmful or prohibited content. Definitions largely agree that success means maintaining safety constraints, or aligned responses, under adversarial prompts, and some papers describe the same behavior as jailbreak robustness or robustness against jailbreaking prompts. A smaller multimodal framing narrows it to resisting harmful generation from adversarial image-text pairs or typographic manipulation.

**Variants.** Most work studies text-based adversarial prompting, including unsafe prompts, real-world adversarial prompts, and adversarial perturbations aimed at circumventing safety constraints or ethical guidelines. Papers use several nearby labels for this setting, including jailbreak resistance, jailbreak attack resistance, jailbreak robustness, and jailbreak susceptibility. A smaller line examines multimodal settings, where the attack is delivered through image-text pairs or typographic manipulation and the focus is on the defense capabilities of multimodal language models.

**Space of elicitation and scores.** Papers measure it with 7 instruments, most often AdvBench and GCG, alongside AutoDAN, HADES, and MM-SafetyBench, plus 2 other instruments. These instruments are used as unsafe-prompt benchmarks, jailbreak attack methods, or attack datasets for evaluating robustness or defense capabilities. The recorded scoring language includes attack success rate on AdvBench, unsafety detection rate on unsafe prompts, and robustness against named jailbreak attacks.

**What it is taken as evidence of.** The only linked construct is Logical reasoning, so the papers do not present competing construct linkages for what this behavior reflects. One paper claims a causal relationship from Logical reasoning to Jailbreak resistance, stating that grounding knowledge and a principled reasoning procedure make a guardrail robust against jailbreak attacks.

## Sources

**Jailbreak resistance** (5 papers: [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf), [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf), [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf), [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf))
> The observable behavior of refusing to comply with prompts designed to bypass safety filters and elicit harmful or prohibited content.

**Jailbreak attack resistance** (1 paper: [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf))
> The model successfully resists attempts to generate harmful content through adversarial image-text pairs or typographic manipulation.

## Relationships

### Jailbreak resistance →
- **AdvBench** (measurement instrument): *measured_by*, 2 papers
  > Results in Table 5 show that TAIA significantly reduces the attack success rate after tuning on three levels of red-teaming data... evaluated on Advbench [10].
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **GCG** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **PAIR** (measurement instrument): *measured_by*, 1 paper
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **AutoDAN** (measurement instrument): *measured_by*, 1 paper
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **SafeBench** (measurement instrument): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)
- **MM-SafetyBench** (measurement instrument): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)
- **HADES** (measurement instrument): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)

### → Jailbreak resistance
- **Logical reasoning** (construct): *causes*, 1 paper
  > The grounding knowledge and principled reasoning procedure enable R2-Guard to be effective, robust against jailbreak attacks, and flexible given new safety categories. (Abstract)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
