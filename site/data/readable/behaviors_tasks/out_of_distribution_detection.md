# Out-of-distribution detection
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** OOD detection  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this as the task of identifying inputs that do not belong to the training distribution. The more specific formulation adds a success criterion: a sample from a different distribution than the model was trained on should typically receive higher uncertainty than an in-distribution sample. One paper also frames it as a benchmark for uncertainty-aware methods, stating that an effective approach should "reliably assign higher uncertainties to OOD samples compared to ID samples."

**Variants.** Papers use both the names "Out-of-distribution detection" and "OOD detection." The studied settings vary by training and evaluation setup: one uses OBQA as the in-distribution dataset and ARC-C, ARC-E, and CSQA as OOD datasets, while another performs OOD detection during pre-training and fine-tuning and evaluates with external OOD datasets including SVHN. Another paper discusses distinguishing ID from OoD inputs in a setting where image interpretation capabilities affect performance.

**Space of elicitation and scores.** Two measurement instruments are linked to this behavior, CommonsenseQA and SVHN, and both are used as dataset-based evaluations. CommonsenseQA appears as an OOD test set in a setup fine-tuned on OBQA, while SVHN appears among external OOD datasets used for validation.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects, and the linked constructs are framed with different relationship types. Two constructs are linked: it is reported as related to epistemic uncertainty, with one paper saying epistemic uncertainty provides an improved indicator for out-of-distribution detection, and another paper claims a causal relationship from visual understanding to out-of-distribution detection, arguing that insufficient image interpretation capabilities limit accurate distinction between ID and OoD inputs.

## Sources

**Out-of-distribution detection** (1 paper: [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf))
> The observable task of identifying whether a given input sample comes from a different data distribution than the one the model was trained on, typically by assigning it a higher uncertainty score.

**OOD detection** (1 paper: [Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf))
> The task of identifying input samples that do not belong to the training distribution.

## Relationships

### Out-of-distribution detection →
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **SVHN** (measurement instrument): *measured_by*, 1 paper
  > The model is trained on CIFAR100-LT Krizhevsky & Hinton (2009) with an imbalance ratio of 100, and validated on external OOD datasets including SVHN Netzer et al. (2011), Places365 Zhou et al. (2017), LSUN Yu et al., iSUN Xu et al. and Texture Cimpoi et al. (2014). (Section 3)
  - [Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf)

### → Out-of-distribution detection
- **Visual understanding** (construct): *causes*, 1 paper
  > We found that one of the reasons for this discrepancy is the insufficient image interpretation capabilities of these models, which limits their ability to accurately distinguish between ID and OoD inputs. (Section 1)
  - [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf)

### Associated with
- **Epistemic uncertainty** (construct), 1 paper
  > “epistemic uncertainty providing an improved indicator for out-of-distribution detection.”
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
