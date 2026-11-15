# Abstraction
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Symbolic abstraction, Logical abstraction, Problem abstraction  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats abstraction as the ability to move from specific instances or detailed information to general concepts, principles, high-level patterns, or summaries. Several definitions converge on this broad framing, including extracting common features from examples and operating on concepts independently of surface details. A smaller line of work narrows the term to symbolic or logical abstraction, where the focus is formal symbolic representation or access to a problem's underlying symbolic structure apart from lexical content. One paper instead uses problem abstraction for simplifying and conceptually representing a problem's core components, so the main variation is between a broad concept-forming capacity and narrower structure-focused reasoning skills.

**Space of facets.** There is no shared subtype scheme, but papers repeatedly distinguish symbolic abstraction, logical abstraction, and problem abstraction under the broader label. These variants differ mainly in what is being abstracted: natural-language problems into formal symbolic systems such as first-order logic, lexical content into logical structure, or full problems into simplified core components. Elsewhere, abstraction is discussed alongside long-text understanding, reasoning, and systematic generalization, and one paper describes transformer architectures as seeking a greater capacity for efficient induction of abstractions.

**Space of measurement.** No measurement instrument is linked to abstraction, and the only linked behavioral indicator is theorem proving, which is related to it rather than used to measure it. Still, papers describe benchmark and task setups for it: a two-part puzzle benchmark with obfuscated variants to test abstraction from lexical content to logical structure, downstream tasks inspired by ARC that were designed to quantify reasoning, abstraction, and long-term prediction, and Symbolic ReAct trajectories formalized in first-order logic. These operationalizations mostly match the narrower definitions that emphasize symbolic or logical structure over surface form, while the broader framing as high-level summary or concept extraction is described without a linked instrument.

**Links.** Only a few explicit links are reported. Individual papers claim a causal relationship from abstraction to reasoning, knowledge transfer, and generalization, with the evidence stating that grounding on high-level concepts and principles lets LLMs leverage intrinsic reasoning capabilities, that "higher levels of abstraction implies more flexible transfer," and that abstraction enables reasoning and generalization in novel contexts. Another paper claims a causal relationship from relational reasoning to abstraction, describing relational reasoning as underlying abstraction and systematic generalization. Separately, one paper relates abstraction to theorem proving, noting that in interactive theorem proving abstractions can be encapsulated in new definitions, lemmas, and tactics.

## Sources

**Abstraction** (3 papers: [Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering](https://aclanthology.org/2025.emnlp-main.788.pdf), [Intelligence at the Edge of Chaos](https://proceedings.iclr.cc/paper_files/paper/2025/file/d791394d32c428aecc7a5b101fb47799-Paper-Conference.pdf), [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf))
> The capacity to identify and represent general concepts, principles, or high-level summaries from specific instances or detailed information.

**Symbolic abstraction** (1 paper: [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf))
> The ability to represent reasoning problems using formal symbolic systems (e.g., first-order logic) that capture structural relationships independent of natural language content.

**Logical abstraction** (1 paper: [Lexical Recall or Logical Reasoning: Probing the Limits of Reasoning Abilities in Large Language Models](https://aclanthology.org/2025.acl-long.664.pdf))
> The ability to identify and operate on the underlying symbolic structure of a problem, separating it from its surface-level lexical representation.

**Problem abstraction** (1 paper: [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf))
> A higher-order reasoning skill involving the simplification and conceptual representation of a problem's core components.

## Relationships

### Abstraction →
- **Reasoning** (construct): *causes*, 1 paper
  > Grounding on the high-level concepts and principles, LLMs can leverage their intrinsic Reasoning capabilities to derive the solution. (Section 7)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Knowledge transfer** (construct): *causes*, 1 paper
  > Higher levels of abstraction implies more flexible transfer
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > The ability to abstract, which is often seen as a human-specific trait, enables reasoning, generalization, and problem-solving in novel contexts
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)

### → Abstraction
- **Relational reasoning** (construct): *causes*, 1 paper
  > Relational reasoning is a central component of generally intelligent systems and is believed to underlie human abilities for abstraction and systematic generalization (Section 1).
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)

### Associated with
- **Theorem proving** (behavioral indicator), 1 paper
  > In interactive theorem proving, abstractions can be encapsulated in new definitions, lemmas, and tactics. (Section 4.2)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
