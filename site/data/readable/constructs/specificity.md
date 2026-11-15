# Specificity
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Logical specificity  

## State of the Field

**Space of definitions.** Across papers, specificity is most commonly framed as a response-quality property: producing concrete, detailed, targeted content instead of vague or general statements. One paper states that responses should "refer to facts and details and avoid vague arguments" (MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models), and related legal and review definitions similarly emphasize clear, precise, fine-grained answers or feedback tied to the issues raised. A smaller line of work uses the same term for abstention behavior, defining specificity as not refusing questions about a concept's siblings or ancestors, so the main axis of disagreement is whether specificity is about generated content or about refusal selectivity. Some legal formulations further narrow it to "logical specificity", adding logically structured answers tailored to the specific facts and rules of a legal question.

**Space of facets.** The clearest subtype in the papers is logical specificity, a narrower legal formulation that keeps the emphasis on detail and precision but adds logical structure and tailoring to case facts and rules. More broadly, the same label is used for at least two different objects: the specificity of generated answers or feedback, and the specificity of abstention behavior. In review work it appears beside evidence support, and in a multi-objective alignment formulation it is listed alongside factual, readable, fair, repeat, and length objectives.

**Space of measurement.** Specificity is linked to 1 measurement instrument and 1 behavioral indicator. The only linked instrument is LLM-as-a-judge, used in an evaluation framework as a multi-perspective criterion alongside comprehensiveness and relevance. Papers operationalize the construct by checking whether responses refer to concrete facts and details, directly address the issues raised, or provide precise, fine-grained feedback; in abstention work, the linked behavioral indicator is Abstention, and specificity is quantified as the proportion of questions about sibling and ancestor concepts that are not refused. These operationalizations follow the two main usages in the definitions, response detail and refusal selectivity.

**Links.** Specificity is linked to 1 construct, Generalization, and papers describe this as a related, not causal, connection. In Knowledge Graph Guided Evaluation of Abstention Techniques, generalization and specificity are said to have an "inherent trade-off": abstaining from everything gives perfect generalization but no specificity, while not abstaining at all gives perfect specificity rates but no generalization. The same paper also reports Abstention as related to Specificity, using whether ancestor and sibling questions are not refused as the relevant behavior. No causal or correlational links are reported.

## Sources

**Specificity** (4 papers: [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf), [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf), [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf), [TreeReview: A Dynamic Tree of Questions Framework for Deep and Efficient LLM-based Scientific Peer Review](https://aclanthology.org/2025.emnlp-main.790.pdf))
> The model's tendency to refer to concrete facts and details rather than making vague or general arguments.

**Logical specificity** (1 paper: [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf))
> The ability of a model to produce detailed, precise, and logically structured answers tailored to the specific facts and rules of a legal question, rather than general statements.

## Relationships

### Specificity →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)

### Associated with
- **Generalization** (construct), 1 paper
  > Generalization and specificity are tied together by an inherent trade-off: abstaining from everything achieves perfect generalization but no specificity, and not abstaining at all results in perfect specificity rates but no generalization. (Section 5.1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > specificity: whether questions about ancestor and sibling concepts are not refused, where abstention is undesirable. (Section 1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
