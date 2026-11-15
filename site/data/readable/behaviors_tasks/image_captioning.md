# Image captioning
**Type:** Behavioral indicator  
**Supporting papers:** 205  
**Also known as:** Literal description writing, Visual captioning, Scene description, Image description generation, Image Caption Generation, Image Captioning, Image caption generation, Captioning, Diagram captioning, Situated captioning, Frame-level caption generation, Scene description generation, Image description, Caption generation, Open-ended generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats image captioning as generating textual descriptions of visual input, most often entire images. Most definitions frame success as a caption that reflects the image's content, and several make this explicit by requiring accurate mention of present objects, attributes, and spatial relations, or by asking for an objective description that avoids conjecture. A smaller line of work asks for brief, single-sentence, or concise captions, while others ask for rich or very detailed descriptions, including style, narrative, or text detailed enough to replace the visual input in downstream problem solving.

**Variants.** Papers use nearby labels such as image description, caption generation, scene description, diagram captioning, and situated captioning. The task is studied at whole-image, region, and crop level, and in both free-form open-ended and structured JSON settings. Domain-specific variants cover comics, medical or pathology images, earth-observation images, driving scenes, and UI elements or 3D surroundings, and some work uses captions as an intermediate step before question answering or as per-image inputs inside summarization pipelines.

**Space of elicitation and scores.** Across papers, image captioning is measured by 9 linked instruments. The most common are MS-COCO, Flickr30k, CHAIR, NoCaps, and COCO Caption. These include standard captioning benchmarks, caption metrics such as BLEU, METEOR, CIDEr, and SPICE, a hallucination-focused metric that assesses object hallucinations in generated captions, and judge-based or human scoring, including GPT-4 ratings of caption accuracy and detailedness on a Likert scale.

**What it is taken as evidence of.** Across papers, there is no single agreed construct that image captioning reflects. It is linked to 7 constructs, most often as related to visual understanding, multimodal understanding, and visual perception; smaller lines add a causal claim from image captioning to brain alignment and a relatedness link to generalization. Further single-paper causal links are also recorded, so the overall usage is mixed rather than centered on one construct.

## Sources

