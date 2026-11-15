# Alignment
**Type:** Construct  
**Supporting papers:** 90  
**Also known as:** Alignment performance, Multimodal alignment  

## State of the Field

**Space of definitions.** Across papers, the prevailing framing treats alignment as a degree or latent property of model behavior or outputs matching human preferences, values, intentions, instructions, and ethical or safety constraints. This usage is often expressed through helpful, harmless, and truthful behavior, and some definitions add faithfulness to internal states, avoidance of inconsistent actions, or adherence to human-endorsed reasoning steps rather than outcome-only proxies. A smaller line narrows the term to post-finetuning output quality under the name "alignment performance," while another extends it to multimodal models as consistent and appropriate integration of visual and linguistic information across inputs and dialogue turns. The main disagreement is therefore over whether alignment is defined at the level of outputs, internal process, finetuning outcome, or multimodal interaction.

**Space of facets.** Papers most often organize alignment around human preference learning and instruction following. Several subtypes recur, including self-alignment, inference-time alignment, native or pre-training alignment, multimodal alignment, and multi-objective alignment, and one paper explicitly describes fine-tuning models to human values and preferences as "the alignment." A smaller strand separates process supervision from outcome-based supervision by rewarding an "aligned chain-of-thought," and another distinguishes superficial stylistic adjustments from deeper cognitive alignment.

**Space of measurement.** Operationally, papers link alignment to 9 measurement instruments and 9 behavioral indicators. The most common instruments are benchmark or dataset evaluations, especially AlpacaEval 2.0, Reddit TL;DR, HH-RLHF, and Arena-Hard, with 5 other linked instruments, while papers also link alignment to jailbreaking and 8 other behavioral indicators. These operationalizations mostly mirror definitions centered on human preferences, instruction adherence, and safety, and one multimodal paper adds an "alignment score" based on consistent performance under stylistically distinct but semantically equivalent questions.

**Links.** Most recurrent link claims say there is a causal relationship from Alignment to helpfulness, safety, and harmlessness, although some papers treat the helpfulness or safety links as related rather than causal. Several additional one-paper claims also record causal relationships from Alignment to other behaviors or properties, and a few papers instead claim causal relationships from other factors to Alignment. Alignment is also related to trustworthiness and jailbreaking, and papers do not report correlational claims.

## Sources

