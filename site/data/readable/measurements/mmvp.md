# MMVP
**Type:** Measurement instrument  
**Supporting papers:** 18  

## State of the Field

**What it is.** Across papers, MMVP is most commonly described as a fine-grained visual benchmark built from visually similar, CLIP-blind image pairs. Definitions say it evaluates visual details or fine-grained visual recognition, with one paper stating that it "collects CLIP-blind pairs" and contains "150 image pairs, each accompanied by a binary-option question," another describing paired classification over 9 visual patterns, and another referring to MMVP(-VLM) for testing object existence, orientation, and counting. A smaller line of work instead places it under single-image VQA, treats it as a multi-image benchmark for image-caption alignment, or describes it as exposing the visual shortcomings of CLIP-based multimodal models.

**What it is claimed to measure.** Papers use MMVP to measure 8 constructs and 2 behavioral indicators, which places it across several nearby targets rather than only one. The most recurrent links frame it as measuring visual understanding, compositional reasoning, and fine-grained perception, while behavioral-indicator uses include fine-grained visual recognition and visual question answering, with 5 other construct-level targets also linked. Overall, papers describe these measurement claims in terms of visual or multimodal perception and understanding.

**Space of uses.** Papers do not link MMVP to another measurement instrument directly, but they usually place it inside broader evaluation suites. It appears alongside MMBench, MME, RealWorldQA, CV-Bench2D, and CV-Bench3D, and papers variously position it as a vision-centric benchmark, a perception benchmark, or part of general VQA and multimodal understanding evaluations. Some method papers also single it out as a challenging fine-grained check when testing whether models can distinguish similar images or capture visual details.

**Concerns raised.** Only limited concerns are explicit. One paper notes that MMVP was "not in paired image-text format" for its evaluation and says it manually converted the benchmark without altering content, and another paper presents a newer benchmark as surpassing the scale of MMVP.

## Sources

**MMVP** (9 papers: [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf), [Exploring How Generative MLLMs Perceive More Than CLIP with the Same Vision Encoder](https://aclanthology.org/2025.acl-long.499.pdf), [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf), [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf), [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf), [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e69ff56d0ebff0752ff29caaddc25dd-Paper-Datasets_and_Benchmarks_Track.pdf), [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf), [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf))
> A benchmark that evaluates the fine-grained visual recognition capabilities of LVLMs using pairs of visually similar (CLIP-blind) images, each with a binary-option question.

## Relationships

### → MMVP
- **Visual understanding** (construct): *measured_by*, 3 papers
  > MMVP [53] aims to evaluate the understanding of visual details for 9 different visual patterns using paired classification accuracy. (Section 4)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **Visual grounding** (construct): *measured_by*, 1 paper
  > the vision-disabled performance on benchmarks like MMVP is notably worse than random guessing, suggesting that strong visual grounding is particularly crucial. (Section 2.1)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Compositional reasoning** (construct): *measured_by*, 1 paper
  > Fine-tuning on this data enhances the model’s ability to distinguish between similar images, showing improvements on challenging benchmarks like Winoground, MMVP, and EQBEN, which test compositional reasoning and fine-grained understanding. (Section 6.1)
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Visual perception** (construct): *measured_by*, 1 paper
  > We conducted extensive evaluations of DEEM on RobustVQA and two widely recognized benchmarks, POPE and MMVP, for visual hallucination and perception respectively (Section 1).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Fine-grained visual recognition** (behavioral indicator): *measured_by*, 1 paper
  > MMVP (Tong et al., 2024) collects CLIP-blind pairs and evaluates the fine-grained visual recognition capabilities of LVLMs (Section 4.1).
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
- **Fine-grained visual understanding** (construct): *measured_by*, 1 paper
  > We evaluate our each variant of ROSS mainly on ... (ii) fine-grained comprehension: MMVP (Tong et al., 2024b) and ChartQA (Masry et al., 2022) (Section 5.1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Fine-grained perception** (construct): *measured_by*, 1 paper
  > Among these benchmarks, MMVP mainly focuses on fine-grained perception. (Section 4.1)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > General VQA: Assessing visual perception and reasoning abilities through single-image question answering, including MMBench (Liu et al., 2025b), MME (Fu et al., 2023), and MMVP (Zhong et al., 2023). (Section 4.5).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
