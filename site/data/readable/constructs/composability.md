# Composability
**Type:** Construct  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the papers, composability is not used with a single settled definition. One paper defines it as the ability to combine parameters or components trained on distinct tasks to create new multitask capabilities without additional training, another defines it as a latent property of interventions or models where sequential updates do not interfere with prior or future interventions, and another defines it for connected modular circuits whose combined operation should logically follow from their individual functions. The disagreement is mainly over what carries the property, model weights or components, interventions, or modular circuits, and over what successful composition consists in, multitask capability, non-interference, or logical functional composition.

**Space of facets.** The papers systematize the construct within their own framings rather than with a shared scheme. In the intervention framing, it is broken into Order-free Error and Order Sensitivity, while in the modular-circuit framing it is defined over a directed connection such as S1→S2 and whether the combined function is a logical composition of the component functions. Across papers, the same name is applied to multitask weight composition, non-interfering intervention composition, and logical composition across modular circuits.

**Space of measurement.** No measurement instrument and no behavioral indicator are linked to it. Instead, papers operationalize it directly with procedures that mirror their definitions: combining weights from models trained on distinct tasks to test multitasking without additional adaptation, using Order-free Error and Order Sensitivity for intervention non-interference, or computing a mutual-information formulation, Composability_T(S1→S2) = MI(S1(d), S2(S1(d))), for modular circuits.

**Links.** It is linked to one construct, General ability, through a related relationship. One paper reports that Composability is related to General ability, noting a disparity between overall utility and composability metrics and calling for evaluations that explicitly target composability; no causal or correlational links are reported.

## Sources

**Composability** (3 papers: [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf), [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf), [Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25x/he25x.pdf))
> The ability to combine model parameters or components trained on distinct tasks to create new, multitask capabilities without requiring additional training.

## Relationships

### Associated with
- **General ability** (construct), 1 paper
  > The disparity between overall utility and composability metrics underscores the need for more nuanced evaluations explicitly targeting composability as a design criterion. (Section 4.4)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
