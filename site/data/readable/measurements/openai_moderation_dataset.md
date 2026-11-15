# OpenAI Moderation dataset
**Type:** Measurement instrument  
**Supporting papers:** 2  
**Also known as:** OpenAI Mod  

## State of the Field

A standard safety dataset used to evaluate the performance of guardrail models in detecting unsafe content.

## Sources

**OpenAI Mod** (1 paper: [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf))
> A standard safety dataset used to evaluate the performance of guardrail models in detecting unsafe content.

## Relationships

### → OpenAI Moderation dataset
- **Harmful content detection** (behavioral indicator): *measured_by*, 3 papers
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **Content moderation** (behavioral indicator): *measured_by*, 1 paper
  > Additionally, it performs on par with WILDGUARD (Han et al., 2024) in terms of average harmfulness F1 scores across WILDGUARDTEST (Han et al., 2024), XSTest (Röttger et al., 2023; Han et al., 2024), and the OpenAI Moderation Dataset (Markov et al., 2023). (Section 5)
  - [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf)
