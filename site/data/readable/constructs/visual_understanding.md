# Visual understanding
**Type:** Construct  
**Supporting papers:** 95  
**Also known as:** Single-image visual understanding, Image comprehension, Image understanding, Visual comprehension, Vision understanding, Medical visual comprehension, Structured image understanding, Visual-semantic understanding, Global image comprehension, Image comprehension ability, Image-level understanding, Visual information comprehension, Image-level visual perception, Visual interpretation, Visual interpretation capability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats visual understanding as a latent ability to comprehend and interpret visual inputs, usually images, well enough to extract relevant information from their content and context. Many definitions keep this broad, covering recognition of objects, scenes, relations, or fine-grained content, while some make the standard more explicit by stressing query-relevant extraction, alignment between image content and questions, or reliance on the image rather than textual priors. A smaller line of work narrows the construct to particular settings, such as single-image inputs, molecular spectra, handwritten math images, multimodal documents, structured images like tables and charts, medical images, or whole-image and global image comprehension.

**Space of facets.** Papers systematize the construct mainly by granularity and domain. Granularity framings include single-image, image-level, and global image comprehension, and one paper places image-level understanding alongside object-level and pixel-level understanding and reasoning tasks; other papers emphasize structured image understanding or visual-semantic understanding, where visual observations are integrated with textual context and task instructions. Terminology is also varied: image understanding, image comprehension, visual comprehension, vision understanding, visual interpretation, and visual information comprehension are used for closely related abilities, sometimes with domain qualifiers such as medical or chemistry-focused use.

**Space of measurement.** Operationalization is broad but benchmark-heavy: papers link visual understanding to 21 measurement instruments, mostly multimodal benchmark suites. The most frequently linked instruments are MMBench, MM-Vet, VQA-v2, GQA, and MME; papers describe these as covering fine-grained abilities, free-form question answering evaluated with GPT-4, fundamental image understanding and question-answering, and compositional or real-world visual understanding. Papers also connect the construct to 7 behavioral indicators, and the measures usually take the form of broad benchmark performance, though some instruments target narrower facets such as visual details, text within images, charts, or domain-specific understanding.

**Links.** Beyond measurement, papers most often treat visual understanding as related to image captioning and textual reasoning, and papers claim causal relationships from visual understanding to visual question answering and hallucination. One paper also reports that brain alignment correlates with visual understanding. Other less frequent links include additional causal claims from visual understanding to reasoning abilities and from other constructs to visual understanding, plus related links involving dialogue, classification, and bias.

## Sources

