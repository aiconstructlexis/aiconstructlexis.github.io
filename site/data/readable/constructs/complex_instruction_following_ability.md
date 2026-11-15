# Complex instruction following ability
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Complex instruction following, Complex instruction understanding  

## State of the Field

**Space of definitions.** Across the definitions, papers treat it as an ability centered on interpreting and executing complex instructions. One framing defines it as accurately interpreting and carrying out multi-step instructions while maintaining consistency across the full task, and another defines it as discerning and executing a user's core intent from long or convoluted instructions that may include irrelevant information. The shared core is accurate execution of complex instructions, while the point of variation is what makes them complex: multi-step structure and task-wide consistency in one case, long context, convolution, and irrelevant content in the other.

**Space of facets.** The papers use two nearby labels, complex instruction following and complex instruction understanding, for closely related abilities with different emphases. In benchmark taxonomies it also appears as a capability or subset: a benchmark lists complex instruction following as one of three capabilities, and another includes a Complex Instruction subset that measures whether an agent can discern user intent from a long context.

**Space of measurement.** Operationalization is entirely benchmark-based: the construct is linked to 5 measurement instruments, CFBench, ComplexBench, FollowBench, MCBench, and TRACE, and to no behavioral indicators. The recurring benchmark design is instruction sets with multiple constraints, as CFBench, FollowBench, and ComplexBench are described that way; MCBench operationalizes it with multi-step prompts averaging over 5,000 characters that require executing each step while maintaining consistency, and TRACE is introduced as a benchmark for improving and evaluating this ability. These measures focus on multiple constraints and multi-step execution, which matches the multi-step definition directly, while the long-context, irrelevant-information framing appears in a separate definition and subset description.

**Links.** Papers link the construct only through measurement: they say it is measured by CFBench, ComplexBench, FollowBench, MCBench, and TRACE. No causal, correlational, or related links are reported.

## Sources

**Complex instruction following** (1 paper: [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf))
> The ability to accurately interpret and execute multi-step instructions while maintaining consistency across the full task.

**Complex instruction understanding** (1 paper: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf))
> The ability to discern and execute a user's core intent from long or convoluted language instructions that may contain irrelevant information.

## Relationships

### Complex instruction following ability →
- **CFBench** (measurement instrument): *measured_by*, 3 papers
  > We mainly perform evaluations on three complex instruction-following benchmarks: CFBench (Zhang et al., 2024b), FollowBench (Jiang et al., 2024b) and ComplexBench (Wen et al., 2024) (Section 4.1).
  - [MuSC: Improving Complex Instruction Following with Multi-granularity Self-Contrastive Training](https://aclanthology.org/2025.acl-long.523.pdf)
  - [IOPO: Empowering LLMs with Complex Instruction Following via Input-Output Preference Optimization](https://aclanthology.org/2025.acl-long.1079.pdf)
  - [AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1628.pdf)
- **ComplexBench** (measurement instrument): *measured_by*, 2 papers
  > To this end, we propose ComplexBench, a benchmark for comprehensively evaluating the ability of LLMs to follow complex instructions composed of multiple constraints. (Abstract)
  - [Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MuSC: Improving Complex Instruction Following with Multi-granularity Self-Contrastive Training](https://aclanthology.org/2025.acl-long.523.pdf)
- **FollowBench** (measurement instrument): *measured_by*, 2 papers
  > We mainly perform evaluations on three complex instruction-following benchmarks: CFBench (Zhang et al., 2024b), FollowBench (Jiang et al., 2024b) and ComplexBench (Wen et al., 2024) (Section 4.1).
  - [MuSC: Improving Complex Instruction Following with Multi-granularity Self-Contrastive Training](https://aclanthology.org/2025.acl-long.523.pdf)
  - [AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1628.pdf)
- **TRACE** (measurement instrument): *measured_by*, 1 paper
  > this paper introduces TRACE, a benchmark for improving and evaluating the complex instruction-following ability, which consists of 120K training data and 1K evaluation data. (Abstract)
  - [IOPO: Empowering LLMs with Complex Instruction Following via Input-Output Preference Optimization](https://aclanthology.org/2025.acl-long.1079.pdf)
- **MCBench** (measurement instrument): *measured_by*, 1 paper
  > MCBench evaluates three key capabilities of LLMs: • Complex Instruction Following: Each prompt in MCBench consists of multi-step instructions averaging over 5,000 characters in length.
  - [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf)
