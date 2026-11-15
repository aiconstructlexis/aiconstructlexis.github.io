# LLaVA-Bench-in-the-Wild
**Type:** Measurement instrument  
**Supporting papers:** 45  
**Also known as:** llava-bench-in-the-wild, LLaVA Bench, LLaVA-in-the-wild, LLaVA-wild, LLaVA-Wild, LLaVABench, LLaVA-Bench Wild, LLaVA-Bench, LLaVA-Bench (In-the-Wild)  

## State of the Field

**What it is.** Across the surveyed work, the prevailing description is of an evaluation benchmark for open-ended multimodal dialogue, image understanding, and visual question answering in unconstrained, real-world settings. Many papers describe it as 24 images with 60 challenging questions spanning conversation, detailed description, and complex reasoning, sometimes framed as multimodal instruction following or visual conversation and often scored with GPT-4, GPT-4V, GPT-4o, or another stronger model as evaluator. A smaller line of work presents it as a case-study set for open-ended responses, distinguishes COCO and Wild variants, or uses it for long-generation settings with single-image contexts and a few hundred tokens.

**What it is claimed to measure.** Papers use it to measure 6 constructs and 9 behavioral indicators, so the reported measurement claims are spread across several targets rather than centered on one. At the construct level, the most common claims are that it measures visual understanding and helpfulness; at the behavioral-indicator level, the recurring uses are for complex reasoning question answering, visual question answering, and detailed image description. Other papers also report it as measuring several additional constructs and behavioral indicators.

**Space of uses.** No other measurement instrument is linked to it. In practice, papers usually report it as part of a broader benchmark suite, most often alongside MMBench, MM-Vet, MME, MMMU, and SEED-Bench. They variously position it as a general benchmark for systematic comprehension, image-level understanding, or overall multimodal capability evaluation, while some papers use it more narrowly as a case study or auxiliary long-generation check.

## Sources

**LLaVA-Bench-in-the-Wild** (3 papers: [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf), [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf), [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf))
> An evaluation benchmark for open-ended multimodal dialogue and image understanding in unconstrained settings.

**llava-bench-in-the-wild** (1 paper: [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf))
> Benchmark for evaluating multimodal language models on image-based tasks and questions.

**LLaVA-Bench** (9 papers: [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf), [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf), [Modality-Aware Neuron Pruning for Unlearning in Multimodal Large Language Models](https://aclanthology.org/2025.acl-long.295.pdf), [Looking Beyond Text: Reducing Language Bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://aclanthology.org/2025.emnlp-main.995.pdf), [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf), [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf), [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf))
> LLaVA-Bench is a benchmark containing challenging multimodal images and questions used to evaluate LVLM responses, including GPT-4V-aided assessment.

**LLaVA Bench** (1 paper: [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf))
> A conversational VQA benchmark containing questions about conversations, detailed descriptions, and complex reasoning.

**LLaVA-wild** (4 papers: [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf), [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf), [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf), [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf))
> An image understanding benchmark for evaluating performance on in-the-wild visual questions.

**LLaVA-Wild** (1 paper: [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf))
> A dataset used for general capability evaluation of multimodal models, often scored using a stronger model as an evaluator.

**LLaVA-in-the-wild** (1 paper: [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf))
> A benchmark evaluating visual conversation abilities and leveraging GPT-4o for response evaluation.

**LLaVABench** (3 papers: [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf), [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf), [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf))
> An evaluation benchmark used to assess Large Vision-Language Models on visual question answering tasks.

**LLaVA-Bench Wild** (1 paper: [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf))
> A benchmark dataset used to introduce visual distribution shifts by varying visual input semantics for evaluating multimodal large language models.

**LLaVA-Bench (In-the-Wild)** (5 papers: [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf), [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf), [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf))
> LLaVA-Bench (In-the-Wild) is an evaluation benchmark consisting of challenging, open-ended visual questions captured 'in the wild' to test real-world performance.

## Relationships

### → LLaVA-Bench-in-the-Wild
- **Complex reasoning question answering** (behavioral indicator): *measured_by*, 3 papers
  > LLaVA-Bench serves as a general benchmark for systematic comprehension, encompassing three categories: conversation, detailed description, and complex questions. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 3 papers
  > In this section, we present the experiment results of STIC across seven visual question answering (VQA) benchmarks. We consider the widely used benchmarks for LVLM evaluation across different domains including: ScienceQA... TextVQA... ChartQA... LLaVA-Bench
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)
- **Visual understanding** (construct): *measured_by*, 3 papers
  > LLaVA-Bench consists of 60 carefully designed open-ended questions across 24 images, evaluating models’ visual reasoning and understanding capabilities. (Sec. 6.1)
  - [Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention](https://aclanthology.org/2025.acl-long.634.pdf)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **Detailed image description** (behavioral indicator): *measured_by*, 2 papers
  > LLaVA-Bench, a generalized dataset, comprising 24 diverse images and 60 questions across categories like simple QA, detailed descriptions, and complex reasoning, is used to further evaluate the model’s generalization and robustness. (Section 4.1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Helpfulness** (construct): *measured_by*, 2 papers
  > we also leverage MMMU (Yue et al., 2024) and LLaVA-Bench (Liu et al., 2024b) to assess the model’s reasoning ability and helpfulness level. (Section 3.3.1)
  - [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **Visual instruction following** (behavioral indicator): *measured_by*, 2 papers
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator): *measured_by*, 1 paper
  > LLaVA-Bench serves as a general benchmark for systematic comprehension, encompassing three categories: conversation, detailed description, and complex questions. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the extent of catastrophic forgetting in Yo’LLaVA, we assessed both the Original LLaVA-1.5-13B [10] and Yo’LLaVA using common benchmarks for multimodal models: POPE [41], MMBench [42], and LLaVA-Wild [2]. (Appendix B)
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator): *measured_by*, 1 paper
  > LLaVA-Bench (Liu et al., 2023b) consists of 24 images and 60 questions to assess LVLMs' performance on complex tasks and domain adaptation. Following Leng et al. (2024), we use GPT-4 to assess the accuracy and detailedness of LVLM's image captioning
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > To assess robustness, we tested on the generalized dataset LLaVA-Bench. (Section 4)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > LLaVA-Bench, a generalized dataset, ... is used to further evaluate the model’s generalization and robustness. (Section 4.1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Open-ended question answering** (behavioral indicator): *measured_by*, 1 paper
  > we mainly used LLaVA v1.5 (Liu et al., 2024a) and LLaVA NeXT (Liu et al., 2024b) in 7B and 13B sizes and evaluated them on the LLaVA-Bench COCO and LLaVA-Bench Wild (Liu et al., 2023) datasets to assess open-ended generation quality.
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)
- **Knowledge grounding** (construct): *measured_by*, 1 paper
  > Furthermore, LLaVABench emphasizes not only multimodal alignment but also the model’s ability to perform knowledge grounding in complex real-world scenarios. (Section 4.2)
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)
- **Long-form text generation** (behavioral indicator): *measured_by*, 1 paper
  > Long Generation: Evaluates extended inference using LLaVABench (Liu et al., 2024b) and MMDU (Liu et al., 2024e). (Section 4.3).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Multimodal understanding** (construct): *measured_by*, 1 paper
  > LLaVA Bench (Li et al., 2024) assesses multimodal understanding and reasoning capabilities, with overall accuracy reported across all tasks (Section 4.1).
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
