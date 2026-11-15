# OSWorld
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** OSWORLD  

## State of the Field

**What it is.** Across papers, the prevailing usage treats OSWorld as a real computer environment and benchmark for open-ended computer tasks with multimodal or OS agents. Definitions commonly describe it as an interactive testbed spanning Ubuntu, Windows, and macOS, with 369 tasks involving real web and desktop applications and execution-based evaluation; some authors stress that agents must interact with the operating system step by step and wait for a response before continuing, while another paper uses it more briefly as a desktop virtual agent benchmark for trajectory collection and evaluation.

**What it is claimed to measure.** Claims about what OSWorld measures are spread across five constructs and one behavioral indicator rather than concentrating on a single target. Papers most often use it to measure Generalization, while smaller lines of work use it for Adaptability, Agency, Commonsense reasoning, and Robustness; it is also linked to one behavioral indicator, with one benchmark description saying results reveal weaknesses in GUI grounding and operational knowledge.

**Space of uses.** In use, papers position OSWorld as a challenging or comprehensive benchmark for evaluating multi-step task completion across applications. Papers relate it to Execution-based evaluation, with one description saying it supports task setup, interactive learning, and execution-based evaluation of open-ended computer tasks, and to a Human baseline; one paper also uses it alongside Android World and other benchmarks to collect agent action trajectories and run evaluations.

**Concerns raised.** The concerns visible in these papers center on difficulty and sensitivity during evaluation. One paper reports that superficial changes can lead to performance drops of 60% and even 80%, and another says the human performance study found OSWorld tasks more time-consuming and challenging than those in prior work.

## Sources

**OSWORLD** (1 paper: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf))
> A scalable, real computer environment and benchmark for evaluating multimodal agents on open-ended computer tasks across Ubuntu, Windows, and macOS, featuring 369 tasks with execution-based evaluation.

**OSWorld** (2 papers: [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf), [Boosting Virtual Agent Learning and Reasoning: A Step-Wise, Multi-Dimensional, and Generalist Reward Model with Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25b/miao25b.pdf))
> An interactive OS agent testbed environment where agents must interact with the operating system at each step and wait for responses before proceeding, evaluating multi-step task completion across various applications.

## Relationships

### → OSWorld
- **Generalization** (construct): *measured_by*, 2 papers
  > To further evaluate the generalization capabilities of our model, we tested it on OSWorld, a unified computer environment designed for multimodal agents. (Section 4.3)
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **Action grounding** (behavioral indicator): *measured_by*, 1 paper
  > Extensive evaluation of state-of-the-art LLM/VLM agents on OSWORLD reveals deficiencies in their ability to serve as computer assistants. While humans accomplish 72.4% of the tasks, the best agents achieve <12.2%, struggling with GUI grounding and operational knowledge. (Abstract)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > It prioritizes a balanced benchmark across eight key applications... highlighting the need for varied operational skills, including commonsense reasoning, software navigation, and precise input control. (Section 3.1)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > We find that current agents are not robust to these superficial changes, which lead to performance drops of 60% and even 80%. (Section 5)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Agency** (construct): *measured_by*, 1 paper
  > In this study, we benchmark our approach on the challenging OS agent testbed, OSWorld (Xie et al., 2024). (Section 4.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **Adaptability** (construct): *measured_by*, 1 paper
  > On the OSWorld (Xie et al., 2024b) and AndroidWorld (Rawles et al., 2024) benchmarks, OSCAR consistently surpassed other agents... demonstrating superior adaptability across real-time dynamic OS tasks. (Section 1)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### Associated with
- **Execution-based evaluation** (measurement instrument), 1 paper
  > “supporting task setup, interactive learning, and execution-based evaluation of open-ended computer tasks”
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Human baseline** (measurement instrument), 1 paper
  > The human performance study indicates that task examples from OSWORLD are more time-consuming and challenging compared to those in prior work. (Section 3.2)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
