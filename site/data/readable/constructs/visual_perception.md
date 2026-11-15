# Visual perception
**Type:** Construct  
**Supporting papers:** 81  
**Also known as:** Vision perception, Perception, Perception capability, Perceptual capability, Sensation, Perception ability, Perceptual understanding  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats visual perception as a latent model ability to process, extract, and interpret visual information from images or other visual inputs. Most definitions center on understanding objects, scenes, text, spatial relations, or structures needed for downstream tasks, and several papers describe it as a foundational capability. A smaller line of work narrows the construct to particular settings such as charts, document screenshots, GUI screenshots, videos, or agricultural images, and one paper shifts the emphasis from model ability to the quality of visual input interpretation, saying it is influenced by resolution, keyframe granularity, and visual encoding.

**Space of facets.** Papers also use neighboring labels such as perception, perception capability, sensation, and perceptual understanding for closely related framings of interpreting visual input. Some works split it into basic details such as count, color, OCR, and scene categories, while chart-focused work distinguishes compositional, color, and spatial perception errors. Other papers contrast it with visual recognition by saying perception also contextualizes what is seen, and some benchmarks place it alongside reasoning or generation as a separate competency.

**Space of measurement.** Operationalization is mainly benchmark-based: papers link visual perception to 14 measurement instruments and 11 behavioral indicators, with MME, GQA, and VQA-v2 appearing most often. Papers describe MME as measuring perception with yes or no questions, while GQA and VQA-v2 assess it through open-ended short answers, and one paper explicitly treats VQA accuracy as a proxy for perception capability. The most recurrent behavioral indicators are visual question answering and image captioning, so measurement usually targets answering questions about images or describing them, which tracks the common definitions focused on extracting and interpreting visual information, even though some definitions narrow the construct to specific domains.

**Links.** Papers link visual perception to 12 constructs and 11 behavioral indicators. The most recurrent construct-level claim is a causal relationship from multimodal alignment to visual perception, with visual-language misalignment said to hinder perception and text alignment said to enhance it. Several papers also report a related link from reasoning to visual perception, with one noting that reasoning benchmarks require a foundational perception capability, while smaller lines of work claim causal relationships from visual perception to abstract visual reasoning and to hallucination. Another reported related link is from cognition to visual perception.

## Sources

