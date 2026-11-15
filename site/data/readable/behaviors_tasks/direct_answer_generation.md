# Direct answer generation
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Direct solution generation, Direct answer prediction  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as producing only a final answer, solution, or plan, with no intermediate reasoning steps, traces, or shown work. Definitions are closely aligned on this point, whether the behavior is framed as direct answer generation, direct solution generation, or direct answer prediction. Some formulations also specify concise outputs, such as a short answer or giving an option letter directly.

**Variants.** Papers place this behavior in several settings. One line contrasts it with step-by-step reasoning in contextual question answering, another presents it as a fast mode that outputs only the solution, and another uses prompts for short-answer or multiple-choice responding, including answering with the option letter directly. The naming varies across these settings, but the observable pattern remains the same: the model returns the final response without visible reasoning.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers, it is instead elicited through prompt instructions and mode settings, such as asking for a short answer, asking for the option letter directly, or invoking a fast mode that outputs only the solution.

**What it is taken as evidence of.** No construct is linked to it. Accordingly, the papers do not explicitly treat this behavior as evidence of a particular construct, and there is no recorded agreement or disagreement to summarize about what it reflects.

## Sources

**Direct answer generation** (1 paper: [T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.185.pdf))
> An observable answering behavior where the model produces a final answer without showing intermediate reasoning steps.

**Direct solution generation** (1 paper: [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf))
> Producing only the final answer or plan without any intermediate reasoning steps or traces.

**Direct answer prediction** (1 paper: [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf))
> Generating a concise final answer without intermediate reasoning, typically in response to prompts asking for short or multiple-choice responses.
