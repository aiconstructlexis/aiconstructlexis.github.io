# Representation learning
**Type:** Construct  
**Supporting papers:** 14  
**Also known as:** Feature learning, Semantic representation learning  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats representation learning as a model's ability to learn embeddings or features of inputs that preserve useful information for downstream tasks, often by encoding similar instances closely in a latent space. A smaller line of work narrows this to learning invariant or environment-relevant contextual features, or to learning semantic rather than token-pattern representations. Some authors also describe it more mechanistically, as lower or deeper layers forming intermediate representations or applying a fixed representation function before later in-context learning.

**Space of facets.** The main named variants are feature learning, which emphasizes contextual, invariant, or environment-relevant features, and semantic representation learning, which emphasizes semantic meaning and is explicitly contrasted with token pattern representations. Several papers use representation learning and feature learning in closely overlapping ways, as learning useful internal features, embeddings, or rich latent representations that transfer across tasks. Another recurring organization places it inside accounts of in-context learning, where lower layers first transform inputs into a useful format and deeper layers are discussed in terms of intermediate representations.

**Space of measurement.** Operationalization is sparse: papers link representation learning to 1 measurement instrument, the Nucleotide Transformer Benchmark, and to no behavioral indicators. The linked instrument is a benchmark, used by fine-tuning pretrained models and evaluating the learned representations on benchmark tasks. This operationalization lines up with the prevailing definitions that present representation learning as producing transferable representations for downstream tasks.

**Links.** One paper claims a causal relationship from representation learning to in-context learning, arguing that in-context learning can improve by learning to encode informative basis representations. Other papers relate representation learning to in-context learning by treating in-context learning as something studied through a representation-learning lens. Separately, one paper claims a causal relationship from representation learning to generation diversity, stating that representation-level learning effectively refines generation diversity, and no correlational links are reported.

## Sources

**Feature learning** (1 paper: [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf))
> The model's capacity to learn useful representations of input data that capture invariant or environment-relevant patterns, which can be enhanced through context-based training.

**Representation learning** (7 papers: [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf), [Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf), [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf), [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf), [Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/60cefc59610f8f59ea10099f99a36726-Paper-Conference.pdf), [On Support Samples of Next Word Prediction](https://aclanthology.org/2025.acl-long.507.pdf), [Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf))
> The ability of a model to learn to encode input data into a latent space where similar instances are represented closely, facilitating downstream tasks.

**Semantic representation learning** (1 paper: [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf))
> The ability to learn and utilize semantic meaning rather than superficial token patterns, which VLLMs rely on for effective MM-ICL performance.

## Relationships

### Representation learning →
- **In-context learning** (construct): *causes*, 3 papers
  > we show that ICL can improve upon the a priori optimal rate when the task class basis resides in a coarser Besov space by learning to encode informative basis representations, emphasizing the importance of pretraining on diverse tasks. (Section 1)
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
  - [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf)
- **Nucleotide Transformer Benchmark** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the learned representations, we fine-tuned our MLM-pretrained, short-context DNA-xLSTM models ... while the DNA-xLSTM-2M model was fine-tuned on the Nucleotide Transformers Tasks (Dalla-Torre et al., 2024) (Section 4.1)
  - [Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/60cefc59610f8f59ea10099f99a36726-Paper-Conference.pdf)
- **Generation diversity** (construct): *causes*, 1 paper
  > Introducing representation-level learning and architectural innovations infuses geometric inductive biases and effectively refines generation diversity. (Section 1)
  - [Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf)
