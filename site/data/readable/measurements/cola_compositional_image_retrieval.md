# Cola (compositional image retrieval)
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** Cola, COLA  

## State of the Field

**What it is.** The prevailing usage treats Cola or COLA as a text-to-image retrieval benchmark for compositional ability or compositional reasoning: captions describe relations between entities, or specific configurations of attributes and objects, and the task is to retrieve the correct image from candidate images or from a database with distractor images. Definitions commonly emphasize composing objects with their relations or retrieving images with the correct attribute-object configuration. One quoted passage using the same name, COLA, refers instead to the Corpus of Linguistic Acceptability for linguistic acceptability, so papers do not use the label uniformly.

**What it is claimed to measure.** Across the papers that link it to other entities, Cola is used to measure compositional reasoning, and that is the only linked construct. No behavioral indicators are linked to it, so the reported measurement claims converge on compositional reasoning rather than spreading across multiple targets.

**Space of uses.** Papers use it as part of compositional evaluation. One paper describes an evaluation procedure that calculates perplexity between a caption and all candidate images and then selects the lower-perplexity image as the prediction, while another places Cola alongside older composition benchmarks such as Valse and Winoground for additional comparisons. No other measurement instruments are linked to it.

## Sources

**Cola** (2 papers: [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf))
> Text-to-image retrieval benchmark that assesses compositional ability by matching captions describing relations between entities to correct images.

**COLA** (2 papers: [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf), [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf))
> A benchmark that evaluates compositional reasoning by tasking a VLM with retrieving correct images based on specific configurations of attributes and objects from a database containing distractor images.

## Relationships

### → Cola (compositional image retrieval)
- **Compositional reasoning** (construct): *measured_by*, 2 papers
  > We first evaluate our CoVLM on compositional reasoning tasks, including... matching the correct captions describing the relation between two images with similar entities (Cola, (Ray et al., 2023))... (Section 4.1)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
