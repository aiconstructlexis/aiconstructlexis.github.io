# Cross-modal retrieval
**Type:** Behavioral indicator  
**Supporting papers:** 47  
**Also known as:** Image-text matching, Image-caption matching, Compositional image-text matching, Audio-to-text retrieval, Text-to-audio retrieval, Image-text retrieval, Text-image retrieval, Text-to-image retrieval, Text-to-video retrieval, Video-to-text retrieval, Video retrieval, Composed image retrieval, Visual question answering retrieval, Image retrieval, Image-to-text retrieval, Long-text-image retrieval, Short-text-image retrieval, Species identification, Retrieval  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage is retrieving a matching item in one modality from a query in another, most often between text and images in both directions. Success is usually defined by selecting or ranking the most relevant item from candidates or a database, sometimes via similarity or matching scores, as one paper puts it: "The goal of text-to-image retrieval is to rank images from a potentially large image collection according to their relevance to an input text query." A smaller line of work formulates the same behavior as pairwise image-text matching, either choosing between two captions or images, or deciding whether a caption describes an image at all.

**Variants.** Most variants stay within image-text retrieval, under names such as image-text retrieval, text-to-image retrieval, image-to-text retrieval, image-text matching, and image-caption matching. Papers also study compositional image-text matching, long-text versus short-text-image retrieval, region-level and whole-image retrieval, and composed image retrieval, where the query combines a source image with a textual modification. Smaller variants extend the same pattern to audio-text, text-to-video and video-to-text retrieval, graph-to-text and text-to-graph retrieval, visual question answering retrieval, species identification, sketch-based image retrieval, and ASL-based retrieval.

**Space of elicitation and scores.** Papers measure this behavior with 12 instruments. The most frequently linked are MS-COCO and Flickr30k, with other linked instruments including AudioCaps, CUB-200-2011, and Clotho; the remainder include video retrieval benchmarks, matching benchmarks, and dialog-based benchmarks. Scoring is commonly reported as ranking or retrieval performance, including Recall at 1/5/10 and semantic retrieval results, and some papers use extracted image-text matching scores or logits. Beyond benchmark evaluation, one paper claims a causal relationship from Ranking to Cross-modal retrieval, reporting that zero-shot reranking can "boost retrieval accuracy" on challenging multimodal queries.

**What it is taken as evidence of.** Papers link this behavior to 3 constructs, but they do not agree on a single construct it reflects. Instead, one paper reports it is related to Long-context understanding, arguing that long-text-image retrieval evaluates a model's ability to comprehend long texts; another reports it is related to Modality bias, describing underperformance in cross-modal retrieval "due to the modality bias" of MLLMs; and another reports it is related to Multimodal alignment, using text-to-image and image-to-text retrieval to evaluate "cross-modal alignment efficacy."

## Sources

**Cross-modal retrieval** (5 papers: [BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf), [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf), [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf), [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf), [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf))
> Retrieving content from one modality (e.g., image) based on input from another modality (e.g., text), including both image-to-text and text-to-image directions.

**Image-text matching** (4 papers: [DevBench: A multimodal developmental benchmark for language learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8d987b2981388c99c7eab6095d1d29fd-Paper-Datasets_and_Benchmarks_Track.pdf), [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf), [Exploring How Generative MLLMs Perceive More Than CLIP with the Same Vision Encoder](https://aclanthology.org/2025.acl-long.499.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf))
> The general task of determining the correspondence or similarity between a given image and a piece of text, often by producing a score.

**Image-caption matching** (1 paper: [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf))
> Selecting the correct caption for an image or the correct image for a caption from two alternatives.

**Compositional image-text matching** (1 paper: [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf))
> The task of correctly identifying the matching image-text pair from a set of distractors that involve compositional changes in objects, attributes, or relations.

**Audio-to-text retrieval** (1 paper: [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf))
> Given an audio input, the model retrieves the matching text caption from a candidate set.

**Text-to-audio retrieval** (1 paper: [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf))
> Given a text caption, the model retrieves the matching audio sample from a candidate set.

**Text-to-image retrieval** (2 papers: [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf))
> The task of selecting and returning an existing image from a database that best matches a given textual description.

**Text-to-video retrieval** (2 papers: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf), [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf))
> Ranking videos given a textual query.

**Video-to-text retrieval** (1 paper: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf))
> Retrieving relevant text descriptions from a collection based on a video query.

**Video retrieval** (1 paper: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf))
> Retrieving videos that are relevant to a textual query, including partially relevant videos from a larger collection.

**Image-text retrieval** (3 papers: [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf), [Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf))
> The task of selecting the most relevant text caption for a given image from a set of candidates, or vice-versa.

