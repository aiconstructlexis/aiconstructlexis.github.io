# Fidelity
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Image fidelity, Visual quality, Image quality  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats fidelity as a quality property of generated outputs, especially images: realism, high quality, clarity, and freedom from artifacts or unintended distortions. Nearby formulations call this image fidelity, visual quality, or image quality, and one paper lists it alongside Overall and Alignment as an evaluation aspect. A smaller line of work uses the same name for different reference standards: in Sparse Autoencoders for Hypothesis Generation, fidelity is how accurately a natural-language concept matches a neuron's firing behavior through precision and recall, while another paper uses fidelity for preserving the semantic information of original watermarked text, described as the similarity between transformed and original text.

**Space of facets.** Rather than a single shared taxonomy, papers mostly position fidelity through overlapping quality labels. Visual quality is defined as aesthetic appeal, fidelity, and clarity in one use, and elsewhere as clarity, resolution, brightness, color, and absence of artifacts; in chart generation, visual quality is also tied to readability, layout, scales, ticks, and the clarity of titles and labels. In other settings, fidelity is contrasted with efficacy, where efficacy concerns minimizing watermark patterns and fidelity concerns preserving semantic information, or treated as distinct from Overall and Alignment.

**Space of measurement.** Papers link fidelity to 1 measurement instrument and 1 behavioral indicator. The only named instrument is the VisEval benchmark, used with a VLM Score metric to assess the visual quality of generated charts, and the only linked behavioral indicator is citation generation. Other operationalizations follow the local framing: one paper uses preference across Overall, Alignment, and Fidelity, another reports FID and aesthetic scores for image quality, and Sparse Autoencoders for Hypothesis Generation measures interpretation fidelity as 1 minus the minimum of recall and precision against neuron firing behavior.

**Links.** Beyond measurement, one paper claims a causal relationship from citation generation to fidelity, reporting that responses with citation can boost both model performance and fidelity; this claim appears in L-CiteEval. No correlations or non-causal related links are reported, and no construct-to-construct links are recorded.

## Sources

**Fidelity** (4 papers: [Neural Residual Diffusion Models for Deep Scalable Vision Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d51ceadaf09a4699f18986702df24987-Paper-Conference.pdf), [Sparse Autoencoders for Hypothesis Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/movva25a/movva25a.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [B4: A Black-Box Scrubbing Attack on LLM Watermarks](https://aclanthology.org/2025.naacl-long.460.pdf))
> The degree to which generated outputs are realistic, high-quality, and free from artifacts.

**Image fidelity** (1 paper: [Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf))
> The degree to which a generated image is realistic, high-quality, and free from artifacts or unintended distortions.

**Visual quality** (3 papers: [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf), [Reliable and Cost-Effective Exploratory Data Analysis via Graph-Guided RAG](https://aclanthology.org/2025.emnlp-main.836.pdf), [GenAI Arena: An Open Evaluation Platform for Generative Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/92249f9233286e437f808fa535d88b26-Paper-Datasets_and_Benchmarks_Track.pdf))
> The overall aesthetic appeal, fidelity, and clarity of the generated image.

**Image quality** (1 paper: [ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment](https://aclanthology.org/2025.emnlp-main.617.pdf))
> A general assessment of the generated image's technical and visual excellence, including aspects like realism and lack of artifacts.

## Relationships

### Fidelity →
- **VisEval** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the visual quality of the generated charts, we conducted an analysis using the VLM Score metric on the VisEval benchmark with k = 15. (Section 4.6)
  - [Reliable and Cost-Effective Exploratory Data Analysis via Graph-Guided RAG](https://aclanthology.org/2025.emnlp-main.836.pdf)

### → Fidelity
- **Citation generation** (behavioral indicator): *causes*, 1 paper
  > we can find that model response with citation can boost both the model performance and its fidelity. (Section 5.2)
  - [L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models](https://aclanthology.org/2025.acl-long.263.pdf)
