# VSR
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Visual Spatial Reasoning  

## State of the Field

**What it is.** Papers most commonly treat VSR, or Visual Spatial Reasoning, as a closed-set benchmark for spatial reasoning over images, testing a model's understanding of coarse object spatial relationships. Some definitions also describe it as the Visual Spatial Reasoning dataset, rich in spatial relational information among objects in images, and one paper places it among single-image benchmarks that test alignment between single images and multiple captions.

**What it is claimed to measure.** Across the papers, VSR is linked to one construct, Spatial reasoning, and no behavioral indicators. The prevailing usage is as a measure of spatial reasoning, with papers referring to it as one of the spatial reasoning benchmarks and reporting results on visual spatial reasoning in VSR.

**Space of uses.** Papers use VSR for evaluation, commonly alongside other spatial reasoning benchmarks. The cited benchmark suites place it with SPEC, Whatsup, and EmbSpatial, and one paper also includes it in a set of single-image benchmarks used to evaluate fine-grained visual-language understanding; no other measurement instrument is directly linked to it.

## Sources

**VSR** (3 papers: [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf), [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf), [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf))
> A closed-set benchmark that tests a model's understanding of coarse object spatial relationships.

**Visual Spatial Reasoning** (1 paper: [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf))
> A benchmark for spatial reasoning over images, used here for evaluation.

## Relationships

### → VSR
- **Spatial reasoning** (construct): *measured_by*, 3 papers
  > Similarly, on spatial reasoning benchmarks (SPEC, Whatsup, VSR), VisMin-CLIP showed an average 7.79% improvement over NegCLIP and 5.21% over CounterCurate-CLIP. (Section 6.1)
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
  - [Why Is Spatial Reasoning Hard for VLMs? An Attention Mechanism Perspective on Focus Areas](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cr/chen25cr.pdf)
