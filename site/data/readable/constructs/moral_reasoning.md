# Moral reasoning
**Type:** Construct  
**Supporting papers:** 17  
**Also known as:** Machine ethics, Ethical reasoning, Ethics, Morality  

## State of the Field

**Space of definitions.** Most papers treat moral reasoning as a latent or cognitive ability to make judgments in ethically complex situations, especially when principles conflict or trade-offs are involved. Closely related definitions cast it as evaluating the moral and consequential implications of actions, adhering to ethical principles, and recognizing actions that are against human morality, with one formulation explicitly placing it beyond "superficial rule-following." A smaller line of work frames it instead as an underlying process of weighing harm, fairness, and social norms, or as a capacity shown through principled or stage-like justification and through associative networks of moral concepts.

**Space of facets.** Papers use several overlapping labels for nearby territory, including ethical reasoning, machine ethics, ethics, and morality, and they do not draw a sharp boundary among them. Some organize the construct through value-based theories and competing moral principles in daily-life dilemmas, while others distinguish underlying moral reasoning from final moral judgments, or describe it in terms of abstract reasoning and "higher moral stages." In a smaller line of work, Action prediction is treated as one of the core concepts of moral reasoning.

**Space of measurement.** Operationalization is fairly concentrated: papers link moral reasoning to 2 measurement instruments and 1 behavioral indicator. ETHICS is the most common instrument, used as a benchmark for machine ethics or moral reasoning, including scenario-based commonsense moral recognition tasks and deontological settings; Social Chemistry 101 appears as another benchmark under morality, and the linked behavioral indicator is Action prediction. These operationalizations mainly use benchmark performance on scenario judgments and moral recognition, which aligns with definitions centered on ethical judgment and recognition, though some definitions also emphasize consequential evaluation, trade-offs, or justification.

**Links.** Beyond measurement, one paper claims a causal relationship from Human preference alignment to moral reasoning, reporting improved machine ethics benchmark performance after RLHF on a general-purpose preference dataset. Papers also report that moral reasoning is related to Trustworthiness, where machine ethics is treated as one component in a broader trustworthiness framework. A smaller line of work relates Action prediction to moral reasoning by treating it as one of its core concepts.

## Sources

**Ethical reasoning** (3 papers: [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf), [A Checks-and-Balances Framework for Context-Aware Ethical AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25a/chang25a.pdf), [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf))
> The latent ability to evaluate the moral and consequential implications of actions, beyond superficial rule-following.

**Machine ethics** (1 paper: [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf))
> The model's adherence to ethical principles and its ability to recognize actions that are against human morality.

**Moral reasoning** (4 papers: [DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://proceedings.iclr.cc/paper_files/paper/2025/file/8587069d00a69d0ea498d547fffad6dd-Paper-Conference.pdf), [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf), [Comparing Moral Values in Western English-speaking societies and LLMs with Word Associations](https://aclanthology.org/2025.acl-long.177.pdf), [EMNLP: Educator-role Moral and Normative Large Language Models Profiling](https://aclanthology.org/2025.emnlp-main.42.pdf))
> The cognitive ability to navigate and make judgments in situations involving complex and often conflicting ethical principles.

**Ethics** (1 paper: [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf))
> The model's capacity to adhere to moral principles and make ethically sound judgments, particularly in complex dilemmas.

**Morality** (1 paper: [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf))
> The model's latent adherence to ethical principles and commonsense moral judgments when presented with scenarios involving right and wrong.

## Relationships

### Moral reasoning →
- **ETHICS** (measurement instrument): *measured_by*, 5 papers
  > To verify ALI-Agent’s effectiveness as a general evaluation framework, we conduct experiments on six datasets from three distinct aspects of human values: ...morality (ETHICS [3], Social Chemistry 101 [37])...
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf)
  - [Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework](https://aclanthology.org/2025.emnlp-main.1541.pdf)
- **Social Chemistry 101** (measurement instrument): *measured_by*, 1 paper
  > To verify ALI-Agent’s effectiveness as a general evaluation framework, we conduct experiments on six datasets from three distinct aspects of human values: ...morality (ETHICS [3], Social Chemistry 101 [37])...
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)

### → Moral reasoning
- **Human preference alignment** (construct): *causes*, 1 paper
  > RLHF applied to a general-purpose preference dataset leads to a substantial average improvement of 31% on the machine ethics benchmark. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)

### Associated with
- **Trustworthiness** (construct), 1 paper
  > These components [truthfulness, toxicity, fairness, robustness, privacy, and machine ethics] collectively contribute to a comprehensive framework for assessing and improving LLM trustworthiness. (Section 2)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Action prediction** (behavioral indicator), 1 paper
  > While numerous tasks can be accomplished using UNIMORAL, we focus on four core concepts of moral reasoning: [I] Action Prediction (AP)... (Section 4)
  - [Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](https://aclanthology.org/2025.acl-long.294.pdf)
