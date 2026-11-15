# Code infilling
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Code insertion, Fill-in-the-middle  

## State of the Field

**Space of definitions.** Most papers describe it as generating a missing code segment between left and right context, often in the middle of an existing file or snippet with code available above and below the target location. A smaller line of work frames the same behavior as code insertion, meaning completing or inserting code into an existing program context rather than generating a solution from scratch. Some descriptions also make the success condition explicit, saying the missing section should be locally coherent and connect properly to the right context, and some evaluations distinguish insertion from ordinary completion and assess outputs against test cases.

**Variants.** Papers use several names for closely similar settings, especially code insertion and fill-in-the-middle (FIM). The variants described include local-file infilling where the model sees code above and below the reference code, missing single lines or broader line or block segments within an existing snippet, and insertion at a designated position or completion at the end of existing code. One paper also reports that code generation is related to code infilling, describing a local-file setting that simulates developers infilling code in the middle of a file.

**Space of elicitation and scores.** No measurement instrument is linked to it. Where papers describe elicitation or scoring, they refer to insertion scores for models that support that mode, performance against test cases, and evaluation of fill-in-the-middle capabilities, without linking a recurring named instrument to the behavior.

**What it is taken as evidence of.** Papers do not link code infilling to any construct, and they do not explicitly state what construct it reflects. Instead, the links stay at the task level, including one paper that says code generation is related to code infilling.

## Sources

**Code infilling** (3 papers: [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf), [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf), [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf))
> Generating code in the middle of a file given code contexts both above and below the target function location.

**Code insertion** (2 papers: [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [CursorCore: Assist Programming through Aligning Anything](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25f/jiang25f.pdf))
> Completing or inserting code into an existing program context rather than generating a solution from scratch.

**Fill-in-the-middle** (1 paper: [LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://aclanthology.org/2025.naacl-long.348.pdf))
> Generating code that fits between a left and right context, simulating real-world editing where code is inserted into existing files.

## Relationships

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > “The local file denotes the code file where the reference code is in. This setting simulates the scenario where developers infill code in the middle of a file.”
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)
