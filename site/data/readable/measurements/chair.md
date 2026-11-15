# CHAIR
**Type:** Measurement instrument  
**Supporting papers:** 32  

## State of the Field

**What it is.** Across the cited definitions, CHAIR is most commonly described as a benchmark, metric, or evaluation protocol for hallucination in image captioning, especially object hallucination. The prevailing description is that it compares generated captions with ground-truth objects or annotations and computes the proportion or ratio of mentioned objects that are not present in the image; most papers describe instance and sentence variants, written as CHAIRi and CHAIRs, for hallucinated object instances and sentences containing hallucinated objects. Some papers describe the same evaluation as open-ended captioning on sampled MS-COCO images, and a smaller line describes broader sentence- or image-level checks such as object, attribute, count, or positional correctness.

**What it is claimed to measure.** Papers link CHAIR to five behavioral indicators and one construct. The most frequent use is to measure Hallucination, Image captioning, and Object hallucination, with papers saying that CHAIR assesses hallucination by comparing objects mentioned in generated captions with ground-truth or reference objects; additional links treat it as measuring Text generation in open-ended generation settings and Visual hallucination in image-consistency evaluations. The only linked construct is Multimodal alignment, where one paper reports using CHAIR to show reward distributions of generated objects on the benchmark.

**Space of uses.** In use, papers commonly place CHAIR alongside other hallucination benchmarks, especially POPE, and some also pair it with GPT-4V-assisted evaluation, MMHal-Bench, or HallusionBench. The only explicit linked instrument is MS-COCO, and some papers describe running CHAIR on random samples of 500 validation images from that dataset. Papers usually position it as a commonly used benchmark for open-ended caption generation and hallucination evaluation, though some also use the CHAIR score to assess synthetic caption quality or to visualize generated-object rewards.

## Sources

**CHAIR** (9 papers: [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf), [Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a6a5e2e8a27262501bda3463fcf7b21-Paper-Conference.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf), [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf), [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf), [Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://aclanthology.org/2025.acl-long.175.pdf), [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf), [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf))
> Evaluation metric for hallucination in image captioning, measuring the fraction of hallucinated object instances (CHAIRi) and sentences containing hallucinated objects (CHAIRs).

## Relationships

### → CHAIR
- **Object hallucination** (behavioral indicator): *measured_by*, 15 papers
  > Caption Hallucination Assessment with Image Relevance (CHAIR) (Rohrbach et al., 2018) is a widely-used metric for evaluating object hallucination in image captioning tasks.
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
  - [Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention](https://aclanthology.org/2025.acl-long.634.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **Image captioning** (behavioral indicator): *measured_by*, 12 papers
  > Caption Hallucination Assessment with Image Relevance (CHAIR) (Rohrbach et al., 2018) is a widely-used metric for evaluating object hallucination in image captioning tasks.
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 10 papers
  > “The CHAIR metric ... evaluates the exact match between generated and ground-truth image captions”
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
  - [Probing Visual Language Priors in VLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25b/luo25b.pdf)
  - [Visual Attention Never Fades: Selective Progressive Attention ReCalibration for Detailed Image Captioning in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jung25c/jung25c.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **Multimodal alignment** (construct): *measured_by*, 1 paper
  > To better demonstrate how our method enhances vision-language alignment and ensures the generation of high-scoring objects, we visualize the reward distribution of generated objects on the CHAIR benchmark, as depicted in Figure 4.
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Visual hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > Finally, for open-ended generation, we use the CHAIR (Rohrbach et al., 2018). (Section 5.1)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)

### Associated with
- **MS-COCO** (measurement instrument), 1 paper
  > As for CHAIR, Following (Wang et al., 2024a; Huang et al., 2024; Yue et al., 2024b), we randomly select 500 images from the validation set of the MSCOCO (Lin et al., 2014) dataset (Section 5.2).
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
