# Knowledge generation
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Fact extraction, General knowledge recall, Supplementary evidence generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as producing or recalling supporting facts, concepts, or other relevant information in response to a prompt, question, answer options, or a claim. Some papers narrow it to extraction-style outputs, asking a model to "extract all facts" from conversational history or to "break the model response into sentence-level factual statements" for verification against context.

**Variants.** Papers use several nearby names for this behavior, including knowledge generation, fact extraction, general knowledge recall, and supplementary evidence generation. The settings range from intermediate knowledge for commonsense reasoning, to question-by-question production of supporting facts for questions and options, to extracting long-term conversational facts, to claim-guided supplementary evidence, and to recalling broad background knowledge during a reasoning phase.

**Space of elicitation and scores.** Papers link it to 1 measurement instrument, TOFU. In the linked usage, TOFU appears under "Fictitious Knowledge Generation" and is described as questions about fake authors synthesized by GPT-4, and no other instrument is linked.

**What it is taken as evidence of.** No construct is linked to this behavior, so the surveyed papers do not explicitly treat it as evidence of a named construct. Separately, one paper reports that Knowledge generation is related to Factual recall, describing generated knowledge prompting as asking the model to recall or synthesize relevant knowledge before answering.

## Sources

**Knowledge generation** (1 paper: [Why and How LLMs Benefit from Knowledge Introspection in Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.352.pdf))
> The observable act of a model producing text that represents supporting facts, concepts, or other relevant information in response to a prompt.

**Fact extraction** (3 papers: [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf), [Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning](https://aclanthology.org/2025.emnlp-main.580.pdf), [LongReward: Improving Long-context Large Language Models with AI Feedback](https://aclanthology.org/2025.acl-long.187.pdf))
> Generating supporting factual statements for a question and answer options from a language model.

**General knowledge recall** (1 paper: [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf))
> The observable behavior of generating broad, background knowledge relevant to a given question and set of options.

**Supplementary evidence generation** (1 paper: [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf))
> Generating additional relevant facts or statements using the LLM’s internal knowledge, guided by the claim and summarized evidence.

## Relationships

### Knowledge generation →
- **TOFU** (measurement instrument): *measured_by*, 1 paper
  > Fictitious Knowledge Generation. TOFU (Maini et al., 2024) consists of questions about fake authors synthesized by GPT-4. (Section 4.1).
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)

### Associated with
- **Factual recall** (behavioral indicator), 1 paper
  > Knowledge recall: Generated knowledge prompting (Liu et al., 2022) asks the model to recall or synthesize relevant knowledge before answering, simulating a form of self-retrieval and improving performance on commonsense benchmarks. (Section 2)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
