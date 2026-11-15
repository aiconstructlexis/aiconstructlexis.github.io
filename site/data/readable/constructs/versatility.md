# Versatility
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Conversational versatility, Skill repertoire  

## State of the Field

**Space of definitions.** Most definitions treat versatility as breadth: a model's ability to perform well or successfully across a wide and diverse range of tasks and domains. Smaller variants keep that breadth framing but narrow the setting, either to conversational versatility, the ability to handle diverse open-ended instruction-following queries across benchmark categories, or to a generalist agent's skill repertoire, the breadth and diversity of goal-directed capabilities for varied real-world user requests. One usage also makes compatibility with augmentation explicit, stating that retrieval can improve factual accuracy without hurting versatility, while indiscriminate retrieval can diminish it.

**Space of facets.** Papers do not build a broader construct hierarchy around versatility, and no linked constructs equate it with or place it under another construct. Instead, the concept is organized through neighboring labels tied to setting: conversational versatility for open-ended instruction-following benchmarks, and skill repertoire for agents with many goal-directed abilities. In biomedical use, the term is attached to doing well on multiple tasks over 8 modalities.

**Space of measurement.** Direct operationalization is narrow: versatility is linked to 1 measurement instrument and 3 behavioral indicators. The only named instrument is MT-Bench, described as a benchmark used to assess conversational versatility across a diverse range of queries. Beyond that, one paper presents strong performance in visual question answering, medical report generation, and medical image classification over 8 modalities as showcasing versatility. These operationalizations largely follow the prevailing breadth-across-tasks framing, although only the conversational variant is directly tied to a named benchmark.

**Links.** No papers claim a causal relationship or a correlation for versatility. One paper reports that versatility is related to visual question answering, and that medical report generation and medical image classification are related to versatility, using a single result statement about best performance across those tasks over 8 modalities.

## Sources

**Versatility** (2 papers: [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf))
> The ability of a model to perform well across a wide range of different tasks and domains without its capabilities being hindered by augmentations like retrieval.

**Conversational versatility** (1 paper: [AMPO: Active Multi Preference Optimization for Self-play Preference Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25c/gupta25c.pdf))
> The breadth of a model's ability to handle diverse open-ended instruction-following queries across different benchmark categories.

**Skill repertoire** (1 paper: [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf))
> The breadth and diversity of goal-directed capabilities an agent can perform, which enables it to handle a wide range of real-world user requests.

## Relationships

### Versatility →
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > These benchmarks are commonly used in the community to assess the conversational versatility of models across a diverse range of queries. (Section 8.1)
  - [AMPO: Active Multi Preference Optimization for Self-play Preference Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25c/gupta25c.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **Medical report generation** (behavioral indicator), 1 paper
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **Medical image classification** (behavioral indicator), 1 paper
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
