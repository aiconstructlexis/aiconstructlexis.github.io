# WMT
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Most commonly, papers treat WMT as the Workshop on Machine Translation benchmark or shared task for translation evaluation, often using the English-German setting as WMT EnDe or EN→DE. Definitions also refer to collections of yearly WMT tasks. A smaller line of work describes WMT instead as a human-preference dataset used to construct contrastive instruction-response pairs for machine translation.

**What it is claimed to measure.** Papers link WMT to one behavioral indicator, Machine translation, and to two constructs, Translation quality and Text generation quality. The prevailing claim is that WMT measures machine translation, and papers also report it as measuring translation quality. A smaller usage treats it as measuring text generation quality, with one study noting that "Quality is measured in terms of BLEU for WMT" (Faster Cascades via Speculative Decoding).

**Space of uses.** Papers use WMT as a translation evaluation task and as one task within multi-task setups. One common pattern is to pair WMT EnDe or EN→DE with CNN/DM, and sometimes XSum, when models are supervised fine-tuned on several tasks; another is to place WMT alongside MLQE-PE and FLORES when discussing benchmarks for translation quality, as one paper states: "Benchmarks like WMT, MLQE-PE, and FLORES have become central to evaluating translation quality" (Evaluating Language Translation Models by Playing Telephone).

## Sources

**WMT** (4 papers: [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf), [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf))
> The Workshop on Machine Translation (WMT) benchmark, specifically the English-German (EnDe) task, is used to evaluate machine translation performance.

## Relationships

### → WMT
- **Machine translation** (behavioral indicator): *measured_by*, 3 papers
  > "WMT for machine translation"
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
  - [When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1402.pdf)
- **Translation quality** (construct): *measured_by*, 1 paper
  > Benchmarks like WMT (Freitag et al., 2021b), MLQE-PE (Fomicheva et al., 2020), and FLORES (Team et al., 2022) have become central to evaluating translation quality. (Section 2)
  - [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT"
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
