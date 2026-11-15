# OCRBench
**Type:** Measurement instrument  
**Supporting papers:** 25  
**Also known as:** OCR-Bench  

## State of the Field

**What it is.** Across papers, OCRBench is most commonly described as a benchmark for optical character recognition, often framed as evaluating OCR capabilities or text reading and text understanding in images or other visual inputs. Some authors use the spelling OCR-Bench, and one source abbreviates it as OCRB. A smaller line of description says it assesses a model's ability to recognize and reason about text within images using OCR tasks, but the prevailing usage remains an OCR-focused benchmark for large multimodal models.

**What it is claimed to measure.** Papers use OCRBench to measure one behavioral indicator and three constructs. The dominant measurement claim is optical character recognition, and additional papers report it as measuring fine-grained visual understanding, fine-grained perception, and multimodal perception. Overall, the measurement claims center on OCR, with some broader perception-oriented framing around the same benchmark.

**Space of uses.** Across papers, OCRBench is usually used as part of broader evaluation suites rather than in isolation. It is frequently grouped with DocVQA, ChartQA, TextVQA, and InfoVQA in OCR-related, OCR-extensive, or OCR/document/chart understanding evaluations, and some papers place it among widely-adopted VLM benchmarks or general datasets. Papers also position it within fine-grained or perception-focused evaluation setups.

## Sources

**OCRBench** (6 papers: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf), [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf), [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf))
> A benchmark for optical character recognition and text reading in visual inputs.

**OCR-Bench** (1 paper: [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf))
> A benchmark designed to evaluate the Optical Character Recognition (OCR) capabilities of large multimodal models.

## Relationships

### → OCRBench
- **Optical character recognition** (behavioral indicator): *measured_by*, 2 papers
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Fine-grained visual understanding** (construct): *measured_by*, 1 paper
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Fine-grained perception** (construct): *measured_by*, 1 paper
  > Ablation results on fine-grained perception tasks. We conduct ablation studies based on LLaVA across five fine-grained benchmarks: ... OCRBench (Liu et al., 2024b)... (Table 3)
  - [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf)
