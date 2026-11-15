# VisDial
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Most definitions converge on treating VisDial as a Visual Dialog dataset or multi-turn visual dialogue benchmark centered on conversation about an image. Papers describe it as evaluating a model's ability to engage in a multi-turn conversation about an image, or to answer a series of questions about an image. A smaller framing presents it as a benchmark for chat-to-image acquisition, with experiments for image acquisition in multi-turn chat scenarios, and one source also places it within an ablation study across five datasets.

**What it is claimed to measure.** Papers link VisDial to one construct and two behavioral indicators. The construct-level use is to measure multimodal understanding, while the behavioral indicators most often attached to it are cross-modal retrieval and visual question answering. These claims are spread across several targets rather than restricted to a single one: one paper evaluates visual question answering on VisDial, another reports using the Visual Dialog dataset in cross-modal retrieval for comparability to previous work, and another includes VisDial when assessing multimodal vision and language capabilities.

**Space of uses.** Papers most often position VisDial as one dataset within broader evaluation setups rather than as a standalone instrument. It appears alongside several tasks when models are evaluated for multimodal vision and language capabilities, is used in an ablation study across five datasets, and is also used for comparability to previous work in cross-modal retrieval; no measurement instrument is linked to it.

## Sources

**VisDial** (3 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf))
> The Visual Dialog dataset, which evaluates a model's ability to engage in a multi-turn conversation about an image.

## Relationships

### → VisDial
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... visual question answering on ... VisDial (Das et al., 2017) (Section 3.2).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... VisDial (Das et al., 2017)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 1 paper
  > In cross-modal retrieval, we use the Visual Dialog (Das et al., 2017) dataset for the comparability to previous work (Koh et al., 2023).
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)
