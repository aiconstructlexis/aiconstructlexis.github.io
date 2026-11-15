# Multimodal reasoning
**Type:** Construct  
**Supporting papers:** 71  
**Also known as:** Cross-modal reasoning, Multi-modal reasoning, X-modal reasoning, Cross-modal consistency reasoning, Audio-visual reasoning, Contrastive cross-modal reasoning, Image understanding and reasoning, Content reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats multimodal reasoning as a latent ability or capacity to integrate information across modalities, most often visual and textual inputs, so a model can draw conclusions, make inferences, or solve complex tasks. A smaller line narrows the construct to judging semantic alignment or consistency between modalities, for example whether text and images are semantically consistent, while other definitions broaden the scope beyond text-image pairs to mixtures that can include audio, video, tables, figures, or visual formatting cues. Some papers further specialize it to multi-step reasoning, audio-visual inference, contrastive selection across modalities, or reasoning grounded mainly in visual inputs.

**Space of facets.** Papers use several overlapping labels for nearby ideas, including cross-modal reasoning, multi-modal reasoning, X-modal reasoning, audio-visual reasoning, and cross-modal consistency reasoning. These labels largely share the same core of integrating information across modalities, but they emphasize different facets: semantic consistency between text and image, contrastive cross-modal semantic comparison, multi-step reasoning under modality misalignment, or document-level reasoning over text, tables, and figures. Some papers also position it alongside, rather than identical to, other abilities such as visual understanding, code generation, visual data interpretation, and algorithmic problem solving.

**Space of measurement.** Operationally, papers link multimodal reasoning to 15 measurement instruments and 4 behavioral indicators. The most frequently linked instruments are benchmark-style evaluations, especially MMBench, MMMU, MathVista, ScienceQA, and AI2D; other linked benchmarks target settings such as chart-to-code generation, multimodal mathematics, image question answering, and retrieval, counting, and reasoning. The linked behavioral indicators are visual question answering, object counting, optical character recognition, and text-to-speech synthesis. These operationalizations usually instantiate the same broad idea of integrating multiple inputs, though some narrow it to specific task formats such as chart reasoning or mathematical reasoning.

**Links.** Beyond measurement, individual papers claim causal relationships from multimodal reasoning to visual grounding and to robustness, and a separate paper claims a causal relationship in the opposite direction, from visual understanding to multimodal reasoning. Papers also report multimodal reasoning as related to commonsense reasoning and to task behaviors such as visual question answering, with other related behaviors also reported. No paper here reports a correlational link.

## Sources

**Cross-modal reasoning** (3 papers: [VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf), [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf), [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf))
> The latent ability to infer whether visual content and textual labels are semantically consistent by combining evidence across modalities.

