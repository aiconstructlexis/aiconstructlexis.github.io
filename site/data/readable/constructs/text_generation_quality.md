# Text generation quality
**Type:** Construct  
**Supporting papers:** 115  
**Also known as:** Generation quality, Content quality, Text Quality, Generative quality, Generator quality, Generative performance, Output effectiveness, Generative model quality, Conversation quality, Composition, Generation capacity, Overall quality, Professional response quality, Hypothesis quality, Storyline quality, Information quality, Overall satisfaction, Output quality, Response quality, Answer quality, Conversational quality, Sample quality, Text quality  

## State of the Field

**Space of definitions.** Across the literature, the dominant framing is a broad, holistic notion of the quality of generated text or responses. Most definitions describe it through combinations of coherence, fluency, relevance, usefulness, correctness or accuracy, and sometimes diversity, factuality, or human preference. A smaller line of work treats it as a latent ability or capacity of the model or generator to produce high-quality outputs, and some papers narrow it to specific domains such as surveys, conversations, narratives, hypotheses, audio, CAD, songs, or synthetic data. The main variation is between output-level judgments and model-level capacity, and between generic quality and domain-specific versions.

**Space of facets.** Rather than treating it as a single primitive score, papers usually unpack it into subcriteria or aggregates over subcriteria. Recurrent facets include fluency, coherence, relevance, informativeness or usefulness, correctness, and diversity; some task-specific formulations add coverage, structure, faithfulness, hallucination, harmlessness, or overall satisfaction, and some explicitly define overall quality as an aggregate over earlier criteria. The label itself is not standardized: closely related names include generation quality, response quality, text quality, output quality, overall quality, and sample quality, while some papers contrast quality with alignment, controllability, efficiency, latency, throughput, or cost.

**Space of measurement.** Papers operationalize the construct with 16 measurement instruments, and it is also linked to 6 behavioral indicators. The most frequently linked instruments are LLM-as-a-judge, MT-Bench, AlpacaEval, ArmoRM, and Human evaluation, within a broader set of benchmark-based evaluations, model-based judges or reward models, and direct human ratings. In practice, papers turn quality into overall judgments, pairwise win rates, comparative rankings, reward scores, or human ratings of facets such as fluency and coherence, but some operationalizations are narrower proxies, including correctness on labeled benchmarks, task metrics such as BLEU or ROUGE, and perplexity-based comparisons, so the measurements range from holistic judgments to task-specific proxy metrics.

**Links.** Beyond measurement, papers connect the construct to 11 constructs and 6 behavioral indicators. Several papers claim a causal relationship from iterative refinement, reward hacking, and context utilization to text generation quality: the quoted evidence describes refinement and dynamic context use as yielding better or more robust outputs, while reward hacking is described as reducing sentence quality. Papers also report that text generation quality is related to generation diversity and collaboration ability, and the remaining linked constructs and behaviors appear in additional related links and causal claims.

## Sources

