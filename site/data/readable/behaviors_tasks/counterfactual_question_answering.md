# Counterfactual question answering
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Counterfactual query answering, Counterfactual inference  

## State of the Field

**Space of definitions.** Most papers treat this behavior as answering a hypothetical what-would-have-happened question under an intervention or altered condition, rather than answering from observed reality alone. Definitions converge on responding to a query that changes a premise of the problem state, and one paper makes this explicit with interventional templates asking for "the potential effects under interventions do(X = x) or do(X = x')". A smaller formulation casts the same behavior as reasoning about what would have happened in a video under different conditions, such as if an object or event were absent; across these definitions, providing the answer to the counterfactual question or query is the stated success criterion.

**Variants.** Papers use closely related labels for the behavior, including counterfactual question answering, counterfactual query answering, and counterfactual inference. The prevailing variants are question or query formats built around hypothetical interventions or assumed conditions, including a setup that assumes one condition is always true and asks whether X would satisfy another condition under that assumption. Another variant appears in video understanding, where the counterfactual asks what would have happened if a depicted object or event were absent.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers describe eliciting it through interventional question templates, counterfactual prompts, and a counterfactual dataset that assumes a condition and records whether X would satisfy another condition under that assumption.

**What it is taken as evidence of.** Papers link it to one construct, causal reasoning. The link is recorded as related, not as measured_by, causal, or correlational: one paper states that "causal reasoning through counterfactual question answering is lacking," treating counterfactual question answering as connected to causal reasoning. No other construct link is reported.

## Sources

**Counterfactual question answering** (1 paper: [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf))
> The observable behavior of providing an answer to a question about what would have happened under a hypothetical intervention or condition that differs from the observed reality.

**Counterfactual query answering** (1 paper: [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf))
> The observable behavior of responding to a query about a hypothetical scenario that requires altering a premise of the problem state.

**Counterfactual inference** (1 paper: [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> The task of reasoning about what would have happened in a video under different conditions (i.e., if a certain object or event were absent).

## Relationships

### Associated with
- **Causal reasoning** (construct), 1 paper
  > “causal reasoning through counterfactual question answering is lacking”
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
