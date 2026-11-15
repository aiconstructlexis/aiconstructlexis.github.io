# Jailbreak prompt generation
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Harmful instruction generation, Jailbreak generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is the generation of malicious or harmful prompts meant to make another model produce unsafe content. Most definitions describe outputs that elicit harmful, offensive, or malicious responses, or that rephrase a harmful query into a more robust jailbreak prompt that bypasses safety defenses. A smaller line of work states this more formally as producing adversarial text inputs that preserve malicious intent while circumventing safety alignment, including an m-step transformation from a malicious input to xjailbreak such that J(M(xjailbreak), xmalicious) = 1.

**Variants.** Papers use several closely related names for this behavior, most often harmful instruction generation, jailbreak prompt generation, and jailbreak generation. It is studied as automatic generation from a new harmful query, as iterative transformation of a malicious input, and as production of diverse malicious instructions through adversarial phrasing or role-playing scenarios. Some work also varies personas and attributes to guide instruction generation, and one quoted passage mentions malicious instructions generated either automatically with LLMs or manually by experts.

**Space of elicitation and scores.** No measurement instrument is linked to it in the papers. Instead, operationalization is described directly through the outputs themselves: harmful instructions, a corresponding rephrased robust jailbreak prompt, or an xjailbreak that preserves malicious intent while eliciting a harmful response.

**What it is taken as evidence of.** Papers do not explicitly use this behavior as evidence of multiple constructs. The only linked construct is Natural language understanding, and one paper claims a causal relationship from Natural language understanding to Jailbreak prompt generation. Papers do not link it to other constructs.

## Sources

**Harmful instruction generation** (2 papers: [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf), [TRIDENT: Enhancing Large Language Model Safety with Tri-Dimensional Diversified Red-Teaming Data Synthesis](https://aclanthology.org/2025.acl-long.733.pdf))
> The observable behavior of an LLM producing prompts or instructions that are designed to elicit harmful, offensive, or malicious responses from another model.

**Jailbreak prompt generation** (1 paper: [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf))
> The automatic generation of a rephrased, robust version of a malicious query designed to bypass safety defenses.

**Jailbreak generation** (1 paper: [An Interpretable N-gram Perplexity Threat Model for Large Language Model Jailbreaks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boreiko25a/boreiko25a.pdf))
> Producing adversarial text inputs that preserve malicious intent while circumventing safety alignment to elicit harmful responses from an LLM.

## Relationships

### → Jailbreak prompt generation
- **Natural language understanding** (construct): *causes*, 1 paper
  > we can fine-tune an existing language model, turning it into a robust jailbreak prompt generator by leveraging LLMs’ advanced language understanding and generation abilities. (INTRODUCITON)
  - [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf)
