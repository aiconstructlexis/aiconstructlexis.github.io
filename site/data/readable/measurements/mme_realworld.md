# MME-RealWorld
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** MME-RW  

## State of the Field

**What it is.** Across the papers, MME-RealWorld is most commonly described as a multimodal benchmark for real-world scenarios and real-world multimodal tasks, used to assess vision-language performance. The prevailing descriptions present it as manually curated or manually annotated, with one line of description specifying five primary categories and 43 sub-class tasks, including monitoring, autonomous driving, OCR, property, and text/address tasks, and another noting an average resolution of 2000×1500. A smaller line of work also refers to an MME-RealWorld-Lite Reasoning subset and a remaining Reasoning subset.

**What it is claimed to measure.** Papers use MME-RealWorld to measure 2 constructs and 4 behavioral indicators. The construct links are to Reasoning and Generalization, while the behavioral indicators linked to it are Agent intention prediction, Diagram understanding, Multiple-choice question answering, and Object counting, so the recorded uses span both broad constructs and task-level behaviors. The supporting descriptions also frame the benchmark as covering 43 perception and reasoning subtasks, and the multiple-choice question answering setup is described as using four manually constructed options with the model's default multiple-choice prompt.

**Space of uses.** In the papers here, MME-RealWorld appears both as one benchmark within a larger evaluation suite and as a further evaluation on real-world applications. One paper reports evaluating a model on six challenging benchmarks including MME-RW, another says it further evaluates on MME-RealWorld, and the only linked instrument is VLMEvalKit, which is named as the evaluation framework employed for these benchmarks. Another reported use builds an Error-book on the MME-RealWorld-Lite Reasoning subset and applies it to the remaining MME-RealWorld Reasoning subset to test Generalization.

## Sources

**MME-RW** (1 paper: [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf))
> A benchmark for real-world multi-modal tasks used to assess vision-language performance.

**MME-RealWorld** (2 papers: [Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf), [ZoomEye: Enhancing Multimodal LLMs with Human-Like Zooming Capabilities through Tree-Based Image Exploration](https://aclanthology.org/2025.emnlp-main.335.pdf))
> A manually curated multimodal benchmark for real-world scenarios with multiple categories and sub-tasks, including monitoring, autonomous driving, OCR, property, and text/address tasks.

## Relationships

### → MME-RealWorld
- **Reasoning** (construct): *measured_by*, 1 paper
  > Our benchmark contains 5 real-world domains, covering 43 perception and reasoning subtasks. (Figure 1)
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For each question, we manually construct four options, with one being the correct answer... We try to use the model's default prompt for multiple-choice questions...
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Object counting** (behavioral indicator): *measured_by*, 1 paper
  > There are 3 perception tasks: object counting, color recognition, and spatial relationship understanding. (Section 2.2)
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Agent intention prediction** (behavioral indicator): *measured_by*, 1 paper
  > Intention Prediction: focus on predicting driving intention of a designated traffic agent in the short-term future. (Section 2.2)
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Diagram understanding** (behavioral indicator): *measured_by*, 1 paper
  > MME-RealWorld covers complex visual reasoning tasks derived from realistic applications across diverse domains (e.g., Autonomous Driving, Diagrams, OCR) (Section 4.1).
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > After creating an Error-book based on MME-RealWorld-Lite (Reasoning) subset, we applied it directly to the remaining MME-RealWorld Reasoning subset, excluding the Lite portion to rigorously test generalization (Section 4.1).
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)

### Associated with
- **VLMEvalKit** (measurement instrument), 1 paper
  > "The evaluation framework employed for these benchmarks was VLMEvalKit (Duan et al., 2024)."
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
