# Code improvement
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Code refinement  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as revising existing code to improve non-functional qualities. Definitions describe modifying code to enhance performance, security, or maintainability, while adjacent uses of "code refinement" describe either fixing identified vulnerabilities in an initially generated snippet or improving readability and style. Success is framed as producing code that addresses the targeted issue, for example fixing vulnerable code, improving latency or resource utilization, or adding docstrings, comments, and consistent conventions without altering functionality.

**Variants.** Papers use both "code improvement" and "code refinement" for this behavior. The settings mentioned include multiple programming languages and function-, class-, or file-level edits, with variants such as bug fixing, latency improvement, resource utilization optimization, vulnerability repair, and readability or style refinement through docstrings, inline comments, and consistent coding conventions. One paper, Generating CAD Code with Vision-Language Models for 3D Designs, claims a causal relationship from Feedback generation to Code improvement, stating that ameliorative feedback is applied to refine the code.

**Space of elicitation and scores.** No measurement instrument is linked to it. The papers operationalize it through task formulations such as vulnerable-code fixing, non-functional code edits, and style or readability refinement, but they do not link the behavior to a named elicitation or scoring instrument.

**What it is taken as evidence of.** No construct is linked to it in the surveyed papers.

## Sources

**Code improvement** (1 paper: [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf))
> The task of modifying code to enhance non-functional properties such as performance, security, or maintainability.

**Code refinement** (2 papers: [ProSec: Fortifying Code LLMs with Proactive Security Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25aa/xu25aa.pdf), [UnitCoder: Scalable Code Synthesis from Pre-training Corpora](https://aclanthology.org/2025.emnlp-main.286.pdf))
> Revising an initially generated code snippet to fix identified vulnerabilities or improve security.

## Relationships

### → Code improvement
- **Feedback generation** (behavioral indicator): *causes*, 1 paper
  > The question-answer pairs are then used to generate ameliorative feedback to further refine the 3D object... feedback, Fref, is then applied to refine the code, as described Eq. (3). (Section 3.3)
  - [Generating CAD Code with Vision-Language Models for 3D Designs](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf)
