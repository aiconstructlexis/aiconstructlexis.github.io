# SNLI
**Type:** Measurement instrument  
**Supporting papers:** 25  

## State of the Field

**What it is.** Most papers describe SNLI as the Stanford Natural Language Inference dataset or benchmark, a large-scale corpus of sentence pairs for textual entailment or natural language inference. One paper explicitly states that it labels pairs of strings as entailment, neutral, or contradiction, and another describes it more specifically as using image captions as premises paired with hypotheses elicited from crowdworkers. Some papers work with adapted versions or slices, including entailment-only pairs, SNLI-TEST-SAMPLE original examples, and negation benchmarks for SNLI.

**What it is claimed to measure.** Across papers, the prevailing use is to measure natural language inference, which is also the most frequently linked behavioral indicator. Papers link SNLI to two behavioral indicators and two constructs overall: it measures natural language inference most often, one paper also uses it to measure multiple-choice question answering, and papers additionally use it to measure generalization and logical consistency. The reported uses therefore cluster around NLI, while the construct-level links are divided between generalization and logical consistency.

**Space of uses.** No measurement instrument is linked to it. In use, papers commonly place SNLI inside broader evaluation suites alongside MNLI, RTE, SST-2, QNLI, and OpenbookQA, with several other tasks also listed, and some frame it as an additional or out-of-domain evaluation task. A smaller set of papers uses more specific SNLI-based setups, such as restricting evaluation to entailment-only pairs, benchmarking on SNLI-TEST-SAMPLE original examples, or combining SNLI with MNLI and synthetic data to generate logical inconsistency stimuli.

## Sources

**SNLI** (11 papers: [Meaning Representations from Trajectories in Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ac1887299ee703ba4e54f8c102161213-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82cc56a5fa0287c438baa8be65a70-Paper-Conference.pdf), [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf), [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf), [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf), [Making Language Models Robust Against Negation](https://aclanthology.org/2025.naacl-long.413.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25t/liu25t.pdf), [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf))
> The Stanford Natural Language Inference dataset, a large-scale corpus for evaluating textual entailment.

## Relationships

### → SNLI
- **Natural language inference** (behavioral indicator): *measured_by*, 2 papers
  > SNLI (Bowman et al., 2015) is an NLI inference task dataset with 10K samples and 3 labels – entailment, neutral and contradiction. (Section 3)
  - [Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf)
  - [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **Logical consistency** (construct): *measured_by*, 1 paper
  > we evaluate their logical consistency between each original SNLI instance and its corresponding sub-problems.
  - [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
