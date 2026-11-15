# Q-Bench
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** QBench-Testset, QBench  

## State of the Field

**What it is.** Across papers, Q-Bench is most commonly described as a benchmark for low-level vision tasks or for assessing the low-level visual capabilities of multimodal or general-purpose foundation models. One definition further specifies that it is divided into perception, description, and quality assessment sections. A smaller usage treats it as an existing benchmark for in-domain multi-image evaluation, and one paper refers to a QBench-Testset, abbreviated QBenchT, as a named test set.

**What it is claimed to measure.** Papers link Q-Bench to 1 construct and no behavioral indicators. The only recorded measurement claim is that it measures Multi-image reasoning, with a paper including QBench among the benchmarks incorporated for multi-image tasks. The reported measurement use therefore centers on a single construct rather than spanning multiple constructs or indicators.

**Space of uses.** In practice, papers often present Q-Bench as one benchmark within broader evaluation suites. It is adopted alongside NLVR2 in multi-image evaluation, appears with Mantis-Eval and BLINK for multi-image tasks, and is also reported together with SEED-Bench Image Part and MM-Vet in result summaries.

## Sources

**Q-Bench** (2 papers: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf))
> A benchmark used in the paper for in-domain multi-image evaluation.

**QBench-Testset** (1 paper: [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf))
> QBench-Testset (QBenchT) is a benchmark for evaluating general-purpose foundation models on low-level vision tasks.

**QBench** (1 paper: [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf))
> A benchmark used to evaluate general-purpose foundation models on low-level vision tasks.

## Relationships

### → Q-Bench
- **Multi-image reasoning** (construct): *measured_by*, 1 paper
  > For multi-image tasks, we incorporate Mantis-Eval (Jiang et al., 2024), QBench (Wu et al., 2024b), and BLINK (Fu et al., 2024b), in line with LLaVA-Interleave (Li et al., 2024a). (Section 2.1)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
