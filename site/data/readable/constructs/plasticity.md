# Plasticity
**Type:** Construct  
**Supporting papers:** 9  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats plasticity as an ability or capacity to quickly and effectively adapt to something new, most commonly a new data distribution such as a different domain or language, and more broadly new information, corpora, or tasks. Definitions agree on adaptation and learning in the new setting, and one formulation makes the speed criterion explicit by describing plasticity as reaching target performance with minimal steps or achieving the highest possible performance. A narrower framing appears in work on self-improving systems, where plasticity is described as acquisition of new knowledge and skills, reflected in solving new types of tasks that the baseline could not solve.

**Space of facets.** The main structuring move is to place plasticity alongside stability. Papers describe a balance or trade-off between the two, and one study explicitly glosses the pair as plasticity, "acquisition of new knowledge," versus stability, "preservation of old knowledge." The term also spans two close uses in the literature here: adaptation to new distributions such as domains or languages, and acquisition of new knowledge or skills for new task types.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to plasticity. In the papers' own operational descriptions, it is assessed through performance on new settings: quick adaptation to new domains or languages, either by reaching target performance with minimal steps or by the highest achievable performance; improvement on new cases and the number of additional tasks solved relative to a baseline; and, in one formulation, lack of plasticity is said to result in poor AP4 and FWT4, while forgetting is discussed through BWT4. These operationalizations follow the same themes as the definitions, centering adaptation to new distributions, information, or tasks.

**Links.** The recorded links are relational rather than causal or correlational. Among linked constructs, plasticity is most often related to stability: multiple papers describe a balance or trade-off between the two, including "well-maintained balance" and "out-of-balance" formulations. It is also related to self-improvement in one paper, where plasticity and stability are among the metrics used to analyze a self-improvement system.

## Sources

**Plasticity** (3 papers: [DEPT: Decoupled Embeddings for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/20ceffa1fcec0f882868e5b891e3e7fa-Paper-Conference.pdf), [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf), [MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRA Experts for Rehearsal-Free Generative Retrieval over Dynamic Corpora](https://aclanthology.org/2025.emnlp-main.20.pdf))
> The model's ability to quickly and effectively adapt to a new data distribution, such as a different domain or language.

## Relationships

### Associated with
- **Stability** (construct), 2 papers
  > This technique demonstrates a negligible reduction in the FP metric, signifying a well-maintained balance between plasticity and stability. (Section 6)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Self-improvement** (construct), 1 paper
  > We conducted further analysis to investigate the improvements of CER with various metrics, such as cross-template success rate, stability (preservation of old knowledge), and plasticity (acquisition of new knowledge) (Grossberg, 1982; Rolnick et al., 2019) (§5.2, §5.3), demonstrating its generalizability and effectiveness as a self-improvement system.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
