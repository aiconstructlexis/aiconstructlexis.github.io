# Task generalization
**Type:** Construct  
**Supporting papers:** 31  
**Also known as:** Cross-task generalization, Multi-task generalization, Generalization to new tasks, Generalization to unseen tasks, Task-level generalization, Unseen task generalization, Cross-task knowledge transfer  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats task generalization as the ability of a model or method to transfer learned capabilities to unseen or different tasks without task-specific fine-tuning or prior task knowledge. Most definitions describe doing well on new target tasks, task categories, or datasets after training on other tasks, sometimes in zero-shot or few-shot settings and sometimes from instructions alone. A smaller line of work narrows the scope to settings such as image processing, gaming scenarios, embodied agents, robotic policies, or time-series QA, while some papers broaden the referent from models to evaluation methods or parameter initialization methods. Definitions also differ on what the transfer spans, including tasks, prompts, domains, function classes, or downstream task types, and on whether the emphasis is latent ability, broad conceptual understanding, or observed effectiveness.

**Space of facets.** Papers use several nearby labels for overlapping ideas, most often cross-task generalization and multi-task generalization, alongside task-level generalization, unseen-task generalization, and generality. In these formulations, the construct is variously cast as knowledge transfer from source to target tasks, maintaining performance across multiple tasks within a unified architecture, or covering an entire function class after training on only a subset of tasks. One line studies it through autoregressive compositional structure and relates it to compositional generalization, while another paper treats instruction following as a common evaluation setting for cross-task generalization.

**Space of measurement.** Papers link task generalization to 4 measurement instruments and 6 behavioral indicators. The recorded instruments are named evaluations, most often MMLU and Super-NaturalInstructions, followed by GPQA and MMLU-Pro; papers use them to test five-shot in-context learning, previously unseen tasks, or adapter generation for unseen tasks. It is also linked to 6 behavioral indicators, most often chain of thought, instruction following, link prediction, problem solving, and question answering, plus 1 other indicator. These operationalizations largely measure performance on previously unseen or cross-task evaluations, which matches the dominant definitions, although some definitions extend more broadly to prompts, domains, function classes, or evaluation methods.

**Links.** Papers also link task generalization to 3 constructs and 6 behavioral indicators. One paper claims a causal relationship from chain of thought to task generalization, stating that adding intermediate reasoning steps allows Transformers to generalize to unseen tasks, and another claims a causal relationship from metacognition to task generalization through self-awareness, monitoring, evaluation, regulation, and meta-reflection. Papers further report that task generalization is related to compositional generalization and zero-shot generalization, and is related to instruction following, link prediction, question answering, problem solving, and unanswerability detection. No correlational links are recorded.

## Sources

