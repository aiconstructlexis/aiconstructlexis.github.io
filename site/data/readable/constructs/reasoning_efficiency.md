# Reasoning efficiency
**Type:** Construct  
**Supporting papers:** 14  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage describes reasoning efficiency as solving a problem with as few reasoning steps or tool calls as possible while avoiding unnecessary exploration. Several definitions make this explicitly process-based, for example by treating it as the number of steps a model takes and its ability to quickly narrow the candidate set. A smaller line of work broadens the construct from step economy to the rational use of computational resources, framing it in terms of inference overhead, response length, or the appropriate level of reasoning complexity for the problem while preserving performance.

**Space of facets.** Some authors describe the construct from both outcome and process perspectives, while others use more specific process-side facets such as step count, tool calls, unnecessary branch explorations, and strategic narrowing of candidates. Another recurring contrast is between minimal-step formulations and broader resource-use formulations, which bring in inference overhead, latency, response length, and computational overhead. One paper also uses the nearby label "inference efficiency" when evaluating avoidance of unnecessary branch explorations.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Even so, papers operationalize it directly in their descriptions: by how many reasoning steps or tool calls a model uses, whether it avoids unnecessary branch exploration, and how much inference overhead or response length it incurs. These operationalizations mostly match the dominant minimal-step or minimal-resource definition, though some descriptions extend them to whether the reasoning complexity is appropriate to the problem and whether overhead is reduced without losing performance.

**Links.** The only linked construct is Chain-of-thought reasoning. One paper claims a causal relationship from Chain-of-thought reasoning to reasoning efficiency, stating that multi-step reasoning with long CoT demands greater computational resources and makes inference practically inefficient.

## Sources

**Reasoning efficiency** (4 papers: [Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf), [GuessArena: Guess Who I Am? A Self-Adaptive Framework for Evaluating LLMs in Domain-Specific Knowledge and Reasoning](https://aclanthology.org/2025.acl-long.534.pdf), [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf), [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf))
> The model's ability to solve a problem using a minimal number of reasoning steps or tool calls, avoiding unnecessary exploration.

## Relationships

### → Reasoning efficiency
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > "Furthermore, multi-step reasoning involving processing long CoT demands greater computational resources, which renders the inference process practically inefficient."
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
