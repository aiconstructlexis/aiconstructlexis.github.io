# MathQA
**Type:** Measurement instrument  
**Supporting papers:** 50  
**Also known as:** MQA  

## State of the Field

**What it is.** Across definitions, the prevailing usage is as a math question answering or mathematical reasoning benchmark built from math word problems. Most descriptions present it as multiple-choice and centered on multi-step quantitative reasoning, and one source notes that it offers five answer options per problem and includes geometry, physics, probability, and algebra. A smaller line of work describes the problems as using operation-based formalisms for interpretability, and one paper using the name MQA frames it instead as GRE and GMAT exam questions requiring more diverse and complex reasoning skills.

**What it is claimed to measure.** Claims concentrate on Mathematical reasoning: papers use MathQA to measure that construct more often than any other, and describe it as assessing mathematical tasks, varying levels of mathematical reasoning ability, and diverse arithmetic and algebraic reasoning challenges. Overall it is linked to four constructs, Mathematical reasoning, Reasoning, Commonsense reasoning, and Problem-solving ability, and to two behavioral indicators, Mathematical problem solving and Classification. The prevailing measurement claim is therefore Mathematical reasoning, while smaller lines of work treat it as measuring mathematical problem solving or broader reasoning, and isolated papers place it under commonsense reasoning, classification, or problem-solving ability.

**Space of uses.** No measurement instrument is linked to it. In practice, papers commonly use MathQA alongside GSM8K, SVAMP, MATH, AQuA, and MMLU-STEM in broader evaluation suites, and some also place it in mixed collections of reasoning, question answering, or lm-evaluation-harness tasks. It is usually one benchmark within a larger battery, though one definition also describes it as used in instruction tuning and retriever fine-tuning, and another paper says it is paired with a custom mathematical knowledge corpus.

**Concerns raised.** Concern evidence is sparse. One paper includes MathQA among popular mathematical reasoning benchmarks used to detect data contamination.

## Sources

**MathQA** (15 papers: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fa1edbc195336e29893cdae0939e495f-Paper-Conference.pdf), [Number Cookbook: Number Understanding of Language Models and How to Improve It](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8ccc9229328bdcedf54b989e7cc330-Paper-Conference.pdf), [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf), [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf), [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf), [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf), [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf), [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf))
> A math question answering dataset used in instruction tuning and retriever fine-tuning.

**MQA** (1 paper: [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf))
> Mathematical reasoning benchmark containing GRE and GMAT exam questions that test complex quantitative reasoning abilities.

## Relationships

### → MathQA
- **Mathematical reasoning** (construct): *measured_by*, 12 papers
  > For evaluation, we employ a range of benchmarks - GSM8K, MATH, MMLU-MATH, AGIEval-SAT-MATH, MathQA, AQuA - to assess varying levels of mathematical reasoning abilities, comparing all models using the same few-shot prompting with greedy decoding. (Section 4.2)
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf)
  - [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf)
  - [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 3 papers
  > For mathematic QA tasks (MathQA and GSM8K)... (Section 3.1)
  - [DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts](https://aclanthology.org/2025.acl-long.951.pdf)
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
  - [RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1630.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > Seven reasoning datasets used in the experiments include OpenbookQA (Banerjee et al., 2020), WinoGrande (Sakaguchi et al., 2021) HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019), ARC-e, ARC-c (Clark et al., 2018). (Section 4.1)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > along with 7 common sense reasoning datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019), ARC-e, and ARC-c (Clark et al., 2018)) (Section 4.1).
  - [MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singular Value Decomposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25az/li25az.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **Problem-solving ability** (construct): *measured_by*, 1 paper
  > It consists of questions that test numerical reasoning and problem-solving skills, requiring models to both understand the text of a word problem and perform mathematical operations to arrive at the correct solution. (Section 3.2.1)
  - [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf)
