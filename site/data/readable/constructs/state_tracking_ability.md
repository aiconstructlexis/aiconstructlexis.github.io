# State tracking ability
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** State tracking, State Tracking, State-tracking, Fluent tracking, Task tracking, Stateful processing, Tracking past actions, Quantity tracking, Long-range consistency  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this construct as a latent ability to maintain and update an internal representation of an evolving state across sequential inputs or updates. Definitions mostly agree on sequential maintenance and updating, but they differ on what state is being tracked: some speak broadly about a system or world state, while narrower formulations focus on the complete final set of fluents after actions, task progress with sub-goals and partner actions, running quantities, or reuse of intermediate results over long computations. A smaller line of work shifts from latent capacity to observable behavior, describing tracking past actions during a task trajectory.

**Space of facets.** The clearest hierarchy appears in action reasoning work, where fluent tracking asks which properties of an object hold after a sequence of actions, and state tracking extends this to the complete set of final-state fluents. Other papers carve the broader family into task tracking, centered on completed and pending sub-goals and partner actions, and stateful processing, where quantity tracking is a specific case based on repeated additions and subtractions. Across papers, neighboring labels such as stateful processing, long-range consistency, and tracking past actions are applied to closely related sequential-update problems.

**Space of measurement.** Operationalization in the linked relations centers on 1 measurement instrument, MCBench, a benchmark that tests long-range consistency by requiring models to carry intermediate results across several steps and reuse them later. Papers also connect it to 3 behavioral indicators, mathematical problem solving, modular arithmetic, and parity checking. More broadly, papers instantiate the construct through output tasks such as answering questions about changed or final fluents after action sequences, keeping a running total, and tracking prior or partner actions, so measurement often targets observable performance even when definitions describe an internal representation.

**Links.** Outside measurement, papers report only related links. One paper reports that mathematical problem solving is related to state tracking ability, and the same paper reports related links from modular arithmetic and parity checking to state tracking ability as settings used to demonstrate improved state-tracking performance. No causal or correlational link is reported, and no linked construct appears.

## Sources

**State tracking** (2 papers: [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf), [(How) Do Language Models Track State?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25r/li25r.pdf))
> The ability to maintain and update an internal representation of state over a sequence of inputs, crucial for complex reasoning and coding tasks.

**State-tracking** (1 paper: [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf))
> The ability of a model to maintain and update an internal representation of a system's state based on a sequence of observed updates.

**State Tracking** (1 paper: [ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf))
> The ability to maintain a complete and accurate representation of all properties (fluents) in the world after a sequence of actions has occurred.

**Fluent tracking** (1 paper: [ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf))
> The ability to infer which properties of an object remain valid after a sequence of actions from the changed state.

**Task tracking** (1 paper: [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf))
> The ability to maintain an internal state of task progress, including which sub-goals have been completed and which are still pending, especially in the presence of a partner's actions.

**Stateful processing** (1 paper: [Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf))
> The ability to maintain and update an internal state based on a sequence of operations described in the context.

**Tracking past actions** (1 paper: [RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf))
> The observable behavior of maintaining and reasoning about the history of actions taken during a task trajectory.

**Quantity tracking** (1 paper: [Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf))
> Maintaining and updating a running total of items through a sequence of add and subtract operations.

**Long-range consistency** (1 paper: [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf))
> The ability to maintain and correctly reuse intermediate results and other information across multiple steps of a long computational process.

## Relationships

### State tracking ability →
- **MCBench** (measurement instrument): *measured_by*, 1 paper
  > MCBench evaluates three key capabilities of LLMs: ... • Long-Range Consistency: To finish the computation, the model must carry intermediate results across several steps and reuse them later
  - [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf)

### Associated with
- **Mathematical problem solving** (behavioral indicator), 1 paper
  > models (especially DeltaNet) with extended eigenvalue range will perform better on language modeling tasks linked to state-tracking such as coding or mathematics
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
- **Parity checking** (behavioral indicator), 1 paper
  > We test the modified methods on parity, modular arithmetic, and permutation composition, demonstrating improved state-tracking performance.
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
- **Modular arithmetic** (behavioral indicator), 1 paper
  > We test the modified methods on parity, modular arithmetic, and permutation composition, demonstrating improved state-tracking performance.
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
