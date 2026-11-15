# VTAB-1k
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** VTAB-1K  

## State of the Field

**What it is.** Most definitions treat VTAB-1k as a vision benchmark or suite of 19 diverse visual tasks, usually described as image classification tasks, spanning Natural, Specialized, and Structured domains. Definitions also describe it as used to evaluate transfer learning methods and the fine-tuning performance of vision models. Some papers make the 1k setting explicit by stating that each dataset has 1000 training examples, and a smaller line of work frames it as assessing generalization capabilities. One quoted passage further specifies 7 Natural, 4 Specialized, and 8 Structured datasets, while another notes structured tasks such as depth and orientation prediction.

**What it is claimed to measure.** Across the recorded links, papers use VTAB-1k to measure 1 behavioral indicator, Image classification, and it has no linked constructs. The claims therefore converge on a single target rather than spreading across multiple constructs: relationship evidence repeatedly describes VTAB-1k as evaluating image classification or visual classification tasks, and one paper says it is designed to test "image classification and prediction capabilities."

**Space of uses.** Papers commonly position VTAB-1k as a main benchmark for checking fine-tuning efficacy, especially for vision models and parameter-efficient transfer learning methods. As one study puts it, it has been "extensively used to evaluate parameter-efficient transfer learning algorithms" (Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization), and other papers describe evaluating the efficacy of their method on VTAB-1k or fine-tuning ViT on the benchmark. No other measurement instrument is linked to it.

## Sources

**VTAB-1K** (2 papers: [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf))
> A diverse vision benchmark consisting of 19 image classification tasks across natural, specialized, and structured domains for evaluating transfer learning methods.

**VTAB-1k** (3 papers: [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf))
> The Visual Task Adaptation Benchmark (VTAB-1k) is a suite of 19 diverse visual tasks across Natural, Specialized, and Structured domains, used to evaluate the fine-tuning performance of vision models.

## Relationships

### → VTAB-1k
- **Image classification** (behavioral indicator): *measured_by*, 7 papers
  > For the CV task, we use ViT-B/16 (Dosovitskiy et al., 2020) as our pre-trained model and evaluate the efficacy of our method on the VTAB-1k (Zhai et al., 2019) benchmark. (Section 4)
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
  - [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf)
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)
  - [Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pham25b/pham25b.pdf)
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)
  - [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf)
