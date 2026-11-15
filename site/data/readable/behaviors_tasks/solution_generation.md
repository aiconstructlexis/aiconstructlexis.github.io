# Solution generation
**Type:** Behavioral indicator  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this behavior as the observable production of a candidate solution for a given problem or prompt. Papers agree on that core task, though they often formulate it as generating multiple candidate solutions rather than only one, and one paper places those candidates in a later ranking step where a verifier picks the most suitable solution.

**Variants.** The main variants concern the collection of multiple outputs and the emphasis on diversity. Papers describe candidate solutions, diverse model-generated solutions, and single-problem settings where many solutions are gathered for later comparison.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it by prompting models to generate candidate solutions, sometimes explicitly seeking diverse outputs, and one paper then has a learned reward model, referred to as a verifier, rank the generated solutions and select the most suitable one.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not specify a broader construct that this behavior is taken to indicate.

## Sources

**Solution generation** (2 papers: [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf), [Unleashing the Reasoning Potential of LLMs by Critique Fine-Tuning on One Problem](https://aclanthology.org/2025.emnlp-main.149.pdf))
> The observable task of an LLM producing a candidate solution in response to a given problem.