**Visual understanding** (8 papers: [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf), [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [AlgoPuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Algorithmic Multimodal Puzzles](https://aclanthology.org/2025.naacl-long.486.pdf), [DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students' Hand-Drawn Math Images](https://aclanthology.org/2025.naacl-long.352.pdf), [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf), [Unsolvable Problem Detection: Robust Understanding Evaluation for Large Multimodal Models](https://aclanthology.org/2025.acl-long.326.pdf), [Diffusion Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25g/jin25g.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf))
> The ability to interpret and extract meaningful chemical information from visual data, specifically from images of various molecular spectra.

**Single-image visual understanding** (1 paper: [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf))
> The ability to comprehend and interpret the content and context of a single visual input.

**Image comprehension** (1 paper: [MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf))
> The latent ability to understand visual inputs well enough to extract relevant query information or recognize important objects and cues.

**Image understanding** (2 papers: [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf), [Can Multimodal Large Language Models Understand Spatial Relations?](https://aclanthology.org/2025.acl-long.31.pdf))
> The model's ability to comprehend and interpret the content and context of visual data.

**Visual comprehension** (4 papers: [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf), [Movie101v2: Improved Movie Narration Benchmark](https://aclanthology.org/2025.acl-long.836.pdf), [Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luu25a/luu25a.pdf), [UnCo: Uncertainty-Driven Collaborative Framework of Large and Small Models for Grounded Multimodal NER](https://aclanthology.org/2025.emnlp-main.388.pdf))
> The latent ability to interpret and understand visual information within a language modeling framework.

**Vision understanding** (1 paper: [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf))
> The latent ability of a multimodal model to interpret, comprehend, and reason about information presented in images.

**Visual-semantic understanding** (1 paper: [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf))
> The ability to integrate visual observations with textual context to understand objects, scenes, and task instructions.

**Structured image understanding** (1 paper: [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf))
> The ability to interpret and reason about information presented in structured formats like tables and charts.

**Medical visual comprehension** (1 paper: [HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf))
> The latent ability of a model to understand and interpret medical images across various modalities and extract meaningful, clinically relevant information through language-based interaction.

**Global image comprehension** (1 paper: [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> The ability to form a coherent, integrated understanding of an entire image by connecting multiple objects and their multi-scale representations.

**Image comprehension ability** (1 paper: [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to accurately interpret visual content in multimodal documents, including details and counts of images.

**Image-level understanding** (1 paper: [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf))
> The model's ability to comprehend and reason about the entire image as a whole, including its overall scene, context, and global properties.

**Visual information comprehension** (1 paper: [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf))
> The ability to comprehend and process visual data, including capturing diverse semantic information within text-image pair data.

**Image-level visual perception** (1 paper: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> The broader ability to understand whole-image content and preserve general vision-language performance while adding region-level prompting.

**Visual interpretation** (1 paper: [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf))
> The model's ability to accurately perceive and represent the objects, relationships, and semantic content within an image.

**Visual interpretation capability** (1 paper: [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf))
> The model's ability to accurately perceive, understand, and describe the content and features of an image.

## Relationships

### Visual understanding →
- **MMBench** (measurement instrument): *measured_by*, 8 papers
  > To examine general visual understanding and instruction following of our model, we follow common practices and employ MMBench [77], MME [78], SEEDBench [79], MMMU [30] and MathVista [80] for evaluation. (Section 4.2)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf)
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 7 papers
  > Comparison with SoTAs in Image Understanding. ... Dense Connector outperforms the LLaVA-1.5 Vicuna 13B [16] with substantial gains of 2.1%, 3.7%, and 5.5% on the GQA [58], MMB [64], and MM-Vet [65] benchmarks, respectively.
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 6 papers
  > We evaluate on the widely used vision-language understanding and generation benchmarks... We report vqa-score on VQAv2... Above results show that X-MoE exhibits enhanced visual information comprehension
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
- **MME** (measurement instrument): *measured_by*, 5 papers
  > In Tab. 8, we evaluate our model on recently proposed MLLM benchmarks such as MME [16], POPE [36], MMbench [42], ScienceQA [43], TextVQA [61], GQA [21]. Our model still achieves comparative results across all benchmarks. This performance indicates that the visual CoT data we proposed not only enhances visual comprehension in CoT-specific scenarios but also boosts the model's overall visual understanding in standard inference setups.
  - [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 5 papers
  > we evaluated the visual understanding ability of LMMs when visual tokens were dropped at different layers. Specifically, we measured the performance of LLaVA-v1.5 on the GQA (Hudson & Manning, 2019) and MMBench (Liu et al., 2024c) (Section 3.2).
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
- **POPE** (measurement instrument): *measured_by*, 4 papers
  > Our study investigates the performance of DYNMOE-LLaVA on image understanding benchmarks. Evaluation Benchmarks include VQA-v2; GQA; VisWiz; SQAI (ScienceQA-IMG); VQAT (TextVQA); POPE; MME; MMB (MMBench); LLaVAW (LLaVA-Bench (in-the-Wild)); MM-Vet. (Table 2)
  - [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)
- **MMMU** (measurement instrument): *measured_by*, 4 papers
  > For image understanding, we reported scores from popular benchmarks like MM-Vet (Yu et al., 2023), MMBench (Liu et al., 2023b), MMMU (Yue et al., 2024), MME (Fu et al., 2023), LLaVA-wild (Liu et al., 2024b), SEED (Ge et al., 2023b), AI2D (Kembhavi et al., 2016), and RealWorldQA (xAI, 2024). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
  - [Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.354.pdf)
  - [Private Attribute Inference from Images with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb97e9a7c811904c9b01f51fde66edcf-Paper-Conference.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 3 papers
  > For examining visual understanding ability, we evaluate our model on the widely adopted zero-shot image-based visual-language benchmarks including VQAv2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023d), MME (Fu et al., 2024), SEED (Li et al., 2023a), MM-Vet (Yu et al., 2023b) (Section 4.1)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **MMVP** (measurement instrument): *measured_by*, 3 papers
  > MMVP [53] aims to evaluate the understanding of visual details for 9 different visual patterns using paired classification accuracy. (Section 4)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 3 papers
  > LLaVA-Bench consists of 60 carefully designed open-ended questions across 24 images, evaluating models’ visual reasoning and understanding capabilities. (Sec. 6.1)
  - [Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention](https://aclanthology.org/2025.acl-long.634.pdf)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 2 papers
  > For examining visual understanding ability, we evaluate our model on the widely adopted zero-shot image-based visual-language benchmarks including VQAv2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023d), MME (Fu et al., 2024), SEED (Li et al., 2023a), MM-Vet (Yu et al., 2023b) (Section 4.1)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 2 papers
  > VizWiz [23] consists of images taken by visually impaired individuals paired with questions they pose about these images, making it crucial for developing AI systems that assist in real-world, accessibility-focused visual understanding tasks. (Section 4.3)
  - [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **CV-Bench 2D** (measurement instrument): *measured_by*, 2 papers
  > Vision-centric task evaluates visual understanding capabilities... We use MMVP (Tong et al., 2024b), CV-Bench2D, and CV-Bench3D (Tong et al., 2024a).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator): *causes*, 2 papers
  > Large vision-language models (LVLMs) have demonstrated remarkable image understanding and dialogue capabilities, allowing them to handle a variety of visual question answering tasks. (ABSTRACT)
  - [Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d368eba3fb546ae5d868dae2ecb17200-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **SciQA** (measurement instrument): *measured_by*, 1 paper
  > For vision understanding evaluations, we use the commonly used vision understanding benchmarks to evaluate the performance similar as LLaVA-1.5, such as VQAv2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), VizWiz (Gurari et al., 2018), SciQA (Lu et al., 2022), TextVQA (Singh et al., 2019), POPE (Li et al., 2023b), MMBench (en) (Liu et al., 2023b), SEED (image) (Li et al., 2023a) and MM-Vet (Yu et al., 2023). (Section 4.1)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **NLVR2** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on the widely used vision-language understanding and generation benchmarks... accuracy for NLVR2... Above results show that X-MoE exhibits enhanced visual information comprehension
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **COCO Caption** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on the widely used vision-language understanding and generation benchmarks... For COCO image captioning... Above results show that X-MoE exhibits enhanced visual information comprehension
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > Despite the task being focused on mathematical reasoning, STIC enhanced the model’s response by improving its image comprehension capabilities. (Section 6)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > To assess their visual understanding capability, numerous benchmarks have been developed, focusing on question-answering tasks, such as MMVet (Yu et al., 2023), MMStar (Chen et al., 2024a), and MMMU (Yue et al., 2024). (Section 1)
  - [Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf)
- **Out-of-distribution detection** (behavioral indicator): *causes*, 1 paper
  > We found that one of the reasons for this discrepancy is the insufficient image interpretation capabilities of these models, which limits their ability to accurately distinguish between ID and OoD inputs. (Section 1)
  - [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **ChartMimic** (measurement instrument): *measured_by*, 1 paper
  > ChartMimic places emphasis on evaluating LMMs’ capacity to harmonize a blend of cognitive capabilities, encompassing visual understanding, code generation, and cross-modal reasoning. (Abstract)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > engaging the MLLMs with a more powerful capability of image understanding so as to enhance the mitigation of hallucination. (Section 1)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
- **MME-P** (measurement instrument): *measured_by*, 1 paper
  > “For visual understanding and generation, Orthus achieves a GenEval score of 0.58 and an MME-P score of 1265.8”
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)
- **Multimodal reasoning** (construct): *causes*, 1 paper
  > the enhanced visual comprehension ability directly benefits the model performance and its multimodal reasoning ability. (Section 4)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **ScienceQA-IMG** (measurement instrument): *measured_by*, 1 paper
  > TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)

### → Visual understanding
- **Visual recognition** (construct): *causes*, 1 paper
  > visual recognition is potential to benefit all understanding tasks as recognition results are important compositions for understanding. (Section 1)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Brain alignment** (construct): *correlates*, 1 paper
  > Instructions related to image understanding (e.g., “describe the most dominant color”) result in higher brain alignment in early visual regions for both the InstructBLIP and mPLUG-OWL models...
  - [Correlating instruction-tuning (in multimodal models) with vision-language processing (in the brain)](https://proceedings.iclr.cc/paper_files/paper/2025/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *causes*, 1 paper
  > "train abstract-grained visual adapters using high-quality image-text pairs to align visual embeddings with textual embeddings, thereby enabling the model to accurately describe medical visual content."
  - [HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf)
- **Language bias** (construct): *causes*, 1 paper
  > "LACING effectively debiases LVLMs from their language bias, enhancing visual comprehension and reducing hallucinations"
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)

### Associated with
- **Image captioning** (behavioral indicator), 4 papers
  > Our OMG-LLaVA unifies image-level (such as image caption and image-based conversation), object-level (such as region caption and visual prompt-based conversation), and pixel-level (such as universal segmentation, referring segmentation, reasoning segmentation, and grounded conversation generation) visual understanding and reasoning tasks into token-to-token generation. (Section 3.1)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Multimodal Situational Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cb57fcf7ff3f6d37eebae5becc9ea6d-Paper-Conference.pdf)
- **Textual reasoning** (behavioral indicator), 2 papers
  > This indicates that VLMs are capable of textual reasoning. This finding suggests that the reasoning challenge does not mainly lie in the VLM’s textual components but in the visual ones. (Page 8)
  - [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf)
  - [ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom](https://aclanthology.org/2025.emnlp-main.1614.pdf)
- **Visual dialogue** (behavioral indicator), 1 paper
  > Our OMG-LLaVA unifies image-level (such as image caption and image-based conversation), object-level (such as region caption and visual prompt-based conversation), and pixel-level (such as universal segmentation, referring segmentation, reasoning segmentation, and grounded conversation generation) visual understanding and reasoning tasks into token-to-token generation. (Section 3.1)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Cultural bias** (construct), 1 paper
  > In this work, we characterize the Western bias of VLMs in image understanding and investigate the role that language plays in this disparity. (Section 1)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Image classification** (behavioral indicator), 1 paper
  > To study the performance of the joint inference framework on tasks that require visual comprehension, we evaluate our methods on seven vision datasets, spanning both image classification tasks (CIFAR-10, CIFAR-100, Food101) and visual question-answering tasks (COCO-Color, COCO-Number, VQAv2 and VizWiz). (Section 5.2)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
