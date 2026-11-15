# OK-VQA
**Type:** Measurement instrument  
**Supporting papers:** 45  
**Also known as:** OKVQA  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats OK-VQA as an open-ended visual question answering benchmark or dataset whose questions require knowledge beyond what is directly visible in the image. Most definitions describe this as external or outside knowledge, while some specify commonsense, world knowledge, reasoning, or general knowledge questions; one study describes it as focusing on knowledge-based questions, one calls it open-domain, and some papers refer specifically to the validation split.

**What it is claimed to measure.** Papers use OK-VQA to measure one behavioral indicator, Visual question answering, and six constructs. The most frequently linked constructs are Multimodal understanding, World knowledge, Generalization, and In-context learning, and papers also link it to other constructs, so the reported measurement claims are spread across several uses rather than centered on one; in these accounts it is used to assess multimodal vision-language capabilities, generalization ability, few-shot or in-context learning, and questions requiring outside or world knowledge.

**Space of uses.** In practice, papers usually place OK-VQA inside broader multimodal or VQA evaluation suites, often alongside VQAv2, TextVQA, VizWiz, GQA, and A-OKVQA. It is variously presented as one of several image question answering tasks, one of several multimodal understanding benchmarks, or one of a few knowledge-based visual reasoning benchmarks, and papers use it in zero-shot, few-shot, four-shot and eight-shot in-context settings, for long-context evaluation, and in one case as the basis for another benchmark's category scheme.

## Sources

**OK-VQA** (12 papers: [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf), [Knowledge Image Matters: Improving Knowledge-Based Visual Reasoning with Multi-Image Large Language Models](https://aclanthology.org/2025.acl-long.1063.pdf), [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf), [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf), [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf), [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf), [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf), [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf), [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf), [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf), [Understanding Information Storage and Transfer in Multi-Modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf), [Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fbf5efe979e6754dc06a0869233f2510-Paper-Datasets_and_Benchmarks_Track.pdf))
> Open-ended Knowledge-based Visual Question Answering, a benchmark used to assess multimodal question answering requiring external knowledge.

**OKVQA** (6 papers: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf), [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf))
> The Outside Knowledge Visual Question Answering (OK-VQA) dataset, which requires external knowledge to answer questions about images.

## Relationships

### → OK-VQA
- **Visual question answering** (behavioral indicator): *measured_by*, 16 papers
  > We first quantitatively evaluate the zero-shot multi-modal understanding capacity of LaVIT on ... Visual Question Answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019), GQA (Hudson & Manning, 2019), VizWiz (Gurari et al., 2018)). (Section 4.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf)
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
  - [A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf)
  - [Backdooring Vision-Language Models with Out-Of-Distribution Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/da37068018f8f7185720b83ea6f48377-Paper-Conference.pdf)
  - [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
- **Multimodal understanding** (construct): *measured_by*, 2 papers
  > “We evaluate Emu on a broad range of vision-language tasks including image question answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019)”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 2 papers
  > OKVQA (Marino et al., 2019) for external knowledge
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fbf5efe979e6754dc06a0869233f2510-Paper-Datasets_and_Benchmarks_Track.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **Knowledge reasoning** (construct): *measured_by*, 1 paper
  > OKVQA (Marino et al., 2019), Visual Common Sense Reasoning (VCR) (Zellers et al., 2019) and A-OKVQA (Schwenk et al., 2022) evaluate whether models are able to integrate outside knowledge in order to answer questions, covering a broad base of common-sense and world knowledge. (Section 2.1)
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)
