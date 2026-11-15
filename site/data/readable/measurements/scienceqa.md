# ScienceQA
**Type:** Measurement instrument  
**Supporting papers:** 78  
**Also known as:** SCIENCEQA, Science-QA  

## State of the Field

**What it is.** Across papers, ScienceQA is most commonly described as a multiple-choice science question answering benchmark, usually multimodal, spanning diverse science topics or knowledge domains. The prevailing descriptions say samples pair a question and options with visual and textual context, and some definitions add optional lecture or context text, background knowledge, and explanations; a smaller line of work narrows evaluation to questions with images or refers to image-based forms such as ScienceQA-Image, while some work also uses text-only samples. Papers also describe it as covering science questions with diagrams and as a benchmark for scientific or complex reasoning from visual and textual inputs.

**What it is claimed to measure.** Papers use ScienceQA to measure 10 constructs and 3 behavioral indicators, so its use is spread across several framings rather than centered on one. The most frequent construct claims treat it as measuring multimodal reasoning and scientific reasoning, followed by knowledge reasoning, multimodal perception, and multimodal understanding, with 5 other constructs also linked. At the behavioral-indicator level, the clearest recurring use is visual question answering, with 2 other behavioral indicators also linked: question answering and scientific question answering.

**Space of uses.** No measurement instrument is linked to it. In practice, papers often place ScienceQA inside broader evaluation suites alongside VQAv2, GQA, TextVQA, MMBench, and POPE, and they position it variously as a VQA benchmark, a downstream dataset, an in-domain fine-tuning and test set, or a source benchmark for MMEVALPRO. Some papers evaluate specific subsets, including image-based versions and text-only samples.

## Sources

**ScienceQA** (9 papers: [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [Error-driven Data-efficient Large Multimodal Model Tuning](https://aclanthology.org/2025.acl-long.992.pdf), [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf), [The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations](https://aclanthology.org/2025.emnlp-main.61.pdf))
> Multiple-choice question answering benchmark assessing scientific reasoning across diverse domains.

**SCIENCEQA** (1 paper: [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf))
> A science question-answering benchmark with multiple-choice questions, some accompanied by images and optional lecture/context text.

**Science-QA** (1 paper: [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf))
> A multimodal science question answering benchmark that evaluates science-related reasoning from visual and textual inputs.

## Relationships

### → ScienceQA
- **Visual question answering** (behavioral indicator): *measured_by*, 12 papers
  > we perform Visual Question Answering (VQA) on ScienceQA (Lu et al., 2022) (Section 4.1)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [GraphVis: Boosting LLMs with Visual Knowledge Graph Integration](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cb04f510593c9ba30da398f5e0a7e7b-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
  - [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf)
- **Scientific reasoning** (construct): *measured_by*, 2 papers
  > We use the ScienceQA dataset (Lu et al., 2022) to evaluate the scientific reasoning ability of the model. (Section 3.1)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 2 papers
  > “We directly utilize ScienceQA’s multi-modal training set to fine-tune LLaMA-Adapter, and conduct in-domain testing.”
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > Question Answering. For ScienceQA (Lu et al., 2022b), we gather text-only samples to form a train and test set with 6,508 and 2,224 samples. (Section 4.1).
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
- **Scientific question answering** (behavioral indicator): *measured_by*, 2 papers
  > ScienceQA with multiple choice are used to evaluate the zero-shot generalization on scientific question answering. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > ScienceQA with multiple choice are used to evaluate the zero-shot generalization on scientific question answering. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Knowledge reasoning** (construct): *measured_by*, 1 paper
  > We employ the ScienceQA [28] dataset for the knowledge reasoning task (Section 5.1.1).
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **Visual perception** (construct): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual reasoning** (construct): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Scientific knowledge** (construct): *measured_by*, 1 paper
  > ScienceQA (Lu et al., 2022b) is utilized to measure scientific knowledge. (Section 4.1)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > To validate the effectiveness of our proposed method, we conduct extensive experiments across multiple reasoning VQA datasets, including ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), and MathV (Wang et al., 2024a). (Section 1)
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
