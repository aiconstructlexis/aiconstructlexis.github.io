# Hallucination detection
**Type:** Behavioral indicator  
**Supporting papers:** 33  
**Also known as:** Hallucination Detection, Knowledge conflict detection, Medical hallucination detection, Sentence-level verification  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a judgment task over model outputs: deciding whether an answer, statement, response, or generated content is hallucinated, meaning factually incorrect, fabricated, unsupported, or not grounded in the available context. Most descriptions treat success as labeling content as hallucinated versus non-hallucinated, though some narrow it to tagging object phrases in a description that do not correspond to an image, or marking explanation sentences with a deletion tag when they show knowledge conflict. A smaller formulation treats success as refusing to answer when the needed information is absent, sometimes with the explicit response that the item is not mentioned in the provided context.

**Variants.** Papers use the label for several variants. A recurring line studies multimodal and visual settings, including concrete inconsistencies in rendered 2D images, responses or captions that are inaccurate relative to an image, and discourse-level hallucination detection over entities or relations in captions. Other variants focus on medical question answering, unsupported claims in data-analysis insights, token-level hallucination degree, and sentence-level verification during generation, and one study describes the task as "identifying a wrong response that coincidentally reaches the correct answer as being wrong."

**Space of elicitation and scores.** Papers measure this behavior with 10 instruments. The most frequently linked are HaluEval, SelfCheckGPT, GAVIE, HallusionBench, and MMHal-Bench, plus 5 other instruments. Most are benchmark or dataset style evaluations, while SelfCheckGPT is described as sampling additional responses from the model and using inconsistency with the target statement for hallucination detection.

**What it is taken as evidence of.** Papers link it to 3 constructs through both causal and related claims, rather than a single common relation. One paper claims a causal relationship from In-context learning to hallucination detection, stating that it can enhance performance for certain models, datasets, and tasks. Other papers report that hallucination detection is related to Semantic uncertainty and to Linguistic quality, with semantic uncertainty described as predictive uncertainty used for hallucination detection and linguistic quality appearing in a contrast between embeddings optimized for linguistic coherence and the separation of truthful from hallucinated content.

## Sources

**Hallucination Detection** (9 papers: [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf), [BIG5-CHAT: Shaping LLM Personalities Through Training on Human-Grounded Data](https://aclanthology.org/2025.acl-long.999.pdf), [GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents](https://aclanthology.org/2025.acl-long.557.pdf), [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://aclanthology.org/2025.acl-long.1041.pdf), [Prompt-Guided Internal States for Hallucination Detection of Large Language Models](https://aclanthology.org/2025.acl-long.1058.pdf), [Diffusion Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25g/jin25g.pdf), [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf), [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf), [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf))
> The observable task of identifying and tagging object phrases in a description that do not correspond to objects in the image.

**Hallucination detection** (6 papers: [Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d75660d6eb0ce31360c768fef85301dd-Paper-Conference.pdf), [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf), [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf), [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf), [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://aclanthology.org/2025.naacl-long.488.pdf), [Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.121.pdf))
> The task of using a large multi-modal model to identify and describe concrete hallucinations or inconsistencies within a rendered 2D image.

**Knowledge conflict detection** (1 paper: [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf))
> Identifying explanation sentences that contradict or are unsupported by comparison triples from the reasoning graph.

**Medical hallucination detection** (1 paper: [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143.pdf))
> The observable task of judging whether a given answer to a medical question is hallucinated (factually incorrect) or not, based on factual accuracy.

**Sentence-level verification** (1 paper: [Efficient Real-time Refinement of Language Model Text Generation](https://aclanthology.org/2025.emnlp-main.1753.pdf))
> The observable process of checking the factual correctness of individual sentences as they are generated during text production.

## Relationships

### Hallucination detection →
- **HaluEval** (measurement instrument): *measured_by*, 3 papers
  > Detecting and flagging hallucinations (HaluEval dataset (Li et al., 2023)). (Section 1)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
  - [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf)
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
- **SelfCheckGPT** (measurement instrument): *measured_by*, 2 papers
  > We compare the proposed AGSER approach with SBERT (Reimers and Gurevych, 2019), SelfCheckGPT (Manakul et al., 2023), INSIDE (Chen et al., 2024) and InterrogateLLM (Yehuda et al., 2024) in zero-shot hallucination detection.
  - [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf)
  - [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > On the challenging TruthfulQA benchmark (Lin et al., 2022a), our approach achieves a significant +12.8% improvement in hallucination detection accuracy (AUROC) compared to state-of-the-art methods. (Section 1. Introduction)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **HallusionBench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the visual perception capabilities of RePer, we conducted assessments across five widely-used benchmarks, covering a range of tasks: ... hallucination detection (HallusionBench (Guan et al., 2024), MMHal-Bench (Sun et al., 2023b), GAVIE (Liu et al., 2023a)) (Section 4.2)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the visual perception capabilities of RePer, we conducted assessments across five widely-used benchmarks, covering a range of tasks: ... hallucination detection (HallusionBench (Guan et al., 2024), MMHal-Bench (Sun et al., 2023b), GAVIE (Liu et al., 2023a)) (Section 4.2)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
- **GAVIE** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the visual perception capabilities of RePer, we conducted assessments across five widely-used benchmarks, covering a range of tasks: ... hallucination detection (HallusionBench (Guan et al., 2024), MMHal-Bench (Sun et al., 2023b), GAVIE (Liu et al., 2023a)) (Section 4.2)
  - [Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf)
- **MedHallu** (measurement instrument): *measured_by*, 1 paper
  > To address this, we introduce MedHallu, one of the first benchmark specifically designed for medical hallucination detection.
  - [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143.pdf)
- **NegHalu** (measurement instrument): *measured_by*, 1 paper
  > we conduct this analysis by reconstructing existing hallucination detection benchmarks with negated expressions and introducing NegHalu, a dataset in which hallucination labels are newly assigned to account for the effects of negation.
  - [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > POPE (Li et al., 2023): hallucination detection. (Section 4.3)
  - [VERITAS: Leveraging Vision Priors and Expert Fusion to Improve Multimodal Data](https://aclanthology.org/2025.emnlp-main.1002.pdf)
- **RAGTruth** (measurement instrument): *measured_by*, 1 paper
  > For our evaluations in the setting of hallucination detection with external references assumed available, we primarily consider the RAGTruth dataset [Wu et al., 2023]. (Section 5)
  - [LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf)

### → Hallucination detection
- **In-context learning** (construct): *causes*, 1 paper
  > These results imply that In-Context Learning can immediately enhance hallucination detection performance for certain models, datasets, and tasks, particularly when balanced examples with pre-/post-negated text and hallucination/no-hallucination cases are included.
  - [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf)

### Associated with
- **Semantic uncertainty** (construct), 1 paper
  > SEMANTIC UNCERTAINTY (Kuhn et al., 2023; Farquhar et al., 2024), which estimate the model’s predictive uncertainty on the generation for hallucination detection.
  - [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf)
- **Linguistic quality** (construct), 1 paper
  > Recent approaches have leveraged the latent space of LLMs for hallucination detection, but their embeddings, optimized for linguistic coherence rather than factual accuracy, often fail to clearly separate truthful and hallucinated content. (Abstract)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **Refusal** (behavioral indicator), 1 paper
  > The hallucination detection task aims to test the model’s ability to decline answering questions that are not mentioned in the given context.
  - [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf)
