# Instruction generation
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats instruction generation as a reverse task: producing an instruction or prompt from a response, so as to infer what user prompt would naturally elicit that response. The formulations agree on recovering an instruction that would make the given text a correct answer, with one description stating that a reverse model "learns to generate instructions given responses" and another describing prediction of a prompt that would be correctly answered by a piece of human-written text.

**Variants.** Papers describe closely related variants centered on the source text used to generate the instruction. One line frames it as generating an instruction from a response, including synthetic instructions paired with seed responses, while another frames it as backtranslating from unlabeled human-written text, sometimes only a portion of a document, into an instruction-following example.

**Space of elicitation and scores.** No measurement instrument is linked to it.

**What it is taken as evidence of.** Papers do not link it to any construct.

## Sources

**Instruction generation** (2 papers: [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.644.pdf), [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf))
> Producing an instruction given a response, typically to infer what user prompt would naturally elicit that response.
