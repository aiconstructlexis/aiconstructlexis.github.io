# Mantis-Eval
**Type:** Measurement instrument  
**Supporting papers:** 9  
**Also known as:** Mantis  

## State of the Field

**What it is.** Across definitions, papers most commonly describe Mantis-Eval as an evaluation dataset or benchmark for multi-image reasoning. The prevailing framing is an evaluation set of high-quality, human-annotated multi-image reasoning samples: one description specifies 207 examples and mentions tasks such as size perception and weight comparison, while another highlights co-reference, reasoning, and comparison. A smaller line of work refers to it simply as Mantis and treats it as a multi-image benchmark used to assess performance on multi-image inputs.

**What it is claimed to measure.** In relationship claims, papers use it to measure 2 constructs and 1 behavioral indicator. The most common measured target is multi-image reasoning, and papers also report it as measuring multimodal reasoning and multi-image visual question answering. Overall, these links cluster around reasoning over multiple images rather than spreading across many different targets.

**Space of uses.** No measurement instrument is linked to it. Papers instead position it as one benchmark within broader multi-image evaluation suites, most often alongside MMMU and BLINK, and sometimes with QBench, NLVR2, or MVBench. In those settings it is used for performance comparison, including on multi-image VQA results tables, and as a probe of multi-image reasoning or analysis abilities.

## Sources

**Mantis-Eval** (3 papers: [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf), [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf), [Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains](https://aclanthology.org/2025.acl-long.1347.pdf))
> An evaluation dataset for multi-image visual reasoning used for performance comparison.

**Mantis** (2 papers: [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multi-image benchmark used to assess performance on multi-image inputs.

## Relationships

### → Mantis-Eval
- **Multi-image reasoning** (construct): *measured_by*, 6 papers
  > We additionally evaluate models on MMMU [Yue et al., 2024](containing both single and multi-image questions) and Mantis-Eval [Jiang et al., 2024](all multi-image questions) to probe a model’s multi-image reasoning abilities beyond in-context learning evaluations. (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Multi-image visual question answering** (behavioral indicator): *measured_by*, 2 papers
  > We additionally evaluate models on ... Mantis-Eval [Jiang et al., 2024](all multi-image questions) to probe a model’s multi-image reasoning abilities... (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > “On more complex multimodal reasoning benchmarks, the MINT-1T model outperforms OBELICS on MMMU but performs worse on Mantis-Eval.”
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