**Image captioning** (31 papers: [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf), [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587.pdf), [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf), [Pay More Attention to Images: Numerous Images-Oriented Multimodal Summarization](https://aclanthology.org/2025.naacl-long.474.pdf), [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf), [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89.pdf), [ImgTrojan: Jailbreaking Vision-Language Models with ONE Image](https://aclanthology.org/2025.naacl-long.360.pdf), [Visual Evidence Prompting Mitigates Hallucinations in Large Vision-Language Models](https://aclanthology.org/2025.acl-long.205.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf), [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf), [An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf), [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf), [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf), [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a6a5e2e8a27262501bda3463fcf7b21-Paper-Conference.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf), [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf), [Vision-by-Language for Training-Free Compositional Image Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/48fd58527b29c5c0ef2cae43065636e6-Paper-Conference.pdf))
> The observable task of producing textual descriptions of input images.

**Literal description writing** (1 paper: [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf))
> The task of generating a short, surface-level text description that illustrates the narrative depicted in the two panels of a comic.

**Image description** (6 papers: [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Defending LVLMs Against Vision Attacks Through Partial-Perception Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25z/zhou25z.pdf), [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf), [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.324.pdf), [MiCEval: Unveiling Multimodal Chain of Thought's Quality via Image Description and Reasoning Steps](https://aclanthology.org/2025.naacl-long.504.pdf), [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26.pdf))
> Generating textual descriptions of the visual content within an image.

**Visual captioning** (1 paper: [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf))
> Generating descriptive text that summarizes or details the content of an image.

**Scene description** (2 papers: [Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf), [WOMD-Reasoning: A Large-Scale Dataset for Interaction Reasoning in Driving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25l/li25l.pdf))
> The task of generating a structured (e.g., JSON) or natural language description of all objects and their features (e.g., color, shape) in a visual scene.

**Image description generation** (3 papers: [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf), [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf), [Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://aclanthology.org/2025.acl-long.175.pdf))
> The task of producing a natural language text that describes the visual content of a given image.

**Image Caption Generation** (3 papers: [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf), [Pragmatics in the Era of Large Language Models: A Survey on Datasets, Evaluation, Opportunities and Challenges](https://aclanthology.org/2025.acl-long.425.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf))
> The observable task of generating textual descriptions for provided images.

**Image Captioning** (1 paper: [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf))
> The observable task of generating detailed textual descriptions of image content and style.

**Image caption generation** (3 papers: [Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad0edc7d5fa1a783f063646968b7315b-Paper-Datasets_and_Benchmarks_Track.pdf), [PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebf8764ecf0688cdd9fe1e5a9c525d0d-Paper-Conference.pdf), [Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25k/shen25k.pdf))
> Describing a diagram or image in text so that the description can substitute for the visual input in downstream problem solving.

**Captioning** (1 paper: [TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf))
> Generating descriptive natural-language text about the content of an earth-observation image.

**Situated captioning** (1 paper: [SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf))
> Generating brief descriptions of surrounding objects and their spatial directions from the agent’s current standing point and orientation.

**Diagram captioning** (1 paper: [MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf))
> The observable behavior of generating a textual description that accurately identifies the mathematical elements and their relationships within a given diagram.

**Scene description generation** (1 paper: [UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf))
> Generating a textual description of the current visual scene in response to a prompt.

**Caption generation** (3 papers: [Rephrase, Augment, Reason: Visual Grounding of Questions for Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/eef6cb60fd59b32d35718e176b4b08d6-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [COVE: COntext and VEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.102.pdf))
> Producing descriptive natural language summaries of visual regions or entire images based on their content.

**Open-ended generation** (1 paper: [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf))
> Producing free-form textual descriptions of an image without constraints on content or structure, typically used in image captioning tasks.

## Relationships

### Image captioning →
- **MS-COCO** (measurement instrument): *measured_by*, 22 papers
  > and the image caption generation task, MSCOCO (Chen et al., 2015) (Section 3.1).
  - [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
  - [VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [Backdooring Vision-Language Models with Out-Of-Distribution Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/da37068018f8f7185720b83ea6f48377-Paper-Conference.pdf)
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
  - [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf)
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)
  - [Diffusion Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25g/jin25g.pdf)
  - [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf)
  - [Case-Based Decision-Theoretic Decoding with Quality Memories](https://aclanthology.org/2025.emnlp-main.1710.pdf)
- **Flickr30k** (measurement instrument): *measured_by*, 15 papers
  > We first quantitatively evaluate the zero-shot multi-modal understanding capacity of LaVIT on Image Captioning (NoCaps (Agrawal et al., 2019), Flickr30k (Plummer et al., 2015)) (Section 4.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
  - [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
  - [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
  - [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
  - [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf)
  - [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 12 papers
  > Caption Hallucination Assessment with Image Relevance (CHAIR) (Rohrbach et al., 2018) is a widely-used metric for evaluating object hallucination in image captioning tasks.
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **NoCaps** (measurement instrument): *measured_by*, 9 papers
  > We first quantitatively evaluate the zero-shot multi-modal understanding capacity of LaVIT on Image Captioning (NoCaps (Agrawal et al., 2019), Flickr30k (Plummer et al., 2015)) (Section 4.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
  - [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf)
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)
  - [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf)
  - [Detecting Knowledge Boundary of Vision Large Language Models by Sampling-Based Inference](https://aclanthology.org/2025.emnlp-main.1458.pdf)
  - [Case-Based Decision-Theoretic Decoding with Quality Memories](https://aclanthology.org/2025.emnlp-main.1710.pdf)
- **COCO Caption** (measurement instrument): *measured_by*, 5 papers
  > For COCO image captioning, we report BLEU@4 (B@4), METEOR (M), CIDEr (C), and SPICE (S). (Section 4.3)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
  - [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > For literal description and contradiction, we report BERT score (recall), BLEURT (BLT), and GPT evaluation score. (Table 2)
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Generative ability** (construct): *causes*, 1 paper
  > image captioning to yield the generative capability of frozen LLMs.
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)
- **CUB-200-2011** (measurement instrument): *measured_by*, 1 paper
  > we use the learned codebook to conduct two visual text reasoning tasks: 1) image captioning on CUB-200; (Section 4.4.2)
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > we also include human evaluation to assess the quality of the outputs for the literal description and contradiction generation tasks. (Section 4.2)
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > LLaVA-Bench (Liu et al., 2023b) consists of 24 images and 60 questions to assess LVLMs' performance on complex tasks and domain adaptation. Following Leng et al. (2024), we use GPT-4 to assess the accuracy and detailedness of LVLM's image captioning
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > Much like humans, who often write down their key observations in an image and refer to them while solving complex reasoning tasks, we hypothesize that grounding the LVLM’s responses in a detailed visual description can significantly enhance its reasoning process. (Section 5)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Brain alignment** (construct): *causes*, 1 paper
  > Specifically, the image captioning instruction leads to stronger brain alignment in regions like the EBA (extrastriate body area), PPA (parahippocampal place area), and FFA (fusiform face area)
  - [Correlating instruction-tuning (in multimodal models) with vision-language processing (in the brain)](https://proceedings.iclr.cc/paper_files/paper/2025/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)

### Associated with
- **Visual understanding** (construct), 4 papers
  > Our OMG-LLaVA unifies image-level (such as image caption and image-based conversation), object-level (such as region caption and visual prompt-based conversation), and pixel-level (such as universal segmentation, referring segmentation, reasoning segmentation, and grounded conversation generation) visual understanding and reasoning tasks into token-to-token generation. (Section 3.1)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Multimodal Situational Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cb57fcf7ff3f6d37eebae5becc9ea6d-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator), 3 papers
  > Dispreferred response: Model-generated descriptions resulting from either (1) corrupted image with low resolution or distorted color, or (2) “bad” prompts that cause the base model to hallucinate and describe elements that may not logically exist in the image. (Section 4)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
- **Multimodal understanding** (construct), 3 papers
  > While conceptually simple, this allows us to explore vision-language understanding tasks such as captioning and VQA, as well as text-to-image generation. (Section 3.3)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Visual perception** (construct), 2 papers
  > Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Is Your Multimodal Language Model Oversensitive to Safe Queries?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50d4f8ff0416cedfe0771b7ad947a197-Paper-Conference.pdf)
- **Object hallucination** (behavioral indicator), 1 paper
  > “HALVA substantially reduces hallucination in image descriptions compared to the base variants.”
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > Meanwhile, image captioning is conducted on the unseen BLIP-2 (OPT-2.7b) (Li et al., 2023), to demonstrate the generalization capacity. (Section 4.1)
  - [Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25k/shen25k.pdf)
