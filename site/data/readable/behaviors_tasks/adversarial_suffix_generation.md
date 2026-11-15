# Adversarial suffix generation
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this behavior as generating a text suffix that is appended to a harmful query or user instruction so a target or victim model gives a non-refused response. Most descriptions frame success as producing harmful, undesirable, or otherwise unintended output, while some state the goal more narrowly as making the model begin its response with a target phrase, and others describe it as increasing the likelihood of a harmful response by bypassing safety mechanisms or safety alignment.

**Variants.** Papers study it in several settings: as autoregressive suffix generation, as training an adversarial prompter or ADV-LLM to produce a successful adversarial suffix, and as a universal and transferable attack. The names used include adversarial suffixes, successful adversarial suffix, adversarial prompting, and adversarial prompter. Specific generation setups mentioned include simple decoding with beam search, and attack algorithms such as GCG, AutoDAN-Liu, and SCAV; another description presents GCG as combining affirmative prompting with greedy and gradient-based discrete optimization.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. In practice, papers operationalize it by appending the generated suffix to a harmful query or instruction and checking whether the target model stops refusing, begins with a target phrase, or produces harmful, undesirable, or unintended output.

**What it is taken as evidence of.** Papers do not link this behavior to any construct, so there is no prevailing construct-level interpretation attached to it here. Instead, one paper relates it to Jailbreaking, stating that jailbreaking attacks typically involve appending adversarial suffixes to instructions.

## Sources

**Adversarial suffix generation** (4 papers: [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf), [Iterative Self-Tuning LLMs for Enhanced Jailbreaking Capabilities](https://aclanthology.org/2025.naacl-long.297.pdf), [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf), [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf))
> The process by which an LLM generates a text suffix that, when appended to a harmful query, causes a victim model to produce a non-refused response to that query.

## Relationships

### Associated with
- **Jailbreaking** (behavioral indicator), 1 paper
  > Jailbreaking attacks typically involve appending adversarial suffixes to instructions.
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
