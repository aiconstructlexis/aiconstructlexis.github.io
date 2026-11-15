# ToxiGen
**Type:** Measurement instrument  
**Supporting papers:** 27  
**Also known as:** Toxigen, TOXIGEN  

## State of the Field

**What it is.** Across papers, ToxiGen is most commonly described as a toxicity benchmark or dataset for evaluating toxic versus neutral generation behavior. Definitions vary in emphasis: some frame it as a benchmark for toxic language generation or safety, while others describe a synthetic or machine-generated dataset for adversarial and implicit hate speech detection. Several papers specify content such as benign or neutral and toxic statements or questions about 13 demographic or minority groups, and one description says it comprises approximately 274k statements evenly split between toxic and non-toxic language. A smaller line of work highlights subset use, for example taking only prompts designed to elicit toxic language.

**What it is claimed to measure.** Across the surveyed work, claims concentrate on safety and toxicity: papers link ToxiGen to 3 constructs in total, most often Safety and Toxicity, with a smaller line using it to measure Harmlessness. Papers also link it to 4 behavioral indicators, most often Harmful content generation, and additionally Harmful content detection, Hate speech detection, and Text generation. The recorded links consistently describe ToxiGen as measuring these targets, and some papers specifically say it evaluates a model's ability to avoid generating toxic content or use it for toxicity detection.

**Space of uses.** Papers often use ToxiGen alongside other safety or toxicity benchmarks, especially RealToxicityPrompts and TruthfulQA, and also with Hendrycks Ethics, MMLU, and XSTest, usually as part of broader evaluation suites. It appears both in dedicated safety evaluations and in broader setups that also assess coding, reasoning, or general capability. Operationalizations differ across papers: some use zero-shot or default evaluation-harness protocols, some report two-way classification accuracy, and others generate continuations and then score the outputs with an external toxicity classifier.

## Sources

**ToxiGen** (9 papers: [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf), [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf), [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf), [The Art of Saying No: Contextual Noncompliance in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/58e79894267cf72c66202228ad9c6057-Paper-Datasets_and_Benchmarks_Track.pdf), [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf))
> A toxicity benchmark for evaluating toxic versus neutral generation behavior.

**Toxigen** (5 papers: [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf), [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf), [AmpleHate: Amplifying the Attention for Versatile Implicit Hate Detection](https://aclanthology.org/2025.emnlp-main.1469.pdf))
> Toxigen, a benchmark used in LLM Harness for toxicity evaluation.

**TOXIGEN** (1 paper: [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf))
> Benchmark for detecting toxic language generation, used to assess whether fine-tuning increases harmful output tendencies.

## Relationships

### → ToxiGen
- **Safety** (construct): *measured_by*, 5 papers
  > Results of MOD ... achieving precise control over general capabilities, including safety (Toxigen), coding (Codex), and reasoning (∗ COT).
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **Toxicity** (construct): *measured_by*, 5 papers
  > We rely on ToxiGen [13] for assessing the model’s toxicity.
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 3 papers
  > We take only the prompts designed to produce toxic language (‘hateful’ prompts) and use 500 prompts per group to reduce evaluation costs. (Appendix D).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > For the open-ended generation tasks, we apply SADI on TriviaQA (Joshi et al., 2017), TruthfulQA (Lin et al., 2022), ToxiGen (Hartvigsen et al., 2022) datasets. (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Hate speech detection** (behavioral indicator): *measured_by*, 1 paper
  > ToxiGen (Hartvigsen et al., 2022): A large-scale machine-generated dataset for hate speech detection. (Section 7.1)
  - [ImpScore: A Learnable Metric For Quantifying The Implicitness Level of Sentences](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd6bb13e78da078d8adcabbe6d9ca737-Paper-Conference.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > Our experiments focus on Helpfulness (Alpaca Eval 2.0 (Dubois et al., 2024) and IFEval (Zhou et al., 2023)), Harmlessness (Toxigen (Hartvigsen et al., 2022)), and Coding (MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021)). (Section 4)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 1 paper
  > we evaluate general capability using MMLU... and toxicity detection using ToxiGen (Section 3).
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
