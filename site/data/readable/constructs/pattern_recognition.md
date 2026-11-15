# Pattern recognition
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Pattern identification  

## State of the Field

**Space of definitions.** Across the surveyed work, one common framing treats pattern recognition as detecting recurring forms or regularities, especially in visual material: papers describe identifying and understanding repeating forms, structures, or themes, and detecting recurring visual structures across image sets that define group membership. Other papers use the term differently along several axes: one frames it as a model's latent tendency to rely on statistical regularities and surface-level cues in question formats, answer structures, or word associations rather than deep semantic understanding; one defines pattern identification as finding regularities in a sequence that support a shorter generating program; and one treats it as observable problem-solving behavior, using underlying patterns to derive a solution instead of exhaustive search.

**Space of facets.** When papers situate the construct, they place it in a few neighboring categories rather than a shared taxonomy. One paper lists it among visual reasoning abilities, Bongard work pairs it with abstract reasoning and with finding concepts that describe a set of diagrams, medical benchmark work contrasts it with deep semantic understanding or genuine material comprehension, and a mathematical reasoning example contrasts it with exhaustive search. The naming also shifts between "pattern recognition" and "pattern identification", with the latter used for sequence regularities that can be exploited for compression; no construct-to-construct links are recorded.

**Space of measurement.** Operationalization is sparse in the recorded links: papers connect it to 1 measurement instrument, Bongard Problems, and 1 behavioral indicator, Sequence compression. Bongard Problems function as a benchmark of visual rule identification from a limited set of images, while the related behavioral indicator is Sequence compression, where models identify patterns in an input sequence and produce a short program that outputs the sequence. Other uses, such as surface-cue recognition in question formats or pattern-based solution behavior rather than exhaustive search, are described in prose rather than linked to additional instruments.

**Links.** Beyond measurement, the only recorded link is that pattern recognition is related to Sequence compression. In that relation, a paper describes tasks where models identify patterns in an input sequence and compress it by producing a short program, and no causal or correlational links are recorded.

## Sources

**Pattern recognition** (3 papers: [OlympicArena: Benchmarking Multi-discipline Cognitive Reasoning for Superintelligent AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/222d2eaf24cf8259a35d6c7130d31425-Paper-Datasets_and_Benchmarks_Track.pdf), [Pattern Recognition or Medical Knowledge? The Problem with Multiple-Choice Questions in Medicine](https://aclanthology.org/2025.acl-long.266.pdf), [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf))
> The ability to identify and understand repeating forms, structures, or recurring themes within visual information.

**Pattern identification** (1 paper: [The KoLMogorov Test: Compression by Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/db1d69ee01c2b42554f8e14e6f8ca8b6-Paper-Conference.pdf))
> Detecting regularities in an input sequence that can be exploited to write a shorter generating program.

## Relationships

### Pattern recognition →
- **Bongard Problems** (measurement instrument): *measured_by*, 1 paper
  > Bongard problems (BPs), a class of visual puzzles that require identifying underlying rules based on a limited set of images, provide a unique and challenging benchmark for assessing visual reasoning abilities in AI (Bongard & Hawkins, 1970). Conceived by Mikhail Bongard in 1970, these visual puzzles test cognitive abilities in pattern recognition and abstract reasoning, posing a formidable challenge even to advanced AI systems (Hern´andez-Orallo et al., 2016).
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)

### Associated with
- **Sequence compression** (behavioral indicator), 1 paper
  > “we task them to identify patterns in an input sequence and to compress it by producing a short program that outputs said sequence”
  - [The KoLMogorov Test: Compression by Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/db1d69ee01c2b42554f8e14e6f8ca8b6-Paper-Conference.pdf)
