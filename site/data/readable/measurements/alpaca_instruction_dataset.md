# Alpaca instruction dataset
**Type:** Measurement instrument  
**Supporting papers:** 57  
**Also known as:** Alpaca, Alpaca dataset, Alpaca Instruction Tuning Dataset  

## State of the Field

**What it is.** Across papers, the prevailing description is an instruction-following dataset, often described as 52,000 instruction-following demonstrations or instruction-response pairs. Some definitions make its format more explicit as instruction, input, output triples, and papers also refer to the Alpaca training dataset, a cleaned version of Alpaca, code prompts from Alpaca, and an Alpaca subset without unsafe instructions. A smaller line of work uses it less as a standalone tuning set and more as a source of human-written prompts, out-of-domain queries, seed data, or target and anti-target prompts.

**What it is claimed to measure.** Papers link it to 5 constructs and 4 behavioral indicators, and the dominant measurement claim is instruction following. It is also reported as measuring helpfulness and question answering, while smaller lines of work use it for general ability and text generation. Overall, papers spread its use across several targets rather than tying it to a single construct.

**Space of uses.** No measurement instrument is linked to it. In practice, papers position it in several roles: as a fine-tuning or supervised instruction-tuning set, as calibration and recovery-tuning data after pruning or compression, as language-modeling test data, and as a source of control, seed, or out-of-domain queries. When it appears alongside other resources, recurring pairings include WikiText-2 and FLAN v2 in training setups, and SAMSum, CNN/DM, and GSM8K in broader evaluation suites.

**Concerns raised.** A few papers work with restricted or cleaned variants, referring to a cleaned version of Alpaca for post-training or focusing on Alpaca without unsafe instructions. Another stated concern is safety under benign fine-tuning: one study uses Alpaca to test whether utility-oriented fine-tuning can compromise safety.

## Sources

**Alpaca** (16 papers: [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [Language Model Inversion](https://proceedings.iclr.cc/paper_files/paper/2024/file/999fcab97007ebef0cda9949550b4a9e-Paper-Conference.pdf), [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf), [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf), [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf), [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [Mamba-Shedder: Post-Transformer Compression for Efficient Selective Structured State Space Models](https://aclanthology.org/2025.naacl-long.195.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf), [EverTracer: Hunting Stolen Large Language Models via Stealthy and Robust Probabilistic Fingerprint](https://aclanthology.org/2025.emnlp-main.358.pdf), [A Drop-In Solution for On-the-Fly Adaptation of Speculative Decoding in Large Language Models](https://aclanthology.org/2025.acl-long.482.pdf), [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf), [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf), [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf), [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf))
> Instruction-following dataset used for calibration and recovery fine-tuning, serving as a basis for assessing model performance post-compression.

**Alpaca dataset** (3 papers: [Can Watermarks be Used to Detect LLM IP Infringement For Free?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8fba406323cb3930aeaccc9aa64c83a8-Paper-Conference.pdf), [Detecting Strategic Deception with Linear Probes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goldowsky-dill25a/goldowsky-dill25a.pdf), [IDGen: Item Discrimination Induced Prompt Generation for LLM Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a14ac7911df7d369919a687909a14a8b-Paper-Conference.pdf))
> A dataset of instruction-following examples, used in the paper as a source of out-of-domain queries for detecting model infringement.

**Alpaca Instruction Tuning Dataset** (1 paper: [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf))
> An instruction dataset used here as a source of prompts for hallucination-related editing and evaluation setup.

## Relationships

### → Alpaca instruction dataset
- **Instruction following** (behavioral indicator): *measured_by*, 7 papers
  > "Alpaca contains 52K instruction-following data generated from text-davinci-003 (GPT 3.5)" (Section 4.1)
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
  - [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf)
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > The ﬁrst task is Q&A and summarization, including Alpaca [68] and SAMSum [22], and perplexity (PPL) is used to measure their performance. (Section 4.1)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf)
  - [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf)
- **Helpfulness** (construct): *measured_by*, 3 papers
  > To evaluate helpfulness, we assessed the quality of responses generated on the Alpaca dataset (Taori et al., 2023)...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)
  - [Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1510.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Language modeling ability** (construct): *measured_by*, 1 paper
  > Instead, we choose the Alpaca (Taori et al., 2023) dataset, distinct from all four calibration data sources, as our language modeling test data. (Section 5.1)
  - [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf)
- **Semantic consistency** (construct): *measured_by*, 1 paper
  > We create semantically equivalent pairs of questions for evaluation by randomly sampling 300 questions from the Alpaca dataset (Taori et al., 2023) — a popular human-preference dataset - and rephrasing them using gpt-4o mini. (Section 6.1)
  - [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > We employ three distinct text generation datasets: Alpaca (Taori et al., 2023), tldr_news (Belvèze, 2022), and MHC (Amod, 2024), to evaluate the effectiveness of our method across various generation tasks.
  - [JoPA: Explaining Large Language Model's Generation via Joint Prompt Attribution](https://aclanthology.org/2025.acl-long.1074.pdf)

### Associated with
- **Refusal** (behavioral indicator), 1 paper
  > “For the refusal behavior vector, we randomly select 100 instructions from the Alpaca dataset ... and append them with 100 typical refusal or compliance behavior prefixes as responses”
  - [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf)
