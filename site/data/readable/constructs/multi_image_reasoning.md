# Multi-image reasoning
**Type:** Construct  
**Supporting papers:** 14  
**Also known as:** Multi-image comprehension, Multi-frame integration, Multi-image understanding  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this as a latent model ability to integrate information across multiple images within a single context. Most descriptions emphasize cross-image comparison, synthesis, and answering questions or inferring relations from multiple images, while some frame the same ability as multi-image comprehension or understanding, focusing on identifying shared or consistent elements or handling multiple images with interleaved text. A smaller line of work extends the framing from multiple images to non-overlapping video frames, describing a need to accumulate geometric and visual cues across time to form a unified scene understanding.

**Space of facets.** Papers use several neighboring names, multi-image reasoning, multi-image comprehension, and multi-image understanding, for closely related descriptions of integrating across multiple images. They systematize it mainly by the kind of cross-image relation to recover: some ask for spatial, temporal, or logical relations among images, some focus on shared or consistent elements, and one paper recasts the problem as multi-frame integration across disjoint video frames. It is also contrasted with single-image visual understanding, with one study noting that models focused on single images are limited in their ability to interpret and integrate information across multiple images.

**Space of measurement.** Papers link it to 10 measurement instruments and 1 behavioral indicator, and the operationalization is almost entirely benchmark-based. The most common instruments are Mantis-Eval, BLINK, MMMU, NLVR2, and MVBench, with the remaining instruments also introduced as multi-image evaluation benchmarks or tasks; the evidence describes Mantis-Eval as a benchmark for multi-image reasoning, MuirBench as a benchmark to assess multi-image understanding, and SEED-Bench-2 as evaluating comprehension of multimodal inputs containing multiple images. This largely matches the definitions, because the instruments are presented as probing multi-image reasoning, understanding, or comprehension rather than a different target.

**Links.** Beyond measurement, one paper reports that Knowledge-based visual question answering is related to multi-image reasoning. The evidence places both within a benchmark that comprises scenarios involving multi-image reasoning and understanding, listing Knowledge Grounded QA alongside Multi-Image Reasoning.

## Sources

**Multi-image reasoning** (3 papers: [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf), [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf), [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf))
> The latent ability to integrate information across multiple images and answer questions or infer relations that require cross-image comparison and synthesis.

**Multi-image comprehension** (2 papers: [EasyRef: Omni-Generalized Group Image Reference for Diffusion Models via Multimodal LLM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zong25a/zong25a.pdf), [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf))
> The latent ability of a multimodal model to understand and integrate visual content across multiple images to identify shared or consistent elements.

**Multi-frame integration** (1 paper: [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://aclanthology.org/2025.emnlp-main.816.pdf))
> The capacity to accumulate and synthesize geometric and visual cues across non-overlapping video frames to form a unified understanding of a scene.

**Multi-image understanding** (1 paper: [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf))
> The latent ability to correctly interpret and reason over inputs containing multiple images and interleaved text.

## Relationships

### Multi-image reasoning →
- **Mantis-Eval** (measurement instrument): *measured_by*, 6 papers
  > We additionally evaluate models on MMMU [Yue et al., 2024](containing both single and multi-image questions) and Mantis-Eval [Jiang et al., 2024](all multi-image questions) to probe a model’s multi-image reasoning abilities beyond in-context learning evaluations. (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **BLINK** (measurement instrument): *measured_by*, 4 papers
  > “Table 4 presents the the evaluation results on multi-image understanding benchmarks. The evaluation benchmarks consist of ... BLINK ...”
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **MMMU** (measurement instrument): *measured_by*, 2 papers
  > We additionally evaluate models on MMMU [Yue et al., 2024](containing both single and multi-image questions) and Mantis-Eval [Jiang et al., 2024](all multi-image questions) to probe a model’s multi-image reasoning abilities beyond in-context learning evaluations. (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
- **NLVR2** (measurement instrument): *measured_by*, 2 papers
  > “Table 4 presents the the evaluation results on multi-image understanding benchmarks. The evaluation benchmarks consist of NLVR2 ...”
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
- **MathVerse-mv** (measurement instrument): *measured_by*, 1 paper
  > “Table 4 presents the the evaluation results on multi-image understanding benchmarks. The evaluation benchmarks consist of ... MathVerse-mv ...”
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **SciVerse-mv** (measurement instrument): *measured_by*, 1 paper
  > “Table 4 presents the the evaluation results on multi-image understanding benchmarks. The evaluation benchmarks consist of ... SciVerse-mv ...”
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **MVBench** (measurement instrument): *measured_by*, 1 paper
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce MUIRBENCH (MULTI-IMAGE UNDERSTANDING BENCHMARK), a comprehensive benchmark designed to rigorously assess and evaluate multi-image understanding by multimodal LLMs. (Section 2)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **SEED-Bench-2** (measurement instrument): *measured_by*, 1 paper
  > Multi-image Tasks: Seed-Bench-2 (Li et al., 2024) evaluates the ability to comprehend multimodal inputs containing multiple images.
  - [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf)
- **Q-Bench** (measurement instrument): *measured_by*, 1 paper
  > For multi-image tasks, we incorporate Mantis-Eval (Jiang et al., 2024), QBench (Wu et al., 2024b), and BLINK (Fu et al., 2024b), in line with LLaVA-Interleave (Li et al., 2024a). (Section 2.1)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)

### Associated with
- **Knowledge-based visual question answering** (behavioral indicator), 1 paper
  > DemonBench comprises seven scenarios involving multi-image reasoning and understanding, including tasks such as Multi-Modal Dialogue, Visual Relation Inference, Knowledge Grounded QA, and Multi-Image Reasoning.
  - [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf)
