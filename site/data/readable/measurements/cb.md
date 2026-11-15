# CB
**Type:** Measurement instrument  
**Supporting papers:** 14  

## State of the Field

**What it is.** Across the papers, CB is most commonly described as CommitmentBank, a SuperGLUE natural language inference or textual entailment task, dataset, or benchmark built around short premise-hypothesis pairs or short texts. The prevailing descriptions frame it as evaluating entailment, with some definitions adding whether a sentence or statement commits the author to a belief or entailment, one definition specifying entailment, contradiction, or neutrality, and another highlighting pragmatic inference. A smaller usage treats it more broadly as a general NLU task for textual entailment or related classification evaluation.

**What it is claimed to measure.** In the reported literature, CB is only claimed to measure one behavioral indicator, Natural language inference, and it is not tied to any construct. That use converges on NLI rather than spreading across several targets, sometimes stated as textual entailment and, in one definition, textual entailment with an emphasis on pragmatic inference.

**Space of uses.** Papers usually use CB as one task within larger evaluation bundles rather than in isolation. The only instrument relationship reported for CB is a related link to SuperGLUE, and papers commonly place it alongside other SuperGLUE tasks such as BoolQ, COPA, RTE, and WiC, while some also include it in broader NLU or fine-tuning task sets.

## Sources

**CB** (8 papers: [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf), [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf), [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf), [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf))
> A textual entailment benchmark used to evaluate natural language inference on short premise-hypothesis pairs.

## Relationships

### → CB
- **Natural language inference** (behavioral indicator): *measured_by*, 2 papers
  > Natural language inference: CB (De Marneff et al., 2019) and WiC (Pilehvar & Camacho-Collados, 2018) from superGLUE (Wang et al., 2019) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)

### Associated with
- **SuperGLUE** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... CB”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
