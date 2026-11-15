# RedPajama-V2
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** RedPajama V2, RedpajamaV2  

## State of the Field

**What it is.** Across the papers, RedPajama-V2 is most commonly treated as a large-scale web-text or web-corpus resource for training or pretraining language models. Definitions also describe it as a preprocessed dataset from diverse internet sources, in one case specifying 30 trillion tokens, while narrower variants include the "sample" and "sample-100B" subsets and, in another use, the validation split.

**What it is claimed to measure.** Most descriptions do not present RedPajama-V2 as a benchmark for named constructs. One paper defines its validation set as a benchmark to measure forgetting by tracking changes in pretraining loss, and papers otherwise do not link it to any constructs or behavioral indicators.

**Space of uses.** The prevailing usage is as pretraining data: papers use it as the corpus on which language models are trained, or as a starting point for a general-domain pretraining dataset. A smaller line of work uses it more instrumentally, as the source of pretraining text domains on which model losses are measured for data selection, and one paper uses both the pretraining set and its validation loss in analyses of forgetting. No other measurement instruments are linked to it.

## Sources

**RedPajama V2** (1 paper: [Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf))
> A web-corpus dataset used as the source of pretraining text domains on which model losses were measured for data selection.

**RedPajama-V2** (2 papers: [No Need to Talk: Asynchronous Mixture of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ae2d3297891cad0c56dd12d60ff7dde-Paper-Conference.pdf), [Programming Every Example: Lifting Pre-training Data Quality Like Experts at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25aa/zhou25aa.pdf))
> A large-scale web-text corpus used to train the language models in the paper.

**RedpajamaV2** (1 paper: [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf))
> A large and diverse corpus (Weber et al., 2024) used for pretraining models, with its validation set also used as a benchmark to measure forgetting by tracking changes in pretraining loss.
