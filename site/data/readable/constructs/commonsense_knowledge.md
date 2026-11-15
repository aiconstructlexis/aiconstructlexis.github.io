# Commonsense knowledge
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Common sense, Common-sense knowledge, Commonsense, Common sense knowledge  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats commonsense knowledge as implicit or latent world knowledge encoded in a model and applied to reasoning about everyday, complex, and contextualized situations. Many definitions phrase it as background knowledge about everyday objects, social conventions, and typical properties or relationships, while some instead foreground an ability or tendency to make judgments and inferences that align with human intuition, including plausible unstated inferences. A smaller line of work narrows the notion to domain uses such as rational decision-making in driving scenarios, adjudicating object scales, or preserving background knowledge during fine-tuning.

**Space of facets.** Papers often place the concept beside reasoning and world knowledge, and some pair it with language comprehension, text generation, factualness, scientific knowledge, or comprehension of the physical world. Several papers also use near-interchangeable labels, including "commonsense knowledge," "common-sense knowledge," "common sense knowledge," and "common sense": some definitions refer to the knowledge itself, while others define an ability to understand, judge, or reason with it. In planning-oriented formulations, papers describe it as prior knowledge that can be sampled from the model or preserved while other capabilities are tuned.

**Space of measurement.** Operationalization is benchmark-heavy: papers link the construct to 8 measurement instruments and 3 behavioral indicators. The most frequently linked instruments are A-OKVQA, ALFWorld, InfoSeek, MME, and MMLU, and 3 other instruments; the evidence describes them as tasks or benchmarks that rely on outside or background knowledge, covering multimodal question answering, image understanding, household work, and complex interactive environments. This usually matches the dominant definition, but some operationalizations are broader, for example measuring outputs in terms of factualness and common sense, bundling commonsense with diverse image-understanding abilities, or using MMLU performance as evidence that commonsense knowledge is preserved.

**Links.** Beyond measurement, papers link it to 3 behavioral indicators and 2 constructs, with causal claims for action selection, generalization, and embodied planning. The causal claims are stated in different settings: commonsense knowledge is used with memory-derived experiences for decision-making in a traffic scenario, said to enhance generalizable performance in keypoint localization, and treated as acquired knowledge for task planning. Separate papers report that it is related to object placement and to general ability, where common sense appears alongside comprehension and reasoning.

## Sources

**Commonsense knowledge** (9 papers: [Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [PlaSma: Procedural Knowledge Models for Language-based Planning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2024/file/16bce4070c4e23434451b180348e3814-Paper-Conference.pdf), [Tree-Planner: Efficient Close-loop Task Planning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d53538ba21c05fa361d2b21704172753-Paper-Conference.pdf), [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf), [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf), [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf), [GER-LLM: Efficient and Effective Geospatial Entity Resolution with Large Language Model](https://aclanthology.org/2025.emnlp-main.1186.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf))
> The implicit knowledge about the world required to reason about complex and contextualized situations.

**Commonsense** (1 paper: [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf))
> The model's ability to understand and make judgments about everyday situations and concepts that are typically taken for granted by humans.

**Common-sense knowledge** (2 papers: [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf))
> The pre-existing, general world knowledge embedded within the LLM that can be applied to understand and make rational decisions in driving scenarios.

**Common sense** (3 papers: [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf), [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf))
> The latent ability of a model to understand and reason about situations in a way that aligns with general human knowledge and intuition.

**Common sense knowledge** (3 papers: [Architect: Generating Vivid and Interactive 3D Scenes with Hierarchical 2D Inpainting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf), [Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface](https://proceedings.iclr.cc/paper_files/paper/2025/file/25458943db16e0f78f748ca5bc34fff6-Paper-Conference.pdf), [COLA: Collaborative Multi-Agent Framework with Dynamic Task Scheduling for GUI Automation](https://aclanthology.org/2025.emnlp-main.227.pdf))
> The latent knowledge a model possesses about the typical properties, functions, and relationships of objects and concepts in the everyday world, used here to adjudicate object scales.

## Relationships

### Commonsense knowledge →
- **A-OKVQA** (measurement instrument): *measured_by*, 2 papers
  > InfoSeek and A-OKVQA Rely on Commonsense Knowledge (RCK) (Table 2).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)
- **Action selection** (behavioral indicator): *causes*, 1 paper
  > In the Reasoning module, we utilize the experiences derived from the Memory module and the common-sense knowledge of the LLM to perform decision-making for the current traffic scenario. (Section 3.3)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **InfoSeek** (measurement instrument): *measured_by*, 1 paper
  > InfoSeek and A-OKVQA Rely on Commonsense Knowledge (RCK) (Table 2).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > Figure 1: Across 7B to over 110B parameters, comparing lots of open- and closed-source LLVMs with Meteor on MME [35], MMB [36], MathVista [37], and AI2D [38] requiring diverse capabilities for image understanding, common-sense knowledge, non-object concept understanding, etc.
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > we use TruthfulQA [27] to measure the reliability of the outputs generated by Aligner in terms of factualness and common sense. (Section 3.2)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > Overall, we show that leveraging detailed keypoint descriptions through comprehensive text, combined with commonsense knowledge from LLMs, effectively enhances generalizable performance in keypoint localization. (Section 4.4)
  - [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > "Notably, TPO does not lead to performance degradation of LLMs on MMLU tasks, indicating that commonsense knowledge is preserved during the TPO fine-tuning process."
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **ScienceWorld** (measurement instrument): *measured_by*, 1 paper
  > We choose ScienceWorld (Wang et al., 2022), a complex interactive environment requiring skills in long-term memory, sub-task decomposition, and scientific and commonsense knowledge. (Section 4.2)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
- **ALFWorld** (measurement instrument): *measured_by*, 1 paper
  > "The main challenge of this benchmark is to locate the target object and fulfill household work with commonsense knowledge of LLMs."
  - [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > “Finally, OpenBookQA evaluates the understanding of common knowledge (Mihaylov et al., 2018).”
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Embodied planning** (behavioral indicator): *causes*, 1 paper
  > Large language models(LLMs) trained on massive corpora are generally considered to have acquired common sense knowledge for task planning
  - [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf)

### Associated with
- **General ability** (construct), 1 paper
  > degradation in foundational LLM capabilities such as comprehension, reasoning, and common sense — an effect known as alignment tax (Section 1)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Object placement** (behavioral indicator), 1 paper
  > Holodeck [Yang et al., 2024c], leveraging common sense from LLMs to generate floor plans and place objects (Section 4)
  - [Architect: Generating Vivid and Interactive 3D Scenes with Hierarchical 2D Inpainting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
