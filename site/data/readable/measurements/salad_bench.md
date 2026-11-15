# SALAD-Bench
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** SALAD-BENCH, SaladBench  

## State of the Field

**What it is.** Across papers, SALAD-Bench is most commonly described as a safety benchmark for LLMs. Definitions present it as an established benchmark that provides prompts and safety scores for evaluating LLM safety and its relationship to value systems, and another description calls it a hierarchical benchmark covering different task types and jailbreak attack methods. A smaller line of work treats it as a dataset source of harmful prompts used in training and evaluating refusal mechanisms.

**What it is claimed to measure.** Papers portray it as measuring more than one target rather than centering on a single construct. In the recorded links, it is used to measure one construct, privacy awareness, where authors extract the "privacy infringement" category, and one behavioral indicator, jailbreaking, where it is used as a safety benchmark to assess the generalizability of a weak-to-strong attack. Definitions also frame it more broadly as evaluating LLM safety, and in one paper its prompts and safety scores are used to study safety in relation to value systems.

**Space of uses.** No measurement instrument is linked to it. Papers mainly position it as an evaluation source: one study draws prompts and safety scores from SALAD-Bench, another uses SALAD-Bench with ALPACA to construct harmless and harmful prompts, and another expands safety evaluation by adding it alongside SORRY-Bench. One paper also uses predefined "unfair representation" and "privacy infringement" categories from it to build fairness-awareness and privacy-awareness query sets.

## Sources

**SALAD-Bench** (1 paper: [Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models](https://aclanthology.org/2025.acl-long.585.pdf))
> Established safety benchmark providing prompts and safety scores for evaluating LLM safety and its relationship to value systems.

**SALAD-BENCH** (1 paper: [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf))
> A dataset used as a source of harmful prompts for training and evaluating refusal mechanisms.

**SaladBench** (1 paper: [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://proceedings.neurips.cc/paper_files/paper/2024/file/de7b99107c53e60257c727dc73daf1d1-Paper-Datasets_and_Benchmarks_Track.pdf))
> A hierarchical safety benchmark for LLMs that covers different task types and jailbreak attack methods.

## Relationships

### → SALAD-Bench
- **Privacy awareness** (construct): *measured_by*, 1 paper
  > From Salad-bench, we extract query subsets under the predefined categories of “unfair representation” and “privacy infringement” to construct fairness awareness query set Qf and privacy awareness query set Qp, respectively. (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 1 paper
  > To assess the generalizability of the weak-to-strong attack, we expanded our evaluation to include two new safety benchmarks: SALAD-Bench (Li et al., 2024) and SORRY-Bench (Xie et al., 2024). (Section 5.1)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
