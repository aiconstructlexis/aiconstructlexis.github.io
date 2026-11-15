# HallusionBench
**Type:** Measurement instrument  
**Supporting papers:** 26  
**Also known as:** HallBench  

## State of the Field

**What it is.** Across the surveyed work, HallusionBench is most commonly described as a benchmark or diagnostic suite for assessing hallucination in multimodal or vision-language models. A recurring formulation is that it targets both language or knowledge hallucination and visual illusion, and some papers add that it distinguishes different VLM reasoning error modes or evaluates across question type and difficulty. A smaller line of descriptions treats HallBench or HallB as the same resource and frames it more broadly as a multimodal understanding benchmark with an emphasis on hallucination-related performance, or as an image-context reasoning benchmark built from paired images and questions.

**What it is claimed to measure.** Papers use HallusionBench to measure 1 construct and 4 behavioral indicators. The prevailing use is to measure hallucination, with papers saying it evaluates visual illusions and knowledge hallucinations, or how well multimodal models handle language hallucinations and visual illusions. Smaller strands report it as measuring hallucination detection, visual hallucination, and visual question answering, and one paper uses it to measure the construct hallucination resistance.

**Space of uses.** Papers usually use HallusionBench as one component in broader evaluation suites rather than in isolation. It is repeatedly paired with POPE in hallucination evaluations, and other studies use it alongside CHAIR, MMHal-Bench, GAVIE, and LLaVABench in visual perception, hallucination, or specific-domain VQA setups. Some authors also position HallBench among more challenging benchmarks for multimodal large language models.

## Sources

**HallusionBench** (7 papers: [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf), [Diffusion Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25g/jin25g.pdf), [Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.121.pdf), [Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a13ff984831deea39e6132bafdfdd6d5-Paper-Datasets_and_Benchmarks_Track.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf))
> HallusionBench is a benchmark for assessing hallucination in multimodal models.

**HallBench** (1 paper: [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf))
> HallBench, a benchmark used to evaluate multimodal understanding with an emphasis on hallucination-related performance.

## Relationships

### → HallusionBench
- **Hallucination** (behavioral indicator): *measured_by*, 4 papers
  > HallusionBench (Guan et al., 2024) evaluates visual illusions and knowledge hallucinations, featuring 346 images and 1129 questions. (Sec. 5.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
- **Hallucination resistance** (construct): *measured_by*, 1 paper
  > HallusionBench focuses on diagnosing both the visual illusion and knowledge hallucination of MLLMs.
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Hallucination detection** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the visual perception capabilities of RePer, we conducted assessments across five widely-used benchmarks, covering a range of tasks: ... hallucination detection (HallusionBench (Guan et al., 2024), MMHal-Bench (Sun et al., 2023b), GAVIE (Liu et al., 2023a)) (Section 4.2)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > Additionally, we evaluate performance on specific-domain VQA tasks, which include ChartQA (Masry et al., 2022), LLaVABench (Liu et al., 2024c), and HallusionBench (Guan et al., 2023). (Section 4.1)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)
- **Visual hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Furthermore, we use HallBench (Guan et al., 2024) to quantify the extent of visual hallucinations in VLMs or VRMs. (Section 4.1)
  - [Look Again, Think Slowly: Enhancing Visual Reflection in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.470.pdf)