**Multimodal reasoning** (10 papers: [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf), [FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf), [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.188.pdf), [AlgoPuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Algorithmic Multimodal Puzzles](https://aclanthology.org/2025.naacl-long.486.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.185.pdf), [Progressive Multimodal Reasoning via Active Retrieval](https://aclanthology.org/2025.acl-long.180.pdf), [RBench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25r/guo25r.pdf), [SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models](https://aclanthology.org/2025.emnlp-main.27.pdf))
> The capacity to draw conclusions and make inferences by integrating information from both visual and textual inputs in a coherent manner.

**Multi-modal reasoning** (4 papers: [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf), [MAPS: Advancing Multi-Modal Reasoning in Expert-Level Physical Science](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0422224da8dc076cab83709b9839b7b-Paper-Conference.pdf), [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf))
> The capacity of a model to process, integrate, and reason about information from multiple modalities, such as text and images, to perform complex tasks.

**X-modal reasoning** (1 paper: [LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf))
> The ability of a model to reason and perform tasks that involve integrating information from multiple, different modalities, such as text, image, video, and audio.

**Cross-modal consistency reasoning** (1 paper: [MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf))
> The latent ability to judge the semantic alignment and consistency between textual and visual modalities.

**Audio-visual reasoning** (1 paper: [video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25x/sun25x.pdf))
> The model's ability to perform logical inference by integrating and jointly processing information from both auditory and visual streams in a video.

**Contrastive cross-modal reasoning** (1 paper: [Contra4: Evaluating Contrastive Cross-Modal Reasoning in Audio, Video, Image, and 3D](https://aclanthology.org/2025.emnlp-main.1288.pdf))
> The ability to reason contrastively across multiple modalities to select the one that best satisfies a natural language prompt.

**Image understanding and reasoning** (1 paper: [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf))
> Producing responses that demonstrate comprehension and logical inference based on visual inputs, such as diagrams or scenes.

**Content reasoning** (1 paper: [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf))
> The model's ability to perform logical inference based on the visual and textual content provided.

## Relationships

### Multimodal reasoning →
- **MMMU** (measurement instrument): *measured_by*, 2 papers
  > “On more complex multimodal reasoning benchmarks, the MINT-1T model outperforms OBELICS on MMMU but performs worse on Mantis-Eval.”
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf)
- **MMBench** (measurement instrument): *measured_by*, 2 papers
  > LLaMA-Adapter showcases higher tuning efficiency with competitive reasoning capacity on MME (Fu et al., 2023), MMBench (Liu et al., 2023c), and LVLM-eHub (Xu et al., 2023) benchmarks. (Section 1)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 2 papers
  > “We directly utilize ScienceQA’s multi-modal training set to fine-tune LLaMA-Adapter, and conduct in-domain testing.”
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **MathVista** (measurement instrument): *measured_by*, 2 papers
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [Progressive Multimodal Reasoning via Active Retrieval](https://aclanthology.org/2025.acl-long.180.pdf)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > LLaMA-Adapter showcases higher tuning efficiency with competitive reasoning capacity on MME (Fu et al., 2023), MMBench (Liu et al., 2023c), and LVLM-eHub (Xu et al., 2023) benchmarks. (Section 1)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **MM-NIAH** (measurement instrument): *measured_by*, 1 paper
  > Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SQA** (measurement instrument): *measured_by*, 1 paper
  > We conduct extensive experiments on multiple challenging tasks such as arithmetic, knowledge reasoning, and multimodal benchmarks spanning GSM8K, MMLU, SQA, and VQA (Abstract).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > We conduct extensive experiments on multiple challenging tasks such as arithmetic, knowledge reasoning, and multimodal benchmarks spanning GSM8K, MMLU, SQA, and VQA (Abstract).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Mantis-Eval** (measurement instrument): *measured_by*, 1 paper
  > “On more complex multimodal reasoning benchmarks, the MINT-1T model outperforms OBELICS on MMMU but performs worse on Mantis-Eval.”
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ChartMimic** (measurement instrument): *measured_by*, 1 paper
  > ChartMimic places emphasis on evaluating LMMs’ capacity to harmonize a blend of cognitive capabilities, encompassing visual understanding, code generation, and cross-modal reasoning. (Abstract)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **WE-MATH** (measurement instrument): *measured_by*, 1 paper
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [Progressive Multimodal Reasoning via Active Retrieval](https://aclanthology.org/2025.acl-long.180.pdf)
- **Visual grounding** (construct): *causes*, 1 paper
  > RSVP employs multimodal chain-of-thought visual prompts to help MLLMs understand queries and infer targets, generating interpretable region proposals that enhance visual grounding. (Abstract)
  - [RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought](https://aclanthology.org/2025.acl-long.715.pdf)
- **MMMU-Pro** (measurement instrument): *measured_by*, 1 paper
  > MMMU-Pro is designed to more accurately and rigorously assess a model’s true multimodal understanding and reasoning capabilities across a wide range of academic disciplines. (Section 1)
  - [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://aclanthology.org/2025.acl-long.736.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > MVoT demonstrates comparable performance on MAZE (92.95%) and MINIBEHAVIOR (95.14%), while achieving a higher accuracy of 85.60% on FROZENLAKE compared to both Direct and CoT. This demonstrates better stability and robustness of MVoT than CoT.
  - [Imagine While Reasoning in Space: Multimodal Visualization-of-Thought](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cz/li25cz.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > To further investigate how well M-STAR generalizes to multiple benchmarks, we select four extra multi-modal ones focus on reasoning as well: M3CoT (Chen et al., 2024b), MMStar (Chen et al., 2024a), MMBench (Dev set, v1.1) (Liu et al., 2025), AI2D (Kembhavi et al., 2016). (Section 4.2)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **AI2D** (measurement instrument): *measured_by*, 1 paper
  > To further investigate how well M-STAR generalizes to multiple benchmarks, we select four extra multi-modal ones focus on reasoning as well: M3CoT (Chen et al., 2024b), MMStar (Chen et al., 2024a), MMBench (Dev set, v1.1) (Liu et al., 2025), AI2D (Kembhavi et al., 2016). (Section 4.2)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **GQA** (measurement instrument): *measured_by*, 1 paper
  > ...and a multimodal experiment using GQA (Hudson and Manning, 2019) and the image-based subset of ScienceQA (Lu et al., 2022).
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)

### → Multimodal reasoning
- **Visual understanding** (construct): *causes*, 1 paper
  > the enhanced visual comprehension ability directly benefits the model performance and its multimodal reasoning ability. (Section 4)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > Large vision-language models (LVLMs) [31, 53] have achieved outstanding performance in a large number of multi-modal reasoning tasks such as visual question answering [45, 28], embodied instruction following [1] and robot navigation [2, 16], which are benefited from numerous network parameters and vast training data. (Section 1)
  - [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf)
- **Text-to-speech synthesis** (behavioral indicator), 1 paper
  > We also note that the generated audio appears different from all context audio samples, demonstrating the cross-modal reasoning capability of LLMs when using the LLM-Codec as the connector for text and audio. (Section 5.2)
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)
- **Object counting** (behavioral indicator), 1 paper
  > We also show some multi-modal reasoning examples in Figure 6. Our approach exhibits better object counting, OCR, and commence reasoning performance. (Section 4.2)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Optical character recognition** (behavioral indicator), 1 paper
  > We also show some multi-modal reasoning examples in Figure 6. Our approach exhibits better object counting, OCR, and commence reasoning performance. (Section 4.2)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Commonsense reasoning** (construct), 1 paper
  > We also show some multi-modal reasoning examples in Figure 6. Our approach exhibits better object counting, OCR, and commence reasoning performance. (Section 4.2)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
