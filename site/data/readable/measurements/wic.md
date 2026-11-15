# WiC
**Type:** Measurement instrument  
**Supporting papers:** 23  
**Also known as:** WIC  

## State of the Field

**What it is.** Across papers, WiC is most commonly described as the Word-in-Context dataset or benchmark for word sense disambiguation. The standard task framing is to decide whether a target word has the same meaning in two sentences or contexts, and some papers make this explicit as a binary classification setup; one study also notes that "all WiC datasets are class-balanced," giving a 50% chance baseline. A smaller line of work places WiC within SuperGLUE, and a few definitions describe it as evaluating polysemy disambiguation or context-sensitive word representations.

**What it is claimed to measure.** Papers link WiC to 3 behavioral indicators and no constructs. The prevailing usage is that WiC measures word sense disambiguation, often phrased as contextual word sense disambiguation. Only isolated papers treat it as measuring natural language inference or zero-shot task performance, so the measurement claims mostly converge on disambiguation despite a few alternative framings.

**Space of uses.** Papers commonly use WiC inside broader evaluation suites rather than describe it on its own. The only explicit instrument-level link relates it to SuperGLUE, and several definitions also place it among SuperGLUE tasks. In practice, papers frequently list it alongside SST-2, RTE, BoolQ, and WSC in shared task collections and comparison tables.

## Sources

**WiC** (15 papers: [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [Zeroth-Order Fine-Tuning of LLMs with Transferable Static Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/266983d0949aed78a16fa4782237dea7-Paper-Conference.pdf), [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf), [Language Models Can be Efficiently Steered via Minimal Embedding Layer Transformations](https://aclanthology.org/2025.emnlp-main.1170.pdf), [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf), [MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models](https://aclanthology.org/2025.emnlp-main.935.pdf), [MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines](https://aclanthology.org/2025.emnlp-main.1022.pdf), [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [Surprise Calibration for Better In-Context Learning](https://aclanthology.org/2025.emnlp-main.1175.pdf), [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf), [Making Language Models Robust Against Negation](https://aclanthology.org/2025.naacl-long.413.pdf))
> The Word-in-Context dataset, a benchmark for word sense disambiguation that involves determining if a word has the same meaning in two different sentences.

**WIC** (1 paper: [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf))
> A word-in-context benchmark requiring judgment of whether a word has the same meaning in two contexts.

## Relationships

### → WiC
- **Word sense disambiguation** (behavioral indicator): *measured_by*, 5 papers
  > word disambiguation: WiC (Pilehvar & Camacho-Collados, 2019); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **Natural language inference** (behavioral indicator): *measured_by*, 1 paper
  > Natural language inference: CB (De Marneff et al., 2019) and WiC (Pilehvar & Camacho-Collados, 2018) from superGLUE (Wang et al., 2019) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > “Table 1. Comparison of zero-evaluation performance... WIC ↑”
  - [MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25u/luo25u.pdf)

### Associated with
- **SuperGLUE** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... WiC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
