# Grounding
**Type:** Construct  
**Supporting papers:** 34  
**Also known as:** Grounding ability, Grounding capability, Visual localization, Grounded understanding  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats grounding as a latent ability to connect language or high-level reasoning to concrete referents, most often fine-grained visual details or exact spatial locations in images, videos, UIs, and 3D scenes. Definitions repeatedly describe localizing regions or elements from text, producing coordinates or bounding boxes, or tying predictions to object identities, motion, interactions, and other low-level evidence; as one paper puts it, "model predictions need to be grounded in fine-grained low-level details, such as object motions and object interactions" (Look, Remember and Reason: Grounded Reasoning in Videos with Language Models). Smaller lines of work use the same term more broadly for anchoring outputs in environmental context and feedback, executable actions, structured schemas, provided evidence, or retrieved context. There is also a recurring difference between papers that frame grounding as a latent capacity and one UI-focused definition that treats it as the observable task of locating elements on a screen.

**Space of facets.** Papers systematize grounding mainly by setting rather than through one shared taxonomy. The most common family is spatial grounding, expressed with nearby labels such as grounding ability, grounding capability, visual localization, and grounded understanding, and some authors separate it from referring as a related capability. Other papers use grounding for broader anchoring of responses or actions to environment feedback, fixed schemas, visual evidence, or retrieved context, so the same name covers both precise localization and broader context anchoring.

**Space of measurement.** Papers link grounding to 2 measurement instruments and 5 behavioral indicators. The named instruments are both benchmarks: ScreenSpot is used for GUI grounding capabilities, and InfiniBench includes grounding-based MCQ skills. Operationalizations are usually explicit localization or anchoring tasks, such as outputting coordinates or bounding boxes from screenshots, listing widgets, finding text or a described widget on a screen, localizing image regions from semantic descriptions, or justifying answers with visual evidence. The most frequently linked behavioral indicators are object recognition, object tracking, and referring expression generation, plus 2 other behavioral indicators; these operationalizations mainly instantiate spatial localization or action-linked grounding, while some definitions also use the term for anchoring to provided or retrieved context.

**Links.** Only a few explicit links are recorded. Papers claim causal relationships from grounding to visual reasoning and agency, and papers report related links from grounding to instruction following ability and spatial understanding. Separate papers also record causal links from low-level surrogate tasks to grounding, a causal link from grounding to a referring behavior, and another causal link from a UI referring behavior to grounding, while tool use is described as related to grounding.

## Sources

**Grounding** (11 papers: [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [Multi-modal Situated Reasoning in 3D Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/feaeec8ec2d3cb131fe18517ff14ec1f-Paper-Datasets_and_Benchmarks_Track.pdf), [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/file/394c7c30ea87b5c3521b4d9e9d419071-Paper-Conference.pdf), [GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.420.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf), [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://aclanthology.org/2025.naacl-long.488.pdf), [On the Limit of Language Models as Planning Formalizers](https://aclanthology.org/2025.acl-long.242.pdf), [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf), [RAGferee: Building Contextual Reward Models for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.414.pdf))
> The model's ability to connect high-level concepts and reasoning processes to fine-grained, low-level visual details in a video, such as object identities, motion, and interactions.

**Grounding ability** (2 papers: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf), [GUICourse: From General Vision Language Model to Versatile GUI Agent](https://aclanthology.org/2025.acl-long.1065.pdf))
> The capacity to produce precise spatial outputs for GUI elements, such as coordinates or bounding boxes, from screenshots.

**Grounding capability** (2 papers: [Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf), [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> The latent ability to accurately associate textual references with specific visual locations or bounding boxes in a UI.

**Visual localization** (1 paper: [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf))
> The latent ability to identify where in an image the relevant subject or evidence for a question is located.

**Grounded understanding** (1 paper: [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf))
> The ability to connect language expressions to specific image regions or objects with precise spatial localization.

## Relationships

### Grounding →
- **Visual reasoning** (construct): *causes*, 1 paper
  > many visual reasoning problems in videos require grounding in fine-grained low-level information (Section 1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **Agency** (construct): *causes*, 1 paper
  > Emergent agentic abilities are strongly dependent on basic abilities like grounding, world modeling, and self-reflection.
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ScreenSpot** (measurement instrument): *measured_by*, 1 paper
  > We first evaluated AGUVIS’s fundamental GUI grounding capabilities using ScreenSpot (Cheng et al., 2024), a benchmark that spans mobile, desktop, and website platforms. (Section 3.1)
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
- **InfiniBench** (measurement instrument): *measured_by*, 1 paper
  > InfiniBench skills: covers eight core skills, grouped into grounding-based (MCQ) and reasoning-based (open-ended) categories.
  - [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf)
- **Referring expression generation** (behavioral indicator): *causes*, 1 paper
  > “Particularly, when adding grounding data into training, the referring performance gets improved, and vice versa.”
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)

### → Grounding
- **Object recognition** (behavioral indicator): *causes*, 1 paper
  > Our multi-modal LRR model is grounded to relevant low-level visual information in the scene by stochastically introducing low-level surrogate tasks during training, including object recognition, re-identification, and tracking (Section 1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **Object tracking** (behavioral indicator): *causes*, 1 paper
  > Our multi-modal LRR model is grounded to relevant low-level visual information in the scene by stochastically introducing low-level surrogate tasks during training, including object recognition, re-identification, and tracking (Section 1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **UI element referring** (behavioral indicator): *causes*, 1 paper
  > “Particularly, when adding grounding data into training, the referring performance gets improved, and vice versa.”
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)

### Associated with
- **Tool use** (behavioral indicator), 1 paper
  > This requires decomposing a task, grounding intention to tools, and using the results for further actions, relying on natural language reasoning and programming abilities (Section 3.2)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **Spatial understanding** (construct), 1 paper
  > In vision-language learning, how to enable spatial understanding in models is a fundamental research problem. Two desired capabilities stem from this problem: referring and grounding.
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Instruction following ability** (construct), 1 paper
  > Errors in grounding valid actions highlight a limitation in the model’s ability to follow instructions and format actions correctly (Section 4.3).
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
