# Compositionality
**Type:** Construct  
**Supporting papers:** 40  
**Also known as:** Symbolic composition, Skill composition, Compositional capability, Compositional capabilities  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats compositionality as a latent ability or property that lets a model combine simpler elements, subproblems, or operations into correct, structured solutions for more complex tasks. Many definitions describe this as systematic combination, whether sentence meaning derived from constituents and composition rules, multi-step reasoning built from smaller sub-problems, or plans assembled from reusable components. Several papers use the term evaluatively, reporting worse performance as difficulty rises, a remaining compositionality gap on complex multi-hop questions, or a lack of compositional ability even with in-context learning. A smaller line of work narrows the term to symbolic composition in code, while other papers place it in learned action representations or algebraically composable model components.

**Space of facets.** Papers organize the construct by the units being composed: linguistic constituents and their structure, objects, attributes, and relations in multimodal settings, atomic reasoning steps, high-level actions or macro actions, and learned components such as expert vectors. They also use neighboring labels, including skill composition, symbolic composition, and compositional capability or capabilities, for abilities to combine simpler operations, concepts, or components into more complex solutions or meanings. Some authors distinguish compositionality from broader semantic and lexical understanding, or note that models can show compositional plausibility without conceptual coherence.

**Space of measurement.** Operationally, papers link compositionality to 4 measurement instruments and no behavioral indicators. All linked instruments are benchmarks: CREPE is used for systematicity and productivity, Winoground is used among challenging benchmarks for VLM compositionality, and BIG-Bench Hard is described as evaluating reasoning, compositionality, and generalization; ARC-AGI appears as a related benchmark setting where ARC tasks are treated as complex compositions of atomic operations. These measures mostly align with the dominant definitions by testing systematic combination and complex reasoning, though BIG-Bench Hard is described more broadly than compositionality alone.

**Links.** Individual papers claim causal relationships from compositionality to semantic understanding and to two forms of generalization. One paper also claims a causal relationship from modality gap to compositionality, describing poor compositionality in contrastive vision-language models. Separately, compositionality is reported as related to inductive reasoning and adaptability, and one related evaluation setting treats ARC tasks as complex compositions of atomic operations; no correlation link is reported.

## Sources

**Compositionality** (11 papers: [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [Conversational Drug Editing Using Retrieval and Domain Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/d390199c28b467315b454789b6584f19-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf), [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf), [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf), [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf), [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.185.pdf), [How Humans and LLMs Organize Conceptual Knowledge: Exploring Subordinate Categories in Italian](https://aclanthology.org/2025.acl-long.224.pdf), [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf), [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf))
> The degree to which a model can combine simpler subproblems into correct solutions for more complex problems as difficulty increases.

**Symbolic composition** (1 paper: [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf))
> The latent ability to compose multiple distinct concepts together using symbolic code, uniquely equipped in induction models.

**Skill composition** (1 paper: [Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the ARC Task](https://aclanthology.org/2025.naacl-long.423.pdf))
> The ability to combine multiple atomic operations or reasoning steps into a coherent solution for a complex task, reflecting compositional generalization in problem-solving.

**Compositional capability** (1 paper: [Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/petruzzellis25a/petruzzellis25a.pdf))
> The ability of a model to construct complex plans by combining simpler, reusable components (e.g., macro actions) in a structured and coherent way, reflecting systematic generalization across tasks.

**Compositional capabilities** (1 paper: [Circuit Complexity Bounds for RoPE-based Transformer Architecture](https://aclanthology.org/2025.emnlp-main.561.pdf))
> The ability to combine simpler computational or linguistic elements to form more complex structures and meanings.

## Relationships

### Compositionality →
- **CREPE** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on the CREPE benchmark (Ma et al., 2023) that focuses on systematicity (Fodor & Pylyshyn, 1988) and productivity (von Humboldt et al., 1988; Chomsky, 1956).
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Semantic understanding** (construct): *causes*, 1 paper
  > methods that improve compositionality of CLIP such as NegCLIP and CLIP-SVLC also achieve better performance on SUGARCREPE++ compared to CLIP, underscoring the importance of compositionality as a critical component for understanding semantic and lexical differences. (Section 3.1)
  - [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Out-of-distribution generalization** (construct): *causes*, 1 paper
  > Large language models can solve tasks that were not present in the training set. This capability is believed to be due to in-context learning and skill composition. (Abstract)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *causes*, 1 paper
  > “compositionality contributes significantly to zero-shot generalization”
  - [Human-Object Interaction Detection Collaborated with Large Relation-driven Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a54def490213ee10631b991c5acc6b5-Paper-Conference.pdf)
- **Winoground** (measurement instrument): *measured_by*, 1 paper
  > We use several challenging benchmarks, Winoground (Thrush et al., 2022), NaturalBench (Li et al., 2024), SeeTrue (Yarom et al., 2024), SugarCREPE (Hsieh et al., 2024), for assessing VLMs’ compositionality. (Section 2.1)
  - [Exploring How Generative MLLMs Perceive More Than CLIP with the Same Vision Encoder](https://aclanthology.org/2025.acl-long.499.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > BIG-Bench Hard (BBH; Srivastava et al., 2023; Suzgun et al., 2023) is a benchmark comprising 27 challenging tasks across 23 task types, designed to evaluate large language models on reasoning, compositionality, and generalization. (Section 5.1)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)

### → Compositionality
- **Modality gap** (construct): *causes*, 1 paper
  > The modality gap (Liang et al., 2022) is one of the primary factors contributing to the poor compositionality of contrastive vision-language models... (Section 6.1)
  - [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf)

### Associated with
- **Inductive reasoning** (construct), 1 paper
  > Inductive program synthesis excels at precise computations, and at composing multiple concepts (Abstract).
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Adaptability** (construct), 1 paper
  > While compositionality and scalability are crucial for effective adaptation, current LLM training methodologies fall short of achieving both these properties simultaneously. (Section 1)
  - [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf)
- **ARC-AGI** (measurement instrument), 1 paper
  > Therefore, we regard ARC tasks as complex compositions of atomic operations for evaluation. (Section 4.2)
  - [Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the ARC Task](https://aclanthology.org/2025.naacl-long.423.pdf)
