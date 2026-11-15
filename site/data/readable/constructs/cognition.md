# Cognition
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Cognitive capability, Cognitive capacity, Cognitive ability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats cognition as a latent or general capacity that combines perception, knowledge, and reasoning. Definitions commonly describe it as integrating perceptual information or attributes with domain-specific knowledge to deduce more complex answers, or as a broad mental capacity spanning knowledge, perception, and reasoning. Smaller lines of work narrow it to understanding and interpreting a system's actions and their consequences in an environment, or frame cognitive capacity as an inherent, unobservable limit on a model's ability to comprehend and execute complex reasoning steps, sometimes said to correlate with parameter size.

**Space of facets.** Papers most often break cognition into knowledge, perception, and reasoning, or treat it as a cognition component that requires reasoning about images. One line of work explicitly theorizes cognitive capability as foundational to associative ability, while another places cognition alongside emotion in multimodal understanding. The label family is not fully uniform: "cognition," "cognitive capability," and "cognitive capacity" are used for a broad mental capacity, a specific cognition component, and an underlying limit on reasoning steps.

**Space of measurement.** Operationalization is linked to 2 measurement instruments, both benchmarks, and to no behavioral indicators. MME is used to measure perception and cognition abilities across 14 subtasks, so cognition is operationalized jointly with perception, and MMMU scores are used as an indicator of cognitive ability because the benchmark is described as evaluating comprehensive cognitive skills. These measures match the common definitions that tie cognition to perception and reasoning, and among linked measures the operationalization is entirely benchmark-based.

**Links.** Papers link cognition to 3 other constructs, and no causal relationship is claimed. One paper reports that associative reasoning correlates with cognition, noting Pearson correlation coefficients above 0.66 and several above 0.71. Papers also relate cognition to visual perception, through descriptions of integrating perceptual attributes with knowledge, and to fine-grained visual understanding, which one source says is needed for understanding cognition and emotion.

## Sources

**Cognition** (2 papers: [Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf), [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf))
> The latent ability to integrate perceptual information with domain-specific knowledge to deduce more complex answers and reason about an image.

**Cognitive capability** (1 paper: [AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.263.pdf))
> A general mental capacity encompassing knowledge, perception, and reasoning, which is theorized to be foundational to associative ability.

**Cognitive capacity** (1 paper: [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf))
> The inherent, unobservable limit on a model's ability to comprehend and execute complex reasoning steps, which often correlates with its parameter size.

## Relationships

### Cognition →
- **MME** (measurement instrument): *measured_by*, 2 papers
  > MME benchmark measures both perception and cognition abilities on a total of 14 subtasks. (Section 4.2)
  - [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > we use scores from the MMMU benchmark (Yue et al., 2024) as an indicator of models’ cognitive ability, as MMMU is specifically designed to evaluate comprehensive cognitive skills of MLLMs. (Section 6)
  - [AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.263.pdf)

### → Cognition
- **Associative reasoning** (construct): *correlates*, 1 paper
  > As shown in Fig. 3, all Pearson Correlation Coefficient values exceed 0.66, with three exceed 0.71, demonstrating a strong positive correlation between cognition and association. (Section 6)
  - [AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.263.pdf)

### Associated with
- **Visual perception** (construct), 1 paper
  > cognition capabilities (integrating perceptual attributes and knowledge to deduce more complex answers) (Section 1).
  - [Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fine-grained visual understanding** (construct), 1 paper
  > While recent MLLMs show promising results in basic perception, they still struggle to perceive fine-grained details (Tong et al., 2024b), which is essential for understanding cognition and emotion.
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
