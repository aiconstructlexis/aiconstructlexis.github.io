# Logical reasoning
**Type:** Construct  
**Supporting papers:** 228  
**Also known as:** Logical Thinking, Logical deduction, Logic inference, Logical capabilities, Logic reasoning, Logic, Syllogistic reasoning, Deduction, Deductive reasoning, Deductive generalization, Coherence & reasoning, First-order logic reasoning, Logical inference, Propositional inference, Multi-domain deductive reasoning, Disjunctive reasoning, Deductive inference, Formal inference  

## State of the Field

**Space of definitions.** Across the literature, the prevailing usage treats logical reasoning as a latent ability to derive conclusions from stated premises, rules, or constraints, usually by formal logic and deductive inference. Many definitions keep that core but widen the scope to multi-step, logically coherent reasoning paths, contradiction detection, and internally consistent outputs, while some frame it operationally as solving tasks such as logical deduction, formal fallacies, or entailment. A smaller line narrows it to specific forms, including first-order logic, syllogistic or propositional inference, implication elimination, and content-independent formal inference, and a few task-specific definitions recast it as pattern generalization over unseen tokens, legal inference from facts and rules, or deduction of hidden roles from observed actions.

**Space of facets.** Several papers explicitly divide the area into deductive, inductive, abductive, and analogical forms, while others use narrower subtype labels such as syllogistic reasoning, deductive inference, disjunctive reasoning, propositional inference, first-order logic reasoning, and multi-domain deductive reasoning. Some frameworks fold it into broader evaluation dimensions, for example logical thinking with logical correctness, robustness, and efficiency, or couple it with coherence, consistency, soundness, and rigor. Another recurring distinction separates structural validity from factual correctness, and a few papers contrast failures of logical reasoning with memory recall or pattern matching rather than treating them as the same problem.

**Space of measurement.** Operationalization is broad but dominated by benchmarks and evaluation datasets: papers link the construct to 37 measurement instruments and 12 behavioral indicators. The most recurrent instruments are LogiQA, PrOntoQA, FOLIO, ProofWriter, and ReClor, which instantiate it as inferring conclusions from premises, ontology-derived logical problems, human-annotated deductive questions with first-order logic annotations, small rulebases of facts and rules, and standardized-test logical reasoning questions. Other instruments extend this to formal-rule, long-context, multimodal, legal, and broad evaluation settings, and the behavioral side appears through prompting or downstream task settings. These measures mostly match the dominant premise-to-conclusion definition, though some broaden it to commonsense-adjacent QA, table reasoning, code-related settings, and response quality dimensions such as logical thinking.

**Links.** Papers mostly frame its links as causal or relatedness claims. Several papers claim a causal relationship from in-context learning and from chain of thought to logical reasoning, stating that task demonstrations can enhance the capability to apply common sense and logical reasoning and that CoT helps mainly on mathematical, logical, or algorithmic problems. Several other papers treat logical reasoning as related to abductive reasoning, inductive reasoning, and logical consistency. Single papers add several other downstream causal links from logical reasoning to other abilities and behaviors, as well as a few further related links to adjacent forms of reasoning.

## Sources

