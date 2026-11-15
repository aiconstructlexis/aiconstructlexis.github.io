# Error recovery
**Type:** Construct  
**Supporting papers:** 17  
**Also known as:** Failure recovery, Error tolerance, Error handling, Out-of-sync recovery  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats error recovery as a latent ability or capability to recover from mistakes in perception, skill execution, partner actions, invalid actions, or unexpected state changes and continue toward task completion or goal progress; one paper reports that LLMs "struggle to recover from skill failures and perception grounding errors." Several definitions broaden this to handling and managing execution errors, including revising code or adjusting reasoning from execution feedback. A smaller, narrower framing specializes it to out-of-sync recovery, where the agent must notice that its belief has diverged from the true state, diagnose the mismatch, and update its understanding to resynchronize, while one paper instead casts it as observable self-correction during inference rather than a latent capability.

**Space of facets.** Papers use adjacent labels such as failure recovery, error tolerance, error handling, and out-of-sync recovery for overlapping formulations of the same general idea. One framing groups supporting mechanisms such as error identification, recovery loops, self-correction, and fallback strategies under error handling, while the out-of-sync variant is explicitly broken into recognizing state mismatch, identifying root causes, acquiring the missing update, and updating belief to match the world state. Across these formulations, the main variation is whether detection is bundled into the construct itself or treated as preceding recovery, and whether recovery targets general task execution, the reasoning process itself, or belief-state resynchronization.

**Space of measurement.** No measurement instrument is linked to it. Papers instead operationalize it through five behavioral indicators, most often Backtracking, then Error detection, Self-reflection, Task completion, and Technical problem solving. These indicators make recovery visible through observing action outcomes, sending unconfirmed actions to a recovery module, revising reasoning or tool choice after self-reflection, associating successful recovery with technical problem-solving proficiency, and resuming progress to completion, which aligns with definitions centered on correcting errors and continuing the task.

**Links.** Papers claim a causal relationship from Backtracking to Error recovery, from Self-reflection to Error recovery, and from Technical problem solving to Error recovery. In the recorded evidence, backtracking lets an agent observe action outcomes and recover from error states effectively, self-reflective inference supports iterative reasoning, tool use, and error recovery, and successful out-of-sync recoveries are said to hinge on technical problem-solving proficiency. Error recovery is also related to Error detection, which sends the agent to a reflector when an action is not confirmed, and related to Task completion, with one report describing an agent that can recover from such states and complete the requested instruction. No correlational link is reported.

## Sources

**Error recovery** (3 papers: [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf), [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf), [CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.194.pdf))
> The ability to recover from mistakes in perception, skill execution, or partner actions and continue toward task completion.

**Failure recovery** (1 paper: [Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf))
> The ability of an agent to effectively adjust its plan and continue making progress toward a goal after encountering an invalid action or unexpected state change.

**Error tolerance** (2 papers: [OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf), [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf))
> The capability of a model to effectively handle and recover from errors, such as by revising its code or adjusting its reasoning based on execution feedback.

**Error handling** (1 paper: [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf))
> The latent capability of an agent to detect, recover from, and manage execution errors or unexpected situations during task performance.

**Out-of-sync recovery** (1 paper: [SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf))
> The ability of an agent to detect that its internal understanding of a system state has diverged from the true state, diagnose the cause of the mismatch, and update its understanding to resynchronize.

## Relationships

### → Error recovery
- **Technical problem solving** (behavioral indicator): *causes*, 1 paper
  > This observation further substantiates that successful out-of-sync recoveries hinge on not only agents’ technical problem-solving proficiency, but their efficient cause analysis and effective collaboration capabilities.
  - [SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > SCRIBE combines domain-specific tools with a self-reflective inference pipeline that supports iterative reasoning, tool use, and error recovery. (Abstract)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > BacktrackAgent explicitly incorporates a backtracking mechanism to observe the outcomes of action executions, allowing it to detect and recover from error states effectively. (Section 2)
  - [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf)

### Associated with
- **Task completion** (behavioral indicator), 1 paper
  > “DigiRL is able to recover from such states and complete complex instruction as requested”
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
- **Error detection** (behavioral indicator), 1 paper
  > If both the Verifier and the Judger confirm that ai t is correct, the agent considers it the final action at time-step t and proceeds to time-step t+1. Otherwise, the agent goes to the Reflector for error recovery. (Section 3.2)
  - [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf)
