# Zero-shot question answering
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Zero-shot Question Answering  

## State of the Field

**Space of definitions.** The prevailing usage treats zero-shot question answering as answering questions without task-specific examples in the prompt or context, and often without fine-tuning or additional training. Most definitions describe success as producing correct answers, commonly on multiple-choice tasks, and papers usually report it as zero-shot accuracy; some authors broaden it to downstream or reasoning tasks answered from provided context or general knowledge, while one paper frames it as relying only on pre-trained internal knowledge and the prompt.

**Variants.** Papers use closely related labels such as zero-shot QA, zero-shot evaluation, zero-shot accuracy evaluation, and zero-shot tasks or zero-shot settings. The behavior is most often studied on benchmark tasks like BoolQ, PIQA, WinoGrande, HellaSwag, and ARC, and some papers broaden it to question answering and other natural language understanding tasks across various domains.

**Space of elicitation and scores.** Papers link this behavior to 10 measurement instruments. It is most often measured by benchmark datasets or tasks, especially BoolQ, PIQA, WinoGrande, HellaSwag, and ARC; scoring is typically reported as zero-shot accuracy or task accuracy, and one linked instrument is an evaluation toolkit rather than a benchmark task.

**What it is taken as evidence of.** Papers do not report this behavior as evidence of any construct, so no agreement or disagreement is stated about what it reflects.

## Sources

**Zero-shot question answering** (5 papers: [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf), [QLLM: Accurate and Efficient Low-Bitwidth Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/437bc4ccafd3fc6d4289bd10940be42b-Paper-Conference.pdf), [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf), [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf), [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.624.pdf))
> Generating correct answers to multiple-choice questions without any task-specific training examples provided in context.

**Zero-shot Question Answering** (1 paper: [ShiftAddLLM: Accelerating Pretrained LLMs via Post-Training Multiplication-Less Reparameterization](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c30a37c75f062e0bf79297c73db8c6c-Paper-Conference.pdf))
> The observable behavior of answering questions on downstream tasks without fine-tuning or additional training.

## Relationships

### Zero-shot question answering →
- **BoolQ** (measurement instrument): *measured_by*, 4 papers
  > For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022). (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 4 papers
  > For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022). (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
  - [Let LLM Tell What to Prune and How Much to Prune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25p/yang25p.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 4 papers
  > For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022). (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
  - [Let LLM Tell What to Prune and How Much to Prune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25p/yang25p.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 3 papers
  > “accuracies of zero-shot tasks including Winogrande [29], HellaSwag [41], PIQA [4], BoolQ [7], and ARC [8] are also reported.”
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
  - [Let LLM Tell What to Prune and How Much to Prune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25p/yang25p.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > To verify the effectiveness and generalizability, we perform extensive evaluation of our models on 7 zero-shot tasks. We employ a set of seven tasks sourced from the EleutherAI LM Harness [50]. (Section 7.1).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 2 papers
  > “accuracies of zero-shot tasks including Winogrande [29], HellaSwag [41], PIQA [4], BoolQ [7], and ARC [8] are also reported.”
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > "we evaluate our method and other methods on five well-known zero-shot tasks: PIQA [4]; WinoGrande [33]; HellaSwag [45]; ARC-e and ARC-c [6]."
  - [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 2 papers
  > "we evaluate our method and other methods on five well-known zero-shot tasks: PIQA [4]; WinoGrande [33]; HellaSwag [45]; ARC-e and ARC-c [6]."
  - [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > Moreover, we also evaluate the accuracy for 7 zero-shot QA datasets: ARC-c (Clark et al., 2018), ARC-e (Clark et al., 2018), BoolQ (Clark et al., 2019), Hellaswag (Zellers et al., 2019), OBQA (Mihaylov et al., 2018), PIQA (Bisk et al., 2020), and Winogrande (Sakaguchi et al., 2020). (Section 4.1)
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We evaluate quantized LLMs using ... zero-shot accuracy on the benchmarks ARC (Clark et al., 2018), LAMBADA (Paperno et al., 2016), MMLU (Hendrycks et al., 2020), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), and WinoGrande (Sakaguchi et al., 2021) (Section 4).
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
