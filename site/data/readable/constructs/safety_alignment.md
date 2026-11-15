# Safety alignment
**Type:** Construct  
**Supporting papers:** 100  
**Also known as:** Safety policy compliance, Safety control  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats safety alignment as the degree to which a model's behavior conforms to safety guidelines, human values, ethical principles, or usage policies, mainly by avoiding harmful or undesirable outputs. Many definitions also cast it as a latent property of the model, sometimes specifically the ability to refrain from harmful content or to recognize and refuse unsafe queries. A smaller line of work narrows the concept to explicit safety policy compliance or safety control for agents' action trajectories, while one paper frames it as consistency between internal processing and safety training objectives, visible in stable gradient patterns. Some definitions further fold in maintaining utility, helpfulness, or balanced compliance on benign instructions, whereas others focus only on preventing harm.

**Space of facets.** Papers use several nearby names for overlapping ideas: safety alignment, safety policy compliance, and safety control all center on adherence to safety policies, but the latter two are defined in agent settings with explicit external rules. Several definitions explicitly situate it within AI alignment more broadly, as adherence to human intentions and values. The concept is also specialized across settings, including text LLMs, multimodal and audio models, vision-language models, and web agents, and some work localizes it to internal components such as image encoder layers, representation spaces, or safety-trained gradients. A recurring contrast is between aligned refusal of unsafe instructions and unwanted overrefusal or oversafety on benign instructions, with some papers defining successful alignment as balancing harmlessness with helpfulness or benign compliance.

**Space of measurement.** Operationally, papers link safety alignment to 12 measurement instruments and 6 behavioral indicators. AdvBench is the most common benchmark, often used as a harmful-behavior or jailbreak-rate evaluation; HEx-PHI and HH-RLHF also recur, and other work uses AIAH and CipherChat. These operationalizations are mostly benchmark-based tests of harmful question answering, harmfulness-inducing instructions, or generalization to non-natural language prompts, and one measure assigns harmfulness scores to model responses; alongside them, papers operationalize the construct through harmful content generation, refusal of harmful requests, refusal behavior, overrefusal, and safe response generation. This mostly matches the dominant output-behavior definition, though one paper instead characterizes alignment through stable versus sharp gradient patterns under benign and harmful prompts.

**Links.** Several papers claim a causal relationship from safety alignment to harmful content generation, typically by describing compromised or insufficient alignment as leading to harmful responses. Several papers also claim a causal relationship from safety alignment to overrefusal, often when alignment is described as enhanced, over-conservative, or thresholded too strictly; other papers describe it as producing refusal of unsafe prompts, safe responses, and harmless or helpful behavior. Related links connect it to jailbreaking and to broader capability or robustness discussions. In the opposite direction, one paper claims a causal relationship from compositional generalization to safety alignment and another from logical reasoning to safety alignment. The papers do not report correlation claims.

## Sources

**Safety alignment** (15 papers: [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf), [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf), [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf), [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf), [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://proceedings.neurips.cc/paper_files/paper/2024/file/de7b99107c53e60257c727dc73daf1d1-Paper-Datasets_and_Benchmarks_Track.pdf), [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://aclanthology.org/2025.naacl-long.470.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf), [Jailbreak Large Vision-Language Models Through Multi-Modal Linkage](https://aclanthology.org/2025.acl-long.74.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [Persuasion Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD](https://aclanthology.org/2025.emnlp-main.81.pdf))
> The degree to which a model's behavior conforms to safety guidelines, preventing it from generating harmful or undesirable outputs.

**Safety policy compliance** (1 paper: [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf))
> The latent ability of an agent to adhere to explicit safety rules derived from regulatory or organizational policies across dynamic action sequences.

**Safety control** (1 paper: [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiang25a/xiang25a.pdf))
> The latent property of a system to ensure its actions align with predefined safety policies and do not lead to harmful outcomes.

## Relationships

### Safety alignment →
- **Harmful content generation** (behavioral indicator): *causes*, 7 papers
  > “Safety alignment is essential to prevent unintended model behaviors and mitigate risks in downstream applications.”
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/45673dbf3f331fbd911b0689872de396-Paper-Conference.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 6 papers
  > we test safety on the “harmful behaviors” subset of the AdvBench benchmark curated by Zou et al. [2023] (Section 2)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf)
- **Overrefusal** (behavioral indicator): *causes*, 6 papers
  > Safety alignment is crucial for Large Language Models (LLMs) to resist malicious instructions but often results in over-refusals, where benign prompts are unnecessarily rejected, impairing user experience and model utility. (Abstract)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.485.pdf)
  - [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf)
