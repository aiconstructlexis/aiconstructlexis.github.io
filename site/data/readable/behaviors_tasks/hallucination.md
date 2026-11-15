# Hallucination
**Type:** Behavioral indicator  
**Supporting papers:** 646  
**Also known as:** Hallucinated response generation, Factuality hallucination, Hallucinated tool calling, Soliloquizing, Hallucinatory success, Hallucinated content generation, Confusion, Generating false preambles, Non-factual response generation, Hallucinated reasoning, Hallucinated geometry, Hallucinated citations, Cross-modal hallucination, Factual inconsistency, Hallucinated generation, Knowledge hallucination  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats hallucination as output that is factually incorrect, fabricated, nonsensical, or otherwise ungrounded in the provided input, source text, image, video, table, tool set, or established world knowledge. Many definitions also include content that is merely unsupported or irrelevant, and some stress that the output may still sound plausible or confident. A smaller line of work gives task-specific criteria, for example any ungrounded span in a response, answers to unanswerable questions, contradictions with a source document, or fabricated numbers, tools, citations, code assets, or observations.

**Variants.** Variants are most common in multimodal settings, where papers study visual or cross-modal hallucination as object, action, attribute, relation, counting, or spatial errors, such as mentioning entities absent from an image or video or hearing imaginary sounds from visual cues. Text-centered work often treats it as factual inconsistency or grounding error in summarization, question answering, simplification, translation, table or graph generation, and reference generation. More specialized variants include hallucinated reasoning and tool hallucination.

**Space of elicitation and scores.** Papers link hallucination to 28 measurement instruments. The most common are POPE, CHAIR, MMHal-Bench, LLM-as-a-judge, and AMBER, with 23 other instruments used less often. These instruments are mostly multimodal hallucination evaluations: POPE uses yes or no questions about object presence, CHAIR compares mentioned objects in captions with reference captions, MMHal-Bench uses GPT-4 to score response quality and hallucination across several question types, judge-based setups have a large model classify or score hallucinated responses, and AMBER extends object checks to attributes and relations.

**What it is taken as evidence of.** Across 40 linked constructs, papers do not converge on a single construct that hallucination reflects. The most frequent links are to factuality, faithfulness, multimodal alignment, trustworthiness, and reliability, with 35 other constructs linked less often. In the recorded relationships, papers claim a causal relationship from factuality and from multimodal alignment to hallucination, report hallucination to correlate with faithfulness, and claim causal links from hallucination to trustworthiness and reliability.

## Sources

