# Chronological ordering
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Ordering, Plot unscrambling, Image ordering, Visual ordering  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage is a sequencing task in which a model must arrange shuffled or retrieved items into the correct temporal or logical order. Most formulations treat success as giving the full correct sequence, described variously as restoring the original logical sequence of plot-synopsis sentences, identifying the chronological order of inserted video needles, arranging images by temporal or visual progression, or ordering events and states from earliest to latest.

**Variants.** Papers study this behavior across text, video, and multi-image settings, and use several names for it, including plot unscrambling, ordering, image ordering, visual ordering, and chronological ordering. The variants differ in what is being sequenced: shuffled movie-synopsis sentences, multiple inserted needles in a video, numbered image patches whose order must be stated, or retrieved dates, events, and states; some descriptions place image ordering under temporal reasoning, while movie synopsis unscrambling appears under language comprehension.

**Space of elicitation and scores.** It is measured by one instrument, VNBench. Papers describe VNBench as a video benchmark that includes retrieval, ordering, and counting tasks, with ordering used to evaluate chronological ordering; papers also report accuracy for temporal and visual ordering tasks, but no other named instrument is linked to this behavior.

**What it is taken as evidence of.** As a broader construct link, papers only relate it to Natural language understanding. That link comes from work that groups movie synopsis unscrambling with language comprehension, and papers do not report other construct links for this behavior.

## Sources

**Plot unscrambling** (1 paper: [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf))
> Reordering shuffled sentences of a plot synopsis into the original logical sequence.

**Ordering** (1 paper: [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf))
> Identifying the correct chronological order of multiple inserted needles in a video.

**Image ordering** (1 paper: [MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf))
> The task of arranging a set of images into a correct temporal or logical sequence.

**Visual ordering** (1 paper: [MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf))
> Ordering images according to visual progression or sequence cues.

**Chronological ordering** (1 paper: [Episodic Memories Generation and Evaluation Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ff013b7e372ba5b790352ccd6908f03-Paper-Conference.pdf))
> The task of arranging a set of retrieved events or states in the correct temporal sequence, from earliest to latest.

## Relationships

### Chronological ordering →
- **VNBench** (measurement instrument): *measured_by*, 1 paper
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)

### Associated with
- **Natural language understanding** (construct), 1 paper
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
