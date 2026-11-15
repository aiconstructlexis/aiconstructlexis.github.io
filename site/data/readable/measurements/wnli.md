# WNLI
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Most commonly described as a Winograd Natural Language Inference benchmark or dataset, papers frame WNLI as a natural language inference evaluation centered on sentence-level understanding and pronoun reasoning. Across definitions, the recurring focus is pronoun resolution or ambiguity, coreference resolution, and reasoning in pronoun disambiguation, with some descriptions adding textual entailment-style reasoning or logical inference. One paper specifically reports using the validation set to measure performance.

**What it is claimed to measure.** Explicit measurement claims are narrow: papers link WNLI to one behavioral indicator and one construct. One paper uses it to measure natural language inference, describing RTE and WNLI as inference tasks, while another uses it as an out-of-domain task to evaluate generalization. The named targets are natural language inference and generalization, and no other constructs or behavioral indicators are linked in these papers.

**Space of uses.** Usage is most often as part of broader GLUE evaluations. It is related to one other instrument, GLUE, and papers place it alongside tasks such as CoLA, MRPC, RTE, and SST-2; reported setups include baseline comparisons across NLU tasks, zero-shot accuracy reporting for pruned models, and GLUE evaluation tables for fine-tuning. A smaller line of use treats WNLI as an out-of-domain task, and another reports validation-set performance on a finetuned model exhibiting length bias.

## Sources

**WNLI** (5 papers: [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf), [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [FISTAPruner: Layer-wise Post-training Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.1498.pdf), [MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines](https://aclanthology.org/2025.emnlp-main.1022.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf))
> A natural language inference benchmark used to evaluate sentence-level understanding and pronoun reasoning.

## Relationships

### → WNLI
- **Natural language inference** (behavioral indicator): *measured_by*, 1 paper
  > for inference tasks, the RTE and WNLI (both from GLUE) datasets (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurement instrument), 1 paper
  > for inference tasks, the RTE and WNLI (both from GLUE) datasets (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
