# World knowledge
**Type:** Construct  
**Supporting papers:** 88  
**Also known as:** General knowledge, Real-world knowledge grounding, Background knowledge, Basic knowledge, World understanding, Prior knowledge, General world knowledge, World knowledge priors, Open-world knowledge, Background Knowledge, External knowledge  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats world knowledge as a broad store of factual and conceptual information internalized from training or pretraining and encoded in a model's weights or parameters, available for recall and use across downstream tasks. Many definitions stress application as much as storage, describing a latent capacity to answer questions, reason about category names, provide supplementary evidence, or draw on facts not present in the immediate input, and one study describes LLMs as having 'a wealth of world knowledge.' A smaller line broadens the construct toward real-world properties and behaviors, multimodal grounding, or a coherent internal representation beyond surface patterns, while another narrows it to memorized priors about typical visual attributes.

**Space of facets.** Most papers use several near-synonyms for roughly the same idea, including general knowledge, general world knowledge, open-world knowledge, background knowledge, prior knowledge, and basic knowledge. A smaller line separates adjacent notions: some frameworks place it under broader background knowledge together with factuality and commonsense understanding, while vision-language papers use labels like external knowledge or real-world knowledge grounding when answers must go beyond the given image or text. Another distinction appears in work on world knowledge priors, which narrows the term to memorized attribute-object associations, and in world understanding, which contrasts deeper concept relations with surface linguistic performance.

**Space of measurement.** Operationally, papers link world knowledge to 22 measurement instruments and 2 behavioral indicators. The dominant instruments are benchmarks, most often MMLU, then TriviaQA, Natural Questions, ARC-Easy, and BIG-Bench Hard, typically scored with multiple-choice accuracy, exact match, or F1 in zero-shot or few-shot evaluations; 17 other instruments are also linked. These operationalizations mostly test recall, retrieval, and application of factual knowledge, while some definitions use broader language about multimodal grounding or deeper world understanding.

**Links.** Beyond measurement, papers link world knowledge to 7 constructs and 2 behavioral indicators. Several papers claim a causal relationship from world knowledge to calibration and generalization, and one paper claims a causal relationship from catastrophic forgetting to world knowledge; 3 other constructs and 1 other behavioral indicator are also linked by causal claims or relatedness statements. Related links also place factuality and commonsense reasoning alongside world knowledge under background knowledge.

## Sources

