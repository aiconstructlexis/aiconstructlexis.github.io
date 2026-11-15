# Understanding
**Type:** Construct  
**Supporting papers:** 33  
**Also known as:** Comprehension, Comprehension ability, General comprehension capability, Understanding capability, Understanding ability  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats understanding as a latent capability to comprehend and correctly interpret meaning, intent, content, or task requirements. Many definitions emphasize instructions and user requests, such as understanding the implicit and explicit purpose and requirements of an instruction, while others apply the same framing to technical text, multimodal prompts, OS environments, or a client's symptoms and emotional context. A smaller line of work defines it through performance on discriminative or interrogative tasks, explicitly separating understanding from generative fluency and stating that generative capability may not be contingent upon understanding capability. Some authors also describe it as a foundational or general capability, and one definition adds that it is shaped by left-to-right autoregressive processing.

**Space of facets.** Papers often use understanding and comprehension for overlapping constructs, and they frequently place it alongside reasoning and generation as one of several model abilities. Where authors systematize it explicitly, a legal taxonomy treats Understanding as one aspect beside Memorization, Logic Inference, Discrimination, Generation, and Ethic, and describes it as comprehending and interpreting facts, entities, concepts, and relationships in legal texts. Within that scheme, the recorded related tasks are information extraction, fact checking, and named entity recognition. A smaller set of papers instead narrows the construct to instruction purpose and requirements, multi-hop query intent, or contextual meaning in long or multimodal inputs.

**Space of measurement.** Operationalization is sparse in the recorded links: understanding is linked to one measurement instrument, LexEval, and three behavioral indicators, fact checking, information extraction, and named entity recognition. LexEval is a benchmark that measures it as one aspect of a legal cognitive ability taxonomy, with tasks aimed at whether models comprehend and interpret facts, entities, concepts, and relationships in legal text. Papers also operationalize understanding through discriminative or interrogative tasks, question answering analyses that treat lack of coherence as a symptom of not fully understanding a request, and human evaluation of which response is more appropriate for panic scenarios. This generally matches the dominant definitions, because the operationalizations focus on correct interpretation of input meaning or intent rather than fluent generation alone.

**Links.** In the recorded relations, one paper reports that generative ability is correlated with understanding, while noting weaker correlation between generation and understanding performance than in humans. One paper conjectures a causal relationship from understanding to coherence, arguing that lack of coherence is a symptom of not fully understanding a request. Understanding is also related to general ability in one paper, and, in a legal taxonomy, it is related to information extraction, fact checking, and named entity recognition.

## Sources

**Comprehension ability** (3 papers: [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf), [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf))
> The latent capacity of a large language model to understand and correctly interpret complex instructions or tasks, such as those provided in a few-shot prompt.

**Understanding** (7 papers: [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://proceedings.neurips.cc/paper_files/paper/2024/file/5acd3c628aa1819fbf07c39ef73e7285-Paper-Datasets_and_Benchmarks_Track.pdf), [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf), [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf), [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf), [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf), [PanicToCalm: A Proactive Counseling Agent for Panic Attacks](https://aclanthology.org/2025.emnlp-main.649.pdf))
> The latent ability to correctly identify, interpret, or reason about content, as evidenced by performance on discriminative or interrogative tasks, independent of generative fluency.

**Comprehension** (9 papers: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf), [SongCreator: Lyrics-based Universal Song Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/92a7a03e1c716970848a4a86cc8243ee-Paper-Conference.pdf), [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf), [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf), [ToolHop: A Query-Driven Benchmark for Evaluating Large Language Models in Multi-Hop Tool Use](https://aclanthology.org/2025.acl-long.150.pdf), [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf), [Why Has Predicting Downstream Capabilities of Frontier AI Models with Scale Remained Elusive?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schaeffer25b/schaeffer25b.pdf))
> The ability to understand the implicit and explicit purpose and requirements of an instruction.

**General comprehension capability** (1 paper: [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf))
> The foundational ability of a large language model, derived from training on extensive text data, to understand and process information.

**Understanding capability** (1 paper: [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> The model's latent ability to comprehend and correctly interpret the meaning and intent of input text.

**Understanding ability** (1 paper: [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf))
> The latent capability of a large language model to comprehend and process textual information, which is influenced by its autoregressive, left-to-right processing nature.

## Relationships

### Understanding →
- **LexEval** (measurement instrument): *measured_by*, 1 paper
  > to systematically organize various evaluation tasks, we propose a Legal Cognitive Ability Taxonomy (LexAbility Taxonomy), which includes six aspects: Memorization, Understanding, Logic Inference, Discrimination, Generation, and Ethic. (Section 3.1)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coherence** (construct): *causes*, 1 paper
  > We conjecture that the instability, or lack of coherence, is a symptom of the model not being able to fully understand a request, i.e., accessing its parametric knowledge necessary for generating a correct answer. (Section 1)
  - [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf)

### → Understanding
- **Generative ability** (construct): *correlates*, 1 paper
  > Our results show that although models can outperform humans in generation, they consistently fall short of human capabilities in measures of understanding, showing weaker correlation between generation and understanding performance... (Section 1)
  - [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf)

### Associated with
- **Information extraction** (behavioral indicator), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts, which serves as a foundational requirement for applying knowledge to downstream tasks. We construct five tasks at this level: Legal Element Recognition (2-1)... (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts... We construct five tasks at this level: ...Legal Fact Verification (2-2)... (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Named entity recognition** (behavioral indicator), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts... We construct five tasks at this level: ...Named-entity Recognition (2-5). (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **General ability** (construct), 1 paper
  > degradation in foundational LLM capabilities such as comprehension, reasoning, and common sense — an effect known as alignment tax (Section 1)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
