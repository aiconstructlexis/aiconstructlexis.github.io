# Novelty
**Type:** Construct  
**Supporting papers:** 14  

## State of the Field

**Space of definitions.** Most commonly, papers use novelty to mean that generated content, hypotheses, or ideas contain fresh, non-redundant information relative to existing literature, retrieved material, or other generated outputs. In this usage, novelty is tied to whether a proposal is original rather than a restatement of existing ideas, or whether one hypothesis adds meaningfully new information beyond another. A narrower usage defines novelty as the dissimilarity of generated protein structures from known database structures, with greater novelty corresponding to lower similarity to known structures.

**Space of facets.** Where papers place novelty in a broader scheme, they usually treat it as one evaluation dimension among others rather than divide it into named subtypes. It appears alongside utility, clarity, and plausibility in hypothesis evaluation, alongside feasibility in research proposals and future research ideas, and alongside relevance, breadth, and depth in machine writing; one paper also frames novelty against redundancy. Across these uses, the same label covers both originality of generated ideas or text and structural dissimilarity in protein generation.

**Space of measurement.** The recorded measurement space links novelty to 2 measurement instruments, Human evaluation and LLM-as-a-judge, and to no behavioral indicators. Human evaluation is the more common linked instrument: papers use it to assess novelty of generated content and future research ideas, while a smaller line of work uses LLM-based metrics to score novelty. One paper also makes the operationalization explicit by comparing generated protein structures to known PDB structures with TMScore (pdb-TM), where lower values indicate greater novelty. These operationalizations mostly mirror the two main definitions, judgment of fresh non-redundant content on one side and dissimilarity from known structures on the other.

**Links.** No causal, correlational, or generic related links are recorded for novelty. The only recorded relationships are that novelty is measured by Human evaluation and by LLM-as-a-judge.

## Sources

**Novelty** (4 papers: [DPLM-2: A Multimodal Diffusion Protein Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/57c30b677add9aa78e1745f0643104d0-Paper-Conference.pdf), [Literature Meets Data: A Synergistic Approach to Hypothesis Generation](https://aclanthology.org/2025.acl-long.12.pdf), [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf), [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.50.pdf))
> The degree to which generated protein structures are dissimilar from known, existing structures in protein databases.

## Relationships

### Novelty →
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > we also assess the intrinsic quality of the generated content. Specifically, we focus on two key dimensions: novelty and feasibility...human evaluation includes results on 40 of them. (Section 10, Table 4)
  - [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf)
  - [Can Large Language Models Unlock Novel Scientific Research Ideas?](https://aclanthology.org/2025.emnlp-main.1704.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > In addition to assessing the effectiveness of hypotheses in downstream task usage, we also evaluate their helpfulness (Liu et al., 2024) and novelty (Liu et al., 2024; Si et al., 2024) through LLM-based metrics. (Section 4.2)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
