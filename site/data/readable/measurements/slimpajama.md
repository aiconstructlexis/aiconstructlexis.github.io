# SlimPajama
**Type:** Measurement instrument  
**Supporting papers:** 26  
**Also known as:** Slimpajama  

## State of the Field

**What it is.** Across the papers, SlimPajama is most commonly treated as a large-scale text corpus or pre-training dataset. Several definitions present it simply as the corpus from which files are selected or as the data source for language-model pretraining, while some papers describe it more specifically as a cleaned and deduplicated version of RedPajama and a high-quality corpus with diverse sources such as C4, ArXiv, GitHub, and Books. A smaller line of work foregrounds subsets within it, either by selecting categories such as StackExchange, Github Codes, ArXiv, and Book, or by drawing token subsets for experiments.

**What it is claimed to measure.** Papers do not report SlimPajama as measuring any construct or behavioral indicator. The descriptions instead use it as experimental data for training, post-training, pruning recovery, and related model-development procedures.

**Space of uses.** Most papers position SlimPajama as a training or continued-training corpus rather than a standalone evaluation protocol. Papers use it for file selection, post-prune recovery, continual pre-training after architectural changes, post-training after pruning, general language-model training, and finetuning; one study also samples topic-specific categories from it to simulate collaboration among users with different preferences. No other measurement instrument is linked to it.

## Sources

**SlimPajama** (7 papers: [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf), [FlexiGPT: Pruning and Extending Large Language Models with Low-Rank Weight Sharing](https://aclanthology.org/2025.naacl-long.31.pdf), [ReGLA: Refining Gated Linear Attention](https://aclanthology.org/2025.naacl-long.147.pdf), [P2 Law: Scaling Law for Post-Training After Model Pruning](https://aclanthology.org/2025.acl-long.283.pdf), [On-Device Collaborative Language Modeling via a Mixture of Generalists and Specialists](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25h/fan25h.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf))
> A large text corpus used as the pre-training data source from which files are selected.

**Slimpajama** (1 paper: [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf))
> A cleaned and deduplicated version of the RedPajama dataset, serving as a high-quality pre-training corpus with diverse sources.
