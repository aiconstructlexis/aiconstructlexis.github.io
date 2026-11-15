# Factuality
**Type:** Construct  
**Supporting papers:** 144  
**Also known as:** Factual correctness, Correctness, Factual consistency, Entity-relation consistency, Factual reliability, Medical factuality, Independent factuality, Factual reasoning, Factual and Logical Correctness, Factuality hallucination, Factual accuracy, Fact discernment, Factuality preservation, Knowledge accuracy, Information accuracy  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats factuality as output correctness: generated statements, answers, rationales, summaries, or queries should be factually correct, accurate, and aligned with real-world or otherwise externally verifiable knowledge, often framed as being free from factual errors, unsupported claims, or hallucinations. Many definitions also tie it to grounding in retrieved documents, evidence, or other knowledge sources. A smaller line of work treats it as a latent ability or tendency of the model, sometimes tied to parametric knowledge or even to the hidden truth status of a statement, and some papers narrow the reference standard from world knowledge to source- or task-specific correctness, such as consistency with images, source articles, ground-truth annotations, dialogue state labels, or the user’s intended question.

**Space of facets.** Systematizations are mixed rather than uniform. Some papers place factuality under broader abilities, for example as part of Background Knowledge or as one dimension of instruction following, while others pair it with logical correctness as an objective criterion distinct from stylistic preferences. Several papers explicitly separate factuality from faithfulness: factuality is alignment with external or real-world knowledge, whereas faithfulness is alignment with the provided context, and one paper adds an independent factuality variant in which each subclaim is judged in isolation. Beyond this, papers reuse nearby labels such as factual accuracy, factual correctness, correctness, factual consistency, and factual reliability, and also introduce narrower variants tied to medical content, entity-relation consistency, fact discernment, or preservation across iterations.

**Space of measurement.** Operationally, papers link factuality to 21 measurement instruments and 6 behavioral indicators. The most frequent instruments are TruthfulQA, FActScore, LLM-as-a-judge, TriviaQA, and Human evaluation, with other instruments appearing less often. In practice, these operationalizations include short-form QA benchmarks, long-form claim or atomic-fact decomposition with verification against Wikipedia or retrieved passages, GPT-4 or GPT-4o judging or counting factual errors, F1 or exact-match factual QA scores, and direct human judgments that a response is accurate and has no factual errors. These measures usually follow the dominant correctness framing, though some papers operationalize factuality as source-grounded agreement, for example overlap of radiological entities and clinical relations, consistency with original annotations or source articles, or whether a SQL query correctly answers the user question.

**Links.** Relationally, papers connect factuality to 18 constructs and 6 behavioral indicators. The most recurring link is to hallucination: one paper records a causal relationship from factuality to hallucination, while many others treat them as related by describing hallucinations as non-factual, fabricated, or unsupported outputs and by targeting factuality in order to reduce hallucinations. Some papers treat constraint satisfaction as related to factuality, and one paper claims a causal relationship from logical consistency to factuality, while another treats the two as related. Single papers also report that factuality correlates with helpfulness and is related to faithfulness, with additional one-off causal or related links connecting it to several other constructs and behaviors.

## Sources

