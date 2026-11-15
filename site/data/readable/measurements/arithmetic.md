# Arithmetic
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the papers, Arithmetic is described as an evaluation task built from arithmetic questions or expressions, though the exact format varies. One description uses natural language addition and subtraction questions with at most 5-digit numbers, another uses mathematical expressions with six unique two-digit numbers and addition, multiplication, and subtraction, and another describes 1,000 generated problems in the form a + b · c + d − e · f.

**What it is claimed to measure.** Papers use Arithmetic to measure one construct, Mathematical reasoning, and no behavioral indicators are linked to it. The measurement claim therefore converges on a single construct rather than being spread across several: the paper that makes this link describes Arithmetic as evaluating a model's fundamental mathematical reasoning abilities.

**Space of uses.** Papers use Arithmetic in different evaluation setups. In Benchmarking and Improving Generator-Validator Consistency of Language Models, it is used to instantiate generator-validator consistency by randomizing correctness, prompting a generator to produce a correct or incorrect response and having a validator check it; elsewhere, papers place it among broader evaluations on diverse datasets across multiple domains. No other measurement instrument is linked to it.

## Sources

**Arithmetic** (3 papers: [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf), [Let Models Speak Ciphers: Multiagent Debate through Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/e444859b2a22df6b56af9381ad1e9480-Paper-Conference.pdf), [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf))
> Benchmark task involving natural language arithmetic questions (addition and subtraction of up to 5-digit numbers) used to assess generator-validator consistency via correctness randomization.

## Relationships

### → Arithmetic
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > Arithmetic (Brown et al., 2020): a datasets evaluates the model’s fundamental mathematical reasoning abilities. (Section 4.1)
  - [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf)
