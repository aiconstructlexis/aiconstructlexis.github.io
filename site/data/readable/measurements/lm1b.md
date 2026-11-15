# LM1B
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** lm1b  

## State of the Field

**What it is.** Papers treat LM1B as a dataset. One description names it the One-Billion Word Language Model Benchmark and uses it for language modeling evaluation, while another uses it to run experiments and check whether results seen on C4 also appear on a different data source.

**What it is claimed to measure.** Papers link LM1B to one construct and no behavioral indicators. The only reported measurement claim is that it measures Zero-shot generalization: a paper describes out-of-domain unseen datasets as validating models' ability in zero-shot generalization, and LM1B is linked to that evaluation.

**Space of uses.** Papers do not link it to another measurement instrument. In use, LM1B appears alongside C4, where authors report 'observed similar results,' and alongside the OpenWebText test set in an evaluation that uses out-of-domain unseen datasets to validate zero-shot generalization; elsewhere it is presented as a language modeling benchmark.

## Sources

**lm1b** (1 paper: [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf))
> A dataset used for running experiments to observe results similar to those on C4, validating the method across different data sources.

**LM1B** (1 paper: [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf))
> The One-Billion Word Language Model Benchmark (LM1B), a dataset used for evaluating language modeling performance.

## Relationships

### → LM1B
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > We evaluate the model capacity for both the OpenWebText test set and seven out-of-domain unseen datasets, used to validate the models' ability in zero-shot generalization. These unseen datasets include Our Penn Tree Bank (PTB)... Wikitext... LM1B
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
