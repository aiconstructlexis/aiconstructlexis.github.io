# HaluEval
**Type:** Measurement instrument  
**Supporting papers:** 16  

## State of the Field

**What it is.** Across the papers, HaluEval is most commonly described as a large-scale benchmark for evaluating hallucination, especially factual hallucination in model-generated responses. Most descriptions place it in large language model evaluation, often in question answering, while some instead emphasize language-only dialogue, and one paper reuses dialogue and summarization subsets called HaluDial and HaluSum. Papers describe its instances in several ways: one calls it synthetically generated hallucination data, another says each example pairs a user query with factual and hallucinated LLM responses annotated by human evaluators, and another describes a QA track of 10000 questions with reference knowledge, a right answer, and a hallucinated answer. Some uses also frame it as a discriminative yes or no judgment task for deciding whether an answer contains a hallucination.

**What it is claimed to measure.** Papers use HaluEval to measure 3 behavioral indicators and 2 constructs. The prevailing use is for Hallucination and Hallucination detection: papers describe it as evaluating hallucination tendencies, detecting and flagging hallucinations, or judging whether an answer contains a hallucination, and one paper also uses its summarization data to measure Text summarization. Beyond these behavioral uses, several papers use HaluEval to measure Generalization, for example by applying methods learned on TruthfulQA to HaluEval to validate generalizability, while a smaller line of work uses it for Factual reasoning. Overall, the claims cluster around hallucination-focused evaluation, with Generalization and Factual reasoning as secondary uses.

**Space of uses.** No measurement instrument is linked to HaluEval. Even so, papers often use it alongside TruthfulQA, for example by contrasting a generative benchmark with the discriminative HaluEval, transferring settings learned on TruthfulQA to HaluEval, training on TruthfulQA and then testing on HaluEval for generalization, or using HaluEval instances to calculate editing projections before evaluating on TruthfulQA. Smaller comparisons place it beside HalluQA, TrivialQA, BamBoo, and SelfCheckGPT-WikiBio, and some papers also treat it as a third-party English evaluation set.

## Sources

**HaluEval** (11 papers: [FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data](https://aclanthology.org/2025.naacl-long.258.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf), [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.276.pdf), [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf), [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf), [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf), [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf), [WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia](https://proceedings.neurips.cc/paper_files/paper/2024/file/c63819755591ea972f8570beffca6b1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Large-scale benchmark for evaluating factual hallucination in model-generated responses.

## Relationships

### → HaluEval
- **Hallucination** (behavioral indicator): *measured_by*, 4 papers
  > We further verify this hypothesis by measuring the capabilities coefficient on a generative benchmark (TruthfulQA Generation [45]) and a discriminative benchmark (HaluEval [43]). (Appendix A.5)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.276.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Generalization** (construct): *measured_by*, 3 papers
  > The results in Tab. 6 reveal that our annotation model achieves notable accuracies on both HaluEval and HalluQA... underscoring the generalization capability of ANAH-v2. (Section 4.4)
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Hallucination detection** (behavioral indicator): *measured_by*, 3 papers
  > Detecting and flagging hallucinations (HaluEval dataset (Li et al., 2023)). (Section 1)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
  - [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf)
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 1 paper
  > Similar to DRS, we adopt the summarization data from the HaluEval [40] benchmark as the evaluation dataset (denoted as HaluSum).
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factual reasoning** (construct): *measured_by*, 1 paper
  > "TruthfulQA (Lin et al., 2022) and HaluEval (Li et al., 2023) for factual reasoning"
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf)
