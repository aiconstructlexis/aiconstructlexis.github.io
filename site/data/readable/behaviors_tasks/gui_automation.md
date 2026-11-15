# GUI automation
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** GUI control, GUI interaction, UI control, GUI navigation, Pixel-level operation, On-device control, Mobile device control, Computer interaction, Cross-application task completion, Cross-app task execution, Single-app task execution, Software application manipulation, Computer control, UI interaction, Interface manipulation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats GUI automation as end-to-end task completion through direct interaction with a graphical or computer interface: agents navigate pages or applications and execute actions such as clicking, typing, scrolling, tapping, swiping, or keyboard and mouse input to accomplish a user goal or reach a goal state. Definitions mostly agree that success is completing the requested task through a sequence of UI actions, sometimes explicitly from natural-language instructions or from screenshots and instructions. A smaller line of work narrows this to pixel-level operation, describing direct clicks or typing at screen coordinates without relying on underlying code structures.

**Variants.** Papers study this behavior under several names, including GUI control, GUI interaction, UI control, GUI navigation, computer control, mobile device control, and interface manipulation. Common variants differ by platform and task scope: web and mobile tasks from screenshots and instructions, desktop or enterprise software operation, and on-device smartphone control. Some papers separate single-app task execution from cross-app or cross-application workflows, including tasks that require switching between apps or coordinating actions across multiple GUIs, APIs, or both; others emphasize everyday software use such as browsing, email, editing, and office workflows.

**Space of elicitation and scores.** One measurement instrument is linked to this behavior. The only linked instrument, and therefore the most common in these papers, is AitW, which is described as a mobile navigation benchmark with operation trajectories and is used for fine-tuning and evaluation on corresponding test subsets.

**What it is taken as evidence of.** The relations do not frame GUI automation as measured evidence of a construct. Only one construct is linked to it, Visual grounding, and one paper claims a causal relationship from Visual grounding to GUI automation, describing accurate mapping of referring expressions for GUI elements to screen coordinates as the basis for pixel-level operation. Separately, one paper claims a causal relationship from Code generation to GUI automation, stating that executable Python code can enable semantically clear and precise actions for operating-system control.

## Sources

**GUI control** (2 papers: [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf), [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf))
> The observable action of interacting with graphical user interfaces, including navigating web pages, clicking buttons, and filling in forms, to manage enterprise software systems.

**GUI automation** (1 paper: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> Performing end-to-end computer interface tasks by navigating software and executing interface actions to achieve a goal state.

**GUI interaction** (1 paper: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf))
> Interacting with a computer system by manipulating graphical elements like windows, icons, and buttons using a mouse and keyboard.

**UI control** (1 paper: [On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf))
> The observable behavior of an agent interacting with a digital device's user interface to accomplish tasks specified in natural language.

**GUI navigation** (2 papers: [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf), [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf))
> Selecting and executing actions on interface elements to complete web or mobile tasks from screenshots and instructions.

**Pixel-level operation** (1 paper: [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf))
> Executing direct interactions on a GUI such as clicking or typing at specific screen coordinates without relying on underlying code structures.

**On-device control** (1 paper: [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e472cd579c83e2f6aa3459f46aac28-Paper-Conference.pdf))
> The act of operating a mobile device's applications and functionalities to fulfill user requests.

**Mobile device control** (2 papers: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf), [ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation](https://aclanthology.org/2025.naacl-long.244.pdf))
> Completing tasks by operating mobile interfaces and apps through GUI actions.

**Computer interaction** (1 paper: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf))
> Completing tasks through direct interaction with desktop or GUI-based computer interfaces.

**Cross-application task completion** (1 paper: [AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf))
> The observable performance on tasks that require navigating and interacting with multiple distinct software applications to achieve a single goal.

**Cross-app task execution** (1 paper: [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf))
> Completing a task that requires switching between multiple applications and coordinating actions across them.

**Single-app task execution** (1 paper: [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf))
> Completing a task within one mobile application by performing the required sequence of UI actions.

**Software application manipulation** (1 paper: [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf))
> Using desktop applications to perform everyday tasks such as browsing, email, editing, and office workflows.

**Computer control** (1 paper: [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf))
> The observable task of an agent interacting with a computer environment, such as a webpage or application, by perceiving states and executing actions via keyboard and mouse inputs.

**UI interaction** (1 paper: [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381.pdf))
> The model interacts with graphical user interface elements such as menus, buttons, and controls to perform actions step by step.

**Interface manipulation** (1 paper: [Boosting Virtual Agent Learning and Reasoning: A Step-Wise, Multi-Dimensional, and Generalist Reward Model with Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25b/miao25b.pdf))
> Operating UI elements in digital environments to accomplish tasks.

## Relationships

### GUI automation →
- **AitW** (measurement instrument): *measured_by*, 2 papers
  > Android In The Wild (AITW) (Rawles et al., 2023) dataset is a mobile navigation benchmark including 30K instructions and 715K corresponding operation trajectories.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
  - [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e472cd579c83e2f6aa3459f46aac28-Paper-Conference.pdf)

### → GUI automation
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > OSCAR generates executable Python code to directly interface with the OS, enabling semantically clear and precise actions, ensuring broad applicability across diverse tasks. (Section 2)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **Visual grounding** (construct): *causes*, 1 paper
  > In this paper, we advocate a human-like embodiment for GUI agents that perceive the environment entirely visually and directly perform pixel-level operations on the GUI. The key is visual grounding models that can accurately map diverse referring expressions of GUI elements to their coordinates on the GUI across different platforms. (ABSTRACT)
  - [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf)
