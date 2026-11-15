# Action grounding
**Type:** Behavioral indicator  
**Supporting papers:** 12  
**Also known as:** Clicking, Dragging, UI grounding, GUI action grounding, GUI grounding  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats action grounding as locating the GUI element or screen position needed to carry out a natural language instruction. Most definitions operationalize success as returning coordinates, usually a click position or bounding box for the target element, while some broaden it to converting an instruction into an executable action and its associated parameters within a GUI or operating system. A smaller line of work specifies action-level forms such as clicking, which requires localizing the element to click, and dragging, which requires both initial and end coordinates.

**Variants.** Papers study closely related variants on webpages, screenshots, mobile screens, and general GUI or operating-system interfaces. The most explicit sub-tasks are clicking, drag-and-drop, and bbox-style element or action grounding, and similar task names include UI grounding, GUI action grounding, and GUI grounding. Some formulations emphasize single target localization, such as finding the element to click for a specified action, while others describe selecting executable elements or locations such as a button or menu item.

**Space of elicitation and scores.** Papers link action grounding to 3 measurement instruments. ScreenSpot is the most frequent and is used to assess single-step or cross-platform GUI grounding, Multimodal Mind2Web is used for further assessment of GUI grounding models after alignment, and OSWorld is used in open-ended computer environments, where one paper reports agents struggling with GUI grounding and operational knowledge. Across these uses, papers present the instruments as evaluations of grounding capability.

**What it is taken as evidence of.** Only 1 construct is linked to action grounding, Out-of-distribution generalization. One paper claims a causal relationship from action grounding to this construct, in the context of grounding data synthesis and scaling the pre-training corpus to improve OOD downstream performance, and no competing construct link appears in the papers cited. Separately, one paper says action grounding is related to privacy leakage, stating that attacks on the action grounding stage can leak users' specific PII.

## Sources

**Action grounding** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> Locating the click position or target element needed to carry out a specified action on a webpage.

**Clicking** (1 paper: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> The action of identifying and specifying the coordinates of a target UI element to be clicked.

**Dragging** (1 paper: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> The action of identifying and specifying both the start and end coordinates for a drag-and-drop operation on a UI element.

**UI grounding** (2 papers: [UI-Hawk: Unleashing the Screen Stream Understanding for Mobile GUI Agents](https://aclanthology.org/2025.emnlp-main.920.pdf), [AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf))
> Producing bounding box coordinates that accurately localize a specified UI element on a mobile screen in response to a textual instruction.

**GUI action grounding** (1 paper: [GUI-Bee: Align GUI Action Grounding to Novel Environments via Autonomous Exploration](https://aclanthology.org/2025.emnlp-main.1688.pdf))
> Mapping natural language instructions to specific executable elements or locations on a GUI screen, such as clicking a button or selecting a menu item.

**GUI grounding** (1 paper: [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf))
> The model's ability to transform natural language instructions into executable actions, such as coordinate-based operations, within a graphical user interface.

## Relationships

### Action grounding →
- **ScreenSpot** (measurement instrument): *measured_by*, 3 papers
  > We also include Bbox-version of element and action grounding subtasks in VisualWebBench (Liu et al., 2024c), ScreenSpot (Cheng et al., 2024), RefExp (Wichers et al., 2018) for GUI grounding.
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
  - [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf)
- **OSWorld** (measurement instrument): *measured_by*, 1 paper
  > Extensive evaluation of state-of-the-art LLM/VLM agents on OSWORLD reveals deficiencies in their ability to serve as computer assistants. While humans accomplish 72.4% of the tasks, the best agents achieve <12.2%, struggling with GUI grounding and operational knowledge. (Abstract)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Out-of-distribution generalization** (construct): *causes*, 1 paper
  > omitting the pre-training stage significantly degrades performance... These results highlight the critical importance of the data infrastructure for grounding data synthesis; with this infrastructure in place, we can easily improve OOD downstream performance simply by scaling the pre-training corpus. (Section 5.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **Multimodal Mind2Web** (measurement instrument): *measured_by*, 1 paper
  > We extend our evaluation by following Gou et al. (2024) to leverage the test data from Multimodal-Mind2Web (Zheng et al., 2024b) for further assessing the GUI grounding models after the alignment. (Section 5.1)
  - [GUI-Bee: Align GUI Action Grounding to Novel Environments via Autonomous Exploration](https://aclanthology.org/2025.emnlp-main.1688.pdf)

### Associated with
- **Privacy leakage** (behavioral indicator), 1 paper
  > EIA with the MI strategy can attack the action grounding stage of SeeAct and leak users' specific PII
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
