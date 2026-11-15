# Embodied question answering
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Embodied VQA  

## State of the Field

**Space of definitions.** Across the definitions, it is treated as answering questions about embodied 3D environments. One paper describes this as perceiving, navigating, interacting, and reasoning through sequences of multimodal observations and actions to answer questions, while another uses the name "Embodied VQA" and explicitly includes dialogue and planning.

**Variants.** Papers use both "Embodied question answering" and "Embodied VQA" for this behavior. The named variant is embodied VQA with dialogue and planning, and one paper places it alongside 3D scene VQA within a 3D perception setup; another description emphasizes multimodal observations such as video frames and reasoning traces, and one related account says agents must actively explore the environment to answer natural-language questions.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers, the behavior is elicited through questions about 3D environments and described in terms of multimodal observations, actions, and sometimes dialogue or planning, but no instrument is named as measuring or scoring it.

**What it is taken as evidence of.** Papers connect it to three constructs: 3D perception, spatial understanding, and temporal understanding. The usage is not uniform as an evidence claim, because one paper places embodied VQA within 3D perception while another relates embodied question answering to agents' spatial and temporal understanding, and all of these connections are framed as related links.

## Sources

**Embodied question answering** (1 paper: [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> Answering questions about a 3D environment by perceiving, navigating, and interacting with multimodal observations such as video frames and reasoning traces.

**Embodied VQA** (1 paper: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf))
> Answering questions about embodied 3D environments, including dialogue and planning.

## Relationships

### Associated with
- **Spatial understanding** (construct), 1 paper
  > complex embodied tasks like Embodied Question Answering (EQA) where nuanced evaluation of agents’ spatial, temporal, and logical understanding is critical yet not considered by generic approaches. (Abstract)
  - [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf)
- **Temporal understanding** (construct), 1 paper
  > complex embodied tasks like Embodied Question Answering (EQA) where nuanced evaluation of agents’ spatial, temporal, and logical understanding is critical yet not considered by generic approaches. (Abstract)
  - [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf)
- **Environment exploration** (behavioral indicator), 1 paper
  > Embodied Question Answering (EQA) ... must actively explore its environment to answer questions posed in natural language. (Section 1)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
- **3D perception** (construct), 1 paper
  > “For 3D perception, we include 2 tasks: embodied VQA (dialogue and planning), and 3D scene VQA (captioning and grounding).”
  - [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf)
