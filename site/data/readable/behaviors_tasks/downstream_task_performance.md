# Downstream task performance
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Downstream task evaluation, Downstream task solving, Task performance  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is the model's observable performance on downstream tasks or benchmarks, usually after pre-training or fine-tuning. Most definitions treat success as solving representative evaluation problems well, often on supervised tasks, and papers score this with task accuracy or overall benchmark quality; smaller variants narrow it to performance retained after continual growth or to the quality of ensemble outputs on a benchmark.

**Variants.** Authors use nearby labels such as downstream task evaluation, downstream task solving, and task performance. The behavior is studied after pre-training, after fine-tuning, during continual growth or lifelong editing, and in ensemble settings, with tasks ranging from sentiment analysis and math to multi-task suites and language-specific benchmark collections; some papers also vary shot setting by averaging from 0-shot to 5-shot.

**Space of elicitation and scores.** Papers link downstream task performance to 21 measurement instruments. The most frequently used are GSM8K, lm-evaluation-harness, AG News, ARC-Easy, and AlpacaEval, while other papers use additional downstream datasets and suites. Papers use these as downstream datasets, benchmark suites, or evaluation harnesses, and scoring is commonly reported as downstream task accuracy, finetune accuracy, or an average score across shot settings.

**What it is taken as evidence of.** Papers do not converge on a broad construct interpretation for this behavior. Only 1 construct is linked, Generation diversity, and one paper reports it as related to downstream task performance in discussions of a Pareto front of task performance and diversity of model generations. Separately, 1 behavioral indicator is linked: one paper claims a causal relationship from Reward hacking to downstream task performance, describing degradation on downstream tasks as attributable to reward hacking.

## Sources

**Downstream task performance** (1 paper: [LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently](https://proceedings.iclr.cc/paper_files/paper/2025/file/03945380ca5af0dc80782d8e0b72a8d7-Paper-Conference.pdf))
> Producing outputs that support strong performance on supervised language tasks after pre-training or continual growth.

**Downstream task evaluation** (1 paper: [The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dl/wang25dl.pdf))
> The observable performance of a pre-trained model on a suite of specific, often supervised, tasks to assess its acquired capabilities.

**Downstream task solving** (1 paper: [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf))
> The observable performance of the model on specific tasks like sentiment analysis or math after fine-tuning.

**Task performance** (1 paper: [Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf))
> The overall quality of an ensemble's outputs on a downstream benchmark or task, as reflected by how well it solves the target evaluation problems.

## Relationships

### Downstream task performance →
- **GSM8K** (measurement instrument): *measured_by*, 3 papers
  > We assess their impact on task performance, diversity of model generations, and computational requirements. Concretely, we compare MLE-based next token prediction and different IRL methods for fine-tuning LLMs on common benchmarks. ... We use the following datasets and subsets for ablation in the following sections: XSUM, GSM8k, TLDR, and WMT22.
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 3 papers
  > ...and on an aggregate of six downstream tasks using the EleutherAI LM Harness (Gao et al., 2023)... (Section 5)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
  - [Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bu/zhang25bu.pdf)
  - [The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dl/wang25dl.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > “In Table 6, we list the performance on downstream tasks of GLUE and SAQuAD according to LIGO(Wang et al., 2023).”
  - [LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently](https://proceedings.iclr.cc/paper_files/paper/2025/file/03945380ca5af0dc80782d8e0b72a8d7-Paper-Conference.pdf)
  - [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf)
- **SST-2** (measurement instrument): *measured_by*, 2 papers
  > “For fine-tuning task, we consider SST2(Socher et al., 2013), AGNEWS(Zhang et al., 2015), GSM8K(Cobbe et al., 2021) and AlpacaEval (Li et al., 2023a) as the user fine-tuning task.”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **AG News** (measurement instrument): *measured_by*, 2 papers
  > “For fine-tuning task, we consider SST2(Socher et al., 2013), AGNEWS(Zhang et al., 2015), GSM8K(Cobbe et al., 2021) and AlpacaEval (Li et al., 2023a) as the user fine-tuning task.”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 2 papers
  > “For fine-tuning task, we consider SST2(Socher et al., 2013), AGNEWS(Zhang et al., 2015), GSM8K(Cobbe et al., 2021) and AlpacaEval (Li et al., 2023a) as the user fine-tuning task.”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... 4K context: arc easy
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... hellaswag
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... winogrande
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 2 papers
  > Figure 3: Models trained with 4k context length. Final performance (y-axis) on a set of downstream tasks... lambada
  - [nGPT: Normalized Transformer with Representation Learning on the Hypersphere](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c12689a89e98a61bcaa65285a41b7c-Paper-Conference.pdf)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **XSum** (measurement instrument): *measured_by*, 1 paper
  > We assess their impact on task performance, diversity of model generations, and computational requirements. Concretely, we compare MLE-based next token prediction and different IRL methods for fine-tuning LLMs on common benchmarks. ... We use the following datasets and subsets for ablation in the following sections: XSUM, GSM8k, TLDR, and WMT22.
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > “In Table 6, we list the performance on downstream tasks of GLUE and SAQuAD according to LIGO(Wang et al., 2023).”
  - [LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently](https://proceedings.iclr.cc/paper_files/paper/2025/file/03945380ca5af0dc80782d8e0b72a8d7-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **COPA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **WSC** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **IndoCulture** (measurement instrument): *measured_by*, 1 paper
  > To assess the broader impact of safety fine-tuning on downstream performance, we also evaluated the fine-tuned models on a range of Indonesian benchmarks, including IndoMMLU (Koto et al., 2023), IndoCareer (Koto, 2025), IndoCulture (Koto et al., 2024), MAPS (Liu et al., 2024), COPAL-ID (Wibowo et al., 2024), and IndoCloze (Koto et al., 2022).
  - [IndoSafety: Culturally Grounded Safety for LLMs in Indonesian Languages](https://aclanthology.org/2025.emnlp-main.465.pdf)
- **COPAL-ID** (measurement instrument): *measured_by*, 1 paper
  > To assess the broader impact of safety fine-tuning on downstream performance, we also evaluated the fine-tuned models on a range of Indonesian benchmarks, including IndoMMLU (Koto et al., 2023), IndoCareer (Koto, 2025), IndoCulture (Koto et al., 2024), MAPS (Liu et al., 2024), COPAL-ID (Wibowo et al., 2024), and IndoCloze (Koto et al., 2022).
  - [IndoSafety: Culturally Grounded Safety for LLMs in Indonesian Languages](https://aclanthology.org/2025.emnlp-main.465.pdf)

### → Downstream task performance
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > One of the challenges of the alignment step is possible degradation of performance on downstream tasks, which can be attributed to reward hacking (Xu et al., 2024b). (Section 6.2)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)

### Associated with
- **Generation diversity** (construct), 1 paper
  > “Our experiments demonstrate particularly strong gains for IRL on the Pareto front of task performance and diversity of model generations.”
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Pile-CC** (measurement instrument), 1 paper
  > Fortunately, Liu et al. (2024) finds that validation loss on Pile-CC correlates most strongly with downstream performance across their evaluations. (Section 4.2)
  - [Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bu/zhang25bu.pdf)