**World knowledge** (15 papers: [Democratizing Fine-grained Visual Recognition with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/49299a8afda8053932a4cfd62fdfd1b9-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf), [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf), [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.122.pdf), [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf), [Are explicit belief representations necessary? A comparison between Large Language Models and Bayesian probabilistic models](https://aclanthology.org/2025.naacl-long.572.pdf), [Probing LLM World Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.234.pdf))
> The body of general factual information about the world that a model has internalized from its training data.

**General knowledge** (2 papers: [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf), [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf))
> The broad base of factual and conceptual information acquired by a model during pre-training, which can be applied to downstream tasks.

**Real-world knowledge grounding** (1 paper: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf))
> The ability to connect multimodal inputs with factual, external knowledge about the world, enabling accurate and contextually relevant responses.

**Background knowledge** (1 paper: [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf))
> The latent store of general world knowledge and scientific intuition acquired during pre-training that the model can apply to new tasks.

**Prior knowledge** (1 paper: [Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf))
> The vast repository of general world knowledge, including facts about objects, their typical materials, and physical properties, that the model possesses from its training.

**Basic knowledge** (1 paper: [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.626.pdf))
> The parametric world knowledge learned during large-scale unsupervised pre-training, which is at risk of being forgotten during fine-tuning.

**World understanding** (1 paper: [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf))
> The degree to which a model possesses an internal, coherent representation of concepts and their relationships in the world, beyond surface-level linguistic patterns.

**General world knowledge** (1 paper: [SLlama: Parameter-Efficient Language Model Architecture for Enhanced Linguistic Competence Under Strict Data Constraints](https://aclanthology.org/2025.emnlp-main.1198.pdf))
> The model's stored knowledge about facts and concepts from the world that can be applied in evaluation tasks.

**World knowledge priors** (1 paper: [Pixels Versus Priors: Controlling Knowledge Priors in Vision-Language Models through Visual Counterfacts](https://aclanthology.org/2025.emnlp-main.1262.pdf))
> Memorized linguistic associations about typical visual attributes of objects that the model can retrieve from pretraining rather than from the current image.

**Open-world knowledge** (2 papers: [VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf), [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf))
> The latent repository of general knowledge about the world that a model can draw upon to perform tasks that require information not present in the immediate input.

**Background Knowledge** (1 paper: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf))
> The capacity to generate responses by accessing a broad repository of general and domain-specific factual and commonsense information.

**External knowledge** (1 paper: [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf))
> The ability to answer questions that require information not present in the provided image or text, relying on internalized world knowledge.

## Relationships

### World knowledge →
- **MMLU** (measurement instrument): *measured_by*, 17 papers
  > we compare performance on SAD to general knowledge and reasoning abilities as measured by the MMLU benchmark (Hendrycks et al., 2021b). (Section 1).
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [LLaMaFlex: Many-in-one LLMs via Generalized Pruning and Weight Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/685d249ad59836727be209032f082bd7-Paper-Conference.pdf)
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [Advancing Mathematical Reasoning in Language Models: The Impact of Problem-Solving Data, Data Synthesis Methods, and Training Stages](https://proceedings.iclr.cc/paper_files/paper/2025/file/aab3003c922e0fcd2fd2c951fa3c03ad-Paper-Conference.pdf)
  - [Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf)
  - [Towards Scalable Exact Machine Unlearning Using Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf)
  - [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [Organize the Web: Constructing Domains Enhances Pre-Training Data Curation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wettig25a/wettig25a.pdf)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 7 papers
  > For general knowledge on facts, we report the performance on Natural Questions (0-shot) [40] and TriviaQA (0-shot) [41].
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 5 papers
  > World Knowledge (5-shot): NaturalQuestions (NQ, Kwiatkowski et al. (2019))... (Section 4.2).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > World Knowledge (WK): Jeopardy-3-shots [3], ArcEasy-3-shots [13], ArcChallenge-3-shots [13], and WikiDataQA-3-shots [4]
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 2 papers
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 2 papers
  > The world knowledge is evaluated by the exact match scores (%) on TriviaQA [23], NQ open [29], and WebQS [4] (Section 4).
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 2 papers
  > MMLU and MMLU Pro measure the general knowledge of LLMs
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 2 papers
  > OKVQA (Marino et al., 2019) for external knowledge
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fbf5efe979e6754dc06a0869233f2510-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > World Knowledge (WK): Jeopardy-3-shots [3], ArcEasy-3-shots [13], ArcChallenge-3-shots [13], and WikiDataQA-3-shots [4]
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > Then, we evaluate each instruction-tuned model on a range of tasks to evaluate the model’s general/world knowledge (MMLU (Hendrycks et al., 2020), OpenBookQA (Mihaylov et al., 2018))
  - [Towards Scalable Exact Machine Unlearning Using Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > LLMs are pre-trained on massive datasets, allowing them to accumulate broad world knowledge that enhances their ability to generalize across a wide range of downstream tasks. (Section 2.2)
  - [FakeShield: Explainable Image Forgery Detection and Localization via Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d4e0ab9d8ff180bf5b95c258842d16e-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > World-knowledge tasks: TriviaQA (Joshi et al., 2017), Natural Questions (Kwiatkowski et al., 2019), HotpotQA (Yang et al., 2018), WebQuestions (Berant et al., 2013), ComplexWebQuestions (Talmor & Berant, 2018). (Section 5.1)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **CWQ** (measurement instrument): *measured_by*, 1 paper
  > World-knowledge tasks: TriviaQA (Joshi et al., 2017), Natural Questions (Kwiatkowski et al., 2019), HotpotQA (Yang et al., 2018), WebQuestions (Berant et al., 2013), ComplexWebQuestions (Talmor & Berant, 2018). (Section 5.1)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > We measure general knowledge using the CommonsenseQA (CSQA) (Talmor et al., 2019) dataset... (Section 4.1)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Semantic understanding** (construct): *causes*, 1 paper
  > As LLMs encompass general open-world knowledge, they can be utilized for the semantic understanding of nodes’ textual content. (Section 1)
  - [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf)
- **Calibration** (construct): *causes*, 1 paper
  > Our research reveals that LLMs’ prior knowledge causes potential poor calibration due to the ubiquitous presence of known data in real-world fine-tuning, which appears harmful for calibration. (Abstract)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
- **Overconfidence** (construct): *causes*, 1 paper
  > Specifically, data aligned with LLMs’ prior knowledge would induce overconfidence, while new knowledge improves calibration. (Abstract)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
- **Open LLM Leaderboard v2** (measurement instrument): *measured_by*, 1 paper
  > For instruction following and world knowledge, we utilize the recent HuggingFace OpenLLM Leaderboard 2 (Fourrier et al., 2024). (Section 3.1)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
- **VoiceBench** (measurement instrument): *measured_by*, 1 paper
  > VoxEval (Cui et al., 2025) and VoiceBench serve as spoken counterparts to MMLU (Hendrycks et al., 2021) and MMLU-Pro (Wang et al., 2024), testing models across diverse factual domains like social science and humanities.
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **VoxEval** (measurement instrument): *measured_by*, 1 paper
  > VoxEval (Cui et al., 2025) and VoiceBench serve as spoken counterparts to MMLU (Hendrycks et al., 2021) and MMLU-Pro (Wang et al., 2024), testing models across diverse factual domains like social science and humanities.
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **IFEval** (measurement instrument): *measured_by*, 1 paper
  > To validate the effectiveness and generalization capabilities of our approach, we assess model capabilities in general knowledge using IFEval (Zhou et al., 2023c) and MMLU (Hendrycks et al., 2021b) (Section 4.1)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > "general knowledge (TriviaQA [29] and SQuAD [62])"
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)

### → World knowledge
- **Catastrophic forgetting** (behavioral indicator): *causes*, 1 paper
  > the fine-tuned model suffers from catastrophic forgetting of the pre-trained world knowledge
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)

### Associated with
- **Factuality** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: ... Background Knowledge (Factuality, Commonsense Understanding)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Commonsense reasoning** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: ... Background Knowledge (Factuality, Commonsense Understanding)... (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > the QA ability to maintain pre-trained world knowledge (Section 1).
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **Honesty** (construct), 1 paper
  > Model A is more honest than model B IFF it exhibits statistically superior performance on measures of world knowledge (Section 5).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