**Alignment** (17 papers: [#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf), [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf), [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf), [Evaluating Language Model Agency Through Negotiations](https://proceedings.iclr.cc/paper_files/paper/2024/file/03876dc6875571c18b3b09a624c77e96-Paper-Conference.pdf), [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf), [Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/48a4f41ff000b121eabe7b2491b24aef-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf), [Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/092359ce5cf60a80e882378944bf1be4-Paper-Conference.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf), [A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.552.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [A Survey of Post-Training Scaling in Large Language Models](https://aclanthology.org/2025.acl-long.140.pdf), [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf), [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf))
> The degree to which a model's behavior adheres to intended rules, instructions, and ethical constraints, including faithfulness to internal states and avoidance of harmful or inconsistent actions.

**Alignment performance** (1 paper: [Learning Dynamics of LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/afe1aa79e5eea7955f553c61a307273e-Paper-Conference.pdf))
> The overall quality of an LLM's outputs with respect to human-preferred behavior after finetuning.

**Multimodal alignment** (1 paper: [AlignMMBench: Evaluating Chinese Multimodal Alignment in Large Vision-Language Models](https://aclanthology.org/2025.acl-long.327.pdf))
> The latent ability of a vision-language model to consistently and appropriately integrate visual and linguistic information in a manner aligned with human expectations across diverse inputs and dialogue turns.

## Relationships

### Alignment →
- **Helpfulness** (construct): *causes*, 5 papers
  > Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. (ABSTRACT)
  - [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 4 papers
  > "POWER-DL consistently outperforms state-of-the-art methods in alignment benchmarks, achieving improvements of up to 13.0 points on AlpacaEval 2.0"
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)
- **Reddit TL;DR** (measurement instrument): *measured_by*, 4 papers
  > In the experiments, we simulate the soft preference labels with AI feedback from LLMs [4, 24] and show that soft preference labels and weighted geometric averaging achieve consistent improvement to the baselines on popular benchmarks for the alignment research literature, such as Reddit TL;DR [49]... (Section 1).
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [RLTHF: Targeted Human Feedback for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25c/xu25c.pdf)
- **HH-RLHF** (measurement instrument): *measured_by*, 3 papers
  > To evaluate the performance, we use the Anthropic HH-RLHF (Helpful and Harmless) dataset (Bai et al., 2022a), which is the most commonly used dataset for alignment. (Section 3.2)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
  - [RLTHF: Targeted Human Feedback for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25c/xu25c.pdf)
- **Safety** (construct): *causes*, 3 papers
  > “Alignment methods are designed to reduce such undesirable outputs”
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
  - [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf)
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 2 papers
  > We evaluate alignment effectiveness using three benchmarks: ... (2) Arena-Hard
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 2 papers
  > To evaluation the generalization capability of MEGALODON on instruction following and alignment, We finetune the base model... Table 3 summarizes the performance of chat models in 7B scale on MT-Bench4. (Section 4.4).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
- **Harmlessness** (construct): *causes*, 2 papers
  > Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. (ABSTRACT)
  - [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Truthfulness** (construct): *causes*, 1 paper
  > Reinforcement Learning from Human Feedback (RLHF) is a technique that can be used to align an agent — such as a Large Language Model (LLM) — to human preferences and lead to more truthful, more helpful, less harmful and more preferred outputs [29]. (Introduction)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **Training data regurgitation** (behavioral indicator): *causes*, 1 paper
  > Model alignment is a guardrail to prevent unwarranted behaviors, including “inadvertent memorization and [...] regurgitation in model outputs.” (Section 2)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > ...they still face reliability issues such as hallucinations, stemming from misalignment with human instructions... (Section 1)
  - [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf)
- **Harmful request refusal** (behavioral indicator): *causes*, 1 paper
  > Alignment involves calibrating these models... such that they adhere to human values and safely follow human intents. The resultant aligned LLMs should not engage with user requests on certain unsafe or inappropriate topics... Instead, they provide a refusal response (Section 1)
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)
- **MixEval** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate alignment effectiveness using three benchmarks: (1) MixEval ..."
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluate alignment effectiveness using three benchmarks: ... and (3) AdvBench
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > improves alignment performance of Zephyr-7B-SFT model by 8% (relative) on AlpacaEval, compared against training on vanilla DPO objective. (Abstract)
  - [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.452.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > Large language models (LLMs) require alignment to effectively and safely follow user instructions. (Abstract)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
- **Refusal** (behavioral indicator): *causes*, 1 paper
  > aligned LLMs readily refuse to answer many inappropriate prompts where the factual answer, e.g., could cause harm. (Section 1)
  - [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/geisler25a/geisler25a.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > Existing alignment or post-training strategies usually decrease the factuality of language models (Section 1).
  - [Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)

### → Alignment
- **Pairwise comparison** (behavioral indicator): *causes*, 1 paper
  > A key recipe to achieve alignment involves presenting pairs of responses and collecting binary feedback (e.g., preferred, less preferred) based on the comparative quality of these responses. (Section 1)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > As a result, developing interpretability methods for MLLMs is crucial for improving alignment quality and efficiency. (Abstract)
  - [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > we compare the plain BT model and BSR on RLHF training and empirically show that robust RMs better align the policy to the gold preference model. (Abstract).
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)

### Associated with
- **Jailbreaking** (behavioral indicator), 2 papers
  > One way to understand the limitations of these [alignment] methods is to explore their susceptibility to jailbreaking attacks; which are attempts to bypass the target LLM’s safety filters and circumvent its alignment [52].
  - [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf)
  - [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf)
- **Trustworthiness** (construct), 2 papers
  > identifying units whose outputs meet a user-specified alignment criterion... certifying their corresponding outputs as trustworthy.
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Instruction following ability** (construct), 1 paper
  > methods for effectively ‘aligning’ these models; i.e., steering them to follow user instructions effectively and safely, has garnered increasing attention.
  - [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf)
- **Reward hacking** (behavioral indicator), 1 paper
  > Aligning AI systems with human preferences typically suffers from the infamous reward hacking problem, where optimization of an imperfect reward model leads to undesired behaviors. (ABSTRACT)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > They did not investigate the more challenging task of language generation, which is closely tied to alignment and involves a significantly more complex output space. (Section 5)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Deception** (construct), 1 paper
  > Loosely speaking, alignment refers to the performance guarantee that the AI system will generate outcomes that are intended or preferred by the human user without undesirable side effects or behaviors such as deception (Park et al., 2023) or manipulation (Perez et al., 2022).
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Manipulation** (construct), 1 paper
  > Loosely speaking, alignment refers to the performance guarantee that the AI system will generate outcomes that are intended or preferred by the human user without undesirable side effects or behaviors such as deception (Park et al., 2023) or manipulation (Perez et al., 2022).
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Value orientation** (construct), 1 paper
  > To what degree are LLMs’ distributions of implicit values aligned with humans’ distributions? (Section 1)
  - [Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks](https://aclanthology.org/2025.emnlp-main.847.pdf)
- **PLLuM-Align** (measurement instrument), 1 paper
  > By introducing PLLuM-Align, a carefully designed Polish preference dataset explicitly built with alignment in mind, we provided a diverse and nuanced foundation for model training compared to traditional instruction-tuned datasets.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
