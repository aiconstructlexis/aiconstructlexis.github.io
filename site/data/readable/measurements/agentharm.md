# AgentHarm
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across papers, the prevailing framing is a safety benchmark, though its content is described in two ways. One description presents it as 110 malicious tasks for general agents, designed to evaluate general agent safety and vulnerability to harmful instructions. Another describes it as providing detailed safety measurements for tool-using LLMs through 176 examples, including harmful and benign samples and multi-step trajectories with harmful tool outputs to test refusal behavior.

**What it is claimed to measure.** Papers use it to measure two constructs, Harmlessness and Safety, and no behavioral indicators are linked to it. One line of work reports that Harmlessness is measured by AgentHarm, describing it as a benchmark proposed for measuring harmfulness in LLM agents, while another reports that Safety is measured by AgentHarm, saying it measures the potential harm from agents executing malicious tasks. The reported uses therefore span two construct labels rather than centering on a single one.

**Space of uses.** Papers position it as an evaluation benchmark rather than alongside other named instruments, and no other measurement instrument is linked to it. In ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning, it appears in the setup as AgentHarm, "comprising 110 malicious tasks designed for general agents." In ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations, the authors write, "We also created an AgentHarm benchmark to test model safety with multi-step tools whose outputs contain harmful content," using it to test refusal behavior with harmful and benign examples.

## Sources

**AgentHarm** (2 papers: [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf), [ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations](https://aclanthology.org/2025.emnlp-main.714.pdf))
> A benchmark comprising 110 malicious tasks designed to evaluate general agent safety and vulnerability to harmful instructions.

## Relationships

### → AgentHarm
- **Harmlessness** (construct): *measured_by*, 1 paper
  > AgentHarm (Andriushchenko et al., 2024b) is a benchmark proposed for measuring such harmfulness in LLM agents based on Inspect AI (UK AI Safety Institute, 2024).
  - [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > AgentHarm (Andriushchenko et al., 2024) measures the potential harm from agents executing malicious tasks.
  - [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf)
