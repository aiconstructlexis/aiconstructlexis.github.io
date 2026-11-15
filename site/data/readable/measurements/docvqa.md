# DocVQA
**Type:** Measurement instrument  
**Supporting papers:** 51  
**Also known as:** VQADoc  

## State of the Field

**What it is.** Most papers treat DocVQA as a document visual question answering benchmark or dataset for document images, where models answer questions from document text and layout. Some descriptions add scanned or photographed documents, and characterize the task as extractive, span or segment based, or as testing extraction and reasoning over document images. Papers describe its scope differently: some say it is limited to single-page documents, while another defines it as covering single-page and multi-page document QA and retrieval; one paper also uses the name VQADoc, and another refers to a DocVQAVAL split.

**What it is claimed to measure.** Across papers, the prevailing claim is that DocVQA measures document understanding. It is linked to 4 constructs and 4 behavioral indicators overall: beyond document understanding, papers use it to measure fine-grained visual understanding, long-context understanding, and multimodal perception, and among behavioral indicators it most often measures optical character recognition, with additional uses for document question answering, information retrieval, and machine reading comprehension. The reported measurement claims therefore spread across several related abilities, though document understanding and OCR-oriented evaluation are the most common framings.

**Space of uses.** Papers usually position DocVQA as one benchmark within broader evaluation suites rather than as a standalone test, often alongside TextVQA, ChartQA, OCRBench, InfoVQA, and AI2D in OCR, document understanding, or perception bundles. Other papers place it in longer-document comparisons, or reuse it as a source of question-answer pairs or a source domain for another dataset, rather than only as an evaluation endpoint.

**Concerns raised.** The clearest concern is scope: some papers say DocVQA can only assess single-page documents, or describe it as a single-page document understanding dataset, even though another paper gives a broader single-page and multi-page description. One paper says benchmarks like TextVQA and DocVQA require sufficiently high resolution to extract text in an image, and another discussion warns that repeating large-scale evaluation on tasks where DocVQA already contains many similar examples can waste resources.

## Sources

**DocVQA** (13 papers: [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf), [LongDocURL: a Comprehensive Multimodal Long Document Benchmark Integrating Understanding, Reasoning, and Locating](https://aclanthology.org/2025.acl-long.57.pdf), [Diffusion Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25g/jin25g.pdf), [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf), [ScreenQA: Large-Scale Question-Answer Pairs Over Mobile App Screenshots](https://aclanthology.org/2025.naacl-long.477.pdf), [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf), [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf), [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf), [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf), [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf), [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf))
> Document visual question answering benchmark used for evaluating single-page and multi-page document QA and retrieval.

**VQADoc** (1 paper: [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf))
> A document visual question answering benchmark used to evaluate image-based question answering on document images.

## Relationships

### → DocVQA
- **Document understanding** (construct): *measured_by*, 6 papers
  > In order to illustrate the impact of having long in-context text, we evaluate the model for document understanding on DocVQA [15] and OCR VQA [34]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
  - [MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Optical character recognition** (behavioral indicator): *measured_by*, 2 papers
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **Fine-grained visual understanding** (construct): *measured_by*, 2 papers
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > Then, we consider the document questions answering task... We adopt a dataset that originates from a Privacy Preserving Federated Learning Document VQA (PFL-DocVQA) competition (Tito et al., 2023). (Section 4.2)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > “To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. ... In order to illustrate the impact of having long in-context text, we evaluate the model for document understanding on DocVQA [15] and OCR VQA [34].”
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > DocVQA (Mathew et al., 2021) focuses on reading comprehension tasks over document images. (Section 4.1)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
