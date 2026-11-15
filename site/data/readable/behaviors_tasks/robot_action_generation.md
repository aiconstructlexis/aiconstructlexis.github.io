# Robot action generation
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Discrete action generation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this behavior as generating robot control actions from visual observations and language instructions. Most descriptions frame the output as a sequence of action tokens for robot control, while a smaller framing casts it as textual output that corresponds to a predefined set of robot commands. Some work also describes the text output as containing numerical values, such as 2D image coordinates, for a robot action.

**Variants.** Papers study several variants of this behavior. One line focuses on discrete action generation in a fixed action space, with commands such as "base-forward," "base-backward," "base-stop," "gripper-open," and "gripper-close" (Randomized Smoothing Meets Vision-Language Models). Another line describes actions for settings including pick-and-place and rotation decisions, and text outputs aligned to image pixel coordinates for robot actions (LLaRA: Supercharging Robot Learning Data for Vision-Language Policy).

**Space of elicitation and scores.** No measurement instrument is linked to this behavior, so the papers do not identify a recurring instrument that elicits or scores it.

**What it is taken as evidence of.** No construct is linked to this behavior. The papers therefore do not report what construct it is taken to reflect.

## Sources

**Robot action generation** (2 papers: [Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance](https://aclanthology.org/2025.emnlp-main.1367.pdf), [LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://proceedings.iclr.cc/paper_files/paper/2025/file/909f526db5127f8bd8158af32d9e313a-Paper-Conference.pdf))
> The observable task of producing a sequence of action tokens to control a robot based on visual and linguistic inputs.

**Discrete action generation** (1 paper: [Randomized Smoothing Meets Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1396.pdf))
> Producing a textual output that corresponds to a predefined set of robot commands or actions, such as 'base-forward' or 'gripper-open', in a Vision-Language-Action system.
