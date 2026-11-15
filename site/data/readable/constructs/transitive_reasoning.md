# Transitive reasoning
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Transitive inference, Inductive generalization  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this concept as an ability to derive a new or unobserved relation from composed relations. Papers describe it as deducing reachability through concatenated path segments not directly seen in training, inferring a relation through a common intermediate entity, or reasoning from X → Y and Y → Z to the transitive relation X → Z. A smaller competing usage appears under the nearby label "inductive generalization," where the focus is instead on effectively using previously unseen agentic operators during inference and generalizing beyond training-time configurations.

**Space of facets.** Papers organize the idea around different targets of transitivity rather than a single shared subtype. The same family of terms covers reachability and path concatenation, hierarchical or "multi-hop" subsumptions, and transitive causal relations, and one paper places transitive inference under Reasoning by describing it as a fundamental form of reasoning. The clearest naming mismatch is that "inductive generalization" is used both for transitive causal reasoning and for use of unseen agentic operators, so nearby labels are not fully aligned in scope.

**Space of measurement.** Operationalization is sparse in the papers. No measurement instrument is linked to transitive reasoning, and no behavioral indicator is linked to it. Instead, papers refer to it as a capability to be assessed or simulated, for example by inferring "multi-hop" subsumptions or by observing failures in generating paths when concatenation is required, but no benchmark, human evaluation, LLM-as-a-judge procedure, probe, or analysis is linked to it.

**Links.** Among the papers, the only explicit link is that Reasoning is related to transitive reasoning. In that usage, one paper describes transitive inference as a fundamental form of reasoning in which a relational conclusion can be inferred from premises. No causal or correlational links are recorded.

## Sources

**Transitive reasoning** (1 paper: [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf))
> The ability to deduce reachability relationships through the concatenation of path segments that were not directly observed in the training data.

**Transitive inference** (1 paper: [Language Models as Hierarchy Encoders](https://proceedings.neurips.cc/paper_files/paper/2024/file/1a970a3e62ac31c76ec3cea3a9f68fdf-Paper-Conference.pdf))
> The ability to deduce a new relationship between two entities based on their relationships with a common intermediate entity (e.g., if A is a B, and B is a C, then A is a C).

**Inductive generalization** (2 papers: [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf), [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf))
> The ability to reason about a transitive causal relationship (A → C) after being shown examples of its constituent parts (A → B and B → C).

## Relationships

### Associated with
- **Reasoning** (construct), 1 paper
  > TI is a fundamental form of reasoning in which, given some premises, a relational conclusion between stimuli can be inferred. For example, if A is greater than B and B is greater than C, then A must, transitively, be greater than C. TI has historically been used to evaluate the reasoning ability of young pre-verbal children (Burt et al., 1911), but has also been well studied throughout the animal kingdom, from rats (Roberts & Phelps, 1994) to wasps (Tibbetts et al., 2019).
  - [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf)
