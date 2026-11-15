# Visual dialogue
**Type:** Behavioral indicator  
**Supporting papers:** 25  
**Also known as:** Open-ended visual chat, Multimodal chat, Multi-modal chat, Image-based conversation, Visual prompt-based conversation, Visual conversation, Multi-modal dialogue, Multi-turn visual conversation, Visual dialog, Visual chatting, Multi-image dialogue, Image dialogue, Visual chat, Conversational VQA, Biomedical multimodal conversation, Multimodal dialogue, Multimodal conversation, Multi-modal conversation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is open-ended, multi-turn conversation grounded in images, where a model responds in natural language to image-based prompts, questions, or instructions. Most definitions add that replies should be conditioned on both the visual input and prior turns, and several describe the setting broadly as multimodal dialogue with text and images rather than only a single image-centered exchange. A smaller line of work narrows the expected output to contextually relevant biomedical answers or step-by-step responses for interleaved-image tasks.

**Variants.** Authors use several near-synonymous names, most commonly multimodal chat, dialogue, or conversation, and visual conversation, visual chat, or visual dialog; less common labels include image-based conversation, image dialogue, and conversational VQA. Studied settings range from one-image chats to multi-image and interleaved multi-image dialogue, and some papers add visual prompt-based conversation in which users refer to regions with points, boxes, or masks. Other variants place the behavior in biomedical, pathology, or broader clinical contexts, or in multilingual and bilingual conversations grounded in images.

**Space of elicitation and scores.** Papers link this behavior to three measurement instruments. MM-Vet is the instrument mentioned most often: papers say it evaluates a model's capability in engaging in visual conversations, and one description adds that it evaluates correctness and helpfulness with a GPT-4 framework. A smaller usage measures multi-modal chat with GQA and TextVQA.

**What it is taken as evidence of.** Across construct links, papers do not present a broad construct mapping: the only recorded construct is Visual understanding, and the relationship is stated as related rather than causal or measurement-based. One paper places image-based conversation and visual prompt-based conversation within image-level and object-level visual understanding and reasoning tasks. Papers also record one related link to Visual question answering, with one study saying VQA has become a benchmark for evaluating task- and dataset-independent visual dialog.

## Sources

**Open-ended visual chat** (1 paper: [Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec33ab89b5986605cd7c331396e7e5c-Paper-Datasets_and_Benchmarks_Track.pdf))
> Responding to image-based prompts in a multi-round conversational format with contextually relevant biomedical answers.

**Multimodal chat** (2 papers: [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf))
> Engaging in a multi-turn conversational interaction with a user, where the conversation is grounded in one or more images.

**Multi-modal chat** (1 paper: [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf))
> The task of engaging in a conversation that involves understanding and responding to inputs from multiple modalities, such as combined text and image queries.

**Visual dialogue** (1 paper: [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf))
> The observable task of participating in a conversation about an image, where the model's responses are contextually dependent on both the visual input and the dialogue history.

**Image-based conversation** (1 paper: [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf))
> The task of engaging in a multi-turn dialogue with a user about the content of an image.

**Visual prompt-based conversation** (1 paper: [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf))
> The task of engaging in a dialogue about an image where the user can refer to specific areas using visual prompts like points, boxes, or masks.

**Visual conversation** (2 papers: [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf), [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf))
> Engaging in multi-turn dialogue about visual content, producing responses conditioned on images and prior turns.

**Multi-modal dialogue** (1 paper: [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf))
> Engaging in a conversational exchange that involves both textual and visual information.

**Multi-turn visual conversation** (2 papers: [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf), [Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf))
> The observable behavior of engaging in a sequence of dialogue turns involving both visual and textual inputs, where responses depend on prior context.

**Visual dialog** (1 paper: [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf))
> Engaging in a multi-turn conversational exchange with a user about the content of an image.

**Visual chatting** (1 paper: [Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf))
> Engaging in a multi-turn, conversational interaction with a user about the content of an image.

**Multi-image dialogue** (1 paper: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf))
> Engaging in dialogue grounded in multiple images provided together as input.

**Image dialogue** (1 paper: [Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d368eba3fb546ae5d868dae2ecb17200-Paper-Conference.pdf))
> Responding in natural language to image-based prompts in a conversational format.

**Visual chat** (1 paper: [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf))
> Engaging in a multi-turn conversational dialogue with a user about the contents of an image.

**Conversational VQA** (1 paper: [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf))
> The model answers conversational visual questions about images, including dialogue-style prompts and responses.

**Biomedical multimodal conversation** (1 paper: [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf))
> Engaging in a conversational exchange about biomedical topics, involving the interpretation of medical images and related text.

**Multimodal dialogue** (4 papers: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf), [Automating Steering for Safe Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.41.pdf), [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf))
> Engaging in a conversational exchange with a user where the context includes both text and images.

**Multimodal conversation** (1 paper: [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf))
> Engaging in dialogue with users based on visual input, including answering questions and following instructions in multiple languages.

**Multi-modal conversation** (1 paper: [EAGLE: Expert-Guided Self-Enhancement for Preference Alignment in Pathology Large Vision-Language Model](https://aclanthology.org/2025.acl-long.711.pdf))
> Engaging in dialogue involving both image and text inputs, such as responding to follow-up questions or providing detailed descriptions in a clinical context.

## Relationships

### Visual dialogue →
- **MM-Vet** (measurement instrument): *measured_by*, 2 papers
  > MM-Vet evaluates a model’s capabilities in engaging in visual conversations. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 1 paper
  > Multi-Modal Chat Vision-language models (VLMs) are attracting increasing attention due to their ability to process both text and images. ... For this task, we use GQA (Hudson & Manning, 2019) and TextVQA (Singh et al., 2019)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > Multi-Modal Chat Vision-language models (VLMs) are attracting increasing attention due to their ability to process both text and images. ... For this task, we use GQA (Hudson & Manning, 2019) and TextVQA (Singh et al., 2019)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > most recently, VQA also become one of the most powerful benchmarks for evaluating task and dataset independent visual dialog. (Section 5)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **Visual understanding** (construct), 1 paper
  > Our OMG-LLaVA unifies image-level (such as image caption and image-based conversation), object-level (such as region caption and visual prompt-based conversation), and pixel-level (such as universal segmentation, referring segmentation, reasoning segmentation, and grounded conversation generation) visual understanding and reasoning tasks into token-to-token generation. (Section 3.1)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
