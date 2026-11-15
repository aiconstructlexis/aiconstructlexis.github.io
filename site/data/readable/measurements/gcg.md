# GCG
**Type:** Measurement instrument  
**Supporting papers:** 37  
**Also known as:** Greedy Coordinate Gradients (GCG), Greedy Coordinate Gradient Descent, nanoGCG, GCG Attack, GCG attack  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats GCG as a white-box, gradient-based jailbreak attack procedure, usually one that greedily optimizes prompt tokens or an adversarial suffix to induce unsafe, specific, or otherwise target outputs. Most definitions describe suffixes appended to harmful queries, while a smaller line describes attack strings prepended to harmful prompts or universal suffixes used to bypass safety filters; one paper instead refers to filtered GCG-generated jailbreak prompts as a dataset, and another mentions nanoGCG as a lightweight variant.

**What it is claimed to measure.** Papers link GCG to 3 constructs and 2 behavioral indicators. The most common measurement claims use it to measure adversarial robustness and jailbreak resistance, often through attack success or failure under GCG; smaller uses report it as measuring harmlessness, robustness, and harmful content detection. Taken together, these claims spread across several safety-related outcomes rather than one construct only.

**Space of uses.** Papers often position GCG as a popular or state-of-the-art white-box attack within multi-attack evaluation suites, rather than as a standalone check. In one paper it is related to CSRT, and quoted passages repeatedly place it alongside PAIR, AutoDAN, TAP, and DeepInception, with papers using it to test defenses, assess finetuned models, generate adversarial prompts or universal jailbreak suffixes, and in some cases run individual, transfer, or lightweight nanoGCG variants.

**Concerns raised.** Several papers describe GCG as a white-box method that requires access to target-model gradients. One paper additionally notes that it produces unreadable prompts, contrasting it with a human-readable alternative.

## Sources

**GCG** (12 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [ALPACA AGAINST VICUNA: Using LLMs to Uncover Memorization of LLMs](https://aclanthology.org/2025.naacl-long.421.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf), [Scaling Trends in Language Model Robustness](https://raw.githubusercontent.com/mlresearch/v267/main/assets/howe25a/howe25a.pdf), [Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.485.pdf), [A Theoretical Understanding of Self-Correction through In-context Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/a399456a191ca36c7c78dff367887f0a-Paper-Conference.pdf), [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf), [Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf))
> Greedy Coordinate Gradient, a white-box jailbreak attack procedure that searches for adversarial suffixes to elicit unsafe responses.

**Greedy Coordinate Gradients (GCG)** (1 paper: [Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf))
> An automated jailbreak algorithm that uses a greedy projected coordinate descent method to find an adversarial suffix of tokens that guides a model towards generating a specific, often undesirable, target output.

**nanoGCG** (1 paper: [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf))
> nanoGCG is a Greedy Coordinate Gradient method used here as a jailbreak evaluation procedure to generate adversarial prompts.

**Greedy Coordinate Gradient Descent** (1 paper: [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf))
> Greedy Coordinate Gradient Descent (GCG), a white-box adversarial jailbreak procedure that generates attack strings prepended to harmful prompts.

**GCG Attack** (1 paper: [Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf))
> A specific implementation of an adversarial suffix attack from Zou et al. (2023b), used to evaluate model robustness.

**GCG attack** (1 paper: [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf))
> An adversarial attack procedure generating universal suffixes to bypass model safety filters and test jailbreak resistance.

## Relationships

### → GCG
- **Jailbreak resistance** (behavioral indicator): *measured_by*, 2 papers
  > We also evaluate the robustness of R2-Guard against SOTA jailbreak attacks including GCG (Zou et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and AutoDAN (Liu et al., 2023). (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **Adversarial robustness** (construct): *measured_by*, 2 papers
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Scaling Trends in Language Model Robustness](https://raw.githubusercontent.com/mlresearch/v267/main/assets/howe25a/howe25a.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including GCG (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 1 paper
  > "For safety filtering, SMAAT accurately identified harmful prompts generated by GCG (Zou et al., 2023), achieving 97-100% accuracy."
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > "robustness is assessed via failure rates against the GCG attack"
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)

### Associated with
- **CSRT** (measurement instrument), 1 paper
  > We compare the CSRT to three non-multilingual red-teaming baselines (i.e., GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024), and PAIR (Chao et al., 2025)). (Section 4.3)
  - [Code-Switching Red-Teaming: LLM Evaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.657.pdf)
