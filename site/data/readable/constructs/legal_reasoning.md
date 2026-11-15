# Legal reasoning
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Legal document interpretation, Legal multi-hop reasoning, Legal calculation, Interpretive ability  

## State of the Field

**Space of definitions.** Most papers treat legal reasoning as a broad latent ability to interpret legal texts, apply legal rules or principles to facts, and reach legally grounded conclusions, judgments, or arguments across tasks. A recurring emphasis is that this should proceed through structured logical inference, not just surface understanding, sometimes including implicit rules, formal procedures such as legal syllogism, and professional legal judgment. A smaller line uses narrower labels for parts of the same space: legal document interpretation focuses on extracting meaning or implications from documents, legal multi-hop reasoning on multiple inference steps from a legal scenario, legal calculation on computing periods or monetary amounts from rules and facts, and interpretive ability on applying named interpretation methods in context.

**Space of facets.** Papers break the construct into several facets rather than using a single uniform formulation. One decomposition covers issue-spotting, rule-recall, rule-application, rule-conclusion, interpretation, and rhetorical understanding; others organize it around legal syllogism, recognition of legal entities and relationships, and the use of implicit rules. Another strand highlights interpretive methods, including literal, systematic, purposive, sociological, and historical interpretation, so adjacent names in the literature appear as narrower facets within the broader construct.

**Space of measurement.** Operationalization is narrow relative to the breadth of the definitions: papers link legal reasoning to 1 measurement instrument, LegalBench, and to no behavioral indicators. LegalBench is used as a benchmark, described as containing 162 tasks that evaluate various aspects of legal reasoning, and some papers use a specific sub-task or problem templates adapted from it. Outside this named instrument, quoted passages operationalize the construct through performance on issue-spotting, rule application, interpretation, and statement-level decisions about whether text satisfies legal reporting requirements in context.

**Links.** Several papers claim legal reasoning is measured by LegalBench, using it for benchmark evaluation, a sub-task, or adapted problem templates. One paper reports that legal reasoning is related to logical reasoning, describing alignment with a syllogistic reasoning framework common in legal analysis. Papers here make measurement and relatedness claims, rather than causal or correlational claims.

## Sources

**Legal reasoning** (6 papers: [SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea3f85a33f9ba072058e3df233cf6cca-Paper-Conference.pdf), [AIMS.au: A Dataset for the Analysis of Modern Slavery Countermeasures in Corporate Statements](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a33ae4d634b49b0866b4142a1f82a2f-Paper-Conference.pdf), [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf), [LegalViz: Legal Text Visualization by Text To Diagram Generation](https://aclanthology.org/2025.naacl-long.339.pdf), [LegalAgentBench: Evaluating LLM Agents in Legal Domain](https://aclanthology.org/2025.acl-long.116.pdf), [JUREX-4E: Juridical Expert-Annotated Four-Element Knowledge Base for Legal Reasoning](https://aclanthology.org/2025.emnlp-main.188.pdf))
> The latent ability to interpret legal texts, apply legal rules, and draw legally grounded conclusions across diverse legal tasks.

**Legal document interpretation** (1 paper: [SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea3f85a33f9ba072058e3df233cf6cca-Paper-Conference.pdf))
> Interpreting legal texts and extracting their meaning, issues, or implications from prompts about legal documents.

**Legal multi-hop reasoning** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Performing multiple logical inference steps to solve a problem based on given contextual information from a legal scenario.

**Legal calculation** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Computing legally relevant time periods, monetary amounts, or other quantifiable values from legal rules and facts.

**Interpretive ability** (1 paper: [JUREX-4E: Juridical Expert-Annotated Four-Element Knowledge Base for Legal Reasoning](https://aclanthology.org/2025.emnlp-main.188.pdf))
> The capacity to apply hierarchical legal interpretation methods—literal, systematic, purposive, sociological, and historical—to clarify the meaning and application of legal texts in context.

## Relationships

### Legal reasoning →
- **LegalBench** (measurement instrument): *measured_by*, 3 papers
  > “For Law: We use the International Citizenship Questions sub-task in LegalBench [39].”
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf)
  - [Adaptively profiling models with task elicitation](https://aclanthology.org/2025.emnlp-main.1270.pdf)

### Associated with
- **Logical reasoning** (construct), 1 paper
  > We also rewrite samples to align with the syllogistic reasoning framework common in legal analysis. (Section 3.2)
  - [Unilaw-R1: A Large Language Model for Legal Reasoning with Reinforcement Learning and Iterative Inference](https://aclanthology.org/2025.emnlp-main.915.pdf)
