# Collaboration ability
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Collaboration, Coordination, Collaborative ability, Collaborativeness, Coordination ability, Collaboration capability, Collaborative capability, Model coordination  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats collaboration ability as a latent ability or tendency to work with another agent by coordinating actions toward a shared or mutually beneficial outcome. Several definitions make the coordination aspect explicit, describing alignment of actions, establishment of shared conventions, or organization with a partner to minimize redundant or conflicting effort, and one formulation ties this to common knowledge. A smaller line of work narrows the construct to particular settings, such as iterative discussion among models, adaptation to diverse human users or unseen teammates, or the tendency of a model to produce better responses when given other models' outputs as context. One broader framing describes it as the latent potential of AI systems to interact, coordinate, and jointly perform tasks in a distributed ecosystem of specialized agents.

**Space of facets.** Papers do not use a single stabilized label: nearby names include collaboration, coordination, collaboration capability, collaborativeness, and model coordination. The clearest internal breakdown treats collaboration capability as having two components, initiating collaboration and responding to collaboration, while coordination-oriented variants emphasize aligning with teammates' preferred behaviors, establishing shared conventions, or adapting to diverse human users during cooperation without prior retraining. The labels are not fully interchangeable, because collaborativeness is used for response-quality improvement from exposure to other model outputs, whereas other formulations describe an interactional capacity of an agent, model, or model team.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Where papers make the construct concrete, they do so through settings and behaviors rather than a shared instrument: working toward mutually beneficial outcomes in non-zero-sum games, organizing actions with a partner in embodied tasks, solving tasks through iterative discussion or collaborative requests, adapting to unseen teammates or users, and producing better responses when given other models' outputs. One paper also describes process-oriented evaluation metrics for fine-grained collaboration capabilities.

**Links.** Only related links are reported. One paper relates collaboration ability to Help-seeking, in the sense that collaboration capability includes initiating collaboration and responding to collaborative requests. Another paper relates it to Text generation quality, describing collaborativeness as better responses when a model is presented with outputs from other models.

## Sources

**Collaboration** (2 papers: [GTBench: Uncovering the Strategic Reasoning Capabilities of LLMs via Game-Theoretic Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/3191170938b6102e5c203b036b7c16dd-Paper-Conference.pdf), [Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf))
> The tendency or ability to work with another agent towards a mutually beneficial outcome, particularly in non-zero-sum games.

**Coordination** (2 papers: [Secret Collusion among AI Agents: Multi-Agent Deception via Steganography](https://proceedings.neurips.cc/paper_files/paper/2024/file/861f7dad098aec1c3560fb7add468d41-Paper-Conference.pdf), [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf))
> The latent ability of agents to align their actions or establish shared conventions, which is mutually dependent on common knowledge.

**Collaborative ability** (1 paper: [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf))
> The latent capacity of a model or model team to work with another agent through iterative discussion to solve tasks effectively.

**Collaborativeness** (1 paper: [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf))
> The tendency of a language model to improve its response quality when provided with responses from other models as context.

**Coordination ability** (1 paper: [LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dq/li25dq.pdf))
> The latent capacity of an agent to effectively collaborate with diverse teammates by aligning its actions with their preferred coordination behaviors.

**Collaboration capability** (1 paper: [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://aclanthology.org/2025.emnlp-main.249.pdf))
> The composite ability of an agent to effectively initiate and respond to collaborative requests to solve tasks that cannot be completed alone.

**Model coordination** (1 paper: [How to Enable Effective Cooperation Between Humans and NLP Models: A Survey of Principles, Formalizations, and Beyond](https://aclanthology.org/2025.acl-long.22.pdf))
> The latent ability of a model to adapt its behavior dynamically to align with diverse human users during cooperation without prior retraining.

## Relationships

### Associated with
- **Help-seeking** (construct), 1 paper
  > we define collaboration capability as comprising two essential components: the capability to initiate collaboration... and the capability to respond to collaboration... (Section 3.1)
  - [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://aclanthology.org/2025.emnlp-main.249.pdf)
- **Text generation quality** (construct), 1 paper
  > "we identify an inherent phenomenon we term the collaborativeness of LLMs — wherein an LLM tends to generate better responses when presented with outputs from other models"
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
