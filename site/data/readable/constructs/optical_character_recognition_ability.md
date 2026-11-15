# Optical character recognition ability
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** OCR ability, OCR capability, Fine-grained text recognition, OCR perception, OCR recognition, Character recognition  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this construct as a latent ability to recognize text in visual input, usually to read, identify, transcribe, or extract it from images or documents. Several papers use closely aligned OCR labels for this broad framing, and one quoted passage describes better OCR recognition as accurately distinguishing confusing handwritten cases. A smaller line of work narrows the construct to recognizing text in document images and aligning it with query terms or document content, while another narrows it to fine-grained text recognition for small, blurred, or text-dense content. Some authors also use character recognition for identifying digits or characters from visual input, so the main variation is in scope: broad text recognition, document text alignment, fine-grained text reading, or digit and character recognition.

**Space of facets.** Papers organize this construct with several nearby labels, including OCR ability, OCR capability, OCR perception, OCR recognition, fine-grained text recognition, and character recognition. Some treat OCR as a facet of visual perception, and one benchmark places it alongside fine-grained and spatial perception as separate perception tasks. Other papers use narrower names for particular cases, especially fine-grained text recognition for difficult small or dense text, and character recognition for digit or character identification, including handwritten or natural-image digits.

**Space of measurement.** Operationalization is entirely benchmark-based: papers link the construct to 3 measurement instruments, namely MNIST, SVHN, and TextVQA, and no behavioral indicators are linked to it. TextVQA is explicitly used "for OCR abilities," while MNIST and SVHN appear under counting and character recognition, assessing the ability to identify digits within images. These measurements largely match the recognition-centered definitions, but the document-query alignment framing and the fine-grained small or blurred text framing are not tied to separate instruments here.

## Sources

**OCR ability** (1 paper: [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf))
> The latent capacity to recognize and extract text from images or documents.

**OCR capability** (1 paper: [ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf))
> The latent ability to recognize and align text present in document images with query terms or document content.

**Fine-grained text recognition** (1 paper: [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf))
> The latent ability to read and interpret small, blurred, or text-dense visual content in images.

**OCR perception** (1 paper: [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf))
> The specific facet of visual perception involving the detection and recognition of text characters within an image.

**OCR recognition** (1 paper: [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf))
> The ability to accurately identify, read, and transcribe text present within an image.

**Character recognition** (2 papers: [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf), [Sketch2Diagram: Generating Vector Diagrams from Hand-Drawn Sketches](https://proceedings.iclr.cc/paper_files/paper/2025/file/2567c95fd41459a98a73ba893775d22a-Paper-Conference.pdf))
> The ability to identify digits or characters from visual input, including handwritten or natural-image digit recognition.

## Relationships

### Optical character recognition ability →
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > TextVQA (Singh et al., 2019) for OCR abilities
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **MNIST** (measurement instrument): *measured_by*, 1 paper
  > Counting and Character Recognition: Assessing the models' ability to identify digits and count objects within images, a fundamental skill for quantitative understanding. ... including decades old benchmarks such as MNIST and SVHN [LeCun et al., 1998, Netzer et al., 2011].
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SVHN** (measurement instrument): *measured_by*, 1 paper
  > Counting and Character Recognition: Assessing the models' ability to identify digits and count objects within images, a fundamental skill for quantitative understanding. ... including decades old benchmarks such as MNIST and SVHN [LeCun et al., 1998, Netzer et al., 2011].
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
