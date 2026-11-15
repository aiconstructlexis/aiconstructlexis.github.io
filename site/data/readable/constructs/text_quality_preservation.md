# Text quality preservation
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Fluency preservation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as a latent property or ability of a method to preserve output quality when generation is modified. Most definitions center on maintaining fluency and coherence, whether under strong attribute biasing in controlled generation or under the injection of hidden watermark patterns, and one formulation makes the narrower quality target explicit as keeping text natural, coherent, and grammatically correct. A smaller broadening of the concept extends beyond surface text quality to include functional utility, framing preservation as keeping downstream performance from being degraded.

**Space of facets.** Papers do not present a detailed subtype scheme, but they do use two closely overlapping names, "fluency preservation" and "text quality preservation", for related ideas. The main variation is in scope: some authors use it for surface properties of the text, especially fluency, coherence, and grammatical correctness, while others fold in preservation of the model's broader utility, including its "essential abilities for downstream tasks" and comparable performance on summarization and translation.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. Even so, the papers operationalize it through observed retention of quality, including little cost in perplexity, reports that fluency is "not affected," similarity between watermarked and non-watermarked text quality, and comparable downstream task performance; as one paper puts it, "this fine-grained control comes at very little cost with respect to perplexity" (Controlled Text Generation via Language Model Arithmetic). Another paper treats preservation as consistent performance on summarization and translation while still supporting message embedding and extraction (BiMark: Unbiased Multilayer Watermarking for Large Language Models).

## Sources

**Fluency preservation** (1 paper: [Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf))
> The latent property of a controlled generation method to maintain natural, coherent, and grammatically correct text even under strong attribute biasing.

**Text quality preservation** (2 papers: [Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/abdc8c031aa6c6917c3b593166e5e340-Paper-Conference.pdf), [BiMark: Unbiased Multilayer Watermarking for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25u/feng25u.pdf))
> The latent ability of a watermarking method to maintain the fluency and coherence of generated text despite the injection of hidden patterns.