**Task generalization** (3 papers: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf), [Cultivating Gaming Sense for Yourself: Making VLMs Gaming Experts](https://aclanthology.org/2025.acl-long.643.pdf), [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf))
> The capacity of the model to transfer learned capabilities across a wide variety of distinct image-processing tasks without task-specific fine-tuning.

**Cross-task generalization** (5 papers: [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf), [Unraveling the Mechanics of Learning-Based Demonstration Selection for In-Context Learning](https://aclanthology.org/2025.acl-long.132.pdf), [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf), [dEBORA: Efficient Bilevel Optimization-based low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f0c4f3d83c58df58380af3b0729354c-Paper-Conference.pdf), [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf))
> The ability of a model trained on a specific source task, such as node classification, to perform well on a different, unseen target task, such as link prediction, without additional fine-tuning.

**Multi-task generalization** (3 papers: [GenRL: Multimodal-foundation world models for generalization in embodied agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/3076133f08b40607d00a8f48f6acd71c-Paper-Conference.pdf), [Time-MQA: Time Series Multi-Task Question Answering with Context Enhancement](https://aclanthology.org/2025.acl-long.1437.pdf), [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf))
> The ability of an embodied agent to adapt learned behavior to new tasks across domains and prompts beyond the training distribution.

**Generality** (2 papers: [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf))
> The ability of a method or model to perform effectively across a variety of different datasets and task types without task-specific training.

**Task-level generalization** (1 paper: [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf))
> The latent ability of a robotic policy to perform well on unseen tasks after training on a diverse set of simulation tasks, reflecting broad conceptual understanding rather than overfitting to specific instances.

**Unseen task generalization** (1 paper: [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf))
> The model's ability to perform effectively on tasks that were not part of its training set, based only on provided instructions.

**Generalization to unseen tasks** (3 papers: [Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d00071564ec447466fc4577743cf1b3-Paper-Conference.pdf), [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf), [Learngene Tells You How to Customize: Task-Aware Parameter Initialization at Flexible Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25af/xu25af.pdf))
> The model's ability to perform well on tasks and task categories that were not included in its fine-tuning data.

**Generalization to new tasks** (1 paper: [In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf))
> The ability to perform well on function classes not seen during pretraining, which arises when the pretraining task distribution is sufficiently diverse and represents a deviation from strict Bayesian prediction.

**Cross-task knowledge transfer** (1 paper: [LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf))
> The ability of a model to leverage information learned from a set of source tasks to improve learning and performance on new, unseen target tasks.

## Relationships

### Task generalization →
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > we also evaluate multi-task generalization ability with five-shot setting (in-context learning) on MMLU (Hendrycks et al., 2020) (Section 4.1)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 2 papers
  > We evaluate TAGI on the Super-Natural Instructions (SNI) [37] and P3 [30] datasets. Experimental results demonstrate its ability to effectively generate adapters for unseen tasks, surpassing meta-trained models... (Section 1 Introduction).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
  - [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://aclanthology.org/2025.acl-long.816.pdf)
- **GPQA** (measurement instrument): *measured_by*, 1 paper
  > "To explore the efficacy of our general purpose ARCHON architectures, we evaluate them on three previously unseen tasks: GPQA (Rein et al., 2024), MMLU (Hendrycks et al., 2021), and MMLU Pro (Wang et al., 2024b)."
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > "To explore the efficacy of our general purpose ARCHON architectures, we evaluate them on three previously unseen tasks: GPQA (Rein et al., 2024), MMLU (Hendrycks et al., 2021), and MMLU Pro (Wang et al., 2024b)."
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)

### → Task generalization
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > In contrast, we found that incorporating Chain-of-Thought (CoT) reasoning — adding intermediate reasoning steps to the prompt — allows Transformers to easily generalize to unseen tasks. (Section 1)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **Metacognition** (construct): *causes*, 1 paper
  > Our approach integrates self-awareness, monitoring, evaluation, regulation, and meta-reflection, to enhance LLMs’ ability to refine reasoning strategies and generalize across tasks.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)

### Associated with
- **Zero-shot generalization** (construct), 1 paper
  > for better cross-task generalization, the "zero-shot" learning ability of LLMs is crucial for real-world applications (Section 1 Introduction).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > Instruction Following is often used to evaluate the cross-task generalization of LLMs, and it is dedicated to handling any task described in natural language (Section 2 Related Work).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Problem solving** (behavioral indicator), 1 paper
  > horizontally, we examine the task generalization including problem solving, answerable judging, outcome judging, and process judging. (Section 1)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Unanswerability detection** (behavioral indicator), 1 paper
  > horizontally, we examine the task generalization including problem solving, answerable judging, outcome judging, and process judging. (Section 1)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Compositional generalization** (construct), 1 paper
  > While prior work has largely focused on qualitative insights into compositional generalization, our work takes a quantitative approach: studying how many training tasks are needed to achieve task generalization over an entire function class. (Section 2.1)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **Link prediction** (behavioral indicator), 1 paper
  > We employ models trained on node classification tasks directly for link prediction tasks without any fine-tuning. (Section 3.3)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > AQuilt achieves better task generalization by incorporating Chinese data and defining more flexible task types. Specifically, AQuilt assigns the task type as closed/open-book QA and uses task requirements as question prefixes. (Section 4.3)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)
