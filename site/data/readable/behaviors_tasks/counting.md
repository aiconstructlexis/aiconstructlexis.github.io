# Counting
**Type:** Behavioral indicator  
**Supporting papers:** 35  
**Also known as:** Action count, Vertex count, Hyperedge count, Action counting, Repetition counting, Audio content counting, Atom counting, Ring counting, Entity counting  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats counting as producing the correct number for a specified target, most often the number of objects or shapes visible in an image. In this visual framing, models are asked to "state the number of objects present," and some authors explicitly include zero-answer "trick" questions when the queried object is absent. Smaller strands define counting more broadly as mapping a number word to a set's cardinality, outputting the running count of items seen so far in a sequence, determining how often an item appears in a list, or generating the consecutive integers from a start value to an end value and then terminating.

**Variants.** Variants span several modalities and representations. Common ones include image counting of specified objects or shapes, action count, action counting, and repetition counting in video, and audio counting of how many times a specified sound or event occurs in an audio clip or video. Other papers study entity counting in diagrams, vertex count and hyperedge count in hypergraphs, and atom counting or ring counting from molecular strings.

**Space of elicitation and scores.** Papers measure counting with 7 linked instruments. The linked instruments include BABILong, LLM-as-a-judge, MLVU, MuirBench, and TACT, which use counting within broader task sets or evaluation setups, while LLM-as-a-judge specifically compares a model's image-count response with a human-annotated answer. Additional linked instruments cover temporal action-count and long-dependency video-count settings.

**What it is taken as evidence of.** The links do not frame counting as evidence of several constructs. Among constructs, only Length generalization is linked, and papers describe that connection as related: a paper reports that a model trained on count sequences can length-generalize to longer ones. Outside construct links, a separate paper also relates counting to Hallucination as one of several tasks in a multimodal benchmark, so the recorded links are associative rather than measurement or causal claims.

## Sources

**Counting** (6 papers: [Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf), [Language Models Need Inductive Biases to Count Inductively](https://proceedings.iclr.cc/paper_files/paper/2025/file/378226e5df7eded3e401de5c9493143c-Paper-Conference.pdf), [SPHERE: Unveiling Spatial Blind Spots in Vision-Language Models Through Hierarchical Evaluation](https://aclanthology.org/2025.acl-long.568.pdf), [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf), [Diagnosing Memorization in Chain-of-Thought Reasoning, One Token at a Time](https://aclanthology.org/2025.emnlp-main.157.pdf), [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf))
> Reporting the number of objects or shapes visible in an image.

**Action count** (1 paper: [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf))
> Counting how many times an action occurs in a video.

**Vertex count** (1 paper: [Beyond Graphs: Can Large Language Models Comprehend Hypergraphs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/690fc970014e4ecebc8068bbc03b35e6-Paper-Conference.pdf))
> The task of counting the total number of vertices in a given hypergraph.

**Hyperedge count** (1 paper: [Beyond Graphs: Can Large Language Models Comprehend Hypergraphs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/690fc970014e4ecebc8068bbc03b35e6-Paper-Conference.pdf))
> The task of counting the total number of hyperedges in a given hypergraph.

**Action counting** (1 paper: [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf))
> Detecting and enumerating the number of times a specific action or scene occurs within a video sequence.

**Repetition counting** (1 paper: [D-CoDe: Scaling Image-Pretrained VLMs to Video via Dynamic Compression and Question Decomposition](https://aclanthology.org/2025.emnlp-main.597.pdf))
> The observable task of counting the number of times a specific action or event occurs within a video.

**Audio content counting** (1 paper: [Audio-centric Video Understanding Benchmark without Text Shortcut](https://aclanthology.org/2025.emnlp-main.333.pdf))
> Counting how many times a specified audio event occurs in a video.

**Atom counting** (1 paper: [Molecular String Representation Preferences in Pretrained LLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.56.pdf))
> Extracting and reporting the number of each type of atom (e.g., carbon, chlorine) present in a given molecular string representation.

**Ring counting** (1 paper: [Improving Chemical Understanding of LLMs via SMILES Parsing](https://aclanthology.org/2025.emnlp-main.791.pdf))
> Identifying and counting the number of rings of a specific size (e.g., five- or six-membered) in a molecule from its SMILES string.

**Entity counting** (1 paper: [Do Vision-Language Models Really Understand Visual Language?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25c/hou25c.pdf))
> The observable task of counting the number of entities of a certain type within a diagram.

## Relationships

### Counting →
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > TACT offers a diverse range of tasks, primarily focusing on two types of instructions–“Calculate” and “Count”: (Section 2.3)
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To assess this dimension, we query GPT-4V about the number of target objects in the image and compare its response with the human-annotated answer. (Sec. 3.1.1)
  - [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > [COUNTING] aims to evaluate the ability of models to count the number of specific objects across multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **TOMATO** (measurement instrument): *measured_by*, 1 paper
  > TOMATO comprises 1,484 carefully curated, human-annotated multiple-choice questions spanning six distinct temporal reasoning tasks (action count, direction, rotation, shape & trend, velocity & frequency, and visual cues)... (Section 1)
  - [TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf)
- **VNBench** (measurement instrument): *measured_by*, 1 paper
  > "VNBench contains three distinct tasks to address various aspects of video understanding, including a short-dependency task (retrieval) and two long-dependency tasks (ordering and counting)"
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **MLVU** (measurement instrument): *measured_by*, 1 paper
  > "the results of each subtask in MLVU (Zhou et al., 2024) show significant performance improvements when using cross-modal queries, particularly for frame-retrieval tasks such as counting and needle detection."
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Length generalization** (construct), 1 paper
  > We train a Transformer with learned positional embeddings on count sequences of lengths up to 50, with random a and b points in [0, 155]. This trained model then length-generalizes near perfectly when prompted to count sequences of length 100 (see Figure 1b).
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
