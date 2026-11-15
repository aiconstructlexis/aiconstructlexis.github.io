# Linguistic quality
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Linguistic correctness, Linguistic coherence, Language quality, Grammaticality  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats linguistic quality as a property of generated text, usually described with overlapping terms such as logical, coherent, smooth, natural-sounding, clear, fluent, and free of grammatical errors. Many definitions narrow this further to linguistic correctness, grammaticality, or language quality, emphasizing adherence to grammatical, spelling, punctuation, and stylistic norms, sometimes defined by the absence of repetition or inconsistency. A smaller line of work shifts from output-level description to a latent property of the model or its representations, describing linguistic coherence as fluency, plausibility, and syntactic correctness, or describing linguistic quality through richness, coherence, and complexity in generated text.

**Space of facets.** Papers break the construct into recurring facets, most often clarity, fluency, naturalness, coherence, and grammatical correctness, with some adding spelling, punctuation, vocabulary richness, sentence structure, stylistic appropriateness, plausibility, or structural complexity. They also use partially overlapping labels, including linguistic quality, language quality, linguistic correctness, linguistic coherence, and grammaticality, so papers use the same name for both broad naturalness-and-coherence notions and narrower rule-based correctness notions. One paper contrasts grammaticality with faithfulness, while another contrasts linguistic coherence with factual accuracy, saying models can be optimized for fluency and syntactic correctness rather than truthfulness.

**Space of measurement.** Papers link linguistic quality to 5 measurement instruments and 2 behavioral indicators. The most common operationalizations are human evaluation and LLM-as-a-judge prompts that rate whether responses are logical, clear, fluent, smooth, natural, and free of grammatical, spelling, or punctuation errors; other linked measures are manual error analysis of inconsistencies and linguistic errors, PLLuM-Align's 5-point Likert ratings for linguistic correctness, and WikiText-2 log perplexity, described as measuring general language quality. These operationalizations mostly match the dominant fluency-and-correctness definitions, though some work also operationalizes the construct more indirectly, for example by using fluency as an estimate of post-edit linguistic quality or by inferring it from word-transition graph metrics such as graph energy, spectral entropy, and density.

**Links.** No causal or correlational claims are reported. Instead, papers describe related links from knowledge editing to linguistic quality, where it is analyzed alongside accuracy, locality, and generalization, and from hallucination detection to linguistic quality, where embeddings optimized for linguistic coherence rather than factual accuracy are said to fail to clearly separate truthful and hallucinated content. Papers do not link it to any other construct.

## Sources

**Linguistic quality** (5 papers: [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.481.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf), [A Graph-Theoretical Framework for Analyzing the Behavior of Causal Language Models](https://aclanthology.org/2025.emnlp-main.1014.pdf))
> The quality of a model's generated text in terms of being logical, coherent, smooth, and natural-sounding.

**Linguistic correctness** (1 paper: [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf))
> The latent proficiency of a model in producing grammatically correct, stylistically appropriate, and normatively fluent text in the target language.

**Linguistic coherence** (1 paper: [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf))
> The quality of generated text being fluent, plausible, and syntactically correct, for which LLMs are primarily optimized via next-token prediction.

**Language quality** (2 papers: [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf), [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> The linguistic correctness and fluency of a model's generated text, assessed by the absence of flaws like repetition or inconsistency.

**Grammaticality** (1 paper: [CLEME2.0: Towards Interpretable Evaluation by Disentangling Edits for Grammatical Error Correction](https://aclanthology.org/2025.acl-long.10.pdf))
> The degree to which a system's output text is grammatically correct and adheres to the rules of a language.

## Relationships

### Linguistic quality →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > Linguistic Quality: The response logical. The model correctly understands the medical task, and the expressions smooth and natural. (Section 4.2.4, The Prompt for GPT-4 to Rate the Performance of QA Tasks)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > Linguistic Quality: The response logical. The model correctly understands the medical task, and the expressionis smooth and natural. (Section 4.2.5, The Instruction of Human Evaluation)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.868.pdf)
- **Manual error analysis** (measurement instrument): *measured_by*, 1 paper
  > To investigate the impact of DPSGD and distillation on inconsistencies and linguistic quality, we manually annotated 50 outputs each from the XSum, MRPC, and Pubmed test sets. (Section 5.4)
  - [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf)
- **WikiText-2** (measurement instrument): *measured_by*, 1 paper
  > log perplexity, the average negative log-likelihood of generated tokens on the Wikitext-2 dataset (Merity et al., 2016); ... The latter two metrics measure general language quality (Section 3.1)
  - [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf)
- **PLLuM-Align** (measurement instrument): *measured_by*, 1 paper
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### Associated with
- **Knowledge editing** (behavioral indicator), 1 paper
  > “We analyze ICE across four critical aspects of knowledge editing: accuracy, locality, generalization, and linguistic quality, demonstrating its advantages.”
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Hallucination detection** (behavioral indicator), 1 paper
  > Recent approaches have leveraged the latent space of LLMs for hallucination detection, but their embeddings, optimized for linguistic coherence rather than factual accuracy, often fail to clearly separate truthful and hallucinated content. (Abstract)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
