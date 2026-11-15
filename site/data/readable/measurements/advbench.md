# AdvBench
**Type:** Measurement instrument  
**Supporting papers:** 120  
**Also known as:** Advbench, ADVBENCH  

## State of the Field

**What it is.** Most papers treat AdvBench as an adversarial or jailbreak benchmark built from harmful instructions, prompts, queries, questions, or behaviors that are used to test whether models will produce harmful responses. The prevailing framing is a text benchmark of harmful requests, though some definitions describe separate "Harmful Behaviors" and "Harmful Strings" components, and multimodal work reuses or refines it for vision-language or audio attack settings. Definitions also differ on exact scope, with some papers describing the full dataset and others focusing on curated or refined subsets.

**What it is claimed to measure.** Papers use AdvBench to measure 6 constructs and 6 behavioral indicators. The dominant measurement claims center on safety and safety alignment, and on the behavioral side on jailbreaking, harmful content generation, and harmful request refusal; the remaining links cover 4 other constructs and 3 other indicators. Authors operationalize these uses through attack or jailbreak rates, refusal-based metrics, unsafety detection, and harmfulness scoring.

**Space of uses.** Papers do not link it to other measurement instruments, but they often deploy it alongside HarmBench, MaliciousInstruct, HEx-PHI, JailbreakBench, and SafeBench, with several other benchmarks also appearing. It is usually positioned as a commonly or widely used jailbreak, safety, or harmful-query benchmark, and some papers use it as an out-of-domain test set, to generate adversarial prompts, or in refined and held-out subsets for defense and multimodal evaluations.

## Sources

**AdvBench** (14 papers: [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf), [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf), [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://aclanthology.org/2025.naacl-long.470.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf), [Iterative Self-Tuning LLMs for Enhanced Jailbreaking Capabilities](https://aclanthology.org/2025.naacl-long.297.pdf), [Root Defense Strategies: Ensuring Safety of LLM at the Decoding Level](https://aclanthology.org/2025.acl-long.97.pdf), [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf))
> A benchmark dataset comprising 500 instances of harmful behaviors expressed as specific instructions, used to evaluate model jailbreak vulnerabilities.

**Advbench** (3 papers: [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf), [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf))
> A dataset containing malicious prompts designed to test the alignment and safety of LLMs by attempting to induce harmful responses.

**ADVBENCH** (1 paper: [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf))
> A benchmark dataset containing 50 harmful behaviors used to evaluate the effectiveness of jailbreak attacks on LLMs.

## Relationships

### → AdvBench
- **Jailbreaking** (behavioral indicator): *measured_by*, 11 papers
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
- **Safety alignment** (construct): *measured_by*, 6 papers
  > we test safety on the “harmful behaviors” subset of the AdvBench benchmark curated by Zou et al. [2023] (Section 2)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf)
- **Safety** (construct): *measured_by*, 6 papers
  > Also, we wonder if weakening model’s exaggerated safety will also lead to a drop in its overall safety, hence we conducted another experiment on AdvBench (Zou et al. [2023b]), which contains 500 harmful instructions. (Section 4.2)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
  - [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **Harmlessness** (construct): *measured_by*, 4 papers
  > "we red-team LLaMA2-7B-chat using three attack levels and evaluated on Advbench [10]."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 3 papers
  > For our prompts, we sample 100 instructions from AdvBench (Zou et al., 2023). We say that the model output reflects the ANSWER task if it attempts to answer the question... (Section 4.3)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
  - [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
- **Adversarial robustness** (construct): *measured_by*, 3 papers
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
  - [AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf)
- **Safety robustness** (construct): *measured_by*, 2 papers
  > We performed experiments on the Advbench dataset [70] which is one of the most prevailing benchmark datasets to measure the security of LLMs. (Section 4)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 2 papers
  > Results in Table 5 show that TAIA significantly reduces the attack success rate after tuning on three levels of red-teaming data... evaluated on Advbench [10].
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Harmful request refusal** (behavioral indicator): *measured_by*, 2 papers
  > “we evaluate on the first 80 prompts of AdvBench [51] ‘Harmful Behaviors’ split (Adv 80) with ASR as the safety metric.”
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 1 paper
  > (1) Harmfulness Detection (AdvBench): classify prompts as “harmful” or “safe” (Section 4.6)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
- **Alignment** (construct): *measured_by*, 1 paper
  > We evaluate alignment effectiveness using three benchmarks: ... and (3) AdvBench
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **Refusal** (behavioral indicator): *measured_by*, 1 paper
  > on a set of 520 high-risk queries from AdvBench (Zou et al., 2023), all 9 LRMs models... consistently exhibited a significant drop in overall refusal rate under first-person prompting (Section 3.1)
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.990.pdf)
