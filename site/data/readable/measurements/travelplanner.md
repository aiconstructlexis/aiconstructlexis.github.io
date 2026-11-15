# TravelPlanner
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** Travelplanner  

## State of the Field

**What it is.** Across papers, the dominant framing is a benchmark for evaluating travel planning agents or LLM agents on complex planning tasks. Most descriptions add a sandbox environment with tools for accessing nearly four million data records, plus curated planning intents or queries, reference plans, and user-specified constraints; some narrow this to U.S. domestic travel planning, while others emphasize itinerary generation over flights, accommodations, and other arrangements, with hard and sometimes soft constraints. A smaller line describes it as a dataset or benchmark task rather than simply a benchmark, and one paper reports results on a TravelPlanner validation setting.

**What it is claimed to measure.** Papers link TravelPlanner to 2 constructs and no behavioral indicators. The prevailing usage is to measure Planning, with papers describing it as a benchmark for real-world, complex, or challenging planning; a smaller line of work uses it to measure Long-horizon planning under user-defined constraints. These measurement claims stay concentrated on planning-related constructs rather than spreading across many targets.

**Space of uses.** No measurement instrument is linked to it, although papers often report evaluating it alongside other planning benchmarks, including OpenAGI, Natural Plan, Tau-bench, and PlanBench. The common positioning is as a challenging benchmark for comparing agent systems and planning methods, while one paper uses it as a further validation task after other evaluations.

**Concerns raised.** When papers note problems on TravelPlanner, they mostly emphasize difficulty: authors describe it as challenging and failure-prone, and a few report low success rates, including 15.6% in one study and a 10% viable-plan success rate for the best LLM in another. One paper also says its results show that LLMs are not capable of handling multi-constraint tasks.

## Sources

**Travelplanner** (3 papers: [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf), [SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection](https://aclanthology.org/2025.emnlp-main.839.pdf), [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf))
> A benchmark for evaluating LLM agents on travel-planning tasks.

**TravelPlanner** (6 papers: [Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface](https://proceedings.iclr.cc/paper_files/paper/2025/file/25458943db16e0f78f748ca5bc34fff6-Paper-Conference.pdf), [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [Large Language Models Can Solve Real-World Planning Rigorously with Formal Verification Tools](https://aclanthology.org/2025.naacl-long.176.pdf), [Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents](https://aclanthology.org/2025.acl-long.857.pdf), [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf))
> A benchmark for evaluating travel planning agents, providing a sandbox environment with tools for accessing travel data and a set of curated planning intents with constraints.

## Relationships

### → TravelPlanner
- **Planning** (construct): *measured_by*, 4 papers
  > Planning in complex and realistic environments is also a crucial skill for building autonomous agents. Thus, we also select TravelPlanner (Xie et al., 2024), a benchmark designed to evaluate language agents in real-world complex planning with multiple constraints. (Section 4.3)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)
- **Long-horizon planning** (construct): *measured_by*, 1 paper
  > TravelPlanner (TP) (Xie et al., 2024), which tests long-horizon planning under user-defined constraints (Section 5.1)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)
