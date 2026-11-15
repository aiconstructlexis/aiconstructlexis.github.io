# VQA-v2
**Type:** Measurement instrument  
**Supporting papers:** 106  
**Also known as:** VQA-V2, VQA, VQA v2, VQAv2, VQAV2  

## State of the Field

**What it is.** Papers most commonly describe VQA-v2 as an open-ended visual question answering benchmark or dataset on natural images, where models answer free-form questions about images. Some descriptions add dataset structure, stating that it contains images, associated questions, and ten ground-truth answers per question, and a few papers name specific evaluation splits or subsets such as validation, test-dev, and a 32+50 subset. A smaller line of work also presents it as a more balanced version of the original VQA dataset, and some authors say its questions require understanding of vision, language, and commonsense knowledge.

**What it is claimed to measure.** Across papers, VQA-v2 is linked to 11 constructs and 2 behavioral indicators, so measurement claims are distributed across many targets. The most common links treat it as measuring visual understanding, then multimodal understanding and visual perception; it is also used to measure the behavioral indicators visual question answering and answer generation. Other papers link it to several additional constructs.

**Space of uses.** In use, papers usually place it inside larger multimodal benchmark suites, most often alongside GQA, OKVQA, VizWiz, TextVQA, and MMBench. They report zero-shot accuracy on test-dev or validation splits, use four-shot and eight-shot in-context settings in some studies, and sometimes position it as a utility check by computing standard VQA-v2 accuracy or utility metrics such as ATR-UT and AAS-UT.

**Concerns raised.** Only a minority of descriptions foreground balance and bias: some define VQAv2 as a more balanced version of the original VQA dataset or as having balanced answer distributions, and one definition says it is used to evaluate robustness to language biases.

## Sources

**VQA-V2** (9 papers: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf), [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.505.pdf), [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf), [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf), [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf), [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf), [Unveiling Encoder-Free Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e2217482fa75556f1970be809acd3f8-Paper-Conference.pdf), [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf))
> A benchmark for visual question answering on natural images.

**VQA-v2** (3 papers: [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf))
> A benchmark dataset for visual question answering (Goyal et al., 2017) that requires models to provide open-ended answers to questions about images.

**VQA** (2 papers: [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf), [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf))
> The Visual Question Answering (VQA) dataset requires models to provide a free-form natural language answer to a question about a given image.

**VQAv2** (2 papers: [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf))
> A visual question answering benchmark used to assess multimodal question answering performance.

**VQA v2** (1 paper: [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf))
> A benchmark dataset for visual question answering, comprising a large set of images, associated questions, and ten ground-truth answers per question for evaluation.

**VQAV2** (1 paper: [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf))
> A large-scale visual question answering dataset, which is a more balanced version of the original VQA dataset.

## Relationships

### → VQA-v2
- **Visual question answering** (behavioral indicator): *measured_by*, 39 papers
  > For visual question-answering, we evaluate zero-shot performance on the test-dev set of VQAv2. (Sec. 4.3).
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
  - [Rephrase, Augment, Reason: Visual Grounding of Questions for Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/eef6cb60fd59b32d35718e176b4b08d6-Paper-Conference.pdf)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
  - [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
  - [Backdooring Vision-Language Models with Out-Of-Distribution Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/da37068018f8f7185720b83ea6f48377-Paper-Conference.pdf)
  - [Language-Image Models with 3D Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a829e299ebc1c1615ddb09e98fb6ce8-Paper-Conference.pdf)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
  - [$\gamma-$MoD: Exploring Mixture-of-Depth Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
  - [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf)
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
  - [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf)
  - [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf)
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
- **Visual understanding** (construct): *measured_by*, 6 papers
  > We evaluate on the widely used vision-language understanding and generation benchmarks... We report vqa-score on VQAv2... Above results show that X-MoE exhibits enhanced visual information comprehension
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
- **Multimodal understanding** (construct): *measured_by*, 4 papers
  > “We evaluate Emu on a broad range of vision-language tasks including image question answering (VQAv2 (Goyal et al., 2017)”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Visual perception** (construct): *measured_by*, 3 papers
  > GQA and VQA-v2 evaluate the model’s visual perception capabilities on open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **Fine-grained visual understanding** (construct): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Fairness** (construct): *measured_by*, 1 paper
  > In VHELM, this is assessed by asking questions drawn from A-OKVQA [34] and VQAv2 [12] in African-American English (AAE)... (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > We introduce typos into A-OKVQA [34] and VQAv2 [12] to test the robustness against text perturbations. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > We conduct extensive experiments on multiple challenging tasks such as arithmetic, knowledge reasoning, and multimodal benchmarks spanning GSM8K, MMLU, SQA, and VQA (Abstract).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Answer generation** (behavioral indicator): *measured_by*, 1 paper
  > We experiment on samples from i) 3 datasets requiring free-form answer generation – VQA (Goyal et al., 2017), GQA, and GQA balanced (Hudson & Manning, 2019) (Section 4.1).
  - [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Visual reasoning** (construct): *measured_by*, 1 paper
  > VQAv2 Goyal et al. (2017) and VizWiz Gurari et al. (2018) test general visual reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > we selected several common comprehensive benchmarks and VQA datasets, such as ... VQAv2 ... to evaluate the general capabilities of VLMs (Section 5.1).
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
