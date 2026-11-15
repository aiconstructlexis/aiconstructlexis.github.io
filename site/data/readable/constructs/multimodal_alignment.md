# Multimodal alignment
**Type:** Construct  
**Supporting papers:** 73  
**Also known as:** Cross-modal alignment, Vision-language alignment, Multi-modal alignment, Cross-modal knowledge alignment, Cross-modality alignment, Cross-modal semantic alignment, Video-language alignment, Image-text alignment, Audio-visual alignment, Visual-language alignment, Visual-text alignment, Image-text modality alignment, Visual-linguistic alignment, Text alignment, Vision-text alignment, Visual-textual token alignment, Visual-semantic consistency, Prompt faithfulness, Audio-visual content consistency, Logical awareness, Modality alignment, Diagram-language alignment, Alignment quality  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats multimodal alignment as a latent ability, or sometimes a degree, of semantic correspondence across modalities, most often vision and language. In this dominant framing, representations are mapped into a shared or coherent space, can "contain the same information," and support grounded multimodal understanding. Papers largely agree on the need for matched semantics across modalities, but differ on where the construct resides: most definitions place it in internal representations, while a smaller line of work defines it through output faithfulness, such as answers consistent with an image, text faithful to video content, generated images satisfying prompts, or models reasoning with both modalities rather than ignoring one.

**Space of facets.** Paper terminology is broad but largely overlapping, with cross-modal alignment, vision-language alignment, modality alignment, image-text alignment, and video-language alignment used for closely related notions of semantically matched multimodal information, plus other modality-specific variants. Some papers decompose alignment into finer units, including instance-, temporal-, and perceptive-level alignment, as well as hierarchical, sub-unit, token-level, or region-level forms. Other labels recast specific facets rather than a wholly separate construct, for example prompt faithfulness or alignment quality.

**Space of measurement.** Papers link the construct to 7 measurement instruments and 5 behavioral indicators. The most common instruments are benchmark or dataset-based evaluations, especially ImageNet-1k, MS-COCO, CC3M, CHAIR, and CIFAR-10, with 2 other instruments also used; operationalizations include alignment scores on held-out sets, zero-shot image classification, image-text retrieval, reconstruction or text-alignment metrics, object-focused benchmark analyses, and one judge-based setup that assesses caption fluency and image alignment. Quoted passages also describe representation-focused analyses through visual-linguistic inconsistency, cross-modal assignment prediction, token or embedding similarity, and layerwise distance calculations, while linked behavioral indicators bring in retrieval and hallucination-related performance. These measures mostly line up with shared-space definitions, though some operationalize the construct as downstream faithfulness of outputs.

**Links.** Across its 5 linked behavioral indicators and 10 linked constructs, most reported links are causal claims from multimodal alignment to downstream outcomes. The most recurrent claim is a causal relationship from multimodal alignment to hallucination, and papers also claim causal relationships from multimodal alignment to visual perception, factuality, hallucination resistance, and modality gap; the supporting language often describes misalignment as producing outputs not grounded in visual input or favoring text over images. Some papers instead report related, noncausal links in retrieval- or segmentation-oriented settings, and additional single-paper claims attach multimodal alignment to several other constructs. A smaller line of work reverses the direction by treating multimodal alignment as an effect rather than a source.

## Sources

