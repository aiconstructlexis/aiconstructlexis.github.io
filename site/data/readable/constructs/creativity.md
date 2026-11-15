# Creativity
**Type:** Construct  
**Supporting papers:** 52  
**Also known as:** Creative thinking, Creative problem-solving, Creative intelligence, Creative reasoning, Creative quality  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats creativity as either a latent model ability or an output quality centered on producing novel, original, imaginative, or unconventional content, ideas, or solutions. Many definitions pair novelty with another criterion such as diversity, value, appropriateness, attractiveness, or coherence, for example novel robotic tasks beyond existing benchmarks, out-of-the-box solutions to social problems, or content that reimagines beyond literal translation. A smaller line of work narrows this to creative thinking under constraints, creative problem-solving through non-obvious steps, or creative reasoning in unfamiliar environments, while some papers shift from model ability to human-perceived creative quality judged through cleverness, remoteness, and uncommonness. Definitions differ chiefly on whether creativity is a broad latent capability of the model or a quality of particular outputs such as advice, lyrics, stories, images, or ideas.

**Space of facets.** Where papers systematize the concept, they break it into neighboring facets rather than using a single shared taxonomy. One line explicitly says creativity includes convergent thinking, described as purposefulness toward a goal, and divergent thinking, described as adaptability to explore new environments or constraints; other work separates intrinsic qualities of ideas, such as semantic flexibility or diversity, from extrinsic statistical infrequency, or breaks advertisement creativity into atypicality and originality. Nearby labels are also used for different levels of scope: creative intelligence is presented as a broader trait in a triarchic model, alongside analytical and practical capabilities, creative reasoning as a more specific ability within unfamiliar problem settings, and creative quality as the human-rated overall creativity of an idea.

**Space of measurement.** In operational use, papers link creativity to 4 measurement instruments and 2 behavioral indicators. The named instruments span expert or trained-rater judgment, LLM scoring, and benchmarking: the Consensual Assessment Technique asks domain experts for holistic judgments of creativity, human evaluation rates outputs on dimensions that include creativity, LLM-as-a-judge grades samples for creativity alongside qualities such as clarity or factuality, and WildBench is used because its real-user tasks are described as requiring creativity. These operationalizations reflect the same split seen in definitions, since some papers treat creativity as performance on demanding tasks, while others score outputs directly for novelty, exceptional quality relative to a reference, coherence and creativity together, or dimensions such as uncommonness, remoteness, and cleverness; among linked behavioral indicators, creative writing is treated as related to creativity, while bias amplification appears in a causal claim rather than a direct measure.

**Links.** In the linked relations, creativity is connected most often to divergent thinking, with several papers describing diverse solution generation or adaptability under constraints as related to creativity. Other papers report it as related to associative reasoning, generation diversity, coherence, originality, imagination, and the behavioral indicator creative writing. Papers also claim causal relationships from bias amplification, visual perception, domain knowledge, and emotional intelligence to creativity: one paper says amplifying bias negatively influences creativity, while another says weak perception inhibits reasoning and creation and that tasks involving professional knowledge or emotional intelligence influence later creation tasks. No correlational relationship is reported.

## Sources

