# ASDiv
**Type:** Measurement instrument  
**Supporting papers:** 37  
**Also known as:** ASDIV, Asdiv  

## State of the Field

**What it is.** Across the papers, ASDiv is most commonly described as a benchmark, dataset, or corpus of diverse arithmetic or math word problems used in reasoning evaluation. Definitions emphasize diversity in problem types, operations, and difficulty levels, and one paper further describes it as an English math word problem corpus with 2,305 instances typically found in elementary schools. A smaller line of work frames it as an out-of-distribution or out-of-domain benchmark or as a held-out test set, and papers vary in its expanded name, including A Set of Diverse Math Word Problems, Another Solved Dataset of Diverse Word Problems, and Another Simple Math Word Problem Set.

**What it is claimed to measure.** Papers link ASDiv to 3 constructs and 1 behavioral indicator. The prevailing usage is to measure Mathematical reasoning, with many papers listing it among math reasoning benchmarks or using it to assess mathematical reasoning aptitude. Smaller uses report it as measuring the behavioral indicator Mathematical problem solving and the constructs Reasoning and Generalization, and the claims overall converge mainly on Mathematical reasoning rather than being evenly spread across many targets.

**Space of uses.** In use, papers usually place ASDiv inside larger benchmark suites rather than as a standalone protocol. It commonly appears alongside GSM8K, SVAMP, MATH, TabMWP, and MAWPS, and several papers position it specifically as an out-of-distribution, out-of-domain, or held-out evaluation set for testing generalization.

## Sources

**ASDIV** (4 papers: [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf))
> A Set of Diverse Math Word Problems, a benchmark containing math problems across various types and difficulty levels to assess robustness in mathematical reasoning.

**ASDiv** (9 papers: [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf), [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf), [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf), [MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dp/li25dp.pdf), [Superficial Self-Improved Reasoners Benefit from Model Merging](https://aclanthology.org/2025.emnlp-main.301.pdf))
> A benchmark dataset of diverse math word problems for assessing arithmetic reasoning.

**Asdiv** (2 papers: [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf), [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf))
> An out-of-distribution benchmark dataset of diverse math word problems.

## Relationships

### → ASDiv
- **Mathematical reasoning** (construct): *measured_by*, 17 papers
  > We evaluated models on... ASDIV... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
  - [No Need for Explanations: LLMs can implicitly learn from mistakes in-context](https://aclanthology.org/2025.emnlp-main.1686.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 3 papers
  > ...GSM-Plus [18], MATH, TheoremQA [6], SVAMP [28], and ASDiv [22] for math. (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > Additionally, we include two mathematical reasoning datasets, i.e., SVAMP [12] and ASDiv [18], to evaluate the out-of-domain generalizability of the models fine-tuned on the data generated from GSM8K and MATH datasets.
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
