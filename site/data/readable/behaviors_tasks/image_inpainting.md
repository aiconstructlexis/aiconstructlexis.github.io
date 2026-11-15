# Image inpainting
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Image in-painting, Image infilling, Generative fill  

## State of the Field

**Space of definitions.** Across definitions, the common core is filling missing, masked, or corrupted parts of an image. Authors differ in how the fill is conditioned: some describe using the visible parts of the image, others specify a textual instruction or in-context visual examples, and one definition makes success explicit as producing plausible, contextually appropriate content.

**Variants.** Papers use several nearby names, most commonly image inpainting or image in-painting, with smaller variants such as image infilling and generative fill. The behavior appears in both low-level and downstream settings, including zero-shot control settings, filling different pixel-space masks, and completing the missing half of an example; examples are shown on CelebA-HQ, SVHN, MNIST, and CIFAR-10.

**Space of elicitation and scores.** No measurement instrument is linked to it. Elicitation is described procedurally by masking part of an image and having the model generate within that region, in one paper by teacher-forcing ground-truth tokens outside the mask and generating only inside it, and in another by asking for the missing half of an example; no separate scoring instrument is named.

**What it is taken as evidence of.** Only one construct is linked. Papers relate image in-painting to Zero-shot generalization: one paper presents it as a downstream task through which a model showcases zero-shot generalization ability, and no other construct link is recorded.

## Sources

**Image inpainting** (1 paper: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf))
> The task of filling in missing or corrupted parts of an image based on a textual instruction.

**Image in-painting** (1 paper: [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf))
> The task of filling in a missing or masked region within an image with plausible, contextually appropriate content.

**Image infilling** (1 paper: [Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf))
> The task of generating pixels to fill in a masked or missing region of an image based on the visible parts.

**Generative fill** (1 paper: [Can Generative AI Solve Your In-Context Learning Problem? A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf))
> Completing missing parts of an image based on in-context visual examples.

## Relationships

### Associated with
- **Zero-shot generalization** (construct), 1 paper
  > VAR further showcases zero-shot generalization ability in downstream tasks including image in-painting, out-painting, and editing.
  - [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf)
