# FineWeb
**Type:** Measurement instrument  
**Supporting papers:** 10  

## State of the Field

**What it is.** Across the papers, FineWeb is described as a web-text or pretraining corpus. Definitions variously call it a web-text corpus for analyzing bilinear transformer feature interactions, a high-quality LLM pretraining dataset used to synthesize prompts, and a large corpus of deduplicated English web documents from which one study samples 10k examples to evaluate negative log-likelihood. One paper also refers to "two FineWeb models" with 12 and 16 layers, labeled "fw-small" and "fw-medium."

**What it is claimed to measure.** Papers link FineWeb to one construct and no behavioral indicators. The only recorded measurement claim is that papers use it to measure Generalization: one study evaluates a model trained on C4 on FineWeb as one of several other datasets. In the recorded relationships, measurement claims therefore center on Generalization rather than spreading across multiple constructs.

**Space of uses.** Papers use FineWeb in several ways: as a prompt source for base LLMs, as a source of deduplicated English web documents for negative log-likelihood evaluation, and as data for analyzing bilinear transformer feature interactions at different model sizes. In one evaluation setup, it appears alongside Anthropic HH-RLHF, Synthetic Instruct, PKU SafeRLHF, UltraFeedback, and other datasets, after training on C4. Another paper reports that quantization errors of different methods are strongly correlated on FineWeb.

## Sources

**FineWeb** (3 papers: [Bilinear MLPs enable weight-based mechanistic interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7504142a20a3e1fe9dd7de42f475828c-Paper-Conference.pdf), [Idiosyncrasies in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf), [Why Do Some Inputs Break Low-Bit LLM Quantization?](https://aclanthology.org/2025.emnlp-main.168.pdf))
> A web-text corpus used for analyzing bilinear transformer feature interactions at different model sizes.

## Relationships

### → FineWeb
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
