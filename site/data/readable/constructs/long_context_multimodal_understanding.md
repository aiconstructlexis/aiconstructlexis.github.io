# Long-context multimodal understanding
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Long multimodal document comprehension, Long image-sequence understanding, Long-context visual processing, Long-document understanding, Long-range modeling  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is broad: a latent model ability to process, comprehend, and use very long multimodal contexts, often interleaving visual and textual inputs. Most definitions focus on understanding extended sequences or documents and, in several cases, on integrating information for reasoning or question answering. A smaller line of work narrows the construct to vision-heavy settings, either extended image sequences or many visual inputs presented at once, while another framing emphasizes maintaining coherent understanding and performance over long multimodal sequences. The main disagreement is over scope and modality emphasis, from broad interleaved multimodal reasoning to document-centric, video-centric, or vision-centric processing.

**Space of facets.** Papers use several labels around this construct: long-context multimodal understanding, long multimodal document comprehension, long image-sequence understanding, long-context visual processing, long-document understanding, and long-range modeling. These labels sort the space mostly by input regime, interleaved video-language streams, multi-image sequences, or long visually rich documents with text, tables, charts, and images, and by task emphasis, from general understanding and reasoning to answering questions over long documents or maintaining performance across long sequences. A vision-centric formulation also separates raw capacity to process many visual tokens from effective retrieval and reasoning.

**Space of measurement.** Papers operationalize it through benchmarks rather than behavioral indicators. They link the construct to 3 measurement instruments and no behavioral indicators: MM-NIAH, LongVideoBench, and MileBench. MM-NIAH is described as a benchmark for comprehending long multimodal documents and for detecting image and text needles in hybrid long contexts; LongVideoBench is a question-answering benchmark with interleaved video and subtitles up to an hour long, designed to evaluate long-term multimodal understanding; MileBench is described as progressively challenging multi-image tasks that quantify long-context capability from textual-token and visual-token perspectives. These instruments mirror the definitional spread between long documents, interleaved video-language inputs, and broader long visual contexts.

**Links.** No causal, correlational, or generic related links are reported beyond these measurement links.

## Sources

**Long-context multimodal understanding** (1 paper: [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of a model to process and comprehend long sequences of interleaved multimodal inputs, such as video frames and text subtitles, to perform complex reasoning tasks.

**Long multimodal document comprehension** (1 paper: [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent ability of a model to understand, integrate, and reason about information from long documents containing interleaved text and images.

**Long image-sequence understanding** (1 paper: [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf))
> The model's latent ability to process and comprehend information from extended sequences of images, such as those found in lengthy videos or multi-image documents.

**Long-context visual processing** (1 paper: [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf))
> The ability of a model to effectively process and utilize information from a large number of visual inputs presented simultaneously in its context window.

**Long-document understanding** (1 paper: [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf))
> The latent ability to comprehend and answer questions about lengthy, multi-page documents containing mixed modalities such as text, tables, charts, and images.

**Long-range modeling** (1 paper: [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf))
> The latent ability of a VLM to maintain coherent understanding and performance across extended sequences of multimodal inputs, particularly over long videos or interleaved images.

## Relationships

### Long-context multimodal understanding →
- **MM-NIAH** (measurement instrument): *measured_by*, 2 papers
  > In this work, we present Needle In A Multimodal Haystack (MM-NIAH), the first benchmark specifically designed to systematically evaluate the capability of existing MLLMs to comprehend long multimodal documents. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **LongVideoBench** (measurement instrument): *measured_by*, 1 paper
  > To mitigate this gap, we introduce LONGVIDEOBENCH, a question-answering benchmark that features video-language interleaved inputs up to an hour long. Our benchmark includes 3,763 varying-length web-collected videos with their subtitles across diverse themes, designed to comprehensively evaluate LMMs on long-term multimodal understanding. (Abstract)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MileBench** (measurement instrument): *measured_by*, 1 paper
  > And MileBench (Song et al., 2024) progressively challenging tasks with 2-109 images. These benchmarks systematically quantify long-context capabilities from both textual token and visual token perspectives. (Section 4.4)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
