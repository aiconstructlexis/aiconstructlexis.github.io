# PGD
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the definitions, PGD is treated as an iterative adversarial attack that repeatedly takes small steps in the gradient direction and projects each update back into a constrained perturbation space. One definition further specifies it as a white-box attack, and some usage is stated specifically as PGD-l∞, where the projection keeps perturbations within ε∞ constraints; papers also describe it as a method for crafting or generating adversarial examples.

**What it is claimed to measure.** The papers do not report PGD as measuring any construct or behavioral indicator, and no linked target construct is identified.

**Space of uses.** One paper explicitly employs PGD-l∞ alongside CW-l2 as two standard adversarial attack methods, while other papers refer to PGD more generally as an iterative approach for crafting adversarial examples.

## Sources

**PGD** (3 papers: [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf))
> Projected Gradient Descent, a white-box iterative adversarial attack that takes multiple small steps in the gradient direction and projects the result back into a constrained space.
