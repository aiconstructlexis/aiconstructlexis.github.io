# Instruction understanding
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Instruction comprehension  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats instruction understanding, often also called instruction comprehension, as a latent model ability to grasp the meaning, intent, constraints, or goals expressed in natural language instructions and to map them to appropriate actions, plans, or task execution. Most definitions place this ability in complex settings, such as constrained environments, specialized domains with intricate terminology, multi-condition questions, README-guided deployment, or embodied tasks, and one paper states that "Instruction Understanding Difficulty measures whether the model comprehends the instruction." A smaller line of work narrows the emphasis either to command-to-action mapping in embodied or tool-using contexts, or to understanding diverse phrasings and the full intent of instructions, including implicit and explicit constraints, across varied tasks.

**Space of facets.** The recurring facets are understanding meaning and intent, interpreting explicit or implicit constraints, handling specialized terminology, and converting directives into goals, actions, or plans. Another recurring distinction is between general instruction following and robustness to variation in wording, with some authors testing whether the same goal is understood under diverse natural-language phrasings or unseen instructions. Across these uses, "instruction understanding" and "instruction comprehension" are used for largely the same construct, and some papers discuss it alongside neighboring abilities such as visual grounding, planning, and strict constraint compliance.

**Space of measurement.** No measurement instrument is linked to it, and papers link it to 2 behavioral indicators, Robotic manipulation and Text-to-SQL. In practice, papers operationalize the construct through task-based and analytic checks: constrained embodied tasks that require turning instructions into sequential navigation or manipulation, difficulty analyses that ask whether the model comprehends the instruction, held-out instruction formulations to test unseen phrasings, and error analyses in which failures are defined as "overlook[ing] or misinterpret[ing] a critical constraint specified in the question." These operationalizations mostly match the dominant definitions by testing comprehension of instructions, constraints, and action mapping, though some assess it through downstream task performance or error categories rather than a separate dedicated instrument.

**Links.** Among linked constructs, Generalization is reported to correlate with Instruction understanding in ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL, which says smaller LLMs show "lower generalizability" alongside limited capacity to understand complex instructions. For behavioral indicators, DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution claims a causal relationship from Instruction understanding to Robotic manipulation, citing the "strong task instruction understanding and visual grounding capabilities" of MLLMs in language-instructed multitask manipulation. The same ROUTE paper also claims a causal relationship from Text-to-SQL to Instruction understanding, warning that training on a single SQL generation task can diminish performance in understanding instructions.

## Sources

**Instruction comprehension** (5 papers: [TCPO: Thought-Centric Preference Optimization for Effective Embodied Decision-making](https://aclanthology.org/2025.emnlp-main.484.pdf), [OSDA Agent: Leveraging Large Language Models for De Novo Design of Organic Structure Directing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38fbf326eb71f4749d04102323f7f79-Paper-Conference.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science Research Repositories](https://aclanthology.org/2025.naacl-long.633.pdf), [CFBench: A Comprehensive Constraints-Following Benchmark for LLMs](https://aclanthology.org/2025.acl-long.1581.pdf))
> The model's ability to understand task instructions and map them to appropriate actions in constrained environments.

**Instruction understanding** (5 papers: [3DS: Medical Domain Adaptation of LLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.983.pdf), [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf), [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf), [MultiChartQA: Benchmarking Vision-Language Models on Multi-Chart Problems](https://aclanthology.org/2025.naacl-long.566.pdf), [GeLLM³O: Generalizing Large Language Models for Multi-property Molecule Optimization](https://aclanthology.org/2025.acl-long.1225.pdf))
> The latent ability of an LLM to comprehend the meaning and intent of an instruction, particularly in specialized domains with complex terminology.

## Relationships

### Instruction understanding →
- **Robotic manipulation** (behavioral indicator): *causes*, 1 paper
  > The strong task instruction understanding and visual grounding capabilities of MLLMs [5, 4] have exhibited great promise for language-instructed multitask robotic manipulation [7, 8, 9].
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)

### → Instruction understanding
- **Generalization** (construct): *correlates*, 1 paper
  > This is due to the limited capacity of smaller LLMs to understand complex instructions, showing lower generalizability.
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **Text-to-SQL** (behavioral indicator): *causes*, 1 paper
  > Additionally, training LLMs on a single SQL generation task poses a substantial risk of diminishing performance in understanding instructions... (Section 1)
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
