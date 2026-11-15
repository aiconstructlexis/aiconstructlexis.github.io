# Creative writing
**Type:** Behavioral indicator  
**Supporting papers:** 37  
**Also known as:** Content creation, Story continuation, Sonnet writing, Ancient prose writing, Poetry writing, Ci writing, Qu writing, Couplet writing, Text creation, Storytelling, Poem writing, Poem generation, Poetry composition, Novel writing, Creative story generation, Creative composition, Long-form Narrative Generation, Story completion  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is open-ended generation of novel, imaginative, or original text from a prompt, commonly stories, poems, blog posts, scripts, narratives, or other authored text. Some papers narrow this to collaborative writing with a model, multimodal prompting such as writing from audio, or knowledge-intensive story writing that must incorporate specified information. A smaller group operationalizes it as continuation or completion of a given story, and one benchmark-style formulation treats success as choosing the most plausible continuation; when papers state evaluation criteria, they emphasize originality, innovation, coherence, or adherence to prompt-specified form and tone.

**Variants.** Papers use several names and settings around the same behavior, including content creation, text creation, storytelling, story continuation, and story completion. Common variants center on poetry and narrative writing, from open-ended story generation to long-form fiction of 1,000-2,000 tokens, and from general poem writing to constrained forms such as sonnets or poem generation with specified format, rhyme, rhythm, and tone. Other variants cover classical Chinese prose and poetic forms, multimodal writing from audio prompts, collaborative poem writing from personal or fictional prompts, and one paper treats creative composition as related to text generation tasks that require novel artifacts under defined constraints.

**Space of elicitation and scores.** Papers link it to 2 evaluation benchmarks, AlpacaEval 2.0 and WildBench. In AlpacaEval 2.0, creative writing is grouped with tasks that require modeling human open-ended preference, while WildBench includes creative writing with multiple constraints on style and content among its challenging tasks.

**What it is taken as evidence of.** The construct linkage is narrow: papers relate it to 1 construct, Creativity, rather than linking it to multiple constructs. The recurring language is that creative writing gives greatest weight to a creativity dimension, and open-ended poem writing is discussed alongside emerging abilities like creativity, so the construct-linked papers use the same creativity-centered framing.

## Sources

**Creative writing** (7 papers: [Condor: Enhance LLM Alignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1091.pdf), [Personality Matters: User Traits Predict LLM Preferences in Multi-Turn Collaborative Tasks](https://aclanthology.org/2025.emnlp-main.71.pdf), [LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf), [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf), [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf), [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.357.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf))
> Generating novel and imaginative text, such as stories, blog posts, or scripts, based on a given prompt.

**Content creation** (2 papers: [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf), [A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf))
> Generating creative or original written content such as stories or other authored text.

**Story continuation** (2 papers: [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf), [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf))
> Generating the next words of a story from a short story beginning so that the output extends the narrative.

**Sonnet writing** (1 paper: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf))
> Generating a poem following a strict rhyme scheme and incorporating specific provided words.

**Ancient prose writing** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> Composing original prose in classical Chinese in response to a prompt or scenario.

**Poetry writing** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> Composing an ancient-style poem based on a specified theme and form.

**Ci writing** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> Composing a ci poem according to a specified theme and tune pattern.

**Qu writing** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> Composing a qu poem according to a specified theme and tune pattern.

**Couplet writing** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> Composing a complete couplet for a specified theme or occasion.

**Text creation** (1 paper: [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf))
> The task of generating creative text, such as writing poetry or crafting headlines.

**Storytelling** (1 paper: [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf))
> The task of generating a narrative or story from a given prompt or context.

**Poem writing** (1 paper: [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf))
> The task of generating a poem based on a given prompt or theme.

**Poem generation** (1 paper: [3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf))
> The task of creating poetry that adheres to specific constraints on format, rhyme, rhythm, and tone as specified in the prompt.

**Poetry composition** (1 paper: [AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf))
> The task of generating poems, often based on a prompt or an initial line from an existing poem.

**Novel writing** (1 paper: [AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf))
> The task of generating paragraphs of a novel, often initiated with a starting sentence from an existing human-written work.

**Creative story generation** (1 paper: [Improving Diversity in Language Models: When Temperature Fails, Change the Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verine25a/verine25a.pdf))
> Generating diverse and engaging stories from prompts in an open-ended setting.

**Creative composition** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> The observable behavior of performing a generation task that requires the production of a novel artifact given a set of defined constraints.

**Long-form Narrative Generation** (1 paper: [Agents' Room: Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf))
> The observable action of producing continuous fiction text of 1,000-2,000 tokens from a writing prompt.

**Story completion** (1 paper: [Measuring Diversity in Synthetic Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ac/zhu25ac.pdf))
> A generative language task where the model produces a continuation or ending for a given narrative prompt, used as one of the tasks for evaluating synthetic dataset diversity.

## Relationships

### Creative writing →
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as ... creative writing with multiple constraints on the style and content”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... and the other two tasks are tasks that require modeling human open-ended preference: Creative writing and making personal recommendations (Recommendation).
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)

### Associated with
- **Creativity** (construct), 2 papers
  > For Creative Writing, SaMer assigns the greatest importance to the creativity dimension, followed sequentially by logic, relevance, harmlessness, and style, which aligns closely with the essential attributes of creative writing.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > Creative composition encompasses generation tasks that require everyday creativity for personal goals... brainstorming solutions to personal problems requires inventive and harmless advice. (Section 1)
  - [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf)
