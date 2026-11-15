# TREC
**Type:** Measurement instrument  
**Supporting papers:** 35  
**Also known as:** Trec  

## State of the Field

**What it is.** Across the papers, TREC is most commonly described as the Text REtrieval Conference question classification benchmark, usually framed as a 6-way task with coarse question types such as abbreviation, entity, description, human, location, and numeric. Some descriptions add that it has 50 subclasses or that it is used to classify questions into fine-grained answer types, while a few papers describe it more broadly as a general NLU dataset or as used for information retrieval tasks. A smaller usage treats "Trec" as a dataset from LongBench for few-shot evaluation.

**What it is claimed to measure.** Its reported measurement role is concentrated rather than spread across many targets. Papers most commonly use TREC to measure the behavioral indicator Text classification, typically in the form of 6-way question classification, and papers link it to one behavioral indicator overall and one construct overall. A smaller line of work reports it as measuring Prompt sensitivity, using TREC examples to compare predicted class distributions across prompt rephrasings.

**Space of uses.** No measurement instrument is linked to it through explicit relationships. In the paper descriptions, TREC is usually one dataset in a broader evaluation bundle for text classification or general NLU, often appearing alongside AG News, Subj, MR, DBPedia, and CB. Some papers also place it in in-context, few-shot, or long-context evaluation settings rather than using it only as a standalone classification benchmark.

## Sources

**TREC** (12 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [Revisiting In-context Learning Inference Circuit in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/22d4f952efa13970f0b1ffb22170d416-Paper-Conference.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf), [Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25x/he25x.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf))
> A question classification dataset from the Text REtrieval Conference (TREC), where the task is to classify questions into six types.

**Trec** (2 papers: [DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf))
> A dataset from the LongBench suite used to evaluate few-shot learning performance.

## Relationships

### → TREC
- **Text classification** (behavioral indicator): *measured_by*, 8 papers
  > We study 4-way news classification AGNews (Zhang et al., 2015), 6-way question classification TREC (Voorhees & Tice, 2000)... (Section 5.1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
  - [DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf)
- **Prompt sensitivity** (construct): *measured_by*, 1 paper
  > “Figure 2: Predicted class distributions over prompt rephrasings pτ across three samples of the same class Person (TREC dataset, Section 4).”
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
