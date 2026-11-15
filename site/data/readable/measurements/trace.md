# TRACE
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the papers, TRACE is most commonly described as a public benchmark for continual learning or continual instruction tuning, organized around a learning sequence or multiple sequential fine-tuning tasks. Definitions and quoted passages describe task content such as multi-choice QA, code generation, mathematical reasoning, and summarization, and one paper also describes 8 diverse tasks including domain-specific QA, code completion, and mathematical reasoning. A smaller line of work describes TRACE as a benchmark for improving and evaluating complex instruction-following ability, with 120K training data and 1K evaluation data, while another description says it is designed to evaluate general ability, instruction following, and safety.

**What it is claimed to measure.** Papers link TRACE to 3 constructs and 2 behavioral indicators. The most frequently linked constructs are Complex instruction following ability, Mathematical reasoning, and Safety, and the most frequently linked behavioral indicators are Code completion and Instruction following. Taken together, papers use TRACE to measure several different targets rather than centering it on a single reported construct, and some descriptions also frame it more broadly as evaluating general ability.

**Space of uses.** No other measurement instrument is linked to TRACE. Most papers position it as a benchmark for continual learning or continual instruction tuning in sequential or multi-round fine-tuning settings, and some use it as an added testbed for extending experiments or checking an approach on a public benchmark, while another paper positions it as the benchmark introduced for improving and evaluating complex instruction-following ability.

## Sources

**TRACE** (3 papers: [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf), [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.626.pdf), [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf))
> A public benchmark for continual learning that includes a sequence of tasks such as multi-choice QA, code generation, mathematical reasoning, and summarization.

## Relationships

### → TRACE
- **Code completion** (behavioral indicator): *measured_by*, 1 paper
  > TRACE (Wang et al., 2023b) serves as a challenging continual instruction tuning benchmark comprising 8 diverse tasks, including domain-specific QA, code completion, mathematical reasoning (Section 2).
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > TRACE (Wang et al., 2023b) serves as a challenging continual instruction tuning benchmark comprising 8 diverse tasks, including domain-specific QA, code completion, mathematical reasoning (Section 2).
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Complex instruction following ability** (construct): *measured_by*, 1 paper
  > this paper introduces TRACE, a benchmark for improving and evaluating the complex instruction-following ability, which consists of 120K training data and 1K evaluation data. (Abstract)
  - [IOPO: Empowering LLMs with Complex Instruction Following via Input-Output Preference Optimization](https://aclanthology.org/2025.acl-long.1079.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > TRACE, another continual instruction tuning benchmark, is designed to evaluate the general ability, instruction following, and safety for LLMs (Wang et al., 2023). (Section 2. Related Work)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > TRACE, another continual instruction tuning benchmark, is designed to evaluate the general ability, instruction following, and safety for LLMs (Wang et al., 2023). (Section 2. Related Work)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
