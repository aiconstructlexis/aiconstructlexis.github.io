# Natural language reasoning
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Textual reasoning, Language reasoning, Text reasoning, Language-based reasoning, Linguistic reasoning capacity, Linguistic reasoning, Linguistic inference, Text-based reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats natural language reasoning, often under labels such as textual, language, or linguistic reasoning, as a latent model capability to understand, manipulate, and draw logical inferences from natural language or text. Many definitions describe reasoning over text-only inputs, language structure and meaning, or logical relationships between sentences and documents, and some broaden this to logically coherent or commonsensical response generation, including proposing plausible causes. A smaller line of work defines it more narrowly through the production of explanatory text and explicit step-by-step derivations, especially when models solve problems by generating a natural-language solution rather than relying on tools or code.

**Space of facets.** The label is not fully standardized: papers alternate among textual reasoning, language reasoning, linguistic reasoning, text reasoning, and text-based reasoning for closely related abilities, while one paper uses linguistic inference for a narrower grammatical version. One paper organizes text-based reasoning into subtypes such as semantic and pragmatic phenomena, and describes this category as relying on surface-level linguistic evidence in the premise and hypothesis without world knowledge. Other papers distinguish it from neighboring capacities such as OCR or transcription, tool manipulation, visual interpretation, captioning, and cross-modal retrieval, treating natural-language reasoning as the part that operates over the textual representation.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to it. The papers nonetheless describe several task-based assessments: one uses the XNLI benchmark for sentence entailment, others evaluate whether models can solve problems by generating natural-language solutions or explicit step-by-step reasoning, reason over transcribed text to produce an answer, detect and remove contradictions, or solve plausibility tasks from gold textual descriptions instead of images. So papers operationalize the construct either through text-only end tasks such as entailment, contradiction handling, and plausibility judgment, or through the model's ability to produce natural-language reasoning steps.

**Links.** One paper relates natural language reasoning to semantic reasoning and pragmatic understanding by placing both within a broader text-based reasoning category. In that account, the category covers explanations based only on surface-level linguistic evidence in the premise and hypothesis, without appealing to world knowledge.

## Sources

**Textual reasoning** (3 papers: [HLM-Cite: Hybrid Language Model Workflow for Text-based Scientific Citation Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/5635925cf9d2274f338eb0dd5971e845-Paper-Conference.pdf), [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf), [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf))
> The ability to comprehend and analyze textual content to discern complex, implicit relationships between documents.

**Natural language reasoning** (1 paper: [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf))
> The ability to solve problems by generating explanatory text and step-by-step derivations in human language.

**Language reasoning** (1 paper: [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf))
> The latent capability of a large language model to understand, manipulate, and draw logical inferences from natural language text.

**Text reasoning** (1 paper: [OmnixR: Evaluating Omni-modality Language Models on Reasoning across Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa3e67220ca4cd50010165c950fc8056-Paper-Conference.pdf))
> The ability to reason over extracted textual content and produce a final answer.

**Linguistic reasoning capacity** (1 paper: [PB-LLM: Partially Binarized Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3ab228c4703c4459b1a600ebadc5732c-Paper-Conference.pdf))
> The latent ability of a language model to understand and manipulate language in a logical or commonsensical way to perform complex tasks.

**Language-based reasoning** (1 paper: [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf))
> The inherent capability of LLMs to generate logically coherent and contextually appropriate responses based on linguistic patterns and prior knowledge, including proposing plausible causes for observed findings.

**Linguistic reasoning** (1 paper: [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf))
> The latent ability to process and manipulate language structure and meaning logically, including disentangling syntax from semantics and inferring entailments.

**Linguistic inference** (1 paper: [LingGym: How Far Are LLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.69.pdf))
> The capacity to draw correct conclusions about missing linguistic forms or glosses from contextual and grammatical evidence.

**Text-based reasoning** (1 paper: [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf))
> The ability to solve problems using only natural language to generate an explicit, step-by-step thought process.

## Relationships

### Associated with
- **Semantic reasoning** (construct), 1 paper
  > The first broad category, Text-Based (TB) Reasoning, includes explanations that depend solely on surface-level linguistic evidence found within the premise and hypothesis, without appealing to world knowledge. Six subtypes are defined: Coreference, Syntactic, Semantic, Pragmatic, Absence of Mention and Logic Conflict. (Section 3.1)
  - [LiTEx: A Linguistic Taxonomy of Explanations for Understanding Within-Label Variation in Natural Language Inference](https://aclanthology.org/2025.emnlp-main.1728.pdf)
- **Pragmatic understanding** (construct), 1 paper
  > The first broad category, Text-Based (TB) Reasoning, includes explanations that depend solely on surface-level linguistic evidence found within the premise and hypothesis, without appealing to world knowledge. Six subtypes are defined: Coreference, Syntactic, Semantic, Pragmatic, Absence of Mention and Logic Conflict. (Section 3.1)
  - [LiTEx: A Linguistic Taxonomy of Explanations for Understanding Within-Label Variation in Natural Language Inference](https://aclanthology.org/2025.emnlp-main.1728.pdf)
