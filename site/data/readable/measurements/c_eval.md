# C-Eval
**Type:** Measurement instrument  
**Supporting papers:** 26  
**Also known as:** CEval  

## State of the Field

**What it is.** Most commonly, papers treat C-Eval as a comprehensive Chinese benchmark or evaluation suite for foundation models. Definitions repeatedly describe it as multi-level and multi-discipline, usually spanning 52 subjects or disciplines, with one paper adding four difficulty levels and another specifying 13,948 multiple-choice questions; some definitions say it covers STEM, humanities, and social sciences or broader academic and professional domains, and targets factual knowledge, foundational knowledge, reasoning, and problem solving. A smaller set of papers describes particular slices of the suite, such as the logic subject or eight selected subjects, and some frame its use as assessing multi-task language understanding in a cross-linguistic setting or Chinese instructions.

**What it is claimed to measure.** Papers link C-Eval to 3 constructs and 2 behavioral indicators. The prevailing usage is to measure General ability, with several papers placing CEval among general-domain or authoritative benchmarks and reporting changes on C-Eval as changes in general abilities; smaller strands use it to measure Cross-lingual generalization and Multilingual understanding, and to evaluate Instruction following and Multiple-choice question answering. Overall, papers spread its measurement claims across several targets, though General ability is the most common framing.

**Space of uses.** Most papers use C-Eval alongside broader benchmark suites rather than on its own, commonly next to MMLU and also with CMMLU, GSM8K, HumanEval, and MATH. In those settings it is positioned as part of a "complete capability evaluation," a general-domain evaluation set, or a group of Chinese language understanding and commonsense reasoning datasets. Some papers also use subsets of it for narrower checks, such as the logic subject for logical-rule application or eight subjects for multi-choice QA.

## Sources

**C-Eval** (11 papers: [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf), [Pre-training Distillation for Large Language Models: A Design Space Exploration](https://aclanthology.org/2025.acl-long.181.pdf), [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf), [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf), [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf), [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> C-Eval, a benchmark used here to assess multi-task language understanding in a cross-linguistic setting.

**CEval** (2 papers: [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf), [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf))
> Comprehensive evaluation suite covering 52 Chinese academic subjects requiring factual and reasoning abilities.

## Relationships

### → C-Eval
- **General ability** (construct): *measured_by*, 3 papers
  > For the general domain evaluation benchmarks, we select MATH, MBPP, MMLU, and CEVAL from the aforementioned experimental settings. (Section 3.3).
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
  - [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For multi-choice QA, we choose eight subjects from CEVAL (Huang et al., 2023), covering compulsory courses from middle school to university in China. (Section 4.2)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > Instruction benchmarks evaluate a model’s ability to comprehend and execute detailed directives. ... with C-Eval (Huang et al., 2024) focusing on Chinese instructions.
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **Multilingual understanding** (construct): *measured_by*, 1 paper
  > a broad suite of general benchmarks—...CEval...—that cover ... multilingual understanding. (Section 4.1)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
- **Cross-lingual generalization** (construct): *measured_by*, 1 paper
  > "SEC’s competitive performance on C-Eval shows its capability in the cross-linguistic scenario"
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
