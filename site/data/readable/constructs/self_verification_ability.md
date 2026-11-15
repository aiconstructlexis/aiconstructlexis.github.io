# Self-verification ability
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Self-verification, Solution summarization, Self-evaluation  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage treats self-verification ability as an inherent, intrinsic, or emergent model capability to assess the correctness, validity, or quality of its own outputs, solutions, or reasoning steps, sometimes explicitly without external ground truth or assistance. Several papers make this capability concrete as code-based validation, natural-language checking, or confirmation of conclusions and overlooked cases. A smaller line uses the same label for a technique or procedure, namely prompting an LLM to reconsider a judgment or verify an extracted entity type, so the main divide is between self-verification as a latent capacity and as an elicited routine.

**Space of facets.** Papers differentiate the construct mainly by what is being checked and at what granularity. Some describe checking final answers, others verifying intermediate reasoning steps, reasoning trajectories, or the feasibility of an already generated reasoning path, and one formulation recasts it as solution summarization, where the model recalls intermediate steps, organizes them, and works backward to check consistency. Related labels remain nearby rather than fully merged: self-evaluation is used for assessing correctness and progress and for allocating self-assigned rewards, self-verification is discussed alongside self-correction and trial-and-error, and one paper mentions self-consistency separately from self-verification.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to it. When papers operationalize it directly, they usually do so procedurally: generating and ranking multiple answers, executing generated code to verify answers and then voting among them, asking the model to reconsider a previous judgment, checking whether an extracted entity has the correct type before retaining it, selecting among sampled responses through natural-language self-verification, or training the model to predict [eos] versus [refine] as an intrinsic verification signal. These operationalizations all instantiate internal checking, but they range from code execution to prompt-based re-evaluation and token-level refinement.

## Sources

**Self-verification** (6 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf), [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf), [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf))
> The inherent ability of a model to assess the correctness of its own generated solutions or reasoning steps, particularly by generating and executing code to validate an answer.

**Solution summarization** (1 paper: [CogMath: Assessing LLMs’ Authentic Mathematical Ability from a Human Cognitive Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ab/liu25ab.pdf))
> The latent ability to reflect on and verify one's own reasoning process, including explaining intermediate steps and performing backward reasoning to check consistency.

**Self-evaluation** (1 paper: [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf))
> The model's capacity to assess the correctness and progress of its own reasoning steps and solutions without relying on external ground truth.
