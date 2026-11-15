# SciQA
**Type:** Measurement instrument  
**Supporting papers:** 11  

## State of the Field

**What it is.** Across papers, SciQA is most commonly presented as a science question-answering resource. Definitions describe it as a dataset of science exam questions with "rich domain-specific language and complex reasoning," while some authors instead present it as a science question answering benchmark for visual question answering, including scientific diagrams that require scientific reasoning; another usage places it among reading comprehension tasks.

**What it is claimed to measure.** Papers use SciQA to measure one construct and two behavioral indicators. It is reported as measuring Visual understanding, and it also measures Knowledge-based question answering and Machine reading comprehension, so the recorded uses are spread across several targets rather than centered on a single reported construct.

**Space of uses.** Papers often list SciQA as one item in broader evaluation suites. It appears with ARC-Challenge, ARC-Easy, LogiQA, PIQA, and LAMBADA in downstream-task testing, and other papers include it in collections of vision-understanding or visual question answering benchmarks.

## Sources

**SciQA** (4 papers: [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf), [SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bf/chen25bf.pdf), [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf), [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf))
> A question-answering dataset consisting of science exam questions with rich domain-specific language and complex reasoning.

## Relationships

### → SciQA
- **Visual understanding** (construct): *measured_by*, 1 paper
  > For vision understanding evaluations, we use the commonly used vision understanding benchmarks to evaluate the performance similar as LLaVA-1.5, such as VQAv2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), VizWiz (Gurari et al., 2018), SciQA (Lu et al., 2022), TextVQA (Singh et al., 2019), POPE (Li et al., 2023b), MMBench (en) (Liu et al., 2023b), SEED (image) (Li et al., 2023a) and MM-Vet (Yu et al., 2023). (Section 4.1)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **Knowledge-based question answering** (behavioral indicator): *measured_by*, 1 paper
  > For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ... and SciQA (Auer et al., 2023) challenges models using the Open Research Knowledge Graph.
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > Additionally, the DWM not only enhances the model’s performance on reading comprehension tasks, such as SciQA and BoolQ, but also improves its performance on commonsense reasoning tasks, such as the WinoGrande.
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