**Text-image retrieval** (1 paper: [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf))
> Retrieving images or text items based on cross-modal similarity between text and images.

**Composed image retrieval** (1 paper: [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf))
> The observable task of retrieving a target image based on a query that combines a source image with a textual description of desired modifications.

**Visual question answering retrieval** (1 paper: [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf))
> The observable task of retrieving a document (e.g., text or an image-description pair) that contains the answer to a question posed about a given image.

**Image retrieval** (2 papers: [MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf), [Uplifting Lower-Income Data: Strategies for Socioeconomic Perspective Shifts in Large Multi-modal Models](https://aclanthology.org/2025.naacl-long.106.pdf))
> The task of finding and selecting a correct target image from a set of candidates based on a query, such as matching a sketch to a natural image.

**Image-to-text retrieval** (1 paper: [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf))
> Given an image, finding the most semantically similar text description from a collection of candidate texts.

**Long-text-image retrieval** (1 paper: [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf))
> The task of retrieving the correct image from a set given a long, detailed text query, or retrieving the correct text given an image.

**Short-text-image retrieval** (1 paper: [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf))
> The task of retrieving the correct image from a set given a short, concise text query, or retrieving the correct text given an image.

**Species identification** (1 paper: [INQUIRE: A Natural World Text-to-Image Retrieval Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4ad9c75f0d60ed75700f020adb3f705-Paper-Datasets_and_Benchmarks_Track.pdf))
> Retrieving images that match a query about a particular species or taxon.

**Retrieval** (1 paper: [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf))
> Selecting the correct matching item or text from candidates based on ASL input.

## Relationships

### Cross-modal retrieval →
- **MS-COCO** (measurement instrument): *measured_by*, 10 papers
  > We evaluate the performance of Causal Q-Former on the image-text retrieval using COCO (Lin et al., 2014) and Flickr30K (Young et al., 2014). (Section 4)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
  - [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
  - [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf)
  - [An End-To-End Graph Attention Network Hashing for Cross-Modal Retrieval](https://proceedings.neurips.cc/paper_files/paper/2024/file/03e7eaa586f0990c633f8a8e57e08ca6-Paper-Conference.pdf)
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf)
  - [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf)
- **Flickr30k** (measurement instrument): *measured_by*, 9 papers
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
- **CUB-200-2011** (measurement instrument): *measured_by*, 1 paper
  > we provide several image-to-text retrieval cases on CelebA-HQ and CUB-200 datasets based on VQ-GAN+LG. (Section 4.3)
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **AudioCaps** (measurement instrument): *measured_by*, 1 paper
  > “Table 3: Semantic retrieval (R@1, R@5, and R@10) for CLAP and ELSA calculated over the original (non-spatial) versions of Clotho and AudioCaps.”
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Clotho** (measurement instrument): *measured_by*, 1 paper
  > “Table 3: Semantic retrieval (R@1, R@5, and R@10) for CLAP and ELSA calculated over the original (non-spatial) versions of Clotho and AudioCaps.”
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Winoground** (measurement instrument): *measured_by*, 1 paper
  > Image-text matching evaluation through binary retrieval tasks... We report results on two benchmarks (Winoground (Thrush et al., 2022), EqBen (Wang et al., 2023b))
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > [IMAGE-TEXT MATCHING] aims to evaluate the ability of models to understand the meaning of a text snippet and match it with the corresponding visual content or vice versa. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **MSR-VTT** (measurement instrument): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **MSVD** (measurement instrument): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **LSMDC** (measurement instrument): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **DiDeMo** (measurement instrument): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **VisDial** (measurement instrument): *measured_by*, 1 paper
  > In cross-modal retrieval, we use the Visual Dialog (Das et al., 2017) dataset for the comparability to previous work (Koh et al., 2023).
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)

### → Cross-modal retrieval
- **Ranking** (behavioral indicator): *causes*, 1 paper
  > We find that MLLMs can be used as zero-shot rerankers to further boost retrieval accuracy in challenging tasks that require the understanding of multimodal queries, such as ... composed image retrieval. (Section 6)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)

### Associated with
- **Modality bias** (construct), 1 paper
  > it underperforms compared to a smaller CLIP retriever in cross-modal retrieval tasks due to the modality bias exhibited by MLLMs. (Section 1)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > The long-text-image retrieval task necessitates the alignment of text features from long texts with the image features from the corresponding images, which thereby evaluates the model’s ability to comprehend long texts. (Section 4.1)
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **Multimodal alignment** (construct), 1 paper
  > In our study, we evaluate pretrained models’ cross-modal alignment efficacy by conducting both zero-shot text-to-image and image-to-text retrieval tasks in multiple hierarchical levels. (Section 4.2)
  - [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf)