- **Harmlessness** (construct): *causes*, 4 papers
  > Specifically, harmless is achieved by safety alignment that empowers the LLM with safety guardrails so that the model can refuse harmful instructions.
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Helpfulness** (construct): *causes*, 4 papers
  > Via this channel, an LLM learns how to react to human instruction in a harmless and helpful way, as demonstrated in the alignment dataset. (Section 1)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **HEx-PHI** (measurement instrument): *measured_by*, 2 papers
  > “To assess the harmfulness of the compromised LLMs, we select the Policy-Oriented Safety Evaluation Benchmarks”
  - [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf)
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **HH-RLHF** (measurement instrument): *measured_by*, 2 papers
  > To further evaluate the effectiveness of SimPER in safety alignment on Pythia-2.8B following (Rafailov et al., 2024), we use the Anthropic-HH dataset.
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Refusal** (behavioral indicator): *causes*, 2 papers
  > In response, researchers have developed several methods to enhance LLM safety, known as safety alignment, including supervised fine-tuning (SFT) (Ouyang et al., 2022) and reinforcement learning from human feedback (RLHF) (Bai et al., 2022; Dai et al., 2024). As a result of these advancements, pre-trained LLMs like GPT-4 (OpenAI, 2023) and Llama (Touvron et al., 2023b) have become more adept at rejecting unsafe prompts.
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
  - [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf)
- **Harmful request refusal** (behavioral indicator): *causes*, 2 papers
  > During this alignment stage, LLMs learn to reject harmful queries, ensuring their behavior remains well within a defined safety scope. (Section 3.1)
  - [Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25c/guan25c.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **FigStep** (measurement instrument): *measured_by*, 1 paper
  > we conduct experiments on FigStep (Gong et al., 2023), VL-Guard (Zong et al., 2024), MOSSBench (Li et al., 2024d) and SIUO (Wang et al., 2024c) to evaluate the safe alignment of our approach. (Section 5.1)
  - [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf)
- **CipherChat** (measurement instrument): *measured_by*, 1 paper
  > We propose a novel framework CipherChat to systematically examine the generalizability of safety alignment to non-natural languages – ciphers. (ABSTRACT)
  - [GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf)
- **Safe response generation** (behavioral indicator): *causes*, 1 paper
  > A perfectly aligned LLM is expected to generate harmless response given a harmful instruction x
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
- **Llama Guard 3** (measurement instrument): *measured_by*, 1 paper
  > “Then evaluate the harmfulness score on its responses with the Llama-Guard-3-8B (Llama Team, 2024).”
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **VLGuard** (measurement instrument): *measured_by*, 1 paper
  > we conduct experiments on FigStep (Gong et al., 2023), VL-Guard (Zong et al., 2024), MOSSBench (Li et al., 2024d) and SIUO (Wang et al., 2024c) to evaluate the safe alignment of our approach. (Section 5.1)
  - [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf)
- **SIUO** (measurement instrument): *measured_by*, 1 paper
  > we conduct experiments on FigStep (Gong et al., 2023), VL-Guard (Zong et al., 2024), MOSSBench (Li et al., 2024d) and SIUO (Wang et al., 2024c) to evaluate the safe alignment of our approach. (Section 5.1)
  - [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf)
- **AIAH** (measurement instrument): *measured_by*, 1 paper
  > We adopt AIAH (Yang et al., 2025) as the benchmark to evaluate the safety-alignment of LALMs to harmful questions
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **Ti-SafetyBench** (measurement instrument): *measured_by*, 1 paper
  > TLUE consists of 22,963 evaluation questions, divided into Ti-MMLU for knowledge assessment and Ti-SafetyBench for safety evaluation. (Section 3.2)
  - [TLUE: A Tibetan Language Understanding Evaluation Benchmark](https://aclanthology.org/2025.emnlp-main.1777.pdf)

### → Safety alignment
- **Compositional generalization** (construct): *causes*, 1 paper
  > The success of PTST suggests that LLMs have certain abilities of compositional generalization, which enable them to generalize from one template to another while being aware of safety constraints in the new template.
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Logical reasoning** (construct): *causes*, 1 paper
  > To tackle these challenges, we propose SHIELDAGENT, the first guardrail agent designed to enforce explicit safety policy compliance for the action trajectory of other protected agents through logical reasoning. (Section 1)
  - [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf)

### Associated with
- **Jailbreaking** (behavioral indicator), 2 papers
  > Although aligned with human preference data before release, LLMs remain vulnerable to various malicious attacks. In this paper, we adopt a red-teaming strategy to enhance LLM safety and introduce SEQAR, a simple yet effective framework to design jailbreak prompts automatically. (Section 1)
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)
  - [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf)
- **General ability** (construct), 1 paper
  > The shape of the LLM capability landscape is drastically different from the one in the LLM safety landscape; these landscapes do not exhibit the same trend, further confirming that the basin shape is indeed unique to the safety of LLM.
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **Adversarial robustness** (construct), 1 paper
  > larger models are more susceptible to multimodal attacks, revealing the lack of safety alignment in the additional modalities. (Section 4.2, Finding A3)
  - [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf)
- **Visual reasoning** (construct), 1 paper
  > This observation highlights a fundamental trade-off: as visual reasoning capabilities increase, safety alignment tends to degrade. (Section 1)
  - [VisCRA: A Visual Chain Reasoning Attack for Jailbreaking Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.312.pdf)
- **BeaverTails** (measurement instrument), 1 paper
  > “For the alignment task, we use the safe samples from the alignment dataset of BeaverTails (Ji et al., 2023).”
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **PKU-SafeRLHF** (measurement instrument), 1 paper
  > Using the large-scale annotation data, we further train severity-sensitive moderation for the risk control of LLMs and safety-centric RLHF algorithms for the safety alignment of LLMs. (Abstract)
  - [PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference](https://aclanthology.org/2025.acl-long.1544.pdf)
