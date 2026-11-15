# Multimodal integration
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Cross-modal fusion, Cross-modal integration, Multimodal fusion, Multi-modal fusion  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as a latent or internal model capability to combine, fuse, or integrate information from multiple modalities and reason over the result to form a coherent or unified understanding. Most definitions also tie that capability to downstream reasoning, generation, or task performance, while a smaller line of work narrows the emphasis to preserving semantic and structural correspondences between modalities, or to coordinated use of textual and visual inputs for accurate medical interpretations. The scope of modalities varies across papers, from audio, video, and text to text and images or medical text and images, but the shared framing is effective combination and use of more than one modality.

**Space of facets.** Papers use several near-overlapping names for this construct, including multimodal integration, cross-modal fusion, cross-modal integration, multimodal fusion, and multi-modal fusion, with a shared core around combining information from different modalities. The main variation is which facet is foregrounded: some definitions emphasize coordinated reasoning across modalities, some emphasize semantic and structural correspondences, and some describe it through internal processing sites such as pre-fusion operations, modality fusion layers, or cross-modal attention and feature alignment. Quoted passages also localize it differently, for example in middle layers where cross-attention focuses on instruction-relevant or semantically critical regions.

**Space of measurement.** No measurement instrument is linked to this construct, and no behavioral indicator is linked to it. Instead, the quoted passages discuss it through architectural manipulations and resulting task outcomes, such as adding pre-fusion operations, using a modality fusion layer, masking cross-attention and observing performance deterioration, or comparing a baseline with access to both modalities against conditions that remove one modality. Several quoted passages also describe failures in these terms, such as underutilization of acquired information or neglecting to integrate the visual data presented.

## Sources

**Multimodal integration** (2 papers: [AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25a/lian25a.pdf), [SHIFT: Selected Helpful Informative Frame for Video-guided Machine Translation](https://aclanthology.org/2025.emnlp-main.161.pdf))
> The model's latent capability to effectively fuse and reason over information from different modalities, such as audio, video, and text, to form a coherent understanding.

**Cross-modal fusion** (2 papers: [Graph4MM: Weaving Multimodal Learning with Structural Information](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ning25a/ning25a.pdf), [VisiPruner: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs](https://aclanthology.org/2025.emnlp-main.955.pdf))
> The latent ability to combine information from different modalities (e.g., text and vision) in a way that preserves and leverages their semantic and structural correspondences for downstream reasoning and generation.

**Cross-modal integration** (1 paper: [Who is in the Spotlight: The Hidden Bias Undermining Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.768.pdf))
> The latent ability of a model to effectively combine and reason over information from different modalities, such as text and images, in a coordinated manner.

**Multimodal fusion** (1 paper: [Can MLLMs Understand the Deep Implication Behind Chinese Images?](https://aclanthology.org/2025.acl-long.700.pdf))
> The model's internal capability to effectively integrate and process information from different modalities, such as text and images, to form a unified understanding.

**Multi-modal fusion** (1 paper: [Asclepius: A Spectrum Evaluation Benchmark for Medical Multi-Modal Large Language Models](https://aclanthology.org/2025.acl-long.1178.pdf))
> The latent ability to synthesize and reason over both textual and visual inputs in a coordinated way to produce accurate medical interpretations.
