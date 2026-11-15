# Entity linking
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Entity alignment  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats entity linking as mapping entity mentions or names to canonical identifiers. One clinical formulation describes ICD coding as akin to entity linking, where disease mentions in a doctor’s diagnosis are assigned a set of unique ICD codes and extracted entities are linked to ICD entries by semantic similarity. Another formulation maps entities in generated logical forms to their corresponding mid-identifiers in a knowledge base using popularity and similarity scoring, while a smaller line of work uses closely related entity alignment language for pairing entities in separate multi-modal knowledge graphs that refer to identical real-world concepts.

**Variants.** Papers study this behavior in several settings and with overlapping names. One variant is clinical entity linking for automated ICD coding from diagnosis text, another is entity alignment in knowledge base question answering, where surface-form entities in logical forms are mapped to mids and candidate entities are selected with FACC1-based scoring, and another is multi-modal entity alignment, defined as matching 1-to-1 corresponding entities across distinct MMKGs that describe the same real-world concept.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, the papers operationalize the behavior through task-specific procedures, including semantic similarity to ICD dictionary entries for code assignment and popularity or similarity scoring, including FACC1-based candidate selection, for mapping entities to mid-identifiers.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not explicitly treat this behavior as evidence of a broader construct.

## Sources

**Entity linking** (1 paper: [RuCCoD: Towards Automated ICD Coding in Russian](https://aclanthology.org/2025.emnlp-main.129.pdf))
> The observable process of mapping disease mentions in clinical text to standardized ICD codes from a formal hierarchy.

**Entity alignment** (1 paper: [CompKBQA: Component-wise Task Decomposition for Knowledge Base Question Answering](https://aclanthology.org/2025.emnlp-main.16.pdf))
> Mapping surface-form entity names in generated logical forms to their canonical identifiers (mids) in the knowledge base using popularity and similarity scoring.
