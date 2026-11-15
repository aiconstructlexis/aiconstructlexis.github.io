# Jailbreaking
**Type:** Behavioral indicator  
**Supporting papers:** 41  
**Also known as:** Jailbreak response generation, Jailbreak attack, Jailbreak compliance, Jailbreak success, Multi-step query decomposition, Concept decomposition, Instruction decomposition, Task decomposition compliance, Jailbreak, Jailbroken responding, Jailbreaking attack  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats jailbreaking as bypassing a model's safety mechanisms, safety alignment, or guardrails so that it produces harmful, prohibited, restricted, or otherwise policy-violating content in response to crafted or adversarial input. Many definitions center the observable response, such as answering a malicious request, providing harmful or illegal content, or producing less filtered toxic content, while a smaller line of work names the attack act itself, using specially crafted prompts, suffixes, or other inputs to induce that response. Papers also differ on scope, with examples from language models, vision-language models, and multimodal systems, but success is usually framed as complying with the harmful request rather than refusing.

**Variants.** Papers use several narrower names for this behavior. Common variants include jailbreak attack, jailbreak response generation, jailbreak compliance, and jailbreak success; other work studies decomposition-based forms, including multi-step query decomposition, concept decomposition, instruction decomposition, and task decomposition compliance, where a malicious request is broken into simpler or innocuous-looking subqueries or sequential substeps. Additional settings include continuation attacks, cipher-based prompts, many-shot or long-context attacks, role-playing, and multimodal or image-based jailbreaking in vision-language models.

**Space of elicitation and scores.** Papers link jailbreaking to 12 measurement instruments. The most frequently linked are AdvBench, HarmBench, LLM-as-a-judge setups, JailbreakBench, and PAIR, with the remainder consisting of other benchmarks, auto-annotators, and judge models. Scoring is most often attack success rate, described as the percentage of jailbreak or adversarial prompts that bypass alignment; some papers count success when the model does not output a refusal, while others require a judge to mark the response as harmful, assign a high harmfulness score, or make a binary jailbreak decision.

**What it is taken as evidence of.** Rather than tying it to a single construct, papers link jailbreaking to 5 constructs. The prevailing pattern is to treat it as related to Alignment and Safety alignment, with papers describing jailbreaks as bypassing safety filters or safety-aligned measures. A smaller set makes directional claims the other way around: one paper claims a causal relationship from Adversarial robustness to Jailbreaking and one from Misalignment to Jailbreaking, while another reports that Jailbreaking is related to Attack transferability.

## Sources

