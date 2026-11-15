# Prompt decomposition
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Text decomposition  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats prompt decomposition as taking a complex textual description or query and splitting it into multiple shorter units. Papers agree on the core operation, decomposition into semantically coherent phrases or distinct sub-prompts, and differ mainly in how they describe the outputs: some frame them as short phrases, while others frame them as sub-prompts for individual concepts such as scene, objects, and motion.

**Variants.** A smaller naming variation appears between text decomposition and prompt decomposition. The studied settings range from decomposing a complex text description into short phrases to decomposing a complex query for video generation into several concept-specific sub-prompts.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior in the papers. Operationalization is described directly through the task itself, as decomposing a complex input into shorter phrases or distinct concept-level sub-prompts.

**What it is taken as evidence of.** No construct is linked to this behavior in the papers.

## Sources

**Text decomposition** (1 paper: [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf))
> The task of breaking down a complex text description into multiple, shorter, semantically coherent phrases.

**Prompt decomposition** (2 papers: [Compositional 3D-aware Video Generation with LLM Director](https://proceedings.neurips.cc/paper_files/paper/2024/file/edbeca7811f9365c924c72a8a9bce83a-Paper-Conference.pdf), [Rare-to-Frequent: Unlocking Compositional Generation Power of Diffusion Models on Rare Concepts with LLM Guidance](https://proceedings.iclr.cc/paper_files/paper/2025/file/262ba7d20578417435414ce00e69fb12-Paper-Conference.pdf))
> Splitting a complex textual input into distinct sub-prompts that describe individual concepts such as scene, objects, and motion.
