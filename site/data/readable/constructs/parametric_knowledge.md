# Parametric knowledge
**Type:** Construct  
**Supporting papers:** 22  
**Also known as:** Multi-task knowledge, Model knowledge, Internal knowledge, Implicit knowledge, Latent knowledge, Parametric memory, Prior knowledge, Task knowledge  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats parametric knowledge as knowledge stored in a model's parameters, usually acquired during pre-training and available without external retrieval or prompt-supplied information. Many papers present it under closely related labels such as internal, implicit, latent, or model knowledge, and several describe it as what a model falls back on when retrieval is misleading or absent. The main variation is scope: some definitions mean broad factual or world knowledge, while a smaller line of work narrows it to task, language, or domain-specific priors. Another variation concerns expression, with one paper defining latent knowledge as information learned in the parameters that may not be fully expressed in the final output layer.

**Space of facets.** Across papers, several labels are used for closely related ideas, especially parametric memory, prior knowledge, internal knowledge, and model knowledge, with narrower variants such as task or multi-task knowledge. The most common organizing contrast is between knowledge in parameters and non-parametric or contextual information from retrieval, source documents, demonstrations, or the immediate input. Some papers further single out facets such as commonsense, factual, professional or domain-specific, and language-specific knowledge, while a few extend the notion to knowledge and rules used for implicit reasoning, describe elicited parametric memory as the model's internal belief, or localize storage to FFN modules.

**Space of measurement.** It is linked to 1 measurement instrument, MMLU, and 1 behavioral indicator, knowledge-based question answering. MMLU is a benchmark and is described as assessing parametric or multi-task knowledge, with one paper adding that it primarily assesses parametric knowledge and requires minimal reasoning; the linked behavioral indicator is described as evaluating the model's internal knowledge retained by base large language models. Beyond this named benchmark, several papers operationalize the construct by withholding external information, for example testing without retrieval or source documents, using closed-book question answering, or enciphering inputs to quantify prior knowledge, and one paper analyzes early-layer versus final-layer logits to access latent knowledge that may not appear in standard outputs.

**Links.** It is linked to 3 constructs. One paper claims a causal relationship from parametric knowledge to factuality, stating that latent knowledge can guide self-refinement of outputs and improve factual accuracy, and another claims a causal relationship from parametric knowledge to weak-to-strong generalization by eliciting latent knowledge from pre-trained LLMs. One paper relates knowledge transfer to parametric knowledge, stressing transferability across model scales, and another relates knowledge-based question answering to parametric knowledge as an evaluation of internal knowledge; no correlational link is reported.

## Sources

**Parametric knowledge** (4 papers: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf), [When Long Helps Short: How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models](https://aclanthology.org/2025.emnlp-main.522.pdf))
> The knowledge implicitly stored within the parameters of a language model, as opposed to knowledge accessed from an external source.

**Prior knowledge** (2 papers: [Aggregation Artifacts in Subjective Tasks Collapse Large Language Models' Posteriors](https://aclanthology.org/2025.naacl-long.284.pdf), [Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu](https://aclanthology.org/2025.acl-long.429.pdf))
> The general knowledge and task-related understanding acquired by a model during its pre-training phase, which influences its predictions independently of in-context examples.

**Multi-task knowledge** (1 paper: [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf))
> The latent breadth of factual and domain knowledge that supports performance across many subject areas.

**Model knowledge** (1 paper: [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf))
> The latent store of factual world knowledge encoded in a model during pre-training and potentially altered during fine-tuning, which supports accurate responses in closed-book settings.

**Internal knowledge** (1 paper: [NILE: Internal Consistency Alignment in Large Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf))
> The knowledge acquired by a large language model during its pre-training phase, which is embedded within its parameters.

**Implicit knowledge** (1 paper: [HLM-Cite: Hybrid Language Model Workflow for Text-based Scientific Citation Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/5635925cf9d2274f338eb0dd5971e845-Paper-Conference.pdf))
> The latent professional or domain-specific knowledge encoded within a model's parameters that is not explicitly provided in the input context.

**Latent knowledge** (1 paper: [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf))
> The factual information implicitly learned and stored within the model's internal parameters during training, which may not be fully expressed in the final output layer.

**Parametric memory** (3 papers: [Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf), [Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://proceedings.iclr.cc/paper_files/paper/2024/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf), [Grokking of Implicit Reasoning in Transformers: A Mechanistic Journey to the Edge of Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad217e0c7fecc71bdf48660ad6714b07-Paper-Conference.pdf))
> The knowledge stored implicitly within the learned parameters of a language model, as opposed to knowledge accessed from an external source.

**Task knowledge** (1 paper: [Prompt Optimization with EASE? Efficient Ordering-aware Automated Selection of Exemplars](https://proceedings.neurips.cc/paper_files/paper/2024/file/dd8e7dae18cecd7c9137840161e1bf62-Paper-Conference.pdf))
> The amount of prior task-specific knowledge the model already has before receiving in-context exemplars.

## Relationships

### Parametric knowledge →
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > MMLU primarily assesses a model’s parametric knowledge and requires minimal reasoning, thus offering limited benefits from CoT reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > our SLED framework leverages the latent knowledge embedded within the LLM by contrasting the output logits from the final layer with those from early layers. It then utilizes an approximate gradient approach to enable latent knowledge to guide the self-refinement of outputs, thereby effectively improving factual accuracy. (Abstract)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **Weak-to-strong generalization** (construct): *causes*, 1 paper
  > We prove that weak-to-strong generalization is possible by eliciting latent knowledge from pre-trained LLMs.
  - [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf)

### Associated with
- **Knowledge transfer** (construct), 1 paper
  > Our findings highlight the critical factors contributing to the process of parametric knowledge transfer, underscoring the transferability of model parameters across LLMs of different scales. (Section 1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Knowledge-based question answering** (behavioral indicator), 1 paper
  > Knowledge-based Question Answering (KG): This type of question evaluates the model’s internal knowledge, which is retained by the base large language models (Section 2.2).
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
