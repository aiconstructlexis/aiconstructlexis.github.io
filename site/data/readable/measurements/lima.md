# LIMA
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the definitions, papers consistently treat LIMA as a dataset, though they describe its role differently. One description presents it as a natural language dataset used to study memorization in a non-code domain and to test whether findings generalize beyond code. Another frames it as a dataset for instruction fine-tuning, consisting of curated prompts and responses designed to teach models to follow specific instructional formats.

**What it is claimed to measure.** Its measurement role is narrow. Papers link it to 1 construct, Memorization, and to no behavioral indicators; the recorded claim is that Memorization is measured by LIMA. One study uses it to examine memorization on natural language datasets across task domains (Measuring memorization in RLHF for code completion).

**Space of uses.** The uses split between studying memorization and additional training. One paper studies memorization on LIMA alongside Anthropic HH as a natural language dataset, while another reports additional training using LIMA in an instruction fine-tuning setup (Peri-LN: Revisiting Normalization Layer in the Transformer Architecture). No measurement instrument is linked to it.

## Sources

**LIMA** (2 papers: [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf), [Peri-LN: Revisiting Normalization Layer in the Transformer Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25u/kim25u.pdf))
> A natural language dataset used to study memorization in a non-code domain to test the generalizability of findings.

## Relationships

### → LIMA
- **Memorization** (construct): *measured_by*, 1 paper
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
