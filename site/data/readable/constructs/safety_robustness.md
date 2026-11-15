# Safety robustness
**Type:** Construct  
**Supporting papers:** 25  
**Also known as:** Jailbreak vulnerability, Jailbreak robustness, Robustness to jailbreaking, Susceptibility to jailbreaking, Jailbreaking resistance, Ethical risk, Jailbreak susceptibility  

## State of the Field

**Space of definitions.** Across definitions, papers converge on an adversarial safety framing: the construct concerns whether safety mechanisms, constraints, guardrails, or restrictions hold up when inputs are designed to manipulate the model into harmful or prohibited outputs. A common positive formulation treats it as jailbreak robustness, resistance, or robustness to jailbreaking, while another common formulation names the inverse as jailbreak vulnerability, susceptibility, or ethical risk. The main variation is scope rather than core meaning, with some definitions focusing on multilingual prompts, template-region manipulation, role-based pressure, or fine-tuning and inference-time triggers.

**Space of facets.** Papers do not offer a single formal taxonomy, but they do organize the construct around recurring attack settings. One recurring distinction is between prompt-based bypass attempts in general and narrower variants involving multilingual prompts, visual inputs, manipulative role prompts, or acquired susceptibility from fine-tuning. Across these uses, different names are applied to closely overlapping content, and one paper further describes safety functions in two parts, identifying harmful content and using that processed information during generation; papers do not link the construct to any other construct.

**Space of measurement.** Operationalization is benchmark-centered: papers link the construct to 5 measurement instruments and 1 behavioral indicator, with harmful content generation as the only linked indicator. AdvBench is the most frequently linked instrument, followed by DAN, FigStep, JailbreakV, and MM-SafetyBench, and the evidence describes these as datasets or benchmarks used to assess safety or jailbreak robustness with malicious prompts, including multimodal inputs. Several quoted passages make the measurement target explicit through attack success rates, reductions in attack success rates, and refusals to answer unsafe questions rather than producing harmful outputs.

**Links.** Outside measurement, one paper claims a causal relationship from safety robustness to harmful content generation, with supporting language that jailbreak attacks exploit vulnerabilities to elicit unintended or harmful outputs. Papers do not report correlational or general related links for this construct.

## Sources

**Safety robustness** (1 paper: [Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region](https://aclanthology.org/2025.acl-long.738.pdf))
> The degree to which a model's safety mechanisms remain effective under adversarial conditions or interventions, particularly when the template region is manipulated.

**Jailbreak vulnerability** (3 papers: [Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/7423902b5534e2b267438c85444a54b1-Paper-Conference.pdf), [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf))
> The susceptibility of an LLM to adversarial inputs that bypass its safety mechanisms and elicit harmful content generation, particularly when non-English or multilingual prompts are used.

**Jailbreak robustness** (1 paper: [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf))
> The model's latent ability to resist attacks that use specially crafted prompts to circumvent its safety mechanisms and elicit harmful responses.

**Robustness to jailbreaking** (1 paper: [Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb7baa005c239c1c7c4098c2a9e00450-Paper-Conference.pdf))
> The model's ability to resist attempts to bypass its safety mechanisms and refuse to generate harmful content, even when subjected to adversarial attacks.

**Susceptibility to jailbreaking** (1 paper: [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf))
> The model's vulnerability to adversarial prompts designed to bypass its safety mechanisms and elicit prohibited information.

**Jailbreaking resistance** (1 paper: [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf))
> The model's ability to adhere to its intended functions and restrictions when prompted with inputs designed to manipulate or exploit it.

**Ethical risk** (1 paper: [EMNLP: Educator-role Moral and Normative Large Language Models Profiling](https://aclanthology.org/2025.emnlp-main.42.pdf))
> The latent tendency of a model to produce harmful content when exposed to manipulative or adversarial role prompts, reflecting vulnerability in safety alignment.

**Jailbreak susceptibility** (1 paper: [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://aclanthology.org/2025.emnlp-main.669.pdf))
> The latent tendency of a model to bypass its safety guardrails when exposed to specific fine-tuning or inference-time triggers, reflecting an acquired vulnerability to compliance with harmful requests.

## Relationships

### Safety robustness →
- **AdvBench** (measurement instrument): *measured_by*, 2 papers
  > We performed experiments on the Advbench dataset [70] which is one of the most prevailing benchmark datasets to measure the security of LLMs. (Section 4)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Harmful content generation** (behavioral indicator): *causes*, 1 paper
  > jailbreak attacks, which exploit vulnerabilities to elicit unintended or harmful outputs, threaten LLMs safety significantly. (Abstract)
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **DAN** (measurement instrument): *measured_by*, 1 paper
  > use the AdvBench and DoAnythingNow (Shen et al., 2024) datasets to assess the safety of the LLMs. (Section 4.2.2)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
- **MM-SafetyBench** (measurement instrument): *measured_by*, 1 paper
  > ...for evaluating jailbreak robustness, we employ MM-SafetyBench (Liu et al., 2024b), FigStep (Gong et al., 2025) and JailBreaKV (Luo et al., 2024) (Section 2.1).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **FigStep** (measurement instrument): *measured_by*, 1 paper
  > ...for evaluating jailbreak robustness, we employ MM-SafetyBench (Liu et al., 2024b), FigStep (Gong et al., 2025) and JailBreaKV (Luo et al., 2024) (Section 2.1).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **JailbreakV** (measurement instrument): *measured_by*, 1 paper
  > ...for evaluating jailbreak robustness, we employ MM-SafetyBench (Liu et al., 2024b), FigStep (Gong et al., 2025) and JailBreaKV (Luo et al., 2024) (Section 2.1).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
