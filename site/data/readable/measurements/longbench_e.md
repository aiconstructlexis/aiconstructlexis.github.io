# LongBench-E
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Papers most commonly describe LongBench-E as a benchmark covering 13 real-world long-context applications, including coding, question answering, and few-shot learning. Some authors instead describe it as the English-language subset of the LongBench benchmark, used for evaluating long-context understanding. One recurring characterization also calls it a multitask benchmark for long-context understanding, with task lengths averaging between 5k and 32k tokens.

**What it is claimed to measure.** Across the surveyed work, the prevailing claim is that LongBench-E measures Long-context understanding: it is linked to one construct, and papers describe it as evaluating large language models' ability to understand long contexts or to find key information within a long multi-document context. It is also linked to two behavioral indicators, Coding and Few-shot task performance, through papers that use its coding and few-shot learning applications. Overall, papers use it mainly for one construct, with two additional task-level indicators attached to it.

**Space of uses.** Papers use LongBench-E as an evaluation benchmark for comparing models and methods, including experiments with proposed approaches and baseline methods. Some authors position it as an added evaluation, saying they evaluate or further test a model on tasks within LongBench-E, and one paper reports comparing methods on LongBench-E while using EM score to measure the ability to find key information within a long multi-document context. No measurement instrument is linked to it.

## Sources

**LongBench-E** (2 papers: [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf), [Core Context Aware Transformers for Long Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cg/chen25cg.pdf))
> A benchmark covering 13 real-world long-context applications including coding, question answering, and few-shot learning.

## Relationships

### → LongBench-E
- **Long-context understanding** (construct): *measured_by*, 4 papers
  > In addition, we evaluate LongMamba on the tasks within LongBench-E (Bai et al., 2023), which are representative of many real-world long-context applications. (Section 6.1)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
  - [Curse of High Dimensionality Issue in Transformer for Long Context Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cr/zhang25cr.pdf)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
- **Coding** (behavioral indicator): *measured_by*, 1 paper
  > we further test LongMamba on the LongBench-E dataset (Bai et al., 2023), which covers 13 long-context applications, such as coding and few-shot learning. (Section 6.2)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **Few-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > we further test LongMamba on the LongBench-E dataset (Bai et al., 2023), which covers 13 long-context applications, such as coding and few-shot learning. (Section 6.2)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
