# Toxicity
**Type:** Construct  
**Supporting papers:** 51  
**Also known as:** Non-toxicity, Anti-toxicity  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats toxicity as a latent tendency, risk, or propensity of a model or its outputs to contain harmful, offensive, inappropriate, rude, disrespectful, or otherwise undesirable language. Many definitions stay at this broad level, while some narrow the content to hostility and aggression in community discourse, or to forms such as hate speech, violent speech, abusive language, threats, profanity, sexually explicit language, and stereotype-perpetuating text. A smaller line of work uses the opposing labels non-toxicity or anti-toxicity for avoidance or suppression of harmful content, and one paper uses the term differently for poisoned data samples that are easy to retrieve and induce incorrect responses.

**Space of facets.** Where papers systematize the construct, they usually break it into subtypes of harmful language. One recurring breakdown includes toxic, severe toxic, obscene, threat, insult, and identity hate, while other papers describe the space with hate speech, violent speech, abusive language, hostility, aggression, or sexual content, and one paper reports sexual content as the most prevalent type among toxic user turns. Related naming is not uniform: some authors use non-toxicity or anti-toxicity for the opposing trait, and papers place toxicity as one component of safety and trustworthiness, while one paper contrasts it with stereotyping inside social bias.

**Space of measurement.** Operationally, papers link toxicity to 12 measurement instruments and 1 behavioral indicator. The most common instruments are Perspective API, RealToxicityPrompts, Detoxify, ToxiGen, and LLM-as-a-judge, with 7 other instruments also used; the dominant setup is to elicit continuations with prompt sets such as RealToxicityPrompts or ToxiGen and score them with automated detectors or judges. Papers report outputs such as a toxicity probability, mean toxicity, toxicity rate, or expected maximum toxicity, and one mechanistic study also uses linear probes to classify toxic versus non-toxic inputs, so measurement usually targets toxic generations directly, though some papers assess identification and avoidance of offensive material or reflection of hostility and aggression in community discourse.

**Links.** Beyond measurement, papers link toxicity to 4 constructs and 1 behavioral indicator. One paper claims a causal relationship from self-correction to toxicity, reporting that CRITIC lowers the occurrence of toxic generations. Toxicity is also related to safety in several papers, to trustworthiness as one component in a broader framework, to social bias as one of two harms alongside stereotyping, and to political bias, where one paper cites a suggested link through hate speech predictions.

## Sources

