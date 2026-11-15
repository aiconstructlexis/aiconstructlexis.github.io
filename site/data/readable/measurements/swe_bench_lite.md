# SWE-bench Lite
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** SWE-Bench Lite, SWE-Bench-Lite  

## State of the Field

**What it is.** Most papers treat SWE-bench Lite as the lite subset of SWE-bench, and some explicitly call it the most commonly used subset, sampled from the full benchmark for a more self-contained evaluation of functional bug fixes. Some descriptions broaden this to a repository-level evaluation suite for automated software engineering, built from real GitHub issues, code patches, and repository-level code changes; some also specify Python codebases or repositories, and a minority mention hidden unit tests.

**What it is claimed to measure.** Claims about what it measures are concentrated rather than spread across many targets: papers link it to two behavioral indicators and no constructs. It is used to measure software issue resolution and GitHub issue resolution, with relationship evidence referring to issue resolution rate on SWE-bench Lite and to comparing systems on the same issues' resolution.

**Space of uses.** Papers commonly use it as a main evaluation benchmark for autonomous or automated software engineering systems, including comparisons of state-of-the-art performance and agentic issue resolution. The only linked instrument is SWE-bench, and papers position SWE-bench Lite in relation to it as a subset of the full benchmark; some also describe choosing SWE-bench Lite under budget constraints to compare on the same issue-resolution tasks.

## Sources

**SWE-bench Lite** (3 papers: [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cf/li25cf.pdf), [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf))
> The most commonly used subset of the SWE-bench benchmark for evaluating state-of-the-art performance in autonomous software engineering systems.

**SWE-Bench-Lite** (1 paper: [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf))
> SWE-Bench-Lite, an evaluation suite for repository-level software engineering tasks involving real GitHub issues and code patches.

**SWE-Bench Lite** (2 papers: [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf), [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://aclanthology.org/2025.acl-long.189.pdf))
> SWE-Bench Lite, a 300-instance benchmark of real GitHub issue resolution with hidden unit tests for evaluating functional bug fixes.

## Relationships

### → SWE-bench Lite
- **Software issue resolution** (behavioral indicator): *measured_by*, 2 papers
  > We conduct our experiments on SWE-Bench Lite, a 300-instance subset sampled from the full SWE-Bench for providing a more self-contained evaluation of functional bug fixes (Jimenez et al., 2024).
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **GitHub issue resolution** (behavioral indicator): *measured_by*, 2 papers
  > Considering budget constraints, we conducted experiments on SWE-bench lite to compare with them on the same issues’ resolution. (Appendix D)
  - [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf)
  - [DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal](https://aclanthology.org/2025.acl-long.973.pdf)

### Associated with
- **SWE-bench** (measurement instrument), 1 paper
  > We conduct our experiments on SWE-Bench Lite, a 300-instance subset sampled from the full SWE-Bench for providing a more self-contained evaluation of functional bug fixes (Jimenez et al., 2024).
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)
