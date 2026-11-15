# A-OKVQA
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** AOKVQA  

## State of the Field

**What it is.** Across papers, A-OKVQA is most commonly described as a visual question answering dataset or benchmark of image-question pairs whose answers require knowledge beyond direct visual evidence, usually framed as external real-world, commonsense, or world knowledge about objects or actions in the image. Some definitions add that it supports open-ended and multiple-choice settings, and one paper describes MSCOCO images with one correct answer and three distractors written by English speakers on Mechanical Turk. A smaller line of work presents it more broadly as a general-purpose VQA benchmark for larger visual concepts.

**What it is claimed to measure.** Papers link A-OKVQA to 6 constructs and 2 behavioral indicators. The most recurrent measurement claim is that it measures commonsense knowledge, and papers also report it as measuring cultural bias, fairness, generalization, multilingual ability, and robustness; among behavioral indicators, it is used to measure visual question answering and object hallucination. Overall, the measurement claims are spread across several targets rather than concentrated on one alone, although knowledge and world-knowledge reasoning is the prevailing framing.

**Space of uses.** Papers commonly place A-OKVQA alongside other VQA benchmarks, especially GQA, OK-VQA, and VQAv2, and sometimes with InfoSeek and CVQA. It is usually positioned as one benchmark within a broader evaluation suite for complex or knowledge-based VQA, and some papers use it for cross-dataset or unseen-category generalization checks. Other papers adapt it by translating questions and answers, or by introducing typos, when evaluating multilingual ability, fairness, and robustness.

**Concerns raised.** The clearest concern raised in the papers is cultural bias. One study uses A-OKVQA to measure Western bias and notes that it contains MSCOCO images queried for Western concepts from ImageNet, with questions and four candidate answers written by English speakers on Mechanical Turk.

## Sources

**A-OKVQA** (10 papers: [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [Rephrase, Augment, Reason: Visual Grounding of Questions for Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/eef6cb60fd59b32d35718e176b4b08d6-Paper-Conference.pdf), [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bc/li25bc.pdf), [CoMMIT: Coordinated Multimodal Instruction Tuning](https://aclanthology.org/2025.emnlp-main.582.pdf), [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.305.pdf), [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf), [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf))
> A visual question answering dataset where questions require external, real-world knowledge about objects or actions depicted in the image.

**AOKVQA** (2 papers: [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf))
> A general-purpose visual question answering benchmark used to evaluate performance on larger visual concepts.

## Relationships

### → A-OKVQA
- **Visual question answering** (behavioral indicator): *measured_by*, 2 papers
  > Focusing on three visual question answering tasks, we show that REPARE can result in a 3.85% (absolute) increase in zero-shot accuracy on VQAv2, 6.41%, and 7.94% points increase on A-OKVQA, and VizWiz respectively. (Sec. 1)
  - [Rephrase, Augment, Reason: Visual Grounding of Questions for Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/eef6cb60fd59b32d35718e176b4b08d6-Paper-Conference.pdf)
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **Commonsense knowledge** (construct): *measured_by*, 2 papers
  > InfoSeek and A-OKVQA Rely on Commonsense Knowledge (RCK) (Table 2).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > The reason behind selecting GQA, InfoSeek, and A-OKVQA is to evaluate the generalization capability of our framework across datasets that do not necessitate up-to-date knowledge (Section 5.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Fairness** (construct): *measured_by*, 1 paper
  > In VHELM, this is assessed by asking questions drawn from A-OKVQA [34] and VQAv2 [12] in African-American English (AAE)... (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multilingual ability** (construct): *measured_by*, 1 paper
  > We augment A-OKVQA [34] by translating the questions and answers from English to either Chinese, Hindi, Spanish, or Swahili to test whether the VLMs are invariant to VQA in different languages. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > We introduce typos into A-OKVQA [34] and VQAv2 [12] to test the robustness against text perturbations. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Object hallucination** (behavioral indicator): *measured_by*, 1 paper
  > we... examined object hallucination using the SEEM-annotated MSCOCO and A-OKVQA datasets from POPE. (Section 4)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Cultural bias** (construct): *measured_by*, 1 paper
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
