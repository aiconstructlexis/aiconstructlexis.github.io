# PRMBench
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** PRMBENCH  

## State of the Field

**What it is.** Across the surveyed work, PRMBench is most commonly described as a benchmark dataset for process-level reward models in reasoning chains, built on the PRM800K corpus and focused on step-level correctness in multi-step problem solving. Definitions describe it as covering about 6k math problems across 9 error categories, while one benchmark description gives a more exact inventory of 6,216 problems and 83,456 step-level labels, aimed at reasoning correctness and error detection.

**What it is claimed to measure.** Papers use it to measure 2 constructs and 1 behavioral indicator. The prevailing links are that PRMBench measures Soundness and Simplicity, and one paper also reports it as measuring Error analysis, describing the benchmark as supporting granular error diagnosis; the reported uses therefore span a small set of process-evaluation targets rather than a single repeated construct.

**Space of uses.** Papers typically position PRMBench as one evaluation dataset within a broader suite. As one study notes, "We evaluate on four datasets: PRMBench, DeltaBench, ClaimTrees, and CaptainCookRecipes" (Probabilistic Soundness Guarantees in LLM Reasoning Chains), while another paper reports benchmark table results on it; the only linked measurement instrument is Human evaluation, which papers relate to PRMBench through manual review of 10% of instances by volunteers.

## Sources

**PRMBENCH** (1 paper: [Dynamic and Generalizable Process Reward Modeling](https://aclanthology.org/2025.acl-long.212.pdf))
> Benchmark dataset built on PRM800K corpus with 6k math problems across 9 error categories, designed to evaluate process-level reward models on reasoning correctness and error detection.

**PRMBench** (1 paper: [Probabilistic Soundness Guarantees in LLM Reasoning Chains](https://aclanthology.org/2025.emnlp-main.382.pdf))
> Benchmark for evaluating process-level rewards in reasoning chains, assessing step-level correctness in multi-step problem solving.

## Relationships

### → PRMBench
- **Soundness** (construct): *measured_by*, 2 papers
  > PRMBENCH comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.
  - [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://aclanthology.org/2025.acl-long.1230.pdf)
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **Simplicity** (construct): *measured_by*, 1 paper
  > PRMBENCH comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.
  - [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://aclanthology.org/2025.acl-long.1230.pdf)
- **Error analysis** (behavioral indicator): *measured_by*, 1 paper
  > PRMBench (Song et al., 2025) constitutes a comprehensive benchmark for evaluating PRMs, with particular emphasis on granular error diagnosis (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)

### Associated with
- **Human evaluation** (measurement instrument), 1 paper
  > Furthermore, to further ensure the quality of the data, we manually evaluate 10% of the total instances... We recruited five volunteers to evaluate our proposed PRMBENCH... (Section 3.3)
  - [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://aclanthology.org/2025.acl-long.1230.pdf)
