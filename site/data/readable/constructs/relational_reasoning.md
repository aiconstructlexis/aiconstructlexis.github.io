# Relational reasoning
**Type:** Construct  
**Supporting papers:** 18  
**Also known as:** Relation reasoning, Relational inference, Implicit relation inference  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats relational reasoning as the ability to understand and operate on abstract relationships while being independent of the specific identity, or in some definitions the absolute properties, of the symbols or stimuli involved. Some papers keep this abstract framing and describe evaluation with unseen symbols, while others define it more concretely as reasoning over structured entity relations, such as multi-hop constraints in knowledge graphs, primary-foreign key links and dependencies in databases, or explicit interactions and counterfactual dependencies among entities. A smaller line of work uses nearby labels for reasoning about relations in visual or multimodal scenes, shopping concept compatibility, or relations that are implicit in text rather than explicitly stated, and some authors frame it as a latent model ability whereas others use it for task-specific reasoning in particular domains.

**Space of facets.** Papers do not present a single shared breakdown of the construct, but they repeatedly organize it by the kind of relation being handled. The recurring facets are abstract symbolic relations, multi-hop and constraint-based relations in structured data, subject relations and attributes in images, explicit interactions and counterfactual dependencies among entities, compatibility relations between shopping concepts, and implicit relations inferred across sentences. The naming is also uneven: closely related usages appear under relational reasoning, relation reasoning, relational inference, and implicit relation inference, with some papers using these labels for a broad ability and others for narrower domain-specific forms.

**Space of measurement.** Operationalization is benchmark-based: papers link relational reasoning to 3 measurement instruments and 3 behavioral indicators. The named instruments are CLUTRR, described as a benchmark based on human-written stories about family relations, GQA, used to test relational reasoning in general visual question answering, and MEBench, whose relational questions target explicit interactions and counterfactual dependencies among entities. The linked behavioral indicators are Document-level relation extraction, Intent classification, and Visual question answering, although papers present these as related task settings rather than direct measures. Overall, the measurements make the construct observable as performance on relation-heavy tasks, while many definitions describe a broader abstract or latent reasoning ability.

**Links.** One paper claims a causal relationship from relational reasoning to Abstraction and to Systematic generalization, stating that it is believed to underlie those abilities. Other papers say it is related to Visual question answering, where it appears alongside multimodal understanding capabilities, to Document-level relation extraction, where implicit relations require relational reasoning for identification, and to Intent classification, where authors call for relational reasoning methods focused on fine-grained multimodal semantics. No correlational links are reported.

## Sources

**Relational reasoning** (6 papers: [When can transformers reason with abstract symbols?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a78459dbbcdc90783d183999e72176c-Paper-Conference.pdf), [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf), [MLPs Learn In-Context on Regression and Classification Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/62302a24b04589f9f9cdd5b02c344b6c-Paper-Conference.pdf), [Large Language Models are Good Relational Learners](https://aclanthology.org/2025.acl-long.386.pdf), [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf), [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.77.pdf))
> The ability to understand and operate on abstract relationships between symbols, independent of the specific identity of those symbols.

**Relation reasoning** (2 papers: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf))
> The ability to reason about relationships among entities in visual scenes and multimodal contexts.

**Relational inference** (1 paper: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to reason about the compatibility and interactions between different shopping concepts, such as between product categories and attributes.

**Implicit relation inference** (1 paper: [DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement](https://aclanthology.org/2025.emnlp-main.398.pdf))
> Inferring relationships between entities that are not explicitly stated in the text but can be deduced from context, such as deducing (cat, near, window) from 'The cat is on the mat' and 'The mat is under the window'.

## Relationships

### Relational reasoning →
- **GQA** (measurement instrument): *measured_by*, 1 paper
  > for general VQA tasks, we use ... GQA (Hudson & Manning, 2019) to test ... relational reasoning. (Section 4.1)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **CLUTRR** (measurement instrument): *measured_by*, 1 paper
  > CLUTRR (Sinha et al., 2019) is a relational reasoning benchmark based on human-written stories about family relations. (Section 4.1)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
- **Abstraction** (construct): *causes*, 1 paper
  > Relational reasoning is a central component of generally intelligent systems and is believed to underlie human abilities for abstraction and systematic generalization (Section 1).
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
- **Systematic generalization** (construct): *causes*, 1 paper
  > Relational reasoning is a central component of generally intelligent systems and is believed to underlie human abilities for abstraction and systematic generalization (Section 1).
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
- **MEBench** (measurement instrument): *measured_by*, 1 paper
  > Our benchmark comprises 4,780 questions which are systematically categorized into three primary categories: Comparative Reasoning, Statistical Reasoning and Relational Reasoning, further divided into eight distinct types, ensuring broad coverage of real-world multi-entity reasoning scenarios.
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.77.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > This question tests the model’s multimodal understanding capabilities, such as visual perception and relational reasoning. (Introduction)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Document-level relation extraction** (behavioral indicator), 1 paper
  > Document-level RE poses greater challenges than sentence-level RE counterpart, primarily due to the presence of numerous implicit relations that require relational reasoning for identification. (Section 1. Introduction)
  - [DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf)
- **Intent classification** (behavioral indicator), 1 paper
  > Consequently, there is a need for relational reasoning methods concentrating on fine-grained semantics for multimodal intent recognition... (Introduction)
  - [LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1130.pdf)
