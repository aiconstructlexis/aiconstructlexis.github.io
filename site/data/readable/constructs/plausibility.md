# Plausibility
**Type:** Construct  
**Supporting papers:** 11  

## State of the Field

**Space of definitions.** Across the surveyed work, plausibility is most commonly described as a human-facing quality of generated explanations or rationales: they are relevant to the input question, supported by established language-based facts, and make sense on their own. Some papers add that this judgment can rest on common, logical, or factual sense and can be separated from whether the final answer is correct. A smaller line of work broadens the term to human judgments of hypotheses or explanations as credible, reasonable, intuitive, coherent, and convincing, even when this does not fully reflect the model's internal decision process.

**Space of facets.** Papers most often systematize plausibility through contrasts rather than subtypes. It is repeatedly paired with faithfulness, with papers saying explanations should be both faithful and plausible, and one paper explicitly discussing a trade-off between the two, and it is also used as a dimension of interpretability and explainability. In work on explanation quality, implausibility is separated from hallucination: explanations that lack informativeness are described as implausible, whereas explanations that contradict visual-grounded facts are described as hallucinations.

**Space of measurement.** Plausibility is linked to 3 measurement instruments and no behavioral indicators. The most common instrument is human evaluation, used for direct judgments of explanations, including Likert-scale ratings of plausibility alongside faithfulness or alongside character consistency, engagement, and reasoning depth. Other operationalizations are BLiMP, a benchmark used to examine whether attributions align with human-understood linguistic rationales, and LLM-as-a-judge, where GPT-4o rates how reasonable, likely, or believable action sequences are given the context and known behavior patterns. These measures target different objects, explanations, attributions, and activity sequences, but all operationalize plausibility through judged reasonableness or alignment with human-understood rationales.

**Links.** Beyond measurement, plausibility is linked to 3 constructs. Papers relate it to interpretability and explainability by treating faithful and plausible explanations as the preferred combination and by evaluating explainability with plausibility and faithfulness metrics. Faithfulness is also separately related to plausibility, with one paper explicitly framing their connection as a trade-off. One paper claims a causal relationship from plausibility to reasoning, reporting that improving plausibility Token F1 during training also improved the model's reasoning.

## Sources

**Plausibility** (4 papers: [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf), [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf), [Literature Meets Data: A Synergistic Approach to Hypothesis Generation](https://aclanthology.org/2025.acl-long.12.pdf), [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf))
> The quality of a model's generated explanation being relevant to the input question and supported by established, language-based facts.

## Relationships

### Plausibility →
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > In addition, we build human evaluation for explanation on plausibility and faithfulness since automatic metric measures not always reflect the correctness and logicality. (Section 4.2)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
  - [R-CHAR: A Metacognition-Driven Framework for Role-Playing in Large Language Models](https://aclanthology.org/2025.emnlp-main.1372.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > When evaluating the likelihood of the activity sequences, GPT-4o is instructed to take the following criteria into account: ... Plausibility: How reasonable, likely, or believable a sequence of actions is, given the circumstances, context, and known behavior patterns.
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > We also observe that guiding models to focus on explanation signals from our dataset during training improves the plausibility Token F1 score by 3-4%, improving the model’s reasoning. (Abstract)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **BLiMP** (measurement instrument): *measured_by*, 1 paper
  > ...to examine its plausibility, i.e., the extent to which its attributions align with human-understood linguistic rationales provided by BLiMP... (Section 5)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)

### Associated with
- **Interpretability and explainability** (construct), 2 papers
  > Ideally, the explanation should be both faithful (reflecting the model’s actual behavior) and plausible (aligning with human understanding)
  - [Is the MMI Criterion Necessary for Interpretability? Degenerating Non-causal Features to Plain Noise for Self-Rationalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d53d51e88d92d3723755f6d425bc513b-Paper-Conference.pdf)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Faithfulness** (construct), 1 paper
  > In terms of interpretability, this paper focuses on the trade-off between plausibility and faithfulness. (Section 4.3)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
