# Time series forecasting
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Time-series forecasting, Context-aided forecasting, Few-shot forecasting, Zero-shot forecasting  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is predicting future data points or values in a sequence from historical observations. Success is usually framed as producing the next value or values at future time steps, often described as forecasting the next H timestamps or the next n values; some formulations specify multivariate or univariate series, and one prompting setup asks for continuing the sequence without any additional text. A smaller line of work narrows the behavior to forecasts that change when relevant textual context accompanies the numerical history.

**Variants.** Papers study several variants under this label. Common variants include multivariate time-series forecasting, next-value prediction, and long-term versus short-term forecasting; additional settings are few-shot forecasting, where only a small fraction of the available training data is used, and zero-shot forecasting, where forecasting is done on a target dataset or domain without training on its data, often in source-to-target setups. Some work also uses the name context-aided forecasting for cases where accurate forecasts depend on both numerical sequences and accompanying text.

**Space of elicitation and scores.** Papers measure this behavior with 4 instruments. Weather appears most often, followed by ETTh1, ETTm1, and M4; Weather, ETTh1, and ETTm1 are described as benchmark or real-world datasets used to evaluate forecasting performance, while M4 appears as a competition setting used in transfer learning experiments. Overall, the linked instruments are dataset-style evaluation benchmarks rather than separate scoring rubrics.

**What it is taken as evidence of.** Papers do not present time series forecasting as directly measuring a construct. The 3 linked constructs instead appear in relationships directed toward forecasting or alongside it: in-context learning is the most recurrent connection, with some papers claiming a causal relationship from in-context learning to time series forecasting and others simply relating the two, while smaller lines of work claim causal relationships from contextual understanding and from knowledge transfer to time series forecasting. No linked construct is stated as what forecasting itself evidences.

## Sources

**Time series forecasting** (4 papers: [TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting](https://proceedings.iclr.cc/paper_files/paper/2024/file/5132940b1bced8a7b28e9695d49d435a-Paper-Conference.pdf), [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf), [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf), [Enhancing LLM Reasoning via Vision-Augmented Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/328c922d068dd4ccb23cec5c64e6c7fc-Paper-Conference.pdf))
> The observable task of predicting future data points in a sequence based on historical observations.

**Time-series forecasting** (1 paper: [Density estimation with LLMs: a geometric investigation of in-context learning trajectories](https://proceedings.iclr.cc/paper_files/paper/2025/file/380afe1a245a3b2134010620eae88865-Paper-Conference.pdf))
> The task of predicting future values in a sequence of numerical data points based on past observations provided in context.

**Context-aided forecasting** (1 paper: [Context is Key: A Benchmark for Forecasting with Essential Textual Information](https://raw.githubusercontent.com/mlresearch/v267/main/assets/williams25a/williams25a.pdf))
> Generating forecasts that change when relevant textual context is provided in addition to the numerical history.

**Few-shot forecasting** (1 paper: [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf))
> The task of performing time series forecasting using only a small fraction of the available training data.

**Zero-shot forecasting** (1 paper: [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf))
> The task of performing time series forecasting on a target dataset without having been trained on any of its data, typically by training on a different source dataset.

## Relationships

### Time series forecasting →
- **Weather** (measurement instrument): *measured_by*, 3 papers
  > We evaluate on 8 benchmark datasets from various domains: ETTh1, ETTh2, ETTm1, ETTm2, Electricity, Weather, Exchange, and ILI, which have been widely adopted for evaluating time series forecasting performance. (Section 4)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
  - [Are Language Models Actually Useful for Time Series Forecasting?](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ed5bf446f59e2c6646d23058c86424b-Paper-Conference.pdf)
  - [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf)
- **ETTh1** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on 8 benchmark datasets from various domains: ETTh1, ETTh2, ETTm1, ETTm2, Electricity, Weather, Exchange, and ILI, which have been widely adopted for evaluating time series forecasting performance. (Section 4)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **ETTm1** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on 8 benchmark datasets from various domains: ETTh1, ETTh2, ETTm1, ETTm2, Electricity, Weather, Exchange, and ILI, which have been widely adopted for evaluating time series forecasting performance. (Section 4)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **M4** (measurement instrument): *measured_by*, 1 paper
  > We conduct the transfer learning between the M3 and M4 competitions, both of which encompass abundant temporal variation patterns but follow different data distributions. (Section 4.2)
  - [AutoTimes: Autoregressive Time Series Forecasters via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)

### → Time series forecasting
- **In-context learning** (construct): *causes*, 3 papers
  > DICL projects trajectories into a disentangled feature space before performing zero-shot forecasting using a pre-trained LLM and in-context learning.
  - [Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf)
  - [From News to Forecast: Integrating Event Analysis in LLM-Based Time Series Forecasting with Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/6aef8bffb372096ee73d98da30119f89-Paper-Conference.pdf)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **Knowledge transfer** (construct): *causes*, 1 paper
  > We attribute the performance gains of TIME-FFM to the valid knowledge transferability across domains. (Section 4.3)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **Contextual understanding** (construct): *causes*, 1 paper
  > In these scenarios, Context-Alignment paradigm provides a robust contextual prior, enabling accurate logical and structural understanding that enhances the potential of LLMs for cross-domain TS processing. (Section 4.5)
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)

### Associated with
- **Few-shot task performance** (behavioral indicator), 1 paper
  > Based on the settings in Zhou et al. (2023), we present few-shot forecasting for 10% time steps in training datasets. (Section 4.2)
  - [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
