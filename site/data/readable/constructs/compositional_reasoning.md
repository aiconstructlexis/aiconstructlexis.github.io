# Compositional reasoning
**Type:** Construct  
**Supporting papers:** 39  
**Also known as:** Composite task solving  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats compositional reasoning as reasoning over combinations of familiar parts, often novel ones, rather than recognizing elements in isolation. Definitions repeatedly describe understanding relations among components, for example visual entities and relations, action components such as verb, subject, and object, or acoustic events with order and attribute binding, and one paper describes it as the capacity for "infinite use of finite means." A second, also recurring framing casts it as solving a complex task by decomposing it into smaller subtasks or sub-questions, executing them in sequence, and combining the intermediate results. One paper narrows this further under the name composite task solving, restricting it to tasks with two sequential subtasks and no explicit intermediate steps in the input.

**Space of facets.** Papers organize the construct by the kind of components and relations under consideration. Some focus on scenes or videos, stressing objects, attributes, relations, motion, and interactions; others define it through audio-event interrelationships such as order and attribute binding, through multimodal problems that combine visual and textual reasoning steps, or through linguistic composition in wordplay. One paper further divides the compositionality problem into Text, Image, and Group subtasks, while another treats compositional questions as mixtures of known and unknown sub-questions that require both internal reasoning and external acting. The same general idea is also given a narrower name in one paper, composite task solving.

**Space of measurement.** Operationalization is benchmark-based: papers link the construct to 10 measurement instruments and 3 behavioral indicators. The most frequently linked instruments are Winoground, GQA, Cola, Bamboogle, and BigCodeBench, with five other instruments also used. These measures make the construct concrete through image-text matching where captions use the same words in different orders, real-world visual questions that require compositional reasoning, caption retrieval based on relations between similar images, complex questions said to assess compositional reasoning, and code tasks that require sequences of function calls from multiple libraries to solve one task. Across these benchmarks, the construct is operationalized both as sensitivity to relations among components and as successful composition of sequential task steps.

**Links.** No causal or correlational relationships are reported, and no linked constructs are recorded. A few papers instead record related links: Chain of thought is related to compositional reasoning through step-by-step operations and intermediate results that let a model learn components of compositional tasks, Code refactoring is related because multi-file refactoring requires reasoning and composition of multiple smaller changes, and compositional reasoning is related to Visual question answering in work arguing that many such tasks depend on interactions and that marginal attributions are insufficient.

## Sources

**Compositional reasoning** (14 papers: [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf), [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf), [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf), [KiVA: Kid-inspired Visual Analogies for Testing Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/435cce71b4007699041dfffa4f034079-Paper-Conference.pdf), [GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.420.pdf), [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.331.pdf), [“What do you call a dog that is incontrovertibly true? Dogma”: Testing LLM Generalization through Humor](https://aclanthology.org/2025.acl-long.1117.pdf), [MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf), [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf))
> The ability to understand and reason about novel combinations of familiar components, such as recognizing an action composed of a known verb, subject, and object in a new configuration.

**Composite task solving** (1 paper: [Internal Chain-of-Thought: Empirical Evidence for Layer-wise Subtask Scheduling in LLMs](https://aclanthology.org/2025.emnlp-main.1147.pdf))
> Producing correct outputs for tasks that require two sequential subtask applications, such as retrieving knowledge and then transforming it, without explicit intermediate steps in the input.

## Relationships

### Compositional reasoning →
- **Winoground** (measurement instrument): *measured_by*, 5 papers
  > Fine-tuning on this data enhances the model’s ability to distinguish between similar images, showing improvements on challenging benchmarks like Winoground, MMVP, and EQBEN, which test compositional reasoning and fine-grained understanding. (Section 6.1)
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
  - [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
  - [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 3 papers
  > ...GQA (Hudson and Manning, 2019) for real-world compositional reasoning... (Section 3.1)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **Cola (compositional image retrieval)** (measurement instrument): *measured_by*, 2 papers
  > We first evaluate our CoVLM on compositional reasoning tasks, including... matching the correct captions describing the relation between two images with similar entities (Cola, (Ray et al., 2023))... (Section 4.1)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **SugarCrepe** (measurement instrument): *measured_by*, 1 paper
  > We comprehensively analyze the compositional understanding of models on the SugarCrepe benchmark, as detailed in Table 4. (Section 4.2)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > Fine-tuning on this data enhances the model’s ability to distinguish between similar images, showing improvements on challenging benchmarks like Winoground, MMVP, and EQBEN, which test compositional reasoning and fine-grained understanding. (Section 6.1)
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **CREPE** (measurement instrument): *measured_by*, 1 paper
  > Crepe [16] also evaluates several SOTA VLMs and highlights the lack of CR abilities.
  - [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BigCodeBench** (measurement instrument): *measured_by*, 1 paper
  > BigCodeBench frequently invokes a sequence of function calls from multiple libraries to solve a single task, requiring significant compositional reasoning ability for task-solving. (Section 3)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **FreshQA** (measurement instrument): *measured_by*, 1 paper
  > Experimental results on CuQA and FreshQA (Vu et al., 2023) datasets show the superiority of Self-DC in terms of both effectiveness and efficiency, revealing its promising potential to solve compositional reasoning problem. (Section 1)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.331.pdf)
- **Bamboogle** (measurement instrument): *measured_by*, 1 paper
  > Bamboogle (Press et al., 2023) includes complex questions that Google answers incorrectly, assessing compositional reasoning. (Section 4.1)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on general video understanding benchmarks: ... NeXTQA (Xiao et al., 2021) (compositional reasoning)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)

### Associated with
- **Chain of thought** (behavioral indicator), 1 paper
  > “This format includes step-by-step operations and intermediate results, allowing the model to learn the individual components of compositional tasks.”
  - [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Code refactoring** (behavioral indicator), 1 paper
  > Unlike isolated function-level edits, multi-file refactoring requires comprehensive reasoning and composition of multiple smaller changes. (Section 1)
  - [RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator), 1 paper
  > In many compositional reasoning tasks, interactions are key and marginal attributions are insufficient. We illustrate this using an image of a dog playing with a basketball and prompting the LLaVA-NeXT-Mistral-7B model (Liu et al., 2023) with “What is shown in this image?”. (Sec. 7.2)
  - [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf)
