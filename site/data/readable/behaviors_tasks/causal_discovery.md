# Causal discovery
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Causal graph discovery, Causal graph construction, Full causal discovery  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats causal discovery as recovering or inferring causal structure from data or text. Most commonly, papers describe recovering the latent causal structure of variables; narrower formulations cast it as deciding, for each variable pair, whether A causes B, B causes A, or no relation, or as building a directed structure of item-action dependencies from interaction records and interventions. One recurring process description is that interaction records support initial causal assumptions and interventions then refine them into a causal subgraph.

**Variants.** Papers use several nearby names and settings for this behavior. Some frame it as causal graph discovery, including a temporal, lag-dependent directed graph over stocks that represents lagged causal links; others use causal graph construction for an embodied setting, where action-specific causal subgraphs are built from interaction records and interventions and then integrated into an ever-growing comprehensive graph. Another variant is full causal discovery, which asks for pairwise relation detection and direction across a given set of variables.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, COPA, through a measured_by relation. The linked description says COPA is used for causal discovery, and the papers linked here do not specify a separate scoring rule beyond using that instrument.

**What it is taken as evidence of.** The most prevalent linked construct is causal reasoning: papers relate causal discovery to causal reasoning by stating that causal reasoning tasks include causal discovery, or that causal reasoning includes causal discovery and inference. A smaller line of work claims a causal relationship from causal discovery to continual learning and to interpretability and explainability, with one paper saying an iterative discovery process ensures lifelong learning and that constructing a causal graph enables strong interpretability. Overall, the linked papers do not converge on a single construct it reflects, because they mix a broad related relation to causal reasoning with narrower causal claims to other constructs.

## Sources

**Causal discovery** (2 papers: [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf), [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf))
> The task of recovering the latent causal structure of variables from data or text.

**Causal graph discovery** (1 paper: [CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf))
> Inferring a temporal directed graph over stocks that represents lagged causal links between variables.

**Causal graph construction** (1 paper: [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf))
> Building a directed structure of item-action dependencies from interaction records and interventions.

**Full causal discovery** (1 paper: [On the Reliability of Large Language Models for Causal Discovery](https://aclanthology.org/2025.acl-long.471.pdf))
> The observable task of, for each pair of variables in a given set, identifying whether a causal relation exists and in which direction (A causes B, B causes A, or no relation).

## Relationships

### Causal discovery →
- **Continual learning** (construct): *causes*, 1 paper
  > Newly discovered items enable the execution of new unknown actions and the CD on these actions. This iterative process ensures the lifelong learning through continuous engagement and adaptation.
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > "ADAM constructs a nearly perfect causal graph from scratch, enabling efficient task decomposition and execution with strong interpretability."
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **COPA** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we use COPA (Roemmele et al., 2011), NPDS (Tu et al., 2019), e-CARE (Du et al., 2022), and Corr2Cause (Jin et al., 2023b) for causal discovery... (Section 4.1)
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf)

### Associated with
- **Causal reasoning** (construct), 3 papers
  > Causal Reasoning tasks include causal discovery, cause attribution, and causal effect estimation [30, 58, 65]. (Section 2.2)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf)
- **Hypothesis generation** (behavioral indicator), 1 paper
  > In hypothesis generation, we produce a causal graph by use of an LLM.
  - [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe90657b12193c7b52a3418bdc351807-Paper-Conference.pdf)
