# HTML understanding
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** HTML comprehension, Structural awareness  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats HTML understanding as an ability, often a latent one, to comprehend the structure and semantics of HTML documents or elements. The more common HTML-specific definitions add adjacent aspects: some include content and say this understanding informs actions, while others include the functionality of elements. A smaller framing broadens the construct to structural awareness, the ability to comprehend and use hierarchical and semantic information in document structures such as HTML tags to improve representation quality.

**Space of facets.** Papers mostly use HTML comprehension and HTML understanding for closely similar ideas centered on structure and semantics in HTML. A smaller line of work uses the broader label structural awareness for a wider scope, shifting from individual HTML documents and elements to hierarchical document structure and its use in representation learning. In the quoted passages, the construct is also discussed as something instruction-finetuning can improve, and as a requirement in conditional program synthesis where models must follow natural-language instructions while understanding the semantics and functionality of HTML elements.

**Space of measurement.** The measurement space is narrow: papers link the construct to one measurement instrument, WebSRC, and to no behavioral indicators. WebSRC is described as a static HTML comprehension benchmark, so operationalization takes the form of benchmark performance on static HTML comprehension tasks. This operationalization matches the dominant definitions' focus on understanding HTML structure and semantics.

**Links.** The only explicit relationship claim is measurement: a paper says HTML understanding is measured by WebSRC, described there as a static HTML comprehension benchmark. No recorded relationships report that it causes another construct, correlates with one, or is otherwise related to one.

## Sources

**HTML comprehension** (1 paper: [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf))
> The ability to understand the structure, semantics, and content of HTML documents to inform actions.

**HTML understanding** (1 paper: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf))
> The latent ability to comprehend the structure, semantics, and functionality of elements within an HTML document.

**Structural awareness** (1 paper: [SEAL: Structure and Element Aware Learning Improves Long Structured Document Retrieval](https://aclanthology.org/2025.emnlp-main.429.pdf))
> The model's latent ability to comprehend and utilize the hierarchical and semantic information embedded in document structures, such as HTML tags, to improve representation quality.

## Relationships

### HTML understanding →
- **WebSRC** (measurement instrument): *measured_by*, 1 paper
  > In Appendix F, we also test WebAgent on WebSRC (Chen et al., 2021b), a static HTML comprehension benchmark (Section 4).
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
