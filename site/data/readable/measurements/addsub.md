# AddSub
**Type:** Measurement instrument  
**Supporting papers:** 18  

## State of the Field

**What it is.** Across the surveyed work, the dominant framing treats AddSub as an arithmetic word-problem dataset or benchmark centered on addition and subtraction. Definitions repeatedly describe it as containing addition and subtraction word problems for arithmetic, basic operational reasoning, or basic mathematical reasoning, and one evaluation section describes it as containing simple math word problems on addition and subtraction. One paper additionally frames it as a near-shift out-of-distribution benchmark, while another uses it as a seed dataset and as a well-defined evaluation set within PMC.

**What it is claimed to measure.** Papers use AddSub mainly to measure Mathematical reasoning. It is linked to 1 construct and 1 behavioral indicator: the construct is Mathematical reasoning, which papers evaluate through arithmetic datasets and mathematical reasoning testbeds, and the behavioral indicator is Mathematical problem solving, which one paper measures with AddSub as part of a more general benchmark suite. The reported measurement claims therefore converge on Mathematical reasoning rather than spreading across many targets.

**Space of uses.** Most papers use AddSub as one dataset within multi-dataset evaluations, commonly alongside GSM8K, SVAMP, MultiArith, SingleEq, and AQuA. In these studies it is positioned as an arithmetic reasoning dataset, sometimes selected among datasets of different difficulty and sometimes treated as an out-of-distribution or near-shift evaluation set. One paper also uses it as a seed dataset to construct PMC and as one of PMC's original four well-defined subsets.

## Sources

**AddSub** (7 papers: [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf), [Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf), [AdaDHP: Fine-Grained Fine-Tuning via Dual Hadamard Product and Adaptive Parameter Selection](https://aclanthology.org/2025.acl-long.467.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf), [LoRACoE: Improving Large Language Model via Composition-based LoRA Expert](https://aclanthology.org/2025.emnlp-main.1594.pdf), [VCSearch: Bridging the Gap Between Well-Defined and Ill-Defined Problems in Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.642.pdf))
> A dataset of arithmetic word problems involving addition and subtraction, used as a near-shift out-of-distribution benchmark.

## Relationships

### → AddSub
- **Mathematical reasoning** (construct): *measured_by*, 8 papers
  > We select eleven mathematical reasoning datasets... while the OOD datasets include GSM8K, SVAMP, AddSub, SingleEq, SingleOp, and MATH. (Section 2.2)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
