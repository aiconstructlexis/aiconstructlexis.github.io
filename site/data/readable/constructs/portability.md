# Portability
**Type:** Construct  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats portability as the ability or extent to which an edit carries beyond direct queries about the edited knowledge. Definitions agree that it concerns applying newly edited knowledge to related but distinct content or contexts. A broader framing extends this to transfer in downstream tasks, multi-hop reasoning chains, and different model variants, describing portability as generalization beyond the original setting and as evidence of deeper integration into the model's knowledge structure.

**Space of facets.** Papers mostly organize portability as an evaluation dimension within knowledge editing rather than as a standalone taxonomy. In that role, it is described as one of the criteria an editing method should satisfy, and the surrounding language often treats it as the generalization or transfer of an edit. The recurring facets are transfer to related content, downstream tasks, and multi-hop reasoning, while one paper also includes different model variants and another ties portability to reasoning about the downstream effects of edited knowledge through N-hop questions.

**Space of measurement.** Across the papers, portability is linked to 1 measurement instrument and 2 behavioral indicators. The only named instrument is MQuAKE, a multi-hop benchmark used to assess whether modified knowledge can be applied effectively to related content, especially in multi-hop reasoning. The linked behavioral indicators are knowledge editing and multi-hop question answering: papers assess portability as one dimension of knowledge editing evaluation, and one paper uses N-hop efficacy questions as portability questions, which matches the definitions' emphasis on transfer beyond direct queries.

**Links.** Several papers relate portability to knowledge editing, describing it as a criterion or dimension for assessing editing algorithms. Multi-hop reasoning is reported to correlate with portability, including a claim that portability metrics decline as the number of hops increases, and multi-hop question answering is related to portability through N-hop evaluation questions designed to capture downstream effects of edited knowledge. One paper claims a causal relationship from instruction following ability to portability, attributing better portability to better instruction-following capability.

## Sources

**Portability** (2 papers: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf), [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.803.pdf))
> The ability of a model to successfully apply newly edited knowledge to related but distinct content or contexts.

## Relationships

### Portability →
- **MQuAKE** (measurement instrument): *measured_by*, 1 paper
  > MQuAKE (Zhong et al., 2023) is a multi-hop benchmark... Portability evaluates the robustness of the generalization of the edit, evaluating whether the modified knowledge can be applied effectively to related content (e.g. Multi-Hop Reasoning).
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)

### → Portability
- **Multi-hop reasoning** (construct): *correlates*, 2 papers
  > Portability Metrics Decline with Increasing Number of Hops... This phenomenon can be attributed to the escalating complexity of reasoning required to accurately apply the edited knowledge across multiple interconnected facts.
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > For reliability, generalization, and portability evaluations, LLaVA-1.5 outperforms BLIP-2 and MiniGPT-4. This improved performance can be attributed to its larger model size and better instruction-following capability... (Section 5.2.1)
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)

### Associated with
- **Knowledge editing** (behavioral indicator), 2 papers
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (2) Portability: relevant knowledge such as the first lady of United States should be updated as well. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Multi-hop question answering** (behavioral indicator), 1 paper
  > The Portability Scores intend to measure the ability of LLMs to reason about the downstream effects of edited knowledge. Thus, we design the Efficacy Evaluation Questions with N hops (N = 1 ∼6) as Portability Evaluation Questions. (Section 2.2, Facet 3)
  - [Can Knowledge Editing Really Correct Hallucinations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/db93ccb6cf392f352570dd5af0a223d3-Paper-Conference.pdf)
