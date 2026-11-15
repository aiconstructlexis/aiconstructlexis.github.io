# JailbreakBench
**Type:** Measurement instrument  
**Supporting papers:** 31  
**Also known as:** Jailbreakbench, JBB-Behavior, JBB-Behaviors, JBB  

## State of the Field

**What it is.** Across the papers, the dominant framing treats JailbreakBench as an open or standardized benchmark for evaluating jailbreak attacks and model safety or robustness. Most descriptions present it as a dataset of harmful queries, unsafe behavior prompts, or instructions, often using 100 prompts or instances, though some papers define it more narrowly as an evaluation protocol that uses an LLM judge to detect detailed disallowed responses, and one describes a leaderboard that collects attacks designed to bypass safety filters. A smaller line of work refers to template and direct variants, and some authors use the names JBB, JBB-Behavior, or JBB-Behaviors for harmful-query or harmful-behavior versions used in evaluation.

**What it is claimed to measure.** Papers link JailbreakBench to three constructs, Harmlessness, Adversarial robustness, and Safety, and to one behavioral indicator, Jailbreaking. The prevailing use is to measure jailbreak performance, success, or resistance, often through Attack Success Rate, while other papers use it to assess harmlessness on mixed harmful-query sets, adversarial robustness to prompt injection, or safety on harmful prompts. Taken together, the measurement claims are spread across several evaluation targets rather than centered on a single construct.

**Space of uses.** No measurement instrument is linked to it. Papers frequently use it alongside other safety benchmarks, most commonly HarmBench, and more occasionally AdvBench, Malicious Instruct, StrongReject, and WildChat. Most papers use it directly to evaluate attacks or defenses, sometimes with sampled prompts or prior jailbreak results on JBB, while some operationalizations rely on an LLM judge or a pretrained Llama-3-70B-Instruct classifier for overall evaluation.

## Sources

**JailbreakBench** (14 papers: [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf), [The TIP of the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks on LLMs](https://aclanthology.org/2025.acl-long.334.pdf), [Activation Space Interventions Can Be Transferred Between Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oozeer25a/oozeer25a.pdf), [Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models](https://aclanthology.org/2025.emnlp-main.1471.pdf), [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf), [Foot-In-The-Door: A Multi-turn Jailbreak for LLMs](https://aclanthology.org/2025.emnlp-main.100.pdf), [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf), [Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://aclanthology.org/2025.emnlp-main.1493.pdf), [SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.825.pdf), [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf), [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf), [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf), [Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks](https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf), [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf))
> A standardized benchmark designed to evaluate a large language model's safety and robustness against a variety of jailbreak attacks.

**Jailbreakbench** (1 paper: [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf))
> A harmful-query benchmark used to test jailbreak resistance and safety degradation after head ablation.

**JBB-Behavior** (1 paper: [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf))
> JBB-Behavior, a safety benchmark used to assess harmful or unsafe behavior generation.

**JBB-Behaviors** (1 paper: [SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1291.pdf))
> Safety benchmark dataset containing harmful behaviors used to evaluate model responses to malicious queries.

**JBB** (1 paper: [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf))
> Jailbreak Benchmark (JBB), a dataset used here to collect jailbreak results for experience initialization and evaluation of jailbreak attacks.

## Relationships

### → JailbreakBench
- **Harmlessness** (construct): *measured_by*, 2 papers
  > For harmlessness evaluation, we generated responses from the aligned LLM on a mixed dataset of AdvBench (Zou et al., 2023) and JailbreakBench (Chao et al., 2024)...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 2 papers
  > We adopt Attack Success Rate (ASR) as an evaluation metric for successful jailbreaks following the default framework employed in HarmBench and JbBench. (Section 5.4)
  - [SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.825.pdf)
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > We evaluated Jailbreak Antidote using JailbreakBench (Chao et al., 2024) for assessing safety, focusing on 100 harmful prompts. (Section 5.1)
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **Adversarial robustness** (construct): *measured_by*, 1 paper
  > To assess how robust our models are to adversarial prompt injection, we evaluate them on the JailBreakBench dataset. (Section 3.3.4. ADVERSARIAL ROBUSTNESS EVALUATION)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
