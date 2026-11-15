# Conditional text generation
**Type:** Behavioral indicator  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is a task where a model produces a text response or completion conditioned on a provided input context or prompt. Definitions agree on that conditioning requirement, and one formulation describes it as generating "fluent and coherent text completions based on input contexts" (SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation). A smaller line of work frames it more generally as prediction from an arbitrary subset of input tokens, with outputs expected to respect and incorporate arbitrary contextual evidence.

**Variants.** Papers most often place this behavior in familiar conditional generation tasks, with text summarization and data-to-text generation treated as related settings. Another usage names specific generation modes, including CAR generation and arbitrary-context (AC) generation, where the model predicts using arbitrary context. One paper also contrasts relatively open-ended and strongly constrained conditional settings.

**Space of elicitation and scores.** The measurement evidence is narrow: papers link this behavior to one measurement instrument, the dataset ParaDetox. In that usage, ParaDetox appears in a study that contrasts datasets by how strong their conditional constraints are, and describes Paradetox as imposing the strongest constraints among those datasets. No other measurement instrument is linked by the papers.

**What it is taken as evidence of.** No construct is linked to conditional text generation as what it evidences. Instead, papers relate it to text summarization, data-to-text generation, and hallucination, all through related rather than evidential links.

## Sources

**Conditional text generation** (3 papers: [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [Tractable Transformers for Flexible Conditional Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ao/liu25ao.pdf))
> Producing fluent and coherent text completions based on provided input contexts.

## Relationships

### Conditional text generation →
- **ParaDetox** (measurement instrument): *measured_by*, 1 paper
  > In particular, we focus on two datasets that significantly differ in their level of conditional constraints: RocStories (Mostafazadeh et al., 2016), which is relatively open-ended, and Paradetox (Logacheva et al., 2022), which imposes the strongest conditional constraints (Section 5.1).
  - [Conditional [MASK] Discrete Diffusion Language Model](https://aclanthology.org/2025.emnlp-main.450.pdf)

### Associated with
- **Text summarization** (behavioral indicator), 1 paper
  > This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Data-to-text generation** (behavioral indicator), 1 paper
  > This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > Large Language Models (LLMs), when used for conditional text generation, often produce hallucinations, i.e., information that is unfaithful or not grounded in the input context. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