**Hallucination** (61 papers: [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf), [GAPO: Learning Preferential Prompt through Generative Adversarial Policy Optimization](https://aclanthology.org/2025.acl-long.13.pdf), [Continuously Updating Digital Twins using Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/amad25a/amad25a.pdf), [JUDGEBERT: Assessing Legal Meaning Preservation Between Sentences](https://aclanthology.org/2025.emnlp-main.5.pdf), [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Can LLM-Generated Misinformation Be Detected?](https://proceedings.iclr.cc/paper_files/paper/2024/file/94bbcb744bbada8808fda05b9d9290d6-Paper-Conference.pdf), [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf), [Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Paper-Conference.pdf), [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf), [Guiding Instruction-based Image Editing via Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf), [In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf), [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf), [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf), [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf), [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [Anticipating Future with Large Language Model for Simultaneous Machine Translation](https://aclanthology.org/2025.naacl-long.286.pdf), [Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.481.pdf), [ConQRet: A New Benchmark for Fine-Grained Automatic Evaluation of Retrieval Augmented Computational Argumentation](https://aclanthology.org/2025.naacl-long.293.pdf), [DTELS: Towards Dynamic Granularity of Timeline Summarization](https://aclanthology.org/2025.naacl-long.136.pdf), [Decoding Hate: Exploring Language Models' Reactions to Hate Speech](https://aclanthology.org/2025.naacl-long.45.pdf), [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf), [Ethical Concern Identification in NLP: A Corpus of ACL Anthology Ethics Statements](https://aclanthology.org/2025.naacl-long.580.pdf), [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf), [FiNE: Filtering and Improving Noisy Data Elaborately with Large Language Models](https://aclanthology.org/2025.naacl-long.437.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf), [Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval](https://aclanthology.org/2025.naacl-long.216.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf), [Leveraging LLM For Synchronizing Information Across Multilingual Tables](https://aclanthology.org/2025.naacl-long.329.pdf), [Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness](https://aclanthology.org/2025.naacl-long.408.pdf), [Style Transfer with Multi-iteration Preference Optimization](https://aclanthology.org/2025.naacl-long.135.pdf), [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.152.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf), [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf), [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf))
> The observable act of a model generating factually incorrect or nonsensical information that is not grounded in its input or training data.

**Misinformation generation** (1 paper: [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf))
> Producing incorrect factual content as an observable failure mode linked to model collapse.

**Hallucinated response generation** (5 papers: [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf), [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf), [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf), [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf), [X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf))
> The observable behavior of a model producing a factually incorrect or speculative response to a question, particularly when the question's premise is not supported by the video content.

**Factuality hallucination** (1 paper: [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf))
> The specific observable behavior where a model's generated output diverges from established real-world facts.

**Hallucinated tool calling** (1 paper: [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf))
> The observable generation of invalid tool calls, including fabricated tools, incorrect parameters, or redundant invocations not grounded in the user input or task requirements.

**Soliloquizing** (1 paper: [EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramovich25a/abramovich25a.pdf))
> An observable phenomenon where a language model self-generates a complete thought-action-observation loop, including a hallucinated observation, in a single response without interacting with the environment.

**Hallucinatory success** (1 paper: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf))
> Incorrectly concluding that a task has been completed when key steps remain unexecuted, often due to weak contextual memory.

**Hallucinated content generation** (1 paper: [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf))
> The observable behavior of generating factually incorrect or counterfactual statements, often as the target of a truthfulness steering intervention.

**Confusion** (1 paper: [JUDGEBERT: Assessing Legal Meaning Preservation Between Sentences](https://aclanthology.org/2025.emnlp-main.5.pdf))
> The introduction of factual errors in the simplified text that contradict the original, such as reversing the direction of a requirement (e.g., claiming the opposite of what the source states).

**Generating false preambles** (1 paper: [Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions](https://aclanthology.org/2025.emnlp-main.90.pdf))
> An observable error where the model generates non-existent or invalid preambles, such as library imports, for a formal code block.

**Non-factual response generation** (1 paper: [FacLens: Transferable Probe for Foreseeing Non-Factuality in Fact-Seeking Question Answering of Large Language Models](https://aclanthology.org/2025.emnlp-main.937.pdf))
> The observable behavior in which an LLM produces an answer to a fact-seeking question that fails to convey the correct, verifiable fact.

**Hallucinated reasoning** (2 papers: [Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1544.pdf), [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf))
> Producing reasoning steps that are not supported by the input evidence, involving fabricated or incorrect justifications for outputs.

**Hallucinated geometry** (1 paper: [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://aclanthology.org/2025.emnlp-main.816.pdf))
> Generating confident but unfounded claims about object size, position, or visibility that are inconsistent with the actual scene structure.

**Hallucinated citations** (1 paper: [NitiBench: Benchmarking LLM Frameworks on Thai Legal Question Answering Capabilities](https://aclanthology.org/2025.emnlp-main.1739.pdf))
> An observable error where a model cites legal sections that are irrelevant or non-existent in its generated answer.

**Cross-modal hallucination** (1 paper: [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc685788a311fa35d8d41df93e288ca-Paper-Conference.pdf))
> A phenomenon where a model generates outputs based on cross-interactions between modalities that are not present in the input signals, such as hearing imaginary sounds from visual cues or seeing fake events from audio cues.

**Factual inconsistency** (1 paper: [Discourse-Driven Evaluation: Unveiling Factual Inconsistency in Long Document Summarization](https://aclanthology.org/2025.naacl-long.103.pdf))
> The phenomenon where a model-generated summary contains information that contradicts or is unsupported by the source document or established world knowledge.

**Hallucinated generation** (1 paper: [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf))
> The observable output of a model producing factually incorrect or nonsensical text.

**Knowledge hallucination** (2 papers: [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf))
> The phenomenon of a model generating plausible but factually incorrect or non-existent knowledge.

## Relationships

### Hallucination →
- **POPE** (measurement instrument): *measured_by*, 19 papers
  > Similar results are seen in other tasks, like the hallucination question "Is there a car in the image?" from POPE.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [Unveiling Encoder-Free Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e2217482fa75556f1970be809acd3f8-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
  - [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf)
  - [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf)
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 10 papers
  > “The CHAIR metric ... evaluates the exact match between generated and ground-truth image captions”
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
  - [Probing Visual Language Priors in VLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25b/luo25b.pdf)
  - [Visual Attention Never Fades: Selective Progressive Attention ReCalibration for Detailed Image Captioning in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jung25c/jung25c.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 9 papers
  > MMHal-Bench is designed to quantify hallucinations with the assistance of GPT-4 [43]. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 7 papers
  > To measure hallucination on the realistic tasks, we use GPT-4 as an evaluator (OpenAI, 2023), following Yue et al. (2023); Gao et al. (2023a). (Section 3.2)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Robust Multimodal Large Language Models Against Modality Conflict](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25dq/zhang25dq.pdf)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)
  - [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
  - [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 6 papers
  > Building upon previous studies [62, 22], we utilized the TrustfulQA benchmark [26] for evaluating the tendency of models to produce hallucinations (Section 5.2)
  - [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [Tokenized Bandit for LLM Decoding and Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25h/shin25h.pdf)
  - [Eliciting Language Model Behaviors with Investigator Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25i/li25i.pdf)
  - [Adaptively profiling models with task elicitation](https://aclanthology.org/2025.emnlp-main.1270.pdf)
- **AMBER** (measurement instrument): *measured_by*, 6 papers
  > AMBER (Wang et al., 2023a) was designed to be evaluated without LLM assistance. ... Metrics: ... (c) Response-level hallucination (Hal); (d) Human cognition hallucination (Cog). (Sec. 5.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
  - [RICO: Improving Accuracy and Completeness in Image Recaptioning via Visual Reconstruction](https://aclanthology.org/2025.emnlp-main.1105.pdf)
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
- **Trustworthiness** (construct): *causes*, 6 papers
  > hallucinations — non-factual or non-sensical information generated by the model — have become challenging barriers to trustworthy and reliable artificial intelligence
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
  - [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf)
  - [WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia](https://proceedings.neurips.cc/paper_files/paper/2024/file/c63819755591ea972f8570beffca6b1b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf)
  - [Where Confabulation Lives: Latent Feature Discovery in LLMs](https://aclanthology.org/2025.emnlp-main.1515.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Reliability** (construct): *causes*, 5 papers
  > Long CoT suffers from high cost for training and exhibits low reliability due to table content hallucinations. (Abstract)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
  - [DecoupleSearch: Decouple Planning and Search via Hierarchical Reward Modeling](https://aclanthology.org/2025.emnlp-main.222.pdf)
  - [MusKGC: A Flexible Multi-source Knowledge Enhancement Framework for Open-World Knowledge Graph Completion](https://aclanthology.org/2025.emnlp-main.508.pdf)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f14fb9acd243c13c95d4a490d1684ce-Paper-Conference.pdf)
- **HaluEval** (measurement instrument): *measured_by*, 4 papers
  > We further verify this hypothesis by measuring the capabilities coefficient on a generative benchmark (TruthfulQA Generation [45]) and a discriminative benchmark (HaluEval [43]). (Appendix A.5)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.276.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **HallusionBench** (measurement instrument): *measured_by*, 4 papers
  > HallusionBench (Guan et al., 2024) evaluates visual illusions and knowledge hallucinations, featuring 346 images and 1129 questions. (Sec. 5.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
- **Truthfulness** (construct): *causes*, 4 papers
  > LLMs are prone to hallucinations [53] and misunderstandings of text, especially in specific technical domains, that can lead to a lack of truthfulness from the model [35].
  - [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://proceedings.neurips.cc/paper_files/paper/2024/file/5acd3c628aa1819fbf07c39ef73e7285-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **MME** (measurement instrument): *measured_by*, 3 papers
  > To evaluate HIO’s capability on object-level and attribute-level hallucination, we compare it with several state-of-the-art Decoding methods on MME. (Section 6.2).
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
- **Uncertainty** (construct): *correlates*, 3 papers
  > we go beyond merely understanding knowledge refusal, and find SAE latents, seemingly representing uncertainty, that are predictive of incorrect answers.
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **SelfCheckGPT** (measurement instrument): *measured_by*, 2 papers
  > and also evaluate its ability to correct Hallucination in SelfCheckGPT [48]. (Section 3.1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf)
- **Object HalBench** (measurement instrument): *measured_by*, 1 paper
  > “On the Object HalBench dataset, CHiP outperforms DPO in hallucination reduction”
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To address this, we extend human evaluation guidelines from Clark et al. (2023), assessing repetition, fluency, coherence, compatibility (ROCStories/DialogSum), and hallucination (DeliData): (Section 4.2)
  - [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf)
- **GAVIE** (measurement instrument): *measured_by*, 1 paper
  > To efficiently measure the hallucination generated by LMMs, we propose GPT4-Assisted Visual Instruction Evaluation (GAVIE), a stable approach to evaluate visual instruction tuning like human experts. (ABSTRACT)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 1 paper
  > Our experiments require a source of hallucinations to edit, which we draw from the Multi-CounterFact (MCF) [26] and ZsRE [27] datasets. (Section 5)
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
- **MMLongBench-Doc** (measurement instrument): *measured_by*, 1 paper
  > These three types of questions evaluate the LVLMs’s long-context DU capabilities from complementary aspects: the localization ability, the cross-page comprehension ability, and the hallucination severity, respectively. (Section 3.4)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > we further introduce three additional L-2 capabilities specific to MMBench-Video: Hallucination, Commonsense Reasoning, and Temporal Reasoning.
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BFCL** (measurement instrument): *measured_by*, 1 paper
  > Accuracy performance comparison on BFCL-v3 leaderboard (updated on 09/20/2024). ... Hallucination (Table 2)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **APIBench** (measurement instrument): *measured_by*, 1 paper
  > We also evaluate APIBench in Halluation Rate. (Section 4.1)
  - [Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf)
- **LLMEval** (measurement instrument): *measured_by*, 1 paper
  > Then, for each example, we can rate it as “correct” or “abstain” or “hallucinate” depending on the LLMEval output. (Section 4.2)
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
- **Geometric reasoning** (construct): *causes*, 1 paper
  > State-of-the-art MLLMs suffer severe hallucination on geometric figures, which greatly hinders their abilities on solving geometric problems. (Figure 1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **Representational stability** (construct): *correlates*, 1 paper
  > We comprehensively present and analyze the correlation between vision feature stability and model hallucinations in Section 3. (Section 1).
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
- **BLINK** (measurement instrument): *measured_by*, 1 paper
  > Some efforts include POPE (Li et al., 2023g), LLaVA-RLHF (Sun et al., 2023), BLINK (Fu et al., 2024), and Rohrbach et al. (2018); Biten et al. (2022) are the few examples that consider multimodal hallucination. (Section 5.1)
  - [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf)
- **Fact checking** (behavioral indicator): *causes*, 1 paper
  > the LLM world knowledge conversion produces hallucinatory evidence, directly impacting claim validation (Section 4.7)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
- **CAA** (measurement instrument): *measured_by*, 1 paper
  > Seven concepts, relevant to the helpful, honest, and harmless of LLMs, are included from CAA dataset (Rimsky et al., 2024): AI Coordination (AIC., for short), Corrigibility (CORR.), Hallucination (HALLU.), Myopic Reward (MR.), Survival Instinct (SI.), Sycophancy (SYC.), and Refusal (REF.).
  - [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf)
- **LongFact** (measurement instrument): *measured_by*, 1 paper
  > hallucination on LongFact (Figure 1).
  - [Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://aclanthology.org/2025.acl-long.804.pdf)
- **FActScore** (measurement instrument): *measured_by*, 1 paper
  > it enables direct measurement of hallucination using metrics such as FActScore (Min et al., 2023) and SAFE (Wei et al., 2024) (Section 1)
  - [Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study Over Open-ended Question Answering](https://aclanthology.org/2025.acl-long.622.pdf)
- **SAFE** (measurement instrument): *measured_by*, 1 paper
  > it enables direct measurement of hallucination using metrics such as FActScore (Min et al., 2023) and SAFE (Wei et al., 2024) (Section 1)
  - [Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study Over Open-ended Question Answering](https://aclanthology.org/2025.acl-long.622.pdf)
- **FaithEval** (measurement instrument): *measured_by*, 1 paper
  > As shown in Table 5, the ablation study on FaithEval (Ming et al., 2024) demonstrates that OpAmp not only enhances robustness to noisy contexts but also reduces hallucinations as a valuable secondary benefit.
  - [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf)
- **Verbalized confidence** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, we replace the hallucination detection module in DSSP-RAG with two existing methods: Trained Probes, Verbalization and Hybrid Consistency (Hyb-Cons). (Section 4.3.3)
  - [Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://aclanthology.org/2025.emnlp-main.549.pdf)
- **Expert evaluation** (measurement instrument): *measured_by*, 1 paper
  > Due to incomplete text annotations on the MMHal, GPT-4 couldn't reliably detect hallucinations. To make the results more reliable, we invited experts to manually annotate the data
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Planning** (construct): *causes*, 1 paper
  > LLMs often experience hallucinations (Huang et al., 2023), which present two major challenges in planning. First, they might struggle to assess if a plan is achievable given a specific problem description (Aghzal et al., 2023; Kambhampati, 2024). (Section 10)
  - [PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://aclanthology.org/2025.acl-long.958.pdf)
- **Reasoning faithfulness** (construct): *causes*, 1 paper
  > LLMs still struggle with conducting faithful reasoning due to issues of lack of knowledge and hallucination (Section 1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)

### → Hallucination
- **Factuality** (construct): *causes*, 24 papers
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
- **Faithfulness** (construct): *correlates*, 9 papers
  > Informative Context Improves Faithfulness and Reduces Hallucination.
  - [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [No Free Lunch: Fundamental Limits of Learning Non-Hallucinating Generative Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2a11632520f4b7473d7838f074a7d25-Paper-Conference.pdf)
  - [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf)
  - [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [SARA: Salience-Aware Reinforced Adaptive Decoding for Large Language Models in Abstractive Summarization](https://aclanthology.org/2025.acl-long.1236.pdf)
- **Multimodal alignment** (construct): *causes*, 6 papers
  > Misalignment between modalities can lead to safety risks such as biased or inappropriate content generation (Gong et al., 2023; Tu et al., 2023) and hallucinations, where outputs are not grounded in visual input (Wang et al., 2023).
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf)
  - [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Language bias** (construct): *causes*, 3 papers
  > language bias in VLMs, a common issue for VLMs that often leads to hallucination when faced with extensive textual context. (ABSTRACT)
  - [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf)
  - [Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://aclanthology.org/2025.acl-long.175.pdf)
  - [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **Calibration** (construct): *causes*, 3 papers
  > Calibrating language models (LMs) is crucial, as it plays a vital role in detecting and mitigating hallucinations of LMs as well as building more trustworthy models. (ABSTRACT)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
  - [Trustworthy Medical Question Answering: An Evaluation-Centric Survey](https://aclanthology.org/2025.emnlp-main.1398.pdf)
- **Tool use** (behavioral indicator): *causes*, 3 papers
  > Recent studies have shown that LLMs can mitigate hallucination by accessing general-purpose tools (Schick et al., 2023; Tang et al., 2023; Patil et al., 2023; Qin et al., 2023; Wang et al., 2024b). (Section 1)
  - [Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf)
  - [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Visual grounding** (construct): *causes*, 3 papers
  > Several causes of hallucinations have been identified including biased training data (Liu et al., 2023), the inability of vision encoders to accurately ground images (Jain et al., 2024), misalignment among different modalities (Liu et al., 2024b), and insufficient context attention in LLM decoders (Huang et al., 2024; Liu et al., 2024d). (Section 2.2)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
- **Explanation generation** (behavioral indicator): *causes*, 3 papers
  > produces more explanations matching golden explanations but also generates redundant QA pairs, potentially leading to hallucination issues
  - [MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations](https://proceedings.neurips.cc/paper_files/paper/2024/file/e560a0b22e4432003d0dba63ff8dc457-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Knowledge boundary awareness** (construct): *causes*, 2 papers
  > “The knowledge boundary of an LLM limits its factual understanding, beyond which it may begin to hallucinate.”
  - [Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf)
  - [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf)
- **Overconfidence** (construct): *causes*, 2 papers
  > tuning LLMs on data containing unseen knowledge can encourage models to be overconfident, leading to hallucinations (Section 2).
  - [Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://aclanthology.org/2025.acl-long.804.pdf)
  - [Identifying and Answering Questions with False Assumptions: An Interpretable Approach](https://aclanthology.org/2025.emnlp-main.1228.pdf)
- **Self-correction** (behavioral indicator): *causes*, 2 papers
  > to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors, the model alignment and self-correction mechanism are adopted in LLMOPT. (Abstract)
  - [LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf)
  - [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf)
- **Predictive uncertainty** (construct): *causes*, 2 papers
  > When an LLM is uncertain about the semantic meaning of the next tokens to generate, it is likely to start hallucinating. Thus, it has been suggested that predictive uncertainty is one of the main causes of hallucinations. (Abstract)
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
  - [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://aclanthology.org/2025.emnlp-main.976.pdf)
- **Logical consistency** (construct): *causes*, 2 papers
  > A logically consistent LLM is less likely to hallucinate since its response is unlikely to change due to the logical manipulation of the prompt.
  - [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf)
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 2 papers
  > Asking the Constructor to complete the whole chain reduces hallucination, and avoids a sub-optimal greedy approach. (Section 3.2)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594.pdf)
- **Text generation** (behavioral indicator): *causes*, 1 paper
  > We theorise that as the VLLMs have not been explicitly trained on image-language pairs of manipulated images, a large number of parameters on the language generation leads to more hallucinations [25, 79] for this simple but abstract task. (Section 5.1)
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Detailed image description** (behavioral indicator): *correlates*, 1 paper
  > Results in Tab.6 show that longer captions tend to have higher hallucination rates. (Section 4.5)
  - [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf)
- **Reversal curse** (construct): *causes*, 1 paper
  > A well-studied failure mode underlying hallucinations is the reversal curse
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Long-context reasoning** (construct): *causes*, 1 paper
  > This trend underscores that larger graph sizes, and their associated challenges in long-range multi-step reasoning, are major contributors to hallucination.
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > Results in Table 2 show that this code-writing approach effectively reduced hallucination rates, particularly on large graphs.
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **Visual perception** (construct): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > ...they still face reliability issues such as hallucinations, stemming from misalignment with human instructions... (Section 1)
  - [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf)
- **Aleatoric uncertainty** (construct): *correlates*, 1 paper
  > This approach provides a precise measure of aleatoric semantic uncertainty, detecting whether the initial text is likely to be hallucinated. (Abstract)
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
- **Knowledge grounding** (construct): *causes*, 1 paper
  > In this way, we can force the skill LoRA to ground the LLM’s answers to its internal knowledge, thus reducing hallucinations. (Section 1)
  - [Fictitious Synthetic Data Can Improve LLM Factuality via Prerequisite Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98ecdc722006c2959babbdbdeb22eb75-Paper-Conference.pdf)
- **Synthetic recall** (behavioral indicator): *causes*, 1 paper
  > completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model’s retrieval ability. (Abstract)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Epistemic uncertainty** (construct): *causes*, 1 paper
  > Overall, we find strong evidence that accounting for weight uncertainty can improve decoding and reduce hallucinations when finetuning and pretraining from scratch, even without computational overhead. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Visual reasoning** (construct): *causes*, 1 paper
  > existing tuning methods train models to provide conclusive responses to instructions based on visual inputs, causing them to overlook essential intermediate visual reasoning. This often leads to ... even generating hallucinations. (Section 1)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **Image reconstruction** (behavioral indicator): *causes*, 1 paper
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Visual understanding** (construct): *causes*, 1 paper
  > engaging the MLLMs with a more powerful capability of image understanding so as to enhance the mitigation of hallucination. (Section 1)
  - [Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://aclanthology.org/2025.naacl-long.75.pdf)
- **Abstention** (behavioral indicator): *causes*, 1 paper
  > CDA successfully shifts the distribution towards abstention, preventing hallucinations. (Section 6.6, Figure 10)
  - [When to Speak, When to Abstain: Contrastive Decoding with Abstention](https://aclanthology.org/2025.acl-long.479.pdf)
- **Self-awareness** (construct): *causes*, 1 paper
  > This capability [self-awareness] would help mitigate hallucinations, discourage attempts at solving unsolvable problems, and prevent engagement in unethical tasks, ensuring more responsible and reliable behavior.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Memorization** (construct): *causes*, 1 paper
  > However, when the attacker’s merging rate is high, the merged model fails to retain the victim model’s memorization ability, leading to hallucination phenomenon. (Section 5.4.1)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
- **Consistency** (construct): *correlates*, 1 paper
  > smaller attentive consistency scores and larger non-attentive consistency scores indicate greater probabilities of hallucinations.
  - [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf)

### Associated with
- **Image captioning** (behavioral indicator), 3 papers
  > Dispreferred response: Model-generated descriptions resulting from either (1) corrupted image with low resolution or distorted color, or (2) “bad” prompts that cause the base model to hallucinate and describe elements that may not logically exist in the image. (Section 4)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
- **Object hallucination** (behavioral indicator), 2 papers
  > In the realm of MLLMs, “hallucination” typically refers to “object hallucination,” where the models generate plausible outputs containing objects that are either absent from or mismatched with the images (Section 2)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator), 2 papers
  > This issue is particularly prevalent in tasks such as image captioning and visual question answering (Liu et al., 2023a; Yin et al., 2023; Zhou et al., 2023b; Zhu et al., 2024a; Gunjal et al., 2024), where maintaining coherence between modalities is critical. (Section 2)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
- **Groundedness** (construct), 1 paper
  > Do groundedness predictions detect argument hallucinations? (Section 6.3)
  - [ConQRet: A New Benchmark for Fine-Grained Automatic Evaluation of Retrieval Augmented Computational Argumentation](https://aclanthology.org/2025.naacl-long.293.pdf)
- **Abstractive summarization** (behavioral indicator), 1 paper
  > Hallucinations in the abstractive summarization setting are grounding errors: errors where the output contains some information that is not supported by the context. (Section 2.1)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > These hallucinations (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. (Section 1).
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
- **Knowledge storage** (construct), 1 paper
  > They still struggle with issues such as hallucinations [5–7]... and these problems are exacerbated by the enigmatic internal mechanisms of knowledge storage within language models. (Introduction)
  - [Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf)
- **Knowledge retrieval** (behavioral indicator), 1 paper
  > Hallucinations pose a significant hurdle to the adoption of language models, especially in domains where reliable knowledge retrieval is paramount (Dahl et al., 2024). (Section 1)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Honesty** (construct), 1 paper
  > we first refine and extend the definition of honesty in LLMs based on the definition proposed by Askell et al. [14], as the ability to recognize their limitations, remain objective without pandering, and thereby avoid spreading misinformation or inducing hallucinations. (Section 1)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > This lack of proper evaluation can then materialize in persistent issues of deployed systems related to generalization, e.g., hallucination [30], out-of-distribution generalization [39], fairness [6], and generalization to the long-tail [23, 24]. (Section 1).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Confidence** (construct), 1 paper
  > generating nonfactual responses with unwarranted confidence. (Section 1)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Video detailed captioning** (behavioral indicator), 1 paper
  > We observed that generating all captions in a single conversation round often introduces hallucinations in the detailed captions. (Section 3.1.2)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Counting** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Attribute recognition** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Action prediction** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Style transfer** (behavioral indicator), 1 paper
  > First, we observe repetitions and hallucinations in some transferred texts. (Limitations)
  - [Style Transfer with Multi-iteration Preference Optimization](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Code summarization** (behavioral indicator), 1 paper
  > in the context of code summarisation, hallucination can be defined as a condition in which the generated summary does not accurately capture the intent and implementation details of the given input code. (Section 1)
  - [ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](https://aclanthology.org/2025.acl-long.1480.pdf)
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > (Zhai et al., 2023) deem that the hallucination in large models is related to the catastrophic forgetting in continual tuning. (Section 5.4. Analysis of Examples)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Closed-book question answering** (behavioral indicator), 1 paper
  > One significant challenge in CBQA is addressing hallucinations-instances where the model generates incorrect or fabricated answers (Section 2).
  - [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf)
- **Verbal uncertainty** (construct), 1 paper
  > Hallucinations arise from a miscalibration between VU and SU, where the model fails to express its high uncertainty in its generated output. (Section 4)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Semantic uncertainty** (construct), 1 paper
  > Hallucinations arise from a miscalibration between VU and SU, where the model fails to express its high uncertainty in its generated output. (Section 4)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Interpretability and explainability** (construct), 1 paper
  > ...problematic due to the opaque nature of LLMs’ parametric knowledge, which leads to poor interpretability and frequent hallucination issues. (Section 1)
  - [MusKGC: A Flexible Multi-source Knowledge Enhancement Framework for Open-World Knowledge Graph Completion](https://aclanthology.org/2025.emnlp-main.508.pdf)
- **Text-to-speech synthesis** (behavioral indicator), 1 paper
  > LLM-based TTS systems face challenges, with hallucinations being a prominent issue (Sahoo et al., 2024; Song et al., 2024; Neekhara et al., 2024a; Borsos et al., 2023).
  - [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://aclanthology.org/2025.emnlp-main.1076.pdf)
- **Dialogue summarization** (behavioral indicator), 1 paper
  > Finally, a notable limitation is the persistence of hallucinations in the generation of item recommendation information and dialogue summaries, where the model fabricates features not present in the source content. (Limitations)
  - [Refining Text Generation for Realistic Conversational Recommendation via Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.1456.pdf)
- **Accuracy** (construct), 1 paper
  > accuracy: whether the responses contains any hallucination, and present correct attributes; (Section 4)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
- **Definition generation** (behavioral indicator), 1 paper
  > In generating definitions, errors include gross hallucinations as in defining law as 'a system of rules created and enforced through social or governmental institutions to regulate behavior' in a context in which 'legal document setting forth rules governing a particular kind of activity' is the right sense (Section 4.2).
  - [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf)
- **Example generation** (behavioral indicator), 1 paper
  > When prompting the model to generate new examples, we still find gross hallucinations (Section 4.2).
  - [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf)
- **Misinformation generation** (behavioral indicator), 1 paper
  > We propose to categorize the LLM-based misinformation generation methods into three types based on real-world scenarios (Table 1): Hallucination Generation (HG) (Section 3)
  - [Can LLM-Generated Misinformation Be Detected?](https://proceedings.iclr.cc/paper_files/paper/2024/file/94bbcb744bbada8808fda05b9d9290d6-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > However, we also observed that autoregressive large language models like GPT-4o-mini tend to hallucinate responses... in answering questions within the privacy policy context.
  - [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf)
- **Conditional text generation** (behavioral indicator), 1 paper
  > Large Language Models (LLMs), when used for conditional text generation, often produce hallucinations, i.e., information that is unfaithful or not grounded in the input context. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Reasoning error** (behavioral indicator), 1 paper
  > hallucinations are not limited to factual inaccuracies; they can also extend to faulty or incomplete reasoning, a significant concern for multi-step reasoning-based tasks (Creswell et al., 2022). (Section 2)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
- **Answer generation** (behavioral indicator), 1 paper
  > In Answer Generation... answers containing the correct labels are of higher quality and suffer less from hallucination.
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **MMMU** (measurement instrument), 1 paper
  > We also include self-reported MMMU (Yue et al., 2024) results to demonstrate their significant correlation with hallucination rates: the Pearson correlation between −log HT and MMMU score is 0.902 with a p-value of 3.45×10−4. (Table 2)
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
