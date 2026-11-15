# Intent understanding
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Speaker meaning inference, Intention inference, Intent perception, Intention awareness, User intent understanding  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing framing is a latent ability to recover an underlying purpose, goal, task, or information need from an utterance, prompt, or interaction sequence, often when that intent is not stated directly. Most definitions place the construct in context-sensitive inference, for example over conversational turns, GUI trajectories, vague or incomplete queries, or instructions that omit the target object or action. Smaller strands narrow the reference standard to pragmatic speaker meaning beyond literal content, to relevance to social and cultural expectations, or to recognizing malicious versus benign requests.

**Space of facets.** The construct appears under several neighboring names, including speaker meaning inference, intention inference, intent perception, intention awareness, and user intent understanding, and one paper says the task is sometimes called goal understanding. Across these uses, papers shift the object of inference, from another person's intentions in interaction, to intended meaning and implications, to intended task, to text-based user intentions for recommendation, or to information need in conversational search. Papers do not explicitly relate it to other named constructs through nesting or contrast.

**Space of measurement.** No named measurement instrument is linked to it, and one behavioral indicator is linked: Harmful content generation. Papers instead operationalize the construct through task setups and probes, including intent extraction from UI interaction trajectories, evaluation of inferring human instructions when the target object or action is omitted, conversational query reformulation that uses the current query plus historical context to clarify user intent, and a prompt-based probe that scores the template "This intent is [MASK]" with prediction logits. These operationalizations generally match the definitions by requiring recovery of intent from context, ambiguity, or incomplete specification.

**Links.** Among the papers summarized, only one explicit link is stated: one paper claims a causal relationship from Intent understanding to Harmful content generation. Its evidence says adversarial sequences can obstruct a model's intent recognition by shifting attention away from malicious-intent tokens, thereby eliciting harmful responses. No correlational or generic related links are reported.

## Sources

**Intent understanding** (2 papers: [Cultural Learning-Based Culture Adaptation of Language Models](https://aclanthology.org/2025.acl-long.156.pdf), [Small Models, Big Results: Achieving Superior Intent Extraction through Decomposition](https://aclanthology.org/2025.emnlp-main.949.pdf))
> The latent ability to infer the underlying purpose or goal behind a conversational turn, particularly in relation to social and cultural expectations, enabling more contextually appropriate responses.

**Speaker meaning inference** (1 paper: [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf))
> Inferring intended meaning, implications, or pragmatic intent behind utterances, beyond literal content.

**Intention inference** (1 paper: [PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf))
> The ability to infer the user's intended task when the instruction does not explicitly name the target object or action.

**Intent perception** (1 paper: [Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf))
> The latent ability of a model to recognize the underlying purpose or intent of an input prompt, particularly in discerning malicious from benign requests.

**Intention awareness** (1 paper: [Language Representations Can be What Recommenders Need: Findings and Potentials](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bab1843c8d5a69f5abfd0824593493-Paper-Conference.pdf))
> The latent capacity to perceive text-based user intentions and refine recommendation results accordingly.

**User intent understanding** (1 paper: [AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.193.pdf))
> The ability to correctly interpret a user's information need from a conversational turn by considering both the current query and the historical context.

## Relationships

### Intent understanding →
- **Harmful content generation** (behavioral indicator): *causes*, 1 paper
  > By incorporating adversarial sequences, these attacks can redirect the source LLM’s focus away from malicious-intent tokens in the original input, thereby obstructing the model’s intent recognition and eliciting harmful responses. (Abstract)
  - [Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf)
