# Flickr30k
**Type:** Measurement instrument  
**Supporting papers:** 46  
**Also known as:** Flickr30K, FLICKR30K  

## State of the Field

**What it is.** Across the surveyed work, Flickr30k is most commonly described as a benchmark dataset for image captioning: papers depict it as 30,000 images from Flickr paired with descriptive captions, often five per image, and sometimes emphasize human-annotated captions. A smaller but recurring framing treats it as an image-text retrieval benchmark, where models match images to captions or the reverse, and some papers also use it for text-to-image generation. One paper further specifies evaluation on the Flickr30k Karpathy split test set.

**What it is claimed to measure.** Across the papers, Flickr30k is linked to 3 behavioral indicators and 2 constructs. The prevailing measurement claim is image captioning, with papers using it to evaluate image-level caption ability, zero-shot caption generation, and general image captioning; a smaller line of work uses it to measure cross-modal retrieval, including image-to-text and text-to-image retrieval, and a few papers use it for image generation. At the construct level, papers report it as measuring visual perception through captioning scenarios and as evaluating multimodal understanding.

**Space of uses.** Papers commonly position Flickr30k as a standard or widely used benchmark, using it both for dedicated zero-shot or few-shot captioning and retrieval evaluations and as part of broader benchmark suites. It is often used alongside MS-COCO or COCO and NoCaps, and some broader suites pair it with VQAv2, VizWiz, and POPE. Usage also spans in-context learning and generalizability checks, and one study reports retrieval in both image-to-text and text-to-image directions.

**Concerns raised.** One paper reports that performance on popular cross-modal retrieval benchmarks such as Flickr30K has reached saturation. Separately, a study using it for in-context learning notes that few-shot performance on Flickr30K decreases as more examples are given.

## Sources

**Flickr30k** (7 papers: [Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf), [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf))
> Image-text retrieval benchmark where models match images to corresponding captions or vice versa.

**Flickr30K** (6 papers: [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf))
> Image captioning dataset with 30,000 images and associated captions, used to evaluate vision-to-text generation and in-context learning effects.

**FLICKR30K** (1 paper: [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf))
> An image captioning dataset consisting of 30,000 images collected from Flickr, each with multiple descriptive captions.

## Relationships

### → Flickr30k
- **Image captioning** (behavioral indicator): *measured_by*, 15 papers
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
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 9 papers
  > We evaluate the performance of Causal Q-Former on the image-text retrieval using COCO (Lin et al., 2014) and Flickr30K (Young et al., 2014). (Section 4)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
  - [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
  - [4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities](https://proceedings.neurips.cc/paper_files/paper/2024/file/71883294314045d60c900113a359934b-Paper-Conference.pdf)
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf)
  - [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf)
- **Image generation** (behavioral indicator): *measured_by*, 2 papers
  > We evaluate the text-to-image generation on MS-COCO (Chen et al., 2015) and Flickr30K (Young et al., 2014) and compute the pair-wise CLIP similarity score as the evaluation metric following GILL (Koh et al., 2023b). (Section 4.1.1)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf)
- **Visual perception** (construct): *measured_by*, 1 paper
  > “Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. VHELM uses scenarios such as Flickr-30k [46], VQAv2 [12], VizWiz [14] and POPE [23] to assess this aspect.”
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > Following LLaVA (Liu et al., 2024b), we evaluate the multimodal understanding capabilities of Show-o on POPE, MME, Flickr30k, VQAv2, GQA, and MMMU benchmarks. (Section 4.1)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
