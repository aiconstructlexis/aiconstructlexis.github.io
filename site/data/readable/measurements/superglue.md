# SuperGLUE
**Type:** Measurement instrument  
**Supporting papers:** 46  

## State of the Field

**What it is.** Across papers, SuperGLUE is most commonly described as a benchmark suite or collection of diverse, challenging language understanding tasks, usually framed as more difficult than GLUE and aimed at reasoning, inference, and comprehension. Definitions differ on its size and composition, with some papers describing 6 tasks, others 7 or 8, and several naming subsets such as MultiRC, BoolQ, WiC, WSC, CB, COPA, RTE, and ReCoRD; some also characterize it through task families such as question answering, textual entailment, coreference resolution, logical reasoning, and classification-style tasks.

**What it is claimed to measure.** Papers use SuperGLUE to measure 2 constructs and 4 behavioral indicators. Most often, they use it to measure Natural language understanding, with a smaller line of work also using it to measure Multi-task ability; one paper says it allows evaluation of "different aspects of natural language understanding" (BERTs are Generative In-Context Learners). At the behavioral level, it is reported as measuring Classification, Coreference resolution, Language understanding task performance, and Word sense disambiguation, so the construct-level claims converge most clearly on language understanding while the behavioral links are spread across several task-level indicators.

**Space of uses.** Across uses, papers typically employ SuperGLUE for evaluation: they fine-tune on it, report few-shot or in-context results on it, use dev sets from its datasets, or draw subsets from it for studies of energy use, continual learning, and text quality. It is frequently paired with GLUE, sometimes with Super Natural-Instructions, and papers also relate it to 7 task-level instruments, most often BoolQ, CB, COPA, MultiRC, and RTE; one study calls it "a widely acceptable benchmark for evaluating general-purpose language understanding" (Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning).

## Sources

**SuperGLUE** (19 papers: [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a692a24dbc744fca340b9ba33bc6522-Paper-Conference.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf), [Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/06960915ba8674c7a898ec0b472b80ff-Paper-Conference.pdf), [On the Crucial Role of Initialization for Matrix Factorization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d67ec04032cccf4a21d04c0ae4ab268-Paper-Conference.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [Efficient and Effective Prompt Tuning via Prompt Decomposition and Compressed Outer Product](https://aclanthology.org/2025.naacl-long.225.pdf), [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf), [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf))
> A more challenging benchmark suite than GLUE, consisting of complex language understanding tasks that test reasoning and comprehension abilities.

## Relationships

### → SuperGLUE
- **Natural language understanding** (construct): *measured_by*, 3 papers
  > We assess the effectiveness of MPDistil using two natural language understanding benchmarks, SuperGLUE (Wang et al., 2019) and GLUE (Wang et al., 2018), encompassing 15 NLU tasks. (Section 1)
  - [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > The first benchmark, SuperGLUE, is a collection of eight challenging language understanding and reasoning tasks.
  - [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf)
- **Multi-task ability** (construct): *measured_by*, 1 paper
  > “we conducted experiments on two publicly available multitasking benchmarks: SuperGLUE (Wang et al., 2019) and Super Natural-Instructions (Super NI) (Wang et al., 2022).”
  - [Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a692a24dbc744fca340b9ba33bc6522-Paper-Conference.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > examine BAdam's capability in classification tasks by training RoBERTa-large on SuperGLUE benchmarks.
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)
- **Word sense disambiguation** (behavioral indicator): *measured_by*, 1 paper
  > The SuperGLUE benchmark comprises advanced language understanding tasks... word sense disambiguation (WiC; (Pilehvar and Camacho-Collados, 2019))... (Section 4.1)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Coreference resolution** (behavioral indicator): *measured_by*, 1 paper
  > The SuperGLUE benchmark comprises advanced language understanding tasks... coreference resolution (WSC; ())... (Section 4.1)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)

### Associated with
- **BoolQ** (measurement instrument), 3 papers
  > For question answering tasks, we utilize BoolQ (from SuperGLUE) (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **CB** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... CB”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **COPA** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... COPA”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **MultiRC** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... MRC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **RTE** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... RTE”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **WiC** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... WiC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
- **WSC** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... WSC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
