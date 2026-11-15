# Cultural understanding
**Type:** Construct  
**Supporting papers:** 30  
**Also known as:** Cultural awareness, Local cultural reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats cultural understanding as a latent model ability to comprehend, interpret, or reason about culturally specific knowledge, norms, values, and context, usually with reference to a particular audience, language community, or national setting. Most definitions keep this broad, covering shared cultural references, social norms, and context, while narrower variants tie it to specific domains such as regional cuisines, proverbs, or narrative clues. A smaller line of work uses nearby labels differently: cultural awareness is defined either as navigating social interactions in line with a culture's norms or as recognizing and incorporating culturally specific information rather than producing culturally generic or Western-centric outputs, and local cultural reasoning narrows the construct to causal reasoning within a specific cultural sphere.

**Space of facets.** Papers organize the construct mostly by the kinds of culturally grounded content it covers: some stress shared references and beliefs, others foreground social norms and interactions, and many instantiate it through local knowledge domains such as history, art, laws, festivals, or cuisines. Several definitions make it explicitly local, including dialects and region-specific socio-political structures, while one benchmark describes assessment in terms of perception, inference, and cultural alignment. The terminology is not fully uniform, because closely related work uses cultural understanding, cultural awareness, and local cultural reasoning for overlapping but not identical targets, and one line contrasts deeper contextual synthesis with surface-level detail use.

**Space of measurement.** Operationalization is entirely instrument-based in the linked literature, with 4 measurement instruments and no linked behavioral indicators. The most frequently linked instruments are the benchmarks CVQA, COPAL-ID, and DRISHTIKON, which are used to assess reasoning about culturally diverse visual content, the Indonesian cultural sphere, or culturally grounded Indian content; another instrument, LITRANSPROQA, places cultural understanding inside literary quality assessment and integrates humans in the loop around this dimension. Most linked instruments therefore operationalize the construct through benchmark tasks about culturally grounded reasoning and understanding, while narrower instruments target local-culture reasoning or literary translation quality.

**Links.** Beyond measurement, papers connect cultural understanding to 2 other constructs, and both links are framed as relatedness rather than causation or correlation. One paper relates cultural bias to cultural understanding, saying that tackling cultural bias requires an LLM to acknowledge cultural differences, and another relates cultural knowledge to cultural understanding through cultural awareness that leverages cultural knowledge to detect inappropriate interactions.

## Sources

**Cultural understanding** (8 papers: [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e297fb6cd1690ee5b39c5bb4c58ad801-Paper-Datasets_and_Benchmarks_Track.pdf), [JAWAHER: A Multidialectal Dataset of Arabic Proverbs for LLM Benchmarking](https://aclanthology.org/2025.naacl-long.613.pdf), [PerCul: A Story-Driven Cultural Evaluation of LLMs in Persian](https://aclanthology.org/2025.naacl-long.631.pdf), [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf), [WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://aclanthology.org/2025.naacl-long.167.pdf), [ITALIC: An Italian Culture-Aware Natural Language Benchmark](https://aclanthology.org/2025.naacl-long.68.pdf), [JMMMU: A Japanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.43.pdf), [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf))
> The ability to comprehend and reference shared cultural knowledge, norms, or contexts relevant to a specific audience.

**Cultural awareness** (2 papers: [LLM-Human Pipeline for Cultural Grounding of Conversations](https://aclanthology.org/2025.naacl-long.48.pdf), [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.152.pdf))
> The latent ability to understand and navigate social interactions in a manner that is consistent with the social norms of a specific culture.

**Local cultural reasoning** (1 paper: [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf))
> The ability to perform causal reasoning within specific cultural contexts, including understanding local dialects and social norms.

## Relationships

### Cultural understanding →
- **CVQA** (measurement instrument): *measured_by*, 2 papers
  > This benchmark can serve as a probing evaluation suite for assessing the cultural capability and bias of multimodal models and hopefully encourage more research efforts toward increasing cultural awareness and linguistic diversity in this field. (Abstract)
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
- **LITRANSPROQA** (measurement instrument): *measured_by*, 1 paper
  > LITRANSPROQA integrates humans in the loop to incorporate insights from professional literary translators and researchers, focusing on critical elements in literary quality assessment such as literary devices, cultural understanding, and authorial voice. (Abstract)
  - [LiTransProQA: An LLM-based Literary Translation Evaluation Metric with Professional Question Answering](https://aclanthology.org/2025.emnlp-main.1482.pdf)
- **DRISHTIKON** (measurement instrument): *measured_by*, 1 paper
  > We introduce DRISHTIKON, a first-of-its-kind multimodal and multilingual benchmark centered exclusively on Indian culture, designed to evaluate the cultural understanding of generative AI systems. (Abstract)
  - [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf)
- **COPAL-ID** (measurement instrument): *measured_by*, 1 paper
  > We evaluate both TransWebLLM and TransWebLLM-web on this benchmark in a 5-shot setting to assess their ability to reason within the Indonesian cultural sphere. (Section 5.2.1)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)

### Associated with
- **Cultural bias** (construct), 1 paper
  > Tackling cultural bias necessitates that a large language model (LLM) acknowledges cultural differences. (Section 1)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **Cultural knowledge** (construct), 1 paper
  > Cultural Awareness, which leverages cultural knowledge to detect inappropriate interactions.
  - [SocialCC: Interactive Evaluation for Cultural Competence in Language Agents](https://aclanthology.org/2025.acl-long.1594.pdf)
