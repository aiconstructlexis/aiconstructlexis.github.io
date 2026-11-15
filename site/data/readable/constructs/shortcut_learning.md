# Shortcut learning
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Reliance on spurious correlations, Spurious correlation capture, Task-specific heuristics  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats shortcut learning as a tendency to exploit spurious, superficial, or statistically common correlations between inputs and labels, rather than the intended task features or underlying concept. Several definitions tie this to good in-distribution performance alongside poor generalization on minority or out-of-distribution examples, and one study says models can show "apparent task proficiency" that stems from shortcut learning rather than genuine understanding. Smaller variants narrow the phenomenon to batch-level spurious correlation capture, or recast it as task-specific heuristics, meaning narrow non-generalizable strategies instead of a unified, interpretable world model.

**Space of facets.** Papers most often use shortcut learning interchangeably with reliance on spurious correlations, superficial patterns, or simple statistical correlations, and one paper describes "shortcut circuits" that directly influence outputs based on salient features. The recurring contrasts are between shortcuts and intended underlying task features, deeper task-relevant reasoning, robust underlying concepts, genuine core knowledge understanding, or a single universal law or world model. The main variation is the level at which the shortcut is located: broad regularities in majority training data versus locally induced correlations within particular mini-batches.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to the construct. Instead, papers describe it through patterns such as exploiting majority-data correlations, relying on salient cues like names or stereotypes, partially encoding batch-specific irrelevant content as if it were predictive, or showing task proficiency without acquiring the underlying concept. These descriptions mirror the definitional language rather than a separate linked instrument.

**Links.** Across the recorded relationships, papers only claim causal links outward from shortcut learning, to generalization, robustness, and out-of-distribution generalization. One paper claims a causal relationship from shortcut learning to generalization, reporting statistical evidence that it undermines generalization in argument mining; another claims a causal relationship from shortcut learning to robustness, stating that learned shortcuts can undermine robustness; and that same paper also claims a causal relationship from shortcut learning to out-of-distribution generalization, noting that models may rely on shortcuts and fail to generalize to out-of-distribution data.

## Sources

**Shortcut learning** (4 papers: [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf), [Core Knowledge Deficits in Multi-Modal Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25p/li25p.pdf), [Robust Native Language Identification through Agentic Decomposition](https://aclanthology.org/2025.emnlp-main.423.pdf), [Co-occurrence is not Factual Association in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/775226eaa2a36c543e2bd6cc9eae1b6a-Paper-Conference.pdf))
> The tendency of models to rely on spurious correlations between input features and labels that are prevalent in majority training data but irrelevant to the actual task, leading to poor generalization on minority or out-of-distribution examples.

**Reliance on spurious correlations** (1 paper: [Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases](https://aclanthology.org/2025.acl-long.469.pdf))
> The model's tendency to use superficial or statistically common but causally unrelated patterns in the training data to make predictions, rather than learning the intended underlying task features.

**Spurious correlation capture** (1 paper: [Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ju25a/ju25a.pdf))
> The model's propensity to learn and encode spurious patterns that appear correlated with the objective within a specific mini-batch, even if they are globally irrelevant.

**Task-specific heuristics** (1 paper: [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf))
> The tendency of a foundation model to develop narrow, non-generalizable strategies for specific tasks rather than learning a unified, interpretable world model, leading to poor extrapolation under distribution shift.

## Relationships

### Shortcut learning →
- **Generalization** (construct): *causes*, 1 paper
  > Statistical evidence that shortcut learning undermines generalization in argument mining. (Section 1)
  - [Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments](https://aclanthology.org/2025.acl-long.1164.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > This association can create a spurious correlation between the filmmaker’s names and sentiment, leading LMs to learn shortcuts that can undermine their robustness. (Section 3.1)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf)
- **Out-of-distribution generalization** (construct): *causes*, 1 paper
  > ...the model can rely on these ‘shortcuts’ and fail to generalize to out-of-distribution data. (Section 3.1)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf)
