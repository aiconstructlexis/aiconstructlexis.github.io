# Sentence completion
**Type:** Behavioral indicator  
**Supporting papers:** 28  
**Also known as:** Sentence completion reasoning, Last word completion, Content analysis, Sentence continuation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is selecting or generating the most plausible continuation of a sentence or broader context. Definitions variously describe the target as the most likely option to complete a sentence or paragraph ending, the correct completion for a given sentence context, or the next sentence in a coherent passage. Papers differ mainly in output format: some use free generation, often with prompts like "Complete the sentence:", while others treat success as choosing the better, more natural, or most plausible continuation from fixed options.

**Variants.** A smaller line of work narrows the behavior to final-word prediction, under names such as last word completion and content analysis, where the task is to predict a passage's missing last word and test long-range or narrative context. Other variants recast it as sentence completion reasoning, sentence continuation between two options, graph-conditioned completion of a node's remaining text using surrounding graph information, or bias-probing completions that check whether a model produces stereotypical output.

**Space of elicitation and scores.** Papers link sentence completion to four measurement instruments. HellaSwag is the most commonly linked instrument and is described as a context or text completion task in which the model generates or chooses the most natural or appropriate ending, often from candidate sentences; the other linked instruments are COPA, SWAG, and StereoSet. SWAG is also described as requiring sentence completions for challenging commonsense scenarios, while StereoSet uses sentences with a gap and three possible completions: stereotypical, anti-stereotypical, and meaningless.

**What it is taken as evidence of.** Papers do not treat sentence completion as evidence of any construct. Separately, one paper reports that it is related to textual reasoning, placing sentence completion within a natural language reasoning suite alongside question answering, natural language inference, co-reference resolution, and general intelligence.

## Sources

**Sentence completion** (7 papers: [ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf), [Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models](https://aclanthology.org/2025.naacl-long.35.pdf), [Fine-Tuned LLMs are “Time Capsules” for Tracking Societal Bias Through Books](https://aclanthology.org/2025.naacl-long.118.pdf), [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf), [GOFA: A Generative One-For-All Model for Joint Graph Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/652c104b5b0652a03684efeaf805463b-Paper-Conference.pdf), [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf), [Taming Knowledge Conflicts in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25c/li25c.pdf))
> Selecting or generating the most plausible continuation of a sentence or context.

**Sentence completion reasoning** (1 paper: [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf))
> The task behavior of selecting or generating the correct completion for a given sentence context.

**Last word completion** (1 paper: [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf))
> The observable task of predicting the final word of a text passage, which often requires understanding long-range context.

**Content analysis** (1 paper: [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf))
> The task of analyzing a passage of text to predict a missing final word, testing the model's ability to understand narrative context.

**Sentence continuation** (1 paper: [DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization](https://aclanthology.org/2025.acl-long.1414.pdf))
> Generating or selecting the most plausible next sentence in a coherent text passage, testing local and global coherence.

## Relationships

### Sentence completion →
- **HellaSwag** (measurement instrument): *measured_by*, 6 papers
  > Hellaswag: Can a machine really finish your sentence? (Section References [46])
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **StereoSet** (measurement instrument): *measured_by*, 1 paper
  > This task contains 765 sentences, each with a gap and three possible completions: stereotypical, anti-stereotypical, and meaningless. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **COPA** (measurement instrument): *measured_by*, 1 paper
  > COPA (Gordon et al., 2012) for sentence completion (Section 4.1).
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
- **SWAG** (measurement instrument): *measured_by*, 1 paper
  > SWAG (Zellers et al., 2018) and HellaSwag (HSwag) (Zellers et al., 2019) requires sentence completions about challenging commonsense scenarios. (Section 4.1)
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)

### Associated with
- **Textual reasoning** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