**Cross-modal alignment** (6 papers: [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf), [VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf), [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf), [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf), [Foundation Molecular Grammar: Multi-Modal Foundation Models Induce Interpretable Molecular Graph Languages](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25aa/sun25aa.pdf), [Exploring How Generative MLLMs Perceive More Than CLIP with the Same Vision Encoder](https://aclanthology.org/2025.acl-long.499.pdf))
> The latent ability of a model to ensure that representations from different modalities (e.g., vision and language) encode equivalent semantic information, enabling interoperability between them.

**Vision-language alignment** (4 papers: [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf), [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf))
> The latent ability of a model to integrate and relate visual and linguistic information into a coherent joint representation, enabling understanding of multimodal inputs.

**Multimodal alignment** (4 papers: [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf), [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf))
> The latent ability of a model to connect and integrate information from visual and textual modalities, creating a shared semantic space.

**Multi-modal alignment** (1 paper: [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf))
> The degree to which a vision-language model forms semantically aligned representations across modalities, enabling effective use of multi-modal context.

**Modality alignment** (5 papers: [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf), [Mitigating Spurious Correlations in Zero-Shot Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2649b1d435f02524812ccbcae0dfe48b-Paper-Conference.pdf), [Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf), [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf), [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf))
> The degree to which a model effectively bridges and correlates information between visual and textual representations internally.

**Cross-modal knowledge alignment** (1 paper: [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf))
> The ability to correctly associate textual concepts, especially knowledge-intensive ones like landmarks or species, with their corresponding visual representations.

**Cross-modality alignment** (2 papers: [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf), [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf))
> The extent to which a model correctly integrates and reasons over information from different modalities, such as medical images and text, rather than relying on one while ignoring the other.

**Cross-modal semantic alignment** (1 paper: [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf))
> The degree to which a model's internal representations for images and their corresponding textual descriptions are congruent in semantic space.

**Video-language alignment** (1 paper: [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf))
> The degree to which a model's textual outputs accurately and coherently correspond to the semantic content of a given video input.

**Image-text alignment** (1 paper: [Corrupted but Not Broken: Understanding and Mitigating the Negative Impacts of Corrupted Data in Visual Instruction Tuning](https://aclanthology.org/2025.emnlp-main.1317.pdf))
> The latent ability to match visual content with textual instructions and responses so that answers are consistent with the image.

**Audio-visual alignment** (1 paper: [Audio-centric Video Understanding Benchmark without Text Shortcut](https://aclanthology.org/2025.emnlp-main.333.pdf))
> The latent ability to integrate and synchronize information across auditory and visual modalities, such as linking spoken words to visual characters, objects, or on-screen text, or aligning audio segments with corresponding video frames.

**Visual-language alignment** (1 paper: [Proactive Assistant Dialogue Generation from Streaming Egocentric Videos](https://aclanthology.org/2025.emnlp-main.605.pdf))
> The degree to which a model integrates visual percepts with linguistic representations to produce contextually grounded responses.

**Visual-text alignment** (1 paper: [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf))
> The latent capacity of a VLLM to identify and leverage correspondences between visual content and textual input, ensuring that relevant visual tokens are aligned with the semantic context of the question or prompt.

**Image-text modality alignment** (1 paper: [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf))
> The degree to which a model correctly associates textual concepts with corresponding visual evidence in an image, forming the basis for cross-modal understanding.

**Visual-linguistic alignment** (1 paper: [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf))
> The latent ability of a model to correctly associate textual descriptions with corresponding visual regions in an image.

**Text alignment** (1 paper: [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf))
> The degree to which the model's internal representations of visual content are semantically aligned with corresponding textual descriptions.

**Visual-textual token alignment** (1 paper: [Parrot: Multilingual Visual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ad/sun25ad.pdf))
> The degree to which visual features extracted from images are semantically aligned with textual tokens in a given language, enabling coherent multimodal understanding and generation.

**Vision-text alignment** (1 paper: [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf))
> The degree to which a model's textual outputs accurately correspond to the visual elements and context present in an image.

**Visual-semantic consistency** (1 paper: [FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf))
> The degree to which the model's visual representations maintain a coherent and meaningful alignment with their corresponding semantic (textual) representations across different levels of granularity.

**Prompt faithfulness** (1 paper: [Who Evaluates the Evaluations? Objectively Scoring Text-to-Image Prompt Coherence Metrics with T2IScoreScore (TS2)](https://proceedings.neurips.cc/paper_files/paper/2024/file/9b9cfd5428153ccfbd4ba34b7e007305-Paper-Conference.pdf))
> The degree to which a generated image semantically aligns with and satisfies the requirements of the text prompt it was conditioned on.

**Audio-visual content consistency** (1 paper: [AGAV-Rater: Adapting Large Multimodal Model for AI-Generated Audio-Visual Quality Assessment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25f/cao25f.pdf))
> The latent ability of a model to perceive whether the audio aligns semantically and contextually with the visual content in a video, reflecting coherence between modalities.

**Logical awareness** (1 paper: [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf))
> The model's latent awareness of logical relationships between time series data and language prompts, ensuring semantic coherence.

**Diagram-language alignment** (1 paper: [MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf))
> The degree to which visual representations of mathematical diagrams are aligned with language representations so the model can correctly interpret diagram content in text form.

**Alignment quality** (1 paper: [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf))
> A quantifiable measure of the semantic correspondence and proximity between visual token embeddings and their corresponding text representations in the language model's input space.

## Relationships

### Multimodal alignment →
- **Hallucination** (behavioral indicator): *causes*, 6 papers
  > Misalignment between modalities can lead to safety risks such as biased or inappropriate content generation (Gong et al., 2023; Tu et al., 2023) and hallucinations, where outputs are not grounded in visual input (Wang et al., 2023).
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf)
  - [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 2 papers
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... ImageNet-1K ... test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **MS-COCO** (measurement instrument): *measured_by*, 2 papers
  > such fine-tuning also enhances foundational VLMs’ general image-text alignment capabilities as evident by marked improvements in CLIP’s image-text retrieval performance on COCO. (Section 1)
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **Visual perception** (construct): *causes*, 2 papers
  > This suggests a misalignment between its visual and language abilities, hindering complex board recognition. (Section 4.1)
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **Object hallucination** (behavioral indicator): *causes*, 1 paper
  > this design leads to long-term decay [61] in multimodal alignment... but induces insufficient interactions between visual tokens and instruction tokens, leading to inferior multimodal alignment and object hallucinations in the trained LVLMs (see our experiments in Sec. 3 for details). (Introduction)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Multimodal understanding** (construct): *causes*, 1 paper
  > “it is required to involve more image-text pairs for multimodal alignment and more image tokens to represent an image for better comprehending the image information.”
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Modality gap** (construct): *causes*, 1 paper
  > AlignCLIP increases the cross-modal alignment, and thereby reduce the modality gap.
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **CC3M** (measurement instrument): *measured_by*, 1 paper
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the validation sets from CC3M... (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **CIFAR-100** (measurement instrument): *measured_by*, 1 paper
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... CIFAR-100 ... test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **CIFAR-10** (measurement instrument): *measured_by*, 1 paper
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... CIFAR-10 test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 1 paper
  > To better demonstrate how our method enhances vision-language alignment and ensures the generation of high-scoring objects, we visualize the reward distribution of generated objects on the CHAIR benchmark, as depicted in Figure 4.
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > As an early model bridging vision and language with an adaptor, LLaVA’s consistent poor performance highlights how such misalignment can impair both perception and reasoning in such tasks. (Section 4.1)
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
- **Hallucination resistance** (construct): *causes*, 1 paper
  > Due to better cross-modal alignment, our model exhibits lower degrees of hallucination
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Trustworthiness** (construct): *causes*, 1 paper
  > This misalignment undermines trustworthiness, posing challenges for reliable applications of these models in high-stakes medical scenarios (Section 1).
  - [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > GPT-4V (Achiam et al., 2023b), which assesses the fluency and alignment of captions with the given images.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **Visual understanding** (construct): *causes*, 1 paper
  > "train abstract-grained visual adapters using high-quality image-text pairs to align visual embeddings with textual embeddings, thereby enabling the model to accurately describe medical visual content."
  - [HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > However, Medical LVLMs (Med-LVLMs) encounter factuality issues due to modality misalignment, where the models prioritize textual knowledge over visual input, causing hallucinations that conflict with medical images. (Abstract)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)

### → Multimodal alignment
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > The tool use, planning, and reflection steps operate cyclically to become an agentic workflow where audio signals are gradually aligned to visual content.
  - [Aligning Audio-Visual Joint Representations with an Agentic Workflow](https://proceedings.neurips.cc/paper_files/paper/2024/file/6c0ff499edc529c7d8c9f05c7c0ccb82-Paper-Conference.pdf)
- **Representation quality** (construct): *causes*, 1 paper
  > The improvement on MMStar, which emphasizes fine-grained multimodal alignment and reasoning under instruction-following settings, demonstrates DS-VLM’s ability to preserve semantic coherence across modalities through enhanced visual feature quality. (Section 4.2)
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)

### Associated with
- **Region-level understanding** (construct), 1 paper
  > we investigated the multi-modal alignment process in region-level context across intermediate layers by calculating the Wasserstein-2 distance between each layer’s region-encoded token [mask] and the last language token. (Section 3.2)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Referring expression segmentation** (behavioral indicator), 1 paper
  > Despite remarkable progress, most existing RIS works [7, 58, 27, 26, 21, 5] rely heavily on pixel-level ground-truth masks to learn visual-linguistic alignment. (Section 1)
  - [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf)
- **Cross-modal retrieval** (behavioral indicator), 1 paper
  > In our study, we evaluate pretrained models’ cross-modal alignment efficacy by conducting both zero-shot text-to-image and image-to-text retrieval tasks in multiple hierarchical levels. (Section 4.2)
  - [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf)
