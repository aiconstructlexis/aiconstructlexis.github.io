# AI2D
**Type:** Measurement instrument  
**Supporting papers:** 44  

## State of the Field

**What it is.** Across definitions, AI2D is most commonly described as a benchmark or dataset for diagram understanding and question answering. Papers variously specify science, textbook, or grade school science diagrams, and some describe multiple-choice questions, diagram parsing, or exhaustive annotations of constituents and relationships over more than 5,000 diagrams and 15,000 question-answer pairs. A few papers refer to variants or subsets such as AI2D-Test and AI2D-RST, the latter described as "a multimodal corpus of 1000 primary school science diagrams".

**What it is claimed to measure.** Papers use AI2D to measure 3 behavioral indicators and 3 constructs. The recurring behavioral claims are diagram understanding, chart and diagram understanding, and multiple-choice visual question answering, while the construct-level claims link it to multimodal perception, multimodal reasoning, and visual reasoning. Across these links, the prevailing framing stays close to diagram comprehension: papers say it gauges "diagram comprehension," "science diagram comprehension," or challenges of "diagram interpretation and reasoning."

**Space of uses.** Across evaluation setups, papers usually place AI2D inside larger benchmark suites alongside MME, MMBench, ScienceQA, MMMU, and ChartQA. They position it as a benchmark for visual question answering, image-level evaluation, perception and reasoning suites, and sometimes as a domain-specific check for diagram comprehension.

**Concerns raised.** One paper, discussing AI2D-Test, reports that AI2D exhibits an "amazing abnormal hit rate" of 46.2%.

## Sources

**AI2D** (14 papers: [LiveXiv - A Multi-Modal live benchmark based on Arxiv papers content](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa1373fe55b223c2dfe1fd29a277d7-Paper-Conference.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bc/li25bc.pdf), [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf), [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf), [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf), [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf), [NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e69ff56d0ebff0752ff29caaddc25dd-Paper-Datasets_and_Benchmarks_Track.pdf), [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf), [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf), [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf))
> The Allen Institute for AI Diagrams (AI2D) benchmark, an established dataset for diagram understanding and question answering.

## Relationships

### → AI2D
- **Diagram understanding** (behavioral indicator): *measured_by*, 4 papers
  > For domain-specific evaluations, we choose AI2D to gauge diagram comprehension (Section 5.2)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
- **Chart and diagram understanding** (behavioral indicator): *measured_by*, 1 paper
  > Benchmarks that involve spatial understanding and fine-grained features include ... chart understanding (AI2D; Kembhavi et al. 2016)... (Section 5)
  - [Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf)
- **Visual reasoning** (construct): *measured_by*, 1 paper
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Multiple-choice visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > Note that SQA-I, AI2D, RWQA and MMMU are MCVQ datasets, while the others are VQA. (Section 5.1)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > To further investigate how well M-STAR generalizes to multiple benchmarks, we select four extra multi-modal ones focus on reasoning as well: M3CoT (Chen et al., 2024b), MMStar (Chen et al., 2024a), MMBench (Dev set, v1.1) (Liu et al., 2025), AI2D (Kembhavi et al., 2016). (Section 4.2)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **Multimodal perception** (construct): *measured_by*, 1 paper
  > “Perception: Following (Tong et al., 2024a), we conduct experiments on 4 types of perception task (i.e., general, knowledge, ocr, and vision-centric) across 16 benchmarks: MME (Fu et al., 2023), MMBench (Liu et al., 2025), SEED (Li et al., 2024), GQA (Hudson & Manning, 2019), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), OCRBench (Liu et al., 2024), TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021), MMVP (Tong et al., 2024b), RealworldQA (xAI, 2024), and CV-Bench (Tong et al., 2024a).”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