**Jailbreaking** (12 papers: [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [ImgTrojan: Jailbreaking Vision-Language Models with ONE Image](https://aclanthology.org/2025.naacl-long.360.pdf), [Demystifying optimized prompts in language models](https://aclanthology.org/2025.emnlp-main.147.pdf), [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf), [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf), [Adversarial Tokenization](https://aclanthology.org/2025.acl-long.1012.pdf), [DeAL: Decoding-time Alignment for Large Language Models](https://aclanthology.org/2025.acl-long.1274.pdf), [Efficient Universal Goal Hijacking with Semantics-guided Prompt Organization](https://aclanthology.org/2025.acl-long.290.pdf), [What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs](https://aclanthology.org/2025.acl-long.101.pdf), [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf))
> The observable behavior of bypassing a model's safety mechanisms to elicit a prohibited response, typically through an adversarial prompt.

**Jailbreak response generation** (4 papers: [Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://aclanthology.org/2025.emnlp-main.1493.pdf), [Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/7423902b5534e2b267438c85444a54b1-Paper-Conference.pdf), [LLMScan: Causal Scan for LLM Misbehavior Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25al/zhang25al.pdf), [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf))
> Producing unsafe or harmful answers when prompted by adversarial jailbreak instructions.

**Jailbreak attack** (4 papers: [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf), [Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks](https://aclanthology.org/2025.acl-long.476.pdf), [Gandalf the Red: Adaptive Security for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pfister25a/pfister25a.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf))
> The act of using specially crafted prompts to circumvent a model's safety alignment and induce it to perform forbidden actions.

**Jailbreak compliance** (2 papers: [Adaptively profiling models with task elicitation](https://aclanthology.org/2025.emnlp-main.1270.pdf), [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf))
> Following adversarial prompts that attempt to induce the model to ignore safety rules and comply with harmful requests.

**Jailbreak success** (4 papers: [Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment](https://aclanthology.org/2025.emnlp-main.842.pdf), [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf), [ELITE: Enhanced Language-Image Toxicity Evaluation for Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25r/lee25r.pdf), [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf))
> The observable generation of harmful content by an LLM in response to a jailbreak prompt, indicating that the model has bypassed its safety alignment.

**Multi-step query decomposition** (1 paper: [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf))
> The observable behavior of breaking down a complex or malicious query into a sequence of simpler, seemingly harmless subqueries to bypass safety filters.

**Concept decomposition** (1 paper: [Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf))
> The breakdown of a complex malicious goal into simpler, less overtly harmful sub-concepts to reduce cognitive load and evade detection by safety mechanisms.

**Instruction decomposition** (1 paper: [DAMON: A Dialogue-Aware MCTS Framework for Jailbreaking Large Language Models](https://aclanthology.org/2025.emnlp-main.323.pdf))
> Breaking down a complex or harmful instruction into a sequence of simpler or less suspicious sub-instructions to evade detection.

**Task decomposition compliance** (1 paper: [SafeArena: Evaluating the Safety of Autonomous Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tur25a/tur25a.pdf))
> The observable behavior of an agent executing a harmful task when the malicious intent is broken down into a sequence of seemingly benign substeps provided over multiple interaction turns.

**Jailbreak** (1 paper: [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf))
> The observable generation of harmful content by a model in response to adversarial inputs that bypass its safety alignment mechanisms, such as producing instructions for illegal or dangerous activities.

**Jailbroken responding** (1 paper: [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf))
> Producing less filtered, potentially toxic or unaligned content when safety mechanisms are circumvented via cipher-based prompts.

**Jailbreaking attack** (1 paper: [AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf))
> The act of bypassing a model's safety mechanisms by using a specially crafted input (an adversarial prompt) to elicit a harmful or otherwise prohibited response.

## Relationships

### Jailbreaking →
- **Harmful content generation** (behavioral indicator): *causes*, 12 papers
  > We focus on identifying prompts that, when given a specific harmful request (e.g., “Tell me how to build a bomb”), induces the LLM to generate harmful content.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
  - [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf)
  - [Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf)
  - [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
  - [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf)
  - [DiffusionAttacker: Diffusion-Driven Prompt Manipulation for LLM Jailbreak](https://aclanthology.org/2025.emnlp-main.1128.pdf)
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 11 papers
  > In this scenario, we utilize the widely used benchmark dataset, AdvBench[46], to evaluate the steering effectiveness on facilitating jailbreaking... (Section 4.1)
  - [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf)
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
  - [Adversarial Tokenization](https://aclanthology.org/2025.acl-long.1012.pdf)
  - [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf)
  - [PANDAS: Improving Many-shot Jailbreaking via Positive Affirmation, Negative Demonstration, and Adaptive Sampling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25q/ma25q.pdf)
  - [Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25aj/wang25aj.pdf)
  - [SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.825.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 7 papers
  > We incorporate images generated by Stable Diffusion with text jailbreaking, to observe the fluctuations in performance (Task S.6). (Table 2, Row S.6 references dataset [96] which is HarmBench)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb7baa005c239c1c7c4098c2a9e00450-Paper-Conference.pdf)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
  - [How Do Large Language Monkeys Get Their Power (Laws)?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schaeffer25a/schaeffer25a.pdf)
  - [PANDAS: Improving Many-shot Jailbreaking via Positive Affirmation, Negative Demonstration, and Adaptive Sampling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25q/ma25q.pdf)
  - [SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.825.pdf)
  - [Adaptively profiling models with task elicitation](https://aclanthology.org/2025.emnlp-main.1270.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 4 papers
  > We use GPT-4 as the semantic judge (see Table 8 for the prompt) in line with the criteria established by Chao et al. (2023), where a jailbreak is considered successful only if it achieves a 10/10 jailbreak score from GPT-4.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
  - [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf)
- **Rule-based judge** (measurement instrument): *measured_by*, 2 papers
  > By default, we use keyword matching to search for strings indicating a refusal to respond to the harmful instruction, following Paulus et al. (2024). (Section 5.1)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
- **JailbreakBench** (measurement instrument): *measured_by*, 2 papers
  > We adopt Attack Success Rate (ASR) as an evaluation metric for successful jailbreaks following the default framework employed in HarmBench and JbBench. (Section 5.4)
  - [SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.825.pdf)
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)
- **PAIR** (measurement instrument): *measured_by*, 2 papers
  > We also evaluated the effect of the jailbreaking attack PAIR (Chao et al., 2023) on a Llama-2-7b-chat model that had been subjected to the Q-Misalign attack at full precision. (Section 5.2)
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Llama Guard** (measurement instrument): *measured_by*, 1 paper
  > For LLM-based evaluation, we employ LlamaGuard (Inan et al., 2023) and GPT-4 (Souly et al., 2024) to assess whether the response is safe for the given instruction. (Section 5.1)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
- **SafeBench** (measurement instrument): *measured_by*, 1 paper
  > Our approach achieves higher attack success rates compared to existing multimodal attacks on SafeBench (Gong et al., 2023) and AdvBench (Zou et al., 2023). (Abstract)
  - [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf)
- **Llama Guard 2** (measurement instrument): *measured_by*, 1 paper
  > We use Llama Guard 2 as the auto-annotator to classify responses as jailbreak or non-jailbreak, following (Chao et al., 2024). (Section 3.3.4. ADVERSARIAL ROBUSTNESS EVALUATION)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
- **SALAD-Bench** (measurement instrument): *measured_by*, 1 paper
  > To assess the generalizability of the weak-to-strong attack, we expanded our evaluation to include two new safety benchmarks: SALAD-Bench (Li et al., 2024) and SORRY-Bench (Xie et al., 2024). (Section 5.1)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
- **SORRY-Bench** (measurement instrument): *measured_by*, 1 paper
  > To assess the generalizability of the weak-to-strong attack, we expanded our evaluation to include two new safety benchmarks: SALAD-Bench (Li et al., 2024) and SORRY-Bench (Xie et al., 2024). (Section 5.1)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
- **HarmBench classifier** (measurement instrument): *measured_by*, 1 paper
  > “we report the attack success rate (ASR) using HarmBench’s judge”
  - [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/geisler25a/geisler25a.pdf)

### → Jailbreaking
- **Adversarial robustness** (construct): *causes*, 1 paper
  > "LLMs are notably fragile and easily distracted by our complex role-play instructions, thereby enhancing the attack performance of each individual jailbreak character."
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)
- **Role-playing** (behavioral indicator): *causes*, 1 paper
  > Inspired by previous attempts that exploit role-playing to bypass the safety guardrails of LLMs (DAN, 2023; Li et al., 2024) and research on the distraction phenomenon in LLMs (Shi et al., 2023; Xiao et al., 2024), we apply sequential jailbreak characters within a single user query and ask the target LLMs to act as these characters sequentially to provide step-by-step instructions. (Section 2.1)
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)
- **Misalignment** (construct): *causes*, 1 paper
  > “these misalignments activate, rendering the model vulnerable to jailbreak attacks.”
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)

### Associated with
- **Alignment** (construct), 2 papers
  > One way to understand the limitations of these [alignment] methods is to explore their susceptibility to jailbreaking attacks; which are attempts to bypass the target LLM’s safety filters and circumvent its alignment [52].
  - [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf)
  - [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf)
- **Safety alignment** (construct), 2 papers
  > Although aligned with human preference data before release, LLMs remain vulnerable to various malicious attacks. In this paper, we adopt a red-teaming strategy to enhance LLM safety and introduce SEQAR, a simple yet effective framework to design jailbreak prompts automatically. (Section 1)
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)
  - [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf)
- **Adversarial suffix generation** (behavioral indicator), 1 paper
  > Jailbreaking attacks typically involve appending adversarial suffixes to instructions.
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
- **Attack transferability** (construct), 1 paper
  > We evaluate each suffix on all 50 behaviors (universality) including the one it is directly optimized for and on all five target models (transferability) including the one it is optimized on. (Section 3.1)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
