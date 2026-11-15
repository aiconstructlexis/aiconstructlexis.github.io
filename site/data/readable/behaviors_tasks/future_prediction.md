# Future prediction
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Next-state prediction, Observation prediction, State transition prediction, State forecasting  

## State of the Field

**Space of definitions.** Across papers, the common framing treats future prediction as producing the next observation or state from current context, usually a current observation or state together with an action. Definitions differ mainly in output form: some papers ask the model to choose among candidate next observations, others ask it to predict the next observation at each time point in a stochastic sequence, and others frame it as autoregressively predicting the next state and reward. A smaller line of work casts it as either a probabilistic forecast over unknown state values given context or a text description of the next observation after a single-step action.

**Variants.** Papers study several closely related variants under the names observation prediction, next-state prediction, state transition prediction, state forecasting, and future prediction. The settings range from sequential decision making with candidate observations, to stochastic processes such as random walks on a graph, to autoregressive state-and-reward prediction, to uncertainty settings where the output is a probability distribution over state values, and to robot learning where the output is a textual next-observation description.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it directly through task prompts, including selecting between candidate next observations, predicting the next observation at each time point, autoregressively predicting the next state and reward, producing probabilistic forecasts for states, and generating a text description of the next observation.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. The recorded construct links are only related links: one paper relates state forecasting to Calibration by evaluating "the calibration of its state forecasting approach," and another relates predicting the next observation to World modeling by describing a world model that helps an agent "foresee the potential outcome" of its action.

## Sources

**Observation prediction** (1 paper: [On the Modeling Capabilities of Large Language Models for Sequential Decision Making](https://proceedings.iclr.cc/paper_files/paper/2025/file/368cba57d00902c752eaa9e4770bbbbe-Paper-Conference.pdf))
> The observable behavior where the model selects candidate next observations given current state and action.

**Next-state prediction** (1 paper: [Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b594f6dd4931c4af4f12042af8d40ec-Paper-Conference.pdf))
> The task of predicting the next observation in a sequence generated from a stochastic process, such as a random walk on a graph.

**State transition prediction** (1 paper: [Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf))
> Autoregressively predicting the next state and reward given the current state and action.

**State forecasting** (1 paper: [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf))
> The observable task of producing a probabilistic forecast for the values of unknown variables (states) based on provided contextual information.

**Future prediction** (1 paper: [LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://proceedings.iclr.cc/paper_files/paper/2025/file/909f526db5127f8bd8158af32d9e313a-Paper-Conference.pdf))
> The task of generating a textual description of the next observation, given a current observation and a single-step action.

## Relationships

### Associated with
- **Calibration** (construct), 1 paper
  > We evaluate components of DeLLMa, including the calibration of its state forecasting approach and a human agreement study to assess its utility elicitation method. (Section 1).
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **World modeling** (construct), 1 paper
  > this LLM learns the environment dynamics, working as a world model that helps the web agent to foresee the potential outcome (i.e., predict the next observation) of its action. (Section 4.1.3)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
