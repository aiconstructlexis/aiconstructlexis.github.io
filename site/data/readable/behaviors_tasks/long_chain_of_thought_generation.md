# Long chain-of-thought generation
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Long Chain-of-Thought reasoning, Long chain-of-thought reasoning  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats this behavior as producing an extended sequence of reasoning tokens or traces before the final answer, with longer, more detailed, step-by-step outputs than standard chain-of-thought. Most descriptions add explicit reasoning actions such as planning, validation, reflection, verification, backtracking, and subproblem decomposition, and some papers further describe it as deliberate or deep thinking. A smaller line of work treats it as an emergent capability for deep, structured natural language reasoning before formal outputs.

**Variants.** Papers usually refer to the behavior as long CoT or long chain-of-thought reasoning. Most study it as general extended reasoning trajectories, though some place it in natural-formal hybrid settings, where natural language reasoning is used before or in integration with formal language outputs, including Lean code interaction, theorem proving, and math settings.

**Space of elicitation and scores.** No measurement instrument is linked to it in the recorded relationships. Across the papers, the behavior is described directly through the form of the output, such as extended reasoning tokens or traces, rather than through a named elicitation or scoring instrument.

**What it is taken as evidence of.** The construct-level links are not concentrated on a single construct: papers name two linked constructs, Formal reasoning and Generalization, and both are recorded as causal claims from long chain-of-thought generation. Some papers also claim causal links from the behavior to Backtracking, Self-correction, and Theorem proving.

## Sources

**Long chain-of-thought generation** (3 papers: [Unlocking General Long Chain-of-Thought Reasoning Capabilities of Large Language Models via Representation Engineering](https://aclanthology.org/2025.acl-long.339.pdf), [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf), [Through the Valley: Path to Effective Long CoT Training for Small Language Models](https://aclanthology.org/2025.emnlp-main.251.pdf))
> The observable production of extended reasoning traces that include planning, validation, and backtracking, resulting in longer and more detailed outputs compared to standard chain-of-thought.

**Long Chain-of-Thought reasoning** (1 paper: [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf))
> The emergent capability of a model to perform deep, structured natural language reasoning before generating formal outputs, enabling high-level planning and self-reflection in problem solving.

**Long chain-of-thought reasoning** (1 paper: [Let's Reason Formally: Natural-Formal Hybrid Reasoning Enhances LLM's Math Capability](https://aclanthology.org/2025.emnlp-main.850.pdf))
> The ability to generate extended, coherent, and step-by-step reasoning processes to solve complex problems.

## Relationships

### Long chain-of-thought generation →
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > A proven approach for scaling inference compute is to generate long chains-of-thought (CoTs), enabling models to engage in structured reasoning strategies such as backtracking and error correction. (Abstract)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > A proven approach for scaling inference compute is to generate long chains-of-thought (CoTs), enabling models to engage in structured reasoning strategies such as backtracking and error correction. (Abstract)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > SFT initialization matters: high-quality, emergent long CoT pattern leads to significantly better generalization and RL gains. (Takeaway 3.3)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Formal reasoning** (construct): *causes*, 1 paper
  > Extensive experiments demonstrate that MA-LoT framework effectively enhances the model’s formal reasoning ability through model-collaboration design and emergent formal reasoning in Long CoT. (Section 1)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)
- **Theorem proving** (behavioral indicator): *causes*, 1 paper
  > The emergent Lean reasoning ability in the Long CoT enables the model to write a better-structured proof based on its high-level plan than direct proof generation. (Section 2.3.1)
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)
