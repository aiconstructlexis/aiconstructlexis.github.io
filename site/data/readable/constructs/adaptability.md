# Adaptability
**Type:** Construct  
**Supporting papers:** 90  
**Also known as:** Adaptation, Continual learning efficiency, Self-adaptation, Adaptive capabilities, Domain adaptation, Cross-table generalizability, Task adaptivity, Domain knowledge adaptation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats adaptability as a model, agent, or system's ability to adjust behavior or performance to a specific downstream task, new task, changed environment, or shifted distribution. Many definitions make this dynamic, describing alignment to task distributions, adjustment during inference, or continual adaptation, and some explicitly frame it as possible without retraining. Smaller lines of work narrow it to acquiring new capabilities from limited task-specific reference materials, self-evaluating and modifying behavior without external intervention, or adapting to specialized domains, schemas, opponent strategies, or role-playing situations.

**Space of facets.** Papers use several overlapping names for neighboring ideas: adaptation, adaptability, adaptive capabilities, task adaptivity, continual learning efficiency, self-adaptation, domain adaptation, domain knowledge adaptation, and cross-table generalizability. The most common split is between task-level adjustment and domain-level adjustment, with narrower variants for tool selection across contexts, rapid adaptation to future tasks, real-time self-modification, transfer across tables and schemas, and keeping a character responsive to changing conditions while preserving role identity. The same label is applied to different loci, including the base model, an agent, a routing system, and a guardrail system, and one paper explicitly pairs adaptability with 'generality'.

**Space of measurement.** Papers link adaptability to 8 measurement instruments and 3 behavioral indicators. Operationalization in the linked relationships is through named benchmark or evaluation settings, most often AitW, AndroidWorld, ImageNet-1k, MT-Bench, and Mind2Web, with MiniWoB++, OSWorld, and ScreenSpot also linked. The linked evidence measures it by performance on real-time dynamic OS tasks, on the named ScreenSpot, MiniWoB++, AitW, and Mind2Web evaluations, on routing to new model pairs in MT-Bench, and on 16-shot domain adaptation in ImageNet-1k, so the operationalization mostly tracks performance under new tasks, scenarios, or domains and matches the dominant task and distribution-shift definitions more closely than the narrower self-adaptation or reference-material framings.

**Links.** One paper claims a causal relationship from in-context learning to adaptability, saying context-conditioned input sequences let a system adapt to new tasks, and another claims a causal relationship from plan revision to adaptability through re-planning in response to feedback and exceptions. Several papers report that adaptability is related to catastrophic forgetting. Single-paper claims also report it is related to generalization and multimodal understanding, along with several other constructs or indicators.

## Sources

**Adaptation** (1 paper: [A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf))
> The capacity of a model to acquire new capabilities or knowledge from limited, task-specific reference materials rather than relying on pre-existing training data.

