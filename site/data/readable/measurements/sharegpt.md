# ShareGPT
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Across papers, ShareGPT is most commonly described as a dataset, or a collection from sharegpt.com, of user-shared conversations with ChatGPT. Definitions also frame it as real-world user requests, dialog, instruction-response pairs, and, in some systems work, as real user conversations with LLMs or conversation traces; one description calls sharegpt.com "a platform where ChatGPT users voluntarily share their conversations." Some papers use selected portions or derivatives of it, including 10,000 instruction-response pairs for supervised fine-tuning, another 1,000 instructions for evaluation, subsampled workload types, and synthetic workloads built from its real input and output texts.

**What it is claimed to measure.** The recorded measurement claims are narrow rather than spread across many targets: papers link ShareGPT to one construct and one behavioral indicator. One paper reports that Robustness is measured by ShareGPT, assessing robustness against fine-tuning by fine-tuning on ShareGPT and Evol-Instruct to try to overwrite embedded watermarks. Separately, one paper relates ShareGPT to Instruction following, describing it as a general instruction tuning set that focuses on the instruction-following ability of models.

**Space of uses.** Most commonly, papers use ShareGPT as a source of prompts, instruction-response pairs, or conversation traces for fine-tuning, evaluation, or workload generation. It appears with OpenOrca in supervised fine-tuning, with ArenaHard and Numina in curated prompt-set evaluation, and with WildGPT in workload sampling; other papers also use it as a source of authentic multilingual user queries, as a wild-query source, and as the basis for synthetic or subsampled serving workloads. Papers link it to one other measurement instrument, HelpSteer2, whose prompts are reported to be mostly sourced from ShareGPT.

## Sources

**ShareGPT** (10 papers: [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Quantification of Large Language Model Distillation](https://aclanthology.org/2025.acl-long.248.pdf), [Demystifying Cost-Efficiency in LLM Serving over Heterogeneous GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25c/jiang25c.pdf), [Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations](https://aclanthology.org/2025.emnlp-main.145.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf))
> A dataset of user-shared conversations with ChatGPT, used here for instruction fine-tuning and evaluation.

## Relationships

### → ShareGPT
- **Robustness** (construct): *measured_by*, 1 paper
  > This section assesses the robustness of CLMTracing against fine-tuning, wherein the model is fine-tuned on two clean datasets, ShareGPT and Evol-Instruct, with the goal of overwriting embedded watermarks. (Section 4.2.2)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)

### Associated with
- **HelpSteer2** (measurement instrument), 1 paper
  > Most of the prompts (over 95%) used in HelpSteer2 are sourced from ShareGPT [19], a platform where ChatGPT users voluntarily share their conversations.
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > “ShareGPT is a dialog dataset collected from sharegpt.com, a website collecting user-shared dialog with ChatGPT. This dataset encompasses a wide range of topics, making it suitable as a general instruction tuning set focusing on the instruction-following ability of models.”
  - [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf)
