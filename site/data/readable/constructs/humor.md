# Humor
**Type:** Construct  
**Supporting papers:** 7  

## State of the Field

**Space of definitions.** Across the definitions, humor is consistently treated as a stylistic alignment dimension: a model's tendency or ability to produce witty, amusing, or funny responses when that style is desired. The definitions largely agree on this framing, with only a mild shift in emphasis between model-level tendency or ability and response-level quality, and one formulation also presents humor as a secondary objective in generation.

**Space of facets.** In these papers, humor is positioned alongside helpfulness and harmlessness as one of the pre-defined dimensions, values, or objectives used in multi-objective alignment. The recurring organization is therefore not into subtypes of humor, but into a set of preference dimensions that may need to be balanced and can be described as sometimes conflicting; one paper further frames helpfulness as the primary objective while humor is the target reward.

**Space of measurement.** Humor is linked to one measurement instrument, HH-RLHF, and no behavioral indicators are linked to it. Papers describe this operationalization as using a large-scale dataset, or a task based on the Anthropic-HH dataset, together with open-sourced reward models on "Harmless," "Helpful," and "Humor" to score responses; in one setup, the baseline policy is aligned to helpfulness and humor is the target reward. This operationalization lines up with the definitions by treating humor as something evaluated in generated responses.

**Links.** Humor is linked to two constructs through related relationships: helpfulness is related to humor, and harmlessness is related to humor. Papers describe these links in the language of multi-dimensional human preferences, stating that dimensions such as helpfulness, harmlessness, and humor may need to be balanced, can be sometimes conflicting, and that aligning with one value could inadvertently diminish another.

## Sources

**Humor** (3 papers: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf), [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf), [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf))
> The tendency of a model to produce amusing or humorous responses when such style is desired.

## Relationships

### Humor →
- **HH-RLHF** (measurement instrument): *measured_by*, 2 papers
  > HH-RLHF [3]: a large-scale dataset ... We follow Yang et al. [35] and use open-sourced reward models on three objectives: "Harmless", "Helpful", and "Humor" to score the responses (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)

### Associated with
- **Helpfulness** (construct), 2 papers
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
- **Harmlessness** (construct), 2 papers
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
