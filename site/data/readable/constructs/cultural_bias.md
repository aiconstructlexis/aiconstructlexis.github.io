# Cultural bias
**Type:** Construct  
**Supporting papers:** 14  
**Also known as:** Western bias, Culture bias  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage describes cultural bias as a tendency for models or their generations to favor some cultural perspectives, symbols, or knowledge over others, most often with Western or U.S. content on the favored side. Several definitions also frame it through stereotyped associations or templated outputs for less prevalent cultures, with examples drawn from narrative traits, settings, and food knowledge. A narrower line uses the label "Western bias" for an error disparity in vision-language models, defined as better performance on Western than East Asian images and annotations, so the main disagreement is whether the construct is a broad tendency in outputs and knowledge or a task-level performance gap.

**Space of facets.** Papers use the construct across several task-specific forms, including culture-conditioned generations, food-related cultural knowledge, children's story generation, image understanding, and the use of measurement systems or factual representations associated with dominant cultural contexts. The narrower term "Western bias" is reserved for the Western versus East Asian comparison in vision tasks, while "cultural bias" is used more broadly for uneven cultural representation or understanding. In the recorded relationships, the construct is also placed near neighboring ideas rather than equated with them, being related to cultural alignment, cultural understanding, and visual understanding.

**Space of measurement.** Papers link cultural bias to 3 instruments and 1 behavioral indicator. Measurement is recorded mainly through question answering evaluations, especially CVQA and A-OKVQA: one paper says these are used "to measure Western bias in question answering," and CVQA is also described as "a probing evaluation suite for assessing the cultural capability and bias of multimodal models." The remaining linked instrument is the World Values Survey, but only as related rather than as a recorded measure, and the lone behavioral indicator is text generation; overall, the operationalizations foreground performance disparities in question answering and multimodal evaluation, while several definitions describe bias in open-ended generations and stereotyped associations.

**Links.** Beyond measurement, papers record related links to 3 constructs and 1 behavioral indicator. Cultural bias is related to cultural understanding, with one paper stating that tackling it requires an LLM to acknowledge cultural differences; it is also related to visual understanding, cultural alignment, text generation, and the World Values Survey. The recorded links are relational rather than causal or correlational: one paper discusses Western bias in image understanding, another connects prior probing of cultural alignment to Western bias in encoded world knowledge and values, and another situates cultural bias in open-ended generative tasks such as narrative writing or dialogue.

## Sources

**Western bias** (1 paper: [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf))
> A performance disparity where a vision-language model performs better on tasks involving images and annotations from Western cultures compared to those from East Asian cultures.

**Cultural bias** (3 papers: [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf), [Does Mapo Tofu Contain Coffee? Probing LLMs for Food-related Cultural Knowledge](https://aclanthology.org/2025.naacl-long.496.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf))
> A tendency for model generations to reflect uneven or stereotyped cultural associations, especially favoring some cultures or culturally salient symbols over others.

## Relationships

### Cultural bias →
- **CVQA** (measurement instrument): *measured_by*, 2 papers
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)

### Associated with
- **Cultural understanding** (construct), 1 paper
  > Tackling cultural bias necessitates that a large language model (LLM) acknowledges cultural differences. (Section 1)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **Visual understanding** (construct), 1 paper
  > In this work, we characterize the Western bias of VLMs in image understanding and investigate the role that language plays in this disparity. (Section 1)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Cultural alignment** (construct), 1 paper
  > “In the language only setting, prior work has probed models for such cultural alignment, finding that they exhibit a Western bias in the world knowledge (Naous et al., 2023) and values (AlKhamissi et al., 2024) they encode.”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > "In open-ended generative tasks like narrative writing or dialogue, large language models often exhibit cultural biases"
  - [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf)
- **World Values Survey** (measurement instrument), 1 paper
  > Insights from the WVS can help in understanding the cultural and societal norms that underlie biases
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
