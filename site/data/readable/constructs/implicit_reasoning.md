# Implicit reasoning
**Type:** Construct  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** The only explicit definition treats it as a model capacity for recovering what is not said directly: inferring unstated assumptions, background knowledge, and indirect logical connections needed to interpret ambiguous or incompletely specified argumentative content. This usage is illustrated by descriptions of using different background knowledge to complement implicit information, and by the claim that a model can sometimes identify implicit logic that annotators did not realize. A separate usage overlaps it with multi-hop reasoning, describing implicit reasoning as solving multi-hop reasoning tasks in a single forward pass, without chain of thought.

**Space of facets.** The papers do not divide it into named subtypes. The main difference across uses is scope and framing: one centers on interpreting argumentative content and identifying logical structure from implicit information, while another frames the construct through multi-hop task solving in a single forward pass. Papers also place it alongside broader constructs rather than under a stable taxonomy, especially multi-hop reasoning, and one paper relates it to social intelligence through information reasoning alongside goal completion.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Instead, papers describe it through task behaviors such as inferring unstated assumptions, drawing on background knowledge to fill in implicit information, identifying implicit logic, or solving multi-hop reasoning in a single forward pass without chain of thought.

**Links.** Some papers claim a causal relationship from Grokking to implicit reasoning, stating that transformers can learn implicit reasoning only through grokking and that grokking-based data augmentation can unlock implicit multi-hop reasoning capabilities. Papers also report that implicit reasoning is related to Multi-hop reasoning, with one claim that it aligns closely with multi-hop reasoning and another that defines it through single-pass solution of multi-hop tasks without chain of thought. One paper further reports that implicit reasoning is related to Social intelligence in an evaluation that considers both goal completion and information reasoning.

## Sources

**Implicit reasoning** (1 paper: [Identification of Multiple Logical Interpretations in Counter-Arguments](https://aclanthology.org/2025.emnlp-main.326.pdf))
> The model's capacity to infer unstated assumptions, background knowledge, or indirect logical connections necessary to interpret ambiguous or incompletely specified argumentative content.

## Relationships

### → Implicit reasoning
- **Grokking** (construct): *causes*, 2 papers
  > transformers can learn implicit reasoning, but only through grokking, i.e., extended training far beyond overfitting.
  - [Grokking of Implicit Reasoning in Transformers: A Mechanistic Journey to the Edge of Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad217e0c7fecc71bdf48660ad6714b07-Paper-Conference.pdf)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)

### Associated with
- **Multi-hop reasoning** (construct), 2 papers
  > This property aligns closely with our focus on multi-hop reasoning and underscores the need for implicit reasoning capability (Section 1).
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [Language models can learn implicit multi-hop reasoning, but only if they have lots of training data](https://aclanthology.org/2025.emnlp-main.490.pdf)
- **Social intelligence** (construct), 1 paper
  > We evaluate social intelligence from multiple aspects, considering both goal completion and information reasoning... (Section 1).
  - [AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios](https://aclanthology.org/2025.naacl-long.257.pdf)
