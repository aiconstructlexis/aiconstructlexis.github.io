# BeaverTails
**Type:** Measurement instrument  
**Supporting papers:** 21  
**Also known as:** Beavertails  

## State of the Field

**What it is.** Across the surveyed work, BeaverTails is most commonly described as a safety and alignment evaluation dataset or benchmark for model responses, especially response safety classification. Papers describe it in several ways: as a human-preference dataset with helpfulness and harmlessness annotations for query-answer interactions, as advice queries with candidate answers across 14 harm categories, as human annotations over a 14-category safety taxonomy, and as either a 700-prompt evaluation set or a larger collection of 330k annotated sentences; one paper also refers to safe and unsafe samples from its alignment data.

**What it is claimed to measure.** Papers use BeaverTails to measure 4 constructs and 3 behavioral indicators, so the reported targets are spread across multiple safety-related concepts. The prevailing claims are that it measures harmlessness and helpfulness, while other papers use it to measure safety, harmful content generation, harmful content detection, and response harmfulness classification; one paper also reports BeaverTails as related to safety alignment by using its safe samples for an alignment task.

**Space of uses.** Papers commonly use BeaverTails alongside other benchmarks rather than alone. It appears with XSTest, AdvBench, Safe-RLHF, HarmBench, and Anthropic-HH, among others, for guardrail, response classification, preference-learning, and alignment evaluations, and one paper also uses its safe samples for an alignment task while mixing unsafe samples with benign fine-tuning data.

## Sources

**Beavertails** (5 papers: [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf), [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf), [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf), [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf), [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf))
> A dataset used to evaluate alignment and safety-related responses of finetuned language models.

**BeaverTails** (5 papers: [BingoGuard: LLM Content Moderation Tools with Risk Levels](https://proceedings.iclr.cc/paper_files/paper/2025/file/782b6152c04e9948c2cb3833e9a288ef-Paper-Conference.pdf), [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf), [Whose Boat Does it Float? Improving Personalization in Preference Tuning via Inferred User Personas](https://aclanthology.org/2025.acl-long.168.pdf), [Learning Safety Constraints for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25b/chen25b.pdf), [Gamma-Guard: Lightweight Residual Adapters for Robust Guardrails in Large Language Models](https://aclanthology.org/2025.emnlp-main.614.pdf))
> A benchmark dataset used for evaluating the performance of models on response safety classification.

## Relationships

### → BeaverTails
- **Harmlessness** (construct): *measured_by*, 3 papers
  > BeaverTails dataset... assessing the harmlessness and helpfulness of the models.
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1510.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 3 papers
  > To calculate the harmful score, we sample 1000 instructions from the testing set of BeaverTails (Ji et al., 2023).
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **Helpfulness** (construct): *measured_by*, 3 papers
  > BeaverTails dataset... assessing the harmlessness and helpfulness of the models.
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Response harmfulness classification** (behavioral indicator): *measured_by*, 1 paper
  > "For response classification, we consider Beaver-tails (Ji et al., 2024), Safe-RLHF (Dai et al., 2024), WildGuardTestResponse (Han et al., 2024), and HarmBench (Mazeika et al.) as benchmarks"
  - [BingoGuard: LLM Content Moderation Tools with Risk Levels](https://proceedings.iclr.cc/paper_files/paper/2025/file/782b6152c04e9948c2cb3833e9a288ef-Paper-Conference.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > Conversely, further introducing unsafe guidelines into the system prompt reduces the safety performance on BeaverTails (Ji et al., 2024) (91.40 vs. 63.30). (Section 2.2)
  - [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf)

### Associated with
- **Safety alignment** (construct), 1 paper
  > “For the alignment task, we use the safe samples from the alignment dataset of BeaverTails (Ji et al., 2023).”
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
