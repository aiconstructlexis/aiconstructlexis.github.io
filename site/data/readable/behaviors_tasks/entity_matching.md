# Entity matching
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Cross-lingual product alignment  

## State of the Field

**Space of definitions.** Across the surveyed definitions, the prevailing usage treats entity matching as deciding whether entities from different knowledge graphs refer to the same real-world entity. A smaller formulation presents the same behavior as cross-lingual product alignment: given product metadata, the task is to select the corresponding product metadata in another language. The success criterion is therefore described either as correctly identifying co-referring entities across knowledge graphs or as selecting the matching product entry across languages.

**Variants.** Papers use at least two task names for this behavior. One is "Entity Matching Across KGs," framed around matching entities across different knowledge graphs; another is "Cross-lingual Product Alignment," framed around product metadata in different languages. The descriptions focus on these KG-based and cross-lingual product settings.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers, the behavior is operationalized directly through task prompts or task descriptions, either by asking whether entities across knowledge graphs match or by asking a model to select matching product metadata in another language.

**What it is taken as evidence of.** Only one construct is linked to it. Rather than treating entity matching as evidence of that construct, one paper claims a causal relationship from Semantic understanding to Entity matching, stating that language models provide "advanced semantic understanding" for tasks like EA. No other construct links are present.

## Sources

**Entity matching** (1 paper: [KG-FIT: Knowledge Graph Fine-Tuning Upon Open-World Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/f606d45ae7b991988b6eea2af38b7057-Paper-Conference.pdf))
> Identifying whether entities from different knowledge graphs refer to the same real-world entity.

**Cross-lingual product alignment** (1 paper: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying the same product across different languages based on its metadata.

## Relationships

### → Entity matching
- **Semantic understanding** (construct): *causes*, 1 paper
  > “LMs provide advanced semantic understanding to build and refine KGs through tasks like EA.”
  - [How do Language Models Reshape Entity Alignment? A Survey of LM-Driven EA Methods: Advances, Benchmarks, and Future](https://aclanthology.org/2025.emnlp-main.1184.pdf)