**Creativity** (14 papers: [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Quality-Diversity through AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/5b9bef4eae0f574cedbf9f4bf29d8ae7-Paper-Conference.pdf), [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [Is a Peeled Apple Still Red? Evaluating LLMs' Ability for Conceptual Combination with Property Type](https://aclanthology.org/2025.naacl-long.456.pdf), [Towards Automatic Evaluation for Image Transcreation](https://aclanthology.org/2025.naacl-long.359.pdf), [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf), [Benchmarking Language Model Creativity: A Case Study on Code Generation](https://aclanthology.org/2025.naacl-long.141.pdf), [REFFLY: Melody-Constrained Lyrics Editing Model](https://aclanthology.org/2025.naacl-long.564.pdf), [BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation](https://aclanthology.org/2025.acl-long.773.pdf), [Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf), [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> The latent ability of an LLM to generate novel, diverse, and previously unseen robotic tasks that go beyond the scope of existing human-curated benchmarks.

**Creative thinking** (1 paper: [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf))
> The ability to generate coherent, novel text under constraints that require imaginative planning and composition.

**Creative problem-solving** (1 paper: [LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs](https://aclanthology.org/2025.naacl-long.161.pdf))
> The ability to solve complex problems that require novel, intelligent, or non-obvious steps, rather than just following a straightforward procedure.

**Creative intelligence** (1 paper: [EscapeBench: Towards Advancing Creative Intelligence of Language Model Agents](https://aclanthology.org/2025.acl-long.39.pdf))
> A broad latent trait encompassing the capacity to think innovatively, adapt observations to new contexts, and generate original strategies in unstructured scenarios, as part of a triarchic model of intelligence.

**Creative reasoning** (1 paper: [EscapeBench: Towards Advancing Creative Intelligence of Language Model Agents](https://aclanthology.org/2025.acl-long.39.pdf))
> The latent ability of a language model agent to generate novel, adaptive solutions to problems by repurposing tools, identifying implicit goals, and solving puzzles in unfamiliar environments.

**Creative quality** (1 paper: [MuseScorer: Idea Originality Scoring At Scale](https://aclanthology.org/2025.emnlp-main.1009.pdf))
> A latent trait reflecting the overall perceived creativity of an idea, as judged by human raters on dimensions such as cleverness, remoteness, and uncommonness.

## Relationships

### Creativity →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > we do LLM-based grading of samples before and after self-correction in terms of clarity, grammaticality, factuality, writing style, and creativity. (Sec. 5.4)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > These tasks often require critical thinking, creativity, and technical expertise, making WILDBENCH substantially more challenging than AlpacaEval... (Section 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Consensual Assessment Technique** (measurement instrument): *measured_by*, 1 paper
  > The Consensual Assessment Technique (CAT) (Amabile, 1983) is a method for evaluating creative products by asking experts in the domain to provide their own holistic judgments of creativity, without being given explicit criteria to follow.
  - [Can Large Language Models Outperform Non-Experts in Poetry Evaluation? A Comparative Study Using the Consensual Assessment Technique](https://aclanthology.org/2025.emnlp-main.1625.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Following the evaluation criteria detailed in Section 4.3, we engaged a team of professionally trained evaluators to assess the generated greetings across five dimensions: language quality, creativity, emotional resonance, cultural appropriateness, and content richness.
  - [Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.868.pdf)

### → Creativity
- **Bias amplification** (behavioral indicator): *causes*, 1 paper
  > Conversely, amplifying bias also negatively influences the system in several ways. Besides the cases where the bias is malicious (it can be solved by designing an appropriate interaction phase where hbad /∈ Heff), it also influences the model’s creativity. (Section 3.3)
  - [Bias Amplification in Language Model Evolution: An Iterated Learning Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/4418f6a54f4314202688d77956e731ce-Paper-Conference.pdf)
- **Visual perception** (construct): *causes*, 1 paper
  > the weak perception of LVLMs inhibits authentic strengths in reasoning and creation. (Abstract).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Domain knowledge** (construct): *causes*, 1 paper
  > By analyzing these enhanced creation cases with perfect reasoning information, we found that some reasoning tasks involving Professional Knowledge influence the next creation tasks. (Section 5.1).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Emotional intelligence** (construct): *causes*, 1 paper
  > Some reasoning tasks needing Emotional Intelligence influence the relative creation tasks. (Section 5.1).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Divergent thinking** (construct), 3 papers
  > The DAT is a classic creativity test in which testee write 10 unrelated words, and words with greater “distances” in their context embeddings indicate more divergent thinking. (Section 3.3)
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
  - [Benchmarking Language Model Creativity: A Case Study on Code Generation](https://aclanthology.org/2025.naacl-long.141.pdf)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
- **Creative writing** (behavioral indicator), 2 papers
  > For Creative Writing, SaMer assigns the greatest importance to the creativity dimension, followed sequentially by logic, relevance, harmlessness, and style, which aligns closely with the essential attributes of creative writing.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **Generation diversity** (construct), 1 paper
  > hindering the exploration of novel and diverse ideas — a cornerstone of creativity.
  - [Diversity-Rewarded CFG Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a59a11e8580a7ac850cb792f6179c7a0-Paper-Conference.pdf)
- **Coherence** (construct), 1 paper
  > A central challenge is managing the trade-off between creativity and coherence, which is influenced by the sampling strategy during text generation. (Section 1)
  - [Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/afa5f124e36bed5cc2125067005d43f5-Paper-Conference.pdf)
- **Associative reasoning** (construct), 1 paper
  > A key aspect of evaluating creativity lies in assessing associative ability, which plays a central role in creativity by driving generative processes (Section 1).
  - [AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.263.pdf)
- **Originality** (construct), 1 paper
  > we attempt to break down visual advertisement creativity into atypicality and originality.
  - [Leveraging Large Models to Evaluate Novel Content: A Case Study on Advertisement Creativity](https://aclanthology.org/2025.emnlp-main.1072.pdf)
- **Imagination** (construct), 1 paper
  > Some reasoning tasks containing Imagination like “Tangram Speculation” may influence the corresponding creative task (“Tangram Segmentation”). (Section 5.1).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
