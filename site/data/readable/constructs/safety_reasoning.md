# Safety reasoning
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Safety-aware reasoning  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing framing is a latent internal process or ability for making safety decisions during generation, especially determining whether a request is harmful and choosing a safe course of action. Some papers broaden this by describing the ability to analyze explicit and implicit intents in multimodal inputs, reconstruct the user’s genuine request, and assess potential risks before responding. A smaller line of work, using the name Safety-aware reasoning, emphasizes integrating safety evaluation into each reasoning step, with self-monitoring and dynamic adjustment of responses based on safety status.

**Space of facets.** The papers do not provide a formal taxonomy, but they repeatedly describe the construct through recurring components: harm detection, safe action selection, intent analysis, request reconstruction, risk assessment, and safety-aware reflection at each step of reasoning. They also use both Safety reasoning and Safety-aware reasoning for closely aligned latent capabilities embedded in the reasoning process. The main variation is scope, with some descriptions centering on deciding whether to refuse or respond safely, and others extending to multimodal intent reconstruction and stepwise monitoring during generation.

**Space of measurement.** No measurement instrument is linked to it. The only linked behavioral indicator is Chain of thought, and the surrounding descriptions operationalize the construct through step-by-step analysis, self-improving chain-of-thought reasoning with safety awareness, chain-of-thought-based safety decision-making capabilities, and safety-aware reflections in each reasoning step. This operationalization matches the dominant definitions, which describe a latent reasoning process rather than a standalone output label.

**Links.** One paper reports that Chain of thought is related to Safety reasoning, describing identification of safety risks through step-by-step analysis with safety-aware chain-of-thought reasoning. One paper also claims a causal relationship from Helpfulness to Safety reasoning.

## Sources

**Safety reasoning** (2 papers: [Safety Alignment Can Be Not Superficial With Explicit Safety Signals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25av/li25av.pdf), [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf))
> The latent cognitive process by which a model determines whether a request is harmful and decides on an appropriate, safe course of action.

**Safety-aware reasoning** (1 paper: [Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://aclanthology.org/2025.emnlp-main.1493.pdf))
> The latent ability of a model to integrate safety evaluation into its reasoning process, enabling self-monitoring and dynamic adjustment of responses based on safety status at each step.

## Relationships

### → Safety reasoning
- **Helpfulness** (construct): *causes*, 1 paper
  > Moreover, benefiting from the decomposed problem-solving in reasoning, STAIR mitigates safety-performance trade-offs and gets improvements in multiple dimensions, including helpfulness, truthfulness, robustness, and privacy awareness. (Section 1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)

### Associated with
- **Chain of thought** (behavioral indicator), 1 paper
  > “We enable LLMs to identify safety risks through step-by-step analysis by self-improving chain-of-thought (CoT) reasoning with safety awareness.”
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
