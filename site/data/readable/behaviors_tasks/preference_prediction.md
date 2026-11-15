# Preference prediction
**Type:** Behavioral indicator  
**Supporting papers:** 17  
**Also known as:** Recipe preference prediction, Preference score prediction, Reward model scoring, Preference label classification, Preference classification, Preferred response prediction, Preference judgment  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is pairwise prediction: choosing which of two responses, answers, or solutions is preferred for a prompt, context, or conversation. Papers differ in who supplies the preference signal, including humans, a broader mechanism such as an LLM-as-a-judge or reward model, a community whose members would upvote one answer more, or a judge or jury in multi-turn dialogue; some authors further describe the task as predicting a mechanism's decisions from concept-based representations. A smaller line of work treats the behavior as predicting a scalar preference score or specific preference level for a single response or item, including user-specific reward scores, numerical ratings, generated-text scores, or average consumer satisfaction for recipes. Success is usually framed as selecting the preferred option or assigning it the higher score, with accuracy or the fraction of cases where the preferred item scores higher used as recurring criteria.

**Variants.** Papers use names such as recipe preference prediction, preference score prediction, reward model scoring, preferred response prediction, and preference judgment, alongside other classification-style formulations. The settings range from recipe pairs with similar ingredients but different average ratings, to unseen user-specific response choices, to multi-turn conversations, community-conditioned answer selection by likely upvotes, comparative judgments between mathematical solutions, and user preference levels for items in multimodal recommendation. Across these variants, the output may be a binary label, a relative-quality judgment, or a scalar score.

**Space of elicitation and scores.** Papers link this behavior to 3 measurement instruments overall. The instruments named most often are LLM-as-a-judge, MT-Bench, and RewardBench. For direct measurement, papers say preference prediction is measured by MT-Bench, described as a preference dataset comparing human preferences over model outputs in open-ended multi-turn questions, and by RewardBench, used as a test benchmark; a further paper relates LLM-as-a-judge to preference prediction as using an LLM's predictions to approximate human preferences.

**What it is taken as evidence of.** Papers link preference prediction to 2 constructs, and the links do not repeat a single construct. One paper relates objective mismatch to preference prediction, saying that preference label classification performance reveals mismatch between text generation and preference modeling. Another reports that preference prediction correlates with social bias, with lower accuracy in vegetarian versus non-vegetarian recipe comparisons described as reflecting an omnivore bias.

## Sources

**Recipe preference prediction** (1 paper: [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf))
> Predicting which recipe a target population will prefer or rate more highly.

**Preference score prediction** (1 paper: [CoPL: Collaborative Preference Learning for Personalizing LLMs](https://aclanthology.org/2025.emnlp-main.650.pdf))
> The model's output of a scalar score indicating the degree to which a given response aligns with a specific user's preferences.

**Preference prediction** (5 papers: [Multi-Domain Explainability of Preferences](https://aclanthology.org/2025.emnlp-main.736.pdf), [Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1646e34971facbcda3727d1dc28ab635-Paper-Conference.pdf), [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [ComPO: Community Preferences for Language Model Personalization](https://aclanthology.org/2025.naacl-long.419.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> The task of predicting which of two responses is preferred by a mechanism (human, LLM-as-a-judge, or reward model) based on concept-based representations.

**Reward model scoring** (1 paper: [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf))
> The observable task of a model acting as an evaluator to assign a score to a generated text, predicting its alignment with human preferences.

**Preference label classification** (1 paper: [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf))
> The task of predicting which of two given responses is more preferable for a given prompt.

**Preference classification** (1 paper: [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf))
> Predicting the preferred answer between a pair of responses based on human feedback rankings.

**Preferred response prediction** (1 paper: [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf))
> Selecting the most likely user-preferred response from a set of candidates for a given context, based on a learned reward model.

**Preference judgment** (1 paper: [Amulet: Putting Complex Multi-Turn Conversations on the Stand with LLM Juries](https://aclanthology.org/2025.emnlp-main.1300.pdf))
> The observable act of selecting one of two candidate responses as the better response in a multi-turn conversational context.

## Relationships

### Preference prediction →
- **RewardBench** (measurement instrument): *measured_by*, 1 paper
  > We use RewardBench (Lambert et al., 2024) as the test benchmark. (Section 4)
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-Bench (Zheng et al., 2023) is a preference dataset which compares human preferences of several model outputs on open-ended questions using multi-turn conversations. (Section 3)
  - [Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf)
- **Social bias** (construct): *correlates*, 1 paper
  > Within the vegetarian vs. non-vegetarian meal comparisons, accuracy is lower when vegetarian options are rated higher, reflecting LLMs’ omnivore bias, as LLMs more frequently prefer non-vegetarian options compared to ground truth human preferences.
  - [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf)

### Associated with
- **Objective mismatch** (construct), 1 paper
  > The performance on preference label classiﬁcation also reveals that cDPO struggles with objective mismatch between the text generation and preference modeling... (Section 1).
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > "using an LLM’s predictions to approximate human preferences between them, a technique often referred to as LLM-as-judge"
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
