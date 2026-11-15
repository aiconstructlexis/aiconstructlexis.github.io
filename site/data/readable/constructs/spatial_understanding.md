# Spatial understanding
**Type:** Construct  
**Supporting papers:** 30  
**Also known as:** Spatial awareness, Spatial comprehension, Spatial structure understanding, Spatial relationship understanding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats spatial understanding, often also called spatial awareness, as the model's ability to perceive, interpret, and reason about the arrangement, positions, and relationships of objects in images or visual scenes. Many definitions stay close to this image-based framing, sometimes emphasizing fine-grained spatial details, grounding, or transformations, and some spell it out with relations such as left of and on top of. A smaller line of work extends the construct to positional relationships and sequences in structured lists, the layout of 3D environments, spatially distributed findings in medical images, the connectivity and continuity of road networks, embodied scenes across trajectories, and directional context from audio.

**Space of facets.** Papers most often alternate between spatial understanding and spatial awareness for object positions and relations in scenes, while specialized variants appear for medical-image structure, road-network topology, and explicit object configurations. Some authors distinguish it from numeric and attribute comprehension, and others discuss it together with temporal understanding.

**Space of measurement.** Papers link the construct to three measurement instruments, with MM-Vet appearing most often, followed by MMBench-Video and RealWorldQA, and to two behavioral indicators that place it in question-answering settings, embodied question answering and video question answering. The operationalizations are dataset or benchmark style evaluations: MM-Vet reports a spatial awareness category, RealWorldQA is described as a dataset for basic real-world spatial understanding scored by multiple-choice accuracy, and MMBench-Video assesses spatial and temporal understanding in video. These measures concentrate on real-world, multimodal, or video settings, whereas some definitions also extend the construct to structured lists, road networks, medical images, 3D environments, embodied trajectories, and audio context.

**Links.** Papers relate spatial understanding to grounding, video question answering, and embodied question answering. In these formulations, grounding is presented as a desired capability that stems from the problem of enabling spatial understanding, video question answering includes questions about the positions of items and their relations to other items, and embodied question answering is described as a setting where nuanced evaluation of agents' spatial understanding is needed.

## Sources

**Spatial awareness** (4 papers: [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf), [LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios](https://aclanthology.org/2025.acl-long.803.pdf), [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf), [SING: Spatial Context in Large Language Model for Next-Gen Wearables](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mishra25a/mishra25a.pdf))
> The ability to perceive and reason about the spatial arrangement and relationships of objects in a visual scene.

**Spatial understanding** (5 papers: [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf), [Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users](https://aclanthology.org/2025.acl-long.1260.pdf), [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf), [ScImage: How good are multimodal large language models at scientific text-to-image generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/146b5b0feb14fe8e630669ad1faba25e-Paper-Conference.pdf), [Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25a/hao25a.pdf))
> The ability to perceive and reason about the spatial arrangement, positions, and relationships of objects within an image.

**Spatial comprehension** (1 paper: [SMART: Scalable Multi-agent Real-time Motion Generation via Next-token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cef5c8dec67597b854f0162ad76d92d2-Paper-Conference.pdf))
> The latent ability to understand and model the structural and topological properties of a road network, such as the connectivity and continuity between road segments.

**Spatial structure understanding** (1 paper: [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939.pdf))
> The ability to reason about spatially distributed findings and structural relationships within medical images.

**Spatial relationship understanding** (1 paper: [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf))
> Determining the positional or relational configuration between objects in an image.

## Relationships

### Spatial understanding →
- **MM-Vet** (measurement instrument): *measured_by*, 2 papers
  > Table 5: Multimodal reasoning ability on MM-Vet [92]. Rec denotes Recognition; Know denotes knowledge; Gen denotes Language generation; and Spat denotes Spatial awareness.
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > RealworldQA [57] is the most recent dataset tailored to assess the capability of LMMs in basic real-world spatial understanding, using the accuracy metric within multiple-choice questions. (Section 4)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > "The comprehensive assessment underscores the significant performance disparities between Video-LLMs and leading LVLMs in both spatial and temporal understanding"
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Grounding** (construct), 1 paper
  > In vision-language learning, how to enable spatial understanding in models is a fundamental research problem. Two desired capabilities stem from this problem: referring and grounding.
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator), 1 paper
  > We annotate 98 videos and provide 882 question-answer pairs that target three types of questions: ... 2) spatial Understanding about the position of items and their relation to other items...
  - [Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users](https://aclanthology.org/2025.acl-long.1260.pdf)
- **Embodied question answering** (behavioral indicator), 1 paper
  > complex embodied tasks like Embodied Question Answering (EQA) where nuanced evaluation of agents’ spatial, temporal, and logical understanding is critical yet not considered by generic approaches. (Abstract)
  - [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf)
