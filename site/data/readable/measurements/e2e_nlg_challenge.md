# E2E NLG Challenge
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** E2E NLG, E2E  

## State of the Field

**What it is.** Across papers, the prevailing description is a benchmark or dataset for natural language generation from structured input in the restaurant domain. Authors variously refer to it as E2E NLG Challenge, E2E NLG, or simply E2E, and most describe the task as generating natural language from structured meaning representations; some instead phrase it as data-to-text or table-to-text generation, and one description specifies that it verbalizes key-value attribute pairs in English.

**What it is claimed to measure.** Papers link it to two behavioral indicators and no constructs. The more prevalent recorded use is to measure Text generation, with papers describing it as an NLG or text generation benchmark, and it is also used to measure Data-to-text generation, including table-to-text generation and verbalizing structured attributes, so the recorded claims cluster around those two behavioral indicators rather than a broader construct set.

**Space of uses.** No measurement instrument is linked to it. In practice, papers often use it alongside WebNLG, and one text generation setup also groups it with CommonGen and an Adidas product description dataset; a recurring usage is as a benchmark for fine-tuning or adaptation experiments with GPT-2 medium or large, where authors position it as a commonly used benchmark for evaluating NLG models.

## Sources

**E2E NLG Challenge** (3 papers: [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf), [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf))
> A benchmark for evaluating natural language generation systems in the restaurant domain, focusing on generating text from structured meaning representations.

**E2E NLG** (1 paper: [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf))
> E2E NLG is a text generation benchmark used to evaluate generation from structured meaning representations to natural language.

**E2E** (5 papers: [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.321.pdf), [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf), [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf))
> The E2E NLG Challenge dataset, focused on generating text from structured meaning representations in the restaurant domain.

## Relationships

### → E2E NLG Challenge
- **Text generation** (behavioral indicator): *measured_by*, 8 papers
  > We compare our approach with LoRA and other parameter-efficient adaptation methods on the natural language understanding (GLUE) and natural language generation (E2E) benchmarks... (Section 1)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **Data-to-text generation** (behavioral indicator): *measured_by*, 6 papers
  > ...we consider 7 datasets corresponding to commonly-studied natural language generation (NLG) tasks [51]: ... E2E and WebNLG (data-to-text generation)... (Section 5.1)
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [LoCA: Location-Aware Cosine Adaptation for Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d63d7d489a9338afff53d17410ea2c10-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