**Logical reasoning** (34 papers: [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [Guess & Sketch: Language Model Guided Transpilation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e4996c14d3674b5ca5c318829290783-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/03d7e13f0092405804f3a381ade8f3f0-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf), [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.317.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.374.pdf), [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [RuleArena: A Benchmark for Rule-Guided Reasoning with LLMs in Real-World Scenarios](https://aclanthology.org/2025.acl-long.27.pdf), [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf), [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> The ability to deduce conclusions from a set of premises using formal rules of logic.

**Logical deduction** (3 papers: [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf), [ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf), [Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM’s Reasoning Capability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25j/lin25j.pdf))
> The latent ability to infer logically equivalent statements from given premises, such as deriving 'B is A' from 'A is B' based on the symmetry of identity.

**Logical Thinking** (1 paper: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf))
> The latent ability to apply reasoning, critical thinking, and deductive skills to process and respond to instructions in a logically sound, robust, and efficient manner.

**Logic inference** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to reason from legal facts and rules to derive correct conclusions through deductive or multi-step inference.

**Logical capabilities** (1 paper: [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf))
> The model's capacity for logical reasoning and related problem-solving reflected in benchmark performance.

**Logic reasoning** (2 papers: [From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf), [Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/c239bac713017b0b2257b7622bf8aab3-Paper-Conference.pdf))
> The capacity to recognize abstract token patterns that do not rely on simple co-occurrence and to generalize them to novel tokens or sequences.

**Logic** (1 paper: [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf))
> The ability of a model to reason soundly and produce text that is internally consistent and follows logical principles.

**Syllogistic reasoning** (1 paper: [ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf))
> A form of logical reasoning that joins two or more premises to arrive at a conclusion.

**Deductive reasoning** (1 paper: [ADIFF: Explaining audio difference using natural language](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e337afbbb9fc2de993b88df0db6161e-Paper-Conference.pdf))
> The ability to draw logical conclusions by interpreting and comparing features from provided inputs.

**Deduction** (1 paper: [Strategist: Self-improvement of LLM Decision Making via Bi-Level Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/439dbffb7a044ee4b636babff57d4994-Paper-Conference.pdf))
> The ability to infer hidden information, such as other players' identities or roles, from observable actions and communication.

**Deductive generalization** (1 paper: [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf))
> The tendency for reasoning learned from broader causal relations to transfer to a more specific relation that was not directly demonstrated.

**Coherence & reasoning** (1 paper: [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf))
> The latent ability of a model to generate logically consistent, well-structured responses that demonstrate sound reasoning across multiple steps or ideas.

**First-order logic reasoning** (1 paper: [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf))
> The ability to perform logical deductions and manipulations within the formal system of first-order logic, involving quantifiers, predicates, and logical connectives.

**Logical inference** (1 paper: [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf))
> The latent ability of LLMs to derive conclusions from premises through inductive, abductive, or deductive reasoning processes, reflecting underlying cognitive-style reasoning mechanisms.

**Propositional inference** (1 paper: [Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf))
> Deriving all propositions that follow from a set of rules and known facts.

**Multi-domain deductive reasoning** (1 paper: [LLM-based Typed Hyperresolution for Commonsense Reasoning with Knowledge Bases](https://proceedings.iclr.cc/paper_files/paper/2025/file/67496dfa96afddab795530cc7c69b57a-Paper-Conference.pdf))
> Deriving conclusions from axioms and facts across multiple domains such as biological entities, foods, and vehicles.

**Disjunctive reasoning** (1 paper: [Probing Logical Reasoning of MLLMs in Scientific Diagrams](https://aclanthology.org/2025.emnlp-main.542.pdf))
> Handling questions where the correct answer depends on an 'or' relation, including cases where only one of multiple clauses needs to be true.

**Deductive inference** (1 paper: [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf))
> The ability to apply a rule or hypothesis to premises so that conclusions follow with logical necessity.

**Formal inference** (1 paper: [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf))
> The capacity to abstract and apply logical inference rules independent of the semantic content of the premises, focusing on structural validity rather than factual correctness.

## Relationships

### Logical reasoning →
- **PrOntoQA** (measurement instrument): *measured_by*, 8 papers
  > PrOntoQA (Saparov and He, 2023): A dataset designed for logical reasoning. (Section 4.1)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **LogiQA** (measurement instrument): *measured_by*, 8 papers
  > "LogiQA [31] collects questions about natural language inference (NLI) and requires models to infer the conclusion based on provided premises."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf)
  - [A Graph-Theoretical Framework for Analyzing the Behavior of Causal Language Models](https://aclanthology.org/2025.emnlp-main.1014.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **FOLIO** (measurement instrument): *measured_by*, 7 papers
  > We compare the performance of each setting on math (GSM8K) and logical reasoning (ContextHub and FOLIO) datasets. (Section 5.1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
  - [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf)
  - [Logical Reasoning with Outcome Reward Models for Test-Time Scaling](https://aclanthology.org/2025.emnlp-main.1326.pdf)
  - [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf)
- **ProofWriter** (measurement instrument): *measured_by*, 7 papers
  > ProofWriter (Tafjord et al., 2020): A logical reasoning dataset that, in contrast to PrOntoQA, uses real concepts for all assumptions. (Section 4.1)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf)
- **ReClor** (measurement instrument): *measured_by*, 4 papers
  > "we applied it to the Reclor logic reasoning dataset [21]."
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > BBH contains 21 tasks covering both semantic understanding and logical reasoning tasks. (Section 5.2)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **RuleTaker** (measurement instrument): *measured_by*, 3 papers
  > In the experiment, we employ five logical reasoning datasets: ... (3) RuleTaker (Clark et al., 2021), which is automatically generated via programming, utilizing connectives including ∧, ¬, and → (Section 4.1).
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf)
  - [Order Doesn't Matter, But Reasoning Does: Training LLMs with Order-Centric Augmentation](https://aclanthology.org/2025.emnlp-main.1382.pdf)
- **ZebraLogic** (measurement instrument): *measured_by*, 3 papers
  > We select one logical reasoning benchmark, ZebraLogic... for analysis. (Section 3.5)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf)
  - [ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25i/lin25i.pdf)
- **MMStar** (measurement instrument): *measured_by*, 2 papers
  > We further analyze the detailed scores on MM-Star (Chen et al., 2024a), including coarse perception (CP), fine-grained perception (FP), instance reasoning (IR), logical reasoning (LR)... (Table 4)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **LogicNLI** (measurement instrument): *measured_by*, 2 papers
  > We evaluated both the baselines and our method on three carefully selected logical reasoning datasets: ProntoQA (Saparov and He, 2023), ProofWriter (Tafjord et al., 2021) and LogicNLI (Tian et al., 2021). (Section 4.1)
  - [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153.pdf)
  - [Order Doesn't Matter, But Reasoning Does: Training LLMs with Order-Centric Augmentation](https://aclanthology.org/2025.emnlp-main.1382.pdf)
- **LogiQA 2.0** (measurement instrument): *measured_by*, 2 papers
  > LogiQA2 [Liu et al., 2023] is a revision and re-annotation of LogiQA [Liu et al., 2021], a logical reasoning reading comprehension dataset. (Appendix C.1)
  - [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
- **bAbI** (measurement instrument): *measured_by*, 2 papers
  > "the reasoning skills they assess, including spatial and temporal reasoning, deduction, and coreference resolution"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf)
- **LogicBench** (measurement instrument): *measured_by*, 2 papers
  > Logic LogicBench (Parmar et al., 2024) comprises various logic questions in both binary classification and multiple-choice formats. (Section 2.1)
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
- **ARC** (measurement instrument): *measured_by*, 2 papers
  > Reasoning: The model’s capacity for commonsense and logical reasoning is measured using Winogrande (Sakaguchi et al., 2021) and ARC (easy and challenge subsets) (Clark et al., 2018). (Section 4.1)
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
  - [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://aclanthology.org/2025.emnlp-main.1115.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > MMLU (Hendrycks et al., 2021) provides a comprehensive set of logical reasoning assessments across diverse subjects and difficulties, utilizing multiple-option questions to measure general world knowledge and logical inference capabilities.
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > Reasoning: The model’s capacity for commonsense and logical reasoning is measured using Winogrande (Sakaguchi et al., 2021) and ARC (easy and challenge subsets) (Clark et al., 2018). (Section 4.1)
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > "We further evaluate on various reasoning tasks in BIG-Bench (Srivastava et al., 2022; Suzgun et al., 2022): word sorting, logical deduction five objects, temporal sequences, reasoning about colored objects, and formal fallacies."
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Consistency** (construct): *causes*, 1 paper
  > the deductive reasoning process improves consistency by producing consistent solutions using a given strategy (Introduction).
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **Time-series feature extraction ability** (construct): *causes*, 1 paper
  > analyzing the precision and recall of finding relevant features through the usage of world knowledge and logical reasoning (Section 4.5).
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > LR: Logic Reasoning, AR: Attribute Reasoning, RR: Relation Reasoning, FP-S: Fine-grained Perception (Single-instance), FP-C: Fine-grained Perception (Cross-instance), CP: Coarse Perception. (Table A4)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **LexEval** (measurement instrument): *measured_by*, 1 paper
  > to systematically organize various evaluation tasks, we propose a Legal Cognitive Ability Taxonomy (LexAbility Taxonomy), which includes six aspects: Memorization, Understanding, Logic Inference, Discrimination, Generation, and Ethic. (Section 3.1)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CLUTRR** (measurement instrument): *measured_by*, 1 paper
  > CLUTRR [41] is a deductive reasoning dataset requiring multi-hop reasoning over family relationships. (Section 4).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **Action selection** (behavioral indicator): *causes*, 1 paper
  > The Analytic Process relies on logical reasoning, employing rational thinking to analyze complex situations and make safe driving decisions. (Section 3.3)
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 1 paper
  > And we use StrategyQA [12] for logical reasoning that requires multiple reasoning steps (Section 5.1.1).
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets.
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > PAT can enhance the logical capabilities of the LLMs. We see the scores increase in related aspects of MT-bench such as coding and reasoning.
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Flexibility** (construct): *causes*, 1 paper
  > The grounding knowledge and principled reasoning procedure enable R2-Guard to be effective, robust against jailbreak attacks, and flexible given new safety categories. (Abstract)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **ContextHub** (measurement instrument): *measured_by*, 1 paper
  > We compare the performance of each setting on math (GSM8K) and logical reasoning (ContextHub and FOLIO) datasets. (Section 5.1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **BIG-Bench Logical Deduction** (measurement instrument): *measured_by*, 1 paper
  > We evaluate CLOVER on seven logical reasoning tasks: AR-LSAT (Zhong et al., 2022), ZebraLogic (Lin et al., 2025), Logic grid puzzle (Puzzle), Symbol interpretation (Symbol), and Logical deduction (Deduction) from the BigBench collaborative benchmark (Srivastava et al., 2022), FOLIO (Han et al., 2022), and ProofWriter (Tafjord et al., 2021). (Section 4.1)
  - [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf)
- **e-SNLI** (measurement instrument): *measured_by*, 1 paper
  > e-SNLI (Camburu et al., 2018) for logical reasoning ability (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **MuSR** (measurement instrument): *measured_by*, 1 paper
  > “On datasets that require math (MATH, GSM8K) or formal logic (ContextHub, MuSR to a lesser degree)”
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Relation extraction** (behavioral indicator): *causes*, 1 paper
  > We use these logical rules to elicit the deductive reasoning ability of the LLM, enabling more precise relation prediction. (Section 1)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
- **Argument generation** (behavioral indicator): *causes*, 1 paper
  > generating logically coherent arguments is a challenging task and requires an appropriate combination of reliable evidence and effective logical reasoning (Section 1)
  - [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.374.pdf)
- **Date Understanding** (measurement instrument): *measured_by*, 1 paper
  > Logical Reasoning: Date Understanding (bench authors, 2023). (Section 4)
  - [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 1 paper
  > the performance comparison on the Game of 24 validates the effectiveness of the FoT in the mathematical and logical reasoning task. (Section 4.6)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **Safety alignment** (construct): *causes*, 1 paper
  > To tackle these challenges, we propose SHIELDAGENT, the first guardrail agent designed to enforce explicit safety policy compliance for the action trajectory of other protected agents through logical reasoning. (Section 1)
  - [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf)
- **GPQA** (measurement instrument): *measured_by*, 1 paper
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting and the GPQA (Rein et al., 2023) dataset for graduate-level multiple-choice questions in a 0-shot setting (Section 4).
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **TTT-Bench** (measurement instrument): *measured_by*, 1 paper
  > In this work, we introduce TTT-Bench, a new benchmark that is designed to evaluate basic strategic, spatial, and logical reasoning abilities in LRMs through a suite of four two-player Tic-Tac-Toe-style games that humans can effortlessly solve from a young age. (Abstract)
  - [TTT-Bench: A Benchmark for Evaluating Reasoning Ability with Simple and Novel Tic-Tac-Toe-style Games](https://aclanthology.org/2025.emnlp-main.140.pdf)
- **MLogiQA** (measurement instrument): *measured_by*, 1 paper
  > MLOGIQA (logical reasoning) is almost always at the lowest performance level across all models and sizes, indicating that this type of logical reasoning capability is the most challenging for cross-lingual transfer. (Section 5.2)
  - [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf)
- **SATBench** (measurement instrument): *measured_by*, 1 paper
  > We introduce SATBench, a benchmark for evaluating the logical reasoning capabilities of large language models (LLMs) through logical puzzles derived from Boolean satisfiability (SAT) problems.
  - [SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas](https://aclanthology.org/2025.emnlp-main.1716.pdf)
- **FLASK** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we focus on the ‘logical thinking’ category in FLASK, which encompasses three aspects: logical correctness, logical robustness, and logical efficiency. (Section 5.4)
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)
- **Jailbreak resistance** (behavioral indicator): *causes*, 1 paper
  > The grounding knowledge and principled reasoning procedure enable R2-Guard to be effective, robust against jailbreak attacks, and flexible given new safety categories. (Abstract)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)

### → Logical reasoning
- **In-context learning** (construct): *causes*, 2 papers
  > It has been shown that including task demonstrations in the prompt can enhance the capability of language models to apply common sense and logical reasoning [65, 72] and learn patterns from the supplied demonstrations [14], significantly enhancing the flexibility and generality of language models. (Introduction)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 2 papers
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > In logical reasoning tasks like Date Understanding, LLM’s reasoning ability is degraded when using code, as shown in Appendix Section G. (Section 3.3)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Fine-grained perception** (construct): *causes*, 1 paper
  > This suggests that fusing raw image and text embeddings in a single transformer is beneficial for fine-grained perception and subsequently enhances image-based logical reasoning. (Section 4.3)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)

### Associated with
- **Inductive reasoning** (construct), 3 papers
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
  - [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf)
- **Abductive reasoning** (construct), 3 papers
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
  - [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf)
- **Logical consistency** (construct), 2 papers
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: Logical Thinking (Logical Correctness, Logical Robustness, Logical Efficiency)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
  - [LogicTree: Structured Proof Exploration for Coherent and Rigorous Logical Reasoning with Large Language Models](https://aclanthology.org/2025.emnlp-main.1054.pdf)
- **Reasoning** (construct), 2 papers
  > they discuss reasoning tasks including commonsense reasoning, mathematical reasoning, logical reasoning, and causal reasoning. (Section 2.1)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Legal reasoning** (construct), 1 paper
  > We also rewrite samples to align with the syllogistic reasoning framework common in legal analysis. (Section 3.2)
  - [Unilaw-R1: A Large Language Model for Legal Reasoning with Reinforcement Learning and Iterative Inference](https://aclanthology.org/2025.emnlp-main.915.pdf)
- **Logical soundness** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: Logical Thinking (Logical Correctness, Logical Robustness, Logical Efficiency)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Constrained text generation** (behavioral indicator), 1 paper
  > We posit that one direction is incorporating logical and compositional challenges via constrained text generation.
  - [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator), 1 paper
  > the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > When evaluating the Writing Legal Document scenario, logic is identified as the most critical dimension, followed by considerations of harmlessness and clarity, reflecting the distinct requirements of legal writing.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Pattern matching** (construct), 1 paper
  > ...distinguish genuine reasoning from mere memorization of solutions or responses, or mimicking the logical steps previously encountered (Gignac & Szodorai, 2024). This distinction aligns with ideas akin to the Chinese Room Argument (Cole, 2024), underscoring the difference between true comprehension and pattern-matching. (Section 2)
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
- **Knowledge manipulation** (construct), 1 paper
  > Knowledge manipulation is arguably a simplest form of logical reasoning. (Section 1)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Analogical reasoning** (construct), 1 paper
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Code reasoning** (construct), 1 paper
  > “Code reasoning is a category of tasks that incorporates logical reasoning into code”
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Table reasoning** (construct), 1 paper
  > Tabular reasoning presents an inherently challenging problem, requiring logical, mathematical, and textual reasoning over unstructured queries and structured tables
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Mathematical problem solving** (behavioral indicator), 1 paper
  > math tasks challenge logical reasoning;
  - [GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents](https://aclanthology.org/2025.acl-long.557.pdf)
- **Pragmatic understanding** (construct), 1 paper
  > it thus appears that QwQ32b’s high performance in logical reasoning is achieved at some cost to its capability of pragmatic inference. (Section 4.1)
  - [Pragmatic Inference Chain (PIC) Improving LLMs' Reasoning of Authentic Implicit Toxic Language](https://aclanthology.org/2025.emnlp-main.296.pdf)
- **Reasoning rigor** (construct), 1 paper
  > Current LLM-based methods for logical reasoning still struggle to perform structured exploration while ensuring logical coherence and rigor in complex, multi-step reasoning tasks (Section 2.2).
  - [LogicTree: Structured Proof Exploration for Coherent and Rigorous Logical Reasoning with Large Language Models](https://aclanthology.org/2025.emnlp-main.1054.pdf)
- **Reversal curse** (construct), 1 paper
  > One perspective is that it demonstrates a basic failure of logical deduction in the LLM’s training process.
  - [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > NLI is similar to deductive reasoning in assessing whether a premise supports or contradicts a hypothesis. (Section 6.3)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Word unscrambling** (behavioral indicator), 1 paper
  > Logical reasoning tasks include Word Unscrambling (bench authors, 2023), which requires unscrambling given letters to form an English word for implicit reasoning, and the binary Analytic Entailment task (bench authors, 2023) for linguistic entailment. (Section 4.1)
  - [Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability](https://proceedings.iclr.cc/paper_files/paper/2025/file/88139fdcc82fc597090620d77b023282-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > Mathematical reasoning tasks pose significant challenges for large language models (LLMs) because they require precise logical deduction and sequence analysis. (Abstract)
  - [Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM’s Reasoning Capability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25j/lin25j.pdf)
