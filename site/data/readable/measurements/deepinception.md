# DeepInception
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across the definitions, the prevailing usage treats DeepInception as a manually crafted jailbreak prompt template that uses imaginary scenes and characters to attack target LLMs. One paper describes it as a meticulously crafted manual prompt template that incorporates imaginary scenes with various characters. Other papers use a broader framing, treating it as a jailbreak method or as one of the evaluated state-of-the-art jailbreak attacks.

**What it is claimed to measure.** Papers link DeepInception to one construct, Harmlessness, and to no behavioral indicators. The recorded relationship is that Harmlessness is measured by DeepInception, with supporting evidence coming from an evaluation table that compares harmfulness scores for jailbreak attacks and shows attack success rates in brackets. The measurement claims are therefore concentrated on Harmlessness rather than distributed across multiple constructs.

**Space of uses.** In the usage in the papers examples, papers place DeepInception inside multi-attack evaluations rather than presenting it by itself. One study evaluates it alongside GCG and PAIR, and another lists it with AutoDAN, ReNeLLM, and CodeAttack among jailbreak methods.

## Sources

**DeepInception** (3 papers: [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf))
> A manually crafted jailbreak prompt template that uses imaginary scenes and characters to attack target LLMs.

## Relationships

### → DeepInception
- **Harmlessness** (construct): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including DeepInception (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
