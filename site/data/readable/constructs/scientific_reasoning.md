# Scientific reasoning
**Type:** Construct  
**Supporting papers:** 43  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats scientific reasoning as an ability to reason about scientific concepts and questions, usually with domain-specific knowledge and multi-step inference. Many definitions make this concrete as reasoning over scientific data, figures, or other multimodal evidence, or as answering science questions, while some broaden it to long-context scientific content, research problems that combine knowledge recall, reasoning, and code synthesis, or the interpretation of scientific evidence so as to avoid unjustified conclusions. A smaller line of work extends the label to the scientific process itself, including inference from data, hypothesis formulation, and discovery in a controlled physics-based environment.

**Space of facets.** The clearest explicit scheme places scientific reasoning alongside algebraic reasoning, arithmetic reasoning, geometry reasoning, logical reasoning, numeric common sense, and statistical reasoning as one of seven mathematical reasoning types. Across other papers, the same label is used for somewhat different scopes, including academic paper figures, science question answering, long-context understanding, research coding, and evidence-grounded interpretation. Several papers also pair it with neighboring capacities such as understanding, knowledge recall, and discovery.

**Space of measurement.** Operationalization is concentrated in 5 linked measurement instruments, all benchmarks: ARC-Challenge and ARC for scientific reasoning questions, ScienceQA for scientific multimodal reasoning through multiple-choice questions, SciQ for applying scientific concepts beyond mere fact recall, and SciBench for complex, multi-step scientific questions that integrate knowledge, evidence, and scientific principles. Papers therefore make the construct observable mainly as performance on science question answering and reasoning tasks. They also link it to 2 behavioral indicators, Scientific problem solving and Task decomposition, but those links are causal or related rather than measured_by. This operationalization most directly reflects definitions that cast scientific reasoning as multi-step scientific question answering, while some definitions extend further to academic figures, long-context reasoning, evidence interpretation, and hypothesis formulation.

**Links.** Beyond measurement, one paper claims a causal relationship from Scientific reasoning to Scientific problem solving. Scientific reasoning is also related to Task decomposition in one paper, where proposing novel subgoals is discussed in connection with enhanced scientific reasoning. Another paper relates it to Commonsense reasoning as a contrast, stating that commonsense logic captured by popular language datasets largely deviates from scientific reasoning that requires math and physics backgrounds.

## Sources

**Scientific reasoning** (9 papers: [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [SciCode: A Research Coding Benchmark Curated by Scientists](https://proceedings.neurips.cc/paper_files/paper/2024/file/36850592258c8c41cecdaa3dea5ff7de-Paper-Datasets_and_Benchmarks_Track.pdf), [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf), [Grounding Fallacies Misrepresenting Scientific Publications in Evidence](https://aclanthology.org/2025.naacl-long.491.pdf), [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf), [Gravity-Bench-v1: A Benchmark on Gravitational Physics Discovery for Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/koblischke25a/koblischke25a.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf))
> The ability to reason about scientific concepts, data, and figures, particularly in academic or research contexts involving complex visualizations.

## Relationships

### Scientific reasoning →
- **ARC-Challenge** (measurement instrument): *measured_by*, 3 papers
  > we evaluate the proposed TOW on ... ARC-Challenge (Clark et al., 2018) for scientific reasoning.
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf)
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.759.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 2 papers
  > We use the ScienceQA dataset (Lu et al., 2022) to evaluate the scientific reasoning ability of the model. (Section 3.1)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **SciQ** (measurement instrument): *measured_by*, 2 papers
  > SciQ measures scientific reasoning, challenging models to apply scientific concepts beyond mere fact recall. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 2 papers
  > We evaluate RATIONALYST across diverse reasoning tasks including ... scientific (ARC (Clark et al., 2018)) (Section 4.2)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [IG-Pruning: Input-Guided Block Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.537.pdf)
- **SciBench** (measurement instrument): *measured_by*, 2 papers
  > Tree-Search policy which are compared on college-level scientific reasoning benchmark under three LLMs, such as CoT and ToT, as shown in Table 4. We also evaluated under the same search budget on MATH and SciBench
  - [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Scientific problem solving** (behavioral indicator): *causes*, 1 paper
  > all models substantially improve performance when background is provided, indicating their lack of knowledge and reasoning capability in these natural science fields. (Section 2.4)
  - [SciCode: A Research Coding Benchmark Curated by Scientists](https://proceedings.neurips.cc/paper_files/paper/2024/file/36850592258c8c41cecdaa3dea5ff7de-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Task decomposition** (behavioral indicator), 1 paper
  > PDE-Controller ... enhances scientific reasoning by proposing novel subgoals to improve open-loop control utility. (Section 1)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)
- **Commonsense reasoning** (construct), 1 paper
  > commonsense logic captured by popular language datasets (Gao et al., 2020; Weber et al., 2024) largely deviates from scientific reasoning that requires math and physics backgrounds, leading to poor performance (Table 4 and 9). (Section 1)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)
