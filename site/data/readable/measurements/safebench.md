# SafeBench
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the definitions, SafeBench is most commonly described as a safety benchmark for VLMs or MLLMs. The prevailing description says it contains 500 malicious questions organized into 10 categories based on AI usage policies. Some authors frame it more specifically as a benchmark for evaluating defense against jailbreak attacks or the ability to perceive multimodal risks, and one paper refers to SafeBench11, described as constructed with FigStep and sampled at 200 items.

**What it is claimed to measure.** Papers use SafeBench to measure two behavioral indicators, Jailbreaking and Jailbreak resistance, and no construct is linked to it. The linked uses converge on jailbreak-related behavior: one paper reports attack success rates on SafeBench as evidence for Jailbreaking, while another uses it among jailbreak attack methods or datasets to evaluate defense capabilities against jailbreak attacks, that is, Jailbreak resistance.

**Space of uses.** No measurement instrument is linked to it through recorded relationships. In use, papers most often place it alongside MM-SafeBench or MM-SafetyBench and HADES or HADES-Dataset, and also alongside MML, HIMRD, and AdvBench. The recurring positioning is as one of several established or safety benchmarks, or as one of several jailbreak attack methods or datasets in a broader evaluation.

## Sources

**SafeBench** (3 papers: [Jailbreak Large Vision-Language Models Through Multi-Modal Linkage](https://aclanthology.org/2025.acl-long.74.pdf), [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for evaluating VLM safety, comprising 500 malicious questions organized into 10 categories based on AI usage policies.

## Relationships

### → SafeBench
- **Jailbreaking** (behavioral indicator): *measured_by*, 1 paper
  > Our approach achieves higher attack success rates compared to existing multimodal attacks on SafeBench (Gong et al., 2023) and AdvBench (Zou et al., 2023). (Abstract)
  - [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf)
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)
