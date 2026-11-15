# NQ-Swap
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the surveyed papers, NQ-Swap is most commonly described as a counterfactual version of Natural Questions, where incorrect answers are swapped into the context to test whether a model relies on correct evidence. A closely related description treats it as a knowledge conflict dataset based on Natural Questions, consisting of synthetic conflicting data to test a model's ability to handle discrepancies. Papers also position it as a counterfactual QA benchmark that offers a more challenging and complementary evaluation of whether models can identify and rely on the correct evidence.

**What it is claimed to measure.** The reported measurement claims are concentrated rather than spread across many targets: papers link NQ-Swap to one construct, Context faithfulness, and one behavioral indicator, Question answering. The prevailing usage is to measure Context faithfulness, with papers describing it as evaluating a model's ability to identify and rely on the correct evidence, or to follow instructions and contexts on knowledge conflict datasets. A smaller line of use reports it as measuring Question answering, where it appears as one of the QA datasets used in task evaluation.

**Space of uses.** Papers use NQ-Swap within benchmark sets rather than in isolation. One recurring setup pairs it with ConfiQA as a counterfactual QA benchmark, while another uses it alongside MemoTrap as a knowledge conflict dataset for evaluating instruction and context following. It also appears in broader QA suites with Natural Question, TriviaQA, and PopQA, along with other QA datasets, when papers report performance across diverse QA tasks.

## Sources

**NQ-Swap** (2 papers: [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf))
> A counterfactual version of Natural Questions where incorrect answers are swapped into the context to test a model's reliance on correct evidence.

## Relationships

### → NQ-Swap
- **Context faithfulness** (construct): *measured_by*, 2 papers
  > we also include two counter-factual QA benchmarks: NQ-Swap and ConfiQA, offering a more challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence. (Section 3.2)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > We demonstrate ADACAD’s effectiveness on a diverse range of tasks, covering question-answering (QA) and summarization, with six QA datasets (Natural Question (NQ; Kwiatkowski et al., 2019), NQ-SWAP (Longpre et al., 2021), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023), HotpotQA (Yang et al., 2018), TabMWP (Lu et al., 2023)) (Section 1).
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
