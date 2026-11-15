# Story generation
**Type:** Behavioral indicator  
**Supporting papers:** 25  
**Also known as:** Story writing, Narrative generation, Constrained story generation, Keyword-based story generation, Personalized story generation, Short story generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is prompt-based generation of a narrative or story text. Some definitions widen this to descriptive text that forms a story, describes a scene, or narrates character actions, while smaller lines of work define the task more narrowly as continuing a story from its first sentence, producing brief stories around given characters and plot elements, or generating coherent short stories under explicit prompt constraints.

**Variants.** Papers use several nearby names, most often story writing, narrative generation, and story generation. Smaller variants include constrained story generation, keyword-based story generation, personalized story generation, and short story generation, spanning long-form fiction, story continuation, real-time character and scene narration, keyword placement in the middle or end of sequences, and children's bedtime stories tailored to sociocultural factors.

**Space of elicitation and scores.** Papers link story generation to 3 measurement instruments: StoryCloze, TinyStories, and WritingPrompts. StoryCloze is described as a dataset of short stories with valid and invalid endings and is modified in one study for open-ended generation from a scenario's first sentence, WritingPrompts is used as a story-generation dataset, and TinyStories is used to test a model's ability to continue stories.

**What it is taken as evidence of.** Papers do not link story generation to any construct as something it indicates. Separately, one paper relates instruction following to a set of tasks that paraphrase, simplify, summarize, or generate stories.

## Sources

**Story writing** (2 papers: [First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf), [fLSA: Learning Semantic Structures in Document Collections Using Foundation Models](https://aclanthology.org/2025.emnlp-main.1290.pdf))
> The specific task of generating a narrative or story in response to a user prompt.

**Narrative generation** (2 papers: [Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf), [Beyond Outlining: Heterogeneous Recursive Planning for Adaptive Long-form Writing with Language Models](https://aclanthology.org/2025.emnlp-main.1254.pdf))
> The observable act of producing descriptive text that forms a story, describes a scene, or narrates a character's actions.

**Story generation** (2 papers: [Agents' Room: Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf), [What's the Difference? Supporting Users in Identifying the Effects of Prompt and Model Changes Through Token Patterns](https://aclanthology.org/2025.acl-long.985.pdf))
> The general task of creating a narrative text from a prompt.

**Constrained story generation** (1 paper: [Does quantization affect models' performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.479.pdf))
> The observable task of generating a coherent short story that adheres to an increasing number of specific constraints provided in the prompt.

**Keyword-based story generation** (1 paper: [Conditional [MASK] Discrete Diffusion Language Model](https://aclanthology.org/2025.emnlp-main.450.pdf))
> Generating coherent narratives that incorporate specified keywords at arbitrary positions in the sequence.

**Personalized story generation** (1 paper: [Biased Tales: Cultural and Topic Bias in Generating Children's Stories](https://aclanthology.org/2025.emnlp-main.3.pdf))
> The task of generating a narrative tailored to specific user-provided factors, such as a child's gender, nationality, or ethnicity.

**Short story generation** (1 paper: [Quality-Diversity through AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/5b9bef4eae0f574cedbf9f4bf29d8ae7-Paper-Conference.pdf))
> Creating brief narrative texts involving specified characters and plot elements, with variation in genre and story outcome.

## Relationships

### Story generation →
- **StoryCloze** (measurement instrument): *measured_by*, 1 paper
  > For our story generation task, we use the StoryCloze (Mostafazadeh et al., 2017) dataset, which was originally used for story understanding, and consists of short stories each with a valid ending sentence as well as an invalid ending. (Section 3)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **WritingPrompts** (measurement instrument): *measured_by*, 1 paper
  > "(II) Story-telling: We also fine-tune LLaMa2 on the story-generation dataset WritingPrompts"
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
- **TinyStories** (measurement instrument): *measured_by*, 1 paper
  > In Section 4.2, we first train a model based on ARDTs and test its ability to continue stories on Tinystories Eldan & Li (2023)... (Section 4.2)
  - [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf)

### Associated with
- **Instruction following** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
