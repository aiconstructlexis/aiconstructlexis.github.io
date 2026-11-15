# ChemProt
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Most commonly described as a labeled biomedical dataset for identifying chemical-protein interactions in scientific literature, papers frame ChemProt as a relation extraction, relation/classification, or text classification dataset. One description specifies five relation classes, while a smaller line of work treats it as a named entity detection source with annotations for chemical compounds and gene or protein-related objects, and derives ChemProt-Chem and ChemProt-Gene for detecting chemicals and genes.

**What it is claimed to measure.** Papers link ChemProt to one behavioral indicator and no constructs. The recorded measurement claim is concentrated on relation extraction: one paper reports that Relation extraction is measured by ChemProt, describing it as a chemical-protein dataset featuring five relation classes.

**Space of uses.** In the reported uses, ChemProt appears with other biomedical datasets in evaluation and as a downstream domain adaptation task. Papers place it alongside RCT, PubMedQA, MQP, and USMLE, and another paper repurposes it for named entity detection through derived subsets for chemicals and genes.

## Sources

**ChemProt** (5 papers: [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf), [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.518.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf))
> A labeled biomedical relation/classification dataset used as one of the downstream domain adaptation tasks.

## Relationships

### → ChemProt
- **Relation extraction** (behavioral indicator): *measured_by*, 1 paper
  > ChemProt is a chemical-protein dataset featuring five relation classes (Taboureau et al., 2010). (Section 5.1)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
