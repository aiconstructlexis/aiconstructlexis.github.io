# Interleaved text-and-image generation
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Interleaved image-text generation, Interleaved document generation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as generating a sequence or document that contains both text and images, most commonly in an autoregressive form. Most descriptions also require coherence in the combined output, variously as a single coherent document, alternating image-text content, or contextually and narratively consistent continuation. A smaller line of work states it more broadly as producing an arbitrary sequence of text segments and images, while another frames it as generating interleaved documents in a coherent, free-form layout.

**Variants.** Papers use several near-equivalent names, most often interleaved image-text generation, alongside interleaved text-and-image generation and interleaved document generation. The settings range from long-form content with alternating text and images to raw or free-form interleaved documents, and some papers study story continuation from mixed-modality inputs, including an initial image-text pair followed by the instruction "Please continue this story."

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead describe it through generation setups such as end-to-end interleaved text-image modeling, instruction tuning tailored to interleaved generation, and continuation from mixed-modality inputs.

**What it is taken as evidence of.** No paper links it to a construct, so the papers do not specify what construct this behavior is taken to reflect. Separately, one paper claims a causal relationship from interleaved text-and-image generation to the behavioral indicator Visual storytelling, saying it "opens up possibilities" for that application.

## Sources

**Interleaved text-and-image generation** (1 paper: [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf))
> The task of producing an arbitrary sequence containing both text segments and images.

**Interleaved image-text generation** (3 papers: [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf), [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf))
> The observable task of generating a sequence containing both text and images in an autoregressive manner.

**Interleaved document generation** (1 paper: [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf))
> The task of generating documents that contain a mix of text and images in a coherent, free-form layout.

## Relationships

### Interleaved text-and-image generation →
- **Visual storytelling** (behavioral indicator): *causes*, 1 paper
  > It opens up possibilities for various complex applications, such as multi-step inference (Lu et al., 2024; Kazemi et al., 2024), multimodal situational analysis (Yang et al., 2021), and visual storytelling (Huang et al., 2016). (Section 1)
  - [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf)
