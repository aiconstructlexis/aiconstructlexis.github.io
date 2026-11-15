# Optical character recognition
**Type:** Behavioral indicator  
**Supporting papers:** 45  
**Also known as:** Text recognition, Scene text recognition, Element OCR, Heading OCR, OCR, Handwritten letter recognition, Reading text from images, Chart OCR, Handwritten text recognition, Printed text recognition, Text extraction from images, Text transcription, Document parsing, Text reading from images, OCR token recognition  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is reading, recognizing, extracting, or transcribing text that appears in visual inputs, most often images and documents, and sometimes screenshots or video frames. Most definitions treat the behavior as returning the visible text itself, including formulations about reading and outputting text from an image and extracting the full text from an image. Some authors narrow it to a specified region or element, while a smaller line broadens it to document parsing, where the task includes transcribing content or extracting structured information from dense layouts.

**Variants.** Variants are organized mainly by source type. Papers describe scene text recognition, webpage OCR focused on specific elements or headings, chart OCR, and document-focused forms such as text transcription or document parsing. Other work places the same behavior in video frames, slide images, handwritten letters, historical handwritten or printed documents, multilingual text-in-image settings, and cases involving small or embedded text.

**Space of elicitation and scores.** Papers link this behavior to 8 measurement instruments. It is measured most often by TextVQA, followed by DocVQA, OCRBench, ChartQA, and InfoVQA, among the instruments linked in papers. These instruments are usually described as OCR-related, document or chart understanding, or text-understanding benchmarks, including settings where models answer questions through textual cues on images.

**What it is taken as evidence of.** Construct links are mixed rather than aligned on a single target. Papers connect optical character recognition to 3 constructs: one paper claims a causal relationship from optical character recognition to GUI understanding, another claims a causal relationship from visual perception to optical character recognition, and another reports that optical character recognition is related to multimodal reasoning. Papers therefore do not consistently treat this behavior as evidence of one shared construct.

## Sources

**Optical character recognition** (3 papers: [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf), [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf), [Is Cognition Consistent with Perception? Assessing and Mitigating Multimodal Knowledge Conflicts in Document Understanding](https://aclanthology.org/2025.emnlp-main.1574.pdf))
> The task of identifying and extracting text from images or documents.

**Text recognition** (3 papers: [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf), [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf))
> Reading and transcribing text that appears in images or screenshots.

**Scene text recognition** (1 paper: [ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4fd96b997454b5b02698595df70fccaf-Paper-Conference.pdf))
> Recognizing and reading text within an image region, often treated as an out-of-domain task for referring models.

**Element OCR** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> Extracting the text content from a specific UI element highlighted by a bounding box on a webpage screenshot.

**Heading OCR** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> Identifying and extracting the textual content of headlines or titles from a webpage.

**OCR** (3 papers: [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf), [Taking Notes Brings Focus? Towards Multi-Turn Multimodal Dialogue Learning](https://aclanthology.org/2025.emnlp-main.1690.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf))
> The task of performing Optical Character Recognition to read and interpret text that appears within video frames.

**Handwritten letter recognition** (1 paper: [SCISSOR: Mitigating Semantic Bias through Cluster-Aware Siamese Networks for Robust Classification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25w/yang25w.pdf))
> The observable task of identifying and classifying characters from images of handwritten letters.

**Reading text from images** (1 paper: [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf))
> The observable behavior of extracting and understanding textual content embedded within an image to perform a task.

**Chart OCR** (1 paper: [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf))
> Extracting visible text elements from a chart without semantic structuring.

**Handwritten text recognition** (1 paper: [CHURRO: Making History Readable with an Open-Weight Large Vision-Language Model for High-Accuracy, Low-Cost Historical Text Recognition](https://aclanthology.org/2025.emnlp-main.1763.pdf))
> Transcribing text from images of handwritten historical documents, accounting for diverse handwriting styles, abbreviations, and degradation.

**Printed text recognition** (1 paper: [CHURRO: Making History Readable with an Open-Weight Large Vision-Language Model for High-Accuracy, Low-Cost Historical Text Recognition](https://aclanthology.org/2025.emnlp-main.1763.pdf))
> Transcribing text from images of printed historical documents, handling archaic fonts, layout variations, and orthographic inconsistencies.

**Text extraction from images** (2 papers: [Do Slides Help? Multi-modal Context for Automatic Transcription of Conference Talks](https://aclanthology.org/2025.emnlp-main.814.pdf), [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://aclanthology.org/2025.acl-long.736.pdf))
> The process of identifying and converting textual content from image frames of presentation slides into machine-readable text, using OCR or vision-language models.

**Text transcription** (1 paper: [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf))
> The task of accurately extracting and transcribing textual content from an image or document.

**Document parsing** (1 paper: [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf))
> The task of extracting structured information or transcribing content from document images, which often contain dense text and layouts.

**Text reading from images** (1 paper: [Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model](https://aclanthology.org/2025.acl-long.143.pdf))
> Recognizing and transcribing textual content visible within an image, especially in non-English languages and diverse scripts.

**OCR token recognition** (1 paper: [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf))
> Identifying and transcribing text from images, particularly small or embedded text, based on visual input and natural language queries.

## Relationships

### Optical character recognition →
- **TextVQA** (measurement instrument): *measured_by*, 8 papers
  > our strategy can effectively alleviate these issues, bringing substantial improvements on different benchmarks, especially in TextVQA with rich OCR information. (Section 4.3)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
  - [R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bc/li25bc.pdf)
  - [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 2 papers
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **OCRBench** (measurement instrument): *measured_by*, 2 papers
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **ST-VQA** (measurement instrument): *measured_by*, 1 paper
  > TextVQA and ST-VQA are two texts understanding benchmarks requiring models to answer questions through textual cues on images. (Section 5.1.1)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **InfoVQA** (measurement instrument): *measured_by*, 1 paper
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **VisualMRC** (measurement instrument): *measured_by*, 1 paper
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **GUI understanding** (construct): *causes*, 1 paper
  > OCR samples benefit most in GUI understanding.
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **ChartQA** (measurement instrument): *measured_by*, 1 paper
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **OCR-VQA** (measurement instrument): *measured_by*, 1 paper
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)

### → Optical character recognition
- **Visual perception** (construct): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)

### Associated with
- **Multimodal reasoning** (construct), 1 paper
  > We also show some multi-modal reasoning examples in Figure 6. Our approach exhibits better object counting, OCR, and commence reasoning performance. (Section 4.2)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
