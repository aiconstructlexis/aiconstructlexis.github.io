# VNBench
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** Needle in a Haystack (NIAH)  

## State of the Field

**What it is.** Across the papers, VNBench is most commonly described as a benchmark for long video understanding. Definitions and quoted passages tie it especially to Needle-In-the-Haystack-Search, and a smaller framing presents the associated NIAH protocol as testing whether a model can retrieve specific information from long video sequences. One paper further describes VNBench as containing retrieval, ordering, and counting tasks, with retrieval treated as a short-dependency task and ordering and counting as long-dependency tasks.

**What it is claimed to measure.** Papers use VNBench to measure 2 constructs, Temporal perception and Video understanding, and 2 behavioral indicators, Chronological ordering and Counting. The most detailed measurement claim says its retrieval, ordering, and counting tasks evaluate temporal perception, chronological ordering, and spatio-temporal coherence, while another paper lists it among benchmarks used for video understanding. Overall, the reported measurement claims are spread across several aspects rather than concentrated on a single target.

**Space of uses.** No measurement instrument is linked to it directly. In practice, papers position VNBench as part of broader benchmark suites, appearing alongside ActivityNet-QA, EgoSchema, EventBench, LongVideoBench, and PerceptionTest, with other video benchmarks also included. Another usage emphasizes NIAH experiments for assessing retrieval ability from long videos, and one source notes that VNBench showed the most pronounced improvements among the compared benchmarks in connection with extended temporal context.

## Sources

**VNBench** (1 paper: [Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf))
> A benchmark for evaluating long video understanding, particularly for tasks like Needle-In-the-Haystack-Search that benefit from extended temporal context.

**Needle in a Haystack (NIAH)** (1 paper: [Sharper and Faster mean Better: Towards More Efficient Vision-Language Model for Hour-scale Long Video Understanding](https://aclanthology.org/2025.acl-long.222.pdf))
> Evaluation protocol testing a model's ability to retrieve specific information from long video sequences, analogous to finding a needle in a haystack.

## Relationships

### → VNBench
- **Temporal perception** (construct): *measured_by*, 1 paper
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Chronological ordering** (behavioral indicator): *measured_by*, 1 paper
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Counting** (behavioral indicator): *measured_by*, 1 paper
  > "VNBench contains three distinct tasks to address various aspects of video understanding, including a short-dependency task (retrieval) and two long-dependency tasks (ordering and counting)"
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Video understanding** (construct): *measured_by*, 1 paper
  > Table 3: Performance comparisons on 9 video benchmarks, including ActivityNet-QA (Yu et al., 2019), EgoSchema (Mangalam et al., 2023), EventBench (Du et al., 2024), LongVideoBench (Wu et al., 2024), PerceptionTest (Patraucean et al., 2023), MVBench (Li et al., 2024b), NExT-QA (Xiao et al., 2021), VNBench (Zhao et al., 2024), and VideoMME (Fu et al., 2024a). (Table 3)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
