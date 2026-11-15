# Visual grounding
**Type:** Construct  
**Supporting papers:** 77  
**Also known as:** Multimodal grounding, Shape grounding, Region-text alignment, Grounding ability, Grounding capability, Visual localization, Grounded understanding, Region understanding, Referring expression comprehension, Referring ability  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage treats visual grounding as a latent ability to connect language, such as phrases, referring expressions, or instructions, to specific visual regions, objects, locations, or object states in an image or environment. Many definitions stay close to localization, including matching text to image regions, identifying the instance described by a referring expression, or producing coordinates or bounding boxes for GUI elements; in embodied settings, one paper describes this as the agent being "fully aware of object locations in the scene." A smaller line of work broadens the term to grounding generated answers or multi-step reasoning in image evidence, sometimes emphasizing that outputs should be anchored in the actual image rather than hallucinated or text-derived assumptions. The main variation is between a model-level latent ability and an observable output, and between narrow referential localization and broader grounding of reasoning or responses.

**Space of facets.** Papers use several nearby names for overlapping ideas, including multimodal grounding, spatial understanding, region-text alignment, visual localization, grounded understanding, grounding ability or capability, region understanding, and referring ability or referring expression comprehension. Some papers treat it as an umbrella over phrase grounding and referring expression comprehension, while others use it almost interchangeably with referring expression comprehension or present it as the counterpart of region captioning. Other variants narrow the target domain, such as shape grounding in diagrams, locating ROIs in medical images, grounding GUI elements from screenshots, and locating objects in 3D scenes.

**Space of measurement.** Operationalization is benchmark-centered: papers link the construct to 7 measurement instruments and 13 behavioral indicators. The most common instruments are RefCOCO, RefCOCO+, RefCOCOg, ScreenSpot, and MMStar, plus 2 other instruments; papers use the RefCOCO series to localize image regions for referring expressions, ScreenSpot to map GUI instructions to target element boxes, and some tasks require models to "explicitly ground objects in images by generating coordinates." These measures mostly line up with the dominant definitions by testing region, box, coordinate, mask, or patch-level localization, though some benchmarks are cited more broadly as requiring better visual grounding rather than as direct grounding tasks.

**Links.** No correlational link is reported. Beyond measurement, papers connect visual grounding to 13 behavioral indicators and 5 constructs. Recurring named links include hallucination, referring expression understanding, GUI automation, instruction following, and chain-of-thought reasoning: papers relate visual grounding to referring expression understanding and chain-of-thought reasoning, one paper claims a causal relationship from visual grounding to GUI automation, another claims a causal relationship from instruction following to visual grounding, and work on hallucination describes hallucinated responses as visually ungrounded, with one paper identifying inability to accurately ground images as a cause of hallucinations. Papers report 13 other linked behaviors and constructs as well, including additional causal links in both directions.

## Sources

**Multimodal grounding** (1 paper: [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf))
> The latent ability of a model to associate textual descriptions, such as phrases or referring expressions, with their corresponding spatial regions in an image.

