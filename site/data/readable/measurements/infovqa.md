# InfoVQA
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** InfographicVQA, InfographicsVQA  

## State of the Field

**What it is.** Papers most commonly describe InfoVQA, sometimes written as InfographicVQA or InfographicsVQA, as a visual question answering benchmark or dataset for infographics or infographic images. Some descriptions instead frame it as information visual question answering on document images, emphasizing information localization, extraction, or extracting specific information, and one definition places it among prior single-page document understanding datasets. One paper also characterizes the infographics setting as high-resolution and requiring interpretation of charts and graphical data.

**What it is claimed to measure.** Papers link this instrument to 2 constructs and 1 behavioral indicator. The prevailing claim is that papers use it to measure document understanding, while smaller lines of work also report it as measuring fine-grained visual understanding and optical character recognition. Beyond document understanding, its reported measurement use therefore extends to OCR-related and fine-grained visual evaluation.

**Space of uses.** Papers usually deploy it within broader benchmark suites, commonly alongside DocVQA, ChartQA, TextVQA, and OCRBench, and sometimes with STVQA. In these evaluations, papers position it as part of OCR-related, document-understanding, or textual-reasoning task collections.

**Concerns raised.** When papers discuss pruning or masking on this benchmark, they note that it requires fine-grained visual information and can be highly sensitive to potential information loss in vision tokens. Papers also describe tasks such as InfoVQA as often requiring understanding only small portions of text within an image.

## Sources

**InfoVQA** (4 papers: [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf))
> Information visual question answering benchmark referenced as a prior single-page document understanding dataset.

**InfographicVQA** (1 paper: [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf))
> A visual question answering benchmark for infographic images.

**InfographicsVQA** (2 papers: [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf), [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf))
> A dataset for visual question answering on high-resolution infographics, requiring models to interpret charts and graphical data.

## Relationships

### → InfoVQA
- **Document understanding** (construct): *measured_by*, 1 paper
  > For document understanding, ... We utilize benchmarks such as ChartQA (Masry et al., 2022), DocVQA (Mathew et al., 2021), InfoVQA (Mathew et al., 2022), TextVQA (Singh et al., 2019), STVQA (Biten et al., 2019), FUNSD (Jaume et al., 2019), SROIE (Huang et al., 2019), POIE (Kuang et al., 2023) and OCR-Bench (Liu et al., 2023c). (Section 4.1)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
- **Optical character recognition** (behavioral indicator): *measured_by*, 1 paper
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Fine-grained visual understanding** (construct): *measured_by*, 1 paper
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
