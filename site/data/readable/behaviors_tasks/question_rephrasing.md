# Question rephrasing
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Question rewriting  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats question rephrasing as rewriting or paraphrasing a question while preserving its meaning, and sometimes explicitly its answer. Most formulations describe changing the linguistic form without altering intent, as in instructions to "generate a paraphrase of that question without changing the meaning of it." A smaller line of work adds a further aim beyond paraphrase, such as making the question less ambiguous, more aligned with model capabilities, clarifying conditions, or restating it more simply when models misunderstand the original.

**Variants.** Variants are distinguished mainly by setting. Papers study mathematical question rephrasing, including using "rephrasing prompting" to generate additional questions; vision-language use, where question wording is modified using salient image details and appears as a "Rephrasing and Augmenting the Question" stage; problem-solving use that rephrases questions more simply; and evaluation use that creates rephrased benchmarks. Some authors also use the name "question rewriting" for the same behavior.

**Space of elicitation and scores.** Papers usually elicit this behavior directly as an instruction or pipeline step rather than through a named instrument, for example by tasking an LLM with rephrasing questions in a dataset without altering their meaning, or by specifying a task type of question rewriting. No measurement instrument is linked to it, and the papers do not specify a recurring scoring rule beyond whether the rephrased question preserves meaning, intent, or answer.

**What it is taken as evidence of.** No construct is linked to this behavior. As a result, the papers do not specify a construct that question rephrasing is taken to indicate.

## Sources

**Question rephrasing** (4 papers: [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf), [Rephrase, Augment, Reason: Visual Grounding of Questions for Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/eef6cb60fd59b32d35718e176b4b08d6-Paper-Conference.pdf), [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf), [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf))
> Rewriting a mathematical question in different linguistic forms while preserving its meaning and answer.

**Question rewriting** (1 paper: [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf))
> Rephrasing a question while preserving its meaning.
