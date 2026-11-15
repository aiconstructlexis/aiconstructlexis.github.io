# Image generation
**Type:** Behavioral indicator  
**Supporting papers:** 83  
**Also known as:** Text-to-image generation, Image synthesis, Chest X-ray generation, Controllable generation, Conditional image generation, Text-to-image synthesis, Text-conditioned image generation  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is creating or synthesizing novel images from text prompts or textual descriptions. A smaller but recurring framing broadens this to conditional generation from class labels or other conditioning signals, including the standard ImageNet class-conditional setting, and some definitions also allow visual or multimodal prompts. Success is usually described in terms of realistic or high-quality outputs, with some papers additionally emphasizing fidelity or faithfulness to the described content.

**Variants.** Most named variants specialize the behavior by input or domain: papers use text-to-image generation or text-to-image synthesis for purely textual prompts, conditional image generation for class labels or multimodal context, and controllable generation when text is paired with edges, landmarks, or segmentation maps. Smaller lines of work study image synthesis from visual and spatial clues with an external toolkit, chest X-ray generation from anatomical and pathology descriptions, multilingual prompting in Chinese and English, and subtasks such as style generation, subject generation, or multi-image outputs like visual stories and image sequences. One paper also claims a causal relationship from query rewriting to image generation, using an LLM to rewrite prompts so the final image improves in quality while maintaining or improving faithfulness.

**Space of elicitation and scores.** Papers measure it with 8 linked instruments. MS-COCO is the most frequent, followed by Flickr30k, ImageNet-1k, COCO Caption, and FFHQ, with 3 other instruments also linked. These instruments are mostly benchmark datasets, and the quoted evaluations commonly score outputs with CLIP similarity or CLIPScore and FID or FID-30k; smaller studies also use manual judgments of exact object counts and LLM-based judging.

**What it is taken as evidence of.** Papers do not converge on a single construct to which this behavior is linked. The prevailing linkage is that it is related to visual generation ability, while smaller lines of work also relate it to analogical reasoning, memorization, and semantic alignment. In those papers, image generation is used for completing an analogy problem, depicting image details as a memorization-centered task, or aligning generated images with text prompts.

## Sources

**Image generation** (9 papers: [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf), [Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf), [The Impossibility of Fair LLMs](https://aclanthology.org/2025.acl-long.5.pdf), [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf))
> Producing realistic images from class labels or other conditioning signals using a generative model.

**Text-to-image generation** (12 papers: [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf), [RRInf: Efficient Influence Function Estimation via Ridge Regression for Large Language Models and Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.933.pdf), [Multi-task Adversarial Attacks against Black-box Model with Few-shot Queries](https://aclanthology.org/2025.acl-long.684.pdf), [Multilingual Text-to-Image Generation Magnifies Gender Stereotypes](https://aclanthology.org/2025.acl-long.966.pdf), [When the LM misunderstood the human chuckled: Analyzing garden path effects in humans and language models](https://aclanthology.org/2025.acl-long.403.pdf), [DataInf: Efficiently Estimating Data Influence in LoRA-tuned LLMs and Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e84a0f233611a1dc8fb794dc52415a3-Paper-Conference.pdf), [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf), [LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts](https://proceedings.iclr.cc/paper_files/paper/2024/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf))
> Creating static visual content from textual prompts.

**Image synthesis** (1 paper: [Enhancing LLM Reasoning via Vision-Augmented Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/328c922d068dd4ccb23cec5c64e6c7fc-Paper-Conference.pdf))
> Creating an image from a textual problem description using a drawing or generation tool.

**Chest X-ray generation** (1 paper: [MedRAX: Medical Reasoning Agent for Chest X-ray](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fallahpour25a/fallahpour25a.pdf))
> Synthesizing realistic chest X-ray images from textual descriptions of anatomical features and pathologies.

**Controllable generation** (1 paper: [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf))
> Generating images that align with a text prompt and additional control signals such as edges, landmarks, or segmentation maps.

**Conditional image generation** (2 papers: [Demystifying Poisoning Backdoor Attacks from a Statistical Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/4488bf8354049b1cd592b6418dc30466-Paper-Conference.pdf), [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf))
> The task of synthesizing an image based on a given condition, such as a text prompt or a multimodal context.

**Text-to-image synthesis** (1 paper: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf))
> Generating images from textual prompts or descriptions.

**Text-conditioned image generation** (1 paper: [I Think, Therefore I Diffuse: Enabling Multimodal In-Context Reasoning in Diffusion Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mi25a/mi25a.pdf))
> Generating an image based solely on a textual prompt, following the described content with high fidelity.

## Relationships

### Image generation →
- **MS-COCO** (measurement instrument): *measured_by*, 8 papers
  > We evaluate the text-to-image generation on MS-COCO (Chen et al., 2015) and Flickr30K (Young et al., 2014) and compute the pair-wise CLIP similarity score as the evaluation metric following GILL (Koh et al., 2023b). (Section 4.1.1)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
  - [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/12678c3948153f4bc391f51e2082bd6e-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 2 papers
  > when evaluating on the ImageNet dataset, a gold standard benchmark for image generation (Section 1).
  - [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
- **Flickr30k** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the text-to-image generation on MS-COCO (Chen et al., 2015) and Flickr30K (Young et al., 2014) and compute the pair-wise CLIP similarity score as the evaluation metric following GILL (Koh et al., 2023b). (Section 4.1.1)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf)
- **COCO Caption** (measurement instrument): *measured_by*, 1 paper
  > Table 8: Text-to-Image generation on COCO-caption data [60].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To assess their ability to generate images with the exact number of objects requested, we conducted a human evaluation study. (Section 3.1)
  - [Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf)
- **FFHQ** (measurement instrument): *measured_by*, 1 paper
  > We report the FID (Parmar et al., 2022) values in Table 2 for unconditional 256×256 image synthesis on the CelebA-HQ dataset (Karras et al., 2017) and the FFHQ dataset (Karras et al., 2018).
  - [Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf)
- **GenEval** (measurement instrument): *measured_by*, 1 paper
  > we report results on more comprehensive benchmarks instead of only CLIP score, such as GenEval (Ghosh et al., 2024) and DSG (Cho et al., 2024). (Section 4.3)
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > following the GPT-4V metric introduced in Section 4.2, we randomly select a subset of 3,000 our generated images for GPT-4V evaluation.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)

### → Image generation
- **Query rewriting** (behavioral indicator): *causes*, 1 paper
  > The goal of the LLM is to “rewrite” the prompt passed into the T2I model, such that the final generated image improves in quality, while maintaining or improving the faithfulness to the original text prompt. (Section 4.4)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)

### Associated with
- **Visual generation ability** (construct), 2 papers
  > "Visual Generation is also a wide topic covering a number of different tasks, such as generation, editing, variation, personalization, etc. In VisionLLM v2, we focus on two fundamental tasks, i.e., text-to-image generation and instruction-based image editing."
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Memorization** (construct), 1 paper
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Semantic alignment** (construct), 1 paper
  > “aligning the generated images with the text prompts, which is referred to as semantic alignment”
  - [Token Merging for Training-Free Semantic Binding in Text-to-Image Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8ce25dcb2cb0eb8a24b492bf3e84695-Paper-Conference.pdf)
- **Analogical reasoning** (construct), 1 paper
  > "The aim is to generate an image that completes the analogy problem following perceptual and relational reasoning."
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
