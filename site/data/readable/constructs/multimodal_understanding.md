# Multimodal understanding
**Type:** Construct  
**Supporting papers:** 101  
**Also known as:** Cross-modal understanding, Multi-modal understanding, Multimodal comprehension, Vision-language comprehension, Vision-language understanding, General multimodal ability, General multimodal capabilities, Multimodal capability, Multimodal Capability, Audio-visual understanding, Multimodal information comprehension, Visual-language understanding, Cross-modality comprehension, Trimodal understanding, Image-text understanding  

## State of the Field

**Space of definitions.** Most definitions treat multimodal understanding as a latent ability or general capacity to integrate and interpret information across multiple modalities, most often vision and language, so that models can answer questions, caption, or otherwise respond coherently to mixed inputs. A smaller line of work broadens the modality mix to images, text, IDs and tabular attributes, or to video, audio, speech, sensor signals, emoji, and document elements such as figures, tables, and equations. The main variation is therefore in scope, from standard image-text integration to broader cross-modal or domain-specific mixtures, rather than in the basic idea of joint interpretation.

**Space of facets.** Papers use several near-synonymous labels around this construct, including multimodal comprehension, vision-language understanding, cross-modal understanding, visual-language understanding, and image-text understanding. Some also split it by modality or setting, yielding audio-visual and trimodal variants, and domain-specific versions tied to STEM problems, scientific documents, screenshots or GUIs, financial materials, and sensor-language inputs. Another recurring pattern is to discuss understanding together with reasoning and, in some papers, alongside generation or creation.

**Space of measurement.** Papers link multimodal understanding to 22 measurement instruments and 5 behavioral indicators. Benchmark-based evaluation is the prevailing operationalization, most often with MMBench, MME, MMMU, VQA-v2, and POPE. These evaluations are instantiated through multimodal question answering, captioning, and related public-benchmark tasks; some papers say MMBench covers layout reasoning and structured chart interpretation, and MME separates perception from cognition. This mostly matches the definitions' emphasis on integrating modalities, although one paper cautions that correctly answering a question does not necessarily indicate that the model genuinely knows how to derive the final answer.

**Links.** Papers also connect the construct to 8 other constructs and 5 task behaviors. They claim causal relationships from multimodal alignment, visual grounding, and task interference to multimodal understanding, and report other related links to constructs about reasoning, adaptation, and context length. On the behavioral side, it is most often related to visual question answering; separate papers also report a related captioning link and causal relationships involving video question answering, reconstruction, and generation tasks.

## Sources

