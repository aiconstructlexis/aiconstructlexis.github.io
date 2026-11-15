# Knowledge storage
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Information storage, Knowledge storage capacity  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage describes knowledge storage as a latent, internal property or mechanism of a model's parameters or weights, concerning how factual information is encoded and retained within the model. A smaller line of work uses the near-synonymous label "information storage" and makes the reference source explicit, framing it as facts from a pre-training dataset held in the model's "parametric" memory. A narrower formulation shifts from the mechanism itself to "knowledge storage capacity," defining it as the amount of factual information, measured in bits, that a model can store in its parameters and later retrieve.

**Space of facets.** The main distinction papers draw is between the storage mechanism and its capacity: some focus on the internal mechanisms and structures of storage, while another isolates how much factual information can be stored and retrieved. The terminology also overlaps, with "information storage" used for substantially the same idea and explicitly glossed as parametric memory. One paper further organizes the concept by layer, suggesting shallow layers play a central role in storing knowledge and retrieving information, whereas deeper layers are described as more useful for complicated computations than for storage.

**Space of measurement.** No measurement instrument is linked to this construct. One behavioral indicator, Hallucination, is connected to it, but that connection is framed as related rather than as a measurement. Papers also do not name a benchmark, human evaluation, LLM-as-a-judge, probe, or analysis that measures knowledge storage, although a capacity-focused definition specifies quantification in bits and later retrievability.

**Links.** A paper relates Hallucination to knowledge storage, stating that hallucination problems are "exacerbated by the enigmatic internal mechanisms of knowledge storage within language models." No causal or correlational links are reported.

## Sources

**Knowledge storage** (2 papers: [Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf), [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf))
> The internal mechanisms and structures by which a language model encodes and retains information within its parameters.

**Information storage** (1 paper: [Understanding Information Storage and Transfer in Multi-Modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf))
> The latent mechanism by which factual information from a pre-training dataset is encoded and retained within a model's parameters, also referred to as its parametric memory.

**Knowledge storage capacity** (1 paper: [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/26d3c9a66836ded8f34a944f2bfe868e-Paper-Conference.pdf))
> The amount of factual information, measured in bits, that a language model can store in its parameters and later retrieve.

## Relationships

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > They still struggle with issues such as hallucinations [5–7]... and these problems are exacerbated by the enigmatic internal mechanisms of knowledge storage within language models. (Introduction)
  - [Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf)
