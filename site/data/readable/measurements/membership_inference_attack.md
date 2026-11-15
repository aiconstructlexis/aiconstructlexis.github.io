# Membership inference attack
**Type:** Measurement instrument  
**Supporting papers:** 32  
**Also known as:** Membership Inference Attack (MIA), Membership Inference Attack, Membership inference, Dataset membership inference, Membership inference methods, Membership inference attacks  

## State of the Field

**What it is.** Most papers describe it as a privacy evaluation procedure for testing whether a specific datapoint, input fragment, or sample was used in a model’s training or alignment process, typically by distinguishing member from non-member examples. A few papers specify black-box variants that rely only on model outputs or loss values, and others name heuristics such as perplexity, lowercase probability, zlib compression, and Min-K% probability. A smaller line of work extends the same framing to document-level membership, to suspect-dataset inference, or to unlearning settings where membership is inferred by comparing model behavior before and after unlearning.

**What it is claimed to measure.** Papers link it to 3 constructs and 2 behavioral indicators, so its measurement claims are spread across several privacy- and unlearning-related targets rather than centered on one alone. The prevailing use is to measure privacy preservation, with a smaller but recurring use for privacy leakage, while only a few papers use it to assess forget quality or knowledge memorization. Separately, papers relate it to pre-training data detection, with some describing that task as a special case of membership inference or as determining whether specific data points were used in training.

**Space of uses.** Most papers position it as a privacy-auditing or empirical privacy evaluation step, including for unlearning evaluation, privacy protection capability, and resistance to membership inference attacks. Reported setups include black-box querying of personalized models, output-only auditing without access to logits or token probabilities, and loss-based attacks reported with AUC and TPR at low FPR thresholds. When authors place it alongside named instruments, they link it to 3 measurement instruments, BookMIA, BookTection, and WikiMIA, and one paper also reports using it alongside data extraction attacks.

**Concerns raised.** One paper notes a limitation of output-only, black-box use: inferring whether a particular forget sample was seen during training can be challenging when the attack has access only to model outputs.

## Sources

**Membership Inference Attack (MIA)** (1 paper: [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf))
> An evaluation procedure designed to audit empirical privacy by attempting to determine whether a specific data sample was used in the model's alignment or training process.

**Membership inference attack** (6 papers: [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ju25a/ju25a.pdf), [Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747.pdf), [RewardDS: Privacy-Preserving Fine-Tuning for Large Language Models via Reward Driven Data Synthesis](https://aclanthology.org/2025.emnlp-main.223.pdf), [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf))
> A privacy evaluation procedure that tests whether a datapoint was used in training by distinguishing member from non-member examples.

**Membership Inference Attack** (1 paper: [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf))
> An evaluation procedure designed to determine whether a specific data sample was part of a model's training set by analyzing its output behavior.

**Membership inference** (3 papers: [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf), [Data Mixture Inference Attack: BPE Tokenizers Reveal Training Data Compositions](https://proceedings.neurips.cc/paper_files/paper/2024/file/10e6dfea9a673bef4a7b1cb9234891bc-Paper-Conference.pdf), [Textual Unlearning Gives a False Sense of Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf))
> The observable phenomenon where a model's outputs or internal states can be analyzed to determine if a specific data point was part of its training set.

**Dataset membership inference** (1 paper: [Unlocking Post-hoc Dataset Inference with Synthetic Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25q/zhao25q.pdf))
> The latent ability of a model or method to determine whether a suspect dataset was used in the training of a target LLM, based on statistical signals extracted from model behavior.

**Membership inference methods** (1 paper: [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf))
> Procedures that determine whether a given data point was part of a model’s training set, using heuristics such as perplexity, lowercase probability, zlib compression, and Min-K% probability.

**Membership inference attacks** (1 paper: [OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.emnlp-main.183.pdf))
> Evaluation procedure that tests whether an attacker can determine if specific data was part of the model's training set, used to assess forget quality.

## Relationships

### → Membership inference attack
- **Privacy preservation** (construct): *measured_by*, 3 papers
  > These fully trained prompts, if not properly protected with privacy mechanism, are vulnerable to MIA which aims to infer if an image sample was used for training or not (Section 3.3).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
  - [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf)
- **Privacy leakage** (behavioral indicator): *measured_by*, 2 papers
  > we develop the first Membership Inference Attack (MIA) for evaluating and auditing the empirical privacy for the problem of LLM steering via activation editing
  - [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf)
  - [Privacy Auditing of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e76814a0012a46ade4f997591e86f972-Paper-Conference.pdf)
- **Knowledge memorization** (construct): *measured_by*, 1 paper
  > We adopt four membership inference attack (MIA) methods for knowledge memorization on our collected MIA set. (Introduction)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Forget quality** (construct): *measured_by*, 1 paper
  > To determine whether private information still exists in VLMs after unlearning more accurately, we proposed to use MIAs for evaluation. (Section 2.5.3)
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)

### Associated with
- **Pre-training data detection** (behavioral indicator), 3 papers
  > Pre-training data detection can be considered a special case of Membership Inference Attack (MIA) (Shokri et al., 2017): the goal is to infer whether a given input has been used for training a target LLM
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)
- **WikiMIA** (measurement instrument), 1 paper
  > MIA on LLM pre-training texts. We use the WikiMIA benchmark [52], which leverages the Wikipedia timestamp to separate the early Wiki data as the member data, and recent Wiki data as the non-member data (Section 6.3).
  - [Membership Inference Attacks against Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2c892312af07f8a77afbeed188391f4-Paper-Conference.pdf)
- **BookMIA** (measurement instrument), 1 paper
  > “Previous membership inference benchmarks such as WikiMIA, BookMIA (Shi et al., 2024), and BookTection (Duarte et al., 2024)”
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
- **BookTection** (measurement instrument), 1 paper
  > “Previous membership inference benchmarks such as WikiMIA, BookMIA (Shi et al., 2024), and BookTection (Duarte et al., 2024)”
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
