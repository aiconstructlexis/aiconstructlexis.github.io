# Video-ChatGPT benchmark
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** Video-ChatGPT test set, VideoChatGPT  

## State of the Field

**What it is.** Across the definitions, the prevailing usage is as an evaluation benchmark or test set for video understanding and video-based conversational models, though papers vary in emphasis. It is described as a benchmark for generative performance, a test set for detailed video understanding via large vision and language models, and a long-video question-answering benchmark. Reported evaluation dimensions include Correctness of Information, Contextual Understanding, Temporal Understanding, and Consistency, with one description naming Detail Orientation and another naming Orientation.

**What it is claimed to measure.** In the reported relationships, papers use it to measure one behavioral indicator and one construct. The most common link is to video question answering, where papers evaluate models on the Video-ChatGPT test set or treat it as an open-ended video question-answering benchmark; a smaller line of use links it to temporal understanding through the benchmark's Temporal Understanding metric. Overall, the measurement claims are concentrated on these few targets rather than spread across many constructs.

**Space of uses.** In the papers, it appears as part of benchmark suites for video question answering rather than only as a standalone instrument. One paper reports testing on it alongside MSVD-QA, MSRVTT-QA, and ActivityNet-QA, while another positions it within zero-shot evaluation on open-ended video question-answering benchmarks and highlights its generative performance metrics. Beyond those side-by-side uses, papers do not link it to other measurement instruments.

## Sources

**Video-ChatGPT benchmark** (1 paper: [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf))
> A benchmark for evaluating the generative performance of video-based conversational models on criteria such as correctness, detail, and contextual understanding.

**Video-ChatGPT test set** (1 paper: [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf))
> A test set designed for evaluating detailed video understanding via large vision and language models, used here to assess general video question answering performance.

**VideoChatGPT** (1 paper: [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf))
> A long-video question-answering benchmark used to evaluate detailed video understanding across correctness, orientation, contextual understanding, temporal understanding, and consistency dimensions.

## Relationships

### → Video-ChatGPT benchmark
- **Video question answering** (behavioral indicator): *measured_by*, 2 papers
  > We test the trained model on the Video-ChatGPT test set [37] and the other three benchmarks (i.e., MSVD-QA [8], MSRVTT-QA [53], and ActivityNet-QA [6, 58]) where their training sets was not used to train Artemis. (Section 4.2).
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **Temporal understanding** (construct): *measured_by*, 1 paper
  > ...and the newly proposed generative performance benchmark [51], include evaluation metrics such as Correctness of Information (CI), Detail Orientation (DO), Contextual Understanding (CU), Temporal Understanding (TU), and Consistency (CO). (Section 4.1)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