**Toxicity** (9 papers: [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Improving and Assessing the Fidelity of Large Language Models Alignment to Online Communities](https://aclanthology.org/2025.naacl-long.5.pdf), [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf), [AID: Adaptive Integration of Detectors for Safe AI with Language Models](https://aclanthology.org/2025.naacl-long.229.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [Ethical Concern Identification in NLP: A Corpus of ACL Anthology Ethics Statements](https://aclanthology.org/2025.naacl-long.580.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [Conformal Tail Risk Control for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bd/chen25bd.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf))
> The latent property or risk of a model generating harmful, offensive, or inappropriate content.

**Non-toxicity** (1 paper: [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf))
> The latent trait of a language model to avoid generating harmful or offensive content, especially in response to malicious or provocative prompts.

**Anti-toxicity** (1 paper: [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf))
> The latent tendency of a language model to suppress or counteract toxic content generation, manifested through increased activation of neural components geometrically opposed to toxic representations.

## Relationships

### Toxicity →
- **Perspective API** (measurement instrument): *measured_by*, 14 papers
  > Our evaluation mechanism employs the Perspective API2, which classifies text based on six delineated toxicity attributes. (Section 5.1)
  - [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf)
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
  - [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)
  - [Controllable Generation via Locally Constrained Resampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/d98ce7a82af78cd02968e79ea3fe89e8-Paper-Conference.pdf)
  - [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
  - [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf)
- **RealToxicityPrompts** (measurement instrument): *measured_by*, 11 papers
  > We then prompt all models with “I don’t care if this is controversial” and a prompt from RealToxicityPrompts (Gehman et al., 2020).
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
  - [Controllable Generation via Locally Constrained Resampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/d98ce7a82af78cd02968e79ea3fe89e8-Paper-Conference.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
  - [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf)
- **Detoxify** (measurement instrument): *measured_by*, 10 papers
  > We detect unsafe content using two toxicity classification tools: the OpenAI Moderation API and Detoxify (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
  - [Improving and Assessing the Fidelity of Large Language Models Alignment to Online Communities](https://aclanthology.org/2025.naacl-long.5.pdf)
  - [Conformal Tail Risk Control for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bd/chen25bd.pdf)
  - [Metadata Conditioning Accelerates Language Model Pre-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25p/gao25p.pdf)
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
  - [Who Holds the Pen? Caricature and Perspective in LLM Retellings of History](https://aclanthology.org/2025.emnlp-main.996.pdf)
  - [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 5 papers
  > We rely on ToxiGen [13] for assessing the model’s toxicity.
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **OpenAI Moderation API** (measurement instrument): *measured_by*, 2 papers
  > We detect unsafe content using two toxicity classification tools: the OpenAI Moderation API and Detoxify (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > We evaluate Toxicity and Hallucination using GPT-4o OpenAI (2023) and Claude-3.5-Sonnet Anthropic (2023) through an LLM-as-a-judge approach, as shown in Table 4 and Table 5. (Section 4.7)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the Spectra suite across various safety and toxicity benchmarks of TruthfulQA (Lin et al., 2021), Big Bench BBQ Lite (Parrish et al., 2022) and CrowsPairs (Nangia et al., 2020). (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **BBQ Lite** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the Spectra suite across various safety and toxicity benchmarks of TruthfulQA (Lin et al., 2021), Big Bench BBQ Lite (Parrish et al., 2022) and CrowsPairs (Nangia et al., 2020). (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **CrowS-Pairs** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the Spectra suite across various safety and toxicity benchmarks of TruthfulQA (Lin et al., 2021), Big Bench BBQ Lite (Parrish et al., 2022) and CrowsPairs (Nangia et al., 2020). (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Llama Guard** (measurement instrument): *measured_by*, 1 paper
  > To measure effectiveness of each method, we compute the toxicity rate which is the percentage of generated prompts that are toxic. We consider a prompt toxic if the toxicity classifier $p_\psi$ assigns a score greater than 0.5 to an input pair consisting of the prompt x and response y generated by the target LLM. For $p_\psi$, we use a RoBERTa hate speech classifier (Vidgen et al., 2021) for GPT-2 and dolly-v2-7b, and Llama-Guard (Inan et al., 2023) for Llama-2-7b-chat, Llama-3.1-8B-Instruct, and Gemma-2b-it.
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **ParaDetox** (measurement instrument): *measured_by*, 1 paper
  > "we use the ParaDetox dataset (Logacheva et al., 2022) containing pairwise “non-toxic” and “toxic” sentences"
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
- **ALERT** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the toxicity of the model using the ALERT (Tedeschi et al., 2024) benchmark... (Section 5.4)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)

### → Toxicity
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > The results in Table 3 demonstrate that 1) CRITIC substantially lowers the occurrence of toxic generations, while preserving fluency and diversity as the vanilla LLMs. (Section 4.3 Results)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)

### Associated with
- **Safety** (construct), 2 papers
  > Two most significant topics in the literature of large model safety [124, 132] are the toxicity of AI-generated content [47], which could greatly impact user interactions, and model jailbreaking (Sec. 2.2.2)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Social bias** (construct), 1 paper
  > Our categorization of social bias types in LLMs is structured around two distinct types of harms: Stereotyping and Toxicity.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Political bias** (construct), 1 paper
  > Feng et al. (2023) observed that politically biased language models tend to “propagate social biases into hate speech predictions,” suggesting a link between political bias and toxicity. (Section 3.6)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
- **Trustworthiness** (construct), 1 paper
  > These components [truthfulness, toxicity, fairness, robustness, privacy, and machine ethics] collectively contribute to a comprehensive framework for assessing and improving LLM trustworthiness. (Section 2)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
