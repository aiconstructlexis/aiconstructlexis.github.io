# Code input prediction
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Input prediction  

## State of the Field

**Space of definitions.** The defining paper treats this behavior as recovering plausible inputs from a program and observed outputs. In that usage, it is framed as an input prediction task in which the model backtracks through the program's execution process to recover potential inputs, as described in Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment.

**Variants.** The named variants are limited to the general label input prediction and the benchmark-specific name CruxEval-I. In benchmark use, it appears alongside a separate output prediction task, CruxEval-O.

**Space of elicitation and scores.** Papers link it to 1 measurement instrument, CRUXEval. This instrument is a benchmark, and the reported operationalization is the code-understanding task CruxEval-I, with no other measurement instrument linked.

**What it is taken as evidence of.** Papers link it to 1 construct, abductive code reasoning. The recorded claim is a related link rather than an explicit measurement claim: one paper states that abductive code reasoning is concretized as input prediction tasks, and no other construct framing is linked.

## Sources

**Input prediction** (1 paper: [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf))
> Recovering plausible inputs from a program and observed outputs.

## Relationships

### Code input prediction →
- **CRUXEval** (measurement instrument): *measured_by*, 1 paper
  > two code-understanding tasks—namely, CruxEval-I (input prediction) and CruxEval-O (output prediction) from CruxEval benchmark [6] (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)

### Associated with
- **Abductive code reasoning** (construct), 1 paper
  > Abductive code reasoning is concretized as input prediction tasks.
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
