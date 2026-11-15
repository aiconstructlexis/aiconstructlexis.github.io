# Overthinking
**Type:** Behavioral indicator  
**Supporting papers:** 10  

## State of the Field

**Space of definitions.** Across the surveyed work, overthinking is most commonly treated as an observable pattern of excessive, verbose, or redundant reasoning, especially on simple problems, with papers describing excessive reasoning steps, redundant solutions, and inefficient token use that raise computational cost. A smaller line of work uses the same label for conversational search, where it refers to overly detailed or redundant clarification questions that drift from the user’s original intent and add superfluous steps. Some papers also define it by outcome rather than form, treating it as a failure mode in which additional reasoning episodes do not improve, and can sometimes degrade, final answer accuracy; separately, one paper claims a causal relationship from Chain of thought to Overthinking, describing CoT as often leading to unnecessarily long and verbose reasoning traces.

**Variants.** Papers study this behavior in a few recurring settings. The prevailing usage is simple reasoning tasks, including mathematical benchmarks, where overthinking appears as redundant solutions that contribute little to accuracy or reasoning diversity and are reported to occur more often on simple problems. Another variant appears in iterative conversational search, where the behavior is framed as redundant clarification and rewriting steps, and some authors explicitly call it the overthinking problem, phenomenon, or issue.

**Space of elicitation and scores.** No measurement instrument is linked to it. Rather than tying overthinking to a named instrument, papers describe it through observable traces and outcomes: overly long or redundant reasoning processes, redundant steps in an iterative process, inefficient use of generated tokens, and cases where accuracy does not increase, or sometimes declines, with each added episode.

**What it is taken as evidence of.** Papers do not converge on a construct that overthinking directly measures. The only linked construct is Reasoning diversity, and the recorded relationship is that Overthinking is related to it: one paper reports that overthinking patterns lack diversity in reasoning strategies while contributing minimally to accuracy. No other construct is linked in the recorded relationships.

## Sources

**Overthinking** (2 papers: [MuTIS: Enhancing Reasoning Efficiency through Multi Turn Intervention Sampling in Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.690.pdf), [Optimizing Test-Time Compute via Meta Reinforcement Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qu25g/qu25g.pdf))
> An observable tendency for a model to generate excessively verbose and redundant thinking processes, especially for simple tasks, leading to high computational cost.

## Relationships

### → Overthinking
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > However, this approach [chain-of-thought (CoT) reasoning] often leads to unnecessarily long and verbose reasoning traces, resulting in high inference cost and latency. This overthinking phenomenon has become a practical bottleneck... (Introduction)
  - [Answer Convergence as a Signal for Early Stopping in Reasoning](https://aclanthology.org/2025.emnlp-main.904.pdf)

### Associated with
- **Reasoning diversity** (construct), 1 paper
  > Across extensive analyses of mathematical benchmarks, we found these overthinking patterns: (1) contribute minimally to improving accuracy, (2) lack diversity in reasoning strategies, and (3) occur more frequently with simple problems.
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
