# Temporal perception
**Type:** Construct  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the cited papers, the prevailing usage treats temporal perception as a model ability for recognizing and processing information across a video's time dimension. One definition states this directly, while another frames it as the latent ability to perceive and understand dynamic visual changes over time, especially rapid or subtle motion patterns. A narrower strand of wording also stresses that accurately distinguishing movements requires capturing the full motion sequence rather than sparse frames.

**Space of facets.** Papers most clearly position temporal perception as one aspect of video understanding alongside chronological ordering and spatio-temporal coherence, rather than using these names interchangeably. The linked benchmark material pairs retrieval with temporal perception, ordering with chronological order, and counting with spatio-temporal coherence, and it says the retrieval task "specifically assesses" temporal perception across the time dimension. Beyond this contrast, the papers do not describe further subtypes or construct hierarchies.

**Space of measurement.** Temporal perception is linked to one measurement instrument, the benchmark VNBench, and one behavioral indicator, Synthetic recall. VNBench is described as a video benchmark with retrieval, ordering, and counting tasks for evaluating temporal perception, chronological ordering, and spatio-temporal coherence, and the linked evidence says the retrieval task assesses temporal perception and understanding across the time dimension. This operationalization closely follows the dominant definition centered on time-distributed video information.

**Links.** The papers do not report causal or correlational links for temporal perception. One paper reports that Synthetic recall is related to temporal perception, using the retrieval task as the connection and stating that this task assesses the model's capability for temporal perception across time.

## Sources

**Temporal perception** (2 papers: [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf), [Improving LLM Video Understanding with 16 Frames Per Second](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cg/li25cg.pdf))
> The ability to recognize and process information distributed across the time dimension of a video.

## Relationships

### Temporal perception →
- **VNBench** (measurement instrument): *measured_by*, 1 paper
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)

### Associated with
- **Synthetic recall** (behavioral indicator), 1 paper
  > This task [Retrieval] specifically assesses the model’s capability for temporal perception and understanding across the time dimension. (Section 3.2)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
