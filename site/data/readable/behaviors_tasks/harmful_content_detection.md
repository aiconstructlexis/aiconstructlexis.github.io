# Harmful content detection
**Type:** Behavioral indicator  
**Supporting papers:** 35  
**Also known as:** Harmful meme detection, Offensive language detection, Toxicity detection, Threat detection, Abusive language detection, Instruction classification, Unsafe content detection, Harmful prompt classification, Prompt Classification, Toxicity classification, Harmful prompt detection, Safety filtering, Harmful request discrimination, Unsafe intent identification, Problematic turn detection, Violent communication detection, Harmfulness detection, Risk identification, Offensive content detection, Toxic content detection, Risk detection, Prompt safety classification  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a classification task over text or prompts: models label inputs as harmful versus benign, safe, or unsafe, or as toxic, offensive, abusive, or threatening versus not. Success is usually a binary decision, sometimes with constrained outputs such as "OFF" or "NOT_OFF" and "1" or "0", and some papers explicitly use the result to reject or block unsafe prompts before generation. Smaller variants extend the same behavior to instruction-response pairs, multimodal memes or other multimodal inputs, conversational turns judged as problematic, or probability estimates of unsafety instead of a hard label.

**Variants.** Common variants focus on toxicity detection or classification, offensive language detection, and harmful prompt detection or prompt safety classification. Other papers narrow the target to threats or abusive language, distinguish instruction-only classification from instruction-response pair classification, or ask the model for an explicit harmful request, unsafe intent, or risk judgment, sometimes with finer-grained labels such as hate speech, offensive language, abuse, specific risk categories, sentence or token level labels, or even a 4-point problematic-turn score. The behavior is also studied in multilingual and multimodal settings, including Chinese and Sinhala text, audio or other cross-modality prompt detection, multimodal risk detection, and harmful meme detection from image-text pairs.

**Space of elicitation and scores.** Papers link this behavior to 15 measurement instruments overall. Among the named measures, it is most often measured by the OpenAI Moderation dataset, ToxicChat, and XSTest, followed by Hateful Memes and AdvBench, with 10 other instruments appearing less often. These measures are mostly public safety or moderation benchmarks for binary prompt or content classification, with additional meme datasets and attack-oriented or multilingual prompt sets.

**What it is taken as evidence of.** Papers link this behavior to five constructs, and the construct framing is mixed rather than uniform. One set of claims places it around safety: papers report it as related to Safety, and one paper claims a causal relationship from Harmful content detection to Safety awareness through improved identification of unsafe intent. Separate claims say Cultural knowledge and Natural language understanding have causal relationships to Harmful content detection, while Generalization is only related to it.

## Sources

**Harmful meme detection** (1 paper: [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf))
> The observable task of performing binary classification on a multimodal meme (image and text) to determine if it is harmful or benign.

