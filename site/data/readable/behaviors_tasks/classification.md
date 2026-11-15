# Classification
**Type:** Behavioral indicator  
**Supporting papers:** 41  
**Also known as:** Label inference, Event categorization, Multi-class categorization, Supervised classification  

## State of the Field

**Space of definitions.** Most commonly, papers use classification for tasks where a model assigns a label or category from a predefined set to an input, often treating the task as text-to-text by encoding classes as strings and selecting the highest-scoring choice. Across definitions, the prevailing success criterion is choosing the most likely correct answer from a small or fixed output space, though some papers broaden the behavior to multi-label label inference, predicting a single high-level root label from lower-level inputs, or having a judge decide whether a response meets a stated requirement. Some work also frames it explicitly as supervised classification, where each prompt has a ground-truth label drawn from a valid option set.

**Variants.** Papers study several variants, including answerability and cause-effect classification, movie-tag labeling, structural-prompt validity judgments, and in-context or many-shot classification settings. A smaller line of work extends the same label-selection pattern to image classification with a single word or phrase, hierarchical weather and climate event categorization, and multiclass categorization of multiple waste items within one cluttered scene. Another variant is label inference from natural-language descriptions, where papers ask for labels one at a time, simultaneously, or only for positive labels.

**Space of elicitation and scores.** Papers report that classification is measured by 11 instruments. Among the linked instruments are ARC-Challenge, ARC-Easy, HellaSwag, MMLU-Pro, and MathQA, and the other links are to additional classification benchmarks, datasets, and one evaluation framework. In scoring, papers most often mention accuracy or test accuracy for classification tasks, while one formulation scores each candidate label and returns the highest-scoring choice.

**What it is taken as evidence of.** No construct is linked to classification, so these papers do not explicitly use it as evidence of a named construct.

## Sources

**Classification** (18 papers: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf), [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf), [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf), [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf), [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf), [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf), [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [Learning curves theory for hierarchically compositional data with power-law distributed features](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cagnetta25a/cagnetta25a.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.110.pdf), [More is not always better? Enhancing Many-Shot In-Context Learning with Differentiated and Reweighting Objectives](https://aclanthology.org/2025.acl-long.1475.pdf), [On Many-Shot In-Context Learning for Long-Context Evaluation](https://aclanthology.org/2025.acl-long.1245.pdf))
> Assigning a label from a predefined set based on input context, treated as a text-to-text mapping in this work.

**Label inference** (1 paper: [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf))
> Inferring one or more labels for an unseen sample from its natural-language description.

**Event categorization** (1 paper: [CLLMate: A Multimodal Benchmark for Weather and Climate Events Forecasting](https://aclanthology.org/2025.emnlp-main.886.pdf))
> The observable task of selecting the most probable event category from a predefined hierarchical classification system based on given meteorological data.

**Multi-class categorization** (1 paper: [Waste-Bench: A Comprehensive Benchmark for Evaluating VLLMs in Cluttered Environments](https://aclanthology.org/2025.emnlp-main.1578.pdf))
> The task of classifying multiple waste items within a single complex scene into more than one category.

**Supervised classification** (1 paper: [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf))
> The task of predicting a discrete label from a set of valid options for a given input prompt, based on labeled training examples.

## Relationships

### Classification →
- **SuperGLUE** (measurement instrument): *measured_by*, 1 paper
  > examine BAdam's capability in classification tasks by training RoBERTa-large on SuperGLUE benchmarks.
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **MathQA** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets (OpenbookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), Arc_e (Clark et al., 2018), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019))...
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > ...six classification datasets... with the LM-Evaluation-Harness framework (Gao et al., 2023).
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **MixEval** (measurement instrument): *measured_by*, 1 paper
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