**Visual grounding** (10 papers: [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf), [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf), [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587.pdf), [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89.pdf), [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://aclanthology.org/2025.naacl-long.488.pdf), [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf), [Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning](https://aclanthology.org/2025.acl-long.257.pdf), [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf), [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> The ability to use scene information to connect language instructions with visible objects and their states in the environment.

**Spatial understanding** (1 paper: [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf))
> The latent ability to align visual regions with semantic descriptions, enabling both comprehension of spatial references and localization of described content.

**Shape grounding** (1 paper: [Primitive Vision: Improving Diagram Understanding in MLLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25n/zhang25n.pdf))
> The alignment of detected shapes in a diagram (e.g., circle, rectangle) with their semantic labels and spatial locations.

**Region-text alignment** (1 paper: [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf))
> The model's ability to match textual descriptions with specific image regions, demonstrated through contrastive learning on region-caption pairs.

**Grounding ability** (2 papers: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf), [GUICourse: From General Vision Language Model to Versatile GUI Agent](https://aclanthology.org/2025.acl-long.1065.pdf))
> The capacity to produce precise spatial outputs for GUI elements, such as coordinates or bounding boxes, from screenshots.

**Grounding capability** (2 papers: [Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf), [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> The latent ability to accurately associate textual references with specific visual locations or bounding boxes in a UI.

**Visual localization** (1 paper: [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf))
> The latent ability to identify where in an image the relevant subject or evidence for a question is located.

**Grounded understanding** (1 paper: [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf))
> The ability to connect language expressions to specific image regions or objects with precise spatial localization.

**Region understanding** (1 paper: [CPCF: A Cross-Prompt Contrastive Framework for Referring Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25h/zhu25h.pdf))
> The latent ability of a referring MLLM to accurately interpret and generate responses based on a specific visual region indicated by a prompt, distinguishing it from surrounding or similar regions.

**Referring expression comprehension** (1 paper: [A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f0cd0305f7741659304f5325f3bf6d-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent ability to identify the specific visual instance described by a natural-language referring expression.

**Referring ability** (1 paper: [ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4fd96b997454b5b02698595df70fccaf-Paper-Conference.pdf))
> The latent capability of a multimodal model to understand and ground its responses in specific spatial regions of an image indicated by visual prompts like boxes, masks, scribbles, or points.

## Relationships

### Visual grounding →
- **RefCOCO** (measurement instrument): *measured_by*, 9 papers
  > Visual Grounding. Visual grounding involves a set of tasks that establish referential links between textual mentions in a sentence and specific regions in an image. We evaluate our model on the typical datasets, including Visual7w [Zhu et al., 2016], RefCOCO [Liu et al., 2017], RefCOCO+, and RefCOCOg to ensure completeness. (Section 3)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
  - [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf)
- **RefCOCOg** (measurement instrument): *measured_by*, 3 papers
  > For visual grounding, we use RefCOCO, RefCCO+ and RefCOCOg [62]. (Section 4.1)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **RefCOCO+** (measurement instrument): *measured_by*, 3 papers
  > For visual grounding, we use RefCOCO, RefCCO+ and RefCOCOg [62]. (Section 4.1)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 3 papers
  > Several causes of hallucinations have been identified including biased training data (Liu et al., 2023), the inability of vision encoders to accurately ground images (Jain et al., 2024), misalignment among different modalities (Liu et al., 2024b), and insufficient context attention in LLM decoders (Huang et al., 2024; Liu et al., 2024d). (Section 2.2)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
- **ScreenSpot** (measurement instrument): *measured_by*, 2 papers
  > First, ScreenSpot (Cheng et al., 2024) provides a GUI visual grounding benchmark containing 1,200 instructions with target element bounding boxes across mobile, desktop, and web environments. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
  - [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf)
- **Multimodal understanding** (construct): *causes*, 1 paper
  > visual grounding is crucial for robust multimodal understanding. (Section 1)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > the vision-disabled performance on benchmarks like MMVP is notably worse than random guessing, suggesting that strong visual grounding is particularly crucial. (Section 2.1)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Visual7W** (measurement instrument): *measured_by*, 1 paper
  > Visual Grounding. Visual grounding involves a set of tasks that establish referential links between textual mentions in a sentence and specific regions in an image. We evaluate our model on the typical datasets, including Visual7w [Zhu et al., 2016], RefCOCO [Liu et al., 2017], RefCOCO+, and RefCOCOg to ensure completeness. (Section 3)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > “MMStar [8] is a vision-indispensible benchmark, which requires better visual grounding in trained LVLMs.”
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **GUI automation** (behavioral indicator): *causes*, 1 paper
  > In this paper, we advocate a human-like embodiment for GUI agents that perceive the environment entirely visually and directly perform pixel-level operations on the GUI. The key is visual grounding models that can accurately map diverse referring expressions of GUI elements to their coordinates on the GUI across different platforms. (ABSTRACT)
  - [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf)

### → Visual grounding
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > “These results emphasize the superiority of Text4Seg in following instructions, leading to enhanced visual grounding ability.”
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Multimodal reasoning** (construct): *causes*, 1 paper
  > RSVP employs multimodal chain-of-thought visual prompts to help MLLMs understand queries and infer targets, generating interpretable region proposals that enhance visual grounding. (Abstract)
  - [RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought](https://aclanthology.org/2025.acl-long.715.pdf)
- **Visual editing** (behavioral indicator): *causes*, 1 paper
  > The Set-of-Mark study (Yang et al., 2023) extends this investigation by demonstrating that segmenting the original image can significantly enhance the visual grounding capabilities of GPT-4v models. (Section 2. Related Works)
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)

### Associated with
- **Referring expression understanding** (behavioral indicator), 2 papers
  > For tasks that focus on visual grounding ability like REC [42], and REG [37], the model uses more DINO features to perceive region-level visual information. (Section 4.1)
  - [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Referring expression generation** (behavioral indicator), 1 paper
  > In order to endow our model with consistent, interactive visual grounding capabilities, we collect a high-quality dataset covering 4 types of grounding data: ... (2) Referring Expression Generation (REG)... (Section 2.3)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
- **Object detection** (behavioral indicator), 1 paper
  > This demonstrates that object detection and visual grounding can benefit from each other. (Section 4.3)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Visual recognition** (construct), 1 paper
  > A mainstream of Multi-modal Large Language Models (MLLMs) have two essential functions, i.e., visual recognition (e.g., grounding) and understanding (e.g., visual question answering). (Abstract)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator), 1 paper
  > Several recent works have explored ways to improve the visual localization capability of MLLMs for visual question answering, including chain-of-thought (Shao et al., 2024; Liu et al., 2024b), tool-using (Wu and Xie, 2023), and visual programming approaches (Surís et al., 2023; Gupta and Kembhavi, 2023). (Sec. 2)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **Referring expression segmentation** (behavioral indicator), 1 paper
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Open-vocabulary semantic segmentation** (behavioral indicator), 1 paper
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Region captioning** (behavioral indicator), 1 paper
  > Next, we study visual grounding, a.k.a. referring expression comprehension (REC), the counterpart task to visual referring that requires the model to identify the location of an object with language descriptions.
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
- **Object localization** (behavioral indicator), 1 paper
  > a grounding module (Gaze) provides precise visual focus by predicting bounding box annotations. (Section 1)
  - [Taking Notes Brings Focus? Towards Multi-Turn Multimodal Dialogue Learning](https://aclanthology.org/2025.emnlp-main.1690.pdf)
- **Visual reasoning** (construct), 1 paper
  > it’s essential for the LLM to possess high-level, in-depth vision reasoning capabilities, building upon the foundational low-level pixel grounding.
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Robotic manipulation** (behavioral indicator), 1 paper
  > The strong task instruction understanding and visual grounding capabilities of MLLMs [5, 4] have exhibited great promise for language-instructed multitask robotic manipulation [7, 8, 9].
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > it is crucial to ground the reasoning process to the visual information and VoCoT is the most suitable format (Section 4.3).
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
