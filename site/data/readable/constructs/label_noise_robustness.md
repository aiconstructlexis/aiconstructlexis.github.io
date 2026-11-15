# Label noise robustness
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Robustness to noisy labels, Robustness to noisy textual descriptions, Robustness to noise, Robustness to label noise  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats label noise robustness as maintained model performance, or only minimal degradation, when supervision is corrupted. Most definitions focus on mislabeled or errorful training data, including synthetic label flips and self-generated data with inaccuracies; one paper states that the model "tolerates errors up to a threshold before performance collapses" and that this tolerance rises with more rounds of self-improvement (Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges). A smaller line broadens the noise source beyond labels to noisy captions or textual supervision, and some quoted passages use the broader language of robustness to noise for dialogue annotations, input formulations, or in-context demonstrations.

**Space of facets.** The papers mainly distinguish the construct by where the noise enters: corrupted training labels, noisy textual descriptions or captions, errors in self-generated training data, annotation or input noise, and corrupted labels in demonstrations. Naming varies accordingly, with "robustness to noisy labels", "robustness to label noise", and the broader "robustness to noise" used for closely related usages, while one paper isolates noisy textual descriptions as a specific case. Another recurring facet is tolerance, with one paper describing robustness as error tolerance up to a collapse threshold that increases after more rounds of self-improvement.

**Space of measurement.** Papers link the construct to 1 measurement instrument, CIFAR-10, and to no behavioral indicators. The explicit linked benchmark operationalization flips CIFAR-10 labels at 10%, 30%, and 50% and reads robustness from retained end-model accuracy or relative drop versus clean training; as one study puts it, the robust method achieves the "lowest relative drop in performance vs. training on the clean dataset" (Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning). Other papers operationalize the same idea by injecting 5% synthetic label noise during training and evaluating on MNLI and CivilComments-WILDS, by using a noisier caption dataset such as CC3M to test compositional performance, or by checking whether models keep performing under noisy demonstrations or self-generated errors. These operationalizations mostly match the dominant definitions, though some extend measurement from label corruption to broader textual or annotation noise.

**Links.** The only reported cross-construct link is causal: one paper claims a causal relationship from Flatness to Label noise robustness, citing prior observations that sharpness-minimization can enhance robustness toward label noise. No papers report correlational or generic related links for this construct.

## Sources

**Robustness to noisy labels** (1 paper: [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf))
> The degree to which model performance degrades minimally when training labels are corrupted or mislabeled.

**Robustness to noisy textual descriptions** (1 paper: [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf))
> The degree to which a model maintains compositional performance when captions or textual supervision are noisy.

**Robustness to noise** (1 paper: [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf))
> The resilience of a model's performance in the presence of synthetic label noise in the training data, indicating stability in learning despite data imperfections.

**Robustness to label noise** (1 paper: [Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25d/lee25d.pdf))
> The model's ability to maintain performance and continue the self-improvement process even when trained on self-generated data that contains a certain amount of errors or inaccuracies.

## Relationships

### Label noise robustness →
- **CIFAR-10** (measurement instrument): *measured_by*, 1 paper
  > For this experiment, we use CIFAR10 and randomly flip p percentage of the labels in the dataset—we vary p in {10%, 30%, 50%}.
  - [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf)

### → Label noise robustness
- **Flatness** (construct): *causes*, 1 paper
  > This aligns well with previous observations that sharpness-minimization can enhance robustness toward label noise (Baek et al., 2024). (4.4. Robustness to Noisy Data)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
