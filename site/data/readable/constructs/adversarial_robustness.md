# Adversarial robustness
**Type:** Construct  
**Supporting papers:** 45  
**Also known as:** Adversarial Vulnerability, Attack resistance, Adversarial susceptibility, Adversarial vulnerability, Robustness to phonetic attacks, Distraction susceptibility, Vulnerability, Safety vulnerability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats adversarial robustness as a latent model property or ability to maintain performance, correct predictions, or intended behavior under adversarially crafted perturbations. Most definitions keep this broad, covering small input changes, vision perturbations, or malicious prompts, while narrower uses tie it to factual accuracy under adversarial examples, offensive-language detection under homophonic substitutions, or the stability of safety behavior when attackers try to bypass safeguards. A smaller line of work uses inverse labels such as adversarial vulnerability, adversarial susceptibility, distraction susceptibility, or safety vulnerability, and one paper instead defines attack resistance as the number of input bits an attacker must control to gain one bit of output control.

**Space of facets.** Papers organize the construct mainly by threat model and task: some focus on small, often imperceptible perturbations, others on jailbreak or prompt-injection attempts to elicit undesirable behavior, human-crafted misinformation, phonetic attacks, attacks on internal activations, or adversarial manipulation of LLM judges. They also place it differently in broader conceptual schemes: one paper describes adversarial robustness as an aspect of reliability, another discusses it alongside out-of-distribution robustness, and another relates attack susceptibility to safety alignment in additional modalities. Naming is not uniform, because closely related uses appear under robustness, vulnerability, susceptibility, and resistance labels.

**Space of measurement.** Operationalization is benchmark-heavy: papers link the construct to 11 measurement instruments and 1 behavioral indicator. The most commonly linked instruments are AdvBench, GCG, HarmBench, AG News, and AgentDojo, and the quoted evaluations often make robustness concrete as attack success rate or performance under harmful instructions, adversarial prompt injection, and task-level classification attacks. This mostly matches the dominant definitions about maintaining performance under attack, though some measurements narrow the target to factual adversarial examples, agent tool use over untrusted data, or safety-focused attack settings.

**Links.** In non-measurement links, one paper claims a causal relationship from General ability to adversarial robustness, with the evidence framed as increased model capabilities giving rise to emergent model vulnerabilities. Another paper claims a causal relationship from adversarial robustness to Jailbreaking, describing LLMs as "fragile and easily distracted" by complex role-play instructions, thereby enhancing jailbreak attack performance. Separately, papers relate adversarial robustness to Reliability, discuss it alongside Robustness in the form of out-of-distribution versus adversarial robustness, and relate it to Safety alignment through multimodal attack susceptibility; no correlational link is reported.

## Sources

**Adversarial robustness** (10 papers: [An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf), [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf), [TripleFact: Defending Data Contamination in the Evaluation of LLM-driven Fake News Detection](https://aclanthology.org/2025.acl-long.431.pdf), [An Interpretable N-gram Perplexity Threat Model for Large Language Model Jailbreaks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boreiko25a/boreiko25a.pdf), [Gamma-Guard: Lightweight Residual Adapters for Robust Guardrails in Large Language Models](https://aclanthology.org/2025.emnlp-main.614.pdf))
> The latent property of a model to maintain its performance and make correct predictions when faced with small, intentionally crafted perturbations to its input.

**Adversarial Vulnerability** (1 paper: [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf))
> The latent susceptibility of a model to adversarial perturbations, inferred from attack success rates.

**Adversarial susceptibility** (1 paper: [Scaling Laws for Adversarial Attacks on Language Model Activations and Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434a6b40f8f65488e722bc33d796c8b-Paper-Conference.pdf))
> The degree to which a model's outputs can be manipulated by small, targeted perturbations to its inputs or internal states.

**Attack resistance** (1 paper: [Scaling Laws for Adversarial Attacks on Language Model Activations and Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434a6b40f8f65488e722bc33d796c8b-Paper-Conference.pdf))
> A model property representing the number of bits the attacker must control on the input to exert a single bit of control on the output.

**Adversarial vulnerability** (1 paper: [X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf))
> The degree to which a model's performance degrades or its outputs can be manipulated by small, maliciously crafted input perturbations.

**Robustness to phonetic attacks** (1 paper: [Enhancing Chinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1154.pdf))
> The model's ability to maintain performance in detecting offensive language when faced with inputs that have been intentionally altered with homophonic substitutions to evade detection.

**Distraction susceptibility** (1 paper: [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf))
> The tendency of LLMs to fail in recognizing malicious intent due to cognitive overload or contextual interference caused by complex role-playing instructions.

**Vulnerability** (1 paper: [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://aclanthology.org/2025.emnlp-main.138.pdf))
> The susceptibility of LLM judges to adversarial manipulations such as prompt injection or adversarial phrases that distort judgment outcomes.

**Safety vulnerability** (1 paper: [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.487.pdf))
> A latent weakness in a model's architecture or alignment that can be exploited to bypass its safety mechanisms.

## Relationships

### Adversarial robustness →
- **AdvBench** (measurement instrument): *measured_by*, 3 papers
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
  - [AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 2 papers
  > We compute the correlation between the capability score and safety scores on the following benchmarks: AdvGLUE [91], AdvGLUE++ [34], AdvDemonstration [34], and HarmBench [51]. (Section 4.2)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **GCG** (measurement instrument): *measured_by*, 2 papers
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Scaling Trends in Language Model Robustness](https://raw.githubusercontent.com/mlresearch/v267/main/assets/howe25a/howe25a.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **GLUE** (measurement instrument): *measured_by*, 1 paper
  > Existing research evaluates adversarial robustness of LLMs on the GLUE dataset (Wang et al., 2018)
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **FM2** (measurement instrument): *measured_by*, 1 paper
  > To investigate this [whether LLMs can withstand adversarial examples], we utilize two datasets, namely Symmetric (Schuster et al., 2019) and FM2 (Eisenschlos et al., 2021). (Section 2.1)
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **AgentDojo** (measurement instrument): *measured_by*, 1 paper
  > To measure the adversarial robustness of AI agents, we introduce AgentDojo, an evaluation framework for agents that execute tools over untrusted data.
  - [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AG News** (measurement instrument): *measured_by*, 1 paper
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 1 paper
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **AutoDAN** (measurement instrument): *measured_by*, 1 paper
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **Jailbreaking** (behavioral indicator): *causes*, 1 paper
  > "LLMs are notably fragile and easily distracted by our complex role-play instructions, thereby enhancing the attack performance of each individual jailbreak character."
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)
- **JailbreakBench** (measurement instrument): *measured_by*, 1 paper
  > To assess how robust our models are to adversarial prompt injection, we evaluate them on the JailBreakBench dataset. (Section 3.3.4. ADVERSARIAL ROBUSTNESS EVALUATION)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)

### → Adversarial robustness
- **General ability** (construct): *causes*, 1 paper
  > increased model capabilities give rise to distinct emergent model vulnerabilities. (Section 1)
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)

### Associated with
- **Reliability** (construct), 1 paper
  > This paper studies one key aspect of LLM’s reliability—adversarial robustness.
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > Following the common practice in the field [132, 147], we consider the out-of-distribution (OOD) and adversarial robustness respectively. (Sec. 2.2.3)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety alignment** (construct), 1 paper
  > larger models are more susceptible to multimodal attacks, revealing the lack of safety alignment in the additional modalities. (Section 4.2, Finding A3)
  - [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf)
