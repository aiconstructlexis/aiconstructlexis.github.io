# MM-NIAH
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Papers most commonly describe MM-NIAH as a benchmark for long multimodal or mixed-modality contexts built around a needle-in-a-haystack setup. One line of work presents it as a mixed video-text retrieval benchmark, where 25% of the input is text segments inserted across frames and the model must locate relevant content, with tests reaching up to 4.5k frames, about 1.1M tokens. Another description is broader, framing it as a benchmark for long multimodal documents with interleaved text and images and tasks in retrieval, counting, and reasoning.

**What it is claimed to measure.** Papers link MM-NIAH to one behavioral indicator and two constructs. The prevailing uses are to measure Synthetic recall and Long-context multimodal understanding, with papers describing it as detecting image and text needles within hybrid long contexts and as evaluating the capability to comprehend long multimodal documents. A narrower link treats it as measuring Multimodal reasoning, in line with the benchmark's reasoning task alongside retrieval and counting.

**Space of uses.** In use, papers position MM-NIAH as an evaluation for mixed-modality or long-context multimodal scenarios, including settings where image and text needles are detected within hybrid long inputs. It is linked to one other instrument, BLINK, and a paper states that images from BLINK's Jigsaw and Multi-view reasoning splits are inserted into the document to serve as the image needle.

## Sources

**MM-NIAH** (2 papers: [MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aq/li25aq.pdf), [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf))
> Mixed-Modality Needle in a Haystack, a retrieval benchmark for mixed video-text inputs in which text segments are inserted across frames and the model must locate relevant content.

## Relationships

### → MM-NIAH
- **Synthetic recall** (behavioral indicator): *measured_by*, 2 papers
  > Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Long-context multimodal understanding** (construct): *measured_by*, 2 papers
  > In this work, we present Needle In A Multimodal Haystack (MM-NIAH), the first benchmark specifically designed to systematically evaluate the capability of existing MLLMs to comprehend long multimodal documents. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **BLINK** (measurement instrument), 1 paper
  > for each evaluation data, images sampled from the Jigsaw and Multi-view reasoning split of BLINK benchmark [26] are inserted into the document to serve as the image needle. (Section 3.2)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
