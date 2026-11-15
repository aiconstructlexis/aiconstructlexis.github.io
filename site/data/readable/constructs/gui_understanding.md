# GUI understanding
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** GUI Understanding, UI understanding, Screen understanding, Screen reading comprehension, GUI action grounding  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats GUI understanding as a latent capability or capacity to interpret visual screen or interface information, including structure, content, layout, text, icons, and function, and to identify relevant interactive or actionable elements. Several definitions converge on comprehension from visual inputs and accurate identification of buttons, menus, text fields, or other on-screen information for action selection. A smaller line of work narrows the construct to screen reading comprehension, reading textual and symbolic screen information to answer questions, or to GUI action grounding, mapping natural-language instructions to specific executable elements or locations.

**Space of facets.** Papers use several neighboring labels for overlapping but not identical phenomena: GUI understanding, UI understanding, and screen understanding name the broader interpretation of interface layouts and actionable components, while screen reading comprehension and GUI action grounding denote narrower slices. Element identification and grounding are often folded into the broader construct, with papers describing the need to interpret the screen, identify relevant elements, and "recognise actionable elements." One paper also lists screen understanding alongside planning and tool usage as separate agentic abilities.

**Space of measurement.** Operationalization is limited in the linked evidence: papers connect GUI understanding to 2 measurement instruments and 4 behavioral indicators. The direct instruments named are GUI-WORLD, described as a comprehensive benchmark for GUI understanding, and WebSRC, which one paper selects for GUI understanding. The linked behavioral indicators are Action prediction, Code generation, Optical character recognition, and Question answering, but these appear in causal claims rather than as direct measures. Overall, the direct measurements align most clearly with the broad framing of interpreting GUI content and structure from visual input, while screen reading comprehension and GUI action grounding are introduced as narrower conceptualizations.

**Links.** Papers report causal links only. In one direction, individual papers claim causal relationships from Optical character recognition to GUI understanding and from Question answering to GUI understanding, with one study saying OCR samples benefit most in GUI understanding and another saying QA samples enhance performance in GUI understanding benchmarks. In the other direction, papers claim causal relationships from GUI understanding to Code generation and to Action prediction: one paper says GUI understanding capability enhances generating operational code, and another says action prediction "builds on these skills" of UI understanding.

## Sources

**GUI understanding** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> The capability to comprehend the structure, content, and function of graphical user interfaces from visual inputs.

**GUI Understanding** (1 paper: [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf))
> The latent capability to interpret visual screen information and accurately identify interactive UI elements.

**UI understanding** (1 paper: [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf))
> The capacity to interpret complex mobile interface layouts and identify relevant on-screen information for action selection.

**Screen understanding** (1 paper: [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bonatti25a/bonatti25a.pdf))
> The latent ability to interpret and reason about visual and structural elements of a computer interface, including text, icons, and layout, to identify actionable components.

**Screen reading comprehension** (1 paper: [ScreenQA: Large-Scale Question-Answer Pairs Over Mobile App Screenshots](https://aclanthology.org/2025.naacl-long.477.pdf))
> The capacity to read and understand textual and symbolic information presented on a screen to answer specific questions.

**GUI action grounding** (1 paper: [GUI-Bee: Align GUI Action Grounding to Novel Environments via Autonomous Exploration](https://aclanthology.org/2025.emnlp-main.1688.pdf))
> The latent ability of a model to correctly map natural language instructions to specific actionable elements or locations on a Graphical User Interface screen.

## Relationships

### GUI understanding →
- **WebSRC** (measurement instrument): *measured_by*, 1 paper
  > We select VisualWebBench (Liu et al., 2024c), WebSRC (Chen et al., 2021), ScreenQA-Short (Hsiao et al., 2022), WidgetCap (Li et al., 2020) for GUI understanding.
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **GUI-WORLD** (measurement instrument): *measured_by*, 1 paper
  > Likewise, we also establish a comprehensive benchmark for GUI understanding, which encompasses nine mainstream MLLMs (e.g., GPT-4o (OpenAI, 2024) and Gemini-1.5-Pro (Team et al., 2023)), five keyframe selection strategies (e.g., UVD (Zhang et al., 2024d)), and six GUI scenarios, aiming to provide a thorough evaluation of the GUI-oriented understanding capabilities of MLLMs. (Section 1)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > To further demonstrate how GUI understanding capability enhances mainstream GUI-related tasks, including generating operational code (Cheng et al., 2024) and providing chat assistance (Hong et al., 2024), we conduct experiments as follows... (Section 4.2)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Action prediction** (behavioral indicator): *causes*, 1 paper
  > Action Prediction builds on these skills, testing whether agents can execute interactions like clicking, dragging, and typing based on their UI understanding
  - [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf)

### → GUI understanding
- **Optical character recognition** (behavioral indicator): *causes*, 1 paper
  > OCR samples benefit most in GUI understanding.
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *causes*, 1 paper
  > both QA and Caption samples enhance performance in GUI understanding and OCR-related benchmarks
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