**Offensive language detection** (3 papers: [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf), [Enhancing Chinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1154.pdf), [Sinhala Encoder-only Language Models and Evaluation](https://aclanthology.org/2025.acl-long.422.pdf))
> Classifying a text as offensive or not offensive based on its content.

**Toxicity detection** (4 papers: [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf), [Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/83d349b6eb8125588b5f091e2d47525c-Paper-Conference.pdf), [Adapting Bias Evaluation to Domain Contexts using Generative Models](https://aclanthology.org/2025.emnlp-main.1424.pdf), [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf))
> Classifying text as toxic or non-toxic.

**Threat detection** (1 paper: [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf))
> Classifying text as containing threats or not.

**Abusive language detection** (1 paper: [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf))
> Classifying text as abusive or non-abusive.

**Harmful content detection** (4 papers: [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf), [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf), [Gamma-Guard: Lightweight Residual Adapters for Robust Guardrails in Large Language Models](https://aclanthology.org/2025.emnlp-main.614.pdf), [Fine-Grained Transfer Learning for Harmful Content Detection through Label-Specific Soft Prompt Tuning](https://aclanthology.org/2025.naacl-long.551.pdf))
> The observable task of classifying a given input, such as an instruction or an instruction-response pair, as harmful or not.

**Instruction classification** (1 paper: [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf))
> A specific classification task where the model determines the harmfulness of a user instruction alone, with the response being an empty sequence.

**Unsafe content detection** (1 paper: [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf))
> The observable task of assigning a probability of being unsafe to a given text prompt, based on its adherence to safety policies.

**Harmful prompt classification** (1 paper: [Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/18699b47bb4abf5f92b0b73266b3ffc8-Paper-Conference.pdf))
> The task of identifying and categorizing input prompts as either harmful/malicious or benign/safe.

**Prompt Classification** (1 paper: [Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/18699b47bb4abf5f92b0b73266b3ffc8-Paper-Conference.pdf))
> The system assigning a label (harmful or benign) to an input prompt based on its geometric representation.

**Toxicity classification** (4 papers: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf), [Chinese Toxic Language Mitigation via Sentiment Polarity Consistent Rewrites](https://aclanthology.org/2025.emnlp-main.1808.pdf), [Soft-Label Integration for Robust Toxicity Classification](https://proceedings.neurips.cc/paper_files/paper/2024/file/ac4c13a5c6ec1bba68c9ce1d908321d2-Paper-Conference.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf))
> The task of classifying a given text prompt or response as either toxic/unsafe or non-toxic/safe.

**Safety filtering** (1 paper: [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf))
> Detecting and rejecting harmful or unsafe user prompts before they are processed by a generative model, implemented using encoder-based LLMs as classifiers.

**Harmful prompt detection** (3 papers: [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf), [MULTIGUARD: An Efficient Approach for AI Safety Moderation Across Languages and Modalities](https://aclanthology.org/2025.emnlp-main.819.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf))
> The task of identifying user prompts that are designed to elicit harmful or unsafe responses from a language model.

**Harmful request discrimination** (1 paper: [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf))
> The model's explicit judgment of whether a user input constitutes a harmful or dangerous request, typically expressed in structured safety assessments.

**Unsafe intent identification** (1 paper: [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf))
> The observable process of a model recognizing and articulating the potentially harmful or risky nature of a user's request.

**Problematic turn detection** (1 paper: [Words Like Knives: Backstory-Personalized Modeling and Detection of Violent Communication](https://aclanthology.org/2025.emnlp-main.586.pdf))
> Classifying whether a conversational turn is harmful or conflict-inducing based on linguistic and contextual cues.

**Harmfulness detection** (1 paper: [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf))
> Classifying a prompt as harmful or safe.

**Risk identification** (1 paper: [MCIP: Protecting MCP Safety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.62.pdf))
> The model's observable output when classifying whether a given interaction is safe or unsafe, or assigning it to a specific risk category.

**Offensive content detection** (1 paper: [V-VAE: A Variational Auto Encoding Framework Towards Fine-Grained Control over Human-Like Chat](https://aclanthology.org/2025.emnlp-main.1508.pdf))
> The task of identifying harmful, inappropriate, or offensive content in text.

**Toxic content detection** (1 paper: [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf))
> Identifying and filtering out biased, discriminatory, or violent material in generated dialogues using automated tools like Rewire API.

**Risk detection** (1 paper: [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf))
> The observable task of identifying and flagging whether a given multimodal input contains risky or harmful content.

**Prompt safety classification** (1 paper: [SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bw/li25bw.pdf))
> The task of categorizing a given user prompt as either safe or unsafe for an AI to respond to.

## Relationships

### Harmful content detection →
- **ToxicChat** (measurement instrument): *measured_by*, 3 papers
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
  - [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf)
- **XSTest** (measurement instrument): *measured_by*, 3 papers
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf)
- **OpenAI Moderation dataset** (measurement instrument): *measured_by*, 3 papers
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **Hateful Memes** (measurement instrument): *measured_by*, 2 papers
  > We use three publicly available meme datasets for evaluation: (1) HarM (Pramanick et al., 2021a), (2) FHM (Kiela et al., 2020), and (3) MAMI (Fersini et al., 2022). (Section 4.1)
  - [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://aclanthology.org/2025.acl-long.46.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 1 paper
  > (1) Harmfulness Detection (AdvBench): classify prompts as “harmful” or “safe” (Section 4.6)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
- **BeaverTails** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **SimpleSafetyTests** (measurement instrument): *measured_by*, 1 paper
  > To assess calibration in the context of binary prompt classification, we evaluate performance using a range of public benchmarks, including OpenAI Moderation (Markov et al., 2023), ToxicChat Test (Lin et al., 2023), Aegis Safety Test (Ghosh et al., 2024), SimpleSafetyTests (Vidgen et al., 2023), XSTest (R¨ottger et al., 2023), Harmbench Prompt (Mazeika et al., 2024) and WildGuardMix Test Prompt (Han et al., 2024).
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the safety guard models on four public benchmark datasets: OpenAI Moderation (OAI; Markov et al., 2023), ToxicChat (Lin et al., 2023), HarmBench (Mazeika et al., 2024), and the test split of WildGuardMix.
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **WildGuardMix** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the safety guard models on four public benchmark datasets: OpenAI Moderation (OAI; Markov et al., 2023), ToxicChat (Lin et al., 2023), HarmBench (Mazeika et al., 2024), and the test split of WildGuardMix.
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **HarM** (measurement instrument): *measured_by*, 1 paper
  > We use three publicly available meme datasets for evaluation: (1) HarM (Pramanick et al., 2021a), (2) FHM (Kiela et al., 2020), and (3) MAMI (Fersini et al., 2022). (Section 4.1)
  - [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://aclanthology.org/2025.acl-long.46.pdf)
- **MAMI** (measurement instrument): *measured_by*, 1 paper
  > We use three publicly available meme datasets for evaluation: (1) HarM (Pramanick et al., 2021a), (2) FHM (Kiela et al., 2020), and (3) MAMI (Fersini et al., 2022). (Section 4.1)
  - [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://aclanthology.org/2025.acl-long.46.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 1 paper
  > we evaluate general capability using MMLU... and toxicity detection using ToxiGen (Section 3).
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **GCG** (measurement instrument): *measured_by*, 1 paper
  > "For safety filtering, SMAAT accurately identified harmful prompts generated by GCG (Zou et al., 2023), achieving 97-100% accuracy."
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Safety awareness** (construct): *causes*, 1 paper
  > MLRMs paradoxically enhances safety performance via long reasoning on safety-awareness benchmarks, due to improved capability in identifying unsafe intent (Section 2.2).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **MultiJail** (measurement instrument): *measured_by*, 1 paper
  > Table 3 compares the accuracy of detecting harmful prompts for text benchmarks. Table 3(A) shows results for multilingual benchmarks, where OMNIGUARD ... achieves new state-of-the-art performance for 3 benchmarks: MultiJail, RTP-LX, and AyaRedTeaming.
  - [MULTIGUARD: An Efficient Approach for AI Safety Moderation Across Languages and Modalities](https://aclanthology.org/2025.emnlp-main.819.pdf)

### → Harmful content detection
- **Cultural knowledge** (construct): *causes*, 1 paper
  > introducing more comprehensive knowledge about Chinese culture are both crucial for effectively detecting harmful memes. (Section 5.4)
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Natural language understanding** (construct): *causes*, 1 paper
  > text comprehension plays a more crucial role than image understanding in the detection of harmful memes.
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Content moderation** (behavioral indicator), 1 paper
  > We evaluate on 7 content moderation tasks for 8 different cultures to detect the following content: hate speech, offensive language, spam speech, abusive speech, bias speech, threat speech, and stance of speech in zero-shot evaluation (Section 4.1)
  - [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf)
- **COLD** (measurement instrument), 1 paper
  > Recent datasets such as ToxiCN (Lu et al., 2023), COLD (Deng et al., 2022), Cdial-bias (Zhou et al., 2022), SWSR (Jiang et al., 2022), and SCCD (Yang et al., 2025b) support toxicity classification but do not provide sentiment-preserving rewrites. (Section 1)
  - [Chinese Toxic Language Mitigation via Sentiment Polarity Consistent Rewrites](https://aclanthology.org/2025.emnlp-main.1808.pdf)
- **Safety** (construct), 1 paper
  > Considering the potential harm that these memes may cause, this task can be used to evaluate the safety of LLMs. (Section 6)
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (construct), 1 paper
  > The increasing proliferation of harmful content and its evolving nature require effective and generalizable detection methods. (Section 1)
  - [Fine-Grained Transfer Learning for Harmful Content Detection through Label-Specific Soft Prompt Tuning](https://aclanthology.org/2025.naacl-long.551.pdf)
