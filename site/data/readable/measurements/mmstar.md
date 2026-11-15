# MMStar
**Type:** Measurement instrument  
**Supporting papers:** 31  

## State of the Field

**What it is.** Across papers, MMStar is most commonly described as a benchmark for evaluating large vision-language models, often framed as a single-image or image question-answering benchmark for visual-language understanding. A recurring description presents it as an elite, vision-indispensable multimodal benchmark with 1,500 human-selected or curated samples, six core capabilities, and 18 detailed axes, with papers also noting minimal data leakage and that visual content is necessary for correct answers. Some authors instead emphasize different task scopes, describing it as assessing general understanding and reasoning across visual and textual tasks, while a smaller line of work describes it as an extensive static-content image VQA benchmark, a multimodal mathematical reasoning benchmark, or a benchmark built around high-quality multiple-choice questions.

**What it is claimed to measure.** Across relationships, papers use MMStar to measure 10 constructs and 1 behavioral indicator, so the reported targets are spread across many concepts rather than centered on one. The most frequent links treat it as measuring Logical reasoning and Reasoning; papers also use it for Fine-grained perception and General ability, and the one linked behavioral indicator is Visual question answering, with six other construct links also reported.

**Space of uses.** Most papers position MMStar as one benchmark within a larger evaluation suite, for example alongside MMBench, MathVista, MMVet, and MMMU. A smaller line of work uses it more centrally, calling it the primary benchmark or the primary evaluation metric for an analysis. In the recorded instrument links, MMStar is related to one other instrument, VLMEvalKit, which one paper describes as the evaluation framework employed for these benchmarks.

**Concerns raised.** Rather than direct criticism, papers mainly describe safeguards built into MMStar. They say it ensures vision indispensability, makes a concerted effort to minimize data leakage, excludes questions solvable by blind language models, requires visual content for correct answers, and uses high-quality multiple-choice questions to alleviate misjudgment issues.

## Sources

**MMStar** (14 papers: [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf), [Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf), [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf), [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf), [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf), [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e69ff56d0ebff0752ff29caaddc25dd-Paper-Datasets_and_Benchmarks_Track.pdf), [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf), [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf), [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf))
> A single-image benchmark used to evaluate visual-language understanding.

## Relationships

### → MMStar
- **Logical reasoning** (construct): *measured_by*, 2 papers
  > We further analyze the detailed scores on MM-Star (Chen et al., 2024a), including coarse perception (CP), fine-grained perception (FP), instance reasoning (IR), logical reasoning (LR)... (Table 4)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > MMStar and MMBench (Chen et al., 2024a; Liu et al., 2025) provide comprehensive evaluations by categorizing VLM tasks into two primary domains: perception and reasoning. (Section 5.1)
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Visual perception** (construct): *measured_by*, 1 paper
  > We further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49], GQA [28], Vizwiz [22], MMBench [48] and MMStar [8]... (Appendix D.1)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Fine-grained perception** (construct): *measured_by*, 1 paper
  > We further analyze the detailed scores on MM-Star (Chen et al., 2024a), including coarse perception (CP), fine-grained perception (FP), instance reasoning (IR), logical reasoning (LR)... (Table 4)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > The performance of LLaVA-Next-LLaMA3-8B model with merged task vectors across math-related Benchmarks: MathVista ..., MathVerse ..., MMStar ..., DynaMath ..., MathVision ... (Table 2)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > These benchmarks include visual question answering datasets GQA (Hudson and Manning, 2019), MME (Fu et al., 2024), MMBench (Liu et al., 2024), and MMStar (Chen et al., 2024b) (Table 5)
  - [VisiPruner: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs](https://aclanthology.org/2025.emnlp-main.955.pdf)
- **Visual grounding** (construct): *measured_by*, 1 paper
  > “MMStar [8] is a vision-indispensible benchmark, which requires better visual grounding in trained LVLMs.”
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual understanding** (construct): *measured_by*, 1 paper
  > To assess their visual understanding capability, numerous benchmarks have been developed, focusing on question-answering tasks, such as MMVet (Yu et al., 2023), MMStar (Chen et al., 2024a), and MMMU (Yue et al., 2024). (Section 1)
  - [Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > MMStar benchmarks 6 core capabilities and 18 detailed axes, aiming to evaluate LVLMs’ multi-modal capacities with carefully balanced and purified samples. (Abstract)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Multimodal reasoning** (construct): *measured_by*, 1 paper
  > To further investigate how well M-STAR generalizes to multiple benchmarks, we select four extra multi-modal ones focus on reasoning as well: M3CoT (Chen et al., 2024b), MMStar (Chen et al., 2024a), MMBench (Dev set, v1.1) (Liu et al., 2025), AI2D (Kembhavi et al., 2016). (Section 4.2)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > “We adopt MMStar (Chen et al., 2024c), an advanced benchmark of evaluation the comprehensive capabilities of LVLMs, as the primary evaluation metric.” (Section 4.1)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)

### Associated with
- **VLMEvalKit** (measurement instrument), 1 paper
  > "The evaluation framework employed for these benchmarks was VLMEvalKit (Duan et al., 2024)."
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
