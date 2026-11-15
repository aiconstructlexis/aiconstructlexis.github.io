# Watermark detectability
**Type:** Construct  
**Supporting papers:** 14  
**Also known as:** Detectability, Machine-generated text detectability  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats detectability as successful identification of a watermark signal in model-generated text. Most definitions describe the degree or latent ability with which a detection algorithm, detection system, or watermarking scheme can distinguish watermarked from non-watermarked text from statistical patterns in token selection, sometimes explicitly under tokenization inconsistencies or adversarial attacks, and sometimes with attention to low false positive rates. A smaller line of work uses the same term more broadly for machine-generated text, defining it as the ability to distinguish AI-generated or machine-generated text from human-authored text, with one paper stating that personalization reduces that detectability.

**Space of facets.** The definitions differentiate detectability along two recurring axes. One axis is the target distinction, watermark presence versus human-authored versus machine-generated text, and the other is where the property is located, as papers variously place it in the embedded statistical signal, the detection system, the watermarking scheme, or the generated text itself. Several papers also discuss detectability together with robustness, generation quality, stealthiness, resilience, or safety mechanisms, and one paper expresses it in the language of statistical test power.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to it. In the papers, detectability is nevertheless operationalized through evaluations of whether detectors identify watermarked text, AUROC used to simulate detectability in real-world scenarios, statistical testing framed as test power and test level, evaluations on machine translation and protein generation, and assessments of whether AI detectors distinguish machine-generated from human-authored content. These operationalizations mostly match the dominant definitions by targeting successful detection, though some broaden the target from watermark presence to machine-generated text more generally.

**Links.** No causal, correlational, related, or measured_by links are reported for this construct.

## Sources

**Watermark detectability** (3 papers: [A Watermark for Order-Agnostic Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ce8e3434c7b486bbddff9745b2a1722-Paper-Conference.pdf), [Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking](https://aclanthology.org/2025.emnlp-main.341.pdf), [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf))
> The degree to which a statistical signal embedded in model-generated text can be successfully identified by a detection algorithm.

**Detectability** (3 papers: [Addressing Tokenization Inconsistency in Steganography and Watermarking Based on Large Language Models](https://aclanthology.org/2025.emnlp-main.361.pdf), [Evaluation of LLM Vulnerabilities to Being Misused for Personalized Disinformation Generation](https://aclanthology.org/2025.acl-long.38.pdf), [StealthInk: A Multi-bit and Stealthy Watermark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25j/jiang25j.pdf))
> The ability of a watermark detection system to correctly identify LLM-generated text as watermarked, even in the presence of tokenization inconsistencies or adversarial attacks.

**Machine-generated text detectability** (1 paper: [OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1354.pdf))
> The latent ability of a model or system to distinguish between human-authored and machine-generated text based on underlying linguistic or statistical patterns.
