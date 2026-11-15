# Feedback generation
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Verbal feedback generation, Feedback comment generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats feedback generation as producing natural-language rationales that explain an evaluation or diagnose a failure. Most commonly, it is described as explaining why a response received a particular score, sometimes explicitly as analogous to chain-of-thought in evaluation; smaller lines of work use the same label for short explanations of why code failed, richer reflections on how a model can be improved, qualitative essay comments, or personalized formative feedback on quizzes and exercises. What counts as success is usually that the text explains why a score was assigned or what went wrong, and in some papers that it also offers specific suggestions, pinpoints strengths and weaknesses, or guides improvement.

**Variants.** Papers study several variants under closely related names: general feedback generation, verbal feedback generation, and feedback comment generation. The settings range from model evaluation and socially aligned interaction, where the model provides feedback as rationales, to code self-repair, exemplar-guided reflection for prompt optimization, tutoring, and automated writing evaluation, where comments may be corrective, holistic, or multi-dimensional analytic. Separate papers also claim a causal relationship from feedback generation to response revision, code debugging, and code improvement.

**Space of elicitation and scores.** No measurement instrument is linked to it.

**What it is taken as evidence of.** The papers do not link it to any construct.

## Sources

**Feedback generation** (5 papers: [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [Efficient and Accurate Prompt Optimization: the Benefit of Memory in Exemplar-Guided Reflection](https://aclanthology.org/2025.acl-long.37.pdf), [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> Producing a rationale explaining why a particular score was assigned to a model response, analogous to chain-of-thought reasoning in evaluation.

**Verbal feedback generation** (1 paper: [Data-Driven Discovery of Dynamical Systems in Pharmacology using Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aea8bdc42d8ba3a67a69b3f18be93f69-Paper-Conference.pdf))
> The behavior of generating natural language text that reflects on a model's performance and provides specific suggestions for improvement.

**Feedback comment generation** (1 paper: [LLMs can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of L2 Graduate-Level Academic English Writing](https://aclanthology.org/2025.acl-long.423.pdf))
> The observable task of producing qualitative, textual feedback for an essay, intended to explain an assessment or guide improvement.

## Relationships

### Feedback generation →
- **Code debugging** (behavioral indicator): *causes*, 1 paper
  > Finally, this feedback is used by the code model to repair the program (5). (Figure 1 caption)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Response revision** (behavioral indicator): *causes*, 1 paper
  > “This feedback, comprising ratings and detailed explanations, informs the central agent’s revisions to its initial response.”
  - [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf)
- **Code improvement** (behavioral indicator): *causes*, 1 paper
  > The question-answer pairs are then used to generate ameliorative feedback to further refine the 3D object... feedback, Fref, is then applied to refine the code, as described Eq. (3). (Section 3.3)
  - [Generating CAD Code with Vision-Language Models for 3D Designs](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf)
