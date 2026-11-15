# MMHal-Bench
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** MMHAL-Bench, MM-Hal-Bench  

## State of the Field

**What it is.** Across papers, MMHal-Bench is most commonly described as a benchmark for multimodal or vision-language hallucination. Most definitions portray it as 96 image-question pairs, or questions, spanning eight question types, including object attributes, adversarial objects, comparisons, counting, and spatial relations; one paper additionally describes 12 object topics, and some authors frame it as a question-answering or generative benchmark. Many papers also describe GPT-4-based evaluation, variously for hallucination severity, response quality, hallucination rate, or agreement with human responses, object labels, or ground-truth answers, and a few papers add response informativeness or information richness.

**What it is claimed to measure.** Across papers, it is linked to six behavioral indicators and one construct. The prevailing usage is to measure hallucination: papers say it quantifies hallucinations, evaluates the degree of hallucination, or assesses response-level hallucination rates. Smaller lines of work also use it to measure attribute recognition, hallucination detection, object hallucination, and, in one paper, faithfulness by identifying hallucinations in outputs, plus two other behavioral indicators, so the claims mostly center on hallucination but also extend beyond it.

**Space of uses.** No measurement instrument is linked to it. Papers nevertheless often use it alongside POPE, and sometimes with CHAIR, Object HalBench, HallusionBench, and GAVIE, typically in evaluations that compare several hallucination benchmarks at once. Some papers distinguish it from POPE and CHAIR by saying it takes into account logical considerations such as object count, attributes, and relationships, and one paper positions it as one of two popular benchmarks for investigating potential hallucinations.

## Sources

**MMHal-Bench** (6 papers: [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf), [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf), [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf), [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf), [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf))
> MMHal-Bench is a benchmark designed to assess hallucination in multimodal models across a variety of scenarios.

**MMHAL-Bench** (1 paper: [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf))
> A benchmark for evaluating multimodal hallucination across multiple question types, including object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others.

**MM-Hal-Bench** (1 paper: [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> A hallucination-based benchmark containing 96 questions across 8 categories such as object attribute, adversarial object, and counting.

## Relationships

### → MMHal-Bench
- **Hallucination** (behavioral indicator): *measured_by*, 9 papers
  > MMHal-Bench is designed to quantify hallucinations with the assistance of GPT-4 [43]. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > MMHal-Bench (MMHal) (Sun et al., 2023) is a question-answering benchmark that covers 8 question categories and 12 object topics. (Sec. 5.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Visual hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **Attribute recognition** (behavioral indicator): *measured_by*, 1 paper
  > "MMHAL-Bench (Sun et al., 2023): This benchmark evaluates LVLMs beyond object hallucination and contains eight question types: object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others."
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
- **Object hallucination** (behavioral indicator): *measured_by*, 1 paper
  > “We utilize MMHal-Bench (Sun et al., 2023), which evaluates hallucination across 12 object-topics, including object attributes, presence of adversarial objects, and spatial relations, among others.”
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Faithfulness** (construct): *measured_by*, 1 paper
  > MMHal-Bench (Sun et al., 2023), which gauges the faithfulness of VLMs by identifying hallucinations in their outputs. (Section 5.2)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **Hallucination detection** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the visual perception capabilities of RePer, we conducted assessments across five widely-used benchmarks, covering a range of tasks: ... hallucination detection (HallusionBench (Guan et al., 2024), MMHal-Bench (Sun et al., 2023b), GAVIE (Liu et al., 2023a)) (Section 4.2)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
