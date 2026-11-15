# SWE-bench
**Type:** Measurement instrument  
**Supporting papers:** 28  
**Also known as:** SWE-BENCH, SWE-Bench, SWEBench  

## State of the Field

**What it is.** Across papers, SWE-bench is most commonly described as a benchmark of real-world software engineering tasks built from 2,294 GitHub issues, pull requests, or Issue-Pull Request pairs drawn from 12 Python repositories. Definitions converge on repository-level issue solving, with some papers framing it as testing code editing or code generation capabilities and others as assessing agents' ability to resolve GitHub issues; some also specify evaluation by whether generated patches pass provided unit tests. A related variant, SWE-bench Lite, is described as a 300-instance subset sampled from the full benchmark for a more self-contained evaluation of functional bug fixes.

**What it is claimed to measure.** The prevailing measurement claim is GitHub issue resolution: papers use SWE-bench to evaluate systems' ability to solve software issues from GitHub repositories, and some descriptions add that models must modify the repository to fix a bug or introduce a feature. The reported measurement claims are concentrated rather than spread across many targets, with links to one behavioral indicator, GitHub issue resolution, and one construct, software engineering ability. A smaller line of work treats it more broadly as measuring software engineering ability.

**Space of uses.** Papers position SWE-bench as a common benchmark for autonomous software engineering systems, coding agents, and repository-level code tasks, and one paper uses it where accurate post-hoc quality estimation is available. In reported evaluation setups it appears alongside CrossCodeEval and EvoCodeBench, and within broader agent task suites alongside WEBARENA. Papers also relate the full benchmark to SWE-bench Lite, and one paper adapts it as the basis for constructing TESTGENEVAL.

**Concerns raised.** A narrower characterization appears in one paper: it is described as emphasizing patch-level fixes rather than broader development capabilities.

## Sources

**SWE-bench** (4 papers: [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf), [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.7.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf))
> A benchmark dataset comprising 2,294 real-world issues from 12 popular Python repositories, designed to evaluate a model's ability to perform GitHub issue resolution.

**SWE-BENCH** (1 paper: [StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for evaluating language models on real-world software engineering tasks, using GitHub issues and pull requests to test code editing capabilities.

**SWE-Bench** (4 papers: [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf), [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf), [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://aclanthology.org/2025.acl-long.189.pdf), [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf))
> A benchmark designed to assess an agent's ability to resolve real-world GitHub issues, such as bug reports or feature requests, within a code repository.

**SWEBench** (1 paper: [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf))
> A benchmark dataset of real-world software engineering tasks from which the code repositories and execution environments for TESTGENEVAL are derived.

## Relationships

### → SWE-bench
- **GitHub issue resolution** (behavioral indicator): *measured_by*, 4 papers
  > In the experiments, we employ the SWE-bench dataset as the evaluation benchmark because it is the latest dataset specifically designed for evaluating the performance of the GitHub issue resolution. (Section 4.1)
  - [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf)
  - [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf)
  - [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf)
  - [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)
- **Software engineering ability** (construct): *measured_by*, 1 paper
  > we perform an evaluation of agents over 15 challenging tasks, including software engineering (e.g., SWE-BENCH) and web browsing (e.g., WEBARENA), among others. (ABSTRACT)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)

### Associated with
- **SWE-bench Lite** (measurement instrument), 1 paper
  > We conduct our experiments on SWE-Bench Lite, a 300-instance subset sampled from the full SWE-Bench for providing a more self-contained evaluation of functional bug fixes (Jimenez et al., 2024).
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)
