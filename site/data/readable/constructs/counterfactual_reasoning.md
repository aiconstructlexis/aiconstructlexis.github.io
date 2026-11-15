# Counterfactual reasoning
**Type:** Construct  
**Supporting papers:** 21  
**Also known as:** Counterfactual thinking, Counterfactuality  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats counterfactual reasoning as the ability or capacity to reason in hypothetical or what-if scenarios, usually by considering alternative outcomes under changed conditions or what would have happened if a past event had been different. Several definitions tie it directly to causal reasoning, including simulating outcomes under conditions contrary to what actually happened and describing it as a distinctive feature of causal reasoning. Smaller variants rename it as counterfactual thinking or counterfactuality, and one paper places counterfactuality at the third and highest level of Pearl's causal hierarchy. A minority usage shifts from latent ability to observable behavior, and a few papers apply the label to settings such as imagined edited premises, long-term decision re-evaluation, or counter-factual knowledge sets.

**Space of facets.** Papers use counterfactual reasoning, counterfactual thinking, and counterfactuality for closely overlapping what-if reasoning, but they break it into several recurring forms: answering what-if questions, hypothesizing alternative consequences, exploring what would have happened if a particular past event were different, revising a past choice after observing its outcome, and evaluating how alternative decisions affect long-term outcomes and credit assignment. It is most commonly positioned within causal reasoning, and one paper explicitly places counterfactuality at the top level of Pearl's causal hierarchy. A separate paper also places counterfactual tasks inside a broader visual reasoning suite alongside spatial, temporal, predictive, and causal tasks.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Instead, papers make it concrete through task formats described in the quoted passages: answering what-if questions, analyzing outcomes by hypothesizing alternative scenarios, revising a decision after seeing its first outcome, testing reasoning under an imagined edited premise, and re-evaluating the long-term impact of decisions. These task descriptions generally match the dominant definition of hypothetical-scenario reasoning, though a few operationalizations are narrower, such as using a counter-factual knowledge set to refine answers or framing it as trajectory-level credit assignment.

**Links.** Among linked constructs, papers most often relate counterfactual reasoning to causal reasoning: they describe it as a task within causal reasoning and as closely tied to understanding cause and effect. One paper relates it to reasoning more broadly by requiring consistency when queries are framed counterfactually, and another relates it to visual reasoning by listing counterfactual tasks within a visual reasoning suite. A separate paper claims a causal relationship from counterfactual reasoning to robustness, stating that explicitly modeling counterfactual reasoning in multimodal contexts enhances model robustness.

## Sources

**Counterfactual reasoning** (5 papers: [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf), [SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/693ce820ea7e0f0c70a2a833cbdf7ccc-Paper-Conference.pdf), [Com2 : A Causal-Guided Benchmark for Exploring Complex Commonsense Reasoning in Large Language Models](https://aclanthology.org/2025.acl-long.785.pdf), [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf), [Language Models as Causal Effect Generators](https://aclanthology.org/2025.emnlp-main.107.pdf))
> The ability to reason within hypothetical scenarios, which is a distinctive feature of causal reasoning.

**Counterfactual thinking** (2 papers: [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf), [Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cu/li25cu.pdf))
> The ability to consider alternative outcomes by reasoning about what would happen under changed conditions.

**Counterfactuality** (1 paper: [Gumbel Counterfactual Generation From Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e15790966a4a9d85d688635c88ee6d8a-Paper-Conference.pdf))
> The capacity to reason about what would have happened if past events had unfolded differently, representing the third and highest level of Pearl's causal hierarchy.

## Relationships

### Counterfactual reasoning →
- **Robustness** (construct): *causes*, 1 paper
  > we propose DPCI, a novel Dual-Path Counterfactual Integration framework that enhances model robustness by explicitly modeling counterfactual reasoning in multimodal contexts. (Abstract)
  - [Dual-Path Counterfactual Integration for Multimodal Aspect-Based Sentiment Classification](https://aclanthology.org/2025.emnlp-main.1158.pdf)

### Associated with
- **Causal reasoning** (construct), 2 papers
  > Counterfactual reasoning is an essential task of causal reasoning. (Section 2.2)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [Language Models as Causal Effect Generators](https://aclanthology.org/2025.emnlp-main.107.pdf)
- **Visual reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reasoning** (construct), 1 paper
  > to evaluate the reasoning abilities of the LLM, it is crucial that this consistency is also observed when the queries are framed in a counterfactual manner.
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
