# MathVista
**Type:** Measurement instrument  
**Supporting papers:** 71  
**Also known as:** MATHVISTA  

## State of the Field

**What it is.** Across papers, MathVista is most commonly described as a benchmark for mathematical reasoning in visual or multimodal contexts. Definitions emphasize puzzles or math problems that involve images and joint mathematical and visual understanding, often broken down by reasoning type and image context. Some authors describe or use it through the geometry problem solving task, especially the testmini split, while a smaller line of work presents it as a broader benchmark that also includes general visual question answering tasks and questions outside traditional mathematics.

**What it is claimed to measure.** Papers use it to measure 7 constructs and 2 behavioral indicators. The prevailing usage is mathematical reasoning, often phrased as math reasoning with visual information or visual mathematical reasoning. Other recurring claims are broader reasoning, geometric reasoning, multimodal reasoning, and visual question answering, with 3 other constructs and 1 other behavioral indicator also linked to it. Overall, the claims center on mathematical reasoning but spread across several other reported targets.

**Space of uses.** Papers usually position it as one benchmark within a larger evaluation suite, though some use a focused subset, especially the geometry problem solving task or the testmini split, and one study uses testmini as an out-of-domain testset. It appears alongside GeoQA, MathVision, WE-MATH, and MathVerse in comparative evaluation, and one paper uses it as a data source for MMEVALPRO.

## Sources

**MATHVISTA** (1 paper: [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for mathematical reasoning in LVLMs that involves puzzles with images and categorizes problems by reasoning type and image context.

**MathVista** (6 papers: [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf))
> A benchmark for evaluating mathematical reasoning capabilities of large models, which includes a specific task for geometry problem solving.

## Relationships

### → MathVista
- **Mathematical reasoning** (construct): *measured_by*, 10 papers
  > In this paper, we present MATHVISTA, a consolidated Mathematical reasoning benchmark in Visual contexts. (Section 1)
  - [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf)
  - [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
  - [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf)
- **Reasoning** (construct): *measured_by*, 3 papers
  > For general reasoning, benchmarks like MathVista [31] and MMMU [32] assess models on tasks involving multiple-choice and free-form questions, with a focus on multimodal data.
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 3 papers
  > In this section, we present the experiment results of STIC across seven visual question answering (VQA) benchmarks. We consider the widely used benchmarks for LVLM evaluation across different domains including: ScienceQA... TextVQA... ChartQA... LLaVA-Bench... MMBench... MM-Vet... and MathVista
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Redundancy Principles for MLLMs Benchmarks](https://aclanthology.org/2025.acl-long.612.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Geometric reasoning** (construct): *measured_by*, 2 papers
  > "We evaluate G-LLaVA on the geometry problems solving (GPS) task (testmini split) of MathVista"
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
  - [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 2 papers
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [Progressive Multimodal Reasoning via Active Retrieval](https://aclanthology.org/2025.acl-long.180.pdf)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **Visual reasoning** (construct): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Chart and diagram understanding** (behavioral indicator): *measured_by*, 1 paper
  > Many benchmarks in the popular MathVista evaluation suite [60] are designed to test chart understanding. (Sec 1)
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Calibration** (construct): *measured_by*, 1 paper
  > To evaluate calibration under visual mathematical reasoning, we employ MathVista (Lu et al., 2024) and MathVision (Wang et al., 2024). (Section 3.1.1)
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)
