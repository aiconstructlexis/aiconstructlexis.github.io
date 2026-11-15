# Inductive reasoning
**Type:** Construct  
**Supporting papers:** 37  
**Also known as:** Induction, Rule induction, Inductive inference, Compositional rule inference, Concept inference, Interpretable learning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats inductive reasoning as inferring general rules, principles, patterns, or abstractions from a small or limited set of examples or observations and then applying them to novel situations. One paper phrases this as deriving underlying principles from a handful of observations and then generalizing to novel situations (Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement). Smaller variants make the inferred object more explicit, describing induction as first finding a latent function or hypothesis that explains training examples before predicting test outputs, or as inferring an unstated rule or concept from in-context demonstrations. A smaller line of work narrows the ability further to extracting compact human-understandable predictive rules or deriving possible game mechanisms from interaction history and environmental interaction.

**Space of facets.** Papers use several overlapping names around the construct, including induction, rule induction, inductive inference, compositional rule inference, concept inference, and interpretable learning. Most of these labels preserve the same basic structure, infer something latent from examples and use it on new cases, but they differ in what is induced: abstract rules or operations, latent functions, game mechanisms, compositional rules, concepts linking data to labels, or compact predictive models that a human can understand and apply. Some authors place it within logical reasoning alongside deductive, abductive, and analogical reasoning, while others describe it through rule-based reasoning or hypothesis-generation and program-synthesis styles in which functions are represented as code; one paper also uses the shorter label induction for repeated-subsequence continuation in context.

**Space of measurement.** Operationalization is benchmark-based: papers link inductive reasoning to 8 measurement instruments and 3 behavioral indicators. The most frequently linked instruments are List Functions, ACRE, ARC-AGI, BABILong, and CLUTRR, plus 3 other benchmarks or datasets: List Functions evaluates inferring list transform functions, ACRE is used as an inductive reasoning task with in-context updates, ARC-AGI is described as a visual inductive reasoning benchmark, BABILong includes simple induction within a broader reasoning suite, and CLUTRR is cited as targeting inductive reasoning among other reasoning types. Other operationalizations remain dataset-like, such as using MBPP+ through EvalPlus as an inductive reasoning dataset and profiling CommonsenseQA as peaking in inductive reasoning, while the linked behavioral indicators focus on code generation, hypothesis generation, and iterative refinement. These operationalizations usually match the prevailing definition by testing rule, function, or hypothesis inference from examples, although some uses are broader or repurposed rather than dedicated induction tests.

**Links.** Multiple papers claim a causal relationship from inductive reasoning to generalization, describing the inductive reasoning process as enhancing generalizability and enabling hypotheses that could generalize to new instances. Several papers also relate inductive reasoning to logical reasoning, where it is grouped with deductive and abductive inference. Other papers relate inductive reasoning to rule-based reasoning and iterative refinement, one paper reports that compositionality is related to inductive reasoning, and the remaining linked behavioral indicators are likewise recorded as related to the construct.

## Sources

**Inductive reasoning** (9 papers: [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf), [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf), [Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf), [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf), [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf), [The Stochastic Parrot on LLM's Shoulder: A Summative Assessment of Physical Concept Understanding](https://aclanthology.org/2025.naacl-long.569.pdf), [Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.110.pdf), [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf), [On LLM-Based Scientific Inductive Reasoning Beyond Equations](https://aclanthology.org/2025.emnlp-main.476.pdf))
> The ability to derive underlying principles or high-level abstractions from a limited set of observations and then generalize them to novel situations.

**Induction** (1 paper: [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf))
> The cognitive ability to infer general principles or patterns from specific instances or facts.

**Rule induction** (1 paper: [VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf))
> The ability to infer an underlying abstract rule, operation, or concept from a set of examples rather than being given an explicit instruction.

**Inductive inference** (1 paper: [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf))
> A form of logical reasoning where general rules or conclusions are derived from specific instances or observations, often associated with fast, intuitive System 1 thinking.

**Compositional rule inference** (1 paper: [Investigating the interaction of linguistic and mathematical reasoning in language models using multilingual number puzzles](https://aclanthology.org/2025.emnlp-main.1438.pdf))
> The ability to infer underlying compositional rules from implicit patterns presented in limited data, as humans do when learning language.

**Concept inference** (1 paper: [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf))
> The latent ability of a model to infer an unstated rule or concept that connects data to labels based on the demonstrations provided in-context.

**Interpretable learning** (1 paper: [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf))
> The ability to extract compact, human-understandable predictive rules from labeled data and apply them consistently across examples.

## Relationships

### Inductive reasoning →
- **List Functions** (measurement instrument): *measured_by*, 3 papers
  > We conduct experiments on four inductive reasoning datasets: the Abstraction and Reasoning Corpus (ARC), the one-dimensional variant of ARC (1D-ARC), the Syntax-Guided Synthesis (SyGuS) dataset, and the List Functions dataset. (Section 1)
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
- **Generalization** (construct): *causes*, 2 papers
  > The inductive reasoning process enhances generalizability by formulating general problem-solving strategies (Introduction).
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **ACRE** (measurement instrument): *measured_by*, 2 papers
  > We directly verify our analysis above using an inductive reasoning task called Abstract Causal REasoning (Chi Zhang et al. 2021, ACRE), where all LLM agents update their knowledge via ICL. (Section 5)
  - [Bias Amplification in Language Model Evolution: An Iterated Learning Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/4418f6a54f4314202688d77956e731ce-Paper-Conference.pdf)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **SyGuS** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on four inductive reasoning datasets: the Abstraction and Reasoning Corpus (ARC), the one-dimensional variant of ARC (1D-ARC), the Syntax-Guided Synthesis (SyGuS) dataset, and the List Functions dataset. (Section 1)
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **EvalPlus** (measurement instrument): *measured_by*, 1 paper
  > The abundance of test cases avails utilizing MBPP+ as an inductive reasoning dataset.
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
- **CLUTRR** (measurement instrument): *measured_by*, 1 paper
  > Other datasets like bAbI (Weston et al., 2015), CLUTRR (Sinha et al., 2019)... target specific reasoning types such as deductive, inductive, abductive, temporal, spatial, and mathematical reasoning.
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > “CommonsenseQA, a 5-choice multiple-choice benchmark, peaks in Inductive Reasoning”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **ARC-AGI** (measurement instrument): *measured_by*, 1 paper
  > "We verify our pipeline’s effectiveness on the ARC visual inductive reasoning benchmark"
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)

### Associated with
- **Logical reasoning** (construct), 3 papers
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
  - [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf)
- **Iterative refinement** (behavioral indicator), 1 paper
  > This work investigates LMs’ inductive reasoning capabilities through the lens of iterative hypothesis refinement (Section 1).
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > We represent functions f as Python code, meaning that induction synthesizes programs (Section 1).
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Compositionality** (construct), 1 paper
  > Inductive program synthesis excels at precise computations, and at composing multiple concepts (Abstract).
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Rule-based reasoning** (construct), 1 paper
  > in the rule-based reasoning paradigm, inductive reasoning involves first deriving the correct rule through the observation of examples and then using the inductive rule to answer new questions (like what humans do). (Section 1)
  - [MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b782a3462ee9d566291cff148333ea9b-Paper-Conference.pdf)
- **Hypothesis generation** (behavioral indicator), 1 paper
  > a new paradigm in automatic inductive reasoning has emerged: feeding observations (often referred to as train examples) as prompts into the LLM, sampling multiple hypotheses about the rule, and selecting the one that best explains the observations
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
