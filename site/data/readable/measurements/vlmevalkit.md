# VLMEvalKit
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** VLMEvalkit, OpenCompass VLMEvalKit  

## State of the Field

**What it is.** Most papers describe VLMEvalKit as an evaluation toolkit or standardized platform for assessing vision-language or multimodal models on benchmarks. Recurring details are that it is open-source, serves as a common codebase, and is used to keep settings consistent across methods for fair comparison or unified reproduction of results. A smaller line of work also treats it as a source of benchmark results, with one paper describing it as including diverse benchmarks and performance results from more than 100 MLLMs.

**What it is claimed to measure.** Across papers, VLMEvalKit is not linked to any named constructs or behavioral indicators. Instead, it is described in broad performance terms, assessing vision-language, large vision-language, or multimodal models on various benchmarks, including reasoning benchmarks and benchmark-specific evaluations. The prevailing framing is therefore benchmark evaluation rather than measurement of a single named construct.

**Space of uses.** In use, papers usually position VLMEvalKit as the shared evaluation framework for running experiments under the same configuration, sometimes within OpenCompass, and one paper uses results obtained through it as a data source for redundancy analysis. Papers relate it to three other instruments: MMBench-Video is related to VLMEvalKit because its evaluation code "will be integrated into VLMEvalKit," and MME-RealWorld and MMStar are related to it in work stating that "the evaluation framework employed for these benchmarks was VLMEvalKit."

## Sources

**VLMEvalKit** (10 papers: [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf), [Redundancy Principles for MLLMs Benchmarks](https://aclanthology.org/2025.acl-long.612.pdf), [Parrot: Multilingual Visual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ad/sun25ad.pdf), [KRETA: A Benchmark for Korean Reading and Reasoning in Text-Rich VQA Attuned to Diverse Visual Contexts](https://aclanthology.org/2025.emnlp-main.1696.pdf), [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf), [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf), [GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab7e02fd60e47e2a379d567f6b54f04e-Paper-Datasets_and_Benchmarks_Track.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf), [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf))
> An evaluation toolkit used to assess the performance of Vision-Language Models on various benchmarks.

**VLMEvalkit** (1 paper: [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf))
> A standardized evaluation platform used for assessing Large Vision-Language Models to ensure fair comparisons.

**OpenCompass VLMEvalKit** (1 paper: [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf))
> A universal evaluation platform used to reproduce multimodal benchmark results.

## Relationships

### Associated with
- **MMBench-Video** (measurement instrument), 1 paper
  > The evalutation code of MMBench-Video will be integrated into VLMEvalKit (Abstract)
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MME-RealWorld** (measurement instrument), 1 paper
  > "The evaluation framework employed for these benchmarks was VLMEvalKit (Duan et al., 2024)."
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **MMStar** (measurement instrument), 1 paper
  > "The evaluation framework employed for these benchmarks was VLMEvalKit (Duan et al., 2024)."
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
