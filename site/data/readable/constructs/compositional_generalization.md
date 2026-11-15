# Compositional generalization
**Type:** Construct  
**Supporting papers:** 30  
**Also known as:** Compositional generalisation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats compositional generalization as the capacity to generalize to novel combinations or recombinations of known components that were not seen together during training. Most papers describe those components as concepts, linguistic elements, primitives, subtasks, or procedural steps, and frame success as solving unseen examples by systematically reusing familiar parts. A smaller line of work states this more explicitly as a latent ability to recognise and interpret unseen combinations of known phrases, while some multimodal papers broaden the framing to combining learned skills, such as image understanding and language generation, for novel tasks.

**Space of facets.** Papers organize the term mainly by what is being composed: verbs, subjects, and objects in action understanding, linguistic structures and derivations in semantic parsing, familiar words in novel contexts, known motor skills in robotics, or multiple applications, APIs, and GUI operations in agent tasks. Some authors use skill-combination as a particular sort of compositional generalization, while others use the term as an umbrella for reasoning over novel combinations of familiar primitives or constraints. It is also set alongside length generalization, and one paper distinguishes word-level composition from phrase-level structure. Another paper relates it to task generalization through a quantitative study of how many training tasks are needed to generalize over an entire function class.

**Space of measurement.** No measurement instrument is linked to it, and the only linked behavioral indicators are Integer addition and Sentiment analysis. In the papers, operationalization is usually benchmark-based: held-out splits over unseen verb, subject, and object combinations, synthetic semantic parsing tests, more complex tasks built from simpler subtasks, and evaluations introduced to measure ability to combine skills or novel combinations of primitives and motor skills. These operationalizations mostly match the dominant definition by testing unseen recombinations, though some extend measurement to broader skill composition across multimodal outputs or cross-application agent tasks.

**Links.** Papers link it to 6 constructs, with each specific link reported in individual papers. Individual papers claim causal relationships from compositional generalization to Generalization, described as one of the main drivers of generalization in multi-task training, and to Safety alignment, where it is said to enable transfer across prompt templates with awareness of safety constraints; another paper claims a causal relationship from In-context learning to compositional generalization. Other papers describe it as related to Multimodal understanding and Robustness, and no correlation link is reported.

## Sources

**Compositional generalization** (14 papers: [ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/c43b2989b1ba055aa713a4abbe4a8b05-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf), [SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf), [Zero and Few-shot Semantic Parsing with Ambiguous Inputs](https://proceedings.iclr.cc/paper_files/paper/2024/file/eae78bf2712f222f101bd7d12f875a57-Paper-Conference.pdf), [ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf), [AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf), [GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.420.pdf), [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf), [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf), [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.87.pdf), [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf), [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf), [Circuit Stability Characterizes Language Model Generalization](https://aclanthology.org/2025.acl-long.442.pdf))
> The model's capacity to generalize its understanding to novel combinations of concepts (like verbs, subjects, and objects) that were not seen during training.

**Compositional generalisation** (1 paper: [Compositional Generalisation for Explainable Hate Speech Detection](https://aclanthology.org/2025.emnlp-main.703.pdf))
> The latent ability of a model to recognise and correctly interpret novel combinations of known linguistic elements (e.g., targets and hateful expressions) that were not observed together during training.

## Relationships

### Compositional generalization →
- **Safety alignment** (construct): *causes*, 1 paper
  > The success of PTST suggests that LLMs have certain abilities of compositional generalization, which enable them to generalize from one template to another while being aware of safety constraints in the new template.
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > identified CG as one of the main drivers of the generalization observed in multi-task training. (Abstract)
  - [Exploring Compositional Generalization of Multimodal LLMs for Medical Imaging](https://aclanthology.org/2025.acl-long.639.pdf)

### → Compositional generalization
- **In-context learning** (construct): *causes*, 1 paper
  > What is striking is that learning in-context can under some circumstances lead to compositional generalization, that is generalization to unseen combinations of previously observed constituents
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)

### Associated with
- **Multimodal understanding** (construct), 1 paper
  > Many of the advanced vision-language capabilities demonstrated by GPT-4 can be understood as compositional skills rooted in two foundational skills: image understanding and language generation. (Section 5)
  - [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf)
- **Task generalization** (construct), 1 paper
  > While prior work has largely focused on qualitative insights into compositional generalization, our work takes a quantitative approach: studying how many training tasks are needed to achieve task generalization over an entire function class. (Section 2.1)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **Robustness** (construct), 1 paper
  > our approach considers the interaction between multiple problems, focusing more on the compositional generalization (Xu and Wang, 2024; An et al., 2023; Li et al., 2021) in robustness. (Section 1)
  - [From A and B to A+B: Can Large Language Models Solve Compositional Math Problems?](https://aclanthology.org/2025.emnlp-main.660.pdf)
- **Integer addition** (behavioral indicator), 1 paper
  > These findings reveal a core limitation in LLMs’ compositional generalization for elementary arithmetic. (Contributions)
  - [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf)
- **Sentiment analysis** (behavioral indicator), 1 paper
  > Two tasks that assess different aspects of compositional generalisation are used in the paper: Inverse Dictionary Modelling (IDM) for word-level composition and Sentiment Classification (SC) for phrase-level structure. (Section 4.1)
  - [CARMA: Enhanced Compositionality in LLMs via Advanced Regularisation and Mutual Information Alignment](https://aclanthology.org/2025.emnlp-main.822.pdf)
