# Indirect object identification
**Type:** Behavioral indicator  
**Supporting papers:** 8  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is a sentence completion or final-token prediction behavior in which the model must output the indirect object from syntactic and semantic context. Most descriptions use prompts with two names where one name is repeated, and success means producing the non-repeated recipient name rather than the repeated subject name, as in prompts like “When Mary and John went to the store, John gave a book to” with intended completion “Mary.” One paper states this directly: “The IOI task is to predict the final token in the sentence to be the IO” (Towards Best Practices of Activation Patching in Language Models: Metrics and Methods).

**Variants.** The main setting is the IOI task with sentence prompts built around paired names and a transfer event, sometimes described as a name-swapping sentence. Papers vary the surface examples, such as giving a snack, a book, or a bottle of milk, but the recurring pattern is the same: two names appear, one is repeated, and the model should produce the other name, called “the IO name” in one paper.

**Space of elicitation and scores.** Papers link this behavior to 1 measurement instrument, the IOI task. In the recorded work, this task-style instrument measures the behavior through the same sentence completion or final-token prediction setup used in the definitions, so elicitation and assessment are both tied to whether the model produces the indirect object name.

**What it is taken as evidence of.** Across the papers, the only construct link is to In-context reasoning. The recorded relationship is that In-context reasoning is related to indirect object identification, with a paper listing IOI among examples of reasoning it considers, rather than presenting a measurement, correlational, or causal claim about a broader set of constructs.

## Sources

**Indirect object identification** (4 papers: [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf), [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf), [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf), [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf))
> The observable behavior of correctly predicting the indirect object in a sentence based on syntactic and semantic context (e.g., identifying 'Mary' as the recipient in 'John gave a book to Mary').

## Relationships

### Indirect object identification →
- **IOI task** (measurement instrument): *measured_by*, 1 paper
  > In Wang et al. (2022), the authors analyze how the decoder-only transformer language model GPT-2 Small (Radford et al., 2019) performs the Indirect Object Identification (IOI) task. (Section 3)
  - [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf)

### Associated with
- **In-context reasoning** (construct), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: ... • Indirect object identification (IOI) (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
