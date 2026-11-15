# RACE
**Type:** Measurement instrument  
**Supporting papers:** 48  

## State of the Field

**What it is.** Across papers, RACE is most commonly described as a large-scale reading comprehension dataset or benchmark drawn from English examinations for middle and high school students, built around passage-based multiple-choice questions. Several papers explicitly separate RACE-High and RACE-Middle, and one paper refers to the high test portion. A smaller line of descriptions frames it more specifically as coming from English exams for Chinese students, or more broadly as factual QA or exam-style passages and questions.

**What it is claimed to measure.** Papers link RACE to 6 constructs and 3 behavioral indicators. The prevailing measurement claims are reading comprehension and machine reading comprehension, and one paper describes it as a multiple-choice task used to evaluate reading comprehension abilities and requiring reasoning over provided passages. More occasional uses treat it as measuring general ability, long-context understanding, and natural language understanding, with several other linked targets appearing more sparsely.

**Space of uses.** Papers do not link RACE to another measurement instrument directly, but they frequently place it inside broader benchmark suites. It is commonly used alongside PIQA, AI2-ARC, BoolQ, and LAMBADA, with HellaSwag appearing in some suites, and papers position it as one component of downstream, general-capability, or zero-shot evaluation.

## Sources

**RACE** (18 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion](https://aclanthology.org/2025.acl-long.100.pdf), [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf), [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf), [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf), [ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf), [Learning to Understand: Identifying Interactions via the Möbius Transform](https://proceedings.neurips.cc/paper_files/paper/2024/file/520b379123d16e41f85472e766846486-Paper-Conference.pdf), [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf), [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf), [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf), [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf))
> Reading Comprehension dataset collected from English exams for middle and high school students, assessing reasoning and understanding ability through passage-based multiple-choice questions.

## Relationships

### → RACE
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 7 papers
  > RACE is a reading comprehension benchmark introduced in Lai et al. (2017) collected from English examinations of middle and high school students. (Section 3)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Flexora: Flexible Low-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.acl-long.713.pdf)
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **Reading comprehension** (construct): *measured_by*, 2 papers
  > “we also included the multiple-choice reading comprehension task RACE”
  - [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > “The multiple-choice tasks include: ... reading comprehension (RACE; Lai et al. 2017)”
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > "The RACE dataset represents a \"needle-in-a-haystack\" task demanding identification of critical information within lengthy contexts."
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We also select several reasoning benchmarks, i.e., PIQA (Bisk et al., 2020), ARC (Clark et al., 2018), HellaSwag (Zellers et al., 2019), Winogrande (Sakaguchi et al., 2021), Race (Lai et al., 2017) and LAMBADA (Paperno et al., 2016), using the open-sourced toolkit lm-evaluation-harness (Gao et al., 2023). (Section 4.1)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > “Table 1. Comparison of zero-evaluation performance... RACE ↑”
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > Different datasets including... language understanding and knowledge such as... Race-Middle, Race-High [60]... are comprehensively evaluated. (Section 4)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
