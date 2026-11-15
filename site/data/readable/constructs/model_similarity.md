# Model similarity
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Representation alignment, Model alignment  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats model similarity at the output level: papers describe it as statistical resemblance between two models' output distributions, independent of architecture or size, or as closeness between a draft or fine-tuned model and a reference model on the same inputs. Some definitions narrow this to token-level correspondence for speculative decoding, and another paper describes similarity through statistically similar or confusable outputs inferred from misclassification patterns. A smaller line of work shifts the construct away from outputs, either to internal representation alignment across layers and tasks, or to alignment as adherence to safety constraints, so the main disagreement is whether the construct is about output distributions, internal encodings, or safety behavior.

**Space of facets.** Papers use overlapping labels for partly different ideas. "Model similarity" usually names general output-distribution resemblance across models, "representation alignment" names layer-wise consistency in hidden representations and is described as a proxy for semantic and syntactic knowledge preservation during merging, and "model alignment" is used for several narrower cases: matching a draft model to a target model, keeping a fine-tuned model close to its pre-trained counterpart, and describing a continuum from strong to weak safety alignment. Within the output-level framing, papers also discuss similarity across model families, size ranges, and proprietary versus open-weight models, with one study reporting that models from the same family output more similar distributions than models of similar size, and attributing similarity to training data rather than scale.

**Space of measurement.** Papers do not link this construct to any named measurement instrument or behavioral indicator. Instead, they operationalize it through analyses of model outputs and representations: estimating pairwise distances between output distributions, inferring similarity from misclassification patterns, computing inter-model similarity from layer-wise hidden representations over clustered typical samples, and tracking token acceptance rates or output-space closeness between draft and target models or fine-tuned and pre-trained models. These operationalizations mostly follow the corresponding definitions, with output-based definitions measured through output comparisons and the representation-based definition measured through hidden-state comparisons.

**Links.** It is linked to two constructs, both through claimed causal relationships. One paper claims a causal relationship from model similarity to knowledge retention, stating that aligning a fine-tuned model with its pre-trained counterpart ensures retention of knowledge from large-scale data, and another paper claims a causal relationship from model similarity to attack transferability, citing work that suggests aligning white-box and target models in the safety domain can improve the transferability of adversarial prompts.

## Sources

**Model similarity** (2 papers: [Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf), [Idiosyncrasies in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf))
> The degree of statistical resemblance between the output distributions of two different language models, independent of their architecture or size.

**Representation alignment** (1 paper: [RECALL: REpresentation-aligned Catastrophic-forgetting ALLeviation via Hierarchical Model Merging](https://aclanthology.org/2025.emnlp-main.829.pdf))
> The internal consistency of how models encode inputs across layers and tasks, serving as a proxy for semantic and syntactic knowledge preservation during merging.

**Model alignment** (2 papers: [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf), [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf))
> The degree to which the token-level output distributions of a smaller draft model and a larger target model correspond, which is a critical factor for the efficiency of speculative decoding.

## Relationships

### Model similarity →
- **Knowledge retention** (construct): *causes*, 1 paper
  > aligning the fine-tuned model with the pre-trained one is crucial, as it ensures retention of knowledge obtained from large-scale data (Section 3.3).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **Attack transferability** (construct): *causes*, 1 paper
  > “Building on previous work suggesting that aligning white-box and target models in the safety domain can improve the transferability of adversarial prompts”
  - [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf)
