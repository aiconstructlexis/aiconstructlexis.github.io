# System 2 thinking
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** System-2 thinking, System 2 reasoning, Deliberate reasoning, Deep thinking, Slow thinking  

## State of the Field

**Space of definitions.** Across papers, the dominant framing of System 2 thinking is a slow, deliberate, logical, analytical, and reflective mode of reasoning used for complex problem-solving. Most definitions emphasize methodical, step by step examination of assumptions, conditions, calculations, and logic, sometimes with the aim of detecting mistakes or revising an initial output. Smaller strands narrow it to multi-path conscious evaluation, slower iterative search, or consistent rule-based processing that is not swayed by incidental features, so the main variation is between a broad reasoning mode and narrower formulations centered on error detection, self-revision, search, or robustness to superficial variation.

**Space of facets.** Papers use several closely related labels for this family of ideas, including System-2 thinking, System 2 reasoning, slow thinking, deliberate reasoning, and deep thinking. A recurring organization is the contrast with System 1 or fast thinking, with one definition stating that System 2 can monitor and control System 1 processes, while other papers describe models as transitioning between slow and fast modes. Papers also connect it to neighboring constructs such as meta-reasoning and hierarchical reasoning, and present self-reflection as a manifestation of System 2 reasoning; the labels differ mainly in emphasis, such as step by step traces, exploration of multiple paths, or slower iterative search.

**Space of measurement.** No measurement instrument is linked to it. Papers instead connect it to three behavioral indicators: chain of thought, self-reflection, and self-correction. In these operationalizations, slow mode is described as producing intermediate reasoning steps or detailed reasoning paths, self-reflection is described as a manifestation of System 2 reasoning and also appears in a claimed causal link, and one paper says self-correction is often referred to as system 2 reasoning; these choices align most closely with definitions that stress deliberate intermediate reasoning, reflection, and revision.

**Links.** Papers relate System 2 thinking to five constructs: meta-reasoning, hierarchical reasoning, mathematical reasoning, robustness, and System 1 thinking. Several papers describe related links with meta-reasoning, chain of thought, robustness, System 1 thinking, and hierarchical reasoning, while one paper claims a causal relationship from System 2 thinking to self-reflection and another claims a causal relationship from System 2 thinking to mathematical reasoning. Another paper relates self-correction to System 2 reasoning, and no correlational link is reported.

## Sources

**System 2 thinking** (1 paper: [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf))
> A cognitive mode characterized by slow, deliberate, logical, and analytical thought processes required for complex problem-solving and reasoning.

**System-2 thinking** (1 paper: [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf))
> The cognitive ability to engage in slow, deliberate, and methodical reasoning to thoroughly examine assumptions, conditions, and logic for deep error detection.

**System 2 reasoning** (1 paper: [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf))
> The latent tendency to engage in deliberate, reflective reasoning that can revise and improve an initial output.

**Slow thinking** (2 papers: [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf), [VisuoThink: Empowering LVLM Reasoning with Multimodal Tree Search](https://aclanthology.org/2025.acl-long.1053.pdf))
> The model's ability to engage in a deliberate, step-by-step reasoning process to arrive at a solution, analogous to human System 2 cognition.

**Deliberate reasoning** (1 paper: [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf))
> A reasoning style characterized by exploring multiple paths and conscious evaluation rather than single-path focus.

**Deep thinking** (1 paper: [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf))
> A mode of reasoning analogous to human System 2 cognition, characterized by a slower, more deliberate, and iterative thought process, often implemented via search algorithms like MCTS.

## Relationships

### System 2 thinking →
- **Self-reflection** (behavioral indicator): *causes*, 2 papers
  > This indicates that only LMMs with substantial reasoning capabilities can effectively engage in self-reflection and result optimization, underscoring the critical role of System 2 reasoning in addressing ChartMimic’s challenges. (Section 4.2)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
  - [Agentic Knowledgeable Self-awareness](https://aclanthology.org/2025.acl-long.619.pdf)
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > The continuously improved math reasoning capabilities via rStar-Math self-evolved deep thinking. (Table 4)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)

### Associated with
- **Meta-reasoning** (construct), 2 papers
  > Our meta-reasoning paradigm is especially suited for system-2 slow thinking, mirroring the human cognitive process of carefully examining assumptions, conditions, calculations, and logic to identify mistakes. (Abstract).
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
  - [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator), 2 papers
  > In fast mode, a Transformer will output a final solution without any reasoning steps, whereas the intermediate steps of thinking, such as a search trace for finding a short path, will be generated along with the plan in slow mode. (Section 1)
  - [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [What Happened in LLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective](https://aclanthology.org/2025.acl-long.1545.pdf)
- **Robustness** (construct), 1 paper
  > A truly intelligent system should exhibit System 2 thinking [Kahneman, 2011], which implies performing tasks consistently regardless of incidental features. (Section 1)
  - [SETLEXSEM CHALLENGE: Using Set Operations to Evaluate the Lexical and Semantic Robustness of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a12909ffd7145c41139ad66ecf20fc0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-correction** (behavioral indicator), 1 paper
  > state-of-the-art LLMs (OpenAI, 2024, 2025) are capable of self-correction—often referred to as “system 2” reasoning (Xiang et al., 2025)—without explicit external verification. (Introduction)
  - [Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.699.pdf)
- **System 1 thinking** (construct), 1 paper
  > During the thinking process, LRMs automatically transit between slow thinking and fast thinking, utilizing self-reflection as chain of thoughts (Wei et al., 2022). (Section 2)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
- **Hierarchical reasoning** (construct), 1 paper
  > In System 2, FaST uses many visual agents to accomplish hierarchical reasoning.
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
