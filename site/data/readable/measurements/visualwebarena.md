# VisualWebArena
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** V-WebArena  

## State of the Field

**What it is.** Most descriptions treat VisualWebArena as a real benchmark environment for multimodal agents, or more specifically vision-language agents, on realistic visual web and web navigation tasks. The prevailing description places those tasks across classifieds, social media, and shopping platforms, while some authors emphasize GUI interaction and task completion in browser environments; a smaller usage refers to V-WebArena mainly as a comparison benchmark.

**What it is claimed to measure.** Among reported links, papers connect it to one behavioral indicator and no constructs. The measurement claim is concentrated on Web navigation: papers describe VisualWebArena as designed to evaluate multimodal agent performance across a wide range of web navigation tasks and environments.

**Space of uses.** Papers commonly use it as an evaluation environment to build on, for example by adding targeted adversarial tasks and evaluation scripts on top of it. It also appears alongside OSWorld as an existing agent testing environment, one paper restricts evaluation to an easy-task subset and only tests SoM agents, and another cites V-WebArena for comparison; no measurement instrument is linked to it.

**Concerns raised.** Some papers frame it within adversarial evaluation settings, adding targeted adversarial tasks in a realistic threat model and integrating pop-ups into the environment.

## Sources

**VisualWebArena** (2 papers: [Dissecting Adversarial Robustness of Multimodal LM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/460a1d8eac34125dad453b28d6d64446-Paper-Conference.pdf), [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411.pdf))
> A benchmark environment for evaluating multimodal web agents on realistic tasks across classifieds, social media, and shopping platforms.

**V-WebArena** (1 paper: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for evaluating multimodal agents on realistic visual web tasks, referenced for comparison.

## Relationships

### → VisualWebArena
- **Web navigation** (behavioral indicator): *measured_by*, 1 paper
  > We primarily experiment on VisualWebArena (VWA), a benchmark designed to evaluate multimodal agents performance on across a wide range of web navigation tasks and environments. (Section 4)
  - [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3b893ba1de12f76020b03f7ae8e1afd-Paper-Conference.pdf)
