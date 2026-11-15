# Perspective API
**Type:** Measurement instrument  
**Supporting papers:** 40  
**Also known as:** PERSPECTIVE API, PerspectiveAPI, Perspective toxicity model  

## State of the Field

**What it is.** Across papers, the prevailing description is an external API or automated tool for toxicity assessment, used to score text for harmful language. Most definitions describe an overall toxicity score, often on a 0 to 1 scale, plus finer-grained attribute scores such as severe toxicity, threat, profanity, insult, and identity attack. The granularity varies across papers: some refer to six toxicity attributes, some select five aspects for safety evaluation, and one paper uses eight attributes including sexually explicit and flirtation. A smaller line of work describes it as a moderation tool, or as a benchmark or model for toxic detection.

**What it is claimed to measure.** Papers link it to two constructs and one behavioral indicator. The dominant use is to measure Toxicity, with papers describing it as toxicity evaluation, toxic language and hate speech detection, or a toxicity behavior function for model generations. More narrowly, some papers use Perspective API metrics such as Expected Maximum Toxicity and Toxicity Probability to measure Harmlessness, and several papers report it as measuring Harmful content generation or the harmfulness of responses. Overall, these claims are concentrated on toxicity rather than spread across many constructs.

**Space of uses.** In use, papers most often position it as an automatic evaluation instrument for generated replies, stories, questions, or vision-language model responses, and some also use it for dataset filtering, data augmentation, or quality assessment. It is linked to two other instruments, Human evaluation and RealToxicityPrompts, and one paper additionally samples Perspective-scored outputs for human annotators while another uses it for toxicity evaluation on RealToxicityPrompts. Papers also sometimes present it as a benchmark or baseline classifier, and operational choices vary, with thresholds such as >0.5, ≥0.7, and 0.32 appearing in different setups.

**Concerns raised.** One paper, in a test of detecting harmful fine-tuning examples, reports that Perspective API flagged 4% of 100 harmful instructions at a threshold of ≥0.7. Another paper additionally evaluates sampled Perspective-scored outputs with human annotators.

## Sources

**Perspective API** (15 papers: [Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf), [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf), [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf), [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://aclanthology.org/2025.naacl-long.388.pdf), [SynthDetoxM: Modern LLMs are Few-Shot Parallel Detoxification Data Annotators](https://aclanthology.org/2025.naacl-long.294.pdf), [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf), [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf), [Re-ranking Using Large Language Models for Mitigating Exposure to Harmful Content on Social Media Platforms](https://aclanthology.org/2025.acl-long.44.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf), [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf))
> An external tool used to classify text along multiple dimensions of toxicity, including severe toxicity, threat, profanity, and identity attack.

**PERSPECTIVE API** (2 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf))
> External tool that provides fine-grained toxicity scoring for text, including attributes like insult, profanity, and identity attack.

**PerspectiveAPI** (1 paper: [“Yes, My LoRD.” Guiding Language Model Extraction with Locality Reinforced Distillation](https://aclanthology.org/2025.acl-long.73.pdf))
> Automated content safety evaluation tool that scores text outputs on dimensions such as toxicity, insult, profanity, severe toxicity, and threat to assess model safety alignment.

**Perspective toxicity model** (1 paper: [Biased Tales: Cultural and Topic Bias in Generating Children's Stories](https://aclanthology.org/2025.emnlp-main.3.pdf))
> State-of-the-art benchmark for detecting toxic content in text, assigning a toxicity score from 0 (non-toxic) to 1 (highly toxic), used to assess safety of generated stories.

## Relationships

### → Perspective API
- **Toxicity** (construct): *measured_by*, 14 papers
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
- **Harmful content generation** (behavioral indicator): *measured_by*, 5 papers
  > To measure the toxicity of these harmful generations, we employ automatic evaluation models pre-trained on toxic datasets, including Perspective API and toxic classifiers (Hanu & Unitary team, 2020) with BERT (Kenton & Toutanova, 2019) and RoBERTa (Liu et al., 2019). (Section 4)
  - [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf)
  - [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > For harmlessness, we follow (Li et al., 2024b) and utilize metrics Expected Maximum Toxicity (EMT) and Toxicity Probability (TP) from the Perspective API to examine the harmful content (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)

### Associated with
- **RealToxicityPrompts** (measurement instrument), 1 paper
  > “For toxicity evaluation, we utilize the PERSPECTIVE API (Lees et al., 2022) for REALTOXICITYPROMPTS”
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument), 1 paper
  > “we randomly sample 780 ... toxicity outputs (for Perspective API) ... We additionally evaluate these samples with human annotators”
  - [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf)
