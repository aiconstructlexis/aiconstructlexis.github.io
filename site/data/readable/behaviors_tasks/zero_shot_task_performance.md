# Zero-shot task performance
**Type:** Behavioral indicator  
**Supporting papers:** 23  
**Also known as:** Zero-shot Evaluation, Zero-shot reasoning, Zero-shot downstream task performance  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is evaluation of model performance on downstream or language-understanding tasks when no in-context examples are provided, and often when no task-specific fine-tuning is used. Most definitions describe answering benchmark questions or completing tasks such as question answering, commonsense reasoning, reading comprehension, or natural language inference from the prompt alone. Success is usually expressed as accuracy, including zero-shot accuracy or reasoning accuracy across benchmark tasks, though some authors phrase the setting as instruction-only execution without examples.

**Variants.** Authors also use nearby labels such as zero-shot evaluation, zero-shot reasoning, and zero-shot downstream task performance. The studied settings recur around commonsense and question-answering benchmarks, with some papers narrowing the scope to multiple-choice or yes or no reasoning tasks, others to reading-comprehension datasets, and others to broader prompt-based downstream suites.

**Space of elicitation and scores.** Papers link this behavior to 17 measurement instruments. The dominant operationalization is lm-evaluation-harness, and the most frequently named task instruments are HellaSwag, PIQA, ARC, and LAMBADA, with other benchmark tasks also used. Scoring is most commonly accuracy, zero-shot accuracy, mean zero-shot accuracy, or average accuracy across tasks or runs, though one paper reports zero-evaluation performance with perplexity scores.

**What it is taken as evidence of.** The papers do not identify any construct that this behavior is taken to indicate. They report it directly as an evaluation outcome rather than linking it to a construct.

## Sources

**Zero-shot task performance** (7 papers: [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf), [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf), [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf), [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf), [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf), [Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d00071564ec447466fc4577743cf1b3-Paper-Conference.pdf), [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf))
> The observable performance of a model on various language understanding tasks, such as question answering and commonsense reasoning, when given no in-context examples.

**Zero-shot Evaluation** (1 paper: [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf))
> The observable behavior of performing tasks without any task-specific fine-tuning or examples provided in the prompt.

**Zero-shot reasoning** (1 paper: [GPTAQ: Efficient Finetuning-Free Quantization for Asymmetric Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dn/li25dn.pdf))
> Answering benchmark questions without task-specific fine-tuning across multiple commonsense and reading-comprehension datasets.

**Zero-shot downstream task performance** (1 paper: [SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mozaffari25a/mozaffari25a.pdf))
> The model's ability to perform various natural language tasks without any task-specific training, as evaluated on benchmarks like MMLU, Piqa, and Arc.

## Relationships

### Zero-shot task performance →
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 8 papers
  > For zero-shot evaluation, we use seven tasks from EleutherAI LM Harness (Gao et al., 2021).
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
  - [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf)
  - [Dynamic Low-Rank Sparse Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/675dc71676eb3bec5326824365a9bac2-Paper-Conference.pdf)
  - [OSTQuant: Refining Large Language Model Quantization with Orthogonal and Scaling Transformations for Better Distribution Fitting](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cebc89b113920dbff7c79854ba765a3-Paper-Conference.pdf)
  - [Bypass Back-propagation: Optimization-based Structural Pruning for Large Language Models via Policy Gradient](https://aclanthology.org/2025.acl-long.1421.pdf)
  - [EvoPress: Accurate Dynamic Model Compression via Evolutionary Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sieberling25a/sieberling25a.pdf)
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
  - [GANQ: GPU-Adaptive Non-Uniform Quantization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25ae/zhao25ae.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 5 papers
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [Dynamic Low-Rank Sparse Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/675dc71676eb3bec5326824365a9bac2-Paper-Conference.pdf)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
- **PIQA** (measurement instrument): *measured_by*, 3 papers
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 2 papers
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
- **ARC** (measurement instrument): *measured_by*, 2 papers
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 2 papers
  > We measure the zero-evaluation performance of trained GPT models on LAMBADA and WikiText using perplexity scores. (Section 5.2)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > Secondly, we measure zero-shot accuracy on five tasks: WinoGrande (Sakaguchi et al., 2021), PiQA (Tata & Patel, 2003), HellaSwag, ARC-easy and ARC-challenge (Clark et al., 2018). (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > evaluate zero-shot performance on seven downstream tasks: BoolQ (Clark et al., 2019), ARC Easy and Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), OpenbookQA (Mihaylov et al., 2018), and PIQA (Bisk et al., 2020) (Section 4.1).
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > For a fair comparison, we evaluate the models on MMLU (23), Arc Challenge (6), and OpenBookQA (35) zero-shot tasks implemented in Language Model Evaluation Harness (18).
  - [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf)
- **MuTual** (measurement instrument): *measured_by*, 1 paper
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **ETHICS** (measurement instrument): *measured_by*, 1 paper
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **WikiText** (measurement instrument): *measured_by*, 1 paper
  > We measure the zero-evaluation performance of trained GPT models on LAMBADA and WikiText using perplexity scores. (Section 5.2)
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **COPA** (measurement instrument): *measured_by*, 1 paper
  > “Table 1. Comparison of zero-evaluation performance... COPA ↑”
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > “Table 1. Comparison of zero-evaluation performance... RACE ↑”
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **WiC** (measurement instrument): *measured_by*, 1 paper
  > “Table 1. Comparison of zero-evaluation performance... WIC ↑”
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > evaluate zero-shot performance on seven downstream tasks: BoolQ (Clark et al., 2019), ARC Easy and Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), OpenbookQA (Mihaylov et al., 2018), and PIQA (Bisk et al., 2020) (Section 4.1).
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
