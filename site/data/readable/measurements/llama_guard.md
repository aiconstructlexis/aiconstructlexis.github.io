# Llama Guard
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** LLaMA Guard 7B, LlamaGuard, Llama-Guard, LlamaGuard-7B  

## State of the Field

**What it is.** Across papers, Llama Guard is most commonly described as an LLM-based guard model or safety classifier that judges whether prompts or responses are harmful, unsafe, safe, or harmless. Definitions also refer to LLaMA Guard 7B or LlamaGuard-7B, described as a 7-billion parameter open-source guard model and a dedicated classifier for both prompt classification and response classification. A recurring description is as an evaluation tool that classifies responses so papers can compute Attack Success Rate, though some papers instead frame it as a pretrained text content moderation guardrail, an NSFW filter for user prompts, or a deployed safety mechanism on communication edges in multi-agent systems.

**What it is claimed to measure.** Papers link it to two constructs and two behavioral indicators. The construct claims are Harmlessness and Toxicity: papers use Llama-Guard to determine the safety of responses for harmlessness evaluation, and one paper uses it as the toxicity classifier for some models. The behavioral-indicator claims are Harmful content generation, measured through ASR, and Jailbreaking, assessed by judging whether a response is safe for the given instruction.

**Space of uses.** No measurement instrument is linked to it. In use, papers position it mainly as a judgment model for safety evaluation, sometimes alongside GPT-4 or ShieldGemma, and also as one of several open-source guard models. Other papers use it more operationally, for example to classify all prompts and responses, to filter NSFW user prompts, or as a baseline or existing safety mechanism in agent and multi-agent settings.

**Concerns raised.** Some papers raise applicability and robustness concerns. One paper says LlamaGuard is designed to detect harmful content in LLM inputs and outputs and 'is not aligned with the safety guard requests for agents'; another evaluates bypass rate as cases where a malicious request is classified as safe. A further paper reports that existing safety mechanisms including Llama-Guard 'fail to defend against our attack'.

## Sources

**Llama Guard** (3 papers: [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [GenAI Arena: An Open Evaluation Platform for Generative Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/92249f9233286e437f808fa535d88b26-Paper-Datasets_and_Benchmarks_Track.pdf), [Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks](https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf))
> An evaluation tool used to classify model responses and calculate the Attack Success Rate (ASR) by determining if an output is harmful.

**LLaMA Guard 7B** (1 paper: [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf))
> A 7-billion parameter open-source guard model used as an instrument to evaluate the effectiveness of jailbreak attacks at bypassing safety filters.

**LlamaGuard** (2 papers: [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiang25a/xiang25a.pdf), [Adversarial Tokenization](https://aclanthology.org/2025.acl-long.1012.pdf))
> Pretrained LLM-based guardrail system designed for content moderation in text, used here as a baseline to test its applicability to agent safety tasks.

**Llama-Guard** (2 papers: [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf), [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf))
> A model-based evaluation tool used to classify the safety and harmlessness of LLM-generated responses.

**LlamaGuard-7B** (1 paper: [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://proceedings.neurips.cc/paper_files/paper/2024/file/de7b99107c53e60257c727dc73daf1d1-Paper-Datasets_and_Benchmarks_Track.pdf))
> An LLM-based safety classifier used to judge whether prompts or responses are unsafe.

## Relationships

### → Llama Guard
- **Harmlessness** (construct): *measured_by*, 2 papers
  > For harmlessness evaluation, we ... used Llama-Guard (Inan et al., 2023) to determine the safety of the responses...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 1 paper
  > For LLM-based evaluation, we employ LlamaGuard (Inan et al., 2023) and GPT-4 (Souly et al., 2024) to assess whether the response is safe for the given instruction. (Section 5.1)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
- **Toxicity** (construct): *measured_by*, 1 paper
  > To measure effectiveness of each method, we compute the toxicity rate which is the percentage of generated prompts that are toxic. We consider a prompt toxic if the toxicity classifier $p_\psi$ assigns a score greater than 0.5 to an input pair consisting of the prompt x and response y generated by the target LLM. For $p_\psi$, we use a RoBERTa hate speech classifier (Vidgen et al., 2021) for GPT-2 and dolly-v2-7b, and Llama-Guard (Inan et al., 2023) for Llama-2-7b-chat, Llama-3.1-8B-Instruct, and Gemma-2b-it.
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the VLM output harmfulness, we use the Attack Success Rate (ASR) metric via Llama Guard (Inan et al., 2023), following prior works (Zou et al., 2023; Shayegani et al., 2024; Luo et al., 2024). (Section 4.1)
  - [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf)