**Generation quality** (10 papers: [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/090b23d52bc2722eef2fbf79c5ebf9ec-Paper-Conference.pdf), [Amphista: Bi-directional Multi-head Decoding for Accelerating LLM Inference](https://aclanthology.org/2025.naacl-long.450.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf), [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf), [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf), [On the Learnability of Watermarks for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a86d17b6cd70366d56ab48d2a05a4df1-Paper-Conference.pdf), [Provable Robust Watermarking for AI-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/beae9ed5316bcc48e616754c06c11875-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf))
> The overall quality of a model's generated text, often encompassing aspects like coherence, diversity, and fluency, independent of its alignment to specific objectives.

**Content quality** (3 papers: [AutoSurvey: Large Language Models Can Automatically Write Surveys](https://proceedings.neurips.cc/paper_files/paper/2024/file/d07a9fc7da2e2ec0574c38d5f504d105-Paper-Conference.pdf), [SurveyGen: Quality-Aware Scientific Survey Generation with Large Language Models](https://aclanthology.org/2025.emnlp-main.136.pdf), [SURVEYFORGE : On the Outline Heuristics, Memory-Driven Generation, and Multi-dimensional Evaluation for Automated Survey Writing](https://aclanthology.org/2025.acl-long.609.pdf))
> The overall quality of a generated survey in terms of how comprehensively, coherently, and topically it is written.

**Quality** (2 papers: [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf), [Can Large Language Models Outperform Non-Experts in Poetry Evaluation? A Comparative Study Using the Consensual Assessment Technique](https://aclanthology.org/2025.emnlp-main.1625.pdf))
> The overall goodness of a generated response, assessed through criteria like relevance, accuracy, and insightfulness.

**Text Quality** (1 paper: [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf))
> The degree to which generated text is coherent, grammatical, and practically useful.

**Response quality** (13 papers: [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf), [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf), [Add-One-In: Incremental Sample Selection for Large Language Models via a Choice-Based Greedy Paradigm](https://aclanthology.org/2025.emnlp-main.270.pdf), [Evaluating Language Models as Synthetic Data Generators](https://aclanthology.org/2025.acl-long.320.pdf), [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf), [Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/48a4f41ff000b121eabe7b2491b24aef-Paper-Conference.pdf), [Unmasking Implicit Bias: Evaluating Persona-Prompted LLM Responses in Power-Disparate Social Scenarios](https://aclanthology.org/2025.naacl-long.50.pdf), [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf), [PAPILLON: Privacy Preservation from Internet-based and Local Language Model Ensembles](https://aclanthology.org/2025.naacl-long.173.pdf), [AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.508.pdf), [MixLLM: Dynamic Routing in Mixed Large Language Models](https://aclanthology.org/2025.naacl-long.545.pdf), [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf))
> The overall quality of a model's generated response, encompassing aspects like linguistic correctness, usefulness, and relevance.

**Generative quality** (2 papers: [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf), [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf))
> The overall quality and accuracy of the model's generated output, particularly when comparing a compressed version to its non-quantized original.

**Generator quality** (1 paper: [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf))
> The latent ability of a model to produce high-quality synthesized outputs that can be useful if properly selected.

**Generative performance** (3 papers: [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf), [Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons](https://aclanthology.org/2025.emnlp-main.360.pdf), [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf))
> The overall quality and accuracy of the text generated by the model across various tasks, which sparse attention methods aim to preserve.

**Output effectiveness** (1 paper: [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf))
> The general quality of a model's generated sequences, considered as a property distinct from the efficiency of the generation process.

**Output quality** (3 papers: [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf), [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf), [Unveiling Environmental Impacts of Large Language Model Serving: A Functional Unit View](https://aclanthology.org/2025.acl-long.519.pdf))
> A general latent trait representing the overall quality of a model's generated text, assessed across dimensions like relevance, accuracy, and coherence.

**Generative model quality** (1 paper: [Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf))
> The degree to which a generative model can produce high-fidelity synthetic data that accurately reflects the statistics of real data, influencing the performance of models trained on that data.

**Text quality** (6 papers: [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf), [Conditional [MASK] Discrete Diffusion Language Model](https://aclanthology.org/2025.emnlp-main.450.pdf), [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [Language Model Detectors Are Easily Optimized Against](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f9f07df0992ce21698d800eaa891bd8-Paper-Conference.pdf), [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf), [A Tale of Two Structures: Do LLMs Capture the Fractal Complexity of Language?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alabdulmohsin25a/alabdulmohsin25a.pdf))
> The overall quality of generated text, encompassing aspects like coherence, fluency, and correctness.

**Conversation quality** (1 paper: [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf))
> The overall value of a multi-turn conversation, which is inferred from cumulative rewards based on metrics such as user engagement and safety.

**Composition** (3 papers: [Beyond Outlining: Heterogeneous Recursive Planning for Adaptive Long-form Writing with Language Models](https://aclanthology.org/2025.emnlp-main.1254.pdf), [SongCreator: Lyrics-based Universal Song Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/92a7a03e1c716970848a4a86cc8243ee-Paper-Conference.pdf), [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.87.pdf))
> The latent ability to generate coherent and structured text that meets specified stylistic, length, and organizational requirements.

**Generation capacity** (1 paper: [Language Model Based Text-to-Audio Generation: Anti-Causally Aligned Collaborative Residual Transformers](https://aclanthology.org/2025.emnlp-main.1322.pdf))
> The model's ability to effectively generate complex and high-fidelity outputs, particularly when dealing with a large number of predictive targets like deep RVQ layers.

**Overall quality** (2 papers: [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://aclanthology.org/2025.emnlp-main.138.pdf), [Towards Better Evaluation for Generated Patent Claims](https://aclanthology.org/2025.acl-long.190.pdf))
> A holistic judgment of a candidate output that summarizes multiple aspects into a single general assessment.

**Hypothesis quality** (1 paper: [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf))
> The latent trait reflecting how effectively a generated hypothesis captures meaningful patterns, supports downstream classification, and provides helpful or novel insights.

**Storyline quality** (1 paper: [CogDual: Enhancing Dual Cognition of LLMs via Reinforcement Learning with Implicit Rule-Based Rewards](https://aclanthology.org/2025.emnlp-main.1389.pdf))
> The overall coherence and fluency of the generated narrative, including logical flow and narrative development.

**Information quality** (1 paper: [Certified Mitigation of Worst-Case LLM Copyright Infringement](https://aclanthology.org/2025.emnlp-main.1784.pdf))
> The degree to which a model's output is relevant, faithful to source information, and free from fabrications.

**Overall satisfaction** (1 paper: [Orchestrating Audio: Multi-Agent Framework for Long-Video Audio Synthesis](https://aclanthology.org/2025.emnlp-main.1133.pdf))
> A human-perceived, holistic judgment of the quality and appropriateness of the generated audio for a given video.

**Answer quality** (1 paper: [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/03d7e13f0092405804f3a381ade8f3f0-Paper-Conference.pdf))
> The overall goodness of a model's generated response, assessed across multiple dimensions like helpfulness, correctness, and clarity.

**Conversational quality** (1 paper: [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf))
> The degree to which model responses are fluent, informative, and preferred in dialogue settings, reflecting coherence, completeness, and naturalness.

**Sample quality** (2 papers: [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf), [Optimizing Temperature for Language Models with Multi-Sample Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25f/du25f.pdf))
> The overall quality of generated text as judged by coherence and related generation properties.

**Text generation quality** (2 papers: [Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf))
> The latent ability of a language model to produce text that is coherent, fluent, and preferred by humans over alternatives, reflecting overall textual excellence beyond simple metric optimization.

## Relationships

### Text generation quality →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 7 papers
  > These newly designed criteria leverage human judges or GPT-4 to better evaluate response quality. (Section 3.1)
  - [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf)
  - [Improving Instruction-Following in Language Models through Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf)
  - [Evaluating Language Models as Synthetic Data Generators](https://aclanthology.org/2025.acl-long.320.pdf)
  - [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 7 papers
  > Additionally, we evaluated the output quality of the LLM using MT-bench (Zheng et al., 2024) with its provided dataset.
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/294fd30f8cbb89ce328d5a01fef47fb4-Paper-Conference.pdf)
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
  - [Amphista: Bi-directional Multi-head Decoding for Accelerating LLM Inference](https://aclanthology.org/2025.naacl-long.450.pdf)
  - [Speculative Streaming: Efficient and Scalable Speculative Decoding with Multi-Stream Attention](https://aclanthology.org/2025.emnlp-main.986.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 4 papers
  > The AlpacaEval dataset released by Dubois et al. (2023) is used to evaluate the overall quality of generations. (Section 3.3)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [Learning to Keep a Promise: Scaling Language Model Decoding Parallelism with Learned Asynchronous Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25a/jin25a.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > "we randomly sample 100 cases and evaluate the results ... from four perspectives: fluency, coherence, informativeness, and grammar"
  - [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf)
  - [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf)
- **ArmoRM** (measurement instrument): *measured_by*, 2 papers
  > we assess response quality using reward models... we employ three state-of-the-art reward models from RewardBench (Lambert et al., 2024): ArmoRM-Llama3-8B-v0.1 (Wang et al., 2024a), Skywork-Reward-Llama-3.1-8B (Liu and Zeng, 2024), and Skywork-Reward-Gemma-2-27B (Liu and Zeng, 2024). (Section 4.2)
  - [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf)
  - [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > For performance, we calculate the average response quality: ... where s(MRα(q)) represents an individual response quality score, such as correctness on golden-labeled datasets (e.g., MMLU) (Section 3.2)
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **FLASK** (measurement instrument): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > Table 1: Response quality evaluation on BoolQ and AlpacaEval.
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **WikiText-2** (measurement instrument): *measured_by*, 1 paper
  > “For the base model, we evaluate the quality of text generation using the WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994), and C4 (Raffel et al., 2020) datasets.”
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Human preference evaluation** (measurement instrument): *measured_by*, 1 paper
  > "We also conduct human evaluation on the general quality of the model responses on the combined test set described in Section 3.1"
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > To validate that MTJD indeed betters output quality, we test MTJD (k=4) and standard multinomial sampling on Spider, MTBench, and HumanEval using the Llama-3 series models. ... For this process, the higher the scores, the better the downstream performance. (Section 5.1)
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
- **WMT** (measurement instrument): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT"
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **CNN/DailyMail** (measurement instrument): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT and ROUGE-2 for XSum and CNNDM."
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **XSum** (measurement instrument): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT and ROUGE-2 for XSum and CNNDM."
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)

### → Text generation quality
- **Iterative refinement** (behavioral indicator): *causes*, 2 papers
  > "This iterative refinement process continues for several cycles until obtaining a more robust and comprehensive response."
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Reward hacking** (behavioral indicator): *causes*, 2 papers
  > This decline occurs because a large number of iterations at test time can lead to reward hacking, reducing the quality of the generated sentences. (Section 6.4)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)
- **Token diversity** (construct): *causes*, 1 paper
  > However, when we check the generated content, we discover that the quality is compromised by low token diversity
  - [Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e3b203e72c4e058de26d02a92a81844-Paper-Conference.pdf)
- **Context utilization** (construct): *causes*, 1 paper
  > Radar utilizes context tokens dynamically in a principled manner, resulting in significantly higher generation quality
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
- **Response aggregation** (behavioral indicator): *causes*, 1 paper
  > "Aggregators are models proficient in synthesizing responses from other models into a single, high-quality output."
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Self-evaluation** (behavioral indicator): *causes*, 1 paper
  > This result suggests that evaluation can potentially improve the quality of the generated text, which serves as a stepping stone for building RLC method. (Section 4.3)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)

### Associated with
- **Text generation** (behavioral indicator), 2 papers
  > "we also demonstrate improved generation quality in open-ended text generation"
  - [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Generation diversity** (construct), 2 papers
  > Decoding-based approaches offer greater adaptability but face a fundamental diversity–quality trade-off. (Section 1)
  - [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
- **Language modeling ability** (construct), 1 paper
  > While we believe that perplexity measurements and generation quality are strongly related, this is a hypothesis we aim to investigate in future work. (Section 6)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > the generation quality of GPT4 decreases as the logical constraints become more complex, while the generation quality of Ctrl-G stays relatively consistent across all settings, demonstrating strong generalization performance. (Sec 5.2)
  - [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf)
- **Reward overoptimization** (construct), 1 paper
  > The coherence and diversity metrics drop to nearly zero, which is evidence of reward overoptimization. (Section 6.3)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
- **Factuality** (construct), 1 paper
  > The complexity arises from the inherent subjectivity of “quality” in text generation, which often depends on multiple factors such as relevance, coherence, factual accuracy, and fluency.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Safety** (construct), 1 paper
  > In such applications, the quality (e.g., user engagement, safety) of a conversation is important and can only be exactly known at the end of the conversation. (ABSTRACT)
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > achieving an optimal trade-off between instruction adherence and output quality. (Section 1)
  - [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf)
- **Readability** (construct), 1 paper
  > Text quality is measured by absolute perplexity difference (|∆PPL|), Flesch reading ease score (Flesch), and semantic similarity (Sim) between the attacked and original text. Lower detection accuracy (↓) indicates better evasion, while higher Flesch and Sim scores (↑) reflect better readability and semantic preservation.
  - [TempParaphraser: “Heating Up” Text to Evade AI-Text Detection through Paraphrasing](https://aclanthology.org/2025.emnlp-main.1607.pdf)
- **Semantic preservation** (construct), 1 paper
  > Text quality is measured by absolute perplexity difference (|∆PPL|), Flesch reading ease score (Flesch), and semantic similarity (Sim) between the attacked and original text. Lower detection accuracy (↓) indicates better evasion, while higher Flesch and Sim scores (↑) reflect better readability and semantic preservation.
  - [TempParaphraser: “Heating Up” Text to Evade AI-Text Detection through Paraphrasing](https://aclanthology.org/2025.emnlp-main.1607.pdf)
- **Collaboration ability** (construct), 1 paper
  > "we identify an inherent phenomenon we term the collaborativeness of LLMs — wherein an LLM tends to generate better responses when presented with outputs from other models"
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
