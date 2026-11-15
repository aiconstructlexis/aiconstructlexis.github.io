# Error localization
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Invalid node identification, Process judging, First error step identification, Mistake location  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a fine-grained judgment task in which a model pinpoints where a previously produced solution or reasoning chain goes wrong, most often by identifying the erroneous step or the first step where the error begins. Several formulations describe success as locating the specific faulty step, component, line, or span, and some also require explaining the mistake or giving reasons for the decision, for example by "judge step by step until the wrong step is located." A smaller line of work applies the same pattern to invalid literature-grounded chains, where the model identifies the breakpoint paper nodes where logical progression breaks down.

**Variants.** Papers study this behavior under several names, most commonly Error localization, and also Process judging, First error step identification, Invalid node identification, and Mistake location. The variants differ mainly by domain and target unit: math settings ask for the step where errors begin in a wrong solution, handwritten math asks for the line or part of an image where the error occurs, chemistry asks for the contiguous erroneous text span in a molecular description, literature-grounded reasoning asks for the incorrect paper nodes in an invalid chain, and tutoring evaluations ask whether the tutor points to the mistake location and outlines what the error is. One paper also relates error localization to pairwise comparison, stating that disagreements between candidate solutions strongly signal potential locations of their errors.

**Space of elicitation and scores.** Papers link error localization to 1 measurement instrument, MOLERR2FIX, which is described as a structured four-stage Error-to-Fix evaluation pipeline for chemical reasoning. In that instrument, localization is one stage alongside detection, explanation, and revision, and it is used to assess whether the model can locate the erroneous text span.

**What it is taken as evidence of.** Papers link error localization to 2 constructs, and they do not converge on a single one. One paper reports that it is weakly correlated with problem-solving ability across models and prompts, while another claims a causal relationship from error localization to self-correction ability in a setup that locates and corrects specific error thoughts in smaller student LLMs.

## Sources

**Error localization** (4 papers: [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf), [MolErr2Fix: Benchmarking LLM Trustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction](https://aclanthology.org/2025.emnlp-main.977.pdf), [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf), [Can Vision-Language Models Evaluate Handwritten Math?](https://aclanthology.org/2025.acl-long.720.pdf))
> The observable behavior of a model identifying specific incorrect steps or components within a previously generated solution.

**Invalid node identification** (1 paper: [HypER: Literature-grounded Hypothesis Generation and Distillation with Provenance](https://aclanthology.org/2025.emnlp-main.1292.pdf))
> The task of identifying the specific papers within an invalid reasoning chain where the logical progression or coherence breaks down.

**Process judging** (1 paper: [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf))
> The observable behavior of identifying the specific step in a provided incorrect solution where the first error occurs.

**First error step identification** (1 paper: [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf))
> The observable sub-task of identifying the specific initial step in a flawed reasoning process where the logic first deviates from a correct path.

**Mistake location** (1 paper: [Unifying AI Tutor Evaluation: An Evaluation Taxonomy for Pedagogical Ability Assessment of LLM-Powered AI Tutors](https://aclanthology.org/2025.naacl-long.57.pdf))
> The observable behavior of a tutor specifying where in the student's reasoning or calculation the error occurred and explaining the nature of the mistake.

## Relationships

### Error localization →
- **Self-correction ability** (construct): *causes*, 1 paper
  > We propose cross-model collaborative DPO, which innovatively leverage SOTA LLMs to locate and correct the specific error thoughts in the reasoning process of smaller student LLMs, thus advancing their self-correction ability and breaking their thought bottleneck. (Section 1)
  - [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf)
- **Problem-solving ability** (construct): *correlates*, 1 paper
  > A chi-squared test for independence confirms that error localization and problem-solving accuracy are weakly correlated (p > 0.01; ϕ < 0.2) across models and prompts (Section 4.2)
  - [LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.553.pdf)
- **MOLERR2FIX** (measurement instrument): *measured_by*, 1 paper
  > MOLERR2FIX introduces a structured chain-like, four-stage Error-to-Fix evaluation pipeline—detection, localization, explanation, and revision—offering a fine-grained and progressive framework for assessing LLMs in chemical reasoning. (Section 1)
  - [MolErr2Fix: Benchmarking LLM Trustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction](https://aclanthology.org/2025.emnlp-main.977.pdf)

### Associated with
- **Pairwise comparison** (behavioral indicator), 1 paper
  > "Disagreements between candidate solutions strongly signal the potential locations of their errors."
  - [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf)
