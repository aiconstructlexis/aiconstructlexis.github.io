# Misalignment
**Type:** Construct  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the uses, papers apply misalignment in two distinct ways. One usage treats it as a latent unsafe tendency, or safety misalignment, in the model that can stay dormant in a full-precision setting and become exploitable in another setting, such as post-quantization, leading to harmful outputs. Another usage treats misalignment as the model's failure to follow instructions and produce valid, actionable outputs in a domain task, illustrated by broken or incomplete navigation routes and omission of initial absolute directional guidance. The disagreement is whether misalignment is framed as a latent property of the model or as an observable failure in its outputs.

**Space of facets.** The papers distinguish a few named forms of misalignment. One paper specifies quantization-conditioned misalignment, where safety misalignment is latent in a full-precision model and activates after quantization; another refers to obvious misalignment in route generation, tied to failing to identify information needed for valid routes. Across these uses, the term spans both dormant safety tendencies and overt output deficiencies.

**Space of measurement.** No measurement instrument is linked to it, and one behavioral indicator is linked, Jailbreaking. In direct operational use, one paper says it uses misalignment to measure model performance at outputting valid instructions, treating invalid, broken, or incomplete routes, especially omission of initial absolute directional guidance, as manifestations of misalignment. This operationalization matches the output-failure definition, while the latent safety framing is not tied here to a named instrument.

**Links.** The only reported link is a causal one from Misalignment to Jailbreaking. One paper claims that when these misalignments activate, they render the model vulnerable to jailbreak attacks. No correlational or other related links are reported.

## Sources

**Misalignment** (2 papers: [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf), [TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route](https://aclanthology.org/2025.emnlp-main.440.pdf))
> A latent unsafe tendency in the model that can be hidden in one setting and activated in another, leading to harmful outputs.

## Relationships

### Misalignment →
- **Jailbreaking** (behavioral indicator): *causes*, 1 paper
  > “these misalignments activate, rendering the model vulnerable to jailbreak attacks.”
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
