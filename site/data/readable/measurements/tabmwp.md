# TabMWP
**Type:** Measurement instrument  
**Supporting papers:** 17  

## State of the Field

**What it is.** Most papers describe TabMWP as a benchmark or dataset for mathematical reasoning over tables, usually framed as table-based or tabular math word problems. The prevailing description is that each sample contains one table and one natural-language problem, and solving it requires understanding the problem text, extracting relevant information from the table, and performing calculations; several papers also describe the tables as semi-structured contextual input. A smaller line of work places it under structured data question answering, tabular question answering, or tabular data reasoning, and one paper describes it as an open-domain math word problem dataset containing tabular data.

**What it is claimed to measure.** Across the papers, TabMWP is linked to one construct and one behavioral indicator. The prevailing use is to measure mathematical reasoning, with papers listing it among math reasoning benchmarks or saying that it requires mathematical reasoning; a smaller usage treats it as measuring table question answering, specifically a tabular question-answering setting that requires reasoning over tabular contexts. Overall, the named measurement claims are concentrated mainly on mathematical reasoning rather than spread across many targets.

**Space of uses.** Papers often use TabMWP alongside GSM8k, MATH, SVAMP, ASDIV, and GSM-Hard, with several papers placing it inside broader evaluation suites with other math datasets. The dominant positioning is as one benchmark within larger evaluations of mathematical or structured reasoning; some papers present it as an out-of-distribution test, while others use it as a structured or tabular reasoning check, including numerical reasoning with few-shot demonstrations and settings where semi-structured tables provide the context.

## Sources

**TabMWP** (13 papers: [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [Sample Efficient Demonstration Selection for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/purohit25a/purohit25a.pdf), [CoCoA: Confidence- and Context-Aware Adaptive Decoding for Resolving Knowledge Conflicts in Large Language Models](https://aclanthology.org/2025.emnlp-main.348.pdf), [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for mathematical reasoning that requires processing information from tables to solve math word problems.

## Relationships

### → TabMWP
- **Mathematical reasoning** (construct): *measured_by*, 6 papers
  > We evaluated models on... TabMWP... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
- **Table question answering** (behavioral indicator): *measured_by*, 1 paper
  > "Lastly, we also test on a popular tabular question-answering dataset, TabMWP (Lu et al., 2023), that requires LLMs to use reasoning skills over tabular contexts."
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
