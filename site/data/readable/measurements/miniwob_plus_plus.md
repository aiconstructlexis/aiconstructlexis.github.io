# MiniWoB++
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** MiniWob  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats MiniWoB++ as a standard benchmark suite or interactive benchmark for computer control and web navigation in a simulated, simplified web environment. Definitions usually emphasize diverse instruction-following tasks, from low-level actions to complex multi-step decision making, where agents interact with web elements or pages through keyboard and mouse actions; some descriptions also note built-in reward functions or outcome-based checks. A smaller line of work under the name MiniWob describes it instead as a multimodal or open-ended web navigation benchmark in real web environments.

**What it is claimed to measure.** Papers use MiniWoB++ most often to measure web navigation, and some also use it to measure task completion. A smaller strand reports it as measuring adaptability. These claims do not spread across many targets: the benchmark is linked to 2 behavioral indicators, web navigation and task completion, and to 1 construct, adaptability.

**Space of uses.** No measurement instrument is linked to MiniWoB++. In use, papers commonly position it as a standard or representative benchmark for evaluating computer-control or autonomous agents, and they also report it alongside ALFWorld, WebArena, ScreenSpot, AITW, and Mind2Web. Some papers additionally emphasize its built-in reward functions or outcome-based evaluation with programmatic checkers.

## Sources

**MiniWoB++** (5 papers: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf), [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf), [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6a6891cf1dfc64d664f086cf5976e93-Paper-Conference.pdf))
> A standard benchmark suite for computer control agents, integrating diverse tasks that simulate real-world human-computer interactions in a simplified web environment.

**MiniWob** (2 papers: [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf))
> A web navigation benchmark of open-ended tasks in real web environments that evaluates agents on instruction-following and action execution.

## Relationships

### → MiniWoB++
- **Web navigation** (behavioral indicator): *measured_by*, 2 papers
  > MiniWoB++ (Liu et al., 2018) is an interactive web benchmark, with built-in reward functions. (§4.3)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **Task completion** (behavioral indicator): *measured_by*, 1 paper
  > These manuals allow LLM agents to achieve remarkable success rates of 97.4% with GPT-4-turbo and 86.2% with GPT-3.5-turbo on ALFWorld, 98.3% with GPT-4-turbo and 92.7% with GPT-3.5-turbo on MiniWoB++. (Introduction)
  - [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf)
- **Adaptability** (construct): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
