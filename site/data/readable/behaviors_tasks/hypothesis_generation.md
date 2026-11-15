# Hypothesis generation
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Scientific hypothesis generation, Zero-shot hypothesis generation, Hypothesis formulation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is producing candidate explanations or rules, usually in natural language, from observations, examples, or other available information. In this framing, models are asked to generate one or more plausible, valid, or accurate hypotheses that explain input-output pairs, transformations, or observed patterns, sometimes as multiple alternatives to be evaluated or refined. Smaller lines of work use the same behavior for scientific inquiry, where hypotheses are designed to be testable and grounded in evidence, constraints, or anomalies, and for agent settings, where the hypotheses explain another agent's latent strategy or goal, or propose a strategy before execution.

**Variants.** A common variant studies inductive reasoning from examples, with free-form or constrained textual rules, multiple abstract hypotheses, and sometimes a paired Python implementation. Papers also use names such as scientific hypothesis generation, zero-shot hypothesis generation, and hypothesis formulation, covering cases where models generate scientific hypotheses from evidence, constraints, anomalies, or data patterns, sometimes without demonstrations and sometimes with clear provenance. Other variants place the behavior in multi-agent, embodied, optimization, and causal-modelling settings, where the hypotheses concern latent strategies, possible tool actions, updated hypothetical solutions from feedback, or an LLM-produced causal graph; some work further relates it to iterative refinement through proposing, selecting, and refining textual rules.

**Space of elicitation and scores.** Papers link it to one measurement instrument, DiscoveryBench. There, the behavior is measured in a scientific query setting where a system first generates Python code to analyze a described data schema and then generates scientific hypotheses.

**What it is taken as evidence of.** Papers do not use one shared construct-level interpretation for this behavior. Three constructs are linked: one paper claims a causal relationship from Theory of mind to Hypothesis generation, another claims a causal relationship from Commonsense reasoning to Hypothesis generation, and another reports Hypothesis generation as related to Inductive reasoning, in a setup that samples multiple hypotheses about a rule and selects the one that best explains observations.

## Sources

**Hypothesis generation** (6 papers: [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf), [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf), [Exploiting Edited Large Language Models as General Scientific Optimizers](https://aclanthology.org/2025.naacl-long.270.pdf), [EscapeBench: Towards Advancing Creative Intelligence of Language Model Agents](https://aclanthology.org/2025.acl-long.39.pdf), [On LLM-Based Scientific Inductive Reasoning Beyond Equations](https://aclanthology.org/2025.emnlp-main.476.pdf), [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf))
> The observable act of producing natural language statements that propose explanations for another agent's latent strategies or goals.

**Scientific hypothesis generation** (1 paper: [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf))
> Generating candidate scientific hypotheses from evidence, constraints, and anomalies.

**Zero-shot hypothesis generation** (1 paper: [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf))
> The observable behavior of generating hypotheses without any in-context demonstrations, relying solely on the model's internal knowledge.

**Hypothesis formulation** (1 paper: [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895.pdf))
> Designing testable scientific hypotheses based on identified research ideas or data patterns.

## Relationships

### Hypothesis generation →
- **DiscoveryBench** (measurement instrument): *measured_by*, 1 paper
  > In DiscoveryBench, given the description of input data schema and a scientific query, a method is supposed to first generate Python code to analyze the data based on the query and then generate scientific hypotheses. (Section 4.1)
  - [AutoSDT: Scaling Data-Driven Discovery Tasks Toward Open Co-Scientists](https://aclanthology.org/2025.emnlp-main.1546.pdf)

### → Hypothesis generation
- **Theory of mind** (construct): *causes*, 1 paper
  > The ToM module generates hypotheses about these latent variables in natural language. (Section 3.2)
  - [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *causes*, 1 paper
  > An LLM leverages common-sense reasoning to generate hypotheses, while a symbolic tool ensures their logical consistency through systematic validation. (Section 3.1)
  - [NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf)

### Associated with
- **Iterative refinement** (behavioral indicator), 2 papers
  > Iterative hypothesis refinement employs a three-step process: proposing, selecting, and refining hypotheses in the form of textual rules. (Abstract).
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
  - [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf)
- **Inductive reasoning** (construct), 1 paper
  > a new paradigm in automatic inductive reasoning has emerged: feeding observations (often referred to as train examples) as prompts into the LLM, sampling multiple hypotheses about the rule, and selecting the one that best explains the observations
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
- **Causal discovery** (behavioral indicator), 1 paper
  > In hypothesis generation, we produce a causal graph by use of an LLM.
  - [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe90657b12193c7b52a3418bdc351807-Paper-Conference.pdf)
