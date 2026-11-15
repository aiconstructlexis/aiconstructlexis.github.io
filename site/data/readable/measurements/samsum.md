# SAMSum
**Type:** Measurement instrument  
**Supporting papers:** 32  
**Also known as:** SAMsum, SAMSUM, Samsum, SamSum  

## State of the Field

**What it is.** Across the surveyed work, SAMSum is most commonly described as a dialogue summarization dataset or benchmark built from chat or messenger-like conversations paired with short or human-written summaries. Definitions variously emphasize daily-life messenger conversations, multi-turn or multi-party dialogues, and human-annotated abstractive summarization, and some papers use few-shot variants such as "SAMSUM Few shot" or describe it as a few-shot summarization benchmark. A minority description diverges, with one quoted passage characterizing it as using news articles and machine-generated summaries.

**What it is claimed to measure.** Papers link it to 2 behavioral indicators and 1 construct. The prevailing usage is to measure Text summarization, with a smaller line of work using it for Dialogue summarization, and one paper also uses summarization on SAMSum as part of assessing General ability. Overall, the measurement claims are concentrated on summarization rather than spread broadly across constructs.

**Space of uses.** Across papers, SAMSum is commonly used as one benchmark within broader evaluation suites, though some studies make it the task-specific dataset for text or dialogue summarization experiments. The only explicit instrument-level link is to LongBench, and some authors treat it as a LongBench dataset or a few-shot instruction-following item; other papers place it alongside XSUM, CNN/Daily Mail, TriviaQA, and QMSum. It also appears in practical fine-tuning and evaluation settings, including LoRA finetuning, benign fine-tuning use cases, KV-cache compression, distillation, long-context in-context learning, and uncertainty estimation on summaries.

## Sources

**SAMsum** (6 papers: [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf), [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf), [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf), [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf), [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf))
> Dialogue summarization dataset consisting of chat transcripts and human-written summaries, used to evaluate privacy-preserving summarization.

**SAMSum** (8 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf), [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> A dialogue summarization dataset used to evaluate language generation performance, particularly in summarizing multi-party conversations.

**SAMSUM** (1 paper: [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf))
> A dialogue summarization dataset used as an evaluation set for LLM inference under KV-cache compression.

**Samsum** (1 paper: [Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf))
> A dataset of chat dialogues and their summaries, used for evaluating and fine-tuning models on summarization tasks.

**SamSum** (2 papers: [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf))
> A dialogue summarization benchmark used to evaluate selective generation uncertainty methods on generated summaries.

## Relationships

### → SAMSum
- **Text summarization** (behavioral indicator): *measured_by*, 13 papers
  > As an early application for Hedgehog on larger models, we convert Llama-2 7B (Touvron et al., 2023) before finetuning with low-rank adapters (LoRA) (Hu et al., 2021) on SAMSum summarization (Gliwa et al., 2019).
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
  - [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse Attention](https://aclanthology.org/2025.acl-long.1542.pdf)
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
  - [ACING: Actor-Critic for Instruction Learning in Black-Box LLMs](https://aclanthology.org/2025.emnlp-main.965.pdf)
  - [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf)
- **Dialogue summarization** (behavioral indicator): *measured_by*, 2 papers
  > dialogue summarization: samsum (Gliwa et al., 2019) and qmsum (Zhong et al., 2021) from LongBench (Bai et al., 2024)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
  - [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To explore the side effects of sequential model editing on the general abilities of LLMs, four representative tasks with corresponding datasets were adopted for assessment... including: ... Summarization on the SAMSum (Gliwa et al., 2019)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)

### Associated with
- **LongBench** (measurement instrument), 1 paper
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): ...SAMSum (few-shot instruction following)... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
