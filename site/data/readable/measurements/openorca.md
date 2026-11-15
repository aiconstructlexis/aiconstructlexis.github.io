# OpenOrca
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** ORCA, Orca  

## State of the Field

**What it is.** Across the papers, OpenOrca is most commonly treated as an instruction and reasoning dataset used in supervised fine-tuning and evaluation. Some definitions broaden this to an ORCA family, including OPENORCA and SLIMORCA, described as fine-tuning datasets for instruction-following and as derived from explanations of chain-of-thought reasoning steps from larger models. A smaller framing presents Orca as an SFT collection that combines prior instruction-tuning data such as FLAN, T0, NIV, and CoT, and one paper describes OpenOrca as augmented FLAN collection data.

**What it is claimed to measure.** Papers use OpenOrca to evaluate general reasoning and comprehension performance and instruction-following capabilities, and one paper also describes it as supporting in-domain test sets for model perplexity. These descriptions do not converge on one named construct, and no construct or behavioral indicator is linked to it.

**Space of uses.** Papers most often position OpenOrca as a supervised fine-tuning corpus, with some also using it as an evaluation or validation dataset. In reported setups it appears alongside GSM8K and ChatDoctor in fine-tuning experiments, alongside OpenHermes-2.5 in supervised fine-tuning, and among datasets used to validate self-information retention and sequence-level semantic aggregation. Work using the ORCA framing also treats OPENORCA and SLIMORCA as test datasets for instruction-following.

## Sources

**OpenOrca** (3 papers: [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf), [Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf), [A Lens into Interpretable Transformer Mistakes via Semantic Dependency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25n/dong25n.pdf))
> An instruction/reasoning dataset used to fine-tune and evaluate general reasoning and comprehension performance.

**ORCA** (1 paper: [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf))
> A dataset family (including OPENORCA and SLIMORCA) used for evaluating instruction-following capabilities, derived from explanations of chain-of-thought reasoning steps from larger models.

**Orca** (1 paper: [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf))
> SFT collection that aggregates data from prior instruction-tuning datasets like FLAN, T0, and CoT, used for re-weighting and downstream evaluation.