**Multimodal comprehension** (7 papers: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d74033a247989e8f6f3bf9e0c9629fb5-Paper-Datasets_and_Benchmarks_Track.pdf), [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf), [Just a Scratch: Enhancing LLM Capabilities for Self-harm Detection through Intent Differentiation and Emoji Interpretation](https://aclanthology.org/2025.acl-long.1330.pdf), [On Path to Multimodal Generalist: General-Level and General-Bench](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fei25a/fei25a.pdf), [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf))
> The latent ability to understand and reason over combined text and image inputs, integrating information across modalities to perform tasks like visual question answering and captioning.

**Multi-modal understanding** (7 papers: [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf), [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf), [Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.97.pdf))
> The capacity to integrate and interpret information from multiple modalities such as images, text, IDs, and tabular attributes when making predictions or generating outputs.

**Multimodal understanding** (10 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Measuring Vision-Language STEM Skills of Neural Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a3a661eb3308d0bb686f6a4bac521032-Paper-Conference.pdf), [cPAPERS: A Dataset of Situated and Multimodal Interactive Conversations in Scientific Papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a19a9d527ed544d1272f07b0f8f934e-Paper-Datasets_and_Benchmarks_Track.pdf), [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [ScreenQA: Large-Scale Question-Answer Pairs Over Mobile App Screenshots](https://aclanthology.org/2025.naacl-long.477.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [Open-World Attribute Mining for E-Commerce Products with Multimodal Self-Correction Instruction Tuning](https://aclanthology.org/2025.acl-long.85.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf), [SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://aclanthology.org/2025.emnlp-main.19.pdf))
> The latent ability to integrate and interpret information across vision and language modalities to perform tasks such as question answering and captioning.

**Vision-language understanding** (2 papers: [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf), [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf))
> The latent ability to integrate and interpret information from both visual and linguistic modalities, enabling coherent responses to image-based queries.

**Vision-language comprehension** (1 paper: [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf))
> The latent ability to understand and align information from both visual and textual modalities to perform complex tasks.

**Cross-modal understanding** (5 papers: [Guiding Instruction-based Image Editing via Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf), [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf), [FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://aclanthology.org/2025.acl-long.1426.pdf), [PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25da/zhang25da.pdf), [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf))
> The underlying capacity of a multimodal model to integrate and interpret information from both visual and linguistic inputs to form coherent, context-sensitive responses or actions.

**Audio-visual understanding** (1 paper: [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf))
> The latent ability to integrate auditory and visual information to comprehend videos accurately across multimodal and unimodal settings.

**General multimodal capabilities** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> A broad set of skills for processing and reasoning about information from multiple modalities, such as text and images, in non-specialized contexts.

**Multimodal capability** (1 paper: [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf))
> The latent capacity to process and respond appropriately to image-based or other non-text inputs after vision-language adaptation.

**General multimodal ability** (1 paper: [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf))
> The overall proficiency of a model across a wide range of tasks that require processing and integrating both visual and textual information.

**Multimodal Capability** (1 paper: [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf))
> The general ability of the model to process and integrate information from multiple modalities, such as vision and language.

**Visual-language understanding** (1 paper: [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf))
> The model's latent ability to comprehend and integrate information from both visual (images) and textual modalities.

**Multimodal information comprehension** (1 paper: [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf))
> The ability to correctly interpret and extract meaning from queries that contain a mix of text and images.

**Cross-modality comprehension** (1 paper: [SegLLM: Multi-round Reasoning Segmentation with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e125fb53198f2143716d969584d0a28-Paper-Conference.pdf))
> The latent ability to jointly understand visual scenes and natural-language prompts in order to ground language in image content.

**Trimodal understanding** (1 paper: [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf))
> The ability to comprehend and reason over inputs that simultaneously combine text, image, and speech modalities.

**Image-text understanding** (1 paper: [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf))
> The model's general ability to comprehend the semantic relationship and alignment between visual and textual information.

## Relationships

### Multimodal understanding →
- **MMBench** (measurement instrument): *measured_by*, 8 papers
  > Additionally, we conducted a zero-shot evaluation on the recently developed benchmarks of MMBench and MM-Vet to assess the model’s performance in complex multimodal tasks. (Section 4.1)
  - [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)
- **MMMU** (measurement instrument): *measured_by*, 6 papers
  > For capabilities evaluation, we follow [34] to evaluate multimodal models on LLaVA-Wild for visual chat capability and MMMU [71] for multimodal understanding capability. (Section 4.2)
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
  - [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf)
- **MME** (measurement instrument): *measured_by*, 6 papers
  > we adopt these captions during the pre-training stage and follow the setup of LLaVA-1.5 [37] on various ... multi-modality understanding benchmarks for evaluation, such as ... MME [16]... (Section 4.1)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 4 papers
  > “We evaluate Emu on a broad range of vision-language tasks including image question answering (VQAv2 (Goyal et al., 2017)”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 3 papers
  > “We evaluate Emu on a broad range of vision-language tasks including image question answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018))”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 3 papers
  > we adopt these captions during the pre-training stage and follow the setup of LLaVA-1.5 [37] on various ... multi-modality understanding benchmarks for evaluation, such as ... POPE [34]... (Section 4.1)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 2 papers
  > Additionally, we conducted a zero-shot evaluation on the recently developed benchmarks of MMBench and MM-Vet to assess the model’s performance in complex multimodal tasks. (Section 4.1)
  - [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 2 papers
  > “We evaluate Emu on a broad range of vision-language tasks including image question answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019)”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 2 papers
  > Following LLaVA (Liu et al., 2024b), we evaluate the multimodal understanding capabilities of Show-o on POPE, MME, Flickr30k, VQAv2, GQA, and MMMU benchmarks. (Section 4.1)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator): *causes*, 2 papers
  > These models also exhibit strong multimodal understanding (Lin et al., 2023; Li et al., 2024; Zhang et al., 2023b), capable of answering questions about unseen content, thus opening up new avenues for improving VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 1 paper
  > we adopt these captions during the pre-training stage and follow the setup of LLaVA-1.5 [37] on various ... multi-modality understanding benchmarks for evaluation, such as ... SEED [30]... (Section 4.1)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MS-COCO** (measurement instrument): *measured_by*, 1 paper
  > “We evaluate Emu on a broad range of vision-language tasks including image captioning (MS-COCO (Chen et al., 2015))”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **GAIA** (measurement instrument): *measured_by*, 1 paper
  > It requires various agent capabilities, including reasoning, multi-modal understanding, web browsing, and coding. (§4.4)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Flickr30k** (measurement instrument): *measured_by*, 1 paper
  > Following LLaVA (Liu et al., 2024b), we evaluate the multimodal understanding capabilities of Show-o on POPE, MME, Flickr30k, VQAv2, GQA, and MMMU benchmarks. (Section 4.1)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **MMBench-CN** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on MME (Fu et al., 2023), MMB (Liu et al., 2023c), and MMBCN. Each encompasses various sub-tasks, enabling comprehensive evaluation of multimodal understanding and reasoning capabilities. (Section 4.1)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **VisDial** (measurement instrument): *measured_by*, 1 paper
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... VisDial (Das et al., 2017)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **MMMU-Pro** (measurement instrument): *measured_by*, 1 paper
  > MMMU-Pro is designed to more accurately and rigorously assess a model’s true multimodal understanding and reasoning capabilities across a wide range of academic disciplines. (Section 1)
  - [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://aclanthology.org/2025.acl-long.736.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > MMStar benchmarks 6 core capabilities and 18 detailed axes, aiming to evaluate LVLMs’ multi-modal capacities with carefully balanced and purified samples. (Abstract)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Multimodal generation** (behavioral indicator): *causes*, 1 paper
  > incorporating multimodal understanding data enhances the model’s comprehension of object details, including attributes such as color and quantity, thereby improving its generation capability. (Section 5.2.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > LLaVA Bench (Li et al., 2024) assesses multimodal understanding and reasoning capabilities, with overall accuracy reported across all tasks (Section 4.1).
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
- **DRISHTIKON** (measurement instrument): *measured_by*, 1 paper
  > “offering a robust testbed to advance culturally aware, multimodally competent language technologies”
  - [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf)

### → Multimodal understanding
- **Multimodal alignment** (construct): *causes*, 1 paper
  > “it is required to involve more image-text pairs for multimodal alignment and more image tokens to represent an image for better comprehending the image information.”
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Visual grounding** (construct): *causes*, 1 paper
  > visual grounding is crucial for robust multimodal understanding. (Section 1)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Image reconstruction** (behavioral indicator): *causes*, 1 paper
  > In this way, LMMs are required to preserve every detail of input images, thereby enhancing multimodal comprehension capabilities and reducing hallucinations. (Figure 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Task interference** (construct): *causes*, 1 paper
  > “task interference, where competing control and understanding tasks degrade performance when trained jointly.”
  - [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 4 papers
  > Researchers (Liu et al., 2024a; Zhu et al., 2023; Dai et al., 2024; Alayrac et al., 2022; Chen et al., 2023) have attempted to build a bridge between large language models and image encoders through simple mapping modules, and have already made significant progress in multimodal understanding tasks such as visual question answering (Section 1).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator), 3 papers
  > While conceptually simple, this allows us to explore vision-language understanding tasks such as captioning and VQA, as well as text-to-image generation. (Section 3.3)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Adaptability** (construct), 1 paper
  > This strategy is underpinned by the understanding that the evolution from LLMs to MLLMs can be conceptualized as a domain adaptation process, i.e., transitioning from text-centric to multi-modal understanding. (Section 1)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
- **Compositional generalization** (construct), 1 paper
  > Many of the advanced vision-language capabilities demonstrated by GPT-4 can be understood as compositional skills rooted in two foundational skills: image understanding and language generation. (Section 5)
  - [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > Integrating multi-modal understanding with long-context capability is important. (Section 1)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Temporal understanding** (construct), 1 paper
  > Specifically, temporal understanding issues refer to multimodal information comprehension and cross-modality coherence, while reasoning issues involve complex reasoning and generation capabilities. (Section 5)
  - [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf)
- **Cognitive reasoning** (construct), 1 paper
  > Cognition and Reasoning. This dimension encompasses data inference, cross-modal understanding, trend prediction, causal analysis, scenario-based decision support, and hypothesis analysis. (Section 3.3).
  - [FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://aclanthology.org/2025.acl-long.1426.pdf)
