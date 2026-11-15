# Legal compliance
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Legality  

## State of the Field

**Space of definitions.** Across the definitions, legal compliance is most commonly framed as a latent model-level capacity or disposition to follow legal and regulatory standards. One formulation, under the name "legality," emphasizes understanding and adhering to legal rules when generating responses or instructions, with misalignment described as producing content that "provides unlawful instructions." Another keeps the same latent framing but specifies compliance with GDPR, the EU AI Act, and HIPAA when processing or responding to privacy- and safety-related inputs, so the main difference is broad legality versus regulation-specific privacy and safety compliance.

**Space of facets.** Papers do not offer a detailed subtype scheme. The main naming variation is between "legality" and "legal compliance," used for similar latent properties; one paper places it alongside stereotypes and morality as an aspect of alignment, while another organizes it around three regulatory frameworks and connects it to lawful, safe, and privacy-preserving LLM systems and to contextualized legal reasoning.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. The papers only indicate that legality is assessed in agent-based experiments and that compliance results can be used as rewards for contextualized legal reasoning, without additional named measurement links.

**Links.** The only linked construct is contextual understanding. One paper, PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance, claims a causal relationship from contextual understanding to legal compliance, stating that "better context-understanding abilities further improve legal compliance".

## Sources

**Legality** (1 paper: [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf))
> The model's latent capacity to understand and adhere to legal rules and regulations when generating responses or instructions.

**Legal compliance** (1 paper: [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf))
> The model's latent disposition to adhere to established legal and regulatory standards such as GDPR, EU AI Act, and HIPAA when processing or responding to inputs involving privacy and safety.

## Relationships

### → Legal compliance
- **Contextual understanding** (construct): *causes*, 1 paper
  > Consequently, better context-understanding abilities further improve legal compliance, as indicated by the results of Table 2. (Section 5.2)
  - [PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance](https://aclanthology.org/2025.acl-long.518.pdf)
