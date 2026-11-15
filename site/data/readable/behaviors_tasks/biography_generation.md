# Biography generation
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Factual biography generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats biography generation as producing a biographical passage, text, description, or summary about a named person from a prompt such as "Tell me a bio of <entity>." Most formulations are open-ended and focus on writing about a specific individual, sometimes described as relying on general world knowledge. A smaller line of work narrows the task to factual biography generation, defined as producing a written account of a person's life that adheres to known facts.

**Variants.** Papers study several variants and settings: long-form biography generation, paragraph-level generations, and a structured version that requires bullet point biographies. The named targets vary from a given entity or named individual to popular figures, celebrities, scientists, and famous computer scientists, and one paper describes using entities from the FactScore dataset. The main alternate label is factual biography generation.

**Space of elicitation and scores.** Papers link this behavior to two measurement instruments, most often Biography and then FActScore. Biography is used in fact verification and as a test set for biography generation, including an out-of-domain subset used for biography generation. FActScore is also used for biography.

## Sources

**Biography generation** (6 papers: [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf), [HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://aclanthology.org/2025.acl-long.71.pdf), [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf))
> Generating a biographical passage about a person from a prompt.

**Factual biography generation** (1 paper: [Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf))
> The task of producing a written account of a person's life that adheres to known facts.

## Relationships

### Biography generation →
- **Biography** (measurement instrument): *measured_by*, 2 papers
  > "Fact verification. We evaluate a biography-generation task (Min et al., 2023)"
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **FActScore** (measurement instrument): *measured_by*, 1 paper
  > We use FACTSCORE (Min et al., 2023) for biography. (Section 4.1)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
