# Fine-grained perception
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Fine-grained visual perception  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats fine-grained perception as a facet or latent visual ability centered on recognizing detailed, specific, and subtle visual attributes. Definitions converge on examples such as object locations, celebrity identities, clothing styles, instance-level features, positions, counts, and spatial relationships; some papers further stress pixel-level details like color, texture, and relations among small objects. One paper instead uses the label "fine-grained visual perception" and defines it as the capacity to capture detailed visual attributes and subtle appearance cues from images.

**Space of facets.** Some papers place the construct inside larger perception taxonomies. It is contrasted with OCR and spatial perception in one framing, and appears alongside coarse perception, instance reasoning, and logical reasoning in another. Within the construct itself, papers emphasize detailed appearance and identity cues on the one hand, and localization, counting, and other spatially specific visual detail on the other.

**Space of measurement.** Operationalization is benchmark-heavy: papers link the construct to 8 measurement instruments and 1 behavioral indicator. The most frequently linked instruments include COCO Caption, CapsBench, MMMU, and MMStar, and papers also cite other benchmarks that mainly focus on fine-grained perception or place it in a vision-centric category emphasizing fine-grained perception and localization; MM-Star is used through a detailed fine-grained perception score. These operationalizations mostly mirror the definitions by targeting fine-grained tasks such as movie recognition, position description, counting, and object localization, and one paper also relates the construct to Image classification for low-resolution or tiny-object cases.

**Links.** Only a few cross-construct links are recorded, and no correlational links are reported. One paper claims a causal relationship from fine-grained perception to Logical reasoning, stating that gains in fine-grained perception subsequently enhance image-based logical reasoning, and another claims a causal relationship from fine-grained perception to Localization ability by arguing that better capture of details results in improved localization ability. Separately, one paper reports that fine-grained perception is related to Image classification, especially for low-resolution images or tiny objects.

## Sources

**Fine-grained perception** (4 papers: [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf), [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf), [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf), [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf))
> A specific facet of perception involving the ability to recognize detailed and specific visual attributes, such as object locations, celebrity identities, or clothing styles.

**Fine-grained visual perception** (1 paper: [EasyRef: Omni-Generalized Group Image Reference for Diffusion Models via Multimodal LLM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zong25a/zong25a.pdf))
> The latent ability to capture detailed visual attributes and subtle appearance cues from images.

## Relationships

### Fine-grained perception →
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > We further analyze the detailed scores on MM-Star (Chen et al., 2024a), including coarse perception (CP), fine-grained perception (FP), instance reasoning (IR), logical reasoning (LR)... (Table 4)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > Among these benchmarks, MMVP mainly focuses on fine-grained perception. (Section 4.1)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Logical reasoning** (construct): *causes*, 1 paper
  > This suggests that fusing raw image and text embeddings in a single transformer is beneficial for fine-grained perception and subsequently enhances image-based logical reasoning. (Section 4.3)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Localization ability** (construct): *causes*, 1 paper
  > We visualize the attention maps from the penultimate layer of the CLIP visual encoder for several examples in Fig 2. The attention maps are generally similar w/wo alignment, as the regularization term prevents significant changes in the model’s weights. However, we still observe that the attention maps after alignment are sharper and highlight more fine-grained features. This indicates that the aligned model is better at capturing details from the input image, resulting in improved localization ability. (Section 4.2)
  - [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf)
- **CapsBench** (measurement instrument): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: CapsBench (Liu et al., 2024a)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **Stanford Dogs** (measurement instrument): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... Stanford Dogs (Khosla et al., 2011)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **COCO Caption** (measurement instrument): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... COCO Captions (Chen et al., 2015)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **OCRBench** (measurement instrument): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... OCRBench (Liu et al., 2024b)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... and MMMU (Yue et al., 2024). (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > The Vision-centric category emphasize fine-grained perception and localization, including... RealWorldQA (real-world QA)... (Section 3)
  - [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf)

### Associated with
- **Image classification** (behavioral indicator), 1 paper
  > “The improvements are particularly notable for images with low resolution (e.g., CIFAR) or tiny objects (e.g., EuroSAT), highlighting enhanced fine-grained perception capabilities.”
  - [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf)
