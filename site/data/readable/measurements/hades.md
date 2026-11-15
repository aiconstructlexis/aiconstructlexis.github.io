# HADES
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** In the definitions, HADES is described as a multimodal jailbreak benchmark for probing multimodal safety under adversarial conditions. Papers characterize it as using crafted images with accompanying typography, with malicious intent embedded and amplified in those visual materials. It is also described as providing 750 samples across five harmful scenarios.

**What it is claimed to measure.** In the recorded links, papers use HADES to measure jailbreak resistance. It is linked to one behavioral indicator, Jailbreak resistance, and to no constructs, so the reported use centers on that single indicator rather than being spread across multiple constructs. A single paper also frames it as one of the datasets or attack methods used to evaluate the defense capabilities of multimodal large language models against jailbreak attacks.

**Space of uses.** Papers position HADES as part of a broader evaluation suite rather than as a stand-alone check. In the reported use, it appears alongside SafeBench, MM-SafetyBench, MML, and HIMRD when authors adopt several jailbreak attack methods or datasets to comprehensively evaluate defense capabilities against jailbreak attacks.

## Sources

**HADES** (1 paper: [VisCRA: A Visual Chain Reasoning Attack for Jailbreaking Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.312.pdf))
> HADES is a multimodal jailbreak benchmark with crafted images and accompanying typography designed to probe safety under adversarial conditions across harmful scenarios.

## Relationships

### → HADES
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)
