# BLINK
**Type:** Measurement instrument  
**Supporting papers:** 12  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats BLINK as a multi-image benchmark for reasoning over multi-view and spatial relationships. Some papers describe it more broadly as a benchmark, or collection, of 14 visual perception tasks across indoor, outdoor, and natural scenes, noting that some tasks involve multiple images, such as visual similarity and multi-view reasoning, and that the suite also includes relative depth, spatial reasoning, and correspondence tasks. A smaller set of definitions frames it as testing whether multimodal large language models can perceive as well as see, and one paper specifically refers to its Jigsaw and Multi-view reasoning splits.

**What it is claimed to measure.** Papers link BLINK to 4 constructs and 1 behavioral indicator. Among the measured_by links, the prevailing claim is that it measures multi-image reasoning, with additional work using it to measure visual perception and, through a reported BLINK spatial reasoning task, spatial reasoning; a smaller line of work also cites it as measuring hallucination. Overall, the reported measurement claims spread across several targets rather than converging on a single construct.

**Space of uses.** Papers usually position BLINK as one item in a broader multi-image or perception-focused evaluation suite, often alongside MMMU, Mantis, and QBench or QBench2, with some papers also pairing it with MMDU and MVBench. Several descriptions place it among multi-image understanding benchmarks, and another paper groups it with perception-focused benchmarks. BLINK is also related to 1 other instrument, MM-NIAH, where images from BLINK's Jigsaw and Multi-view reasoning split are inserted into documents to serve as image needles.

**Concerns raised.** A recurring concern is scope for long-context evaluation: one paper relates BLINK to long-context understanding by arguing that multi-image comprehension benchmarks such as BLINK use short contexts and therefore fail to evaluate long-context document comprehension.

## Sources

**BLINK** (6 papers: [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf), [Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains](https://aclanthology.org/2025.acl-long.1347.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf), [ReMI: A Dataset for Reasoning with Multiple Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ea56c0baacac9f7764257a43a93c90a-Paper-Datasets_and_Benchmarks_Track.pdf), [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf))
> A multi-image benchmark used to evaluate reasoning over multi-view and spatial relationships.

## Relationships

### → BLINK
- **Multi-image reasoning** (construct): *measured_by*, 4 papers
  > “Table 4 presents the the evaluation results on multi-image understanding benchmarks. The evaluation benchmarks consist of ... BLINK ...”
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
  - [Design Choices for Extending the Context Length of Visual Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Visual perception** (construct): *measured_by*, 2 papers
  > The perception-focused benchmarks include RealWorldQA, CV-Bench and BLINK (Section 4)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Spatial reasoning** (construct): *measured_by*, 1 paper
  > GPT-4o with SKETCHPAD sets a new state of the art on all tasks, including... BLINK spatial reasoning (83.9%)
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Some efforts include POPE (Li et al., 2023g), LLaVA-RLHF (Sun et al., 2023), BLINK (Fu et al., 2024), and Rohrbach et al. (2018); Biten et al. (2022) are the few examples that consider multimodal hallucination. (Section 5.1)
  - [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > existing benchmarks for multi-image comprehensions, such as SEED-Bench-2 [25] and BLINK [26], consist of short contexts, which fail to evaluate the capability for long-context document comprehension. (Introduction)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MM-NIAH** (measurement instrument), 1 paper
  > for each evaluation data, images sampled from the Jigsaw and Multi-view reasoning split of BLINK benchmark [26] are inserted into the document to serve as the image needle. (Section 3.2)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
