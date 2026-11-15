# Video generation
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Text-to-video generation, Image-to-video generation, Impossible video generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats video generation as synthesizing a sequence of coherent video frames or realistic video sequences. Most commonly, papers frame it as generation conditioned on an input such as a text prompt, a class label, previous frames, or, in some work, a static image, though some definitions also allow unconditional generation. Success is described in terms such as coherence and realism, and some papers further emphasize spatial and temporal coherence with the input description, desired attributes and motion patterns, semantic faithfulness to captions, or fidelity to the prompt and visual quality.

**Variants.** Most papers study text-to-video generation, described as generating a novel video sequence or video clip from a textual description or caption. Smaller lines of work separate image-to-video generation from a static input image, class-conditional generation, and frame prediction with a 5-frame condition. A more specialized variant is impossible video generation, where the prompt asks for scenes that violate physical, biological, geographical, or social laws while the model is still expected to follow the prompt.

**Space of elicitation and scores.** Papers link video generation to three measurement instruments. The most frequently linked instrument is VBench, which papers use for evaluating video generation capability and for GPT-augmented prompts in the video generation domain; MSR-VTT and UCF-101 are also used, described as common datasets for video generation experiments, with MSR-VTT also appearing in text-to-video evaluation. Across these links, the instruments are treated as a mix of a benchmark and datasets.

**What it is taken as evidence of.** These papers do not link video generation to any construct, so they do not explicitly use it as evidence of a construct.

## Sources

**Video generation** (4 papers: [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf), [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf), [Neural Residual Diffusion Models for Deep Scalable Vision Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d51ceadaf09a4699f18986702df24987-Paper-Conference.pdf), [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf))
> Generating coherent and realistic video sequences, either conditioned on class labels or previous frames.

**Text-to-video generation** (4 papers: [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf), [MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf), [Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf), [HAIC: Improving Human Action Understanding and Generation with Better Captions for Multi-modal Large Language Models](https://aclanthology.org/2025.acl-long.501.pdf))
> Creating dynamic video content from textual prompts.

**Image-to-video generation** (1 paper: [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf))
> Creating dynamic video content based on a static input image.

**Impossible video generation** (1 paper: [Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf))
> The observable act of producing a video that depicts a scene violating real-world physical, biological, geographical, or social laws, as prompted by a text description.

## Relationships

### Video generation →
- **VBench** (measurement instrument): *measured_by*, 3 papers
  > To evaluate the visual generation capability, we use... VBench (Huang et al., 2024) for video generation. (Section 4.1)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf)
  - [Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf)
- **UCF-101** (measurement instrument): *measured_by*, 2 papers
  > We use Kinetics-600 (K600) and UCF-101 (Soomro et al., 2012) for video generation experiments (Section 4.1).
  - [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf)
  - [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)
- **MSR-VTT** (measurement instrument): *measured_by*, 2 papers
  > "We also evaluate LVD on common datasets such as UCF-101 (Soomro et al., 2012) and MSR-VTT (Xu et al., 2016)"
  - [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