**Adaptability** (11 papers: [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf), [MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf), [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf), [Decomposed Prompt Decision Transformer for Efficient Unseen Task Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/de18052eb17cce56554a9637dd5aadba-Paper-Conference.pdf), [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf), [LLM-Based Explicit Models of Opponents for Multi-Agent Games](https://aclanthology.org/2025.naacl-long.41.pdf), [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf), [MixLLM: Dynamic Routing in Mixed Large Language Models](https://aclanthology.org/2025.naacl-long.545.pdf), [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399.pdf), [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf), [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf))
> The ability of a model to adjust its behavior and performance to align with specific downstream tasks based on their distributional characteristics.

**Continual learning efficiency** (1 paper: [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf))
> The ability of a model to rapidly adapt to new downstream tasks beyond its initial training set, indicating how well it builds on existing knowledge for future learning.

**Self-adaptation** (1 paper: [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf))
> The ability of a large language model to evaluate and modify its own behavior in real-time in response to the specific demands of a given task or prompt, without external intervention.

**Adaptive capabilities** (1 paper: [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf))
> The latent capacity of a language model to flexibly adjust its behavior to new tasks or scenarios without retraining.

**Domain adaptation** (2 papers: [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf), [Advancing SMoE for Continuous Domain Adaptation of MLLMs: Adaptive Router and Domain-Specific Loss](https://aclanthology.org/2025.acl-long.1290.pdf))
> The model's ability to adjust its output distribution to better suit a specific domain, such as medicine or law, without undergoing additional training.

**Cross-table generalizability** (1 paper: [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf))
> The extent to which learned table representations transfer across different tables and schemas rather than overfitting to a specific table or prompt context.

**Task adaptivity** (1 paper: [Generalization Principles for Inference over Text-Attributed Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bq/wang25bq.pdf))
> The capacity of a model to adjust its internal representations or reasoning based on the specific task context, such as class definitions or labeling goals, without fine-tuning.

**Domain knowledge adaptation** (1 paper: [Test-Time Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25z/hu25z.pdf))
> The latent ability of an LLM to adjust to specialized subject-matter content in vertical domains such as medicine, agriculture, geography, and finance.

## Relationships

### Adaptability →
- **AndroidWorld** (measurement instrument): *measured_by*, 1 paper
  > On the OSWorld (Xie et al., 2024b) and AndroidWorld (Rawles et al., 2024) benchmarks, OSCAR consistently surpassed other agents... demonstrating superior adaptability across real-time dynamic OS tasks. (Section 1)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 1 paper
  > For domain adaptation, following [82, 7], we train on ImageNet [11] with a 16-shot setting, use the validation split by [82] for hyperparameter selection and report the results on the official validation set (Section 4).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **ScreenSpot** (measurement instrument): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **MiniWoB++** (measurement instrument): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **AitW** (measurement instrument): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **Mind2Web** (measurement instrument): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > to demonstrate the adaptability of our routers to new LLMs, we report in Table 4 the performance of our routers on MT Bench when they are used to route between two new model pairs (Section 5.2)
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **OSWorld** (measurement instrument): *measured_by*, 1 paper
  > On the OSWorld (Xie et al., 2024b) and AndroidWorld (Rawles et al., 2024) benchmarks, OSCAR consistently surpassed other agents... demonstrating superior adaptability across real-time dynamic OS tasks. (Section 1)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### → Adaptability
- **In-context learning** (construct): *causes*, 1 paper
  > By leveraging in-context information during both pre-training and inference, Zebra dynamically adapts to new tasks by conditioning on input sequences that incorporate context example trajectories. (Abstract)
  - [Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf)
- **Plan revision** (behavioral indicator): *causes*, 1 paper
  > To enhance stability and adaptability, OSCAR operates as a state machine, equipped with error-handling mechanisms and task-driven re-planning, allowing it to efficiently adjust to real-time feedback and exceptions. (ABSTRACT)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### Associated with
- **Catastrophic forgetting** (behavioral indicator), 2 papers
  > We present DES-MoE, a dynamic framework for multi-domain MoE adaptation that mitigates catastrophic forgetting through adaptive routing and expert-domain correlation mapping. (Section 6)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [Position: Enough of Scaling LLMs! Lets Focus on Downscaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25c/goel25c.pdf)
- **Generalization** (construct), 1 paper
  > Overall, our system integrated with MAS-GPT offers the following key advantages: simplicity, cost-efficiency, and adaptability (generality). (Section 3.3)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Multimodal understanding** (construct), 1 paper
  > This strategy is underpinned by the understanding that the evolution from LLMs to MLLMs can be conceptualized as a domain adaptation process, i.e., transitioning from text-centric to multi-modal understanding. (Section 1)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
- **Text summarization** (behavioral indicator), 1 paper
  > Li et al. (2024) investigates the factors that play a role in domain adaptation for text summarization.
  - [DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.387.pdf)
- **General ability** (construct), 1 paper
  > How can we preserve and transfer the general capabilities of LLMs while enabling them to adapt to domain-specific knowledge? (Section 1).
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
- **Compositionality** (construct), 1 paper
  > While compositionality and scalability are crucial for effective adaptation, current LLM training methodologies fall short of achieving both these properties simultaneously. (Section 1)
  - [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf)
