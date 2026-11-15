# RealToxicityPrompts
**Type:** Measurement instrument  
**Supporting papers:** 32  
**Also known as:** REALTOXICITYPROMPTS, Real Toxicity Prompts, RealToxicity, Real-Toxicity-Prompts, RealToxicPrompts, RealToxicityPrompts Benchmark  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats RealToxicityPrompts as a dataset or benchmark of text prompts, often described as web-derived, naturally occurring, or sentence-level prompts for text continuation or sentence completion that are likely to elicit toxic generations from language models. Several definitions further describe the prompts as incomplete, seemingly benign or neutral, or divided into toxic and non-toxic prompts for controlled testing. Papers also mention variants and subsets, including a challenge or challenging split of 1,199 prompts, a 10K non-toxic sample, toxic and non-toxic 10K samples, and an adapted version of the 100,000-prompt dataset for sentiment, toxicity, and counterfactual fairness under gendered inputs.

**What it is claimed to measure.** Claims about what it measures mostly converge on Toxicity. Papers link it to 3 constructs and 1 behavioral indicator: it is most often used to measure Toxicity, while smaller lines of work use it to measure Safety and Harmlessness, and the linked behavioral indicator is Harmful content generation. The evidence quotes commonly describe prompting models with challenge prompts and evaluating the resulting completions for toxicity or harmful content.

**Space of uses.** Papers typically position it as a prompting benchmark: models are run on selected prompt subsets, and the resulting continuations are then scored. Among linked instruments, papers relate it only to Perspective API, and some quoted passages specify Expected Maximum Toxicity and Toxicity Probability for responses on this dataset. Some papers also use it alongside ToxiGen, TruthfulQA, SafeEdit, and BOLD.

## Sources

**RealToxicityPrompts** (12 papers: [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](https://aclanthology.org/2025.acl-long.1532.pdf), [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf), [Detoxifying Large Language Models via the Diversity of Toxic Samples](https://aclanthology.org/2025.emnlp-main.298.pdf), [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf), [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf), [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf), [IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf))
> A prompt set used to elicit toxic generations from language models for toxicity evaluation.

**REALTOXICITYPROMPTS** (3 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf), [Conformal Tail Risk Control for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bd/chen25bd.pdf))
> A dataset of text prompts designed to be likely to elicit toxic generations from language models.

**RealToxicity** (1 paper: [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf))
> A dataset used to evaluate the toxicity of generated text, providing a score based on the likelihood of the text being perceived as toxic.

**Real Toxicity Prompts** (2 papers: [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf), [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf))
> A dataset of prompts from the web that are likely to elicit toxic generations from language models.

**Real-Toxicity-Prompts** (1 paper: [Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models](https://aclanthology.org/2025.acl-long.128.pdf))
> A dataset containing 100,000 prompts used to evaluate toxicity in language models, subsetted and adapted for assessing sentiment, toxicity, and counterfactual fairness under gendered inputs.

**RealToxicPrompts** (1 paper: [Beyond Prompt Engineering: Robust Behavior Control in LLMs via Steering Target Atoms](https://aclanthology.org/2025.acl-long.1139.pdf))
> A dataset of seemingly benign or neutral prompts designed to induce large language models to generate toxic or harmful content.

**RealToxicityPrompts Benchmark** (1 paper: [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf))
> Benchmark for evaluating toxicity in model outputs by prompting models with potentially toxic inputs and measuring whether they generate toxic completions.

## Relationships

### → RealToxicityPrompts
- **Toxicity** (construct): *measured_by*, 11 papers
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
- **Harmful content generation** (behavioral indicator): *measured_by*, 2 papers
  > We randomly sample 1k prompts from the non-toxic prompts of the REALTOXICITYPROMPTS (Gehman et al., 2020), which was designed to elicit toxic responses. (Section 4.3)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **Safety** (construct): *measured_by*, 2 papers
  > Finally, we report safety evaluations on RealToxicity (Gehman et al., 2020) and TruthfulQA (Lin et al., 2022). (Section 7.2)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > For harmlessness, we follow (Li et al., 2024b) and utilize metrics ... to examine the harmful content generated on RealToxicityPrompts (Gehman et al., 2020). (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)

### Associated with
- **Perspective API** (measurement instrument), 1 paper
  > “For toxicity evaluation, we utilize the PERSPECTIVE API (Lees et al., 2022) for REALTOXICITYPROMPTS”
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