**Visual perception** (8 papers: [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf), [MultiChartQA: Benchmarking Vision-Language Models on Multi-Chart Problems](https://aclanthology.org/2025.naacl-long.566.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [Movie101v2: Improved Movie Narration Benchmark](https://aclanthology.org/2025.acl-long.836.pdf), [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf), [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf))
> The latent ability to accurately interpret and understand visual information such as diagrams, charts, plots, and natural images, especially in the context of mathematical reasoning.

**Vision perception** (1 paper: [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf))
> The latent quality of visual input interpretation, influenced by resolution, keyframe granularity, and visual encoding.

**Perception** (7 papers: [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf), [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf), [Agri-CM3: A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning](https://aclanthology.org/2025.acl-long.576.pdf), [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf))
> The latent ability to extract and interpret visual information from images in order to support downstream multimodal tasks.

**Perception capability** (1 paper: [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf))
> The model's general ability to correctly interpret and understand visual information from an image.

**Perceptual capability** (1 paper: [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to extract and interpret visual information from document screenshots, including charts, images, and layout cues.

**Sensation** (1 paper: [Unveiling the Tapestry of Consistency in Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f094ba0f5ce1720466342f78031bdb-Paper-Conference.pdf))
> The fundamental capability of LVLMs to perceive basic visual details such as count, color, OCR, and scene categories.

**Perception ability** (1 paper: [Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf))
> The model's fundamental capability to interpret and understand visual information across various contexts, styles, and scenarios.

**Perceptual understanding** (1 paper: [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf))
> The latent ability to accurately interpret visual content and extract relevant properties from images.

## Relationships

### Visual perception →
- **MME** (measurement instrument): *measured_by*, 5 papers
  > MME benchmark measures both perception and cognition abilities on a total of 14 subtasks. (Section 4.2)
  - [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 3 papers
  > GQA and VQA-v2 evaluate the model’s visual perception capabilities on open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 3 papers
  > GQA and VQA-v2 evaluate the model’s visual perception capabilities on open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 2 papers
  > In contrast, for several benchmarks primarily targeting the visual perception skills of models, performance remains consistent when gradually reducing the number of visual tokens until a threshold is reached. Beyond this threshold, performance drops significantly (see Figure 5 and Appendix Figure 8). This “turning point" is observed in benchmarks such as MME Cognition, MME Perception, POPE, and MMMU.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 2 papers
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49], GQA [28], Vizwiz [22]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BLINK** (measurement instrument): *measured_by*, 2 papers
  > The perception-focused benchmarks include RealWorldQA, CV-Bench and BLINK (Section 4)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Visual hallucination** (behavioral indicator): *causes*, 2 papers
  > “Neglecting to fine-tune the projector can significantly impair the model’s visual perception capabilities. This deficiency may lead to visual hallucinations”
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49], GQA [28], Vizwiz [22], MMBench [48] and MMStar [8]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Creativity** (construct): *causes*, 1 paper
  > the weak perception of LVLMs inhibits authentic strengths in reasoning and creation. (Abstract).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Abstract visual reasoning** (construct): *causes*, 1 paper
  > A single error in visual feature perception can impact reasoning since the correct pattern must apply to all puzzle shapes. (Section 6)
  - [MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/529d8b3a23991e83db07f21727256374-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49], GQA [28], Vizwiz [22], MMBench [48]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Flickr30k** (measurement instrument): *measured_by*, 1 paper
  > “Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. VHELM uses scenarios such as Flickr-30k [46], VQAv2 [12], VizWiz [14] and POPE [23] to assess this aspect.”
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > We conducted extensive evaluations of DEEM on RobustVQA and two widely recognized benchmarks, POPE and MMVP, for visual hallucination and perception respectively (Section 1).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Optical character recognition** (behavioral indicator): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Document understanding** (construct): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **MNIST** (measurement instrument): *measured_by*, 1 paper
  > The perception capability is tested on CIFAR-10/100 (Krizhevsky et al., 2009) and MNIST (Deng, 2012). (Section 4.1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > The perception-focused benchmarks include RealWorldQA, CV-Bench and BLINK (Section 4)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)

### → Visual perception
- **Multimodal alignment** (construct): *causes*, 2 papers
  > This suggests a misalignment between its visual and language abilities, hindering complex board recognition. (Section 4.1)
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 3 papers
  > Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Reasoning** (construct), 2 papers
  > these reasoning benchmarks require a foundational perception capability to accurately identify key elements. (Section A.3)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Object detection** (behavioral indicator), 2 papers
  > SKETCHPAD can also use specialist vision models during the sketching process (e.g., draw bounding boxes with object detection models... to further enhance visual perception and reasoning.
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator), 2 papers
  > Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Is Your Multimodal Language Model Oversensitive to Safe Queries?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50d4f8ff0416cedfe0771b7ad947a197-Paper-Conference.pdf)
- **Object hallucination** (behavioral indicator), 1 paper
  > With CCA, visual tokens can better interact with instruction tokens, thereby enhancing model’s perception capability and alleviating object hallucination. (Abstract)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Cognition** (construct), 1 paper
  > cognition capabilities (integrating perceptual attributes and knowledge to deduce more complex answers) (Section 1).
  - [Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instance segmentation** (behavioral indicator), 1 paper
  > "Visual Perception covers a wide range of visual tasks, such as open-ended/closed-set object detection, instance segmentation, pose estimation, etc."
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Pose estimation** (behavioral indicator), 1 paper
  > "Visual Perception covers a wide range of visual tasks, such as open-ended/closed-set object detection, instance segmentation, pose estimation, etc."
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Visual recognition** (construct), 1 paper
  > Visual Perception (VP) extends beyond VR by interpreting and contextualizing these elements within the broader scene (Fu et al., 2024), essential for tasks requiring more than basic recognition. (Section 3)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Visual robustness** (construct), 1 paper
  > We explore the impact of diffusion feedback on the visual perception capabilities of LMMs from three dimensions: visual robustness, visual hallucinations, and basic visual perception (Section 3.2).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Memorization** (construct), 1 paper
  > It raises a critical concern: “Does the model genuinely perceive and understand the input, or is it merely memorizing it?” (Section 1)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **Factual retention** (construct), 1 paper
  > For factual retention, we further divide this category into four finer sub-categories: (1) Visual Perception (OCR, Spatial Reasoning), (2) Audio Perception, (3) Full Video Understanding (i.e., tasks that require information across several parts of the video), and (4) Temporal Reasoning (i.e., tasks that require understanding the video with respect to time).
  - [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)
- **Analogical reasoning** (construct), 1 paper
  > Analogical reasoning consists of diverse atomic abilities; perceptual understanding, mapping abstract relationships between visual contents (Gentner, 1983), and transferring relational patterns to novel cases. (Section 1)
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
- **Object recognition** (behavioral indicator), 1 paper
  > Perception MLLMs retrieve information from multimodal inputs, using skills like object recognition and OCR. (Table 3).
  - [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf)
- **Decision-making** (construct), 1 paper
  > Decision-making is a complex task requiring various abilities. Several common ones are evaluated across all games: (1) Perception...
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Synthetic data detection** (behavioral indicator), 1 paper
  > the task of distinguishing between real and synthetic data effectively tests the perception, knowledge, and reasoning capabilities of LMMs. (ABSTRACT)
  - [LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf)
