# 3D question answering
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** 3D scene VQA, 3D visual question answering  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats this behavior as answering questions about 3D objects or scenes. The inputs are most often described as point clouds or 3D models, though some definitions also allow images, multi-view images, and other modalities; a smaller framing folds captioning and grounding into 3D scene VQA, and linked evaluations make answer accuracy an explicit scoring target.

**Variants.** Papers use several nearby labels, including 3D question answering, 3D scene VQA, and 3D visual question answering. The studied settings span questions about individual objects and full scenes, with representations drawn from point clouds, 3D models, multi-view images, images, and other modalities; some work treats captioning and grounding as part of the task, and one benchmark studies indoor scenes in a format that cannot be solved using the given scene alone.

**Space of elicitation and scores.** Papers measure it with four instruments: Human evaluation, LLM-as-a-judge, SQA3D, and ScanQA. In practice, this includes answer-accuracy judgments by human evaluators and GPT-4, as well as benchmark-based evaluation on ScanQA and SQA3D.

**What it is taken as evidence of.** Rather than centering one construct, papers link this behavior to three constructs, all through related claims rather than causal or correlational ones: 3D perception, 3D understanding, and spatial reasoning. The recorded language places 3D scene VQA under 3D perception, uses 3D question answering as a representative example for 3D scene understanding tasks, and relates methods for it to spatial reasoning.

## Sources

**3D question answering** (1 paper: [LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf))
> Answering questions about 3D objects or scenes from point-cloud or 3D model inputs.

**3D scene VQA** (1 paper: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf))
> Answering questions about 3D scenes, including captioning and grounding from multi-view images.

**3D visual question answering** (1 paper: [Hypo3D: Exploring Hypothetical Reasoning in 3D](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mao25b/mao25b.pdf))
> The task of answering a natural language question based on the content of a 3D scene, which may be represented by point clouds, images, or other modalities.

## Relationships

### 3D question answering →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > "we employ both human evaluators and GPT-4 to ascertain answer accuracy"
  - [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > "we employ both human evaluators and GPT-4 to ascertain answer accuracy"
  - [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ScanQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the proposed cdViews on two widely used benchmarks of 3D-QA: ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). (Section 1)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **SQA3D** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the proposed cdViews on two widely used benchmarks of 3D-QA: ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). (Section 1)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)

### Associated with
- **3D understanding** (construct), 1 paper
  > In this work, we explore how to harness their potential to address 3D scene understanding tasks, using 3D question answering (3D-QA) as a representative example. (Abstract)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **Spatial reasoning** (construct), 1 paper
  > "all of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning"
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **3D perception** (construct), 1 paper
  > “For 3D perception, we include 2 tasks: embodied VQA (dialogue and planning), and 3D scene VQA (captioning and grounding).”
  - [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf)
