# Knowledge
**Type:** Construct  
**Supporting papers:** 27  
**Also known as:** Knowledge ability, Knowledge capacity  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats knowledge as a model-level latent ability to recall or retrieve factual information the model has acquired, often framed as world knowledge and as information not directly available in the input. Some authors broaden this to the model's ability to store and correctly apply factual, semantic, procedural, or conceptual information, and a smaller line defines knowledge capacity as retrieving and utilizing acquired knowledge to solve professional problems. The main difference is between a narrower recall-of-facts framing and a broader retrieve-and-apply framing, though both describe knowledge as an underlying ability of the model.

**Space of facets.** Papers use closely related labels such as knowledge, knowledge ability, and knowledge capacity for this family of abilities. One line of work splits evaluation into knowledge ability versus inference ability, while other work repeatedly pairs knowledge with reasoning, including benchmark setups that report separate knowledge and reasoning tasks. A separate relation connects knowledge to general ability through the claim that a single common factor can underlie reasoning-and-knowledge benchmark scores.

**Space of measurement.** Knowledge is measured by 7 instruments and linked to 2 behavioral indicators. The prevailing operationalization uses benchmarks, most commonly MMLU, with ARC-Challenge, ArabicMMLU, LLM-as-a-judge, and MM-Vet also used, plus 2 other instruments. These instruments operationalize knowledge as answering knowledge-intensive or subject-based questions, breadth of expert knowledge across disciplines, a knowledge component within multimodal evaluation, or the correctness of knowledge presented in answers; this mostly matches recall-oriented definitions, though some papers define knowledge more broadly and one paper says MCQA "doesn't fully test knowledge" and may be suboptimal for that goal.

**Links.** Across the papers, links are reported as related rather than causal or correlational. Knowledge is related to 2 behavioral indicators, natural language inference and synthetic data detection, and to 1 construct, general ability. The NLI link is described as tasks that require integrating knowledge and reasoning, synthetic data detection as testing perception, knowledge, and reasoning capabilities, and general ability as a single common factor underlying benchmark scores for reasoning and knowledge.

## Sources

**Knowledge** (4 papers: [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf), [Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](https://aclanthology.org/2025.acl-long.169.pdf), [Integral Transformer: Denoising Attention, Not Too Much Not Too Little](https://aclanthology.org/2025.emnlp-main.118.pdf))
> The latent ability to recall facts or information contained in the model that cannot be found directly in the input.

**Knowledge ability** (1 paper: [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> The extent to which a large language model has acquired and can recall factual information about the world.

**Knowledge capacity** (2 papers: [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf), [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf))
> The ability of a model to retrieve and utilize acquired knowledge to solve professional problems.

## Relationships

### Knowledge →
- **MMLU** (measurement instrument): *measured_by*, 10 papers
  > “the mostly knowledge-driven MMLU benchmark”
  - [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > The input for the task is knowledge-intensive questions from TriviaQA (Joshi et al., 2017). (p. 5)
  - [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > To rigorously assess and push the capabilities of these LLMs, we introduce MMLU-Pro, a new benchmark designed to test the upper limits of reasoning and knowledge in advanced language models. (Section 2.1).
  - [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ArabicMMLU** (measurement instrument): *measured_by*, 1 paper
  > Knowledge assessment: We choose ArabicMMLU [21], and EXAMS [22], which provide a comprehensive evaluation of knowledge across various subjects. (Section 3.1)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > For track 1, we adopt commonly used MMLU [16], Arc-eacy [3], and Arc-challenge [3] to evaluate the knowledge ability of LLMs.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > Table 5: Multimodal reasoning ability on MM-Vet [92]. Rec denotes Recognition; Know denotes knowledge; Gen denotes Language generation; and Spat denotes Spatial awareness.
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > “Knowledge Capability (KC), which leverages Qwen1.5-32B (Bai et al., 2023a) to evaluate the correctness of knowledge presented in answers.”
  - [SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf)

### Associated with
- **Natural language inference** (behavioral indicator), 1 paper
  > notably NLI tasks, which require integrating knowledge and reasoning. (Section 1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **General ability** (construct), 1 paper
  > Finally, the identification of a single common factor underlying all benchmark scores suggests that a general ability for reasoning and knowledge can be effectively measured through a consolidated, sparse benchmark. (Section 4)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Synthetic data detection** (behavioral indicator), 1 paper
  > the task of distinguishing between real and synthetic data effectively tests the perception, knowledge, and reasoning capabilities of LMMs. (ABSTRACT)
  - [LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf)
