# Selection bias
**Type:** Construct  
**Supporting papers:** 8  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats selection bias as a latent or inherent model tendency to favor certain answer options in multiple-choice settings, such as repeatedly choosing particular option identifiers like A or 1 regardless of content. Some formulations emphasize answer positions, and one broadens this to positional or other surface-level patterns rather than content understanding, but the shared core is a systematic preference in option selection rather than content-based choice.

**Space of facets.** Papers usually place the construct in multiple-choice tasks, especially MCQA, where selecting among predefined choices creates room for preference for particular tokens or positions. A recurring breakdown distinguishes token-identity preferences from positional preferences, but the relation to positional bias is not stated uniformly: some work says selection bias is driven by both token identity and positional preferences, while another says it arises less from position bias.

**Space of measurement.** No measurement instrument is linked to it. Papers instead operationalize it through one linked behavioral indicator, multiple-choice question answering, by examining whether models prefer specific option IDs or answer positions when choosing among predefined options; this mirrors the dominant definitions, which also focus on option or position preference regardless of content.

**Links.** Papers link selection bias to four constructs. One paper claims a causal relationship from selection bias to robustness, stating that poor robustness to option position changes results from biased behavior, and another claims a causal relationship from selection bias to reasoning, stating that such bias compromises models' true reasoning capabilities. Selection bias is also related to positional bias, with recorded evidence ranging from being driven by positional preferences to arising less from position bias, and prompt sensitivity is reported to correlate with selection bias; one paper also relates multiple-choice question answering to selection bias.

## Sources

**Selection bias** (3 papers: [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf), [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf), [RoDEval: A Robust Word Sense Disambiguation Evaluation Framework for Large Language Models](https://aclanthology.org/2025.emnlp-main.864.pdf))
> A latent tendency of a model to favor certain option identifiers (e.g., always picking 'A') regardless of content.

## Relationships

### Selection bias →
- **Robustness** (construct): *causes*, 1 paper
  > LLMs’ poor robustness to option position changes results from their biased behavior: they prefer to select speciﬁc option IDs as answers (like “Option A”), which we term as selection bias.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > Such bias compromises fairness, reliability, and the true reasoning capabilities of these models. (Section 1).
  - [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf)

### → Selection bias
- **Prompt sensitivity** (construct): *correlates*, 1 paper
  > This suggests that a model weak on selection bias also tends to change its output for different prompt templates. (Section 7.1)
  - [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf)

### Associated with
- **Positional bias** (construct), 2 papers
  > Our findings show that selection bias, driven by both token identity and positional preferences, intensifies with increasing task difficulty, particularly when MCQ options are fine-grained. (Conclusion)
  - [Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1703.pdf)
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator), 1 paper
  > One such underexplored phenomenon is selection bias in MCQA. Unlike open-ended VQA formats, MCQA requires models to select one option among predefined choices (e.g., A/B/C/D), introducing the possibility of preference for certain option positions or tokens. (Introduction)
  - [Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1703.pdf)
