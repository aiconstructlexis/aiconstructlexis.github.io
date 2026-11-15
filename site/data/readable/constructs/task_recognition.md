# Task recognition
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Task differentiation, Task vector retrieval  

## State of the Field

**Space of definitions.** The prevailing usage describes task recognition as identifying the target or underlying task, sometimes phrased as the required operation, from in-context demonstrations and then solving it with knowledge already acquired in pre-training. A smaller line of work uses nearby labels for narrower or more mechanistic versions of the same general capacity: task differentiation is the ability to distinguish tasks from input characteristics without explicit task labels, while task vector retrieval is a latent ability to extract a high-level task concept vector from demonstration pairs. Across these definitions, papers agree on inferring a task from demonstrations, but differ on whether they describe that capacity as an observable behavior, recognizing the task and using prior knowledge, or as latent retrieval of a task concept.

**Space of facets.** Some papers organize in-context learning by separating task recognition from task learning, and one paper explicitly says ICL is disentangled into the two. Beyond that pairing, papers use adjacent labels for related capacities rather than a single common subdivision: task differentiation highlights unsupervised separation of tasks and generalization to unseen tasks, while task vector retrieval emphasizes retrieval of a task concept vector that supports generalization across queries within the same task.

**Space of measurement.** No measurement instrument is linked to task recognition, and no named benchmark, evaluation scheme, probe, or analysis is explicitly recorded as measuring it. The only linked behavioral indicator is catastrophic forgetting, but that link is recorded as related rather than measured_by, so papers mostly describe the construct through the target behaviors in their definitions: recognizing the task from demonstrations, differentiating tasks without labels, or retrieving a task concept vector.

**Links.** The only linked construct is task learning, which is reported to correlate with task recognition; one paper says that "the performance of task recognition and task learning changes in the opposite direction." The only linked behavioral indicator is catastrophic forgetting, which is related to task recognition in a paper that says the catastrophic effects of fine-tuning may be explained as "shifting task inference" and that prompts farther from the fine-tuning data can recover pretrained capabilities.

## Sources

**Task recognition** (2 papers: [Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/83d349b6eb8125588b5f091e2d47525c-Paper-Conference.pdf), [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf))
> The ability of a language model to identify the target task from in-context demonstrations and then solve it by utilizing its pre-existing knowledge.

**Task differentiation** (1 paper: [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf))
> The model's ability to distinguish between different tasks based on their input characteristics, without relying on explicit task labels.

**Task vector retrieval** (1 paper: [Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf))
> The latent ability of a transformer to extract a high-level task concept vector from demonstration pairs during in-context learning, enabling generalization across queries within the same task.

## Relationships

### → Task recognition
- **Task learning** (construct): *correlates*, 1 paper
  > “the performance of task recognition and task learning changes in the opposite direction”
  - [Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/83d349b6eb8125588b5f091e2d47525c-Paper-Conference.pdf)

### Associated with
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > We find that the catastrophic effects of fine-tuning may be explained as shifting task inference and that transforming prompts further from the fine-tuning data can recover pretrained capabilities. (Section 6)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
