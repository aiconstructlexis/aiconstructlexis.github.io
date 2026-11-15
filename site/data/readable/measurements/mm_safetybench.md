# MM-SafetyBench
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** MM-Safetybench, MM-SafeBench  

## State of the Field

**What it is.** Across papers, MM-SafetyBench is most commonly described as a multimodal safety benchmark for testing whether vision-language models produce unsafe responses to harmful inputs. A smaller set of descriptions makes the content more specific: one defines it as 5,040 text-image pairs across 13 scenarios for assessing safety and robustness against multimodal jailbreak attacks, while another treats it as a dataset of typographical images, stable diffusion-generated images, Typo + SD images, and text-based attack samples. Papers also mention alternate forms or subsets, including an official tiny version with 168 samples, a sampled set of 100 harmful and safe images, and the abbreviation MMSafe.

**What it is claimed to measure.** Its recorded uses are concentrated on safety-related outcomes. Papers link it to 2 constructs, Safety and Safety robustness, and to 2 behavioral indicators, Harmful content generation and Jailbreak resistance; in the relationship evidence, it is used to assess multimodal safety, judge resiliency under harm-inducing instructions, evaluate jailbreak robustness and defense capabilities against jailbreak attacks, and test whether image-query-related inputs elicit harmful responses.

**Space of uses.** Across the surveyed work, MM-SafetyBench is usually used as one benchmark within a broader safety or jailbreak evaluation suite, often alongside FigStep, SIUO, SafeBench, Hades, and JailBreaKV. Papers position it both as a general multimodal safety benchmark and as a jailbreak-focused dataset within multi-benchmark evaluations, and some use reduced variants such as the tiny version or sampled subsets rather than only the full benchmark.

## Sources

**MM-SafetyBench** (5 papers: [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [HiddenDetect: Detecting Jailbreak Attacks against Multimodal Large Language Models via Monitoring Hidden States](https://aclanthology.org/2025.acl-long.724.pdf), [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multimodal safety benchmark used to test whether VLMs produce unsafe responses to harmful inputs.

**MM-Safetybench** (1 paper: [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf))
> A benchmark for assessing the safety of models in multimodal (vision-language) contexts.

**MM-SafeBench** (1 paper: [Jailbreak Large Vision-Language Models Through Multi-Modal Linkage](https://aclanthology.org/2025.acl-long.74.pdf))
> A benchmark featuring 5,040 text-image pairs across 13 scenarios, designed to assess the safety and robustness of vision-language models against multimodal jailbreak attacks.

## Relationships

### → MM-SafetyBench
- **Safety** (construct): *measured_by*, 2 papers
  > We evaluate the VLMs with MM-Safety-Bench [28] to judge the resiliency of VLMs when they are prompted with harm-inducing instructions. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 1 paper
  > We adopt five jailbreak attack methods or datasets to comprehensively evaluate the defense capabilities of MLLMs against jailbreak attacks, including SafeBench (Gong et al., 2023), MM-SafetyBench (Liu et al., 2024b), Hades (Li et al., 2024), MML (Wang et al., 2024c), and HIMRD (Teng et al., 2024).
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf)
- **Safety robustness** (construct): *measured_by*, 1 paper
  > ...for evaluating jailbreak robustness, we employ MM-SafetyBench (Liu et al., 2024b), FigStep (Gong et al., 2025) and JailBreaKV (Luo et al., 2024) (Section 2.1).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 1 paper
  > MM-SafetyBench (Liu et al., 2024b), originally proposed as QR Attack, uses image-query-related inputs to elicit harmful responses from models. (Section 4.1)
  - [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.487.pdf)
