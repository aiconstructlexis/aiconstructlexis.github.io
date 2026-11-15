# COCO Caption
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** COCO Captions, COCO-Cap, COCO-Caption, COCO-Captions, COCO-Capation  

## State of the Field

**What it is.** Across papers, the dominant framing is a COCO-based image captioning benchmark or dataset used to evaluate models that generate textual descriptions for images. Definitions vary at the margins: some describe a large-scale captioning benchmark, some describe the captioning portion of a broader object detection and segmentation dataset with multiple short human-written descriptions per image, and some use it as a source of prompts for text-to-image evaluation. Specific descriptions mention the validation set, the validation split, and the karpathy-test split, and one paper describes over 330,000 images with more than 1.5 million captions and five human-generated captions for each image.

**What it is claimed to measure.** Papers link it to 2 behavioral indicators and 2 constructs. The prevailing usage is to measure image captioning, with several papers explicitly evaluating caption tasks on this benchmark and reporting caption metrics such as BLEU, METEOR, CIDEr, SPICE, ROUGE-L, or BertScore. Smaller lines of work also use it to measure image generation, fine-grained perception, and visual understanding.

**Space of uses.** No measurement instrument is linked to it. Papers usually position it as a standard, widely adopted, or open-response caption benchmark, and they use named splits such as karpathy-test or validation data for evaluation. Some papers instead sample prompts from the COCO Captions validation set or evaluate text-to-image generation on COCO-caption data, so its use includes both caption evaluation and generation-focused setups.

## Sources

**COCO Caption** (4 papers: [A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf), [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf), [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf), [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf))
> A benchmark dataset used to evaluate the capability of models to generate textual descriptions for images.

**COCO Captions** (2 papers: [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf))
> A dataset of image captions (from the Common Objects in Context dataset) used here as a source of prompts for evaluating text-to-image generation tasks.

**COCO-Cap** (2 papers: [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf), [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf))
> A large-scale image captioning benchmark based on the Common Objects in Context (COCO) dataset.

**COCO-Captions** (1 paper: [Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hahn25a/hahn25a.pdf))
> A large-scale object detection, segmentation, and captioning dataset, where the captioning portion provides multiple short, human-generated descriptions for each image.

**COCO-Caption** (2 papers: [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf), [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf))
> A dataset based on the Common Objects in Context (COCO) collection, used for evaluating image captioning models.

**COCO-Capation** (1 paper: [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf))
> Image captioning benchmark used to assess a model's ability to generate descriptive text from images during fine-tuning.

## Relationships

### → COCO Caption
- **Image captioning** (behavioral indicator): *measured_by*, 5 papers
  > For COCO image captioning, we report BLEU@4 (B@4), METEOR (M), CIDEr (C), and SPICE (S). (Section 4.3)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
  - [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf)
- **Visual understanding** (construct): *measured_by*, 1 paper
  > We evaluate on the widely used vision-language understanding and generation benchmarks... For COCO image captioning... Above results show that X-MoE exhibits enhanced visual information comprehension
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Image generation** (behavioral indicator): *measured_by*, 1 paper
  > Table 8: Text-to-Image generation on COCO-caption data [60].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Fine-grained perception** (construct): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... COCO Captions (Chen et al., 2015)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
