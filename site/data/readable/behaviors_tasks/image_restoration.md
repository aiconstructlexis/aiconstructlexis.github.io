# Image restoration
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Blind restoration  

## State of the Field

**Space of definitions.** Across the papers, one common framing treats image restoration as recovering high-quality images from degraded observations through restoration algorithms. Another, narrower framing presents it as blind restoration, where a degraded image is restored without explicit instructions about the degradation type and instead relies on automatically generated analysis or auxiliary prompts; one description says users can input an image "without the need to provide instructions for its restoration."

**Variants.** The named variants are centered on blind restoration under different degradations. Papers explicitly study low-light enhancement, desnowing, and dehazing, and also mention blind restoration alongside combination tasks; separate work discusses image restoration for diverse degradations in real-world applications and relates it to downstream high-level vision tasks.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers, it is elicited through restoration tasks themselves, either by recovering degraded images in general or by blind restoration setups where auxiliary prompts are generated automatically and users do not provide explicit restoration instructions.

**What it is taken as evidence of.** Papers relate image restoration to Generalization and Zero-shot generalization. One paper discusses enhancing generalization ability to diverse degradations in real-world applications, while another reports superior zero-shot capabilities in blind restoration and combination tasks; both links are framed as related rather than as explicit claims that image restoration serves as evidence of either construct.

## Sources

**Blind restoration** (1 paper: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf))
> The task of restoring a degraded image without explicit instructions specifying the type of degradation, instead relying on an automatically generated analysis of the image.

**Image restoration** (1 paper: [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf))
> The process of recovering high-quality images from degraded observations by applying restoration algorithms.

## Relationships

### Associated with
- **Zero-shot generalization** (construct), 1 paper
  > Our proposed model also achieves comparable inference efficiency with these baseline models and exhibits superior zero-shot capabilities in blind restoration and combination tasks.
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Low-light image enhancement** (behavioral indicator), 1 paper
  > We evaluate the model’s performance on such blind restoration tasks, including low-light enhancement, desnowing, and dehazing.
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > Image Restoration (IR)... Recently, researchers have increasingly focused on enhancing the generalization ability to diverse degradations in real-world applications
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Object detection** (behavioral indicator), 1 paper
  > “we assess the benefits of image restoration for downstream high-level vision tasks by conducting detection and segmentation experiments on the COCO 2017 [45] and ADE20K [94] datasets”
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Semantic segmentation** (behavioral indicator), 1 paper
  > “we assess the benefits of image restoration for downstream high-level vision tasks by conducting detection and segmentation experiments on the COCO 2017 [45] and ADE20K [94] datasets”
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
