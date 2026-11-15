# Visual reasoning
**Type:** Construct  
**Supporting papers:** 64  
**Also known as:** Visual-Linguistic Reasoning, Visual thinking, Limited cognitive ability  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats visual reasoning as a latent capacity to understand visual inputs and draw new inferences from them, often by combining perceptual cues with multi-step symbolic, compositional, or otherwise high-level reasoning. Many definitions broaden the scope to multimodal settings, where models reason over visual and textual information together, resolve ambiguity for language tasks, or answer questions from charts, tables, diagrams, and videos. Smaller lines of work rename nearby variants as visual-linguistic reasoning or visual thinking, the latter emphasizing image-based internal representations during reasoning, while one paper frames failure as a limited cognitive ability in which a response is hallucinated despite accurate perception.

**Space of facets.** When papers break the construct down, they most explicitly treat visual reasoning as including spatial, temporal, predictive, causal, and counterfactual forms. Other papers align it with broader cognitive abilities or with "conceptualization" and conceptual abstraction, especially for abstract or structured graphics to be solved "using only visual reasoning and conceptual abstraction, without relying on algorithmic computation." Naming is not uniform: visual-linguistic reasoning usually marks joint image-text reasoning, whereas visual thinking refers to reasoning that proceeds with generated visualizations of the reasoning trace.

**Space of measurement.** Operationalization is dominated by benchmark evaluation: papers link visual reasoning to 15 measurement instruments and 2 behavioral indicators. The most frequently linked instruments are MMMU, GQA, ACRE, AI2D, and ChartQA, and the linked instruments are benchmark datasets, for example MMMU is described as involving complex visual reasoning across multidisciplinary domains, while other papers use datasets said to test general visual reasoning or diverse visual reasoning tasks. The two linked behavioral indicators, hallucination and visual editing, appear in causal claims rather than as standalone instruments. Overall, the measures line up with the broad framing of drawing inferences from visual inputs more than with the internal-visualization emphasis of visual thinking.

**Links.** Beyond measurement, relational claims are varied and usually isolated to single papers. One paper claims a causal relationship from Grounding to visual reasoning, saying many video problems require grounding in fine-grained low-level information, and another claims a causal relationship from Visual editing to visual reasoning by providing an intermediate interface to facilitate it; a separate paper claims a causal relationship from visual reasoning to Hallucination, arguing that overlooking intermediate visual reasoning can lead to hallucinations. Papers also report that Calibration correlates with visual reasoning, and that Safety alignment, Visual grounding, Spatial reasoning, Temporal reasoning, Causal reasoning, and Counterfactual reasoning are related to it; the safety link is described as a trade-off, and visual grounding as a low-level foundation for higher-level reasoning.

## Sources

**Visual reasoning** (11 papers: [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf), [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf), [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.324.pdf), [TurtleBench: A Visual Programming Benchmark in Turtle Geometry](https://aclanthology.org/2025.naacl-long.607.pdf), [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf), [Detect, Disambiguate, and Translate: On-Demand Visual Reasoning for Multimodal Machine Translation with Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.74.pdf), [VReST: Enhancing Reasoning in Large Vision-Language Models through Tree Search and Self-Reward Mechanism](https://aclanthology.org/2025.acl-long.199.pdf), [Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/babaiee25a/babaiee25a.pdf), [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf))
> The capacity to draw inferences from visual inputs by combining perceptual cues with multi-step symbolic or compositional reasoning.

**Visual-Linguistic Reasoning** (1 paper: [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf))
> The latent ability to process and reason about combined visual and textual information to derive answers or descriptions.

**Visual thinking** (1 paper: [Imagine While Reasoning in Space: Multimodal Visualization-of-Thought](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cz/li25cz.pdf))
> The capacity to reason using image-based internal representations or visualizations in addition to text.

**Limited cognitive ability** (1 paper: [Is Cognition Consistent with Perception? Assessing and Mitigating Multimodal Knowledge Conflicts in Document Understanding](https://aclanthology.org/2025.emnlp-main.1574.pdf))
> A constraint in the model’s capacity to correctly comprehend or reason about visual content, leading to hallucinated or incorrect cognitive responses despite accurate perception.

## Relationships

### Visual reasoning →
- **MMMU** (measurement instrument): *measured_by*, 3 papers
  > Additionally, the challenging MMMU [68] is evaluated to assess the visual reasoning abilities of the multimodal LLMs. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)
- **GQA** (measurement instrument): *measured_by*, 2 papers
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
  - [ModalPrompt: Towards Efficient Multimodal Continual Instruction Tuning with Dual-Modality Guided Prompt](https://aclanthology.org/2025.emnlp-main.609.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **MathVista** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **ACRE** (measurement instrument): *measured_by*, 1 paper
  > We demonstrate the effectiveness of our framework on diverse visual reasoning tasks from the ACRE, CATER, Something-Else and STAR datasets (Abstract).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **STAR** (measurement instrument): *measured_by*, 1 paper
  > We demonstrate the effectiveness of our framework on diverse visual reasoning tasks from the ACRE, CATER, Something-Else and STAR datasets (Abstract).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > VQAv2 Goyal et al. (2017) and VizWiz Gurari et al. (2018) test general visual reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 1 paper
  > VQAv2 Goyal et al. (2017) and VizWiz Gurari et al. (2018) test general visual reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **AI2D** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **ChartQA** (measurement instrument): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > existing tuning methods train models to provide conclusive responses to instructions based on visual inputs, causing them to overlook essential intermediate visual reasoning. This often leads to ... even generating hallucinations. (Section 1)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **NLVR2** (measurement instrument): *measured_by*, 1 paper
  > The experiments were conducted on four image-text tasks: VQAv2 (Goyal et al., 2017b), GQA (Hudson & Manning, 2019) for vision question-answering, NLVR2 (Suhr et al., 2019) for visual reasoning, MSCOCO (Chen et al., 2015) for image captioning
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > ...we evaluate the proposed Image-DPO algorithm across three VLM models... using several popular VLM benchmarks that focus on different aspects, including... general visual reasoning (MM-Vet (Yu et al., 2023c))... (Section 5.1)
  - [Probing Visual Language Priors in VLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25b/luo25b.pdf)

### → Visual reasoning
- **Grounding** (construct): *causes*, 1 paper
  > many visual reasoning problems in videos require grounding in fine-grained low-level information (Section 1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **Visual editing** (behavioral indicator): *causes*, 1 paper
  > REFOCUS conducts visual editing on input images as a chain-of-thought, providing an intermediate interface for multimodal LLMs to facilitate visual reasoning and enforce the correct answer with a valid reasoning process. (Section 3. REFOCUS)
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)
- **Calibration** (construct): *correlates*, 1 paper
  > "visual reasoning models (i.e., thinking with images) consistently exhibit better calibration"
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)

### Associated with
- **Spatial reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Temporal reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Causal reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Counterfactual reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety alignment** (construct), 1 paper
  > This observation highlights a fundamental trade-off: as visual reasoning capabilities increase, safety alignment tends to degrade. (Section 1)
  - [VisCRA: A Visual Chain Reasoning Attack for Jailbreaking Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.312.pdf)
- **Visual grounding** (construct), 1 paper
  > it’s essential for the LLM to possess high-level, in-depth vision reasoning capabilities, building upon the foundational low-level pixel grounding.
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