**Factual accuracy** (7 papers: [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/4410c0711e9154a7a2d26f9b3816d1ef-Paper-Conference.pdf), [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [MPVStance: Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification](https://aclanthology.org/2025.acl-long.53.pdf), [DETQUS: Decomposition-Enhanced Transformers for QUery-focused Summarization](https://aclanthology.org/2025.naacl-long.138.pdf), [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.56.pdf), [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf))
> The degree to which a model's generated statements are factually correct and free from errors.

**Factual correctness** (7 papers: [Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/880ee6e23b6ee548ebcccafe0ef0f513-Paper-Conference.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf), [KITAB: Evaluating LLMs on Constraint Satisfaction for Information Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/82846e19e6d42ebfd4ace4361def29ae-Paper-Conference.pdf), [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf), [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf), [AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.508.pdf))
> The degree to which a model's generated text, particularly its reasoning steps and final answers, aligns with established facts from external knowledge sources.

**Factuality** (27 papers: [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf), [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf), [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [CiteME: Can Language Models Accurately Cite Scientific Claims?](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef47f7b768e1a012e3d995ac8d8fac7-Paper-Datasets_and_Benchmarks_Track.pdf), [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf), [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf), [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf), [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf), [Evaluating Evidence Attribution in Generated Fact Checking Explanations](https://aclanthology.org/2025.naacl-long.282.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf), [DTELS: Towards Dynamic Granularity of Timeline Summarization](https://aclanthology.org/2025.naacl-long.136.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf), [Unlearning as multi-task optimization: A normalized gradient difference approach with an adaptive learning rate](https://aclanthology.org/2025.naacl-long.563.pdf), [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf))
> The degree to which a model's generated statements are factually correct and grounded in real-world knowledge.

**Correctness** (1 paper: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf))
> The factual accuracy and correctness of the information provided in the model's response.

**Factual consistency** (2 papers: [SeafloorAI: A Large-scale Vision-Language Dataset for Seafloor Geological Survey](https://proceedings.neurips.cc/paper_files/paper/2024/file/274de7d60333c0848f42e18ae97f13e3-Paper-Datasets_and_Benchmarks_Track.pdf), [What Is That Talk About? A Video-to-Text Summarization Dataset for Scientific Presentations](https://aclanthology.org/2025.acl-long.310.pdf))
> The degree to which generated annotations agree with the original ground-truth or source annotations.

**Entity-relation consistency** (1 paper: [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.186.pdf))
> The degree to which the relationships between entities in a text align with verified real-world knowledge, serving as a discriminative trait between human-written and machine-generated content.

**Factual reliability** (1 paper: [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf))
> The degree to which the outputs and reasoning steps of an LLM-based system are factually correct and free from hallucination.

**Medical factuality** (1 paper: [ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344.pdf))
> The extent to which a model's outputs align with established medical knowledge and avoid factual errors in clinical content.

**Independent factuality** (1 paper: [Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf))
> A property of a generated output where correctness is determined by evaluating each constituent claim in isolation against a ground truth, without considering the logical dependencies between claims.

**Factual reasoning** (1 paper: [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf))
> The ability to produce responses grounded in factual knowledge and to avoid generating false claims, especially in the presence of misleading or humorous prompts.

**Factual and Logical Correctness** (1 paper: [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf))
> The latent ability to distinguish objectively true statements from false or logically flawed ones, independent of stylistic preferences.

**Factuality hallucination** (1 paper: [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.186.pdf))
> The latent tendency of a language model to generate semantically plausible but factually ungrounded relationships between entities, reflecting a failure to align with real-world knowledge.

**Fact discernment** (1 paper: [Pandora's Box or Aladdin's Lamp: A Comprehensive Analysis Revealing the Role of RAG Noise in Large Language Models](https://aclanthology.org/2025.acl-long.250.pdf))
> The ability to accurately distinguish between correct factual information and incorrect or counterfactual statements, especially when both are present in the context.

**Factuality preservation** (1 paper: [LLM as a Broken Telephone: Iterative Generation Distorts Information](https://aclanthology.org/2025.acl-long.371.pdf))
> The degree to which generated text remains faithful to the factual information contained in the original source text across iterations.

**Knowledge accuracy** (2 papers: [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf), [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf))
> The model's ability to retrieve and apply factual knowledge accurately, especially in domains requiring broad general or domain-specific information.

**Information accuracy** (1 paper: [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf))
> The degree to which a system's responses are factually correct and consistent with dialogue state labels and external knowledge.

## Relationships

### Factuality →
- **Hallucination** (behavioral indicator): *causes*, 24 papers
  > underscores the need to develop effective and generalizable methods for fine-grained factuality alignment to reduce hallucinations in Large Language Models (LLMs).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [DTELS: Towards Dynamic Granularity of Timeline Summarization](https://aclanthology.org/2025.naacl-long.136.pdf)
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf)
  - [Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
  - [Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://aclanthology.org/2025.emnlp-main.150.pdf)
  - [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.186.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
  - [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf)
  - [The State of Multilingual LLM Safety Research: From Measuring The Language Gap To Mitigating It](https://aclanthology.org/2025.emnlp-main.800.pdf)
  - [Trustworthy Medical Question Answering: An Evaluation-Centric Survey](https://aclanthology.org/2025.emnlp-main.1398.pdf)
  - [Efficient Real-time Refinement of Language Model Text Generation](https://aclanthology.org/2025.emnlp-main.1753.pdf)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)
  - [Expanding before Inferring: Enhancing Factuality in Large Language Models through Premature Layers Interpolation](https://aclanthology.org/2025.emnlp-main.645.pdf)
  - [RAGEval: Scenario Specific RAG Evaluation Dataset Generation Framework](https://aclanthology.org/2025.acl-long.418.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 12 papers
  > For multiple choices, we use TruthfulQA (Lin et al., 2022) and FACTOR (News/Wiki) (Muhlgay et al., 2023) to assess LMs’ factuality in short-answer/long-paragraph settings, respectively.
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia](https://proceedings.neurips.cc/paper_files/paper/2024/file/c63819755591ea972f8570beffca6b1b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Expanding before Inferring: Enhancing Factuality in Large Language Models through Premature Layers Interpolation](https://aclanthology.org/2025.emnlp-main.645.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
- **FActScore** (measurement instrument): *measured_by*, 11 papers
  > Due to the relatively consistent and high quality of Wikipedia articles, we elect to use FactScore as a representative method of reference-based truthfulness scoring. (Section 3.1)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
  - [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
  - [Fictitious Synthetic Data Can Improve LLM Factuality via Prerequisite Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98ecdc722006c2959babbdbdeb22eb75-Paper-Conference.pdf)
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf)
  - [LLM as a Broken Telephone: Iterative Generation Distorts Information](https://aclanthology.org/2025.acl-long.371.pdf)
  - [Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25aj/lee25aj.pdf)
  - [Agent-as-Judge for Factual Summarization of Long Narratives](https://aclanthology.org/2025.emnlp-main.1204.pdf)
  - [DnDScore: Decontextualization and Decomposition for Factuality Verification in Long-Form Text Generation](https://aclanthology.org/2025.emnlp-main.1205.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 9 papers
  > Using GPT-4 as a judge, we find that FactTune-MC and FactTune-EC can improve both factuality and fluency compared to the SFT model (examples in Appendix Table 8). (Section 4.2)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf)
  - [Identifying Reliable Evaluation Metrics for Scientific Text Revision](https://aclanthology.org/2025.acl-long.335.pdf)
  - [SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25a/su25a.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
  - [TounsiBench: Benchmarking Large Language Models for Tunisian Arabic](https://aclanthology.org/2025.emnlp-main.1756.pdf)
  - [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 5 papers
  > Factuality (Fac): Considering unlearning negates the original knowledge acquired by the model, we evaluate the factuality on TriviaQA [27] with 6-shot, and F1 scores are reported; (Section 3.3.2)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Catastrophic Failure of LLM Unlearning via Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 4 papers
  > Accuracy: The response provided by the large language model is accurate and has no factual errors. (Section 4.2.5, The Instruction of Human Evaluation)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25a/su25a.pdf)
  - [Agent-as-Judge for Factual Summarization of Long Narratives](https://aclanthology.org/2025.emnlp-main.1204.pdf)
  - [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 2 papers
  > We evaluated our decoding strategy on StrategyQA and GSM8K, tasks requiring not just factuality but also Chain-of-Thought (CoT) reasoning (Wei et al., 2022b) ability in order to achieve good performance.
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > "factual QA accuracy (exact match on NaturalQuestions and F1 score on TriviaQA)"
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 2 papers
  > For HelpSteer, we use https://huggingface.co/Haoxiang-Wang/ RewardModel-Mistral-7B-for-DPA-v1 for all attributes of rewards, including helpfulness, correctness, coherence, complexity and verbosity.
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **JudgeBench** (measurement instrument): *measured_by*, 2 papers
  > the focus of JudgeBench is on evaluating the factual and logical correctness of complex responses to challenging questions. (Figure 1)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
  - [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://aclanthology.org/2025.acl-long.775.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > "Further experiments on chain-of-thought reasoning for StrategyQA (Geva et al., 2021) and GSM8K (Cobbe et al., 2021) also show that it can facilitate more factual reasoning."
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We evaluate models on 11 different benchmarks, covering skills such as factuality (MMLU [20]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **FreshQA** (measurement instrument): *measured_by*, 1 paper
  > In recent years a proliferation of benchmarks for evaluating factuality of LLMs has been observed ... They include many established benchmarks such as ... FreshQA... (Section 2)
  - [WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia](https://proceedings.neurips.cc/paper_files/paper/2024/file/c63819755591ea972f8570beffca6b1b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Helpfulness** (construct): *correlates*, 1 paper
  > Conversely, correctness has become a stronger predictor of helpfulness in HelpSteer2 (Pearson’s R=0.9430) than in HelpSteer (Pearson’s R=0.8525).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Context faithfulness** (construct): *causes*, 1 paper
  > current factuality enhancement methods can significantly undermine the context-faithfulness of LLMs. (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Overconfidence** (construct): *causes*, 1 paper
  > factuality enhancement can lead LLMs to become overly confident in their parametric knowledge (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Biography** (measurement instrument): *measured_by*, 1 paper
  > its FactScore on the out-of-domain Biography dataset is also improved from 30.29% to 39.39% (Section 1).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > Does CoS affect factuality? Given that CoS influences content generation, in Appendix C.2 we conduct study on OpenbookQA (Mihaylov et al., 2018) by giving CoS different types of contexts and adjusting the λ. (Sec 4.1)
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Reliability** (construct): *causes*, 1 paper
  > Both aspects [factuality and instruction-following] significantly impact reliability and user experience in real-world applications and are challenging to evaluate effectively with existing reward models (Section 3).
  - [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://aclanthology.org/2025.acl-long.775.pdf)
- **RM-Bench** (measurement instrument): *measured_by*, 1 paper
  > We use RM-Bench (Liu et al., 2024b), JudgeBench (Tan et al., 2024), and a new benchmark IFBENCH as evaluation benchmarks, as both RM-Bench and JudgeBench include response pairs involving factual correctness. (Section 4.1)
  - [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://aclanthology.org/2025.acl-long.775.pdf)
- **Chinese SimpleQA** (measurement instrument): *measured_by*, 1 paper
  > In this work, we present Chinese SimpleQA, the first comprehensive Chinese benchmark to evaluate the factuality ability of LLMs to answer short questions (Abstract).
  - [Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **SimpleQA** (measurement instrument): *measured_by*, 1 paper
  > Recently, SimpleQA (Wei et al., 2024) has been proposed to measure the short-form factuality in LLMs (Section 2).
  - [Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **ASQA** (measurement instrument): *measured_by*, 1 paper
  > In this paper, to evaluate the quantitative performance of methods on ASQA, we follow the official metrics and report: Disambiguous-Rouge (DR) as the overall score, which combines ROUGE-L (R-L) (Lin, 2004) for text quality and Disambig-F1 (Dis-F1; QA accuracy score based on RoBERTa large (Liu et al., 2019)) for factual correctness.
  - [Efficient Real-time Refinement of Language Model Text Generation](https://aclanthology.org/2025.emnlp-main.1753.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > We further report AlpacaEval (Li et al., 2023b) win-rate, the fraction of pairwise comparisons a system wins against the ALL-SFT baseline, providing a human-preference proxy for factual quality. (Section 4.2)
  - [CYCLE-INSTRUCT: Fully Seed-Free Instruction Tuning via Dual Self-Training and Cycle Consistency](https://aclanthology.org/2025.emnlp-main.258.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 1 paper
  > We evaluate factual correctness and spoken question answering abilities of our model on Llama Questions (Nachmani et al., 2024), and a synthesized audio version of TriviaQA (Joshi et al., 2017) and Web Questions (Berant et al., 2013). (Section 5.4)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)

### → Factuality
- **Logical consistency** (construct): *causes*, 2 papers
  > A growing body of research explores improving LLMs’ factuality using the logical consistency across their beliefs (Dalvi et al., 2021; Tafjord et al., 2022; Mitchell et al., 2022; Jung et al., 2022; Hase et al., 2023; Kassner et al., 2023; Akyürek et al., 2024).
  - [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (SELF-RAG) that enhances an LM’s quality and factuality through retrieval and self-reflection. (ABSTRACT)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Parametric knowledge** (construct): *causes*, 1 paper
  > our SLED framework leverages the latent knowledge embedded within the LLM by contrasting the output logits from the final layer with those from early layers. It then utilizes an approximate gradient approach to enable latent knowledge to guide the self-refinement of outputs, thereby effectively improving factual accuracy. (Abstract)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator): *correlates*, 1 paper
  > Our results show a large increase in factual precision of IDK-tuned models while causing only a small decrease in recall of factual knowledge
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
- **Calibration** (construct): *causes*, 1 paper
  > Numerous studies have explored ways to improve factuality at various stages, such as continual pre-training (Chang et al., 2024), uncertainty calibration (Cohen et al., 2024), factuality alignment (Tian et al., 2024), and contrastive decoding (Section 2).
  - [Alleviating Hallucinations from Knowledge Misalignment in Large Language Models via Selective Abstention Learning](https://aclanthology.org/2025.acl-long.1199.pdf)
- **Multimodal alignment** (construct): *causes*, 1 paper
  > However, Medical LVLMs (Med-LVLMs) encounter factuality issues due to modality misalignment, where the models prioritize textual knowledge over visual input, causing hallucinations that conflict with medical images. (Abstract)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
- **Coherence** (construct): *causes*, 1 paper
  > Improved coherence in turn leads to improved accuracy on factual tasks. (Section 1)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > Existing alignment or post-training strategies usually decrease the factuality of language models (Section 1).
  - [Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **Memorization** (construct): *causes*, 1 paper
  > Being able to memorize the facts in the training corpus enables the model to answer fact-seeking, knowledge intensive tasks more factually and accurately.
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)

### Associated with
- **Constraint satisfaction** (construct), 2 papers
  > The framework has been recently proposed for studying and detecting factual errors of LLMs by Yuksekgonul et al. (2023) as a useful perspective which also connects information popularity and constraint feasibility to the LLM’s ability to satisfy such constraints. (Section 1)
  - [KITAB: Evaluating LLMs on Constraint Satisfaction for Information Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/82846e19e6d42ebfd4ace4361def29ae-Paper-Conference.pdf)
  - [Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/880ee6e23b6ee548ebcccafe0ef0f513-Paper-Conference.pdf)
- **World knowledge** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: ... Background Knowledge (Factuality, Commonsense Understanding)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Text generation quality** (construct), 1 paper
  > The complexity arises from the inherent subjectivity of “quality” in text generation, which often depends on multiple factors such as relevance, coherence, factual accuracy, and fluency.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > The experimental results in previous sections indicate that after factuality alignment with questions from a group of topics, the LLM will become more factually correct when answering questions from another group of topics (Section 4.2).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Faithfulness** (construct), 1 paper
  > Factuality refers to whether the model’s generated information aligns with external, real-world knowledge and is typically evaluated against a reference dataset or established knowledge. Faithfulness, on the other hand, evaluates how accurately the generated content reflects the information provided in the input context. (Section 1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Instruction following ability** (construct), 1 paper
  > Specifically, we define three fundamental dimensions of instruction-following: relevance, factuality, and adherence. (Abstract)
  - [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > We define L(∅, ·) = 0, which indicates that we do not penalize the model for abstaining from responding when it is uncertain, as here we only focus on the assurance of factuality while neglecting other aspects of reliability such as omission of information. (Section 3.1)
  - [Towards Statistical Factuality Guarantee for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.576.pdf)
- **Trustworthiness** (construct), 1 paper
  > “The evaluation of trustfulness includes assessments of factuality and uncertainty.”
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Radiology report generation** (behavioral indicator), 1 paper
  > Factual correctness is especially critical in chest radiology domains, as minute textual differences can drastically invert radiology report meaning and downstream prescribed treatments
  - [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf)
- **Factual question answering** (behavioral indicator), 1 paper
  > memory layers improve the factual accuracy of language models by over 100% as measured by factual QA benchmarks (Section 1).
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
- **CLAIR** (measurement instrument), 1 paper
  > The substantial improvement in factuality, compared to the relatively minor coverage loss in the captioning models, is also reflected in the increased CLAIR scores. (Section 4.3)
  - [Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25aj/lee25aj.pdf)
