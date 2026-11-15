# Scientific question answering
**Type:** Behavioral indicator  
**Supporting papers:** 23  
**Also known as:** Science question answering, STEM question answering, Scientific reasoning  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is producing the correct answer to science-domain questions, often in multiple-choice form and over a broad range of topics. Many definitions add reasoning over provided context or external knowledge, and several describe multimodal cases where diagrams, charts, or other visual content must be understood alongside text; one paper says the model must both understand multimodal content and extract external knowledge to arrive at the correct answer. A smaller line of work narrows the scope to school-curriculum, elementary, or simple versus complex science questions, while others use harder formulations such as graduate-level or expert-level questions requiring domain-specific knowledge and logical inference.

**Variants.** Papers most often call the behavior science question answering or scientific question answering. The studied settings include school-curriculum and subject-specific questions, climate science question answering, open-book science questions, and broader science-and-math or STEM formulations; some authors relabel harder versions as scientific reasoning. Several papers also place it inside multimodal reasoning, with visual and textual input, figure-based question answering, or questions about diagrams and data, and one paper studies a generation setting that synthesizes a summary response to a research question from relevant paper abstracts.

**Space of elicitation and scores.** It is measured by 6 instruments. The most frequently linked are ARC-Challenge, ARC-Easy, ScienceQA, ARC, and OpenBookQA, with 1 other instrument also linked. These instruments are mostly benchmark datasets of science questions, ranging from simple, complex, and open-book science questions to multiple-choice scientific question answering and challenging or multi-step scientific reasoning tasks.

**What it is taken as evidence of.** Papers do not explicitly frame it as evidence of a construct; instead, it is related to 4 constructs: Causal reasoning, Domain knowledge, Long-context understanding, and Numerical ability. These links all come from one paper's description of a ScienceQ&A generation task, which says the response must demonstrate those abilities. No other construct link is reported.

## Sources

**Science question answering** (5 papers: [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf), [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf), [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf), [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf), [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf))
> The task of answering multiple-choice questions about a wide range of scientific topics, often requiring reasoning over provided context or external knowledge.

**Scientific question answering** (5 papers: [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf), [ClimaQA: An Automated Evaluation Framework for Climate Question Answering Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3eff068e195daace49955348de9f8398-Paper-Conference.pdf), [SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bf/chen25bf.pdf), [LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts](https://aclanthology.org/2025.emnlp-main.368.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf))
> The task of answering questions related to scientific domains, often requiring understanding of diagrams, charts, or other visual aids in addition to text.

**STEM question answering** (1 paper: [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf))
> Answering questions related to science, technology, engineering, and mathematics.

**Scientific reasoning** (1 paper: [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf))
> Answering expert-level scientific questions requiring domain-specific knowledge and logical inference.

## Relationships

### Scientific question answering →
- **ARC-Challenge** (measurement instrument): *measured_by*, 3 papers
  > Comprehensive Examination: ... ARC-C (0-shot) (Clark et al., 2018), collected from standardized natural science tests (Section 5.1).
  - [Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > ARC Easy (Clark et al., 2018) Simple science questions. (Table 2)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 2 papers
  > ScienceQA with multiple choice are used to evaluate the zero-shot generalization on scientific question answering. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 1 paper
  > ARC (AI2 Reasoning Challenge, Clark et al., 2018) was designed to test the reasoning abilities of AI through a series of challenging science questions. (Section 1.1)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > OpenBookQA (Mihaylov et al., 2018) Open-book science questions. (Table 2)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
- **SciBench** (measurement instrument): *measured_by*, 1 paper
  > SciBench (Wang et al., 2024a) is a benchmark suite of scientific reasoning tasks, where the objective is to answer complex, multi-step scientific questions that require integrating knowledge, reasoning over evidence, and applying scientific principles. (Section 4.4. SciBench)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)

### Associated with
- **Domain knowledge** (construct), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
- **Numerical ability** (construct), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
- **Long-context understanding** (construct), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
- **Causal reasoning** (construct), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
