# Reliability
**Type:** Construct  
**Supporting papers:** 50  
**Also known as:** Model reliability, Reasoning reliability, Clinical reliability, Code reliability, Answer reliability, Internal consistency, Scoring reliability  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats reliability as a broad property of model outputs and behavior, centered on trustworthiness, consistency, dependability, and often correctness or factual accuracy, sometimes extending to safety. Several papers spell this out as producing outputs that are trustworthy, factually correct, or free from outdated, incorrect, biased, low-quality, or hallucinated content, and one account adds that reliable models should generate faithful content while expressing uncertainty or acknowledging missing knowledge. A smaller line of work narrows the construct to specific settings, such as valid reasoning traces, medical reports suitable for clinical decision-making, executable code, reward-model solution selection or scoring, and successful application of a targeted edit. Another minority framing shifts the locus from external outputs to agreement within the model or response pattern, defining reliability through internal consistency between intermediate and final predictions, or between items intended to measure the same construct.

**Space of facets.** Usage varies mainly by scope and locus. Many papers keep reliability as an umbrella term, while others break it into task-specific variants for reasoning, clinical use, code generation, and answer generation, with additional work applying the term to reward models and model editing. One paper explicitly treats adversarial robustness as one aspect of reliability, while other work uses different consistency notions as proxies for reliability. A separate strand focuses on agreement among intermediate predictions or among responses to items aimed at the same construct, which differs from the more common framing around external output dependability.

**Space of measurement.** Papers operationalize it with 2 linked measurement instruments, TruthfulQA and CounterFact, plus 3 linked behavioral indicators, Hallucination, Knowledge editing, and Self-verification. TruthfulQA is explicitly used as a benchmark-style measure of reliability in terms of factualness, common sense, and truthfulness, while CounterFact is used in editing evaluations where reliability is assessed alongside other editing dimensions. These operationalizations cover only part of the broader definitions, focusing mainly on truthful outputs or edit success rather than the wider safety, uncertainty, reasoning, clinical, code, or scoring framings. The behavioral indicators make this concrete by tying low reliability to hallucination, relating it to remembering edits after sequential editing, and improving it through reviewer-style self-verification.

**Links.** Beyond measurement, papers link reliability to 9 constructs and 3 behavioral indicators. Hallucination is the most repeated connection: several papers claim a causal relationship from Hallucination to Reliability, using language such as hallucinations undermining or lowering reliability, while other papers record the pair as related. Single-paper claims also point from Calibration and Editing locality to Reliability, and both pairs are described elsewhere as related rather than causal. Other work adds 4 further causal links and 5 further related links, and no correlational links are reported.

## Sources

**Reliability** (14 papers: [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf), [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf), [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf), [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf), [What Makes a Good Natural Language Prompt?](https://aclanthology.org/2025.acl-long.292.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf), [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/880ee6e23b6ee548ebcccafe0ef0f513-Paper-Conference.pdf), [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf), [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf), [MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf))
> The latent property of a model consistently performing correctly and safely, which uncertainty quantification aims to improve.

**Model reliability** (1 paper: [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf))
> The overall dependability and consistency of a model's performance and outputs across different situations.

**Reasoning reliability** (1 paper: [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf))
> The consistency and trustworthiness of a model's reasoning outputs, such that generated rationales are valid and lead to correct conclusions across diverse problems.

**Clinical reliability** (1 paper: [ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.598.pdf))
> The extent to which a generated medical report is trustworthy and valid for use in real-world clinical decision-making.

**Code reliability** (1 paper: [Reliable and Cost-Effective Exploratory Data Analysis via Graph-Guided RAG](https://aclanthology.org/2025.emnlp-main.836.pdf))
> The latent property of a model to consistently generate code that is syntactically correct and executable without errors.

**Answer reliability** (1 paper: [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf))
> The degree to which the model's generated answers are accurate, complete, and trustworthy, often enhanced through verification processes.

**Internal consistency** (2 papers: [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf), [Fingerprinting LLMs through Survey Item Factor Correlation: A Case Study on Humor Style Questionnaire](https://aclanthology.org/2025.emnlp-main.13.pdf))
> The degree of agreement between latent predictions decoded from intermediate layers and the final prediction, reflecting the stability of the model's internal reasoning process.

**Scoring reliability** (1 paper: [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf))
> The degree to which a reward model consistently and accurately assigns scores that reflect true human preferences, enhanced by access to external verification tools.

## Relationships

### Reliability →
- **TruthfulQA** (measurement instrument): *measured_by*, 2 papers
  > we use TruthfulQA [27] to measure the reliability of the outputs generated by Aligner in terms of factualness and common sense. (Section 3.2)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 1 paper
  > experiments on COUNTERFACT and MQuAKE shows that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)

### → Reliability
- **Hallucination** (behavioral indicator): *causes*, 5 papers
  > Long CoT suffers from high cost for training and exhibits low reliability due to table content hallucinations. (Abstract)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
  - [DecoupleSearch: Decouple Planning and Search via Hierarchical Reward Modeling](https://aclanthology.org/2025.emnlp-main.222.pdf)
  - [MusKGC: A Flexible Multi-source Knowledge Enhancement Framework for Open-World Knowledge Graph Completion](https://aclanthology.org/2025.emnlp-main.508.pdf)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f14fb9acd243c13c95d4a490d1684ce-Paper-Conference.pdf)
- **Calibration** (construct): *causes*, 2 papers
  > Confidence calibration is a critical aspect in developing reliable and trustworthy language models (Nguyen & O’Connor, 2015; Guo et al., 2017; Minderer et al., 2021).
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [COM-BOM: Bayesian Exemplar Search for Efficiently Exploring the Accuracy-Calibration Pareto Frontier](https://aclanthology.org/2025.emnlp-main.1027.pdf)
- **Editing locality** (construct): *causes*, 2 papers
  > "This limitation results in poor editing locality, which can lead to the persistence of irrelevant or inaccurate facts, ultimately compromising the reliability of LLMs."
  - [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > For reliability, generalization, and portability evaluations, LLaVA-1.5 outperforms BLIP-2 and MiniGPT-4. This improved performance can be attributed to its larger model size and better instruction-following capability... (Section 5.2.1)
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Positional bias** (construct): *causes*, 1 paper
  > "This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications."
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > Both aspects [factuality and instruction-following] significantly impact reliability and user experience in real-world applications and are challenging to evaluate effectively with existing reward models (Section 3).
  - [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://aclanthology.org/2025.acl-long.775.pdf)
- **Self-verification** (behavioral indicator): *causes*, 1 paper
  > Reviewer agent – Verifies and refines the initial answer to improve accuracy and reliability (Section 3)
  - [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf)

### Associated with
- **Adversarial robustness** (construct), 1 paper
  > This paper studies one key aspect of LLM’s reliability—adversarial robustness.
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > we find that it seems to be an impossible triangle—reliability, generalization, and locality can not be realized at the same time in the continual editing settings. (Section 1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Knowledge editing** (behavioral indicator), 1 paper
  > i) reliability, the model can remember both current and previous edits after sequential editing
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Preference consistency** (construct), 1 paper
  > logical preference consistency serves as a useful proxy for preference reliability. (Section 1)
  - [Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25u/liu25u.pdf)
- **Instance-level stability** (construct), 1 paper
  > Low DR and NDR values signify that an accelerated VLM maintains behavioral fidelity and reliability. (Section 1)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
