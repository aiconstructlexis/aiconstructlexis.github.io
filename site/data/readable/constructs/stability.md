# Stability
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Local stability, Inference stability  

## State of the Field

**Space of definitions.** Most commonly, papers describe stability as consistency or robustness under small changes, although what is supposed to remain stable differs. Some definitions focus on local prediction robustness, giving higher scores when predictions in an embedding-space neighborhood show high confidence and low variability, while others define stability as consistent performance near an optimal retrieval depth or as consistently high-quality outputs for a fixed input, quantified by low variance in reward scores across sampled generations. Smaller lines of work use the same term for controlled training dynamics that avoid collapse or divergence, bounded sensitivity of a decoding algorithm to perturbed logits, robustness of concepts or explanations to input or concept-set perturbations, and preservation of performance or knowledge across training rounds, languages, self-training, or sequential edits.

**Space of facets.** Papers explicitly distinguish local stability, inference stability, and training stability. Beyond those subtype labels, the same name is used for several levels at once: individual predictions or generations, model performance across retrieval settings or languages, training or self-training dynamics, decoding algorithms, explanations, and multilingual knowledge edits. Some authors use language close to consistency, while a recurring contrast is plasticity, including formulations where stability means preservation of old knowledge and plasticity means acquisition of new knowledge.

**Space of measurement.** Papers link stability to 2 measurement instruments, BIG-bench and MMLU, both benchmarks, and no behavioral indicators. Outside those named instruments, papers operationalize it through analyses: performance fluctuation within a small window around optimal retrieval depth, average confidence and variability in a local embedding neighborhood, the standard deviation of reward-model scores across multiple sampled generations, and bounded changes in output token probabilities under logit perturbations. The operationalizations track different paper-specific definitions rather than a single shared procedure.

**Links.** Papers claim a causal relationship from stability to faithfulness and from stability to instruction following ability. Other papers relate stability to plasticity, coherence, and consistency, with plasticity often discussed as something to balance against stability; additional constructs are also reported as related. No correlational links are reported.

## Sources

**Local stability** (1 paper: [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf))
> A latent property reflecting the robustness of a model's prediction at a given input, determined by the average confidence and variability of predictions in its local neighborhood in the embedding space.

**Stability** (2 papers: [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf), [Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf))
> The consistency of model performance around its optimal retrieval depth, indicating resilience to small variations in the number of retrieved passages.

**Inference stability** (1 paper: [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf))
> The degree to which a model consistently produces high-quality outputs for a given input, measured by the variance in reward scores across multiple generations.

## Relationships

### Stability →
- **Faithfulness** (construct): *causes*, 1 paper
  > Therefore, stability plays a pivotal role in ensuring explanation faithfulness.
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > "Extensive experiments on updated MMLU and BIG-Bench demonstrate the stability of the proposed strategies"
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > "Extensive experiments on updated MMLU and BIG-Bench demonstrate the stability of the proposed strategies"
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > This suggests that the top layers’ weights indeed lack sufficient stability gradient to maintain instruction-following ability initially. (Section 3.2)
  - [Efficient Domain Continual pretraining by Mitigating the Stability Gap](https://aclanthology.org/2025.acl-long.1578.pdf)

### Associated with
- **Plasticity** (construct), 2 papers
  > This technique demonstrates a negligible reduction in the FP metric, signifying a well-maintained balance between plasticity and stability. (Section 6)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Coherence** (construct), 1 paper
  > These models, however, often suffer from instability or lack of coherence, that is the ability of the models to generate semantically equivalent outputs when receiving diverse yet semantically equivalent input variations. (Abstract)
  - [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf)
- **In-context learning** (construct), 1 paper
  > We prove that the reasoning efficacy (measured by empirical prediction loss) can be bounded by an LLM-oriented semantic similarity and an inference stability of demonstrations, which is general for both one-shot and few-shot scenarios. (Abstract)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
- **Generation diversity** (construct), 1 paper
  > Furthermore, stability implies an intuitive notion of diversity, suggesting that tokens with similar logits should have comparable probabilities of being selected.
  - [Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf)
- **Self-improvement** (construct), 1 paper
  > We conducted further analysis to investigate the improvements of CER with various metrics, such as cross-template success rate, stability (preservation of old knowledge), and plasticity (acquisition of new knowledge) (Grossberg, 1982; Rolnick et al., 2019) (§5.2, §5.3), demonstrating its generalizability and effectiveness as a self-improvement system.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
- **Consistency** (construct), 1 paper
  > Our objective is to define a measure, denoted as S(x, f), for an input x and a given fine-tuned model f, that would preemptively quantify the consistency of the prediction ˆf(x) over a broad class of equally-well-performing fine-tuned models. (Section 3)
  - [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf)
