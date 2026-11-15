# GenEval
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, the prevailing framing treats GenEval as a benchmark for whether a model can generate an image that is an accurate depiction of a prompt. Most descriptions emphasize prompt accuracy directly, calling it "a benchmark that examines a model's ability to generate an accurate depiction of the prompt," while one paper instead describes it as a metric of generated image quality and text alignment, based on human preferences and semantic accuracy.

**What it is claimed to measure.** Papers use GenEval most often to measure Visual generation ability, with evaluation quoted passages tying it to visual or text-to-image generation capabilities. A smaller line of work uses it to measure Prompt understanding, with one study saying gains on GenEval reflect enhanced prompt-following capabilities, and it is also reported as measuring the behavioral indicator Image generation. Across papers, it is linked to two constructs and one behavioral indicator, with the claims concentrated on visual generation and a smaller extension to prompt understanding.

**Space of uses.** Papers use GenEval when reporting benchmark scores and model comparisons for image or visual generation. Although no measurement instrument is formally linked to it, some papers use it alongside MS-COCO, DSG, or MME-P, and one paper contrasts it with using only CLIP score.

## Sources

**GenEval** (2 papers: [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/12678c3948153f4bc391f51e2082bd6e-Paper-Conference.pdf), [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf))
> A benchmark designed to evaluate a model's ability to generate an image that is an accurate depiction of a given prompt.

## Relationships

### → GenEval
- **Visual generation ability** (construct): *measured_by*, 3 papers
  > “we follow SD3 (Esser et al., 2024) to evaluate the text-to-image generation capabilities of Show-o on the GenEval (Ghosh et al., 2023) benchmark.”
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Prompt understanding** (construct): *measured_by*, 1 paper
  > Synthetic captions lead to significant improvements on the GenEval benchmark (Ghosh et al., 2024), as shown in Table 6, highlighting the advantage of enhanced prompt-following capabilities. (Section 4.3)
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Image generation** (behavioral indicator): *measured_by*, 1 paper
  > we report results on more comprehensive benchmarks instead of only CLIP score, such as GenEval (Ghosh et al., 2024) and DSG (Cho et al., 2024). (Section 4.3)
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
