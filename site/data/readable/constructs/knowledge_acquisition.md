# Knowledge acquisition
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Knowledge internalization, Fact learning, Knowledge gain  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this as a latent ability to internalize, retrieve, and use factual or contextual knowledge, with papers describing that knowledge as coming from training data, external sources, or internal representations and being used to support decision-making. A smaller line of work instead uses neighboring labels for process views: fact learning is the encoding of factual information into model weights, knowledge internalization is absorbing tool-generated solutions into parametric knowledge so problems can be solved without tool calls, and knowledge gain is the increase in knowledge or certainty after new information, estimated through shifts in an internal knowledge distribution. One paper also describes this acquisition as data-inefficient, saying models may need hundreds to thousands of diverse representations to learn a fact.

**Space of facets.** The papers use several neighboring labels rather than a single uniform breakdown. One recurring split is between broad knowledge use and narrower factual storage, with one paper focusing on simple associations such as birthdays, capital cities, and concept relations, while another says fact learning can occur at both early and late layers and that these yield different forms of generalization. The labels also differ in where knowledge is said to reside or change: fact learning places it in model weights, knowledge internalization in parametric knowledge after tool-generated solutions, and knowledge gain in shifts in an internal knowledge distribution.

**Space of measurement.** Operationalization is sparse: papers link the construct to one measurement instrument, AgentBench, and to no behavioral indicators. AgentBench systematically evaluates it as one of an LLM's core abilities, which lines up with the broad ability-oriented definitions. Other papers describe narrower measurement ideas for adjacent framings, including measuring progress toward effective knowledge acquisition from small corpora and estimating knowledge gain from shifts in the model's internal knowledge distribution.

**Links.** The only linked construct is Reasoning, and a paper claims a causal relationship from knowledge acquisition to it, stating that reasoning capabilities are enhanced through effective knowledge internalization.

## Sources

**Knowledge acquisition** (3 papers: [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf), [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf))
> The latent ability to retrieve and utilize relevant factual or contextual knowledge from external sources or internal representations to support decision-making.

**Fact learning** (1 paper: [Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25m/feng25m.pdf))
> The process by which a language model encodes and stores factual information from training data into its weights.

**Knowledge internalization** (1 paper: [Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf))
> The process by which a model incorporates external, tool-generated solutions into its parametric knowledge, allowing it to solve problems without relying on tool calls.

**Knowledge gain** (1 paper: [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> The increase in an LLM's knowledge or certainty about a topic resulting from exposure to new information, which can be estimated by the shift in its internal knowledge distribution.

## Relationships

### Knowledge acquisition →
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > In this study, we introduced TinyThinker to enhance reasoning capabilities through effective knowledge internalization. (Section 6)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
