# SlideVQA
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the papers, SlideVQA is most commonly described as a public, open-source dataset for visual question answering on presentation slides. The prevailing description adds that each document consists of 20 pages, and one paper further specifies splits of 1,919 slides for training, 400 for test, and 300 for development. A smaller usage describes it more generally as a visual document question-answering dataset that can serve as source material for query refinement.

**What it is claimed to measure.** Across reported uses, papers use SlideVQA to measure 2 behavioral indicators and no constructs. The linked indicators are Information retrieval and Visual question answering, so its reported measurement use is spread across those two tasks rather than centered on any construct. One paper evaluates retrieval accuracy on SlideVQA, while another includes it among VQA datasets used for presentation slides.

**Space of uses.** Papers use SlideVQA in several roles. In one evaluation setup, it appears alongside MM-LongBench, DUDE, DocVQA, and VisR-Bench when comparing retrieval accuracy baselines. Other papers use it as a source of question-document pairs for presentation slides, or describe data construction as derived from refining queries in SlideVQA.

## Sources

**SlideVQA** (2 papers: [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf), [ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents](https://aclanthology.org/2025.emnlp-main.464.pdf))
> A public dataset for visual question answering on presentation slides, where each document consists of 20 pages.

## Relationships

### → SlideVQA
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: ... and SlideVQA (Tanaka et al., 2023) for presentation slides. (Sec. 3.3)
  - [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
